"""Pure composition resolution contracts and evidence preservation."""

import unittest

from scripts.template_composition_preview.registry import RegistrySource
from scripts.template_composition_preview.resolution import (
    OUTCOMES, resolve_composition, resolve_reference,
)
from scripts.template_composition_preview.sources import PhysicalSource, TemplateSource


def physical(identity, folder="example", version="1.0.0"):
    return PhysicalSource(
        identity, "Example", version, "Experimental",
        f"framework/components/readme/{folder}/metadata.yml",
    )


class ResolutionTests(unittest.TestCase):
    def test_nine_resolution_combinations(self):
        identity = "README-EXAMPLE"
        cases = (
            ("Implemented", 0, "Inconsistent", "Missing implementation evidence"),
            ("Implemented", 1, "Resolved", "Matching physical metadata identity"),
            ("Implemented", 2, "Ambiguous", "Multiple physical metadata identities"),
            ("Conceptual", 0, "Conceptual", "Explicit Conceptual classification; no physical match"),
            ("Conceptual", 1, "Inconsistent", "Classification and implementation disagree"),
            ("Conceptual", 2, "Ambiguous", "Multiple physical metadata identities"),
            (None, 0, "Unknown", "No registry or physical evidence"),
            (None, 1, "Inconsistent", "Missing registry entry"),
            (None, 2, "Ambiguous", "Multiple physical metadata identities"),
        )
        for classification, count, expected, reason in cases:
            with self.subTest(classification=classification, count=count):
                record = (RegistrySource(identity, classification, "40. README Component Registry")
                          if classification else None)
                matches = tuple(physical(identity, str(i)) for i in range(count))
                result = resolve_reference(identity, "required", record, matches)
                self.assertEqual(result.id, identity)
                self.assertEqual(result.level, "required")
                self.assertEqual(result.outcome, expected)
                self.assertEqual(result.reason, reason)
                self.assertEqual(result.registry, record)
                self.assertEqual(result.physical, matches)

    def test_order_counts_and_evidence(self):
        template = TemplateSource("TPL-BACKEND", "0.1.0", "template/metadata.yml", (
            ("required", ("README-Z", "README-A")),
            ("recommended", ()),
            ("optional", ("README-B", "README-C", "README-D")),
        ))
        registry = {
            "README-A": RegistrySource("README-A", "Conceptual", "section A"),
            "README-Z": RegistrySource("README-Z", "Implemented", "section Z"),
            "README-B": RegistrySource("README-B", "Implemented", "section B"),
            "README-D": RegistrySource("README-D", "Implemented", "section D"),
            "README-OTHER": RegistrySource("README-OTHER", "Implemented", "unselected"),
        }
        matches = {
            "README-Z": (physical("README-Z"),),
            "README-D": (physical("README-D", "z", "2.0.0"), physical("README-D", "a")),
            "README-OTHER": (physical("README-OTHER"),),
        }
        result = resolve_composition(template, registry, matches)
        self.assertEqual(result.template, template)
        self.assertEqual([g.level for g in result.groups], ["required", "recommended", "optional"])
        self.assertEqual([r.id for r in result.groups[0].references], ["README-Z", "README-A"])
        self.assertEqual([r.id for r in result.groups[2].references], ["README-B", "README-C", "README-D"])
        self.assertEqual(result.groups[1].references, ())
        self.assertEqual(result.groups[1].counts, dict.fromkeys(OUTCOMES, 0))
        self.assertEqual(result.groups[0].counts, dict(zip(OUTCOMES, (1, 1, 0, 0, 0))))
        self.assertEqual(result.groups[2].counts, dict(zip(OUTCOMES, (0, 0, 1, 1, 1))))
        self.assertEqual(result.counts, dict.fromkeys(OUTCOMES, 1))
        self.assertEqual(tuple(result.counts), OUTCOMES)
        self.assertTrue(result.has_conflicts)
        ambiguous = result.groups[2].references[-1]
        self.assertEqual(ambiguous.physical, tuple(reversed(matches["README-D"])))
        self.assertEqual(ambiguous.registry.section, "section D")
        self.assertEqual(result, resolve_composition(template, registry, matches))
        self.assertEqual(result, resolve_composition(
            template, dict(reversed(list(registry.items()))),
            {key: tuple(reversed(value)) for key, value in reversed(list(matches.items()))},
        ))

    def test_required_conceptual_is_not_conflict(self):
        identity = "README-LICENSE"
        template = TemplateSource("TPL-DOCUMENTATION", "0.1.0", "template/metadata.yml", (
            ("required", (identity,)), ("recommended", ()), ("optional", ()),
        ))
        registry = {identity: RegistrySource(identity, "Conceptual", "40. README Component Registry")}
        result = resolve_composition(template, registry, {})
        reference = result.groups[0].references[0]
        self.assertEqual(reference.outcome, "Conceptual")
        self.assertEqual(reference.physical, ())
        self.assertEqual(reference.registry, registry[identity])
        self.assertFalse(result.has_conflicts)
        self.assertEqual(result.counts["Conceptual"], 1)
        changed = resolve_composition(template, {
            identity: RegistrySource(identity, "Implemented", "40. README Component Registry")
        }, {})
        self.assertTrue(changed.has_conflicts)
        self.assertEqual(changed.counts["Inconsistent"], 1)

    def test_empty_composition(self):
        template = TemplateSource("TPL-BACKEND", "0.1.0", "template/metadata.yml", (
            ("required", ()), ("recommended", ()), ("optional", ()),
        ))
        result = resolve_composition(template, {}, {})
        self.assertEqual(result.counts, dict.fromkeys(OUTCOMES, 0))
        self.assertFalse(result.has_conflicts)
