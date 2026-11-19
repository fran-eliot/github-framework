"""Experiment II: strict preflight for the original three-Component probe."""
import json
import platform
import re
import sys
import tempfile
from dataclasses import replace
from pathlib import Path
from urllib.parse import urlsplit

import yaml
import probe

SELECTED = {
    "README-HERO": ("hero", "1.0.0"),
    "README-OVERVIEW": ("overview", "1.0.0"),
    "DOC-CHANGELOG": ("changelog", "0.1.0"),
}


def select(result):
    probe.require(result.template.id == "TPL-BACKEND" and result.template.version == "0.1.0", "unexpected Template")
    refs = [ref for group in result.groups for ref in group.references if ref.id in SELECTED]
    probe.require([ref.id for ref in refs] == list(SELECTED), "selection missing, repeated or reordered")
    for ref in refs:
        probe.require(ref.outcome == "Resolved", f"{ref.id}: {ref.outcome}")
        key, version = SELECTED[ref.id]
        expected = str(Path(probe.SOURCES[key][0]).with_name("metadata.yml").as_posix())
        probe.require(len(ref.physical) == 1 and ref.physical[0].path == expected and ref.physical[0].version == version, "selected identity differs from pinned artifact")
    return refs


def string(value, label):
    probe.require(isinstance(value, str) and bool(value.strip()), "invalid " + label)
    probe.require(not re.search(r"\{\{|\}\}|\{%|%\}|<(?:CATEGORY|CHANGE_DESCRIPTION|VERSION|YYYY-MM-DD)>", value), "placeholder-shaped " + label)


def link(value, label):
    string(value, label)
    parsed = urlsplit(value)
    probe.require(parsed.scheme in ("http", "https") and bool(parsed.netloc) and not any(c.isspace() for c in value), "invalid " + label)


def strict_inputs(values):
    allowed = set(probe.FIXTURE) | {"alignment", "banner", "badges", "short_description"}
    probe.require(isinstance(values, dict) and set(values) <= allowed, "unknown root input")
    for key in probe.FIXTURE:
        string(values.get(key), key)
    if "short_description" in values and values["short_description"] != "":
        string(values["short_description"], "short_description")
    banner = values.get("banner", {})
    probe.require(isinstance(banner, dict) and set(banner) <= {"source", "alt", "link"}, "invalid banner fields")
    if banner:
        for key in ("source", "alt"):
            string(banner.get(key), "banner." + key)
        if "link" in banner:
            link(banner["link"], "banner.link")
    badges = values.get("badges", [])
    probe.require(isinstance(badges, list), "invalid badges")
    for badge in badges:
        probe.require(isinstance(badge, dict) and set(badge) <= {"image", "alt", "link"}, "invalid badge fields")
        for key in ("image", "alt"):
            string(badge.get(key), "badge." + key)
        if "link" in badge:
            link(badge["link"], "badge.link")
    probe.inputs(values)  # Preserve original scalar lengths, alignment and count checks.


def audit(nodes, component, inside_badges=False):
    hero_vars = {"project_name", "tagline", "short_description", "alignment", "banner.source", "banner.alt", "banner.link"}
    vars_allowed = hero_vars if component == "hero" else {"overview"}
    conditions = {"banner", "banner.link", "badges", "short_description"} if component == "hero" else set()
    if inside_badges:
        vars_allowed |= {"image", "alt", "link"}
        conditions |= {"link"}
    for kind, name, *parts in nodes:
        if kind == "text":
            continue
        if kind == "var":
            probe.require(name in vars_allowed, "unknown variable: " + name)
        elif kind == "if":
            probe.require(name in conditions, "unknown condition: " + name)
            audit(parts[0], component, inside_badges)
            audit(parts[1], component, inside_badges)
        elif kind == "each":
            probe.require(component == "hero" and name == "badges" and not inside_badges, "unsupported iteration")
            audit(parts[0], component, True)
        else:
            raise ValueError("unsupported node")


def preflight(result, sources, values, engine):
    select(result)
    strict_inputs(values)
    hero = re.sub(r"\A<!--.*?-->\s*", "", sources["hero"], count=1, flags=re.S)
    audit(probe.parse(hero), "hero")
    audit(probe.parse(sources["overview"]), "overview")
    return probe.assemble(sources, values, engine)


def reject(call, message):
    try:
        call()
    except ValueError as exc:
        assert message in str(exc), (message, str(exc))
        return
    raise AssertionError("expected rejection: " + message)


