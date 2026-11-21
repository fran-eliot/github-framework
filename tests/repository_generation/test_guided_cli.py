"""UX-B2: opt-in terminal guide, confirmation, noninteractive and write safety."""
from contextlib import redirect_stderr
from hashlib import sha256
from io import StringIO
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from scripts.repository_generation.cli import main, run_guided
from scripts.repository_generation.guided import FIELDS
from test_inputs import fixture

ROOT = Path(__file__).resolve().parents[2]


def answers_for(data):
    """Script an explicit set of legitimate project facts, not hidden defaults."""
    result = []
    for field, _, kind in FIELDS:
        value = data.get(field, "" if field == "short_description" else
                         "center" if field == "alignment" else {})
        if kind == "changes":
            for cat in ("Added", "Changed", "Deprecated", "Removed", "Fixed", "Security"):
                if cat in value:
                    result.extend(["yes", *value[cat], "done"])
                else:
                    result.append("no")
        elif kind == "list":
            result.extend([*value, "done"])
        elif kind == "markdown":
            for line in value.split("\n"):
                result.append("::end" if line == ":end" else line)
            result.append(":end")
        else:
            result.append(value)
    return result


class GuidedCliTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.parent = Path(temp.name).resolve()
        self.sample = fixture()
        self.sample["short_description"] = ""
        self.sample["alignment"] = "center"
        self.sample["unreleased_changes"] = {"Added": ["Documented initial plan"]}

    def invoke(self, suffix, *, name="guided-backend"):
        iterator = iter(answers_for(self.sample) + [
            "continue", str(self.parent), name, *suffix,
        ])
        messages = []
        def read(_prompt):
            return next(iterator)
        def write(line):
            messages.append(line)
        err = StringIO()
        with redirect_stderr(err):
            code = run_guided(read=read, write=write)
        return code, "\n".join(messages), err.getvalue()

    def test_help_and_noninteractive_rejection(self):
        help_out = subprocess.run([sys.executable, "-B", "-m", "scripts.repository_generation", "--help"],
                                  cwd=ROOT, capture_output=True, text=True, timeout=30)
        self.assertEqual(help_out.returncode, 0)
        self.assertIn("guide", help_out.stdout)
        rejected = subprocess.run([sys.executable, "-B", "-m", "scripts.repository_generation", "guide"],
                                  cwd=ROOT, capture_output=True, text=True, input="yes\n", timeout=30)
        self.assertEqual(rejected.returncode, 2)
        self.assertEqual(rejected.stdout, "")
        self.assertIn("interactive terminal", rejected.stderr)
        self.assertEqual(list(self.parent.iterdir()), [])

    def test_no_and_empty_confirmation_never_write(self):
        for answer in ("no", "", "cancel", "YES", "unexpected"):
            with self.subTest(answer=answer):
                code, out, err = self.invoke([answer])
                self.assertEqual(code, 3, err)
                self.assertIn("Read-only plan", out)
                self.assertIn("VCL-HERO", out)
                self.assertIn("Cancelled", out)
                self.assertFalse((self.parent / "guided-backend").exists())

    def test_generation_uses_canonical_two_file_output(self):
        code, out, err = self.invoke(["yes"])
        self.assertEqual(code, 0, err)
        self.assertIn("Written and verified files", out)
        target = self.parent / "guided-backend"
        self.assertEqual(sorted(p.name for p in target.iterdir()), ["CHANGELOG.md", "README.md"])
        self.assertIn(self.sample["project_name"], (target / "README.md").read_text(encoding="utf-8"))
        self.assertIn("Documented initial plan", (target / "CHANGELOG.md").read_text(encoding="utf-8"))
        for name in ("README.md", "CHANGELOG.md"):
            digest = sha256((target / name).read_bytes()).hexdigest()
            self.assertIn(f"{name} | SHA-256: {digest}", out)
        code2, out2, err2 = self.invoke(["yes"])
        self.assertEqual(code2, 1)
        self.assertNotIn("Written and verified files", out2)
        self.assertIn("already exists", err2)

    def test_existing_destination_preserved_before_confirmation(self):
        target = self.parent / "guided-backend"
        target.mkdir()
        protected = target / "keep.txt"
        protected.write_bytes(b"preserve")
        code, out, err = self.invoke(["yes"])
        self.assertEqual(code, 1)
        self.assertNotIn("Read-only plan", out)
        self.assertIn("already exists", err)
        self.assertEqual(protected.read_bytes(), b"preserve")

    def test_unsafe_destination_and_invalid_draft_do_not_write(self):
        code, _, err = self.invoke(["yes"], name="../escape")
        self.assertEqual(code, 1)
        self.assertIn("invalid portable", err)
        self.assertFalse((self.parent.parent / "escape").exists())
        self.sample["overview"] = "too short"
        scripted = answers_for(self.sample)
        # Cancel at the immediate retry prompt after rejecting the short
        # overview; do not continue with unrelated scripted field answers.
        scripted = scripted[:scripted.index("too short") + 2] + [":cancel"]
        iterator = iter(scripted)
        messages = []
        with redirect_stderr(StringIO()):
            code = run_guided(read=lambda _: next(iterator), write=messages.append)
        self.assertEqual(code, 3)
        output = "\n".join(messages)
        self.assertIn("Please correct overview", output)
        self.assertIn("Overview requires 80", output)
        self.assertIn("Cancelled; no destination created", output)
        self.assertNotIn("Read-only plan", output)
        self.assertEqual(list(self.parent.iterdir()), [])

    def test_eof_or_interrupt_before_write(self):
        full = answers_for(self.sample) + ["continue", str(self.parent), "guided-backend"]
        for suffix in ([], ["yes"]):
            with self.subTest(suffix=suffix):
                # EOF before confirmation or scripted interruption at confirmation.
                iterator = iter(full + suffix)
                def read(_):
                    answer = next(iterator)  # StopIteration is treated like EOF
                    if answer == "yes":
                        raise KeyboardInterrupt()
                    return answer
                err = StringIO()
                with redirect_stderr(err):
                    code = run_guided(read=read, write=lambda _: None)
                self.assertIn(code, (2, 3))
                self.assertFalse((self.parent / "guided-backend").exists())

    def test_revalidation_and_destination_recheck_after_yes(self):
        # Verify that generate does not trust the prior read-only plan.
        def reject(*_args, **_kwargs):
            raise RuntimeError("writer must not be reached")
        with patch("scripts.repository_generation.cli.write_documents", side_effect=reject):
            code, _, err = self.invoke(["no"])
        self.assertEqual(code, 3)
        self.assertEqual(err, "")
        self.assertEqual(list(self.parent.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
