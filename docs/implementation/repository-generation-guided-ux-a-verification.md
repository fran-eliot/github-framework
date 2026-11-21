# Repository Generation Guided Experience — UX-A Verification

Date: 2026-11-21  
Status: **UX-A implementation integrated; technical verification passed — formal unit acceptance pending**  
Main baseline: `ccb9a51ffc7095443fa28d74cd1d95640a32c9c3`  
CI: [Main run 44928097688](https://github.com/fran-eliot/github-framework/actions/runs/44928097688) — **success**.  
Implementation: [PR #424](https://github.com/fran-eliot/github-framework/pull/424) (merged).  
Continuity: [Kit 1.9.0, PR #423](https://github.com/fran-eliot/github-framework/pull/423) (merged).

## Authorization and boundary

On 2026-11-21, the maintainer explicitly approved [UXG-01–UXG-12 Delivery Scope](repository-generation-core-guided-experience-delivery-scope.md) and the [Guided Experience Implementation Plan](repository-generation-core-guided-experience-implementation-plan.md), authorizing **UX-A only**. Approval did not commit a new release, Sprint or milestone, nor authorize starting UX-B, UX-C or UX-D.

UX-A is an opt-in report and help improvement for the existing bounded `TPL-BACKEND 0.1.0` two-document generator. It does not introduce a guided wizard, edit canonical Component templates, normalize generated Markdown, write to existing destinations or expand template coverage.

## What was implemented

- `scripts/repository_generation/cli.py`: explicit `--summary` switch on `plan` and `generate`; human-first report derived from the **same** typed composition, document objects and validated target. Existing default report remains the detailed provenance report.
- Summary includes supported text-only scope; README and CHANGELOG only; eight selected required and twenty unselected recommended/optional references; named `README-HERO`/`VCL-HERO 1.0.0` Conceptual limitation; intended versus written paths and SHA-256 values; and safe next steps.
- `tests/repository_generation/test_cli.py`: three additional subprocess tests cover help, concise plan without destination writes, unchanged detailed report, generated file digests, collision handling, and validation failure with no false success output.
- `framework/generation/README.md`: copyable opt-in sample, distinction between short and full reports, and plan/generate/inspect sequence.

## Evidence and criteria mapping

| Gate | Evidence | Disposition |
| --- | --- | --- |
| UXG-01 | Legacy detailed default still checked by `test_plan_reports_inventory_and_does_not_write`; new `test_summary_help_and_read_only_plan` confirms full report provenance and short report selection | Technical PASS for UX-A |
| UXG-05 (plan only) | `test_summary_help_and_read_only_plan` asserts only fixture input remains after plan; no destination written | Technical PASS for UX-A plan |
| UXG-07 | Short report checks both artifact names, 8/20 counts, VCL-HERO named limitation, target, intended versus written, SHA-256 and next step | Technical PASS for UX-A |
| UXG-08 (collision/validation subset) | `test_summary_generate_hashes_and_collision` checks exit 1 with no success stdout; `test_summary_validation_failure_is_not_a_success_report` checks exit 2 | Technical PASS for tested errors |
| UXG-09 (regression subset) | Workflow `44928097688` successful on Windows and Ubuntu; existing generator suites, Component catalog parity and generated-document parity completed | Technical PASS for UX-A integration |
| UXG-02–04, 05 (guided confirmation), 06 (guided reuse), 08 (other guided failures), 09 (guided simulation), 11–12 | Beyond UX-A; require UX-B/UX-D and later evidence | **Pending; not claimed** |
| UXG-10 | No renderer or generated-document content changes in UX-A; retain current parity, address blank-line polish only in separately authorized UX-C | **Pending UX-C** |
| GEN-15 | Maintainer's previous first-use report found the tool difficult; summary has not yet been validated by a fresh human walkthrough | **Pending** |

The workflow's successful platform/parity conclusions establish the checks actually executed, not independent usability evidence. The generator's historical exact hashes remain reference evidence for unchanged input/source; no deliberate artifact-byte change was part of UX-A.

## Remaining work / next gates

1. Maintainer reviews and merges this verification record; check exact `main` CI afterward.
2. Request **explicit** authorization to begin UX-B under the approved scope/plan. The suggested `guide` terminal interaction, `yes` confirmation, `:end` multiline terminator and proposed exit 3 remain unimplemented.
3. Keep UX-C generated-document whitespace and UX-D maintainer replay/evidence matrix separate. Do not mark GEN-15 or complete delivery accepted until new actual human first-use evidence supports it.
4. Do not create a new release, tag, Sprint, milestone or change Only Film / UX-02 as a consequence of UX-A.
