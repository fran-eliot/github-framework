"""Document assembly checks on the canonical library; no destination writes."""
from dataclasses import replace
from hashlib import sha256
import json
from pathlib import Path
import unittest

from scripts.repository_generation import GenerationError
from scripts.repository_generation.assembly import assemble
from scripts.repository_generation.composition import load_composition
from scripts.repository_generation.inputs import parse_project_input
from test_inputs import fixture

ROOT = Path(__file__).resolve().parents[2]


class AssemblyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.composition = load_composition(ROOT, "TPL-BACKEND", "0.1.0")

    def build(self, **changes):
        return assemble(self.composition, parse_project_input(json.dumps({**fixture(), **changes})))

    def test_two_documents_and_order(self):
        readme, changelog = self.build()
        self.assertEqual((readme.name, changelog.name), ("README.md", "CHANGELOG.md"))
        text = readme.content.decode("utf-8")
        headings = ('<h1 align="center">', "## 📖 Overview", "## ✨ Features",
                    "## 🛠 Tech Stack", "## 🚀 Quick Start", "## 📚 Documentation", "Documentation seed.")
        positions = [text.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(changelog.content, b"# Changelog\n\n## [Unreleased]\n")

    def test_deterministic_utf8_lf_and_digests(self):
        first = self.build(footer="Información útil\r\n\r\n{{ literal }}")
        self.assertEqual(first, self.build(footer="Información útil\n\n{{ literal }}"))
        for document in first:
            self.assertTrue(document.content.endswith(b"\n"))
            self.assertNotIn(b"\r", document.content)
            self.assertEqual(document.digest, sha256(document.content).hexdigest())
        self.assertIn("Información útil\n\n{{ literal }}".encode("utf-8"), first[0].content)

    def test_single_title_and_html_escaping(self):
        readme, _ = self.build(project_name="A <h1> B")
        self.assertEqual(readme.content.count(b"<h1 "), 1)
        self.assertIn(b"A &lt;h1&gt; B", readme.content)

    def test_reject_extra_headings(self):
        for content in ("# Extra", "Extra\n===", "<H1>Extra</H1>", "> # Extra", "- # Extra"):
            with self.subTest(content=content), self.assertRaises(GenerationError):
                self.build(footer=content)
        for changes in ({"features": ["# Extra"]}, {"unreleased_changes": {"Added": ["<h1>Extra</h1>"]}}):
            with self.subTest(changes=changes), self.assertRaises(GenerationError):
                self.build(**changes)

    def test_preserve_closed_fenced_examples(self):
        for fence in (chr(96)*3, "~~~"):
            example = f"{fence}markdown\n# Example\nTitle\n===\n<h1>Example</h1>\n{fence}"
            with self.subTest(fence=fence):
                readme, _ = self.build(footer=example)
                self.assertIn(example.encode(), readme.content)

    def test_reject_unclosed_fences(self):
        with self.assertRaisesRegex(GenerationError, "unclosed"):
            self.build(footer="~~~markdown\n# Example")

    def test_selection_and_canonical_section_drift(self):
        project = parse_project_input(json.dumps(fixture()))
        selected = self.composition.selected
        altered = replace(selected[1], template=selected[1].template.replace("Overview", "Different"))
        for items in (selected[:-1], tuple(reversed(selected)), (selected[0], altered, *selected[2:])):
            with self.subTest(items=len(items)), self.assertRaises(GenerationError):
                assemble(replace(self.composition, selected=items), project)

    def test_changelog_changes_are_separate(self):
        readme, changelog = self.build(unreleased_changes={"Added": ["Initial documentation"]})
        self.assertNotIn(b"Initial documentation", readme.content)
        self.assertEqual(changelog.content, b"# Changelog\n\n## [Unreleased]\n\n### Added\n\n- Initial documentation\n")


if __name__ == "__main__":
    unittest.main()
