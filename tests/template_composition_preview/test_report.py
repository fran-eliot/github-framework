"""Rendering contracts for complete composition evidence."""

import unittest

from scripts.template_composition_preview.registry import RegistrySource
from scripts.template_composition_preview.report import render_report
from scripts.template_composition_preview.resolution import resolve_composition
from scripts.template_composition_preview.sources import PhysicalSource, TemplateSource


class ReportTests(unittest.TestCase):
    def test_order_evidence_counts_and_limitations(self):
        template = TemplateSource(
            "TPL-BACKEND", "0.1.0",
            "framework/templates/repositories/backend/metadata.yml",
            (("required", ("README-Z", "README-A")),
             ("recommended", ()), ("optional", ("DOC-UNKNOWN",))),
        )
        registry = {
            "README-Z": RegistrySource("README-Z", "Implemented", "40. README Component Registry"),
            "README-A": RegistrySource("README-A", "Conceptual", "40. README Component Registry"),
        }
        physical = {"README-Z": (
            PhysicalSource("README-Z", "Z", "2.0.0", "Stable",
                           "framework/components/readme/z/metadata.yml"),
            PhysicalSource("README-Z", "Z", "1.0.0", "Experimental",
                           "framework/components/readme/a/metadata.yml"),
        )}
        result = resolve_composition(template, registry, physical)
        text = render_report(result)
        self.assertEqual(text, render_report(result))
        self.assertLess(text.index("[required]"), text.index("[recommended]"))
        self.assertLess(text.index("[recommended]"), text.index("[optional]"))
        self.assertLess(text.index("- README-Z"), text.index("- README-A"))
        self.assertLess(text.index("readme/a/metadata.yml"), text.index("readme/z/metadata.yml"))
        self.assertIn("version=1.0.0 | status=Experimental", text)
        self.assertIn("version=2.0.0 | status=Stable", text)
        self.assertIn("40. README Component Registry", text)
        self.assertIn("- DOC-UNKNOWN | Not registered | Unknown", text)
        self.assertIn("Registry: no entry", text)
        self.assertIn("Metadata: no physical match", text)
        self.assertIn("[recommended]\nCounts: Total=0; Resolved=0; Conceptual=0; Unknown=0; Inconsistent=0; Ambiguous=0", text)
        self.assertIn("Overall: Total=3; Resolved=0; Conceptual=1; Unknown=1; Inconsistent=0; Ambiguous=1", text)
        self.assertIn("completeness is not guaranteed", text)
        self.assertIn("No consumer is assessed.", text)
        self.assertTrue(text.endswith("\n"))
