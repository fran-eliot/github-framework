"""Executable preview tests against the checkout and isolated source fixtures."""

import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from scripts.template_composition_preview.registry import SECTIONS, HEADER, SEPARATOR

ROOT = Path(__file__).resolve().parents[2]
MODULE = "scripts.template_composition_preview"


def invoke(root, *args, cwd=None):
    env = os.environ.copy()
    env["PYTHONPATH"] = str(root)
    env["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [sys.executable, "-B", "-m", MODULE, *args],
        cwd=root if cwd is None else cwd, env=env, capture_output=True, text=True, encoding="utf-8",
        timeout=30,
    )


class CLITests(unittest.TestCase):
    def test_real_templates(self):
        for identity in ("TPL-BACKEND", "TPL-FULLSTACK", "TPL-DOCUMENTATION"):
            with self.subTest(identity=identity):
                result = invoke(ROOT, identity)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stderr, "")
                self.assertIn(f"Template: {identity}\n", result.stdout)
                self.assertIn("Version: 0.1.0\n", result.stdout)
                self.assertIn("[required]", result.stdout)
                self.assertIn("[recommended]", result.stdout)
                self.assertIn("[optional]", result.stdout)
                self.assertIn("Overall:", result.stdout)
                self.assertNotIn(str(ROOT), result.stdout)
                if identity == "TPL-DOCUMENTATION":
                    required = result.stdout.split("[required]\n")[1].split("[recommended]")[0]
                    self.assertIn("- README-LICENSE | Conceptual | Conceptual", required)
                    license_row = required.split("- README-LICENSE |")[1].split("\n- ")[0]
                    self.assertIn("Metadata: no physical match", license_row)
                    self.assertIn("40. README Component Registry", license_row)

    def test_baseline_counts_and_repeatability(self):
        expected = {
            "TPL-BACKEND": ((8, 0), (5, 2), (3, 10)),
            "TPL-FULLSTACK": ((9, 0), (4, 4), (3, 8)),
            "TPL-DOCUMENTATION": ((8, 1), (2, 5), (1, 4)),
        }
        with TemporaryDirectory() as outside:
            for identity, levels in expected.items():
                with self.subTest(identity=identity):
                    first = invoke(ROOT, identity)
                    second = invoke(ROOT, identity, cwd=Path(outside))
                    self.assertEqual(first.returncode, 0, first.stderr)
                    self.assertEqual((first.returncode, first.stdout, first.stderr),
                                     (second.returncode, second.stdout, second.stderr))
                    for level, (resolved, conceptual) in zip(
                            ("required", "recommended", "optional"), levels):
                        section = first.stdout.split(f"[{level}]\n")[1].split("\n[")[0]
                        rows = [line for line in section.splitlines() if line.startswith("- ")]
                        self.assertEqual(len(rows), resolved + conceptual)
                        self.assertEqual(sum(row.endswith(" | Resolved") for row in rows), resolved)
                        self.assertEqual(sum(row.endswith(" | Conceptual") for row in rows), conceptual)
                        self.assertIn(
                            f"Counts: Total={resolved + conceptual}; Resolved={resolved}; "
                            f"Conceptual={conceptual}; Unknown=0; Inconsistent=0; Ambiguous=0",
                            section,
                        )
                    resolved = sum(pair[0] for pair in levels)
                    conceptual = sum(pair[1] for pair in levels)
                    self.assertIn(
                        f"Overall: Total={resolved + conceptual}; Resolved={resolved}; "
                        f"Conceptual={conceptual}; Unknown=0; Inconsistent=0; Ambiguous=0",
                        first.stdout,
                    )

    def test_argument_contract(self):
        help_result = invoke(ROOT, "--help")
        self.assertEqual(help_result.returncode, 0)
        self.assertIn("TPL-BACKEND", help_result.stdout)
        for args in ((), ("tpl-backend",), ("TPL-UNKNOWN",),
                     ("TPL-BACKEND", "TPL-FULLSTACK"), ("TPL-BACKEND", "--json")):
            with self.subTest(args=args):
                result = invoke(ROOT, *args)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("error:", result.stderr)


