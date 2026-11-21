"""Bounded, opt-in terminal input collection for the Backend documentation seed.

This module intentionally has no filesystem writes. A subsequent reviewed UX-B
increment will connect the validated draft to the canonical safe generator.
"""
import json

from . import GenerationError
from .inputs import parse_project_input
from .profile import CATEGORIES

# Order follows the public input contract, rather than an independent schema.
FIELDS = (
    ("project_name", "Project title (2-60 characters)", "line"),
    ("tagline", "One-line description (10-100 characters)", "line"),
    ("overview", "Project overview (80-1200 characters; Markdown)", "markdown"),
    ("features", "Proposed or verified features (ordered list)", "list"),
    ("technologies", "Project technology choices (ordered list)", "list"),
    ("prerequisites", "Prerequisites (Markdown)", "markdown"),
    ("installation", "Installation guidance (Markdown)", "markdown"),
    ("execution", "Run instructions or honest unavailability (Markdown)", "markdown"),
    ("documents", "Documentation entries (ordered list)", "list"),
    ("footer", "Final disclosure or footer (Markdown)", "markdown"),
    ("short_description", "Optional short description (0-240 characters)", "optional"),
    ("alignment", "Hero alignment", "alignment"),
    ("unreleased_changes", "Optional Unreleased changelog categories", "changes"),
)
FIELD_NAMES = tuple(field for field, _, _ in FIELDS)


class GuidedCancelled(Exception):
    """User explicitly cancelled a read-only draft."""


def ask(prompt, *, read=input, write=print):
    """Read one line, with an explicit cancellation escape."""
    answer = read(prompt)
    if answer == ":cancel":
        raise GuidedCancelled()
    return answer


def _list(name, *, read, write):
    write(f"{name}: enter one item per line; type done on its own line to finish.")
    values = []
    while True:
        value = ask("item> ", read=read, write=write)
        if value == "done":
            if values:
                return values
            write("At least one item is required.")
            continue
        if not value.strip():
            write("Blank items are not valid.")
            continue
        values.append(value)


def _markdown(name, *, read, write):
    write(f"{name}: enter Markdown; :end finishes, ::end inserts a literal :end line.")
    values = []
    while True:
        line = ask("... ", read=read, write=write)
        if line == ":end":
            return "\n".join(values)
        values.append(":end" if line == "::end" else line)


def _changes(*, read, write):
    write("Unreleased categories are optional; no version is invented.")
    changes = {}
    for category in CATEGORIES:
        while True:
            answer = ask(f"Include {category} changes? (yes/no)> ", read=read, write=write)
            if answer in ("yes", "no"):
                break
            write("Type yes or no.")
        if answer == "yes":
            changes[category] = _list(category, read=read, write=write)
    return changes


def collect_field(field, *, read=input, write=print):
    matches = [item for item in FIELDS if item[0] == field]
    if not matches:
        raise GenerationError(f"unknown guided field: {field}")
    _, description, kind = matches[0]
    write(f"\n{field} — {description}")
    if kind == "markdown":
        return _markdown(field, read=read, write=write)
    if kind == "list":
        return _list(field, read=read, write=write)
    if kind == "changes":
        return _changes(read=read, write=write)
    if kind == "alignment":
        while True:
            value = ask("Alignment (center/left; type center for the default)> ",
                        read=read, write=write)
            if value in ("center", "left"):
                return value
            write("Enter center or left.")
    if kind == "optional":
        write("Leave empty to explicitly accept no short description.")
    return ask(f"{field}> ", read=read, write=write)


def validate_draft(draft):
    """Always reuse the strict JSON contract; no silent coercion or inference."""
    return parse_project_input(json.dumps(draft, ensure_ascii=False))


def collect_draft(*, read=input, write=print):
    """Collect all fields, display every value, and permit correction or cancel.

    No file, directory, network operation or generator execution occurs here.
    """
    write("Guided Backend documentation: text-only README.md and CHANGELOG.md.")
    write("No application code, Git operations or full Template conformance.")
    write("Every project fact comes from you. Type :cancel to stop at any prompt.")
    draft = {}
    for field, _, _ in FIELDS:
        draft[field] = collect_field(field, read=read, write=write)
    while True:
        write("\nReview your exact input (nothing has been written):")
        write(json.dumps(draft, ensure_ascii=False, indent=2))
        try:
            project = validate_draft(draft)
        except GenerationError as exc:
            write(f"Input issue: {exc}; edit a field or cancel.")
            project = None
        action = ask("Type continue, edit or cancel> ", read=read, write=write)
        if action == "cancel":
            raise GuidedCancelled()
        if action == "edit":
            field = ask("Field name to edit> ", read=read, write=write)
            if field not in FIELD_NAMES:
                write("Unknown field. Choose a name shown in the review.")
                continue
            draft[field] = collect_field(field, read=read, write=write)
        elif action == "continue":
            if project is None:
                write("Fix the input issue before continuing.")
            else:
                return draft, project
        else:
            write("Type continue, edit or cancel.")
