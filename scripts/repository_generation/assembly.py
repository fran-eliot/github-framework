"""Assemble and structurally check the bounded two-document output in memory."""
from dataclasses import dataclass
from hashlib import sha256
from html import escape
import re

from . import GenerationError
from .composition import GenerationComposition
from .inputs import ProjectInput
from .profile import REQUIRED, ARTIFACTS
from .rendering import render_component

_SECTION_STARTS = {
    "README-OVERVIEW": "## 📖 Overview",
    "README-FEATURES": "## ✨ Features",
    "README-TECH-STACK": "## 🛠 Tech Stack",
    "README-QUICK-START": "## 🚀 Quick Start",
    "README-DOCUMENTATION": "## 📚 Documentation",
    "README-FOOTER": "---",
}
_FENCE = re.compile(r"^ {0,3}(?P<marker>\x60{3,}|~{3,})(?P<rest>.*)$")
_ATX = re.compile(r"^ {0,3}#(?:[ \t]+|$)")
_SETEXT = re.compile(r"^ {0,3}=+[ \t]*$")
_HTML_OPEN = re.compile(r"<h1(?=[\s/>])[^>]*>", re.I)
_HTML_CLOSE = re.compile(r"</h1\s*>", re.I)
_CONTAINER = re.compile(r"^[ \t]*(?:>[ \t]?|(?:[-+*]|\d+[.)])[ \t]+)")


@dataclass(frozen=True)
class Document:
    name: str
    content: bytes

    @property
    def digest(self) -> str:
        return sha256(self.content).hexdigest()


def _headings(text):
    """Conservative checks, not a CommonMark parser or HTML sanitizer.

    Ignore closed, top-level backtick/tilde fences. Detect ordinary ATX,
    Setext and HTML H1 patterns elsewhere, including common list/quote
    prefixes. Ambiguous literal markup can be rejected intentionally.
    """
    markdown = 0
    previous = ""
    fence = None
    visible = []
    for line in text.split("\n"):
        match = _FENCE.fullmatch(line)
        if fence is not None:
            if match and match["marker"][0] == fence[0] and len(match["marker"]) >= len(fence) and not match["rest"].strip():
                fence = None
            previous = ""
            continue
        if match:
            fence = match["marker"]
            previous = ""
            continue
        visible.append(line)
        current = line
        while prefix := _CONTAINER.match(current):
            current = current[prefix.end():]
        if _ATX.match(current):
            markdown += 1
        if _SETEXT.fullmatch(current) and previous.strip():
            markdown += 1
        previous = current
    if fence is not None:
        raise GenerationError("unclosed top-level code fence")
    outside = "\n".join(visible)
    return markdown, len(_HTML_OPEN.findall(outside)), len(_HTML_CLOSE.findall(outside))


def _document(name, text):
    if "\r" in text or not text.endswith("\n"):
        raise GenerationError(f"{name}: expected LF text with terminal newline")
    try:
        return Document(name, text.encode("utf-8"))
    except UnicodeError as exc:
        raise GenerationError(f"{name}: invalid UTF-8 content") from exc


def assemble(composition: GenerationComposition, project: ProjectInput) -> tuple[Document, ...]:
    """Return exactly README.md and CHANGELOG.md; no destination operations."""
    if tuple((c.id, c.version) for c in composition.selected) != tuple((i, v) for i, v, _ in REQUIRED):
        raise GenerationError("assembly selection differs from supported profile")
    fragments = []
    changelog = None
    for component in composition.selected:
        rendered = render_component(component, project)
        if component.id == "DOC-CHANGELOG":
            changelog = rendered
            continue
        # Trim only edge LF separators, not spaces or internal Markdown.
        fragment = rendered.strip("\n")
        if component.id == "README-HERO":
            heading = f'<h1 align="{project.alignment}">\n  {escape(project.project_name, quote=True)}\n</h1>'
            if not fragment.startswith(heading) or _headings(fragment) != (0, 1, 1):
                raise GenerationError("README-HERO: expected one project H1")
        else:
            first = fragment.split("\n", 1)[0]
            if first != _SECTION_STARTS[component.id]:
                raise GenerationError(f"{component.id}: unexpected section start")
            if _headings(fragment) != (0, 0, 0):
                raise GenerationError(f"{component.id}: additional H1 is not supported")
        fragments.append(fragment)
    readme = "\n\n".join(fragments) + "\n"
    if _headings(readme) != (0, 1, 1):
        raise GenerationError("README.md: expected exactly one project H1")
    if changelog is None or _headings(changelog) != (1, 0, 0):
        raise GenerationError("CHANGELOG.md: expected exactly one document H1")
    return (_document(ARTIFACTS[0], readme), _document(ARTIFACTS[1], changelog))
