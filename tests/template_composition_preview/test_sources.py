"""Source acquisition contracts and filesystem failure cases."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from scripts.template_composition_preview import SourceError
from scripts.template_composition_preview.sources import (
    discover_physical, load_mapping, load_template,
)


class SourceTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for family in ("readme", "documentation", "workflow"):
            (self.root / "framework/components" / family).mkdir(parents=True)
        self.template = "framework/templates/repositories/backend/metadata.yml"
        self.valid = (
            "id: TPL-BACKEND\nversion: 0.1.0\ncomponents:\n"
            "  required: [README-HERO, DOC-API]\n"
            "  recommended: []\n  optional: [VCL-HERO]\n"
        )
        self.write(self.template, self.valid)
        self.component = "framework/components/readme/not-the-id/metadata.yml"
        self.metadata = (
            "id: README-HERO\nname: Hero\nversion: 1.0.0\n"
            "status: Stable\nfamily: README\n"
        )
        self.write(self.component, self.metadata)

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes()
                for p in self.root.rglob("*") if p.is_file()}

    def test_template_order_and_empty_level(self):
        before = self.snapshot()
        result = load_template(self.root, "TPL-BACKEND")
        self.assertEqual(result.references, (
            ("required", ("README-HERO", "DOC-API")),
            ("recommended", ()), ("optional", ("VCL-HERO",)),
        ))
        self.assertEqual(result.path, self.template)
        self.assertEqual(result.version, "0.1.0")
        self.assertEqual(before, self.snapshot())

    def test_invalid_templates(self):
        for text in (
            self.valid + "id: TPL-BACKEND\n",
            self.valid.replace("TPL-BACKEND", "TPL-FULLSTACK"),
            self.valid.replace("0.1.0", "42"),
            self.valid.replace("recommended: []", "recommended: null"),
            self.valid.replace("  recommended: []\n", ""),
            self.valid.replace("VCL-HERO", "README-HERO"),
            self.valid.replace("DOC-API", "README-HERO"),
            self.valid.replace("DOC-API", "bad"),
            self.valid.replace("DOC-API", "42"),
            self.valid.replace("[README-HERO, DOC-API]", "["),
            self.valid.replace("  optional:", "  required:"),
            "[]\n",
        ):
            with self.subTest(text=text):
                self.write(self.template, text)
                before = self.snapshot()
                with self.assertRaises(SourceError):
                    load_template(self.root, "TPL-BACKEND")
                self.assertEqual(before, self.snapshot())

    def test_runtime_identity_and_duplicate_matches(self):
        duplicate = "framework/components/readme/another/metadata.yml"
        self.write(duplicate, self.metadata)
        before = self.snapshot()
        matches = discover_physical(self.root)
        self.assertEqual(list(matches), ["README-HERO"])
        self.assertEqual([r.path for r in matches["README-HERO"]],
                         [duplicate, self.component])
        self.assertEqual(discover_physical(self.root), matches)
        self.assertEqual(before, self.snapshot())

    def test_invalid_physical_metadata(self):
        for metadata in (
            self.metadata.replace("family: README", "family: Documentation"),
            self.metadata.replace("README-HERO", "DOC-HERO"),
            self.metadata.replace("name: Hero", "name: null"),
            self.metadata.replace("version: 1.0.0", "version: false"),
            self.metadata.replace("status: Stable\n", ""),
            self.metadata + "id: README-HERO\n",
        ):
            with self.subTest(metadata=metadata):
                self.write(self.component, metadata)
                with self.assertRaises(SourceError):
                    discover_physical(self.root)

    def test_missing_metadata_and_family(self):
        (self.root / self.component).unlink()
        with self.assertRaises(SourceError):
            discover_physical(self.root)
        self.write(self.component, self.metadata)
        (self.root / "framework/components/workflow").rmdir()
        with self.assertRaises(SourceError):
            discover_physical(self.root)

    def test_unsupported_visual(self):
        (self.root / "framework/components/visual").mkdir()
        with self.assertRaisesRegex(SourceError, "unsupported physical Visual"):
            discover_physical(self.root)

    def test_unreadable_file(self):
        with patch.object(Path, "read_text", side_effect=PermissionError("denied")):
            with self.assertRaisesRegex(SourceError, "unreadable source"):
                load_mapping(self.root, self.template)

    def test_symlink_metadata(self):
        target = self.root / self.component
        target.unlink()
        try:
            target.symlink_to(self.root / self.template)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"symbolic links unavailable: {exc}")
        with self.assertRaisesRegex(SourceError, "linked"):
            discover_physical(self.root)

    def test_real_sources(self):
        root = Path(__file__).resolve().parents[2]
        for identity in ("TPL-BACKEND", "TPL-FULLSTACK", "TPL-DOCUMENTATION"):
            self.assertEqual(load_template(root, identity).id, identity)
        physical = discover_physical(root)
        self.assertIn("README-HERO", physical)
        self.assertIn("DOC-ARCHITECTURE", physical)
        self.assertIn("WCL-BRANCH", physical)
