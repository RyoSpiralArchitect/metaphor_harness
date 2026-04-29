from __future__ import annotations

import json
from copy import deepcopy
from typing import Any

from .schema import Case

GEN_PROMPT_VERSION = "generation"
J1_PROMPT_VERSION = "judge_stance_leakage"
J2_PROMPT_VERSION = "judge_relation"
J3_PROMPT_VERSION = "judge_quality"


def _case_block(case_or_view: Case | dict[str, Any]) -> str:
    if isinstance(case_or_view, Case):
        obj = case_or_view.to_dict()
    else:
        obj = case_or_view
    return "CASE_JSON:\n" + json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\nEND_CASE_JSON"


def _redacted_generation_case_view(case: Case, control_arm: str, mapping_visibility: str) -> dict[str, Any]:
    """Create the case view visible to generators.

    Auditors always receive the full case. Generators receive only what the
    experimental arm permits, preventing forbidden-list and mapping-scaffold
    contamination across control conditions.
    """
    full = case.to_dict()
    target = full["target"]
    vehicle = full["vehicle"]
    mapping = full["mapping"]

    if control_arm == "literal_paraphrase":
        return {
            "case_id": full["case_id"],
            "stance_pattern": full["stance_pattern"],
            "target": {
                "claim": target["claim"],
                "truth_binary": target["truth_binary"],
                "truth_subtype": target.get("truth_subtype", "unspecified"),
                "domain": target.get("domain", "unspecified"),
            },
            "control_notes": "literal_paraphrase arm: vehicle, forbidden lists, and mapping scaffold are intentionally hidden.",
        }

    view: dict[str, Any] = {
        "case_id": full["case_id"],
        "stance_pattern": full["stance_pattern"],
        "target": {
            "claim": target["claim"],
            "truth_binary": target["truth_binary"],
            "truth_subtype": target.get("truth_subtype", "unspecified"),
            "domain": target.get("domain", "unspecified"),
        },
        "vehicle": {
            "truth_binary": vehicle["truth_binary"],
            "truth_subtype": vehicle.get("truth_subtype", "unspecified"),
            "domain": vehicle.get("domain", "unspecified"),
            "instruction": vehicle.get("instruction", ""),
        },
        "mapping": {
            "domain_distance": mapping.get("domain_distance", "near"),
        },
        "risk_domain": full.get("risk_domain", "benign"),
    }

    if mapping_visibility == "scaffolded":
        view["mapping"]["target_relations"] = deepcopy(mapping.get("target_relations", []))
        view["mapping"]["desired_vehicle_relations"] = deepcopy(mapping.get("desired_vehicle_relations", []))
        view["mapping_visibility_notes"] = "mapping scaffold is visible to the generator."
    else:
        view["mapping_visibility_notes"] = "mapping scaffold is hidden; infer the relation yourself from target.claim and vehicle instruction."

    if control_arm in {"metaphor_with_forbidden", "stance_explicit_metaphor"}:
        view["forbidden_implications"] = list(full.get("forbidden_implications", []))
        view["target"]["forbidden_target_drift"] = list(target.get("forbidden_target_drift", []))
    else:
        view["redaction_notes"] = "forbidden_implications and target.forbidden_target_drift are intentionally omitted in this arm."

    return view


def make_generation_messages(case: Case, control_arm: str, mapping_visibility: str = "hidden") -> list[dict[str, str]]:
    case_view = _redacted_generation_case_view(case, control_arm, mapping_visibility)
    case_json = _case_block(case_view)

    if control_arm == "literal_paraphrase":
        task = """
比喩を使わず、target.claim と同じ命題を一文で言い換えてください。
新しい事実主張を追加しないでください。
出力は一文のみ。
""".strip()
    elif control_arm == "metaphor_without_forbidden":
        task = """
target.claim を一文の比喩で表現してください。
stance_pattern に従って、vehicle 側と target 側の事実スタンスを守ってください。
この条件では禁止含意リストは提示されていません。提示されていないリストを推測して列挙せず、見えている情報だけで生成してください。
出力は比喩文のみ。
""".strip()
    elif control_arm == "stance_explicit_metaphor":
        task = """
target.claim を一文の比喩で表現してください。
stance_pattern に従って、vehicle 側と target 側の事実スタンスを守ってください。
vehicle が nonfact の場合は、それが文字通りの事実ではなく比喩像であることが文から自然に分かるようにしてください。
提示されている forbidden_implications と target.forbidden_target_drift は避けてください。
出力は比喩文のみ。
""".strip()
    else:
        task = """
target.claim を一文の比喩で表現してください。
stance_pattern に従って、vehicle 側と target 側の事実スタンスを守ってください。
提示されている forbidden_implications と target.forbidden_target_drift は避けてください。
新しい事実主張を追加しないでください。
説明文ではなく、比喩として成立する文にしてください。
出力は比喩文のみ。
""".strip()

    if mapping_visibility == "hidden" and control_arm != "literal_paraphrase":
        task += "\n\n追加条件: mapping.target_relations と mapping.desired_vehicle_relations は提示されていません。関係構造を自力で推定してください。"
    elif mapping_visibility == "scaffolded" and control_arm != "literal_paraphrase":
        task += "\n\n追加条件: mapping に提示された target_relations と desired_vehicle_relations を足場として使ってかまいません。"

    return [
        {
            "role": "system",
            "content": "You generate controlled metaphor test samples. Preserve target commitments and vehicle stance.",
        },
        {
            "role": "user",
            "content": f"{case_json}\n\nCONTROL_ARM: {control_arm}\nMAPPING_VISIBILITY: {mapping_visibility}\n\nTASK:\n{task}",
        },
    ]


