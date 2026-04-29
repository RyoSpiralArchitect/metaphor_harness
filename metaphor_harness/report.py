from __future__ import annotations

import csv
import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from typing import Any

from .db import HarnessDB
from .eval_rules import (
    apply_computed_pass_labels,
    bool_or_none,
    compute_pass_leakage,
    compute_pass_stance_pattern,
    compute_pass_relation,
    majority_bool,
    mean_number,
)


BOOL_LABELS_STANCE_PRIMITIVE = [
    "target_preserved",
    "stance_pattern_match",
    "stance_slip",
    "literal_vehicle_asserted",
    "unsupported_new_claim",
    "target_drift",
]
BOOL_LABELS_RELATION_PRIMITIVE = [
    "relation_mapping_pass",
    "surface_only_mapping",
    "domain_distance_respected",
]


def _parse_json(text: str) -> dict[str, Any]:
    try:
        obj = json.loads(text)
        return obj if isinstance(obj, dict) else {"parse_error": True}
    except Exception:
        return {"parse_error": True}


def _rate(rows: list[dict[str, Any]], key: str, positive: bool = True) -> float | None:
    vals = [bool_or_none(r.get(key)) for r in rows if bool_or_none(r.get(key)) is not None]
    if not vals:
        return None
    return sum(1 for v in vals if v is positive) / len(vals)


def _undecided_rate(rows: list[dict[str, Any]], key: str) -> float | None:
    if not rows:
        return None
    return sum(1 for r in rows if bool_or_none(r.get(key)) is None) / len(rows)


def _fmt_pct(x: float | None) -> str:
    return "NA" if x is None else f"{100 * x:.1f}%"


def _fmt_num(x: float | None) -> str:
    return "NA" if x is None else f"{x:.2f}"


def cohens_kappa(a: dict[str, bool], b: dict[str, bool]) -> float | None:
    keys = sorted(set(a) & set(b))
    if len(keys) < 2:
        return None
    n = len(keys)
    agree = sum(1 for k in keys if a[k] == b[k]) / n
    p_yes_a = sum(1 for k in keys if a[k]) / n
    p_yes_b = sum(1 for k in keys if b[k]) / n
    p_no_a = 1 - p_yes_a
    p_no_b = 1 - p_yes_b
    expected = p_yes_a * p_yes_b + p_no_a * p_no_b
    if expected == 1:
        return 1.0 if agree == 1 else None
    return (agree - expected) / (1 - expected)


def build_run_level_rows(db: HarnessDB) -> list[dict[str, Any]]:
    generations = {r["run_id"]: dict(r) for r in db.fetch_generations()}
    audits_by_run_type: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for audit in db.fetch_audits():
        parsed = _parse_json(audit["parsed_json"])
        parsed = apply_computed_pass_labels(parsed, audit["audit_type"])
        row = dict(audit)
        row["parsed"] = parsed
        audits_by_run_type[(audit["run_id"], audit["audit_type"])].append(row)

    rows: list[dict[str, Any]] = []
    for run_id, gen in generations.items():
        out = dict(gen)
        stance_audits = audits_by_run_type.get((run_id, "stance_leakage"), [])
        r_audits = audits_by_run_type.get((run_id, "relation"), [])

        for label in BOOL_LABELS_STANCE_PRIMITIVE:
            out[label] = majority_bool(a["parsed"].get(label) for a in stance_audits)
        out["false_entailment_risk_mean"] = mean_number(a["parsed"].get("false_entailment_risk") for a in stance_audits)
        out["ambiguity_risk_mean"] = mean_number(a["parsed"].get("ambiguity_risk") for a in stance_audits)
        # pass_* values are deterministic code-side recomputations applied per audit, then majority-voted.
        out["pass_stance_pattern"] = majority_bool(a["parsed"].get("pass_stance_pattern") for a in stance_audits)
        out["pass_leakage"] = majority_bool(a["parsed"].get("pass_leakage") for a in stance_audits)
        if out["pass_stance_pattern"] is None:
            out["pass_stance_pattern"] = compute_pass_stance_pattern(out)
        if out["pass_leakage"] is None:
            out["pass_leakage"] = compute_pass_leakage(out)

        for label in BOOL_LABELS_RELATION_PRIMITIVE:
            out[label] = majority_bool(a["parsed"].get(label) for a in r_audits)
        out["relation_score_mean"] = mean_number(a["parsed"].get("relation_score") for a in r_audits)
        out["pass_relation"] = majority_bool(a["parsed"].get("pass_relation") for a in r_audits)
        if out["pass_relation"] is None:
            out["pass_relation"] = compute_pass_relation(out)

        out["stance_parse_error_rate"] = _rate([
            {"parse_error": bool(a["parsed"].get("parse_error"))} for a in stance_audits
        ], "parse_error")
        out["relation_parse_error_rate"] = _rate([
            {"parse_error": bool(a["parsed"].get("parse_error"))} for a in r_audits
        ], "parse_error")
        rows.append(out)
    return rows


