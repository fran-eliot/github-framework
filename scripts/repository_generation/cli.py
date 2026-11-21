"""Standalone local plan/generate command for the bounded Backend profile."""
import argparse
from pathlib import Path
import sys

from . import GenerationError
from .assembly import assemble
from .composition import load_composition
from .destination import DestinationError, validate_destination, write_documents
from .inputs import load_project_input
from .guided import GuidedCancelled, ask, collect_draft, validate_draft
from .profile import VISUAL_LIMITATION, require_profile

ROOT = Path(__file__).resolve().parents[2]


def parser():
    result = argparse.ArgumentParser(description="Generate bounded local repository documentation.")
    modes = result.add_subparsers(dest="mode", required=True)
    for mode, help_text in (("plan", "Preview without destination writes"),
                            ("generate", "Create a new local documentation directory")):
        command = modes.add_parser(mode, help=help_text, allow_abbrev=False)
        command.add_argument("template")
        command.add_argument("--template-version", required=True)
        command.add_argument("--input", required=True, type=Path)
        command.add_argument("--output-parent", required=True, type=Path)
        command.add_argument("--name", required=True)
        command.add_argument("--summary", action="store_true",
                             help="Show a short, interpreted report instead of detailed provenance")
    modes.add_parser("guide", help="Interactively prepare, preview and confirm a new documentation seed",
                     allow_abbrev=False)
    return result


def report(mode, composition, documents, target):
    template = composition.resolution.template
    selected = {item.id: item for item in composition.selected}
    lines = [
        f"Template: {template.id} {template.version}",
        f"Template source: {template.path}",
        "Profile: text-only documentation seed; not full Template conformance",
        "Composition:",
    ]
    for group in composition.resolution.groups:
        for reference in group.references:
            identity = reference.id
            state = "Selected" if identity in selected else "Unselected"
            lines.append(f"  {group.level} | {identity} | {reference.outcome} | {state}")
            if identity in selected:
                item = selected[identity]
                lines.extend((f"    Version: {item.version}",
                              f"    Metadata: {item.metadata_path}",
                              f"    Artifact: {item.artifact_path}"))
    lines.append("Direct dependencies:")
    for item in composition.dependencies:
        lines.append(f"  {item.owner} | {item.level} | {item.id} >= {item.minimum_version} | {item.outcome}: {item.note}")
    lines.append("Limitation: " + VISUAL_LIMITATION)
    lines.append(f"Destination: {target}")
    lines.append("Intended artifacts:" if mode == "plan" else "Written and verified artifacts:")
    for document in documents:
        lines.append(f"  {target / document.name} | SHA-256: {document.digest}")
    lines.append("Plan complete; no destination writes." if mode == "plan" else "Generation complete.")
    return "\n".join(lines)


def summary_report(mode, composition, documents, target):
    """User-oriented report derived from the same typed preflight as the full report.

    The detailed report remains the default and retains all source provenance.
    """
    template = composition.resolution.template
    selected = {item.id for item in composition.selected}
    unselected = sum(1 for group in composition.resolution.groups
                     for ref in group.references if ref.id not in selected)
    if len(selected) != 8 or unselected != 20:
        raise GenerationError("summary: unexpected supported composition")
    preview = mode == "plan"
    lines = [
        "Repository documentation " + ("plan" if preview else "generated"),
        f"Profile: {template.id} {template.version} (text-only documentation seed)",
        "Scope: README.md and CHANGELOG.md only; no application code or full Template conformance.",
        f"Composition: {len(selected)} required Components selected; {unselected} recommended/optional references unselected.",
        "Known limitation: README-HERO requires Conceptual VCL-HERO 1.0.0; "
        "a text-only Hero is used, not full Template conformance.",
        f"Destination: {target}",
        "Intended files (not yet written):" if preview else "Written and verified files:",
    ]
    for document in documents:
        lines.append(f"  {document.name} | SHA-256: {document.digest}")
    if preview:
        lines.append("Next: review this plan; run generate with the same input and a fresh destination.")
        lines.append("No destination files were created by plan.")
    else:
        lines.append("Next: open and inspect the generated README.md and CHANGELOG.md for accuracy.")
    lines.append("For source paths, dependency classifications and full provenance, omit --summary.")
    return "\n".join(lines)



