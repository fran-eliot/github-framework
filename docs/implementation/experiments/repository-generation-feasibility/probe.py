"""Bounded feasibility probe, not a production generator. Python 3.11+, Jinja2 3.1.6."""
import hashlib
import html
import json
import platform
import re
import sys
import tempfile
from pathlib import Path

import jinja2

SOURCES = {
    "hero": ("framework/components/readme/hero/template.md", "ab9ce2d2dc9587be8641773c654673eac82dedbc"),
    "overview": ("framework/components/readme/overview/template.md", "baace9693255174158a35d63b42beeae4a268ca3"),
    "changelog": ("framework/components/documentation/changelog/template.md", "390a025ff9b71ecce3855021841912f1438a6b62"),
}
FIXTURE = {
    "project_name": "Sample Backend",
    "tagline": "A documentation seed for a sample backend.",
    "overview": "This synthetic backend project demonstrates a documentation seed assembled from reusable GitHub Framework components. No running service is claimed.",
}
CHANGE = "Initial documentation seed."
TOKEN = re.compile(r"(\{\{.*?\}\})", re.S)
IDENT = re.compile(r"[a-z_]+(?:\.[a-z_]+)?")


def require(test, message):
    if not test:
        raise ValueError(message)


def load(root):
    result = {}
    for key, (path, sha) in SOURCES.items():
        data = (root / path).read_bytes()
        digest = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        require(digest == sha, "source blob mismatch: " + path)
        result[key] = data.decode("utf-8")
    return result


def inputs(values):
    data = {"alignment": "center", "banner": {}, "badges": [], "short_description": "", **values}
    for key, low, high in [("project_name", 2, 60), ("tagline", 10, 100), ("overview", 80, 1200), ("short_description", 0, 240)]:
        value = data.get(key)
        require(isinstance(value, str) and low <= len(value) <= high, "invalid or missing " + key)
        require(not any(marker in value for marker in ("{{", "}}", "{%", "<CATEGORY>")), "placeholder-shaped input")
    require(data["alignment"] in ("center", "left"), "invalid alignment")
    banner = data["banner"]
    require(isinstance(banner, dict), "invalid banner")
    if banner:
        require(all(isinstance(banner.get(k), str) and banner[k] for k in ("source", "alt")), "invalid banner fields")
        data["banner"] = {"link": "", **banner}
    badges = data["badges"]
    require(isinstance(badges, list) and len(badges) <= 6, "invalid badges")
    for badge in badges:
        require(isinstance(badge, dict) and all(isinstance(badge.get(k), str) and badge[k] for k in ("image", "alt")), "invalid badge fields")
    data["badges"] = [{"link": "", **badge} for badge in badges]
    return data


def parse(template):
    require("{%" not in template and not re.search(r"(?<!\{)\{#", template), "foreign syntax")
    tokens = TOKEN.split(template)
    root, stack = [], []
    current = root
    for token in tokens:
        if not token.startswith("{{"):
            require("{{" not in token and "}}" not in token, "unclosed token")
            current.append(("text", token))
            continue
        expr = token[2:-2].strip()
        if expr.startswith("#if ") or expr.startswith("#each "):
            kind, name = expr[1:].split(" ", 1)
            require(IDENT.fullmatch(name), "unsupported block expression")
            node = (kind, name, [], [])
            current.append(node)
            stack.append((node, current))
            current = node[2]
        elif expr == "else":
            require(stack and stack[-1][0][0] == "if" and current is stack[-1][0][2], "invalid else")
            current = stack[-1][0][3]
        elif expr in ("/if", "/each"):
            require(stack and stack[-1][0][0] == expr[1:], "unbalanced block")
            _, current = stack.pop()
        else:
            require(IDENT.fullmatch(expr), "unsupported expression: " + expr)
            current.append(("var", expr))
    require(not stack, "unclosed block")
    return root


def lookup(name, scope):
    value = scope
    for key in name.split("."):
        require(isinstance(value, dict) and key in value, "unknown input " + name)
        value = value[key]
    return value


