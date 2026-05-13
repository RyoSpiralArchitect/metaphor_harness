from __future__ import annotations

import argparse
import asyncio
import sys

from .io_utils import load_cases_jsonl
from .providers import PROVIDER_PROFILE_NAMES, TOKEN_PARAMETER_NAMES, provider_spec_from_profile
from .report import write_report, export_human_gold
from .runner import HarnessRunner, RunOptions


def _parse_csv_floats(text: str) -> list[float]:
    return [float(x.strip()) for x in text.split(",") if x.strip()]


def _parse_csv_strings(text: str) -> list[str]:
    return [x.strip() for x in text.split(",") if x.strip()]


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="metaphor-harness",
        description="Metaphoric Stance & Relational Mapping Harness",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    run = sub.add_parser("run", help="Run generation, audits, and optional pairwise quality comparisons")
    run.add_argument("--cases", required=True, help="Path to cases JSONL")
    run.add_argument("--config", help="Provider config JSON. If omitted, use --model and --judge-model.")
    run.add_argument("--provider", default="openai", choices=PROVIDER_PROFILE_NAMES, help="Generator provider profile")
    run.add_argument("--model", help="Generator model name when --config is omitted")
    run.add_argument("--judge-provider", choices=PROVIDER_PROFILE_NAMES, help="Judge provider profile; defaults to --provider")
    run.add_argument("--judge-model", help="Judge model name when --config is omitted")
    run.add_argument("--base-url", help="Generator base URL for openai_compatible providers")
    run.add_argument("--judge-base-url", help="Judge base URL for openai_compatible providers")
    run.add_argument("--api-key-env", help="Generator API key environment variable")
    run.add_argument("--judge-api-key-env", help="Judge API key environment variable")
    run.add_argument("--max-output-tokens", type=int, default=700, help="Generator output token cap")
    run.add_argument("--judge-max-output-tokens", type=int, default=2000, help="Judge output token cap")
    run.add_argument("--token-parameter", choices=TOKEN_PARAMETER_NAMES, help="Override generator token cap parameter")
    run.add_argument("--judge-token-parameter", choices=TOKEN_PARAMETER_NAMES, help="Override judge token cap parameter")
    run.add_argument("--db", required=True, help="SQLite output DB")
    run.add_argument("--samples", type=int, default=5, help="Samples per cell")
    run.add_argument("--temperatures", default="0.2,0.7,1.1", help="Comma-separated temperatures")
    run.add_argument(
        "--arms",
        default="metaphor_with_forbidden,metaphor_without_forbidden,literal_paraphrase,stance_explicit_metaphor",
        help="Comma-separated control arms",
    )
    run.add_argument(
        "--mapping-visibility",
        default="hidden,scaffolded",
        help="Comma-separated mapping scaffold visibility values: hidden,scaffolded. literal_paraphrase always uses hidden.",
    )
    run.add_argument("--concurrency", type=int, default=4)
    run.add_argument("--retries", type=int, default=2)
    run.add_argument("--dry-run", action="store_true")
    run.add_argument("--allow-risky-false-targets", action="store_true")
    run.add_argument("--no-quality", action="store_true", help="Skip pairwise quality comparisons")
    run.add_argument("--quality-pairs-per-group", type=int, default=12)

    rep = sub.add_parser("report", help="Write Markdown and CSV reports from a DB")
    rep.add_argument("--db", required=True)
    rep.add_argument("--out", required=True, help="Output directory")
    rep.add_argument("--human-labels", default=None, help="Optional human-label CSV exported by export-gold")
    rep.add_argument("--judge-provider", default=None, help="Optional judge provider name filter, e.g. mistral_judge")
    rep.add_argument("--judge-model", default=None, help="Optional judge model filter")

    gold = sub.add_parser("export-gold", help="Export a stratified CSV template for human labels")
    gold.add_argument("--db", required=True)
    gold.add_argument("--out", required=True, help="Output CSV path")
    gold.add_argument("--n", type=int, default=50)
    gold.add_argument("--seed", default="human-gold")

    val = sub.add_parser("validate-cases", help="Validate cases JSONL schema")
    val.add_argument("--cases", required=True)

    return p


async def _run_async(args: argparse.Namespace) -> None:
    generator_specs = None
    judge_specs = None
    if not args.config:
        judge_provider = args.judge_provider or args.provider
        generator_specs = [
            provider_spec_from_profile(
                name=f"{args.provider}_generator",
                provider=args.provider,
                model=args.model,
                base_url=args.base_url,
                api_key_env=args.api_key_env,
                max_tokens=args.max_output_tokens,
                token_parameter=args.token_parameter,
            )
        ]
        judge_specs = [
            provider_spec_from_profile(
                name=f"{judge_provider}_judge",
                provider=judge_provider,
                model=args.judge_model,
                base_url=args.judge_base_url,
                api_key_env=args.judge_api_key_env,
                max_tokens=args.judge_max_output_tokens,
                token_parameter=args.judge_token_parameter,
            )
        ]
    opts = RunOptions(
        cases_path=args.cases,
        db_path=args.db,
        samples=args.samples,
        temperatures=_parse_csv_floats(args.temperatures),
        control_arms=_parse_csv_strings(args.arms),
        mapping_visibility=_parse_csv_strings(args.mapping_visibility),
        config_path=args.config,
        generator_specs=generator_specs,
        judge_specs=judge_specs,
        concurrency=args.concurrency,
        retries=args.retries,
        dry_run=args.dry_run,
        allow_risky_false_targets=args.allow_risky_false_targets,
        run_quality_pairs=not args.no_quality,
        quality_pairs_per_group=args.quality_pairs_per_group,
    )
    runner = HarnessRunner(opts)
    try:
        await runner.run()
    finally:
        runner.close()


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.cmd == "run":
        if not args.config and (not args.model or not args.judge_model):
            parser.error("run requires either --config or both --model and --judge-model")
        asyncio.run(_run_async(args))
        return 0
    if args.cmd == "report":
        write_report(
            args.db,
            args.out,
            human_labels_csv=args.human_labels,
            judge_provider=args.judge_provider,
            judge_model=args.judge_model,
        )
        print(f"wrote report to {args.out}")
        return 0
    if args.cmd == "export-gold":
        export_human_gold(args.db, args.out, n=args.n, seed=args.seed)
        print(f"wrote human-label template to {args.out}")
        return 0
    if args.cmd == "validate-cases":
        cases = load_cases_jsonl(args.cases)
        print(f"valid cases: {len(cases)}")
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
