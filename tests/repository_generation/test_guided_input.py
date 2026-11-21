"""UX-B1: field entry is bounded, read-only and uses the strict JSON contract."""
from contextlib import redirect_stdout
from io import StringIO
import json
import unittest

from scripts.repository_generation import GenerationError
from scripts.repository_generation.guided import (
    FIELDS, GuidedCancelled, collect_draft, collect_field, validate_draft,
)
from test_inputs import fixture


class GuidedInputTests(unittest.TestCase):
    def scripted(self, lines):
        iterator = iter(lines)
        output = []
        def read(_prompt):
            return next(iterator)
        def write(message):
            output.append(message)
        return read, write, output

    def scripted_project(self, item):
        data = fixture()
        responses = []
        for field, _, kind in FIELDS:
            value = item[field] if field in item else data.get(field, "")
            if field == "unreleased_changes":
                for category in ("Added", "Changed", "Deprecated", "Removed", "Fixed", "Security"):
                    if category in value:
                        responses.extend(["yes", *value[category], "done"])
                    else:
                        responses.append("no")
            elif kind == "list":
                responses.extend([*value, "done"])
            elif kind == "markdown":
                responses.extend(value.split("\n") + [":end"])
            else:
                responses.append(value)
        return responses

    def test_complete_draft_matches_original_parser(self):
        sample = fixture()
        sample["short_description"] = ""
        sample["alignment"] = "center"
        sample["unreleased_changes"] = {}
        read, write, messages = self.scripted(self.scripted_project(sample) + ["continue"])
        draft, parsed = collect_draft(read=read, write=write)
        self.assertEqual(draft, sample)
        self.assertEqual(parsed, validate_draft(draft))
        self.assertIn("nothing has been written", "\n".join(messages))
        self.assertEqual(json.loads(json.dumps(draft)), sample)

    def test_edit_invalid_field_then_continue(self):
        sample = fixture()
        sample["alignment"] = "center"
        sample["short_description"] = ""
        sample["unreleased_changes"] = {}
        bad = dict(sample, project_name="A")
        lines = self.scripted_project(bad) + [
            "continue", "edit", "not_a_field",
            "edit", "project_name", "A valid backend title", "continue",
        ]
        read, write, messages = self.scripted(lines)
        draft, _ = collect_draft(read=read, write=write)
        self.assertEqual(draft["project_name"], "A valid backend title")
        self.assertIn("Input issue: project_name", "\n".join(messages))
        self.assertIn("Unknown field", "\n".join(messages))

    def test_markdown_terminator_escape_and_spaces(self):
        read, write, _ = self.scripted(["alpha", "::end", "", "  beta  ", ":end"])
        result = collect_field("footer", read=read, write=write)
        self.assertEqual(result, "alpha\n:end\n\n  beta  ")
        read, write, _ = self.scripted(["  first  ", "second", "done"])
        self.assertEqual(collect_field("features", read=read, write=write),
                         ["  first  ", "second"])

    def test_lists_require_nonempty_items(self):
        read, write, output = self.scripted(["done", "", "real item", "done"])
        self.assertEqual(collect_field("documents", read=read, write=write), ["real item"])
        self.assertIn("At least one item", "\n".join(output))
        self.assertIn("Blank items", "\n".join(output))

    def test_optional_categories_are_explicit(self):
        read, write, output = self.scripted([
            "yes", "First change", "done",
            "no", "no", "no", "no", "no",
        ])
        self.assertEqual(collect_field("unreleased_changes", read=read, write=write),
                         {"Added": ["First change"]})
        self.assertIn("Unreleased", "\n".join(output))

    def test_cancel_and_eof_are_not_success(self):
        read, write, _ = self.scripted([":cancel"])
        with self.assertRaises(GuidedCancelled):
            collect_draft(read=read, write=write)
        read, write, _ = self.scripted([])
        with self.assertRaises(StopIteration):
            collect_draft(read=read, write=write)

    def test_invalid_schema_is_not_coerced(self):
        data = fixture()
        data["features"] = []
        with self.assertRaises(GenerationError):
            validate_draft(data)
        data = fixture()
        data["invented_field"] = "unsupported"
        with self.assertRaises(GenerationError):
            validate_draft(data)


if __name__ == "__main__":
    unittest.main()
