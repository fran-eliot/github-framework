import json
from pathlib import Path
import tempfile
import unittest

from scripts.repository_generation import GenerationError
from scripts.repository_generation.inputs import load_project_input, parse_project_input
from scripts.repository_generation.profile import REQUIRED, require_profile


def fixture():
    return {
        "project_name": "Sample Backend",
        "tagline": "A documented sample backend project.",
        "overview": "This sample backend is a planned service used to demonstrate a reproducible repository documentation structure.",
        "features": ["Planned API endpoints"],
        "technologies": ["Backend: Python"],
        "prerequisites": "Python 3.11 is the intended runtime.",
        "installation": "Not implemented yet.",
        "execution": "Not implemented yet.",
        "documents": ["CHANGELOG.md"],
        "footer": "Documentation seed.",
    }


class InputTests(unittest.TestCase):
    def parse(self, **changes):
        return parse_project_input(json.dumps({**fixture(), **changes}))

    def test_profile(self):
        require_profile("TPL-BACKEND", "0.1.0")
        self.assertEqual(len(REQUIRED), 8)
        for template, version in (("TPL-FULLSTACK", "0.1.0"), ("TPL-BACKEND", "1.0.0")):
            with self.assertRaises(GenerationError):
                require_profile(template, version)

    def test_defaults_and_lists(self):
        result = self.parse(features=["B", "A"])
        self.assertEqual(result.features, ("B", "A"))
        self.assertEqual(result.alignment, "center")
        self.assertEqual(result.short_description, "")
        self.assertEqual(result.unreleased_changes, ())

    def test_markdown_normalization_and_literal_content(self):
        result = self.parse(footer="Line\r\n\r\n{{ literal }}\rNext\tword")
        self.assertEqual(result.footer, "Line\n\n{{ literal }}\nNext\tword")

    def test_categories_in_contract_order(self):
        result = self.parse(unreleased_changes={"Fixed": ["B"], "Added": ["A"]})
        self.assertEqual(result.unreleased_changes, (("Added", ("A",)), ("Fixed", ("B",))))

    def test_missing_fields(self):
        for key in fixture():
            data = fixture()
            del data[key]
            with self.subTest(key=key), self.assertRaises(GenerationError):
                parse_project_input(json.dumps(data))

    def test_invalid_fields(self):
        cases = [
            {"project_name": "x"}, {"project_name": "x"*61}, {"project_name": "A\nB"},
            {"tagline": "short"}, {"tagline": "x"*101}, {"overview": "x"*79},
            {"overview": "x"*1201}, {"features": []}, {"features": [" "]},
            {"technologies": "Python"}, {"documents": [1]}, {"documents": ["A\nB"]},
            {"footer": None}, {"footer": "\t\n"}, {"footer": "x\0y"},
            {"footer": "\ud800"}, {"project_name": "A\u2028B"},
            {"alignment": []}, {"alignment": "right"}, {"short_description": "x"*241},
            {"short_description": None}, {"unreleased_changes": []},
            {"unreleased_changes": {"Fixed": []}}, {"unreleased_changes": {"Other": ["A"]}},
            {"unreleased_changes": {"Fixed": ["A\nB"]}},
            {"banner": {}}, {"badges": []}, {"unknown": True},
        ]
        for changes in cases:
            with self.subTest(changes=changes), self.assertRaises(GenerationError):
                self.parse(**changes)

    def test_invalid_json(self):
        for text in ("{", "null", "[]", '{"x": NaN}', '{"x": Infinity}', '{"x": -Infinity}',
                     '{"project_name":"A","project_name":"B"}',
                     '{"unreleased_changes":{"Fixed":[],"Fixed":[]}}'):
            with self.subTest(text=text), self.assertRaises(GenerationError):
                parse_project_input(text)

    def test_file_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.json"
            path.write_bytes(json.dumps(fixture()).encode("utf-8"))
            self.assertEqual(load_project_input(path), self.parse())
            path.write_bytes(b"\xff")
            with self.assertRaises(GenerationError):
                load_project_input(path)
            with self.assertRaises(GenerationError):
                load_project_input(path.with_name("missing.json"))


if __name__ == "__main__":
    unittest.main()
