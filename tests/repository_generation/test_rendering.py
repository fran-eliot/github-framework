"""Verify canonical rendering policies independently of destination writes."""
from dataclasses import replace
import json
from pathlib import Path
import unittest

from scripts.repository_generation import GenerationError
from scripts.repository_generation.composition import load_composition
from scripts.repository_generation.inputs import parse_project_input
from scripts.repository_generation.rendering import render_component
from test_inputs import fixture

ROOT = Path(__file__).resolve().parents[2]


class RenderingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        composition = load_composition(ROOT, "TPL-BACKEND", "0.1.0")
        cls.components = {c.id: c for c in composition.selected}

    def render(self, identity, **changes):
        project = parse_project_input(json.dumps({**fixture(), **changes}))
        return render_component(self.components[identity], project)

    def test_all_required_components_render(self):
        for identity in self.components:
            with self.subTest(identity=identity):
                self.assertTrue(self.render(identity).strip())

    def test_hero_escapes_html_and_disables_visual_blocks(self):
        output = self.render("README-HERO", project_name='A & <B> "C"', alignment="left",
                             short_description="A <description> & more")
        self.assertIn('<h1 align="left">', output)
        self.assertIn("A &amp; &lt;B&gt; &quot;C&quot;", output)
        self.assertIn("A &lt;description&gt; &amp; more", output)
        for forbidden in ("<img", "<a href", "<!--", "{{"):
            self.assertNotIn(forbidden, output)
        self.assertNotIn("short_description", self.render("README-HERO"))

    def test_literal_markdown_and_no_recursive_expansion(self):
        output = self.render("README-FOOTER", footer="A\n\n\nB\n\n{{ project_name }}")
        self.assertIn("A\n\n\nB\n\n{{ project_name }}", output)

    def test_ordered_lists(self):
        for identity, field in (("README-FEATURES", "features"),
                                ("README-TECH-STACK", "technologies"),
                                ("README-DOCUMENTATION", "documents")):
            with self.subTest(identity=identity):
                output = self.render(identity, **{field: ["Z **first**", "A second"]})
                self.assertLess(output.index("- Z **first**"), output.index("- A second"))

    def test_quick_start_substitutions(self):
        output = self.render("README-QUICK-START", prerequisites="Need A",
                             installation="Install B", execution="Run C")
        for expected in ("### Prerequisites\n\nNeed A", "### Installation\n\nInstall B", "### Run\n\nRun C"):
            self.assertIn(expected, output)

    def test_changelog_empty(self):
        self.assertEqual(self.render("DOC-CHANGELOG"), "# Changelog\n\n## [Unreleased]\n")

    def test_changelog_supplied_changes(self):
        output = self.render("DOC-CHANGELOG", unreleased_changes={
            "Fixed": ["Fix B"], "Added": ["Add A", "Literal <CHANGE_DESCRIPTION>"],
        })
        self.assertEqual(output, "# Changelog\n\n## [Unreleased]\n\n### Added\n\n- Add A\n- Literal <CHANGE_DESCRIPTION>\n\n### Fixed\n\n- Fix B\n")

    def test_unsupported_source_changes(self):
        project = parse_project_input(json.dumps(fixture()))
        hero = self.components["README-HERO"]
        changelog = self.components["DOC-CHANGELOG"]
        cases = (
            replace(hero, version="2.0.0"),
            replace(hero, template=hero.template + "{{#if banner}}{{unknown}}{{/if}}"),
            replace(hero, template=hero.template + "{{banner.source}}"),
            replace(hero, template=" "),
            replace(changelog, template=changelog.template.replace("Unreleased", "Next")),
            replace(changelog, template=changelog.template + "\n{{unknown}}"),
        )
        for altered in cases:
            with self.subTest(identity=altered.id, version=altered.version), self.assertRaises(GenerationError):
                render_component(altered, project)

    def test_newline_normalization_and_repeatability(self):
        project = parse_project_input(json.dumps(fixture()))
        for component in self.components.values():
            with self.subTest(identity=component.id):
                original = render_component(component, project)
                self.assertEqual(original, render_component(component, project))
                windows = replace(component, template=component.template.replace("\n", "\r\n"))
                self.assertEqual(original, render_component(windows, project))
                self.assertNotIn("\r", original)


    def test_canonical_list_spacing_is_compact_and_ordered(self):
        for identity, field, heading in (
            ("README-FEATURES", "features", "## ✨ Features"),
            ("README-DOCUMENTATION", "documents", "## 📚 Documentation"),
        ):
            with self.subTest(identity=identity):
                rendered = self.render(identity, **{field: ["First **bold**", "Second literal"]})
                self.assertEqual(rendered,
                                 f"{heading}\n\n- First **bold**\n- Second literal\n")
                self.assertNotIn("\n\n\n", rendered)

    def test_canonical_list_source_drift_is_rejected(self):
        project = parse_project_input(json.dumps(fixture()))
        for identity in ("README-FEATURES", "README-DOCUMENTATION"):
            original = self.components[identity]
            altered = replace(original, template=original.template.replace(
                "\n\n- {{ this }}", "\n- {{ this }}"
            ))
            with self.subTest(identity=identity), self.assertRaisesRegex(
                GenerationError, "unsupported list whitespace structure"
            ):
                render_component(altered, project)

    def test_hero_removes_only_template_owned_blank_separators(self):
        for description in ("", "A literal {{ variable }} & <tag>"):
            with self.subTest(description=description):
                hero = self.render("README-HERO", short_description=description)
                self.assertNotIn("\n\n\n", hero)
                self.assertIn('<h1 align="center">', hero)
                if description:
                    self.assertIn("A literal {{ variable }} &amp; &lt;tag&gt;", hero)
                self.assertNotIn("<img", hero)

    def test_author_multiline_markdown_and_literal_fragments_unchanged(self):
        literal = "Author paragraph\n\n\nNext paragraph\n\n{{#each untouched}}\n:end"
        output = self.render("README-FOOTER", footer=literal)
        self.assertIn(literal, output)
        overview = self.render("README-OVERVIEW", overview=(
            "A deliberately long authored description with preserved spacing "
            "and ordinary project details to satisfy the strict minimum length."
            "\n\n\nA second paragraph."
        ))
        self.assertIn("\n\n\nA second paragraph.", overview)


if __name__ == "__main__":
    unittest.main()
