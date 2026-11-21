# Repository Generation Core — Guided Experience Delivery Scope

Date: 2026-11-21  
Status: **Proposed — explicit approval required before implementation**  
Baseline: `292c4a2c7898e4648c6b12a34103722044a8daa8`  
Decision: [Guided Experience Decision](repository-generation-core-guided-experience-decision.md)  
Evidence: [First-Use Walkthrough](repository-generation-core-first-use.md); [Usability Improvement Gate](repository-generation-core-usability-improvement-gate.md)

## 1. User problem and outcome

The first maintainer-run walkthrough verified deterministic, safe documentation generation, but the maintainer explicitly described it as **not easy to use** and requested clearer information, help and interpretation. GEN-15 remains open. This is one maintainer's assessment, not independent user research.

A developer should understand what the tool does, provide their own project facts with guidance, review an intelligible read-only plan, explicitly approve output, and inspect the result without learning the internal Component registry.

## 2. Bounded deliverables

### A. Human-first CLI reporting

Provide a concise explanation of: supported TPL-BACKEND 0.1.0 text-only profile; exactly README.md and CHANGELOG.md; intended or actual destination; eight required selected and twenty unselected references; named VCL-HERO Conceptual limitation; SHA-256 and next safe step. Preserve detailed reference/version/path/dependency evidence as an accessible verbose view. Existing `plan`, `generate` and `--help` invocations must continue to work. Presentation is human-oriented, not a stable machine-readable API. Whether to use a new explicit flag or an added heading must be decided before implementation; do not silently remove existing report information.

### B. Opt-in local terminal-guided mode

Introduce a *separately invoked* interaction, using the **same** strict profile schema, canonical resolver, bounded rendering, assembly and exclusive writer. Help users enter the ten required fields (project_name, tagline, overview, features, technologies, prerequisites, installation, execution, documents, footer) and three optional fields (short_description, alignment, unreleased_changes) through understandable descriptions and examples. Inputs are supplied or optional defaults explicitly accepted, never inferred. Support multiline Markdown, ordered lists and clear end-of-entry. Show a complete review/edit step. Require an existing external parent and fresh portable child. Display an understandable plan before asking for explicit generation confirmation; cancellation leaves the destination unchanged. Fail promptly on EOF, noninteractive invocation or interrupt without a partially successful report. No unstated input persistence; JSON export, if desired, requires a separate explicit write policy.

### C. Generated-document readability

Correct excess *renderer-introduced* blank lines demonstrated in the Hero, Features and Documentation fragments. Limit cleanup to structurally known fragment formatting, not arbitrary global Markdown whitespace. Do not edit canonical Component templates or remove intentional whitespace supplied by an author. Document changed outputs and regenerate cross-platform parity evidence; do not pin historical SHA-256 as immutable fixtures.

## 3. Preserved safety and architectural boundaries

- Existing programmatic CLI remains supported without prompting; generation is *never* triggered by merely displaying help or a plan.
- No destination is created before explicit guided confirmation; generation rechecks the entire preflight and destination.
- No overwrite, merge, updating existing repositories, auto-cleanup, hidden network, telemetry, Git operations, inferred technology, or execution of user commands.
- Source acquisition and resolution, the known conceptual visual exception, and the eight required Components stay unchanged.
- Existing destination link/path/collision protection and partial-write inspection policy remain in force; do not promise atomicity or hostile-race resistance.
- Python 3.11 / PyYAML 6.0.2 remain the verified target. The successful maintainer replay on 3.12.2 / 6.0.3 is a compatibility observation only.
- No web UI, extra Template, visual generation, application scaffold, automatic adoption, Only Film or UX-02 modifications. v0.12.0 remains the published version.

## 4. Candidate acceptance criteria

| ID | Observable gate |
| --- | --- |
| UXG-01 | Existing help, plan and generate contracts remain usable; detailed audit/report provenance remains accessible |
| UXG-02 | Prompts run only in opt-in mode; EOF, noninteractive invocation and cancellation cannot hang or create output |
| UXG-03 | All required/optional fields are explained and strictly validated without invented facts or hidden defaults |
| UXG-04 | Multiline author Markdown, literal template-like text and ordered lists survive; review/edit can correct mistakes |
| UXG-05 | Plan and review are read-only; explicit confirmation is mandatory before the destination is created |
| UXG-06 | Guided flow calls the established preflight/assembly/writer rather than implementing a second generator |
| UXG-07 | Summary correctly distinguishes intended from written outputs, selected from unselected, Resolved from Conceptual, and the named VCL-HERO gap |
| UXG-08 | Existing destination, unsafe path, malformed input, failed write and incomplete output produce helpful non-destructive guidance |
| UXG-09 | Automated positive/negative simulation on Ubuntu and Windows Python 3.11 checks existing CLI regressions, guided cancellation and actual output parity |
| UXG-10 | Bounded whitespace correction preserves user Markdown, canonical source text and UTF-8/LF determinism |
| UXG-11 | Fresh maintainer-run guided walkthrough records understanding, difficulties and time only when measured; no independent UX claim |
| UXG-12 | Final evidence reconciles the original GEN-01–GEN-16 with UXG outcomes; release authorization remains separate |

These are **candidate criteria** and not yet an approved extension to GEN-01–GEN-16.

## 5. Proposed implementation units, pending approval

| Unit | Output | Gate |
| --- | --- | --- |
| UX-A | Decide backwards-compatible reporting contract, implement human-first report/help | Accurate summary, complete detailed evidence, existing CLI regression |
| UX-B | Input guidance, review, cancellation/confirmation and shared generation | Explicit safe interaction, strict validation, tests for EOF and noninteractive contexts |
| UX-C | Bounded Markdown output polish, integration regressions, cross-platform actual-document parity | No changed author whitespace or canonical assets; verified hashes |
| UX-D | Maintainer first-use re-evaluation and acceptance matrix | Evidence-backed GEN-15 / GEN-16 disposition, without implying release |

The unit sequence is a proposal, not a Sprint, milestone or coding authorization. Keep thematic PRs and verify main CI after each merged unit.

## 6. Requested decision

Approve or amend **B (opt-in guided CLI) supported by A (human-first reporting)** and the bounded scope and acceptance criteria above. Only then prepare an explicit Implementation Plan covering interaction prompts, cancellation exit semantics, default policies, tests and backward compatibility. **Merging this proposal does not authorize implementation, release, tag, Sprint or milestone.** GEN-15 and delivery acceptance remain pending.
