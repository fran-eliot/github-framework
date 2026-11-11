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