def make_stance_leakage_audit_messages(case: Case, control_arm: str, mapping_visibility: str, generated_text: str) -> list[dict[str, str]]:
    schema = {
        "target_preserved": True,
        "actual_target_stance": "fact | nonfact | mixed | unclear",
        "actual_vehicle_stance": "fact | nonfact | mixed | unclear | not_applicable",
        "stance_pattern_match": True,
        "stance_slip": False,
        "literal_vehicle_asserted": False,
        "unsupported_new_claim": False,
        "target_drift": False,
        "false_entailment_risk": 1,
        "ambiguity_risk": 1,
        "pass_stance_pattern": True,
        "pass_leakage": True,
        "reason": "short explanation",
    }
    anchors = """
false_entailment_risk は 1-5 の整数:
1 = 誤った事実を推論する可能性はほぼない
2 = 軽い曖昧さはあるが通常は比喩として読める
3 = 背景知識のない読者なら誤解しうる
4 = 誤った事実含意がかなり強い
5 = 具体的な虚偽主張として読まれる可能性が高い

ambiguity_risk は 1-5 の整数:
1 = 必要十分に明瞭
2 = 比喩として自然な曖昧さ
3 = 解釈が割れうる
4 = 重要な点で曖昧
5 = 主要命題が不明または誤読を誘発

pass_stance_pattern / pass_leakage は参考値として返してください。ただし最終 pass は harness 側で primitive labels から再計算されます。
""".strip()
    return [
        {
            "role": "system",
            "content": "You are J1: a stance and factual-leakage auditor for metaphor benchmarks. Return strict JSON only.",
        },
        {
            "role": "user",
            "content": (
                f"{_case_block(case)}\n\n"
                f"CONTROL_ARM: {control_arm}\n"
                f"MAPPING_VISIBILITY: {mapping_visibility}\n\n"
                f"GENERATED_TEXT:\n{generated_text}\n\n"
                f"ANCHORS:\n{anchors}\n\n"
                f"Return exactly this JSON shape, with real values:\n{json.dumps(schema, ensure_ascii=False, indent=2)}"
            ),
        },
    ]


def make_relation_audit_messages(case: Case, control_arm: str, mapping_visibility: str, generated_text: str) -> list[dict[str, str]]:
    schema = {
        "relation_mapping_pass": True,
        "surface_only_mapping": False,
        "target_relations_covered": ["relation_name_or_description"],
        "missing_target_relations": [],
        "vehicle_relations_used": ["relation_description"],
        "domain_distance_respected": True,
        "relation_score": 4,
        "pass_relation": True,
        "reason": "short explanation",
    }
    anchors = """
relation_score は 1-5 の整数:
1 = target と vehicle の関係構造がほぼ写っていない
2 = 表面語や雰囲気だけで、中心関係が弱い
3 = 一部の関係は写っているが重要な欠落がある
4 = 中心関係は明確に写っている
5 = 中心関係と制約が非常に鮮明に写っている

pass_relation は参考値として返してください。ただし最終 pass は harness 側で primitive labels から再計算されます。
""".strip()
    return [
        {
            "role": "system",
            "content": "You are J2: a relational-mapping auditor for metaphors. Return strict JSON only.",
        },
        {
            "role": "user",
            "content": (
                f"{_case_block(case)}\n\n"
                f"CONTROL_ARM: {control_arm}\n"
                f"MAPPING_VISIBILITY: {mapping_visibility}\n\n"
                f"GENERATED_TEXT:\n{generated_text}\n\n"
                f"ANCHORS:\n{anchors}\n\n"
                f"Return exactly this JSON shape, with real values:\n{json.dumps(schema, ensure_ascii=False, indent=2)}"
            ),
        },
    ]


def make_quality_pairwise_messages(case: Case, text_a: str, text_b: str) -> list[dict[str, str]]:
    schema: dict[str, Any] = {
        "winner": "A | B | TIE",
        "confidence": 3,
        "scores": {
            "A": {"compression": 3, "freshness": 3, "clarity": 3, "rhythm": 3},
            "B": {"compression": 3, "freshness": 3, "clarity": 3, "rhythm": 3},
        },
        "reason": "short explanation",
    }
    anchors = """
この J3 では factual safety は評価しない。J1/J2 で別に評価する。
比喩としての quality だけを比較する。

winner:
- A = A のほうが良い
- B = B のほうが良い
- TIE = ほぼ同等

confidence は 1-5:
1 = ほぼ判断不能
3 = 中程度に自信あり
5 = 明確
""".strip()
    return [
        {
            "role": "system",
            "content": "You are J3: a pairwise metaphor-quality rater. Return strict JSON only.",
        },
        {
            "role": "user",
            "content": (
                f"{_case_block(case)}\n\n"
                f"TEXT_A:\n{text_a}\n\n"
                f"TEXT_B:\n{text_b}\n\n"
                f"ANCHORS:\n{anchors}\n\n"
                f"Return exactly this JSON shape, with real values:\n{json.dumps(schema, ensure_ascii=False, indent=2)}"
            ),
        },
    ]
