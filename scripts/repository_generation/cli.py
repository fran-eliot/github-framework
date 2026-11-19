"""Standalone local plan/generate command for the bounded Backend profile."""
import argparse
from pathlib import Path
import sys

from . import GenerationError
from .assembly import assemble
from .composition import load_composition
from .destination import DestinationError, validate_destination, write_documents
from .inputs import load_project_input
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


def main(argv=None):
    args = parser().parse_args(argv)
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
    print(report(args.mode, composition, documents, target))
    return 0
