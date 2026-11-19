"""Replay the public generation example through the real standalone CLI."""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "framework/generation/examples/backend-project.json"
ARTIFACTS = ("README.md", "CHANGELOG.md")


def snapshot():
    paths = sorted(p for p in (ROOT / "framework").rglob("*") if p.is_file())
    return {p.relative_to(ROOT).as_posix(): sha256(p.read_bytes()).hexdigest() for p in paths}


class PublicExampleTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.parent = Path(temporary.name).resolve()
        self.before = snapshot()
        self.addCleanup(self.assert_sources_unchanged)

    def assert_sources_unchanged(self):
        self.assertEqual(snapshot(), self.before)

    def invoke(self, mode, name="atlas-sample", source=EXAMPLE,
               template="TPL-BACKEND", version="0.1.0"):
        return subprocess.run(
            [sys.executable, "-B", "-m", "scripts.repository_generation",
             mode, template, "--template-version", version, "--input", str(source),
             "--output-parent", str(self.parent), "--name", name],
            cwd=ROOT, capture_output=True, encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            check=False, timeout=30,
        )

    def success(self, result):
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout.count(" | Selected\n"), 8)
        self.assertEqual(result.stdout.count(" | Unselected\n"), 20)
        self.assertIn("VCL-HERO", result.stdout)
        self.assertIn("not full Template conformance", result.stdout)

    def failure(self, result, code):
        self.assertEqual(result.returncode, code, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertTrue(result.stderr)

    def read_documents(self, name):
        target = self.parent / name
        self.assertEqual(sorted(p.name for p in target.iterdir()), sorted(ARTIFACTS))
        documents = {filename: (target / filename).read_bytes() for filename in ARTIFACTS}
        for content in documents.values():
            content.decode("utf-8")
            self.assertNotIn(b"\r", content)
            self.assertTrue(content.endswith(b"\n"))
        return documents

    def test_public_plan_generate_and_repeated_bytes(self):
        # E2E-01 through E2E-04; E2E-09 is checked by cleanup.
        plan = self.invoke("plan")
        self.success(plan)
        self.assertIn("Plan complete; no destination writes.", plan.stdout)
        self.assertEqual(list(self.parent.iterdir()), [])
        first = self.invoke("generate")
        self.success(first)
        self.assertIn("Generation complete.", first.stdout)
        a = self.read_documents("atlas-sample")
        second = self.invoke("generate", name="atlas-repeat")
        self.success(second)
        b = self.read_documents("atlas-repeat")
        self.assertEqual(a, b)
        for filename, content in a.items():
            digest = sha256(content).hexdigest()
            for result, name in ((plan, "atlas-sample"), (first, "atlas-sample"),
                                 (second, "atlas-repeat")):
                expected = f"{self.parent / name / filename} | SHA-256: {digest}"
                self.assertIn(expected, result.stdout)
            print(f"PUBLIC_EXAMPLE_SHA256 {filename} {digest}", flush=True)
        readme = a["README.md"].decode("utf-8")
        headings = ("<h1 align=", "## 📖 Overview", "## ✨ Features",
                    "## 🛠 Tech Stack", "## 🚀 Quick Start", "## 📚 Documentation",
                    "Synthetic example for GitHub Framework.")
        positions = [readme.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("Atlas Sample API", readme)
        self.assertIn("No application execution is available.", readme)
        self.assertEqual(a["CHANGELOG.md"],
                         b"# Changelog\n\n## [Unreleased]\n\n### Added\n\n- Initial documentation seed for the fictional project.\n")

    def test_existing_destination_preserved(self):
        # E2E-05
        self.success(self.invoke("generate"))
        before = self.read_documents("atlas-sample")
        for mode in ("plan", "generate"):
            with self.subTest(mode=mode):
                self.failure(self.invoke(mode), 1)
                self.assertEqual(self.read_documents("atlas-sample"), before)

    def test_unsupported_template_and_version(self):
        # E2E-06
        for mode in ("plan", "generate"):
            for template, version in (("TPL-FULLSTACK", "0.1.0"),
                                      ("TPL-BACKEND", "9.9.9")):
                with self.subTest(mode=mode, template=template, version=version):
                    self.failure(self.invoke(mode, template=template, version=version), 2)
        self.assertEqual(list(self.parent.iterdir()), [])

    def test_invalid_json_and_visual_input(self):
        # E2E-07 and E2E-08
        input_file = self.parent / "invalid.json"
        sample = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        cases = ("{", '{"project_name":"A","project_name":"B"}',
                 json.dumps({**sample, "banner": {"source": "example.png"}}),
                 json.dumps({**sample, "badges": []}))
        for raw in cases:
            input_file.write_text(raw, encoding="utf-8")
            for mode in ("plan", "generate"):
                with self.subTest(mode=mode, raw=raw[:60]):
                    self.failure(self.invoke(mode, source=input_file), 2)
                    self.assertEqual(list(self.parent.iterdir()), [input_file])


if __name__ == "__main__":
    unittest.main()
