# Repository Generation Core — Unit C Verification

Date: 2026-11-19  
Status: **Verified — Unit C complete within its staged scope**  
Integrated baseline: `3fca128596b57b827fbde977b19bf6f35b2f24f8`  
Authority: [Formal approval](repository-generation-core-approval.md), [Implementation Plan](repository-generation-core-implementation-plan.md), [Delivery Scope](repository-generation-core-delivery-scope.md).  
Preceding evidence: [Unit A Verification](repository-generation-core-unit-a-verification.md), [Unit B Verification](repository-generation-core-unit-b-verification.md).

## Integrated increments

| PR | Responsibility |
| --- | --- |
| #411 | Destination validation, exclusive directory and file creation, byte verification, manual recovery and eleven test methods |
| #412 | Standalone plan/generate CLI, human-readable reporting, exit codes and six test methods |

Both PRs are merged; the #412 branch has been removed. No canonical Component, existing resolver contract or production dependency was changed.

## Observed evidence

[PR CI run 44531913322](https://github.com/fran-eliot/github-framework/actions/runs/44531913322) succeeded for head `9b6b79bb056c16b54c940b399bf6f9ef04b3b1d2`. The three suite invocations, counts and OK results were inspected in both job logs. [Main CI run 44532154780](https://github.com/fran-eliot/github-framework/actions/runs/44532154780) also succeeded at the integrated baseline.

| Suite | [Ubuntu job](https://github.com/fran-eliot/github-framework/actions/runs/44531913322/job/135587152170) | [Windows job](https://github.com/fran-eliot/github-framework/actions/runs/44531913322/job/135587151653) |
| --- | ---: | ---: |
| Framework Validator | 282 OK | 282 OK |
| Composition Preview | 24 OK | 24 OK |
| Repository Generation | 58 OK | 58 OK |
| Generation suite duration | 1.912 s | 3.607 s |

364 methods per platform, 728 executions, not 728 unique tests. Generation includes 41 previous methods and 17 new Unit C methods, with subtests. No skips were reported in the inspected summaries, including the symbolic-link test suite. Smoke, catalog integrity and [cross-platform catalog parity](https://github.com/fran-eliot/github-framework/actions/runs/44531913322/job/135587802826) succeeded. Counts and durations refer to inspected PR logs, not independently inspected main logs.

## Staged acceptance assessment

| Criterion | Unit C evidence | Remaining delivery work |
| --- | --- | --- |
| GEN-01 | Standalone help, plan and generate with explicit arguments; subprocess success and argument error tests | Document invocation and independently replay supported commands in D |
| GEN-02 | Full 28-reference selection report; eight selected and twenty unselected in canonical fixture | Inspect report in final replay |
| GEN-03 | Shared preflight and source/contract rejection mechanisms; CLI input/profile errors exercised | Final negative-case matrix; do not infer exhaustive CLI source-fault coverage |
| GEN-04 | Named visual limitation and direct dependency findings included in reports | Final report inspection |
| GEN-09 | Plan subprocess produces report and leaves fixture destination parent unchanged | First-use replay and evidence |
| GEN-10 | Plan and generate digests match actual file bytes in subprocess tests on each runner | Explicit cross-platform generated-document parity and two fresh destinations |
| GEN-11 | Existing file/directory, symbolic links, unsafe names and invalid parent scenarios rejected; sentinels preserved in tested cases | Integrated negative replay and source preservation evidence |
| GEN-12 | Injected write and byte-verification failures retain incomplete output; CLI exit 1 and diagnostic checked | Final evidence matrix; injected failures are not exhaustive OS failure coverage |
| GEN-14 | Existing suites, smoke and catalog integrity/parity pass without new production dependency | Continue regression through final delivery |

## Limits

The destination policy is bounded to a new local child outside the Framework checkout, two fixed output files and exclusive creation. It does not establish hostile-race resistance, filesystem atomicity or a recovery transaction. Linked/reparse-point ancestor rejection is implemented; symbolic-link tests are not exhaustive coverage of all reparse-point types. After a partial write, no automatic deletion occurs. Plan is read-only with respect to the destination and the documented invocation uses Python -B; generation repeats preflight rather than consuming an approved persisted plan. No Git or network operation is performed by the generator.

The CLI reports intended hashes for plan and verified artifact hashes for generate. Catalog parity is not generated-document parity; explicit cross-platform output hash comparison remains pending. The text-only VCL-HERO limitation and trusted-author Markdown boundary remain unchanged. No real consumer modification, independent user evidence, final GEN-01–GEN-16 acceptance or release authorization is established by Unit C.

## Next gate

Unit C is implemented and verified within its staged responsibility. Proceed to Unit D — Integration & Verification after maintainer authorization under the gated plan. Proposed increments: reproducible public usage guide and synthetic input fixture; real-checkout CLI replay with cross-platform generated-document parity and negative cases; maintainer-run first-use walkthrough with observed friction and timing; final criteria/evidence matrix and completion review. The walkthrough is not independent user research. Keep publication separate from delivery acceptance. No release, tag, Sprint or milestone is committed. Only Film and UX-02 remain unchanged; v0.12.0 remains the published version.
