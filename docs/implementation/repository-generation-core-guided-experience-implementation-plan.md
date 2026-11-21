# Repository Generation Core — Guided Experience Implementation Plan

Date: 2026-11-21  
Status: **Proposed — maintainer approval required before implementation**  
Baseline: `cc3b2810f9a85b8d99cae75e79d0ecad98e0a524`  
Scope: [Guided Experience Delivery Scope](repository-generation-core-guided-experience-delivery-scope.md)  
Decision: [Guided Experience Decision](repository-generation-core-guided-experience-decision.md)  
First-use evidence: [Maintainer Walkthrough](repository-generation-core-first-use.md)  
Release status: v0.12.0 published; Repository Generation Core unreleased.

## 1. Purpose and decision boundary

The current `plan` and `generate` commands already pass the approved bounded generation tests, including strict input checks, safe fresh-destination creation and Ubuntu/Windows output-byte parity. Nevertheless, the maintainer explicitly found the first-use journey difficult and asked for clearer guidance, help and interpretation. This plan specifies a smaller, **opt-in guided terminal journey**, not a new general-purpose generation system.

The Delivery Scope and its UXG-01–UXG-12 gates are integrated as a **proposal**, not automatically approved for production implementation. This document proposes concrete interface and safety decisions for maintainer review; no coding, release, Sprint or milestone is authorized by merging it.

## 2. Proposed UX-A — human-first reporting and help

Keep `python -B -m scripts.repository_generation plan ...` and `generate ...` as existing supported operations. For the current programmatic CLI, preserve the present detailed report by default to avoid silently breaking existing readers and tests. Introduce an **explicit opt-in `--summary` flag** for each command that prints a short human-oriented text report; `--help` documents its meaning. The guided experience always uses the same summary presentation rather than parsing CLI stdout.

The summary must state:

1. Supported profile: `TPL-BACKEND 0.1.0`, text-only documentation seed, **not complete Template conformance**.
2. Two files: `README.md` and `CHANGELOG.md`; exact new target directory.
3. Eight selected required references and twenty unselected recommended/optional references. Do not represent `Conceptual` as a missing selected artifact.
4. The named `README-HERO` → `VCL-HERO 1.0.0` Conceptual exception, not a general authorization to ignore required dependencies.
5. SHA-256 for each intended or written document; distinguish `plan` from verified `generate`.
6. Actionable next step (`generate` after plan, or inspect files after success); avoid claiming that the plan created any files.

Use typed `GenerationComposition` and immutable `Document` objects for presentation; do not parse the text returned by an existing CLI run. If the report cannot be constructed correctly, fail without a misleading success message. Full detailed provenance remains available with the current invocation and unchanged default.

Tests: summary labels, selected/unselected count, named limitation, two hashes, no writes in plan, existing default report unchanged, no new external dependencies.

## 3. Proposed UX-B — interactive user journey

Add an explicit `guide` subcommand (not the default invocation). No positional template is required for this first supported guided profile: the interface clearly states it supports only `TPL-BACKEND 0.1.0`. It must not silently offer nonimplemented Templates. The guide runs only with an actual interactive terminal; if stdin or stdout is non-interactive, fail promptly with a useful diagnostic rather than accepting piped input, blocking or writing. Test non-interactive and EOF paths with isolated mocked streams. Normal `plan`/`generate` stay noninteractive.

### 3.1 Field entry

Prompt the user with field name, description, shape and applicable length constraints. Required inputs: `project_name`, `tagline`, `overview`, `features`, `technologies`, `prerequisites`, `installation`, `execution`, `documents`, `footer`. Optional: `short_description` (empty), `alignment` (`center` or `left`), and `unreleased_changes` (optional categories in the canonical order).

Single-line strings use one explicit prompt. Nonempty lists collect ordered items one at a time and require a distinct `done` sentinel after at least one item; do not trim legitimate interior spaces in items. Multiline Markdown fields collect lines until a line containing the exact dedicated terminator `:end`; a literal `:end` line cannot be entered through this proposed terminal mechanism without escaping. Define escaping (`::end` becomes a literal `:end` data line) and verify it in tests. Reject unintended extra H1s through existing validation rather than automatic rewriting. Display plain-language examples **as guidance only**, never insert them as project facts. Optional defaults are displayed and confirmed; no hidden technology, documentation or run command is generated.

Do not invent a secondary schema. Build the exact JSON-compatible structure and call the existing `parse_project_input` or equivalent strict validation once the draft is complete, with field-focused re-prompting where possible. Correcting any field requires revalidating the whole completed draft, with no silent coercion.

### 3.2 Review and destination

Print a review of every entered field, distinguishing missing optional content and explicitly accepted defaults; escape or delimit multiline content so users can identify its boundaries. Allow a user to choose `edit` by field name, `continue` or `cancel` without writing anything. Enter an existing external destination parent and new portable child name. Reuse `validate_destination`; errors explain which field is invalid, that existing directories are not overwritten, and how to select a fresh name.

Execute `require_profile`, strict input validation, `load_composition` and `assemble` before presenting a plan. Never substitute mock or simplified rendering for the actual canonical sources. Show the human-first summary as a **read-only plan**, including the named visual limitation and what remains outside scope.

