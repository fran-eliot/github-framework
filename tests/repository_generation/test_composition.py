"""Canonical and isolated negative checks for composition preflight."""
from dataclasses import replace
from pathlib import Path
import unittest
from unittest.mock import patch

from scripts.repository_generation import GenerationError
from scripts.repository_generation.composition import load_composition
from scripts.repository_generation.profile import REQUIRED
from scripts.template_composition_preview import SourceError
from scripts.template_composition_preview.registry import load_registry
from scripts.template_composition_preview.sources import discover_physical, load_mapping, load_template, read_text

ROOT = Path(__file__).resolve().parents[2]
MODULE = "scripts.repository_generation.composition."
HERO = "framework/components/readme/hero/metadata.yml"


class CompositionTests(unittest.TestCase):
    def load(self):
        return load_composition(ROOT, "TPL-BACKEND", "0.1.0")

    def test_canonical_profile(self):
        result = self.load()
        self.assertEqual(tuple((c.id, c.version) for c in result.selected),
                         tuple((identity, version) for identity, version, _ in REQUIRED))
        self.assertEqual(result.resolution.counts,
                         dict(Resolved=16, Conceptual=12, Unknown=0, Inconsistent=0, Ambiguous=0))
        self.assertEqual([(d.owner, d.id, d.level, d.outcome) for d in result.dependencies], [
            ("README-HERO", "VCL-HERO", "required", "Conceptual"),
            ("README-HERO", "VCL-BANNER", "recommended", "Conceptual"),
            ("README-HERO", "VCL-BADGES", "recommended", "Conceptual"),
            ("README-OVERVIEW", "README-HERO", "recommended", "Resolved"),
        ])
        self.assertIn("not full Template conformance", result.dependencies[0].note)
        for component in result.selected:
            self.assertEqual(component.template, read_text(ROOT, component.artifact_path))

    def test_invalid_requested_profile(self):
        with self.assertRaises(GenerationError):
            load_composition(ROOT, "TPL-FULLSTACK", "0.1.0")

    def test_template_drift(self):
        template = load_template(ROOT, "TPL-BACKEND")
        for altered in (
            replace(template, version="9.0.0"),
            replace(template, references=(("required", tuple(reversed(template.references[0][1]))),
                                          *template.references[1:])),
        ):
            with self.subTest(altered=altered), patch(MODULE + "load_template", return_value=altered):
                with self.assertRaises(GenerationError):
                    self.load()

    def test_conflict_even_when_unselected(self):
        registry = load_registry(ROOT)
        for identity in ("README-HERO", "README-CONTRIBUTING"):
            altered = {k: v for k, v in registry.items() if k != identity}
            with self.subTest(identity=identity), patch(MODULE + "load_registry", return_value=altered):
                with self.assertRaisesRegex(GenerationError, identity):
                    self.load()

    def test_selected_conceptual(self):
        registry, physical = load_registry(ROOT), discover_physical(ROOT)
        registry["README-HERO"] = replace(registry["README-HERO"], classification="Conceptual")
        del physical["README-HERO"]
        with patch(MODULE + "load_registry", return_value=registry), patch(MODULE + "discover_physical", return_value=physical):
            with self.assertRaisesRegex(GenerationError, "selected reference is Conceptual"):
                self.load()

    def test_selected_identity_drift(self):
        for field, value in (("version", "2.0.0"), ("path", "elsewhere/metadata.yml")):
            physical = discover_physical(ROOT)
            physical["README-HERO"] = (replace(physical["README-HERO"][0], **{field: value}),)
            with self.subTest(field=field), patch(MODULE + "discover_physical", return_value=physical):
                with self.assertRaisesRegex(GenerationError, "unsupported selected path or version"):
                    self.load()

    def test_source_errors_and_empty_artifacts(self):
        for module, effect in (("read_text", SourceError("missing artifact")),
                               ("load_mapping", SourceError("unreadable metadata"))):
            with self.subTest(module=module), patch(MODULE + module, side_effect=effect):
                with self.assertRaisesRegex(GenerationError, "composition source error"):
                    self.load()
        with patch(MODULE + "read_text", return_value=" \n"):
            with self.assertRaisesRegex(GenerationError, "empty canonical artifact"):
                self.load()

    def test_dependency_policy(self):
        cases = [
            ([{"id": "VCL-HERO", "minimum_version": "2.0.0"}], "required dependency VCL-HERO"),
            ([{"id": "VCL-BANNER", "minimum_version": "1.0.0"}], "required dependency VCL-BANNER"),
            ([{"id": "README-MISSING", "minimum_version": "1.0.0"}], "Unknown"),
            ([{"id": "README-OVERVIEW", "minimum_version": "9.0.0"}], "VersionMismatch"),
            ([{"id": "README-HERO", "minimum_version": "1.0.0"}], "self or duplicate"),
            ([{"id": "VCL-HERO", "minimum_version": "invalid"}], "unsupported dependency version"),
            ([], "named VCL-HERO limitation"),
        ]
        for dependencies, message in cases:
            def altered(root, path):
                metadata = load_mapping(root, path)
                if path == HERO:
                    metadata["dependencies"] = {"required": dependencies}
                return metadata
            with self.subTest(dependencies=dependencies), patch(MODULE + "load_mapping", side_effect=altered):
                with self.assertRaisesRegex(GenerationError, message):
                    self.load()


if __name__ == "__main__":
    unittest.main()
