# Repository Generation Core — First-Use Walkthrough

Date: 2026-11-19  
Status: **Maintainer walkthrough completed with usability concerns — GEN-15 acceptance pending**  
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

## Observed maintainer walkthrough (2026-11-21)

Evidence: maintainer-supplied PowerShell transcript (plan and generate, directory listings, file hashes) and subsequent pasted document contents and collision output. These are externally supplied human-run observations, not GitHub Actions jobs.

- Actual checkout commit: `d8c621f7053e545dacfc9d8fc1fc11a062970174`; `main`, working tree clean after fast-forward pull.
- Operator: maintainer; Windows PowerShell 5.1; Python 3.12.2 and PyYAML 6.0.3 in an active virtual environment. This is a compatibility observation outside the documented Python 3.11 / PyYAML 6.0.2 baseline, not an official support-matrix extension.
- FU-01: environment prepared and example located; documented version pair **not** used. Conditional success for the local test only.
- FU-02: help returned the two documented commands. PASS for observed help output; comprehension of boundaries not separately attested.
- FU-03: plan exit 0, target did not exist after planning. PASS.
- FU-04: full 28-reference inventory and conceptual VCL-HERO limitation were displayed; **understanding not independently confirmed**. Partial evidence.
- FU-05: generate exit 0; exactly README.md (1,347 bytes) and CHANGELOG.md (97 bytes) observed. PASS.
- FU-06: maintainer pasted both files; canonical sections, fictional facts, and initial Unreleased change present. PASS with readability issue noted below.
- FU-07: local file hashes match plan/generate reports and the recorded Windows/Ubuntu CI reference: README `e5dd6bf860185d83a9c32b5b7c7b7ea1d5d7de8f75eb87c781644abbb063864d`, CHANGELOG `2506e7084a50ed0d72340b3319083d5bcf2583e0d0fb335067c45f191f560785`. PASS.
- FU-08: second generate attempt into the same child exited 1 with `output destination already exists`; README hash unchanged. PASS for inspected file; no separate post-collision CHANGELOG hash recorded.
- FU-09: **maintainer explicitly reports that the generator is not easy to use and asks for clearer information, help and interpretation for users**. Qualitative friction established; elapsed time and manual recovery understanding remain unrecorded. This is one maintainer observation, not independent user research. Do not claim full GEN-15 acceptance.
- Environment setup duration and walkthrough elapsed duration: not recorded; do not infer from transcript timestamps.

### Friction and presentation findings

1. The maintainer ran inspection commands after the read-only plan but before generate. PowerShell returned missing-path diagnostics. This is a procedure-order difficulty; the subsequent generation succeeded. Improve guide sequence visibility (`plan → generate → inspect`), rather than reporting a generator failure.
2. Generated README contains multiple consecutive blank lines around the Hero, Features and Documentation list items. This is a visible readability/polish issue in otherwise valid output. Assess a **bounded renderer-level whitespace correction** in a separate reviewed change. Do not silently edit canonical templates or globally normalize user-authored Markdown; preserve existing semantics and add cross-platform deterministic regression tests. Reverify changed hashes if corrected.
3. Plan report prints substantial component and dependency detail without a user-oriented interpretation layer. The maintainer reports the overall experience is difficult and requests better information, help and interpretation; exact report-specific causes remain hypotheses until retested.

### Unrecorded first-use feedback

Overall difficulty and request for simpler information/help/interpretation are confirmed by maintainer feedback. Step-specific clarity, recovery understanding, total duration, and any further points of friction remain unconfirmed. Record these if supplied, including `not measured` for duration. Do not substitute automated CI performance timings for human time.

Record actual observations rather than expected outcomes. If a step fails, retain its diagnostic and classify the cause before retrying. Do not delete existing content to satisfy the test. Timing is descriptive, not a performance threshold.

## Known automated reference

The public Atlas fixture produced these hashes on Ubuntu and Windows in PR #416:

- README.md: `e5dd6bf860185d83a9c32b5b7c7b7ea1d5d7de8f75eb87c781644abbb063864d`
- CHANGELOG.md: `2506e7084a50ed0d72340b3319083d5bcf2583e0d0fb335067c45f191f560785`

Compare local results against the actual plan and generation report first. Historical hashes are reference evidence for unchanged inputs and sources, not a permanent acceptance gate.

## Closure boundary

GEN-15 remains pending until the maintainer's remaining observations are assessed and identified usability corrections are dispositioned. Any documentation or implementation correction requires review and appropriate re-verification. No independent UX evidence, full Template conformance, final delivery acceptance or release authorization is established by this protocol.
