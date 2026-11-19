"""Destination contracts and injected local write failures."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.repository_generation.assembly import Document
from scripts.repository_generation.destination import (
    DestinationError, validate_destination, write_documents, _write_document,
)

DOCUMENTS = (
    Document("README.md", b"# Example\n"),
    Document("CHANGELOG.md", b"# Changelog\n\n## [Unreleased]\n"),
)
MODULE = "scripts.repository_generation.destination."


class DestinationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.root = self.base / "framework"
        self.root.mkdir()
        self.parent = self.base / "projects"
        self.parent.mkdir()
        self.sentinel = self.root / "sentinel.txt"
        self.sentinel.write_bytes(b"original")

    def test_read_only_check(self):
        target = validate_destination(self.root, self.parent, "sample-backend")
        self.assertEqual(target, self.parent / "sample-backend")
        self.assertEqual(list(self.parent.iterdir()), [])

    def test_exclusive_write_and_repeat(self):
        target = write_documents(self.root, self.parent, "sample", DOCUMENTS)
        self.assertEqual(sorted(p.name for p in target.iterdir()), ["CHANGELOG.md", "README.md"])
        for document in DOCUMENTS:
            self.assertEqual((target / document.name).read_bytes(), document.content)
        with self.assertRaises(DestinationError):
            write_documents(self.root, self.parent, "sample", DOCUMENTS)
        self.assertEqual(self.sentinel.read_bytes(), b"original")
        for document in DOCUMENTS:
            self.assertEqual((target / document.name).read_bytes(), document.content)

    def test_invalid_names(self):
        for name in ("", ".", "..", "../other", "a/b", r"a\b", "C:foo", "A", "1a",
                     "a-", "-a", "a b", "a.txt", "a_", "á", "a"*64,
                     "con", "prn", "aux", "nul", "com1", "lpt9"):
            with self.subTest(name=name), self.assertRaises(DestinationError):
                validate_destination(self.root, self.parent, name)
        for name in ("a", "a1", "a-b", "a"*63):
            self.assertEqual(validate_destination(self.root, self.parent, name).name, name)

    def test_invalid_parents_and_source_tree(self):
        nested = self.root / "nested"
        nested.mkdir()
        for parent in (self.root, nested, self.sentinel, self.parent / "missing",
                       self.parent / ".." / "projects"):
            with self.subTest(parent=parent), self.assertRaises(DestinationError):
                validate_destination(self.root, parent, "sample")
        self.assertEqual(self.sentinel.read_bytes(), b"original")

    def test_existing_file_and_directory(self):
        (self.parent / "file").write_bytes(b"keep")
        (self.parent / "directory").mkdir()
        sentinel = self.parent / "directory" / "keep.txt"
        sentinel.write_bytes(b"keep")
        for name in ("file", "directory"):
            with self.subTest(name=name), self.assertRaises(DestinationError):
                write_documents(self.root, self.parent, name, DOCUMENTS)
        self.assertEqual((self.parent / "file").read_bytes(), b"keep")
        self.assertEqual(sentinel.read_bytes(), b"keep")

    def test_linked_parent_and_existing_links(self):
        link = self.base / "linked"
        try:
            link.symlink_to(self.parent, target_is_directory=True)
        except OSError as exc:
            self.skipTest(f"symbolic links unavailable: {exc}")
        (self.parent / "dangling").symlink_to(self.base / "missing")
        (self.parent / "existing").symlink_to(self.sentinel)
        for parent, name in ((link, "child"), (self.parent, "dangling"),
                             (self.parent, "existing")):
            with self.subTest(parent=parent, name=name), self.assertRaises(DestinationError):
                validate_destination(self.root, parent, name)
        self.assertEqual(self.sentinel.read_bytes(), b"original")

    def test_invalid_documents_leave_no_destination(self):
        for documents in (DOCUMENTS[:1], tuple(reversed(DOCUMENTS)),
                          (Document("../escape.md", b"x\n"), DOCUMENTS[1]),
                          (Document("README.md", b"x\r\n"), DOCUMENTS[1]),
                          (Document("README.md", b"\xff\n"), DOCUMENTS[1])):
            with self.subTest(documents=documents), self.assertRaises(DestinationError):
                write_documents(self.root, self.parent, "sample", documents)
        self.assertFalse((self.parent / "sample").exists())

    def test_injected_second_write_failure_retains_owned_output(self):
        def fail(path, content):
            if path.name == "CHANGELOG.md":
                raise OSError("injected write failure")
            _write_document(path, content)
        with patch(MODULE + "_write_document", side_effect=fail):
            with self.assertRaises(DestinationError) as caught:
                write_documents(self.root, self.parent, "sample", DOCUMENTS)
        target = self.parent / "sample"
        self.assertEqual(caught.exception.incomplete_path, target)
        self.assertEqual((target / "README.md").read_bytes(), DOCUMENTS[0].content)
        self.assertFalse((target / "CHANGELOG.md").exists())
        self.assertEqual(self.sentinel.read_bytes(), b"original")

    def test_injected_verification_failure(self):
        def corrupt(path, content):
            _write_document(path, b"different\n")
        with patch(MODULE + "_write_document", side_effect=corrupt):
            with self.assertRaisesRegex(DestinationError, "written content mismatch") as caught:
                write_documents(self.root, self.parent, "sample", DOCUMENTS)
        self.assertEqual(caught.exception.incomplete_path, self.parent / "sample")

    def test_exclusive_file_collision(self):
        path = self.parent / "README.md"
        path.write_bytes(b"keep")
        with self.assertRaises(FileExistsError):
            _write_document(path, b"replacement")
        self.assertEqual(path.read_bytes(), b"keep")

    def test_directory_creation_failure_has_no_owned_path(self):
        with patch.object(Path, "mkdir", side_effect=PermissionError("injected")):
            with self.assertRaises(DestinationError) as caught:
                write_documents(self.root, self.parent, "sample", DOCUMENTS)
        self.assertIsNone(caught.exception.incomplete_path)
        self.assertFalse((self.parent / "sample").exists())


if __name__ == "__main__":
    unittest.main()
