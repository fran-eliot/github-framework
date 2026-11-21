"""Materialization policies for the eight required Backend Components."""
from html import escape
import re

from . import GenerationError
from .composition import SelectedComponent
from .inputs import ProjectInput
from .profile import REQUIRED
from .syntax import Text, Variable, IfBlock, EachBlock, parse_component

_SUPPORTED = {identity: version for identity, version, _ in REQUIRED}


def _bullets(items):
    return "\n".join("- " + item for item in items)


def _context(project):
    return {
        "project_name": project.project_name,
        "tagline": project.tagline,
        "short_description": project.short_description,
        "alignment": project.alignment,
        # Internal policy values only: visual materialization is disabled.
        "banner": None,
        "badges": (),
        "overview": project.overview,
        "features": project.features,
        "technologies": _bullets(project.technologies),
        "prerequisites": project.prerequisites,
        "installation": project.installation,
        "execution": project.execution,
        "documents": project.documents,
        "footer": project.footer,
    }


def _lookup(context, name, *, condition=False):
    value = context
    for part in name.split("."):
        if condition and value is None:
            return None
        if not isinstance(value, dict) or part not in value:
            raise GenerationError(f"unavailable rendering reference: {name}")
        value = value[part]
    return value


def _evaluate(nodes, context, *, html=False):
    pieces = []
    for node in nodes:
        if isinstance(node, Text):
            pieces.append(node.value)
        elif isinstance(node, Variable):
            value = _lookup(context, node.name)
            if not isinstance(value, str):
                raise GenerationError(f"non-scalar rendering reference: {node.name}")
            pieces.append(escape(value, quote=True) if html else value)
        elif isinstance(node, IfBlock):
            branch = node.yes if _lookup(context, node.name, condition=True) else node.no
            pieces.append(_evaluate(branch, context, html=html))
        elif isinstance(node, EachBlock):
            values = _lookup(context, node.name)
            if not isinstance(values, tuple):
                raise GenerationError(f"invalid rendering collection: {node.name}")
            for value in values:
                if not isinstance(value, str):
                    raise GenerationError(f"unsupported collection item: {node.name}")
                pieces.append(_evaluate(node.body, {"this": value}, html=html))
        else:
            raise GenerationError("unsupported rendering node")
    return "".join(pieces)


# Recognize the complete canonical initialization shape. Capture the public
# headings and the category/entry patterns; discard only the editorial guide
# and the illustrative release. No general angle-bracket substitution.
_CHANGELOG = re.compile(
    r"(?P<title># Changelog)\n\n(?P<unreleased>## \[Unreleased\])\n\n"
    r"<!--\nAñadir únicamente las categorías que contengan cambios\.\n\n"
    r"Categorías recomendadas:\nAdded\nChanged\nDeprecated\nRemoved\nFixed\nSecurity\n-->\n\n"
    r"(?P<category>### <CATEGORY>)\n\n(?P<entry>- <CHANGE_DESCRIPTION>)\n\n"
    r"---\n\n## \[<VERSION>\] - <YYYY-MM-DD>\n\n"
    r"### <CATEGORY>\n\n- <CHANGE_DESCRIPTION>\n*"
)


def _changelog(source, project):
    match = _CHANGELOG.fullmatch(source)
    if match is None:
        raise GenerationError("DOC-CHANGELOG: unsupported canonical initialization shape")
    sections = [match["title"], match["unreleased"]]
    for category, entries in project.unreleased_changes:
        heading = match["category"].replace("<CATEGORY>", category)
        lines = [match["entry"].replace("<CHANGE_DESCRIPTION>", entry) for entry in entries]
        sections.append(heading + "\n\n" + "\n".join(lines))
    return "\n\n".join(sections) + "\n"


# These are the two canonical list-loop shapes for the supported 0.1.0
# text-only profile. Collapse only template-owned loop separators, never
# user-supplied item contents or free-form Markdown.
_LIST_LOOPS = {
    "README-FEATURES": ("features", "## ✨ Features"),
    "README-DOCUMENTATION": ("documents", "## 📚 Documentation"),
}


def _compact_canonical_list_source(identity, source):
    field, heading = _LIST_LOOPS[identity]
    expected = f"{heading}\n\n{{{{#each {field}}}}}\n\n- {{{{ this }}}}\n\n{{{{/each}}}}"
    if source != expected:
        raise GenerationError(f"{identity}: unsupported list whitespace structure")
    # The loop body is a single list line and one LF. Do not touch values.
    return f"{heading}\n\n{{{{#each {field}}}}}- {{{{ this }}}}\n{{{{/each}}}}"


def _compact_hero_separators(rendered):
    """Strip blank lines left by disabled template-only visual/optional blocks.

    Hero inputs are strictly one-line and HTML escaped, so these separators
    cannot be author-authored multiline Markdown. Other fragments are untouched.
    """
    return re.sub(r"\n{3,}", "\n\n", rendered)


def render_component(component: SelectedComponent, project: ProjectInput) -> str:
    """Render one canonical artifact in memory; input data is never parsed as syntax."""
    identity = component.id
    if identity not in _SUPPORTED or component.version != _SUPPORTED[identity]:
        raise GenerationError(f"unsupported rendering contract: {identity} {component.version}")
    source = component.template.replace("\r\n", "\n").replace("\r", "\n")
    if identity == "DOC-CHANGELOG":
        return _changelog(source, project)

    # Audit the whole source before the Hero editorial comment is removed.
    nodes = parse_component(identity, source)
    if identity == "README-HERO":
        source = re.sub(r"\A<!--.*?-->\s*", "", source, count=1, flags=re.S)
        nodes = parse_component(identity, source)
    if identity in _LIST_LOOPS:
        source = _compact_canonical_list_source(identity, source)
        nodes = parse_component(identity, source)
    rendered = _evaluate(nodes, _context(project), html=identity == "README-HERO")
    if identity == "README-HERO":
        rendered = _compact_hero_separators(rendered)
    if not rendered.strip():
        raise GenerationError(f"{identity}: empty rendered fragment")
    # No global whitespace normalization: preserve literal Markdown content.
    return rendered