def direct(nodes, data, escape):
    out = []
    for kind, value, *parts in nodes:
        if kind == "text":
            out.append(value)
        elif kind == "var":
            item = str(lookup(value, data))
            out.append(html.escape(item, quote=True).replace("&#x27;", "&#39;").replace("&quot;", "&#34;") if escape else item)
        elif kind == "if":
            out.append(direct(parts[0] if lookup(value, data) else parts[1], data, escape))
        else:
            require(value == "badges", "unsupported iteration")
            for item in lookup(value, data):
                out.append(direct(parts[0], {**data, **item}, escape))
    return "".join(out)


def translate(nodes, loop=False):
    out = []
    for kind, value, *parts in nodes:
        expr = "badge." + value if loop and value in ("link", "image", "alt") else value
        if kind == "text":
            out.append(value)
        elif kind == "var":
            out.append("{{ " + expr + " }}")
        elif kind == "if":
            out.extend(["{% if " + expr + " %}", translate(parts[0], loop), "{% else %}", translate(parts[1], loop), "{% endif %}"])
        else:
            require(value == "badges" and not loop, "unsupported iteration")
            out.extend(["{% for badge in badges %}", translate(parts[0], True), "{% endfor %}"])
    return "".join(out)


def render(template, data, engine, escape):
    nodes = parse(template)
    if engine == "direct":
        return direct(nodes, data, escape)
    require(engine == "jinja", "unknown engine")
    env = jinja2.Environment(undefined=jinja2.StrictUndefined, autoescape=escape, keep_trailing_newline=True)
    return env.from_string(translate(nodes)).render(**data)


def normalize(text):
    return re.sub(r"\n{3,}", "\n\n", text.strip())


def assemble(sources, values, engine):
    data = inputs(values)
    hero = re.sub(r"\A<!--.*?-->\s*", "", sources["hero"], count=1, flags=re.S)
    sections = [normalize(render(hero, data, engine, True)), normalize(render(sources["overview"], data, engine, False))]
    readme = "\n\n".join(sections) + "\n"
    # Explicit editorial projection: only the initial Unreleased heading, not the release example.
    require(sources["changelog"].startswith("# Changelog\n\n## [Unreleased]\n"), "changelog source mismatch")
    changelog = "\n".join(sources["changelog"].splitlines()[:3]) + "\n\n### Added\n\n- " + CHANGE + "\n"
    require(len(re.findall(r"(?im)^\s*(?:<h1\b|# )", readme)) == 1, "expected exactly one H1")
    for body in (readme, changelog):
        require(not re.search(r"\{\{|\}\}|<(?:CATEGORY|CHANGE_DESCRIPTION|VERSION|YYYY-MM-DD)>", body), "unresolved placeholder")
    return [("README.md", readme.encode("utf-8")), ("CHANGELOG.md", changelog.encode("utf-8"))]


def materialize(root, name, artifacts):
    require(re.fullmatch(r"[a-z][a-z0-9-]*", name), "unsafe destination")
    names = [p for p, _ in artifacts]
    require(len(names) == 2 and set(names) == {"README.md", "CHANGELOG.md"}, "unsafe, missing or colliding artifact names")
    target = root / name
    require(not target.exists() and not target.is_symlink(), "destination already exists")
    target.mkdir()
    for path, data in artifacts:
        with (target / path).open("xb") as stream:
            stream.write(data)
    return {path: hashlib.sha256((target / path).read_bytes()).hexdigest() for path, _ in artifacts}


def reject(call):
    try:
        call()
    except (ValueError, jinja2.UndefinedError):
        return
    raise AssertionError("expected rejection")