def main(root):
    sys.path.insert(0, str(root))
    from scripts.template_composition_preview.registry import load_registry
    from scripts.template_composition_preview.resolution import resolve_composition
    from scripts.template_composition_preview.sources import discover_physical, load_template

    template, registry, physical = load_template(root, "TPL-BACKEND"), load_registry(root), discover_physical(root)
    result = resolve_composition(template, registry, physical)
    assert result.counts == dict(Resolved=16, Conceptual=12, Unknown=0, Inconsistent=0, Ambiguous=0)
    assert [r.id for r in select(result)] == list(SELECTED)
    sources = probe.load(root)
    hero = "README-HERO"
    no_registry = {k: v for k, v in registry.items() if k != hero}
    no_physical = {k: v for k, v in physical.items() if k != hero}
    conceptual = {**registry, hero: replace(registry[hero], classification="Conceptual")}
    duplicate = {**physical, hero: (*physical[hero], replace(physical[hero][0], path="fixture/duplicate/metadata.yml"))}
    conflicts = [(conceptual, no_physical, "Conceptual"), (no_registry, no_physical, "Unknown"), (registry, no_physical, "Inconsistent"), (registry, duplicate, "Ambiguous")]
    fixture = probe.FIXTURE
    valid = {**fixture, "banner": {"source": "assets/x.svg", "alt": "Example", "link": "https://example.invalid/"}, "badges": [{"image": "a.svg", "alt": "A", "link": "https://example.invalid/a"}, {"image": "b.svg", "alt": "B"}], "short_description": "A synthetic example."}
    invalid = [({**fixture, "banner": {"source": "x.svg", "alt": "X", "link": 123}}, "banner.link"), ({**fixture, "badges": [{"image": "x.svg", "alt": "X", "link": False}]}, "badge.link"), ({**fixture, "banner": {"source": "x.svg", "alt": "X", "link": "javascript:bad"}}, "banner.link"), ({**fixture, "badges": [{"image": "x.svg", "alt": "{{ unknown }}"}]}, "badge.alt"), ({**fixture, "unknown": True}, "unknown root input"), ({**fixture, "banner": {"source": "x.svg", "alt": "X", "extra": True}}, "invalid banner fields"), ({**fixture, "badges": [{"image": "x.svg", "alt": "X", "extra": True}]}, "invalid badge fields")]
    invalid_sources = [({**sources, "hero": sources["hero"] + "{{#if banner}}{{ unknown }}{{/if}}"}, "unknown variable"), ({**sources, "hero": sources["hero"] + "{{#each badges}}{{ unknown }}{{/each}}"}, "unknown variable"), ({**sources, "hero": sources["hero"] + "{{#if banner}}{{#if unknown}}x{{/if}}{{/if}}"}, "unknown condition"), ({**sources, "hero": sources["hero"] + "{{ image }}"}, "unknown variable"), ({**sources, "overview": sources["overview"] + "{{ tagline }}"}, "unknown variable")]
    hashes = {}
    with tempfile.TemporaryDirectory(prefix="gf-refinement-") as temp:
        dest = Path(temp)
        for engine in ("direct", "jinja"):
            for reg, phy, outcome in conflicts:
                conflict = resolve_composition(template, reg, phy)
                reject(lambda: probe.materialize(dest, "rejected", preflight(conflict, sources, fixture, engine)), outcome)
                assert not (dest / "rejected").exists()
            for values, message in invalid:
                reject(lambda: probe.materialize(dest, "rejected", preflight(result, sources, values, engine)), message)
                assert not (dest / "rejected").exists()
            for altered, message in invalid_sources:
                reject(lambda: probe.materialize(dest, "rejected", preflight(result, altered, fixture, engine)), message)
                assert not (dest / "rejected").exists()
            assert preflight(result, sources, valid, engine) == probe.assemble(sources, valid, engine)
            artifacts = preflight(result, sources, fixture, engine)
            assert artifacts == probe.assemble(sources, fixture, engine)
            hashes[engine] = probe.materialize(dest, engine + "-refined", artifacts)
            assert hashes[engine] == probe.materialize(dest, engine + "-repeat", preflight(result, sources, fixture, engine))
        assert hashes["direct"] == hashes["jinja"] == {"README.md": "76fdbac91226ed9475846f937c04c8fa79bc921893d0c46056bed6ea40167f02", "CHANGELOG.md": "92a499cb2fdc0dd320ee1f10f88ab679beda944f4433381353b1da1996a91cdb"}
        assert probe.load(root) == sources
    print(json.dumps({"environment": [platform.system(), platform.python_version(), yaml.__version__, probe.jinja2.__version__], "registry": len(registry), "physical": len(physical), "outcomes": result.counts, "selected": [r.id for r in select(result)], "conflict_cases_per_engine": len(conflicts), "invalid_inputs_per_engine": len(invalid), "invalid_template_cases_per_engine": len(invalid_sources), "hashes": hashes, "result": "PASS (bounded)"}, indent=2))


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("run without Python optimization")
    main(Path(sys.argv[1]).resolve())
