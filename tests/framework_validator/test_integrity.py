"""Unit tests for the read-only Component integrity digest helpers."""

import hashlib
import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch

from scripts.framework_validator.integrity import (
    component_content_sha256,
    metadata_sha256,
)


class ComponentIntegrityTests(unittest.TestCase):
    def test_metadata_digest_hashes_exact_bytes_and_handles_absence(self) -> None:
        with TemporaryDirectory() as directory:
            metadata = Path(directory) / "metadata.yml"
            self.assertIsNone(metadata_sha256(metadata))
            raw = b"version: 0.1.0\r\ndescription: cafe\n"
            metadata.write_bytes(raw)
            self.assertEqual(metadata_sha256(metadata), hashlib.sha256(raw).hexdigest())
            metadata.write_bytes(raw + b"# edited\n")
            self.assertNotEqual(
                metadata_sha256(metadata), hashlib.sha256(raw).hexdigest()
            )

    def test_content_digest_is_stable_across_creation_order(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "first"
            second = root / "second"
            first.mkdir()
            second.mkdir()
            for name, content in (
                ("metadata.yml", b"id: DOC-ONE\n"),
                ("templates/guide.md", b"guide"),
                ("README.md", b"Readme"),
            ):
                for target in (first, second):
                    path = target / name
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(content)
            self.assertEqual(
                component_content_sha256(first), component_content_sha256(second)
            )

    def test_content_digest_changes_for_edit_add_remove_and_rename(self) -> None:
        with TemporaryDirectory() as directory:
            component = Path(directory) / "component"
            component.mkdir()
            metadata = component / "metadata.yml"
            metadata.write_bytes(b"id: DOC-ONE\n")
            baseline = component_content_sha256(component)
            other = component / "guide.md"
            other.write_bytes(b"guide")
            self.assertNotEqual(component_content_sha256(component), baseline)
            with_guide = component_content_sha256(component)
            other.rename(component / "renamed.md")
            self.assertNotEqual(component_content_sha256(component), with_guide)
            (component / "renamed.md").unlink()
            self.assertEqual(component_content_sha256(component), baseline)
            metadata.write_bytes(b"id: DOC-TWO\n")
            self.assertNotEqual(component_content_sha256(component), baseline)

    def test_content_digest_rejects_missing_component_root(self) -> None:
        with TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "not a directory"):
                component_content_sha256(Path(directory) / "missing")

    def test_content_digest_rejects_file_size_change_during_hash(self) -> None:
        with TemporaryDirectory() as directory:
            component = Path(directory) / "component"
            component.mkdir()
            (component / "README.md").write_bytes(b"fixed content")
            real_fstat = os.fstat
            calls = 0

            def changed_size(fd: int) -> object:
                nonlocal calls
                calls += 1
                actual = real_fstat(fd)
                if calls == 2:
                    return SimpleNamespace(
                        st_size=actual.st_size + 1,
                        st_mtime_ns=actual.st_mtime_ns,
                    )
                return actual

            with patch("scripts.framework_validator.integrity.os.fstat",
                       side_effect=changed_size):
                with self.assertRaisesRegex(ValueError, "changed during hashing"):
                    component_content_sha256(component)
            self.assertEqual(calls, 2)

    def test_content_digest_rejects_timestamp_change_during_hash(self) -> None:
        with TemporaryDirectory() as directory:
            component = Path(directory) / "component"
            component.mkdir()
            (component / "README.md").write_bytes(b"fixed content")
            real_fstat = os.fstat
            calls = 0

            def changed_timestamp(fd: int) -> object:
                nonlocal calls
                calls += 1
                actual = real_fstat(fd)
                if calls == 2:
                    return SimpleNamespace(
                        st_size=actual.st_size,
                        st_mtime_ns=actual.st_mtime_ns + 1,
                    )
                return actual

            with patch("scripts.framework_validator.integrity.os.fstat",
                       side_effect=changed_timestamp):
                with self.assertRaisesRegex(ValueError, "changed during hashing"):
                    component_content_sha256(component)
            self.assertEqual(calls, 2)

    def test_digest_helpers_reject_symlinked_files_and_directories(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = root / "component"
            component.mkdir()
            external = root / "external.yml"
            external.write_text("id: OUTSIDE", encoding="utf-8")
            link = component / "metadata.yml"
            try:
                link.symlink_to(external)
            except (OSError, NotImplementedError):
                self.skipTest("Symlinks unavailable in this environment")
            with self.assertRaisesRegex(ValueError, "symbolic link"):
                metadata_sha256(link)
            with self.assertRaisesRegex(ValueError, "symbolic link"):
                component_content_sha256(component)

            link.unlink()
            alias = root / "alias"
            try:
                alias.symlink_to(component, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("Directory symlinks unavailable in this environment")
            with self.assertRaisesRegex(ValueError, "symbolic link"):
                component_content_sha256(alias)
            with self.assertRaisesRegex(ValueError, "symbolic link"):
                metadata_sha256(alias / "metadata.yml")


if __name__ == "__main__":
    unittest.main()
