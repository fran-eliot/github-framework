"""Independent read-only Template composition preview command."""

import argparse
from pathlib import Path
import sys

from . import SourceError
from .registry import load_registry
from .report import render_report
from .resolution import resolve_composition
from .sources import TEMPLATES, discover_physical, load_template

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m scripts.template_composition_preview",
        description="Preview one canonical Repository Template composition (read-only).",
        allow_abbrev=False,
    )
    parser.add_argument("template_id", choices=tuple(TEMPLATES))
    args = parser.parse_args(argv)
    try:
        template = load_template(REPOSITORY_ROOT, args.template_id)
        registry = load_registry(REPOSITORY_ROOT)
        physical = discover_physical(REPOSITORY_ROOT)
        result = resolve_composition(template, registry, physical)
        report = render_report(result)
    except SourceError as exc:
        print(f"Source error: {exc}", file=sys.stderr)
        return 2
    print(report, end="")
    return 1 if result.has_conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
