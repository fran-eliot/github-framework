# Repository Generation Core — Usability Improvement Gate

Date: 2026-11-21  
Status: **Proposed — improvement scope, not implementation authorization**  
Baseline: `e002574c9d5140acd8767e47ce39e9725e05c552`  
Trigger: [Maintainer First-Use Walkthrough](repository-generation-core-first-use.md) and explicit maintainer feedback that the generator is difficult to use and requires easier information, help and interpretation.

## Product decision

The technically verified `plan`/`generate` workflow is not yet an acceptable onboarding experience. Do not close GEN-15 or infer delivery-wide readiness from successful CI. Prioritize an intelligible first-use journey before expanding Templates or adding another generation feature. A single maintainer observation establishes a concrete problem for this maintainer, not usability statistics for the wider audience.

The working hypothesis is that developers should be able to answer **what will be generated, what must I supply, can I safely proceed, and what should I do next** without learning the 28-reference registry or every dependency classification. Keep detailed provenance accessible for maintainers and audit.

## User journey and proposed improvements

| Priority | User need / observed issue | Candidate improvement | Evidence needed |
| --- | --- | --- | --- |
| P0 | Understand the tool before running it | Short entry path: what it generates, does not generate, prerequisites and Plan → Generate → Inspect | Maintainer finds correct starting step unaided |
| P0 | Interpret an extensive technical report | **Human-first** summary with selected count, intended output, safety status, named limitations and next action; retain detailed inventory as a separate accessible view | User can accurately explain output, omitted parts and limitation |
| P0 | Know how to provide correct project facts | Annotated field reference and copyable, complete synthetic JSON with clear required/default labels; direct field-specific validation feedback | Maintainer creates own valid input without consulting source code |
| P1 | Avoid repeatedly typing lengthy commands | Evaluate an opt-in guided, local workflow or a supported shortcut, without changing default safety behavior | Compare manual vs guided steps in controlled replay |
| P1 | Improve generated documents | Correct renderer-induced excess blank lines in Hero/Features/Documentation with bounded tests; preserve author-supplied Markdown | Readability inspection, deterministic byte/hash parity after fix |
| P1 | Recover from failures | Interpret exit codes and distinguish already-existing destination, invalid project facts and incomplete writes | User identifies safe recovery; no destructive retry |

A **wizard** is only a candidate. It is not part of the approved GEN-01–GEN-16 CLI contract and must not be implemented by implication. No default prompts, hidden field values, overwrites, network, unapproved optional-Component selection or output to existing repositories. A changed report presentation or new flag should be specified and regression-tested explicitly, retaining a full evidence path.

## Delivery choice and boundary

**Immediate documentation-only correction** is allowed within the current user guide: add a short first-use orientation, clearly separated plan/generate/inspect steps, a minimal report reading key and pointers to the full schema. The existing long-form reference must remain.

**Before production UX changes:** present one small decision record comparing (A) human-first report plus documented workflow, (B) an opt-in guided flow and (C) a web/UI workflow, on user value, effort, maintainability and safety. Select the smallest option that materially reduces friction, rather than indefinitely adding features. Obtain maintainer approval for any interface/contract expansion. Do not change canonical assets to mask renderer behavior.

## Proposed validation

1. Preserve the baseline automated safety, composition and cross-platform byte parity checks.
2. Re-run on a fresh outside-checkout directory with a genuinely new, maintainer-authored project input.
3. Observe the maintainer performing Plan → Interpret → Generate → Inspect → Collision handling with minimal assistant intervention.
4. Ask whether the user understands selected versus omitted references, the Conceptual VCL-HERO gap, what was actually created and what is not certified.
5. Record friction (with concrete steps), feedback and elapsed time **if measured**; do not invent timing or independent participation.
6. Keep GEN-15 pending until the maintainer accepts the improved first-use experience; then map GEN-01–GEN-16 evidence under GEN-16 without equating that approval to a release.

## Explicit exclusions

No release, tag, Sprint, milestone or changes to Only Film. No automatic adoption, generator-wide schema migration, remote publishing, application code, automatic technology choices or generic template engine. Maintain v0.12.0 as latest published release.