def summarize(rows: list[dict[str, Any]], group_keys: list[str]) -> list[dict[str, Any]]:
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[tuple(row.get(k) for k in group_keys)].append(row)

    summary: list[dict[str, Any]] = []
    for key, items in sorted(groups.items(), key=lambda x: tuple(str(v) for v in x[0])):
        s = {k: v for k, v in zip(group_keys, key)}
        s.update({
            "n": len(items),
            "stance_pattern_match_rate": _rate(items, "stance_pattern_match", True),
            "stance_pattern_undecided_rate": _undecided_rate(items, "stance_pattern_match"),
            "stance_slip_rate": _rate(items, "stance_slip", True),
            "vehicle_leakage_rate": _rate(items, "literal_vehicle_asserted", True),
            "target_drift_rate": _rate(items, "target_drift", True),
            "unsupported_claim_rate": _rate(items, "unsupported_new_claim", True),
            "pass_leakage_rate": _rate(items, "pass_leakage", True),
            "pass_stance_pattern_rate": _rate(items, "pass_stance_pattern", True),
            "relation_pass_rate": _rate(items, "pass_relation", True),
            "relation_undecided_rate": _undecided_rate(items, "pass_relation"),
            "surface_only_rate": _rate(items, "surface_only_mapping", True),
            "false_entailment_risk_mean": mean_number(r.get("false_entailment_risk_mean") for r in items),
            "relation_score_mean": mean_number(r.get("relation_score_mean") for r in items),
        })
        summary.append(s)
    return summary


def _index_summary(rows: list[dict[str, Any]], keys: list[str]) -> dict[tuple[Any, ...], dict[str, Any]]:
    return {tuple(row.get(k) for k in keys): row for row in rows}


