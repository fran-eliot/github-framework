"""Bounded parser and static audit checks; no evaluation or output writes."""
from pathlib import Path
import unittest

from scripts.repository_generation import GenerationError
from scripts.repository_generation.syntax import (
    EachBlock, IfBlock, Text, Variable, parse, parse_component,
)

ROOT = Path(__file__).resolve().parents[2]
COMPONENTS = (
    ("README-HERO", "hero"), ("README-OVERVIEW", "overview"),
    ("README-FEATURES", "features"), ("README-TECH-STACK", "tech-stack"),
    ("README-QUICK-START", "quick-start"), ("README-DOCUMENTATION", "documentation"),
    ("README-FOOTER", "footer"),
)


class SyntaxTests(unittest.TestCase):
    def test_text_and_variable(self):
        self.assertEqual(parse("A\n{{ overview }}\nB"), (Text("A\n"), Variable("overview"), Text("\nB")))
        self.assertEqual(parse(""), ())

    def test_nested_blocks(self):
        source = "{{#if banner}}{{#if banner.link}}A{{else}}B{{/if}}{{/if}}"
        self.assertEqual(parse_component("README-HERO", source), (
            IfBlock("banner", (IfBlock("banner.link", (Text("A"),), (Text("B"),)),), ()),
        ))

    def test_scalar_iteration(self):
        self.assertEqual(parse_component("README-FEATURES", "{{#each features}}- {{this}}{{/each}}"), (
            EachBlock("features", (Text("- "), Variable("this"))),
        ))

    def test_disabled_visual_scope(self):
        source = "{{#if badges}}{{#each badges}}{{#if link}}{{link}}{{/if}}{{image}}{{alt}}{{/each}}{{/if}}"
        self.assertTrue(parse_component("README-HERO", source))

    def test_malformed_and_unsupported_syntax(self):
        cases = ("{{", "}}", "{{{ name }}}", "{{name}}}", "{{ helper name }}", "{{! comment }}",
                 "{{> partial}}", "{{#unless banner}}x{{/unless}}", "{{#if (name)}}x{{/if}}",
                 "{{#if banner}}", "{{/if}}", "{{else}}", "{{#each features}}{{else}}{{/each}}",
                 "{{#if banner}}{{/each}}", "{{#if banner}}{{else}}{{else}}{{/if}}",
                 "{% if name %}", "{# note #}", "{{name {{other}}", "{{ }}")
        for source in cases:
            with self.subTest(source=source), self.assertRaises(GenerationError):
                parse(source)

    def test_nesting_limit(self):
        with self.assertRaisesRegex(GenerationError, "nesting limit"):
            parse("{{#if banner}}" * 33 + "{{/if}}" * 33)

    def test_scope_failure_in_inactive_branches(self):
        cases = (
            ("README-HERO", "{{#if banner}}{{unknown}}{{/if}}"),
            ("README-HERO", "{{#if banner}}x{{else}}{{unknown}}{{/if}}"),
            ("README-HERO", "{{#each badges}}{{unknown}}{{/each}}"),
            ("README-HERO", "{{#each badges}}{{#if banner}}x{{/if}}{{/each}}"),
            ("README-HERO", "{{image}}"),
            ("README-HERO", "{{#if unknown}}x{{/if}}"),
            ("README-FEATURES", "{{this}}"),
            ("README-FEATURES", "{{#each documents}}{{this}}{{/each}}"),
            ("README-FEATURES", "{{#each features}}{{#each features}}{{this}}{{/each}}{{/each}}"),
            ("README-OVERVIEW", "{{tagline}}"),
            ("DOC-CHANGELOG", "{{overview}}"),
        )
        for identity, source in cases:
            with self.subTest(identity=identity, source=source), self.assertRaises(GenerationError):
                parse_component(identity, source)

    def test_canonical_readme_sources(self):
        for identity, directory in COMPONENTS:
            source = ROOT / "framework/components/readme" / directory / "template.md"
            with self.subTest(identity=identity):
                self.assertTrue(parse_component(identity, source.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
