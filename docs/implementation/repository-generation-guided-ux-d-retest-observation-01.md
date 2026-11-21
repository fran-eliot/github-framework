# Guided UX-D — First Maintainer Retest Observation 01

Date: 2026-11-21  
Status: **Observed cancellation and field-entry friction; generation and GEN-15 acceptance pending**  
Source: maintainer-provided PowerShell terminal transcript from `python -B -m scripts.repository_generation guide`.  
Project: fictitious `Prueba` (no consumer repository touched).  
Run commit / OS runtime / dependency versions: **not supplied in this particular transcript**. A previous UX-D baseline `4872fab98cb85b158f579efc9287c88918182f90` had successful CI but must not be falsely recorded as the exact human-tested checkout commit.

## Observed facts

- The human entered `project_name=Prueba`, `tagline=Esto es una prueba`, multiline `overview`, lists, optional short description, alignment, and all `unreleased_changes` categories explicitly set to `no`.
- The `:end` sentinel terminated Markdown entry; `::end` was recorded as the literal `:end` line. A list item entered as `item 3 done` was retained literally; only `done` on its own line terminated a list.
- `documents`: entering `done` as the first value yielded `At least one item is required.`, after which the human entered one item. This is evidence of one correctly reported list error.
- `installation`, `execution`, `footer` were recorded as empty strings after an immediate `:end`, but no early error was shown. `overview` contained fewer than the required 80 characters, and the full review reported only `overview: invalid content or length`. These are real onboarding friction points.
- Selecting `continue` on the invalid review printed `Fix the input issue before continuing.`, repeated the full JSON and the same first error. The maintainer then selected `cancel`, and the program printed `Cancelled; no destination created by this operation.`
- The transcript shows **no generation command, no confirmed output child inspection, no output hashes and no elapsed time**. The no-write property is expected and reported by the program, but there is no separate filesystem check in this transcript. The human's final ease-of-use rating is not provided.

## Usability interpretation and corrective action

The current user journey defers simple constraints to the end and exposes only the first strict parser error. This adds avoidable re-entry and review friction, especially because the entire JSON is reprinted on every failed `continue`. The first error is accurate but insufficiently actionable; other required blank fields would cause additional later errors.

A bounded corrective UX-D change is proposed in this PR:
1. Check each field's basic content/length through the existing strict parser primitives as soon as it is entered; re-prompt that field with a direct explanation instead of silently moving on.
2. Keep the full strict parser as the authoritative final validation; do not invent project facts, default required fields, change original JSON `plan`/`generate`, or auto-generate any documents.
3. Clarify Markdown `:end` versus `::end`, standalone list `done`, required blank fields and the single-H1 restriction.
4. Avoid reprinting unchanged full JSON after an unsuccessful `continue` while retaining the full review after actual field edits.
5. Add tests for immediate correction and cancelling during a retry.

This is **not** evidence that the correction works for the maintainer. A second actual human walkthrough on the merged corrective commit is required.

## Acceptance impact

- UXG-02: observed explicit cancellation; filesystem effect not separately checked in the supplied transcript.
- UXG-03/04: field prompts and literal handling observed; early validation and clarity require improvement/retest.
- UXG-05: no affirmative `yes` or successful creation observed; not accepted by this session.
- UXG-11 / GEN-15: **pending**, due to observed friction and no successful guided completion.
- UXG-12 / GEN-16: **pending** formal reconciliation after corrective evidence.
- UX-C renderer readability **not** human-inspected in this session.

No tag, release, Sprint, milestone, Only Film or UX-02 changes are authorized. v0.13.0 remains only a candidate.