### 3.3 Confirmation, cancellation and failure

The only action that can create the destination is a **separate explicit confirmation**, with the full target path shown immediately above the prompt. Require an unambiguous affirmative token (propose exact `yes`), and treat `no`, empty, `cancel` or unsupported answer as refusal with no writes. After acceptance, repeat composition and in-memory rendering and invoke the existing `write_documents`; do not trust a stale preview. On success, print the two verified file paths, digest and an instruction to inspect actual content.

Proposed exit semantics for `guide`: `0` on verified generation; `1` for destination/write failures; `2` for malformed project inputs or source/contract errors; **`3` for intentional cancellation or terminal interruption**. An EOF/non-interactive refusal should return `2` with a diagnostic, without creating any output. Keep the existing `plan`/`generate` 0/1/2 behavior unchanged. The exact cancellation interface and status must be explicitly approved before implementation.

No input draft is saved automatically. The guided implementation does not add `--save`, telemetry, network, Git initialization or remote publication. This avoids a second uncontrolled write destination; a future optional export requires a separate contract and approval.

### 3.4 Interaction architecture

Prefer a small independent `guided.py` module with replaceable input/output adapters for deterministic tests. The core business operations remain in `inputs.py`, `composition.py`, `assembly.py` and `destination.py`, rather than importing subprocess results or duplicating the renderer. Wire the `guide` entry point through `cli.py`. Keep I/O prompts and terminal detection outside source/metadata parsing. No new dependency is proposed; Python 3.11 and existing PyYAML 6.0.2 remain the verified baseline.

## 4. Proposed UX-C — bounded output polish

The maintainer observed excess blank lines around the Hero, Features and Documentation list items. Inspect the exact canonical source and current rendered fragments to identify **renderer-added** separators. Correct only known whitespace surrounding supported `if`/`each` blocks, not arbitrary whitespace in an author's Markdown.

A unit-level test must preserve multiline author text, intentional blank lines and literal template-like input. Keep seven README Components and the standalone Changelog assembled from the current canonical sources; do not edit those Component templates or silently reformat unknown syntax. Check the one-H1 structure, expected section order, UTF-8/LF and repeatability in two fresh destinations. Updated SHA-256 is expected; do not force agreement with previously recorded hashes after an intentional, approved output change.

CI must continue the existing Validator (282), Composition Preview (24) and Repository Generation (66 as of the baseline) suites, plus smoke tests, Component catalog parity and **byte-level cross-platform generated-document parity**. Report the actual new counts and hashes, not assumed ones.

## 5. Proposed UX-D — acceptance and maintainer replay

After technical tests pass on actual Ubuntu and Windows runners, repeat a first-use walkthrough with a new maintainer-authored project and fresh local destination. The maintainer should begin from the public guide, not assistant-supplied commands. Capture the exact baseline, OS/runtime, successful and failed/cancelled actions, understanding of the text-only limitation and of the selected/unselected references, readability of the generated Markdown, recovery guidance, friction and the maintainer's satisfaction. Measure elapsed time only if actually observed. Do not claim independent user research.

A separate final matrix maps UXG-01–UXG-12 and existing GEN-01–GEN-16 to code tests, actual CI logs, maintainer evidence and limitations. **GEN-15 remains pending** until the improved first-use experience has been performed and accepted; formal delivery acceptance also remains separate from publication.

## 6. Staged work and gates

| Unit | Reviewable implementation increments | Verification before next unit |
| --- | --- | --- |
| UX-A — reporting | Summary formatter, CLI opt-in flag, plain-language help, tests | Preserve exact default detailed report and exit codes; run both CI platforms |
| UX-B — guided journey | Terminal adapter, field collection/validation, review-edit, preflight, confirmation and safe output | Tests for all field types, EOF/non-TTY, edit, cancel, collisions, no writes before confirmation and positive real checkout |
| UX-C — document polish | Narrow rendered-fragment whitespace fixes and regression fixtures | Author Markdown preservation and actual generated-byte parity on Ubuntu/Windows; update hash evidence |
| UX-D — usability acceptance | Guide revisions, maintainer replay, evidence matrix and outstanding risk record | Maintainer explicitly assesses UX; no release without separate approval |

Keep PRs thematic; after each merge, verify CI on `main` and ensure no unintended release or consumer changes. Work may require additional reviewable PRs per unit.

## 7. Unresolved approval points

The following design choices are **recommendations requiring confirmation**:

- `--summary` opt-in with current verbose report as default, rather than changing all existing reports.
- `guide` as a separately invoked terminal-only command, without a template positional argument.
- Multiline `:end` termination with `::end` escaping; ordered list `done` terminator.
- Explicit `yes` confirmation, no implicit consent and no persistent input file.
- `guide` cancellation code 3, while existing CLI exits remain unchanged.
- Restricting whitespace normalization to the known renderer-generated block separators.

If approved, the maintainer authorizes the Delivery Scope UXG-01–UXG-12 and the implementation approach only to the extent explicitly stated in the subsequent approval. No implementation begins solely because this plan is merged. No new Template support, GUI, existing-repository mutations, release, tag, Sprint, milestone, Only Film change or UX-02 execution is implied.