def run_guided(*, read=input, write=print):
    """Explicit guided flow; never writes before an affirmative confirmation.

    The guided draft and CLI plan both reuse the canonical resolver/assembler.
    A confirmed generate repeats preflight and uses the exclusive writer.
    """
    try:
        draft, _project = collect_draft(read=read, write=write)
        write("\nChoose an existing local output parent OUTSIDE the Framework checkout.")
        write("The tool creates a new child; it never overwrites an existing one.")
        parent = Path(ask("Existing output parent path> ", read=read, write=write))
        name = ask("New child directory name (lowercase letters/digits/hyphens)> ",
                   read=read, write=write)
        require_profile("TPL-BACKEND", "0.1.0")
        project = validate_draft(draft)
        composition = load_composition(ROOT, "TPL-BACKEND", "0.1.0")
        documents = assemble(composition, project)
        target = validate_destination(ROOT, parent, name)
        # The summary checks the supported profile before confirmation and writes.
        preview = summary_report("plan", composition, documents, target)
        write("\nRead-only plan (no destination files created):")
        write(preview)
        write(f"\nGenerate only if the exact destination is correct:\n{target}")
        confirmation = ask("Type yes to generate; anything else cancels> ",
                           read=read, write=write)
        if confirmation != "yes":
            raise GuidedCancelled()
        # Reuse and repeat all canonical preflight checks after confirmation.
        project = validate_draft(draft)
        require_profile("TPL-BACKEND", "0.1.0")
        composition = load_composition(ROOT, "TPL-BACKEND", "0.1.0")
        documents = assemble(composition, project)
        target = validate_destination(ROOT, parent, name)
        # Validate report before any write to prevent success-report failures
        # after committed output. The writer rechecks destination exclusively.
        summary_report("generate", composition, documents, target)
        target = write_documents(ROOT, parent, name, documents)
        write(summary_report("generate", composition, documents, target))
        return 0
    except GuidedCancelled:
        write("Cancelled; no destination created by this operation.")
        return 3
    except (EOFError, StopIteration):
        print("Guided error: input ended before confirmation; no generation attempted.",
              file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("\nGuided session interrupted; no automatic cleanup.", file=sys.stderr)
        return 3
    except DestinationError as exc:
        print(f"Destination error: {exc}", file=sys.stderr)
        return 1
    except GenerationError as exc:
        print(f"Generation error: {exc}", file=sys.stderr)
        return 2


def main(argv=None):
    args = parser().parse_args(argv)
    if args.mode == "guide":
        if not (sys.stdin.isatty() and sys.stdout.isatty()):
            print("Guided error: guide requires an interactive terminal; "
                  "use plan/generate for noninteractive scripts.", file=sys.stderr)
            return 2
        return run_guided()
    try:
        require_profile(args.template, args.template_version)
        project = load_project_input(args.input)
        composition = load_composition(ROOT, args.template, args.template_version)
        documents = assemble(composition, project)
        target = validate_destination(ROOT, args.output_parent, args.name)
        if args.mode == "generate":
            target = write_documents(ROOT, args.output_parent, args.name, documents)
    except DestinationError as exc:
        print(f"Destination error: {exc}", file=sys.stderr)
        return 1
    except GenerationError as exc:
        print(f"Generation error: {exc}", file=sys.stderr)
        return 2
    try:
        output = (summary_report(args.mode, composition, documents, target)
                  if args.summary else report(args.mode, composition, documents, target))
    except GenerationError as exc:
        print(f"Generation error: {exc}", file=sys.stderr)
        return 2
    print(output)
    return 0
