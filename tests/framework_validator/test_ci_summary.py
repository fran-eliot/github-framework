"""Tests for the Framework Validator GitHub Actions summary."""

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.framework_validator.ci_summary import render_summary
from scripts.framework_validator.__main__ import REPOSITORY_ROOT


class FrameworkValidatorSummaryTests(unittest.TestCase):
    def test_full_success_summary(self) -> None:
        report = {
            "status": "passed",
            "scope": {
                "families": ["readme", "documentation", "workflow"],
                "filtered": False,
            },
            "summary": {
                "passed_components": 21,
                "failed_components": 0,
                "error_count": 0,
            },
        }
        summary = render_summary(report)
        self.assertIn("| Validation | Passed |", summary)
        self.assertIn("| Scope | Full (readme, documentation, workflow) |", summary)
        self.assertIn("| Passed Components | 21 |", summary)
        self.assertIn("| Validation errors | 0 |", summary)

    def test_partial_failure_summary(self) -> None:
        report = {
            "status": "failed",
            "scope": {"families": ["workflow"], "filtered": True},
            "summary": {
                "passed_components": 2,
                "failed_components": 1,
                "error_count": 3,
            },
        }
        summary = render_summary(report)
        self.assertIn("| Validation | Failed |", summary)
        self.assertIn("| Scope | Partial (workflow) |", summary)
        self.assertIn("| Failed Components | 1 |", summary)
        self.assertIn("| Validation errors | 3 |", summary)

    def test_cli_appends_summary_from_json_file(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "validator-report.json"
            target = root / "summary.md"
            target.write_text("Earlier step\n", encoding="utf-8")
            source.write_text(
                json.dumps({
                    "status": "passed",
                    "scope": {"families": ["documentation"], "filtered": True},
                    "summary": {
                        "passed_components": 1,
                        "failed_components": 0,
                        "error_count": 0,
                    },
                }),
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable, "-m",
                    "scripts.framework_validator.ci_summary", str(source),
                ],
                cwd=REPOSITORY_ROOT,
                env={**os.environ, "GITHUB_STEP_SUMMARY": str(target)},
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            output = target.read_text(encoding="utf-8")
            self.assertTrue(output.startswith("Earlier step\n"))
            self.assertIn("| Scope | Partial (documentation) |", output)

    def test_cli_missing_report_records_diagnostic(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "summary.md"
            result = subprocess.run(
                [
                    sys.executable, "-m",
                    "scripts.framework_validator.ci_summary",
                    str(root / "missing.json"),
                ],
                cwd=REPOSITORY_ROOT,
                env={**os.environ, "GITHUB_STEP_SUMMARY": str(target)},
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(
                "No JSON report was produced",
                target.read_text(encoding="utf-8"),
            )

    def test_failed_components_are_listed_with_error_counts(self) -> None:
        report = {
            "status": "failed",
            "scope": {"families": ["documentation"], "filtered": True},
            "summary": {
                "passed_components": 1,
                "failed_components": 2,
                "error_count": 3,
            },
            "components": [
                {
                    "relative_path": "documentation/architecture",
                    "status": "passed",
                    "errors": [],
                },
                {
                    "relative_path": "documentation/references",
                    "status": "failed",
                    "errors": ["missing metadata.yml"],
                },
                {
                    "relative_path": "documentation/samples",
                    "status": "failed",
                    "errors": ["error one", "error two"],
                },
            ],
        }
        result = render_summary(report)
        self.assertIn("### Failed Components", result)
        self.assertIn("| documentation/references | 1 |", result)
        self.assertIn("| documentation/samples | 2 |", result)
        self.assertNotIn("| documentation/architecture |", result)

    def test_success_summary_does_not_include_failed_table(self) -> None:
        report = {
            "status": "passed",
            "scope": {"families": ["workflow"], "filtered": True},
            "summary": {
                "passed_components": 1,
                "failed_components": 0,
                "error_count": 0,
            },
            "components": [
                {
                    "relative_path": "workflow/issue",
                    "status": "passed",
                    "errors": [],
                },
            ],
        }
        self.assertNotIn("### Failed Components", render_summary(report))

    def test_failed_components_list_is_limited_to_ten(self) -> None:
        components = [
            {
                "relative_path": f"documentation/component-{i:02}",
                "status": "failed",
                "errors": ["invalid metadata"],
            }
            for i in range(12)
        ]
        report = {
            "status": "failed",
            "scope": {"families": ["documentation"], "filtered": True},
            "summary": {
                "passed_components": 0,
                "failed_components": 12,
                "error_count": 12,
            },
            "components": components,
        }
        result = render_summary(report)
        self.assertIn("| documentation/component-09 | 1 |", result)
        self.assertNotIn("| documentation/component-10 | 1 |", result)
        self.assertIn("2 more failed Component(s)", result)

    def test_failed_component_paths_are_escaped(self) -> None:
        report = {
            "status": "failed",
            "scope": {"families": ["documentation"], "filtered": True},
            "summary": {
                "passed_components": 0,
                "failed_components": 1,
                "error_count": 1,
            },
            "components": [
                {
                    "relative_path": "documentation/invalid|line\nbreak",
                    "status": "failed",
                    "errors": ["invalid metadata"],
                },
            ],
        }
        result = render_summary(report)
        self.assertIn(r"| documentation/invalid\|line break | 1 |", result)
