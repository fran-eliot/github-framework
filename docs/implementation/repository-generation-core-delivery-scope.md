# Repository Generation Core — Delivery Scope

Date: 2026-11-19  
Status: **Proposed — scope approval pending; implementation not authorized**  
Baseline: `eb1268e471a56c5a98ef8b882a9ac091a93ef76a`  
Sources: [Discovery Synthesis](experiments/repository-generation-feasibility/SYNTHESIS.md), [Strategic Prioritization](../governance/19_STRATEGIC_PRIORITIZATION.md), [TPL-BACKEND](../../framework/templates/repositories/backend/README.md).

## Formal decision record

On 2026-11-19 the maintainer formally accepted Repository Generation Feasibility as PASS — Bounded Feasibility, including EXP-01–EXP-08 within documented limits, and approved alternative A (Bounded Repository Generation Core) and definition of its Delivery Scope. Implementation, release, Sprint and milestone were explicitly not committed. This record supersedes the pending-approval status in the historical Synthesis, without changing its experimental evidence.

PR #400 is integrated, its remote branch removed; [main CI 44504387801](https://github.com/fran-eliot/github-framework/actions/runs/44504387801) succeeded on this baseline. v0.12.0 remains the published version.

## User outcome and first vertical slice

A developer starting a backend project supplies explicit project facts, previews a local documentation generation plan, then creates a new directory containing a cohesive README.md and CHANGELOG.md. No application code, Git initialization, remote publication or technology choice is performed. Project facts and commands are supplied by the user, not invented or executed by the tool.

Support exactly TPL-BACKEND 0.1.0 and its eight required references in defined relative order. Report all recommended and optional references as unselected, retaining their resolution status. This provides required-reference documentation coverage, not certification of a complete Template instance, backend runtime, maturity or all transitive dependencies.

| Required Component | Proposed materialization |
| --- | --- |
| README-HERO | Identity, tagline, optional short description and alignment; text-only profile |
| README-OVERVIEW | Explicit Markdown overview |
| README-FEATURES | Ordered list of supplied capabilities |
| README-TECH-STACK | Ordered list of supplied technology descriptions |
| README-QUICK-START | Explicit prerequisites, installation and execution text |
| README-DOCUMENTATION | Ordered list of supplied documentation links/descriptions |
| README-FOOTER | Explicit complementary Markdown |
| DOC-CHANGELOG | Separate initial Unreleased document, empty unless explicit changes are supplied |

## Contracts and known gaps

Canonical assets remain authoritative; use their content, not duplicated parallel README skeletons. Review the rendering policy for each required Component and document any editorial projection. The scope proposes a strict JSON project-input document with explicit fields, duplicate/unknown field rejection, documented defaults and deterministic UTF-8/LF output. Required values are nonempty with applicable canonical bounds. Input is trusted author-provided content, not a promise of sanitized arbitrary Markdown. Do not evaluate user text as template syntax or execute commands.

The inspected Features and Documentation fragments use each/this; Tech Stack declares a list but interpolates technologies as one value. Define a deterministic list formatting policy, not a language-specific stack. Quick Start, Documentation and Footer metadata do not explicitly mark all inputs required; requiring their values in this generation profile is a deliberate proposed profile rule, not a metadata edit. Changelog canonical guidance permits an empty Unreleased section; omit sample releases and empty categories.

README-HERO declares required VCL-HERO 1.0.0, which is Conceptual in the catalog; its recommended VCL-BANNER and VCL-BADGES are also conceptual. The first profile excludes banner and badge generation and reports the unresolved required dependency explicitly. Approval of this scope would permit the bounded text-only documentation seed despite that named limitation, not reclassify the dependency, bypass other unresolved required dependencies, or assert full conformance. Any broader dependency policy or canonical changes require separate explicit review.

Reuse Composition Preview source acquisition and resolution without changing its CLI or semantics. Selected references must be Resolved with compatible versions, readable canonical artifacts and supported materialization contracts. A selected conceptual or conflicting reference blocks generation. Report all other reference outcomes; conflicts outside selection block this first profile as a conservative rule. Source errors fail closed. No claim of atomic source snapshots.

