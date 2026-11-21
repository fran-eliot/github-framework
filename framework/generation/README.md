# Repository Generation Guide

> **Unreleased capability.** This guide describes Repository Generation Core in a Framework checkout containing the implementation. It is not a feature of the published v0.12.0 release.

## What you can generate

Supply your project facts, inspect a generation plan and create a fresh local directory containing README.md and CHANGELOG.md. The supported profile is TPL-BACKEND 0.1.0, text-only, with eight required Component references.

The generator does not create application code, install or run the application, initialize Git, publish a remote repository or update an existing project. It does not certify full Template conformance or validate the truth of the project facts supplied.

## Start here — three steps

**This is a documentation generator, not a backend application generator.** It creates only two files in a **new** directory you choose: `README.md` and `CHANGELOG.md`. It cannot overwrite an existing destination. For now it supports one profile, `TPL-BACKEND 0.1.0`, and needs a JSON file containing your own project facts.

1. **Plan** — Preview the intended files and their hashes. No output directory is created.
2. **Generate** — Recheck the same information and create those two files in a fresh directory.
3. **Inspect** — Open both files; review accuracy and compare the printed SHA-256 hashes if needed. Inspect only **after** generate.

For a safe first try, use the [complete fictional JSON example](examples/backend-project.json) and the PowerShell/Bash commands in section 3 below. Set up Python and PyYAML (section 1) first. To document your **own** project, copy and replace the fictional JSON fields (section 2). No technology, feature or application command is inferred for you.

### How to read `plan` and `generate` output

| Report item | Meaning for you |
| --- | --- |
| `Template: TPL-BACKEND 0.1.0` | The single supported documentation profile |
| `Selected` / `Unselected` | Used in your generated files / listed for transparency but **not** generated |
| `Resolved` / `Conceptual` | Library source exists / a declared concept has no physical Component |
| Eight `required ... Selected` | Seven README fragments plus one standalone changelog Component |
| Twenty `recommended/optional ... Unselected` | Not an error, and not part of the two-file seed |
| `VCL-HERO ... Conceptual` | Known visual dependency gap; the profile only generates a text Hero, **not** full Template conformance |
| `Destination` | New folder that would be created by generate |
| `Intended artifacts` | Preview paths and predicted SHA-256; they do **not** exist yet |
| `Written and verified artifacts` | Generated files and their verified SHA-256 after success |
| Exit `0` / `1` / `2` | Success / destination or write error / input, argument or source contract error |

You do **not** need to understand every internal Component or metadata path to perform this first workflow. They appear in the full report for transparency. If `plan` fails, do **not** proceed to generate until the problem is corrected. For an existing destination, choose a different new child name; never delete unrelated content to force success.


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

## Optional short report (UX-A)

For a less technical explanation, append `--summary` to **either** the `plan` or `generate` invocation. Existing commands without this flag continue to display the **same detailed output by default**. The short report is a presentation choice, not a different generation mode or a replacement for provenance.

Example from the Framework root using a fresh external parent and the fictional sample:

```powershell
$parent = (New-Item -ItemType Directory -Path (Join-Path ([System.IO.Path]::GetTempPath()) ("framework-generation-" + [guid]::NewGuid().ToString("N")))).FullName
python -B -m scripts.repository_generation plan TPL-BACKEND --template-version 0.1.0 --input framework/generation/examples/backend-project.json --output-parent "$parent" --name atlas-sample --summary
# Examine the preview first. No files have been created.
python -B -m scripts.repository_generation generate TPL-BACKEND --template-version 0.1.0 --input framework/generation/examples/backend-project.json --output-parent "$parent" --name atlas-sample --summary
# Inspect README.md and CHANGELOG.md inside the new child.
```

The short report explains the supported text-only scope, eight selected required Components versus twenty unselected references, the specific conceptual VCL-HERO limitation, the intended or written destination, and the two SHA-256 hashes. It ends with a safe next step. **Plan is read-only; generate writes only to a fresh child**, exactly as before. If you need exact Component versions, metadata paths, detailed reference classifications or dependencies, omit `--summary` to display the original full report. Do not treat the concise report as full Template conformance or proof that fictional project facts are real.

## Guided terminal workflow (UX-B)

The opt-in guided command asks for your project facts directly, avoiding manual JSON authoring. It uses the **same** Backend text-only profile, strict validation, canonical Components and safe writer as `plan`/`generate`. Use it only in a **real interactive terminal** from the Framework root; it deliberately rejects piped input, CI execution and noninteractive sessions.

```powershell
python -B -m scripts.repository_generation guide
```

The assistant explains the ten required fields and three optional fields. For ordered lists, add one entry per line and type `done` when finished. For multiline Markdown, enter each line and finish with `:end`. To include a literal line consisting of `:end`, enter `::end`. Enter `:cancel` at a field prompt to cancel the current session. Optional changelog categories are explicitly selected; there is no invented version or project content.

A full JSON review appears before planning. Choose `edit` followed by the field name to correct an entry, `continue` when strict validation succeeds, or `cancel` to stop without generating files. A read-only generation plan then shows the destination, the eight selected and twenty unselected Components, the known Conceptual VCL-HERO exception, and the intended two document hashes.

Choose an existing directory **outside** the Framework checkout and a fresh lowercase child name; the tool does not create the parent. After inspecting the plan, the tool displays the exact target and asks you to type **`yes`** to generate. Any other response cancels, with no destination created. The tool revalidates before writing, rejects an existing output directory and never overwrites it. On success, inspect `README.md` and `CHANGELOG.md`; all generated project facts still require your review.

Exit codes for `guide`: **0** verified success, **1** destination or write failure, **2** invalid input, source error or noninteractive/EOF refusal, **3** cancellation or terminal interruption. Existing `plan`/`generate` remain noninteractive and retain their original 0/1/2 semantics. A failure after a directory is created can leave an incomplete child for manual inspection: **never delete files automatically** or assume filesystem-wide atomicity. Project JSON is *not* saved automatically.

The guided workflow does not generate an application, initialize Git, publish anything, support other Templates or certify full Template conformance. Use `plan`/`generate` with JSON for scripts and reproducible automation; use `--summary` when you prefer a short report.


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