def build_mapping_visibility_delta(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    keys = ["stance_pattern", "domain_distance", "control_arm", "provider", "model"]
    summary = summarize([r for r in rows if r.get("mapping_visibility") in {"hidden", "scaffolded"}], keys + ["mapping_visibility"])
    idx = _index_summary(summary, keys + ["mapping_visibility"])
    base_keys = sorted({tuple(row.get(k) for k in keys) for row in summary}, key=lambda t: tuple(str(x) for x in t))
    metrics = ["relation_pass_rate", "surface_only_rate", "pass_leakage_rate", "stance_slip_rate", "relation_score_mean"]
    out: list[dict[str, Any]] = []
    for bk in base_keys:
        hidden = idx.get(bk + ("hidden",))
        scaffolded = idx.get(bk + ("scaffolded",))
        if not hidden or not scaffolded:
            continue
        row = {k: v for k, v in zip(keys, bk)}
        row["n_hidden"] = hidden.get("n")
        row["n_scaffolded"] = scaffolded.get("n")
        for m in metrics:
            hv = hidden.get(m)
            sv = scaffolded.get(m)
            row[f"{m}_hidden"] = hv
            row[f"{m}_scaffolded"] = sv
            row[f"delta_{m}_scaffolded_minus_hidden"] = None if hv is None or sv is None else sv - hv
        out.append(row)
    return out


def build_control_delta(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    keys = ["stance_pattern", "domain_distance", "mapping_visibility", "provider", "model"]
    summary = summarize([
        r for r in rows if r.get("control_arm") in {"metaphor_with_forbidden", "metaphor_without_forbidden"}
    ], keys + ["control_arm"])
    idx = _index_summary(summary, keys + ["control_arm"])
    base_keys = sorted({tuple(row.get(k) for k in keys) for row in summary}, key=lambda t: tuple(str(x) for x in t))
    metrics = ["pass_leakage_rate", "vehicle_leakage_rate", "target_drift_rate", "stance_slip_rate"]
    out: list[dict[str, Any]] = []
    for bk in base_keys:
        with_forbidden = idx.get(bk + ("metaphor_with_forbidden",))
        without_forbidden = idx.get(bk + ("metaphor_without_forbidden",))
        if not with_forbidden or not without_forbidden:
            continue
        row = {k: v for k, v in zip(keys, bk)}
        row["n_with_forbidden"] = with_forbidden.get("n")
        row["n_without_forbidden"] = without_forbidden.get("n")
        for m in metrics:
            wv = with_forbidden.get(m)
            nov = without_forbidden.get(m)
            row[f"{m}_with_forbidden"] = wv
            row[f"{m}_without_forbidden"] = nov
            row[f"delta_{m}_without_minus_with"] = None if wv is None or nov is None else nov - wv
        out.append(row)
    return out


def build_judge_agreement(db: HarnessDB) -> list[dict[str, Any]]:
    label_sets = {
        "stance_leakage": ["pass_leakage", "pass_stance_pattern", "stance_pattern_match", "literal_vehicle_asserted", "stance_slip"],
        "relation": ["pass_relation", "surface_only_mapping"],
    }
    labels: dict[tuple[str, str, str], dict[str, bool]] = defaultdict(dict)
    for audit in db.fetch_audits():
        parsed = _parse_json(audit["parsed_json"])
        parsed = apply_computed_pass_labels(parsed, audit["audit_type"])
        audit_type = audit["audit_type"]
        judge_key = f"{audit['judge_provider']}::{audit['judge_model']}::{audit['judge_index']}"
        for label in label_sets.get(audit_type, []):
            val = bool_or_none(parsed.get(label))
            if val is not None:
                labels[(audit_type, label, judge_key)][audit["run_id"]] = val

    rows = []
    for audit_type in label_sets:
        for label in label_sets[audit_type]:
            judge_keys = sorted(k[2] for k in labels if k[0] == audit_type and k[1] == label)
            for ja, jb in combinations(judge_keys, 2):
                a = labels.get((audit_type, label, ja), {})
                b = labels.get((audit_type, label, jb), {})
                common = len(set(a) & set(b))
                kappa = cohens_kappa(a, b)
                rows.append({
                    "audit_type": audit_type,
                    "label": label,
                    "judge_a": ja,
                    "judge_b": jb,
                    "n_common": common,
                    "cohens_kappa": kappa,
                })
    return rows


def build_quality_scores(db: HarnessDB) -> list[dict[str, Any]]:
    points: dict[str, float] = defaultdict(float)
    comps: dict[str, int] = defaultdict(int)
    for pair in db.fetch_quality_pairs():
        parsed = _parse_json(pair["parsed_json"])
        winner = str(parsed.get("winner", "")).upper()
        a = pair["text_a_run_id"]
        b = pair["text_b_run_id"]
        if winner == "A":
            points[a] += 1
            comps[a] += 1
            comps[b] += 1
        elif winner == "B":
            points[b] += 1
            comps[a] += 1
            comps[b] += 1
        elif winner == "TIE":
            points[a] += 0.5
            points[b] += 0.5
            comps[a] += 1
            comps[b] += 1
    gens = {r["run_id"]: dict(r) for r in db.fetch_generations()}
    run_rows = {r["run_id"]: r for r in build_run_level_rows(db)}
    rows = []
    for run_id, n in comps.items():
        gen = gens.get(run_id, {})
        rr = run_rows.get(run_id, {})
        eligible = (
            bool_or_none(rr.get("pass_stance_pattern")) is True
            and bool_or_none(rr.get("pass_leakage")) is True
            and bool_or_none(rr.get("pass_relation")) is True
        )
        rows.append({
            "run_id": run_id,
            "case_id": gen.get("case_id"),
            "case_hash": gen.get("case_hash"),
            "provider": gen.get("provider"),
            "model": gen.get("model"),
            "control_arm": gen.get("control_arm"),
            "mapping_visibility": gen.get("mapping_visibility"),
            "temperature": gen.get("temperature"),
            "comparisons": n,
            "quality_win_rate": points[run_id] / n if n else None,
            "eligible_quality": eligible,
            "generated_text": gen.get("generated_text", ""),
        })
    return sorted(rows, key=lambda r: (-(r["quality_win_rate"] or 0), r.get("case_id") or ""))


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    keys: list[str] = []
    for row in rows:
        for key in row.keys():
            if key not in keys:
                keys.append(key)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _markdown_table(rows: list[dict[str, Any]], columns: list[str], max_rows: int = 50) -> str:
    if not rows:
        return "_No rows._\n"
    lines = []
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join(["---"] * len(columns)) + " |")
    for row in rows[:max_rows]:
        vals = []
        for col in columns:
            val = row.get(col)
            if isinstance(val, float):
                if "rate" in col or col.endswith("_rate") or col.startswith("delta_") and "rate" in col:
                    vals.append(_fmt_pct(val))
                else:
                    vals.append(_fmt_num(val))
            elif val is None:
                vals.append("NA")
            else:
                vals.append(str(val).replace("|", "\\|"))
        lines.append("| " + " | ".join(vals) + " |")
    if len(rows) > max_rows:
        lines.append(f"\n_Showing {max_rows} of {len(rows)} rows._")
    return "\n".join(lines) + "\n"


def write_report(db_path: str, out_dir: str, human_labels_csv: str | None = None) -> None:
    db = HarnessDB(db_path)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    run_rows = build_run_level_rows(db)
    metaphor_rows = [r for r in run_rows if r.get("control_arm") != "literal_paraphrase"]
    literal_rows = [r for r in run_rows if r.get("control_arm") == "literal_paraphrase"]

    by_stance = summarize(metaphor_rows, ["stance_pattern"])
    by_stance_distance_visibility_arm = summarize(metaphor_rows, ["stance_pattern", "domain_distance", "mapping_visibility", "control_arm"])
    by_provider = summarize(metaphor_rows, ["provider", "model"])
    by_provider_temp = summarize(metaphor_rows, ["provider", "model", "temperature"])
    by_far = summarize([r for r in metaphor_rows if r.get("domain_distance") == "far"], ["stance_pattern", "control_arm", "mapping_visibility", "provider"])
    literal_summary = summarize(literal_rows, ["stance_pattern", "domain_distance", "provider", "model"])
    mapping_delta = build_mapping_visibility_delta(metaphor_rows)
    control_delta = build_control_delta(metaphor_rows)
    agreement = build_judge_agreement(db)
    quality = build_quality_scores(db)
    eligible_quality = [r for r in quality if r.get("eligible_quality")]
    human_agreement = build_human_agreement(db, human_labels_csv) if human_labels_csv else []

    _write_csv(out / "run_level.csv", run_rows)
    _write_csv(out / "summary_by_stance_pattern.csv", by_stance)
    _write_csv(out / "summary_by_stance_distance_visibility_arm.csv", by_stance_distance_visibility_arm)
    _write_csv(out / "summary_by_provider.csv", by_provider)
    _write_csv(out / "summary_by_provider_temperature.csv", by_provider_temp)
    _write_csv(out / "summary_far_conditions.csv", by_far)
    _write_csv(out / "summary_literal_controls.csv", literal_summary)
    _write_csv(out / "summary_mapping_visibility_delta.csv", mapping_delta)
    _write_csv(out / "summary_control_delta.csv", control_delta)
    _write_csv(out / "judge_agreement.csv", agreement)
    _write_csv(out / "quality_scores.csv", quality)
    _write_csv(out / "quality_scores_eligible.csv", eligible_quality)
    if human_labels_csv:
        _write_csv(out / "human_agreement.csv", human_agreement)

    md = []
    md.append("# Metaphoric Stance & Relational Mapping Harness Report\n")
    md.append("## Overview\n")
    md.append(f"- generations: {len(run_rows)}\n")
    md.append(f"- metaphor generations in main metrics: {len(metaphor_rows)}\n")
    md.append(f"- literal paraphrase controls, reported separately: {len(literal_rows)}\n")
    md.append(f"- quality pair comparisons: {len(db.fetch_quality_pairs())}\n")
    md.append("\nMain metaphor summaries exclude `literal_paraphrase`; literal controls are isolated below so vehicle/target stance metrics are not polluted by no-vehicle outputs.\n")

    md.append("\n## Main metaphor summary by stance pattern\n")
    md.append(_markdown_table(by_stance, [
        "stance_pattern", "n", "stance_pattern_match_rate", "stance_slip_rate",
        "vehicle_leakage_rate", "target_drift_rate", "pass_leakage_rate",
        "relation_pass_rate", "false_entailment_risk_mean", "relation_score_mean",
    ]))
    md.append("\n## Main metaphor summary by stance pattern × distance × mapping visibility × control arm\n")
    md.append(_markdown_table(by_stance_distance_visibility_arm, [
        "stance_pattern", "domain_distance", "mapping_visibility", "control_arm", "n",
        "stance_pattern_match_rate", "stance_slip_rate", "vehicle_leakage_rate",
        "pass_leakage_rate", "relation_pass_rate", "surface_only_rate",
    ], max_rows=100))
    md.append("\n## Mapping visibility delta: scaffolded minus hidden\n")
    md.append(_markdown_table(mapping_delta, [
        "stance_pattern", "domain_distance", "control_arm", "provider", "model", "n_hidden", "n_scaffolded",
        "delta_relation_pass_rate_scaffolded_minus_hidden", "delta_surface_only_rate_scaffolded_minus_hidden",
        "delta_pass_leakage_rate_scaffolded_minus_hidden", "delta_stance_slip_rate_scaffolded_minus_hidden",
    ], max_rows=80))
    md.append("\n## Forbidden-list control delta: without minus with\n")
    md.append(_markdown_table(control_delta, [
        "stance_pattern", "domain_distance", "mapping_visibility", "provider", "model", "n_with_forbidden", "n_without_forbidden",
        "delta_pass_leakage_rate_without_minus_with", "delta_vehicle_leakage_rate_without_minus_with",
        "delta_target_drift_rate_without_minus_with", "delta_stance_slip_rate_without_minus_with",
    ], max_rows=80))
    md.append("\n## Literal paraphrase controls\n")
    md.append(_markdown_table(literal_summary, [
        "stance_pattern", "domain_distance", "provider", "model", "n",
        "target_drift_rate", "unsupported_claim_rate", "pass_leakage_rate", "false_entailment_risk_mean",
    ], max_rows=40))
    md.append("\n## Summary by provider, metaphor arms only\n")
    md.append(_markdown_table(by_provider, [
        "provider", "model", "n", "stance_pattern_match_rate", "stance_slip_rate",
        "vehicle_leakage_rate", "pass_leakage_rate", "relation_pass_rate",
    ]))
    md.append("\n## Far-domain conditions, metaphor arms only\n")
    md.append(_markdown_table(by_far, [
        "stance_pattern", "control_arm", "mapping_visibility", "provider", "n", "stance_pattern_match_rate",
        "stance_slip_rate", "relation_pass_rate", "surface_only_rate",
    ], max_rows=80))
    md.append("\n## Judge agreement: pairwise Cohen's κ\n")
    md.append(_markdown_table(agreement, [
        "audit_type", "label", "judge_a", "judge_b", "n_common", "cohens_kappa",
    ], max_rows=80))
    if human_labels_csv:
        md.append("\n## Human gold agreement\n")
        md.append(_markdown_table(human_agreement, ["label", "n_common", "agreement_rate", "cohens_kappa"], max_rows=20))

    md.append("\n## Top raw quality pairwise scores\n")
    md.append(_markdown_table(quality[:20], [
        "case_id", "provider", "model", "control_arm", "mapping_visibility", "temperature", "comparisons", "quality_win_rate", "eligible_quality", "generated_text",
    ], max_rows=20))
    md.append("\n## Top eligible quality pairwise scores\n")
    md.append(_markdown_table(eligible_quality[:20], [
        "case_id", "provider", "model", "control_arm", "mapping_visibility", "temperature", "comparisons", "quality_win_rate", "generated_text",
    ], max_rows=20))

    (out / "report.md").write_text("\n".join(md), encoding="utf-8")
    db.close()


def _parse_human_bool(value: Any) -> bool | None:
    return bool_or_none(value)


def export_human_gold(db_path: str, out_csv: str, n: int = 50, seed: str = "human-gold") -> None:
    import random

    db = HarnessDB(db_path)
    rows = build_run_level_rows(db)
    db.close()
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[(row.get("stance_pattern"), row.get("domain_distance"), row.get("mapping_visibility"), row.get("control_arm"))].append(row)
    rng = random.Random(seed)
    selected: list[dict[str, Any]] = []
    group_keys = list(groups.keys())
    rng.shuffle(group_keys)
    while len(selected) < n and any(groups.values()):
        for key in list(group_keys):
            bucket = groups[key]
            if not bucket:
                continue
            idx = rng.randrange(len(bucket))
            selected.append(bucket.pop(idx))
            if len(selected) >= n:
                break

    out = Path(out_csv)
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "run_id", "case_id", "case_hash", "stance_pattern", "domain_distance", "mapping_visibility", "control_arm",
        "provider", "model", "temperature", "sample_index", "generated_text",
        "human_stance_pattern_match", "human_stance_slip", "human_pass_leakage", "human_pass_relation",
        "human_notes",
    ]
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in selected:
            writer.writerow({k: row.get(k, "") for k in fields})


