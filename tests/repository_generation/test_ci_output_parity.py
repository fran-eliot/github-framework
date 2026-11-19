"""Exercise the CI-only byte comparison and failure paths."""
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
from pathlib import Path
import tempfile
import unittest

from scripts.repository_generation.ci_output_parity import compare


class OutputParityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.left = Path(temporary.name) / "ubuntu"
        self.right = Path(temporary.name) / "windows"
        for directory in (self.left, self.right):
            directory.mkdir()
            (directory / "README.md").write_bytes(b"# Example\n")
            (directory / "CHANGELOG.md").write_bytes(b"# Changelog\n\n## [Unreleased]\n")

    def result(self):
        out, err = StringIO(), StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = compare(self.left, self.right)
        return code, out.getvalue(), err.getvalue()

    def test_match_reports_both_documents(self):
        code, output, error = self.result()
        self.assertEqual(code, 0)
        self.assertEqual(error, "")
        self.assertIn("README.md: MATCH", output)
        self.assertIn("CHANGELOG.md: MATCH", output)
        self.assertIn("byte-identical", output)

    def test_byte_mismatch(self):
        (self.right / "README.md").write_bytes(b"# Different\n")
        code, output, error = self.result()
        self.assertEqual(code, 1)
        self.assertIn("README.md: MISMATCH", output)
        self.assertIn("parity failed", error)

    def test_missing_or_extra_artifacts(self):
        path = self.right / "README.md"
        path.unlink()
        self.assertEqual(self.result()[0], 2)
        path.write_bytes(b"# Example\n")
        (self.right / "extra.md").write_bytes(b"x\n")
        self.assertEqual(self.result()[0], 2)

    def test_invalid_document_encoding_or_line_endings(self):
        path = self.right / "README.md"
        for content in (b"\xff\n", b"# Example\r\n", b"# Example"):
            with self.subTest(content=content):
                path.write_bytes(content)
                self.assertEqual(self.result()[0], 2)
