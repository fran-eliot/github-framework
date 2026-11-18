"""Bounded registry adapter contracts."""

from pathlib import Path
import unittest

from scripts.template_composition_preview import SourceError
from scripts.template_composition_preview.registry import (
    HEADER, SEPARATOR, SECTIONS, load_registry, parse_registry,
)


def fixture():
    return "\n\n".join(
        f"{heading}\n\nRegistry.\n\n{HEADER}\n{SEPARATOR}\n"
        f"| {chr(96)}{prefix}-EXAMPLE{chr(96)} | Example | Conceptual |\n\n---"
        for heading, prefix in SECTIONS
    )


class RegistryTests(unittest.TestCase):
    def test_bounded_and_repeatable(self):
        text = fixture() + "\n# Other table\n| " + chr(96) + "DOC-OTHER" + chr(96) + " | Other | Implemented |\n"
        records = parse_registry(text)
        self.assertEqual(list(records), [f"{prefix}-EXAMPLE" for _, prefix in SECTIONS])
        self.assertEqual(records, parse_registry(text))
        self.assertTrue(all(r.classification == "Conceptual" for r in records.values()))

    def test_malformed_registry(self):
        text = fixture()
        row = f"| {chr(96)}README-EXAMPLE{chr(96)} | Example | Conceptual |"
        changes = (
            text.replace(SECTIONS[0][0], "# Missing"),
            text + "\n" + SECTIONS[0][0],
            text.replace(HEADER, "| Invalid |", 1),
            text.replace(SEPARATOR, "| --- |", 1),
            text.replace(row, row + "\n" + row),
            text.replace(row, row.replace("Conceptual", "Unknown")),
            text.replace(row, row.replace("README-", "DOC-")),
            text.replace(row, row.replace("Example |", " |")),
            text.replace(row, ""),
            text.replace(row, row + "\nInterrupted\n" + row),
            text.replace(row, row + "\n" + HEADER),
        )
        for changed in changes:
            with self.subTest(changed=changed):
                with self.assertRaises(SourceError):
                    parse_registry(changed)

    def test_real_registry(self):
        root = Path(__file__).resolve().parents[2]
        records = load_registry(root)
        self.assertEqual(records["README-HERO"].classification, "Implemented")
        self.assertEqual(records["README-LICENSE"].classification, "Conceptual")
        self.assertEqual(records["VCL-HERO"].classification, "Conceptual")