## User interface and destination policy

Propose one standalone Python 3.11 module invoked from a Framework checkout, with explicit template, input and output arguments, and a read-only plan mode. Exact command spelling, schema examples, diagnostics and engine choice belong to the implementation plan. The plan reports source identities, selection/omissions, dependency limitation and intended files; it never writes the output directory. Generation repeats preflight rather than relying on a stale plan. Invalid requests provide actionable diagnostics and nonzero exit status.

Output is strictly a new local child directory under an existing caller-selected parent. No overwrite, merge, update, deletion of existing files or consumer mutation. Restrict output names to the two fixed files; reject existing destinations (including dangling links), unsafe names, linked/reparse-point parents within the checked path and collisions before writing. Document ownership and behavior under I/O failure; any cleanup is limited to artifacts owned by the invocation, never pre-existing content. Do not promise filesystem-wide atomicity or safety against concurrent hostile path replacement. No external network access from the generator.

## Proposed acceptance criteria

| ID | Observable acceptance |
| --- | --- |
| GEN-01 | Standalone help and documented invocation on Python 3.11; unsupported Template/version and invalid arguments rejected. |
| GEN-02 | Canonical resolver used; full reference inventory reported in declared order, eight required selected, remaining references explicitly unselected. |
| GEN-03 | Missing, conceptual, conflicting or unsupported selected sources and composition conflicts block output; selected paths/versions traceable. |
| GEN-04 | VCL-HERO limitation explicitly reported in plan and generation; text-only profile rejects visual asset requests; no complete-conformance claim. |
| GEN-05 | Strict project input shape, types, required content, bounds, defaults and duplicate/unknown fields verified; no implicit project facts. |
| GEN-06 | Supported template syntax and references checked even in inactive branches; unsupported expressions fail; user text not evaluated as template code. |
| GEN-07 | All seven selected README fragments assembled from canonical sources in defined relative order, one project H1, expected lists and sections. |
| GEN-08 | Separate CHANGELOG from canonical initialization policy: Unreleased, only supplied changes if present, no fabricated versions or empty categories. |
| GEN-09 | Plan succeeds read-only and communicates intended artifacts, selected IDs/versions and omissions; invalid plan has no output writes. |
| GEN-10 | Identical valid inputs and unchanged sources produce byte-identical files in fresh destinations, UTF-8 and LF. |
| GEN-11 | Existing directory/file/link, unsafe paths and output collisions rejected; existing data unchanged; source tree unchanged. |
| GEN-12 | I/O failures diagnosed, bounded ownership/cleanup policy verified with injected failures; no success reported on partial writes. |
| GEN-13 | Positive and negative integration tests on real canonical checkout; Ubuntu and Windows Python 3.11 results and output hashes inspected. |
| GEN-14 | Existing Validator and Composition Preview contracts/tests preserved; no new production dependency without explicit engine decision. |
| GEN-15 | Reproducible first-use walkthrough with complete inputs and plan/generate examples, limitations, output inspection and recovery guidance; maintainer-run timing/friction noted, not independent UX evidence. |
| GEN-16 | Delivery verification maps every criterion to observable evidence and documents remaining limitations; formal acceptance separate from release. |

## Exclusions and decisions

No Fullstack/Documentation Template generation, optional/recommended Component selection, visual asset generation, application scaffolding, remote repositories, Git operations in destinations, existing-repository updates, manifest-based lifecycle management, generic rendering language or automatic adoption. No changes to Only Film, UX-02, existing release or committed Roadmap. The experimental workflow and original probes are historical evidence; any retention/removal decision is separate.

Before implementation, compare a native or existing engine, bounded adapter and canonical normalization against all eight inspected artifacts. Select the smallest maintainable approach and document dependency/escaping/compatibility trade-offs, including the experiment's shared-parser limitation. No renderer or production dependency is approved by this proposal alone.

Request maintainer review of the eight-reference text-only profile, named dependency exception, GEN-01–GEN-16 and exclusions. After scope approval, prepare an Implementation Plan with explicit engine decision, input contract and staged verification. No implementation, release, tag, Sprint or milestone follows automatically.
