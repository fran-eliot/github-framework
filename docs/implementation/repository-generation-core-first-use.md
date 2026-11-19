# Repository Generation Core — First-Use Walkthrough

Date: 2026-11-19  
Status: **Prepared — Maintainer execution pending**  
Baseline: `77c90915d52e0db647c7d4f36800b1390be9f6f8`  
Guide: [Repository Generation Guide](../../framework/generation/README.md)  
Criterion: GEN-15; related evidence for GEN-01, GEN-02, GEN-04, GEN-07–GEN-11.

## Purpose and evidence boundary

Assess whether the public guide enables a maintainer to generate and inspect a local documentation seed without relying on implementation internals. This is a controlled maintainer walkthrough, not independent usability research.

The public example already passed automated CLI tests and generated-document parity in [PR #416 CI](https://github.com/fran-eliot/github-framework/actions/runs/44577797065). Integrated [main CI](https://github.com/fran-eliot/github-framework/actions/runs/44587195735) succeeded. These results are technical evidence only and do not establish human execution, elapsed time, comprehension or satisfaction.

## Procedure

Use a local Framework checkout containing the guide and implementation. Record the actual commit, OS, shell, Python and dependency versions. Follow the guide as written, recording any deviation or assistance. Do not use a real consumer repository.

| ID | Task | Observable result |
| --- | --- | --- |
| FU-01 | Prepare environment and locate guide | Python 3.11, PyYAML 6.0.2; example located |
| FU-02 | Invoke help and understand scope | plan/generate distinguished; text-only boundary understood |
| FU-03 | Choose fresh external parent and run plan | Exit 0; no child created |
| FU-04 | Interpret report | Eight selected and twenty unselected; named VCL-HERO limitation understood |
| FU-05 | Generate documentation | Exit 0; exactly README.md and CHANGELOG.md |
| FU-06 | Inspect both files | Canonical section order, fictional project facts, Unreleased only |
| FU-07 | Independently compute hashes | Plan, generate and local file digests agree |
| FU-08 | Repeat generation with same name | Exit 1; original files unchanged |
| FU-09 | Record friction and recovery understanding | Observations, elapsed time and improvement candidates recorded |

## Recording form

- Execution date and actual checkout commit: pending
- Operator: maintainer
- OS, shell, Python and PyYAML: pending
- Environment setup time (separate from walkthrough): pending
- Walkthrough elapsed time (help through inspection and collision test): pending
- FU-01–FU-09 results: Not executed
- Assistance, deviations, confusing terms and error messages: pending
- README.md and CHANGELOG.md SHA-256: pending
- Recovery policy understood (manual inspection, no automatic deletion): pending
- Outcome and improvement candidates: pending

Record actual observations rather than expected outcomes. If a step fails, retain its diagnostic and classify the cause before retrying. Do not delete existing content to satisfy the test. Timing is descriptive, not a performance threshold.

## Known automated reference

The public Atlas fixture produced these hashes on Ubuntu and Windows in PR #416:

- README.md: `e5dd6bf860185d83a9c32b5b7c7b7ea1d5d7de8f75eb87c781644abbb063864d`
- CHANGELOG.md: `2506e7084a50ed0d72340b3319083d5bcf2583e0d0fb335067c45f191f560785`

Compare local results against the actual plan and generation report first. Historical hashes are reference evidence for unchanged inputs and sources, not a permanent acceptance gate.

## Closure boundary

GEN-15 remains pending until the maintainer walkthrough is executed and recorded. Any documentation or implementation correction requires review and appropriate re-verification. No independent UX evidence, full Template conformance, final delivery acceptance or release authorization is established by this protocol.
