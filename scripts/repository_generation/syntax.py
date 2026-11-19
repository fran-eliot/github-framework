"""Bounded syntax and static scope audit for canonical README fragments."""
from dataclasses import dataclass
import re

from . import GenerationError

_NAME = re.compile(r"[a-z_][a-z0-9_]*(?:\.[a-z_][a-z0-9_]*)*")
_DELIMITER = re.compile(r"\{\{|\}\}|\{%|%\}|\{#|#\}")
_MAX_DEPTH = 32


@dataclass(frozen=True)
class Text:
    value: str


@dataclass(frozen=True)
class Variable:
    name: str


@dataclass(frozen=True)
class IfBlock:
    name: str
    yes: tuple["Node", ...]
    no: tuple["Node", ...]


@dataclass(frozen=True)
class EachBlock:
    name: str
    body: tuple["Node", ...]


Node = Text | Variable | IfBlock | EachBlock


def _tokens(source):
    pos = 0
    while match := _DELIMITER.search(source, pos):
        start = match.start()
        if start > pos:
            yield Text(source[pos:start])
        if match.group() != "{{":
            raise GenerationError(f"unsupported or stray delimiter at offset {start}")
        end = source.find("}}", start + 2)
        if end < 0:
            raise GenerationError(f"unclosed template token at offset {start}")
        value = source[start + 2:end]
        if _DELIMITER.search(value) or "{" in value or "}" in value or source[end + 2:end + 3] == "}":
            raise GenerationError(f"unsupported token at offset {start}")
        yield value.strip()
        pos = end + 2
    if pos < len(source):
        yield Text(source[pos:])


def parse(source: str) -> tuple[Node, ...]:
    """Parse the restricted grammar; no evaluation or user-content interpolation."""
    if not isinstance(source, str):
        raise GenerationError("template source must be text")
    tokens = iter(_tokens(source))

    def sequence(stops, depth):
        if depth > _MAX_DEPTH:
            raise GenerationError("template nesting limit exceeded")
        nodes = []
        for token in tokens:
            if isinstance(token, Text):
                nodes.append(token)
            elif token in stops:
                return tuple(nodes), token
            elif token in ("else", "/if", "/each"):
                raise GenerationError(f"unexpected block terminator: {token}")
            elif _NAME.fullmatch(token):
                nodes.append(Variable(token))
            elif block := re.fullmatch(r"#(if|each)\s+(.+)", token):
                kind, name = block.groups()
                if not _NAME.fullmatch(name):
                    raise GenerationError(f"unsupported block expression: {token}")
                body, stop = sequence({"else", "/if"} if kind == "if" else {"/each"}, depth + 1)
                if kind == "each":
                    nodes.append(EachBlock(name, body))
                else:
                    alternate = ()
                    if stop == "else":
                        alternate, _ = sequence({"/if"}, depth + 1)
                    nodes.append(IfBlock(name, body, alternate))
            else:
                raise GenerationError(f"unsupported template expression: {token}")
        if stops:
            raise GenerationError("unclosed template block")
        return tuple(nodes), None

    return sequence(set(), 0)[0]


# (root variables, root conditions, permitted collection)
_POLICIES = {
    "README-HERO": (
        frozenset(("project_name", "tagline", "short_description", "alignment", "banner.source", "banner.alt", "banner.link")),
        frozenset(("banner", "banner.link", "badges", "short_description")), "badges",
    ),
    "README-OVERVIEW": (frozenset(("overview",)), frozenset(), None),
    "README-FEATURES": (frozenset(), frozenset(), "features"),
    "README-TECH-STACK": (frozenset(("technologies",)), frozenset(), None),
    "README-QUICK-START": (frozenset(("prerequisites", "installation", "execution")), frozenset(), None),
    "README-DOCUMENTATION": (frozenset(), frozenset(), "documents"),
    "README-FOOTER": (frozenset(("footer",)), frozenset(), None),
}


def audit(component_id: str, nodes: tuple[Node, ...]) -> None:
    """Audit every branch and loop body, including disabled visual branches."""
    if component_id not in _POLICIES:
        raise GenerationError(f"unsupported template policy: {component_id}")
    root_vars, root_conditions, collection = _POLICIES[component_id]

    def walk(items, scope=None):
        variables, conditions = root_vars, root_conditions
        if scope == "badges":
            variables, conditions = frozenset(("image", "alt", "link")), frozenset(("link",))
        elif scope is not None:
            variables, conditions = frozenset(("this",)), frozenset()
        for node in items:
            if isinstance(node, Text):
                continue
            if isinstance(node, Variable):
                if node.name not in variables:
                    raise GenerationError(f"{component_id}: unknown or out-of-scope variable {node.name}")
            elif isinstance(node, IfBlock):
                if node.name not in conditions:
                    raise GenerationError(f"{component_id}: unsupported condition {node.name}")
                walk(node.yes, scope)
                walk(node.no, scope)
            elif isinstance(node, EachBlock):
                if scope is not None or node.name != collection:
                    raise GenerationError(f"{component_id}: unsupported iteration {node.name}")
                walk(node.body, node.name)
            else:
                raise GenerationError(f"{component_id}: unsupported node")

    walk(nodes)


def parse_component(component_id: str, source: str) -> tuple[Node, ...]:
    nodes = parse(source)
    audit(component_id, nodes)
    return nodes
