from __future__ import annotations

from typing import Any, Iterable

PASS_RULES_VERSION = "rules"


def bool_or_none(x: Any) -> bool | None:
    if isinstance(x, bool):
        return x
    if isinstance(x, str):
        text = x.strip().lower()
        if text in {"true", "yes", "y", "1", "pass"}:
            return True
        if text in {"false", "no", "n", "0", "fail"}:
            return False
    if isinstance(x, (int, float)) and x in {0, 1}:
        return bool(x)
    return None


def int_or_none(x: Any) -> int | None:
    try:
        if x is None or isinstance(x, bool):
            return None
        return int(float(x))
    except Exception:
        return None


def number_or_none(x: Any) -> float | None:
    try:
        if x is None or isinstance(x, bool):
            return None
        return float(x)
    except Exception:
        return None


def majority_bool(values: Iterable[Any]) -> bool | None:
    vals = [bool_or_none(v) for v in values]
    vals = [v for v in vals if v is not None]
    if not vals:
        return None
    true_count = sum(1 for v in vals if v)
    false_count = len(vals) - true_count
    if true_count > false_count:
        return True
    if false_count > true_count:
        return False
    return None


def mean_number(values: Iterable[Any]) -> float | None:
    nums: list[float] = []
    for v in values:
        n = number_or_none(v)
        if n is not None:
            nums.append(n)
    if not nums:
        return None
    return sum(nums) / len(nums)


def compute_pass_stance_pattern(labels: dict[str, Any]) -> bool | None:
    stance_pattern_match = bool_or_none(labels.get("stance_pattern_match"))
    stance_slip = bool_or_none(labels.get("stance_slip"))
    if stance_pattern_match is False or stance_slip is True:
        return False
    if stance_pattern_match is True and stance_slip is False:
        return True
    return None


def compute_pass_leakage(labels: dict[str, Any]) -> bool | None:
    literal_vehicle = bool_or_none(labels.get("literal_vehicle_asserted"))
    unsupported = bool_or_none(labels.get("unsupported_new_claim"))
    target_drift = bool_or_none(labels.get("target_drift"))
    risk = number_or_none(labels.get("false_entailment_risk"))
    if risk is None:
        risk = number_or_none(labels.get("false_entailment_risk_mean"))

    fail_flags = [literal_vehicle, unsupported, target_drift]
    if any(v is True for v in fail_flags):
        return False
    if risk is not None and risk >= 4:
        return False
    if all(v is False for v in fail_flags) and risk is not None:
        return True
    return None


def compute_pass_relation(labels: dict[str, Any]) -> bool | None:
    surface = bool_or_none(labels.get("surface_only_mapping"))
    mapping_pass = bool_or_none(labels.get("relation_mapping_pass"))
    score = number_or_none(labels.get("relation_score"))
    if score is None:
        score = number_or_none(labels.get("relation_score_mean"))

    if surface is True:
        return False
    if mapping_pass is False:
        return False
    if score is not None and score <= 2:
        return False
    if surface is False and mapping_pass is True and score is not None and score >= 3:
        return True
    return None


def apply_computed_pass_labels(parsed: dict[str, Any], audit_type: str) -> dict[str, Any]:
    """Return a copy with deterministic pass_* labels overriding judge-supplied pass fields.

    The original judge pass fields are preserved as judge_pass_*_raw. Primitive labels
    such as literal_vehicle_asserted and relation_score are left untouched.
    """
    out = dict(parsed)
    out["pass_rules_version"] = PASS_RULES_VERSION

    if audit_type == "stance_leakage":
        if "pass_stance_pattern" in out:
            out["judge_pass_stance_pattern_raw"] = out.get("pass_stance_pattern")
        if "pass_leakage" in out:
            out["judge_pass_leakage_raw"] = out.get("pass_leakage")
        out["pass_stance_pattern"] = compute_pass_stance_pattern(out)
        out["pass_leakage"] = compute_pass_leakage(out)
    elif audit_type == "relation":
        if "pass_relation" in out:
            out["judge_pass_relation_raw"] = out.get("pass_relation")
        out["pass_relation"] = compute_pass_relation(out)
    return out