def main(root):
    sources = load(root)
    expected = [
        ("README.md", ('<h1 align="center">\n  Sample Backend\n</h1>\n\n<p align="center">\n  <strong>A documentation seed for a sample backend.</strong>\n</p>\n\n## 📖 Overview\n\n' + FIXTURE["overview"] + "\n").encode()),
        ("CHANGELOG.md", b"# Changelog\n\n## [Unreleased]\n\n### Added\n\n- Initial documentation seed.\n"),
    ]
    full = {**FIXTURE, "project_name": "Sample & Backend", "banner": {"source": "assets/example.svg", "alt": "Example & illustration", "link": "https://example.invalid/"}, "badges": [{"image": "badge-a.svg", "alt": "A", "link": "https://example.invalid/a"}, {"image": "badge-b.svg", "alt": "B"}], "short_description": "A synthetic example."}
    outputs = {}
    with tempfile.TemporaryDirectory(prefix="gf-feasibility-") as temp:
        dest = Path(temp)
        for engine in ("direct", "jinja"):
            artifacts = assemble(sources, FIXTURE, engine)
            assert artifacts == expected, engine + " differs from hand-authored reference"
            first = materialize(dest, engine + "-a", artifacts)
            second = materialize(dest, engine + "-b", assemble(sources, FIXTURE, engine))
            assert first == second
            outputs[engine] = first
            for key in FIXTURE:
                reject(lambda: assemble(sources, {k:v for k,v in FIXTURE.items() if k != key}, engine))
            for bad in ({**FIXTURE,"project_name":"x"}, {**FIXTURE,"tagline":"short"}, {**FIXTURE,"overview":"short"}, {**FIXTURE,"overview":"x"*1201}, {**FIXTURE,"alignment":"bad"}, {**FIXTURE,"banner":{"source":"a.svg"}}, {**FIXTURE,"badges":[{"image":"a.svg","alt":"A"}]*7}, {**FIXTURE,"project_name":"{{ unknown }}"}):
                reject(lambda: assemble(sources, bad, engine))
            reject(lambda: render("{{#unless banner}}x{{/unless}}", inputs(FIXTURE), engine, True))
            reject(lambda: render("{{ unknown }}", inputs(FIXTURE), engine, True))
            reject(lambda: render("{{#if banner}}", inputs(FIXTURE), engine, True))
            reject(lambda: render("{{#if banner}}{{#unless banner}}x{{/unless}}{{/if}}", inputs(FIXTURE), engine, True))
            reject(lambda: materialize(dest, engine + "-a", artifacts))
            assert first == {p:hashlib.sha256((dest / (engine + "-a") / p).read_bytes()).hexdigest() for p,_ in artifacts}
            existing_file = dest / (engine + "-file")
            existing_file.write_bytes(b"sentinel")
            reject(lambda: materialize(dest, existing_file.name, artifacts))
            assert existing_file.read_bytes() == b"sentinel"
            before = sorted(p.name for p in dest.iterdir())
            reject(lambda: materialize(dest, "../escape", artifacts))
            reject(lambda: materialize(dest, "unsafe", [("../escape", b"x"), artifacts[1]]))
            reject(lambda: materialize(dest, "collision", [artifacts[0], artifacts[0]]))
            assert before == sorted(p.name for p in dest.iterdir())
        assert outputs["direct"] == outputs["jinja"]
        a = assemble(sources, full, "direct")
        b = assemble(sources, full, "jinja")
        assert a == b
        assert b"Sample &amp; Backend" in a[0][1] and b"Example &amp; illustration" in a[0][1]
        assert a[0][1].count(b'<img') == 3 and a[0][1].count(b'<a href=') == 2
        plain = {**full, "banner": {"source": "assets/example.svg", "alt": "Example"}}
        assert assemble(sources, plain, "direct") == assemble(sources, plain, "jinja")
        assert b'<a href="https://example.invalid/">' not in assemble(sources, plain, "direct")[0][1]
        assert load(root) == sources
    print(json.dumps({"python": platform.python_version(), "platform": platform.system(), "jinja2": jinja2.__version__, "fixture": FIXTURE, "sha256": outputs, "checks": "reference, repeatability, optional branches, invalid inputs/syntax, destination safety, source bytes: PASS"}, indent=2))


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("run without Python optimization")
    main(Path(sys.argv[1]))
