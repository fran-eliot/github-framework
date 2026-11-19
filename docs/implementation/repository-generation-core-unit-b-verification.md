# Repository Generation Core — Unit B Verification

Date: 2026-11-19  
Status: **Verified — Unit B complete within its staged scope**  
Integrated baseline: `d91ad9ad4a03c4ff8dc4cd97a4db3d9ab09e6a7b`  
Authority: [Formal approval](repository-generation-core-approval.md), [Implementation Plan](repository-generation-core-implementation-plan.md), [Delivery Scope](repository-generation-core-delivery-scope.md).  
Preceding evidence: [Unit A Verification](repository-generation-core-unit-a-verification.md).

## Integrated increments

| PR | Responsibility |
| --- | --- |
| #407 | Bounded syntax parser and static scope audit; eight test methods |
| #408 | Canonical rendering policies for seven README fragments and Changelog initialization; nine methods |
| #409 | Ordered in-memory document assembly, structural checks and SHA-256 digests; eight methods |

All three PRs are merged. The #409 branch has been removed. No canonical Component, existing resolver contract or production dependency was changed.

## Observed evidence

[PR CI run 44519629631](https://github.com/fran-eliot/github-framework/actions/runs/44519629631) succeeded for head `19d02cdbeea3b490bfcc0653d713e125155d0107`. The three suite invocations, counts and OK results were inspected in both job logs. [Main CI run 44520320025](https://github.com/fran-eliot/github-framework/actions/runs/44520320025) also succeeded at the integrated baseline.

| Suite | [Ubuntu job](https://github.com/fran-eliot/github-framework/actions/runs/44519629631/job/135544620845) | [Windows job](https://github.com/fran-eliot/github-framework/actions/runs/44519629631/job/135544621056) |
| --- | ---: | ---: |
| Framework Validator | 282 OK | 282 OK |
| Composition Preview | 24 OK | 24 OK |
| Repository Generation | 41 OK | 41 OK |
| Generation suite duration | 0.854 s | 0.761 s |

347 methods per platform, 694 executions, not 694 unique tests. Generation includes the 16 Unit A methods and 25 new Unit B methods, with subtests. Smoke, catalog integrity and [cross-platform catalog parity](https://github.com/fran-eliot/github-framework/actions/runs/44519629631/job/135545088733) succeeded. Counts and durations refer to the inspected PR logs, not independently inspected main logs.

## Staged acceptance assessment

| Criterion | Unit B evidence | Remaining delivery work |
| --- | --- | --- |
| GEN-03 | Unsupported source syntax, incompatible selected versions and unexpected canonical section starts rejected in tested cases | CLI diagnostics and integrated preflight in C |
| GEN-05 | HTML escaping for Hero, literal Markdown elsewhere, bounded extra-H1 checks | End-to-end input and diagnostic checks |
| GEN-06 | Bounded syntax parser, component-specific scope audit including inactive branches, nonrecursive substitution | CLI integration and final evidence |
| GEN-07 | Seven canonical README fragments in approved order, project H1, lists and expected sections in fixtures | Destination generation and first-use inspection |
| GEN-08 | Separate Unreleased-only changelog projection, supplied categories and entries in defined order, no fabricated release | End-to-end replay |
| GEN-10 | Repeated in-memory bytes, UTF-8/LF and SHA-256 digest assertions on both runners | Fresh destination writes and explicit cross-platform output digest comparison |
| GEN-14 | Existing Validator, Preview, smoke and catalog integrity/parity passed; no added production dependency | Continue regression through final delivery |

## Limits

The adapter is not a general Handlebars engine. Nesting is bounded to 32 levels. The Changelog recognizes a strict canonical initialization shape; incompatible changes require policy review. Structural heading checks are conservative, not full CommonMark parsing or HTML sanitization; ambiguous markup can be rejected, and coverage is limited to supported patterns. Closed top-level fenced examples are tested. The text-only Hero limitation remains accepted; this is not complete Template conformance. Input remains trusted author content. Deterministic in-memory bytes were tested separately on each runner; no cross-platform generation digest comparison has yet been recorded. Catalog parity is not generated-document parity.

No CLI, destination writes, existing-repository changes, independent user evidence or final acceptance is established by Unit B.

## Next gate

Unit B is implemented and verified within its staged responsibility. Proceed to Unit C — CLI & Safe Local Output only after maintainer authorization under the gated plan. Proposed sequence: destination validation and exclusive writer with failure tests; standalone plan/generate CLI and reporting; integrated verification. The approved manual-recovery policy remains unchanged. No release, tag, Sprint or milestone is committed. Only Film and UX-02 remain unchanged; v0.12.0 remains the published version.
