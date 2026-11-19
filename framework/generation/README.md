# Repository Generation Guide

> **Unreleased capability.** This guide describes Repository Generation Core in a Framework checkout containing the implementation. It is not a feature of the published v0.12.0 release.

## What you can generate

Supply your project facts, inspect a generation plan and create a fresh local directory containing README.md and CHANGELOG.md. The supported profile is TPL-BACKEND 0.1.0, text-only, with eight required Component references.

The generator does not create application code, install or run the application, initialize Git, publish a remote repository or update an existing project. It does not certify full Template conformance or validate the truth of the project facts supplied.

## 1. Prepare your environment

Use Python 3.11 and the existing PyYAML 6.0.2 dependency. Open a terminal in a Framework checkout containing this guide. If needed, use an isolated Python environment and install the dependency:

```sh
python --version
python -m pip install PyYAML==6.0.2
python -B -m scripts.repository_generation --help
```

The installation command may require access to a package index; the generator itself performs no network operations. On systems where Python 3.11 is invoked as python3.11 or py -3.11, use that interpreter consistently.

## 2. Prepare project facts

Start with [backend-project.json](examples/backend-project.json). It is a complete, fictional example, not evidence of a working API. For your own project, copy the JSON to a separate input file and replace all illustrative facts with your own. Use UTF-8 JSON without a byte order mark.

| Field | Required | Contract |
| --- | --- | --- |
| project_name | Yes | Single-line string, 2–60 characters |
| tagline | Yes | Single-line string, 10–100 characters |
| overview | Yes | Markdown string, 80–1200 characters |
| features | Yes | Nonempty ordered array of nonblank single-line strings |
| technologies | Yes | Nonempty ordered array of nonblank single-line strings |
| prerequisites | Yes | Nonblank Markdown string |
| installation | Yes | Nonblank Markdown string |
| execution | Yes | Nonblank Markdown string |
| documents | Yes | Nonempty ordered array of nonblank single-line strings |
| footer | Yes | Nonblank Markdown string |
| short_description | No | Single-line string, at most 240 characters; default empty |
| alignment | No | left or center; default center |
| unreleased_changes | No | Object containing supported categories with nonempty ordered arrays of nonblank single-line strings; default empty object |

Supported categories, in output order: Added, Changed, Deprecated, Removed, Fixed, Security. Omit categories without changes. An empty object creates a Changelog with an empty Unreleased section. No historical release is invented.

Duplicate or unknown fields, nulls where strings/lists/objects are required, unsupported visual inputs, invalid lengths and whitespace-only required values are rejected. JSON escapes such as \n may represent Markdown line breaks. CRLF/CR in multiline Markdown is normalized to LF. Do not introduce extra H1 headings; use lower-level headings when appropriate. The heading check is bounded, not a complete Markdown parser. Content is trusted author-provided Markdown, not sanitized arbitrary input. Placeholder-like user text is literal and commands in documentation are never executed.

## 3. Choose a new destination

The parent must already exist outside the Framework checkout. Use a fresh local directory name (1–63 lower-case ASCII letters, digits and hyphens; start with a letter, no trailing hyphen, no Windows reserved device name). Existing directories, files and dangling links are rejected. Linked/reparse-point ancestors and parent traversal are unsupported.

The examples create a fresh temporary parent outside the checkout. If your temporary directory is inside the checkout or accessed through a link, choose a different existing external parent.

### PowerShell

Run from the Framework root:

```powershell
$parent = (New-Item -ItemType Directory -Path (Join-Path ([System.IO.Path]::GetTempPath()) ("framework-generation-" + [guid]::NewGuid().ToString("N")))).FullName
python -B -m scripts.repository_generation plan TPL-BACKEND --template-version 0.1.0 --input framework/generation/examples/backend-project.json --output-parent "$parent" --name atlas-sample
$LASTEXITCODE
Test-Path (Join-Path $parent "atlas-sample")
```

