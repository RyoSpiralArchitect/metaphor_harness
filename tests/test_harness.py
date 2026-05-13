from __future__ import annotations

import asyncio
import csv
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from metaphor_harness.cli import main
from metaphor_harness.db import HarnessDB
from metaphor_harness.eval_rules import compute_pass_leakage, compute_pass_stance_pattern, compute_pass_relation, majority_bool
from metaphor_harness.io_utils import load_cases_jsonl
from metaphor_harness.prompts import make_generation_messages
from metaphor_harness.providers import OpenAICompatibleProvider, ProviderSpec, provider_spec_from_profile
from metaphor_harness.report import build_run_level_rows, write_report
from metaphor_harness.runner import HarnessRunner, RunOptions
from metaphor_harness.schema import case_content_hash


ROOT = Path(__file__).resolve().parents[1]


class HarnessTests(unittest.TestCase):
    def test_generation_prompt_redacts_forbidden_and_mapping_when_hidden(self) -> None:
        case = load_cases_jsonl(ROOT / "data" / "seeds.jsonl")[0]
        hidden = make_generation_messages(case, "metaphor_without_forbidden", mapping_visibility="hidden")[-1]["content"]
        scaffolded = make_generation_messages(case, "metaphor_with_forbidden", mapping_visibility="scaffolded")[-1]["content"]
        literal = make_generation_messages(case, "literal_paraphrase", mapping_visibility="scaffolded")[-1]["content"]

        for forbidden in case.forbidden_implications + case.target.forbidden_target_drift:
            self.assertNotIn(forbidden, hidden)
            self.assertNotIn(forbidden, literal)
            self.assertIn(forbidden, scaffolded)

        relation_name = case.mapping.target_relations[0]["name"]
        self.assertNotIn(relation_name, hidden)
        self.assertNotIn(relation_name, literal)
        self.assertIn(relation_name, scaffolded)
        self.assertNotIn('"vehicle"', literal)

    def test_case_hash_changes_when_case_content_changes(self) -> None:
        case = load_cases_jsonl(ROOT / "data" / "seeds.jsonl")[0]
        obj = case.to_dict()
        h1 = case_content_hash(obj)
        obj["target"]["claim"] = obj["target"]["claim"] + " 追加。"
        h2 = case_content_hash(obj)
        self.assertNotEqual(h1, h2)

    def test_pass_rules_are_deterministic(self) -> None:
        self.assertIs(True, compute_pass_stance_pattern({"stance_pattern_match": True, "stance_slip": False}))
        self.assertIs(False, compute_pass_stance_pattern({"stance_pattern_match": False, "stance_slip": False}))
        self.assertIs(False, compute_pass_leakage({
            "literal_vehicle_asserted": False,
            "unsupported_new_claim": False,
            "target_drift": False,
            "false_entailment_risk": 4,
        }))
        self.assertIs(True, compute_pass_leakage({
            "literal_vehicle_asserted": False,
            "unsupported_new_claim": False,
            "target_drift": False,
            "false_entailment_risk": 1,
        }))
        self.assertIs(False, compute_pass_relation({
            "relation_mapping_pass": True,
            "surface_only_mapping": True,
            "relation_score": 5,
        }))
        self.assertIs(None, majority_bool([True, False]))

    def test_mock_runner_smoke_and_report_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            db_path = tmp / "runs.sqlite"
            report_dir = tmp / "reports"
            opts = RunOptions(
                cases_path=str(ROOT / "data" / "seeds.jsonl"),
                config_path=str(ROOT / "config" / "providers.mock.json"),
                db_path=str(db_path),
                samples=1,
                temperatures=[0.2],
                control_arms=["metaphor_with_forbidden", "metaphor_without_forbidden", "literal_paraphrase"],
                mapping_visibility=["hidden", "scaffolded"],
                concurrency=16,
                retries=1,
                run_quality_pairs=False,
            )
            runner = HarnessRunner(opts)
            try:
                asyncio.run(runner.run())
            finally:
                runner.close()

            db = HarnessDB(db_path)
            try:
                generations = db.fetch_generations()
                # literal_paraphrase collapses to hidden only: 8 cases * 3 generators * (2 metaphor arms*2 + 1 literal) = 120
                self.assertEqual(len(generations), 8 * 3 * 5)
                rows = build_run_level_rows(db)
                self.assertTrue(all("case_hash" in r for r in rows))
                self.assertTrue(any(r["mapping_visibility"] == "scaffolded" for r in rows))
                self.assertTrue(any(r["control_arm"] == "literal_paraphrase" for r in rows))
            finally:
                db.close()

            write_report(str(db_path), str(report_dir))
            self.assertTrue((report_dir / "summary_by_stance_pattern.csv").exists())
            self.assertTrue((report_dir / "summary_by_stance_distance_visibility_arm.csv").exists())
            self.assertTrue((report_dir / "summary_mapping_visibility_delta.csv").exists())
            self.assertTrue((report_dir / "summary_literal_controls.csv").exists())
            with (report_dir / "run_level.csv").open("r", encoding="utf-8", newline="") as f:
                first = next(csv.DictReader(f))
            self.assertIn("case_hash", first)
            self.assertIn("stance_pattern", first)
            self.assertIn("mapping_visibility", first)

    def test_openai_profile_uses_max_completion_tokens(self) -> None:
        spec = provider_spec_from_profile(
            name="openai_generator",
            provider="openai",
            model="gpt-5.2",
        )
        self.assertEqual(spec.base_url, "https://api.openai.com/v1")
        self.assertEqual(spec.api_key_env, "OPENAI_API_KEY")
        self.assertEqual(spec.token_parameter, "max_completion_tokens")
        judge_spec = provider_spec_from_profile(
            name="gemini_judge",
            provider="gemini",
            model="gemini-3-flash-preview",
        )
        self.assertEqual(judge_spec.token_parameter, "max_tokens")
        mistral_spec = provider_spec_from_profile(
            name="mistral_judge",
            provider="mistral",
            model="mistral-large-latest",
        )
        self.assertEqual(mistral_spec.base_url, "https://api.mistral.ai/v1")
        self.assertEqual(mistral_spec.api_key_env, "MISTRAL_API_KEY")
        self.assertEqual(mistral_spec.token_parameter, "max_tokens")

    def test_openai_compatible_payload_uses_configured_token_parameter(self) -> None:
        spec = ProviderSpec(
            name="provider",
            type="openai_compatible",
            model="gpt-5.2",
            base_url="https://api.openai.com/v1",
            api_key="test-key",
            max_tokens=123,
            token_parameter="max_completion_tokens",
        )
        provider = OpenAICompatibleProvider(spec)
        captured_payload = {}

        class FakeResponse:
            def __enter__(self) -> "FakeResponse":
                return self

            def __exit__(self, exc_type, exc, tb) -> None:
                return None

            def read(self) -> bytes:
                return b'{"choices":[{"message":{"content":[{"type":"text","text":"ok"}]}}]}'

        def fake_urlopen(req, timeout):
            del timeout
            captured_payload.update(json.loads(req.data.decode("utf-8")))
            return FakeResponse()

        with patch("metaphor_harness.providers.urllib.request.urlopen", fake_urlopen):
            self.assertEqual(provider._complete_sync([{"role": "user", "content": "hi"}], 0.2), "ok")

        self.assertEqual(captured_payload["max_completion_tokens"], 123)
        self.assertNotIn("max_tokens", captured_payload)

    def test_cli_profile_dry_run_without_config_or_keys(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            out = io.StringIO()
            with redirect_stdout(out):
                code = main([
                    "run",
                    "--cases", str(ROOT / "data" / "seeds.jsonl"),
                    "--model", "gpt-5.2",
                    "--judge-provider", "gemini",
                    "--judge-model", "gemini-3-flash-preview",
                    "--db", str(Path(td) / "runs.sqlite"),
                    "--samples", "1",
                    "--temperatures", "0.2",
                    "--arms", "metaphor_with_forbidden",
                    "--mapping-visibility", "hidden",
                    "--no-quality",
                    "--dry-run",
                ])
        self.assertEqual(code, 0)
        dry_run = json.loads(out.getvalue())
        self.assertEqual(dry_run["generators"], ["openai_generator"])
        self.assertEqual(dry_run["judges"], ["gemini_judge"])
        self.assertEqual(dry_run["planned_new_generations"], 8)


if __name__ == "__main__":
    unittest.main()
