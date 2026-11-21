"""Bounded, opt-in terminal collection and review for the Backend seed.

No filesystem writes: the existing CLI connects the validated draft to the
canonical generator only after a separate explicit confirmation.
"""
import json

from . import GenerationError
from .inputs import parse_project_input, _string, _items
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
    write(f"{name}: enter one item per line; type done ALONE on a line to finish.")
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
    write(f"{name}: enter Markdown; :end ALONE finishes, ::end inserts a literal :end line.")
    if name == "overview":
        write("Use ## for headings inside the README; a second # H1 will be rejected.")
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


def _validate_field(field, value):
    """Validate a field using the same primitive rules as the strict JSON parser.

    Complete-draft parsing remains authoritative (including cross-field and
    assembled-document rules). No placeholder facts are inserted to test fields.
    """
    if field == "project_name":
        _string(value, field, minimum=2, maximum=60)
    elif field == "tagline":
        _string(value, field, minimum=10, maximum=100)
    elif field == "overview":
        _string(value, field, markdown=True, minimum=80, maximum=1200)
    elif field in ("prerequisites", "installation", "execution", "footer"):
        _string(value, field, markdown=True)
    elif field in ("features", "technologies", "documents"):
        _items(value, field)
    elif field == "short_description":
        _string(value, field, maximum=240, empty=True)
    elif field == "alignment":
        if value not in ("center", "left"):
            raise GenerationError("alignment: expected left or center")
    elif field == "unreleased_changes":
        for category, items in value.items():
            if category not in CATEGORIES:
                raise GenerationError("unsupported Unreleased category")
            _items(items, f"unreleased_changes.{category}")
    else:
        raise GenerationError(f"unknown guided field: {field}")


def _collect_valid_field(field, *, read, write):
    while True:
        value = collect_field(field, read=read, write=write)
        try:
            _validate_field(field, value)
        except GenerationError as exc:
            write(f"Please correct {field}: {exc}")
            if field == "overview":
                write("Overview requires 80–1200 characters; provide actual project details.")
            elif field in ("prerequisites", "installation", "execution", "footer"):
                write("This field is required. Enter at least one nonblank Markdown line.")
            write("This entry has not been accepted; please enter this field again.")
            continue
        return value


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
        draft[field] = _collect_valid_field(field, read=read, write=write)
    show_review = True
    while True:
        if show_review:
            write("\nReview your exact input (nothing has been written):")
            write(json.dumps(draft, ensure_ascii=False, indent=2))
        try:
            project = validate_draft(draft)
        except GenerationError as exc:
            write(f"Input issue: {exc}; edit a field or cancel.")
            project = None
        action = ask("Type continue, edit or cancel> ", read=read, write=write)
        show_review = False
        if action == "cancel":
            raise GuidedCancelled()
        if action == "edit":
            field = ask("Field name to edit> ", read=read, write=write)
            if field not in FIELD_NAMES:
                write("Unknown field. Choose a name shown in the review.")
                continue
            draft[field] = _collect_valid_field(field, read=read, write=write)
            show_review = True
        elif action == "continue":
            if project is None:
                write("Fix the input issue before continuing.")
            else:
                return draft, project
        else:
            write("Type continue, edit or cancel.")