Expected: exit 0 and False. Review the report before continuing.

```powershell
python -B -m scripts.repository_generation generate TPL-BACKEND --template-version 0.1.0 --input framework/generation/examples/backend-project.json --output-parent "$parent" --name atlas-sample
$LASTEXITCODE
Get-ChildItem -LiteralPath (Join-Path $parent "atlas-sample")
Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $parent "atlas-sample/README.md"), (Join-Path $parent "atlas-sample/CHANGELOG.md")
```

### Bash (Linux)

Run from the Framework root:

```bash
parent="$(mktemp -d)"
python -B -m scripts.repository_generation plan TPL-BACKEND --template-version 0.1.0 --input framework/generation/examples/backend-project.json --output-parent "$parent" --name atlas-sample
echo "$?"
test ! -e "$parent/atlas-sample"
echo "$?"
```

Expected: both exit codes 0. Review the report before continuing.

```bash
python -B -m scripts.repository_generation generate TPL-BACKEND --template-version 0.1.0 --input framework/generation/examples/backend-project.json --output-parent "$parent" --name atlas-sample
echo "$?"
ls -la "$parent/atlas-sample"
sha256sum "$parent/atlas-sample/README.md" "$parent/atlas-sample/CHANGELOG.md"
```

## 4. Understand the report and inspect results

Both operations perform the same input, canonical composition and rendering preflight. Plan creates no destination files. Generate repeats preflight and creates the new child exclusively; it does not consume a saved plan.

On the current profile, expect eight selected required references and twenty unselected recommended/optional references. Resolution outcomes and selection are distinct. The report includes selected versions and source paths, direct dependencies, the VCL-HERO conceptual limitation, intended or written paths, and SHA-256 digests.

Inspect the two generated files:

- README.md: project title and tagline, overview, features, tech stack, quick start, documentation and footer in canonical order.
- CHANGELOG.md: Unreleased with the supplied Added entry, but no invented version.

Compare the two printed SHA-256 values with your hash command output (hexadecimal case does not matter). With unchanged input and sources, plan and generate should report identical document digests. Review the actual content for accuracy and suitability. The example commands above are documented expected behavior, not a recorded execution result.

## 5. Troubleshooting and recovery

| Exit code | Meaning | Action |
| --- | --- | --- |
| 0 | Successful help, plan or generation | Review the report and, after generate, inspect both files |
| 1 | Destination, write or verification error | Read stderr; use a valid fresh destination or inspect incomplete output |
| 2 | Argument, input, source or rendering contract error | Read stderr, correct the request or restore compatible canonical sources, then rerun plan |

A repeated generation into the same child must fail rather than overwrite. To compare a second successful generation, use a different fresh child name.

If a write fails after the new directory was created, the error identifies the incomplete path for manual inspection. Nothing is automatically deleted. Do not treat incomplete output as a successful generation. After confirming ownership and reviewing its contents, decide whether to remove it manually or leave it and use a fresh name. Never remove an unrelated directory to make generation succeed.

## 6. Known limitations

The required visual dependency VCL-HERO 1.0.0 remains Conceptual, as do the recommended VCL-BANNER and VCL-BADGES dependencies. This profile intentionally produces a text-only Hero and rejects banner/badge input. The eight selected references do not establish full Template or transitive dependency conformance. Optional/recommended selection, other Templates, visual assets, application scaffolding, existing-repository updates and lifecycle manifests are outside scope.

The adapter supports a bounded canonical syntax, not general Handlebars. Source reads are not an atomic snapshot. Destination checks do not guarantee protection against concurrent hostile filesystem changes or filesystem-wide atomicity. The generator verifies written bytes but is not a runtime or security certification.

For implementation details and acceptance boundaries see the [Delivery Scope](../../docs/implementation/repository-generation-core-delivery-scope.md) and [Implementation Plan](../../docs/implementation/repository-generation-core-implementation-plan.md).