def build_human_agreement(db: HarnessDB, human_csv_path: str) -> list[dict[str, Any]]:
    run_rows = {r["run_id"]: r for r in build_run_level_rows(db)}
    comparisons = {
        "stance_pattern_match": "human_stance_pattern_match",
        "stance_slip": "human_stance_slip",
        "pass_leakage": "human_pass_leakage",
        "pass_relation": "human_pass_relation",
    }
    human: dict[str, dict[str, bool]] = {label: {} for label in comparisons}
    llm: dict[str, dict[str, bool]] = {label: {} for label in comparisons}

    with open(human_csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            run_id = row.get("run_id", "")
            rr = run_rows.get(run_id)
            if not rr:
                continue
            for label, human_col in comparisons.items():
                hv = _parse_human_bool(row.get(human_col))
                lv = bool_or_none(rr.get(label))
                if hv is not None and lv is not None:
                    human[label][run_id] = hv
                    llm[label][run_id] = lv

    out: list[dict[str, Any]] = []
    for label in comparisons:
        common = set(human[label]) & set(llm[label])
        if not common:
            out.append({"label": label, "n_common": 0, "agreement_rate": None, "cohens_kappa": None})
            continue
        agree = sum(1 for k in common if human[label][k] == llm[label][k]) / len(common)
        kappa = cohens_kappa({k: human[label][k] for k in common}, {k: llm[label][k] for k in common})
        out.append({"label": label, "n_common": len(common), "agreement_rate": agree, "cohens_kappa": kappa})
    return out