class FixtureCLITests(unittest.TestCase):
    def setUp(self):
        temp = TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        shutil.copytree(ROOT / "scripts/template_composition_preview",
                        self.root / "scripts/template_composition_preview",
                        ignore=shutil.ignore_patterns("__pycache__"))
        for family in ("readme", "documentation", "workflow"):
            (self.root / "framework/components" / family).mkdir(parents=True)
        self.template = "framework/templates/repositories/backend/metadata.yml"
        self.write(self.template,
                   "id: TPL-BACKEND\nversion: 0.1.0\ncomponents:\n"
                   "  required: [README-EXAMPLE]\n"
                   "  recommended: []\n  optional: [DOC-EXAMPLE]\n")
        self.catalog = "docs/design-system/09_COMPONENT_CATALOG.md"
        self.write(self.catalog, "\n\n".join(
            f"{heading}\n\nRegistry.\n\n{HEADER}\n{SEPARATOR}\n"
            f"| {chr(96)}{prefix}-EXAMPLE{chr(96)} | Example | "
            f"{'Implemented' if prefix == 'README' else 'Conceptual'} |\n\n---"
            for heading, prefix in SECTIONS
        ))
        self.metadata = ("id: README-EXAMPLE\nname: Example\nfamily: README\n"
                         "version: 1.0.0\nstatus: Experimental\n")
        self.physical = "framework/components/readme/example/metadata.yml"
        self.write(self.physical, self.metadata)

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_clean_and_conflicting_reports(self):
        clean = invoke(self.root, "TPL-BACKEND")
        self.assertEqual(clean.returncode, 0, clean.stderr)
        self.assertIn("- README-EXAMPLE | Implemented | Resolved", clean.stdout)
        self.assertIn("- DOC-EXAMPLE | Conceptual | Conceptual", clean.stdout)
        self.assertIn("Counts: Total=0; Resolved=0; Conceptual=0; Unknown=0; Inconsistent=0; Ambiguous=0", clean.stdout)
        self.write("framework/components/readme/another/metadata.yml", self.metadata)
        self.write(self.template,
                   "id: TPL-BACKEND\nversion: 0.1.0\ncomponents:\n"
                   "  required: [README-EXAMPLE, DOC-UNKNOWN]\n"
                   "  recommended: []\n  optional: [DOC-EXAMPLE]\n")
        result = invoke(self.root, "TPL-BACKEND")
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertIn("- README-EXAMPLE | Implemented | Ambiguous", result.stdout)
        self.assertIn("- DOC-UNKNOWN | Not registered | Unknown", result.stdout)
        self.assertIn("Overall: Total=3; Resolved=0; Conceptual=1; Unknown=1; Inconsistent=0; Ambiguous=1", result.stdout)
        self.assertLess(result.stdout.index("readme/another/metadata.yml"),
                        result.stdout.index("readme/example/metadata.yml"))
        (self.root / self.physical).unlink()
        (self.root / self.physical).parent.rmdir()
        (self.root / "framework/components/readme/another/metadata.yml").unlink()
        (self.root / "framework/components/readme/another").rmdir()
        missing = invoke(self.root, "TPL-BACKEND")
        self.assertEqual(missing.returncode, 1, missing.stderr)
        self.assertIn("- README-EXAMPLE | Implemented | Inconsistent", missing.stdout)

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): (
            p.read_bytes() if p.is_file() else None
        ) for p in self.root.rglob("*")}

    def assert_read_only_repeatable(self, expected):
        before = self.snapshot()
        first = invoke(self.root, "TPL-BACKEND")
        second = invoke(self.root, "TPL-BACKEND")
        self.assertEqual(first.returncode, expected, first.stderr)
        self.assertEqual((first.returncode, first.stdout, first.stderr),
                         (second.returncode, second.stdout, second.stderr))
        self.assertEqual(self.snapshot(), before)
        return first

    def test_read_only_success_conflict_and_source_error(self):
        self.assert_read_only_repeatable(0)
        self.write("framework/components/readme/duplicate/metadata.yml", self.metadata)
        self.assert_read_only_repeatable(1)
        self.write(self.template, "id: TPL-BACKEND\nid: TPL-BACKEND\n")
        result = self.assert_read_only_repeatable(2)
        self.assertEqual(result.stdout, "")
        self.assertIn("duplicate YAML key", result.stderr)

    def test_missing_metadata_is_source_error(self):
        (self.root / self.physical).unlink()
        result = self.assert_read_only_repeatable(2)
        self.assertEqual(result.stdout, "")
        self.assertIn("unavailable source", result.stderr)

    def test_source_error_has_no_partial_report(self):
        self.write(self.catalog, "invalid registry")
        result = invoke(self.root, "TPL-BACKEND")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("Source error:", result.stderr)
        self.assertIn(self.catalog, result.stderr)


if __name__ == "__main__":
    unittest.main()
