"""Standalone CLI integration and failure reporting."""
from contextlib import redirect_stdout, redirect_stderr
from hashlib import sha256
from io import StringIO
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from scripts.repository_generation.cli import main
from scripts.repository_generation.destination import DestinationError
from test_inputs import fixture

ROOT = Path(__file__).resolve().parents[2]


class CliTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.parent = Path(temp.name).resolve()
        self.input = self.parent / "project.json"
        self.input.write_text(json.dumps(fixture()), encoding="utf-8")

    def arguments(self, mode="plan", name="sample-backend"):
        return [mode, "TPL-BACKEND", "--template-version", "0.1.0",
                "--input", str(self.input), "--output-parent", str(self.parent),
                "--name", name]

    def invoke(self, args):
        return subprocess.run([sys.executable, "-B", "-m", "scripts.repository_generation", *args],
                              cwd=ROOT, capture_output=True, encoding="utf-8",
                              env={**os.environ, "PYTHONIOENCODING": "utf-8"},
                              check=False, timeout=30)

    def test_help_and_bad_arguments(self):
        help_result = self.invoke(["--help"])
        self.assertEqual(help_result.returncode, 0, help_result.stderr)
        self.assertIn("plan", help_result.stdout)
        self.assertIn("generate", help_result.stdout)
        for args in ([], ["plan"], self.arguments() + ["--unknown"],
                     self.arguments()[:-2] + ["--nam", "sample"]):
            with self.subTest(args=args):
                result = self.invoke(args)
                self.assertEqual(result.returncode, 2)
                self.assertTrue(result.stderr)

    def test_plan_reports_inventory_and_does_not_write(self):
        result = self.invoke(self.arguments())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count(" | Selected\n"), 8)
        self.assertEqual(result.stdout.count(" | Unselected\n"), 20)
        self.assertIn("required | README-HERO | Resolved | Selected", result.stdout)
        self.assertIn("VCL-HERO", result.stdout)
        self.assertIn("not full Template conformance", result.stdout)
        self.assertIn("Metadata: framework/components/readme/hero/metadata.yml", result.stdout)
        self.assertIn("Artifact: framework/components/readme/hero/template.md", result.stdout)
        self.assertIn("Plan complete; no destination writes.", result.stdout)
        self.assertEqual(list(self.parent.iterdir()), [self.input])

    def test_generate_matches_plan_and_only_writes_fixed_documents(self):
        planned = self.invoke(self.arguments())
        self.assertEqual(planned.returncode, 0, planned.stderr)
        result = self.invoke(self.arguments("generate"))
        self.assertEqual(result.returncode, 0, result.stderr)
        target = self.parent / "sample-backend"
        self.assertEqual(sorted(p.name for p in target.iterdir()), ["CHANGELOG.md", "README.md"])
        for path in target.iterdir():
            digest = sha256(path.read_bytes()).hexdigest()
            self.assertIn(digest, planned.stdout)
            self.assertIn(digest, result.stdout)
        self.assertIn("Generation complete.", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_generate_rechecks_input_and_destination(self):
        self.assertEqual(self.invoke(self.arguments()).returncode, 0)
        initial = self.input.read_bytes()
        self.input.write_text("{}", encoding="utf-8")
        result = self.invoke(self.arguments("generate"))
        self.assertEqual(result.returncode, 2)
        self.assertFalse((self.parent / "sample-backend").exists())
        self.input.write_bytes(initial)
        target = self.parent / "sample-backend"
        target.mkdir()
        sentinel = target / "keep.txt"
        sentinel.write_bytes(b"keep")
        result = self.invoke(self.arguments("generate"))
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertEqual(sentinel.read_bytes(), b"keep")

    def test_unsupported_profile_and_invalid_input(self):
        args = self.arguments()
        args[1] = "TPL-FULLSTACK"
        for mode in ("plan", "generate"):
            args[0] = mode
            result = self.invoke(args)
            self.assertEqual(result.returncode, 2)
            self.assertIn("unsupported Template", result.stderr)
            self.assertEqual(result.stdout, "")
        self.input.write_text('{"project_name":"A","project_name":"B"}', encoding="utf-8")
        result = self.invoke(self.arguments())
        self.assertEqual(result.returncode, 2)
        self.assertIn("duplicate", result.stderr)
        self.assertEqual(list(self.parent.iterdir()), [self.input])

    def test_destination_error_and_partial_failure_reporting(self):
        result = self.invoke(self.arguments(name="../escape"))
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertIn("Destination error", result.stderr)
        target = self.parent / "sample-backend"
        with patch("scripts.repository_generation.cli.write_documents",
                   side_effect=DestinationError(f"inspect incomplete output at {target}", target)):
            out, err = StringIO(), StringIO()
            with redirect_stdout(out), redirect_stderr(err):
                code = main(self.arguments("generate"))
        self.assertEqual(code, 1)
        self.assertEqual(out.getvalue(), "")
        self.assertIn(str(target), err.getvalue())


if __name__ == "__main__":
    unittest.main()
