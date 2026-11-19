# Repository Generation Core — Unit A Verification

Date: 2026-11-19  
Status: **Verified — Unit A complete within its staged scope**  
Integrated baseline: `675b18b911be6606a5d0f8c444ff646ae3a55bc1`  
Authority: [Formal approval](repository-generation-core-approval.md), [Implementation Plan](repository-generation-core-implementation-plan.md), [Delivery Scope](repository-generation-core-delivery-scope.md).

## Integrated increments

| PR | Responsibility |
| --- | --- |
| #403 | Fixed text-only profile, strict JSON input, input tests and approval record |
| #404 | Canonical composition preflight, direct dependency findings and tests |
| #405 | Existing Ubuntu/Windows CI matrix now runs the generation suite |

All three PRs are merged. The CI integration branch has been removed. No production dependency, canonical Component or existing resolver contract was changed.

## Observed evidence

[PR CI run 44513523780](https://github.com/fran-eliot/github-framework/actions/runs/44513523780) succeeded for PR head `c6dd31bddf25dfc8fd86fc831bab6b39e3834b36`. Job logs were inspected for the three suite invocations, counts and OK results. The integrated [main CI run 44514688209](https://github.com/fran-eliot/github-framework/actions/runs/44514688209) also completed with success at the baseline above.

| Suite | [Ubuntu job](https://github.com/fran-eliot/github-framework/actions/runs/44513523780/job/135523521906) | [Windows job](https://github.com/fran-eliot/github-framework/actions/runs/44513523780/job/135523522116) |
| --- | ---: | ---: |
| Framework Validator | 282 OK | 282 OK |
| Composition Preview | 24 OK | 24 OK |
| Repository Generation | 16 OK | 16 OK |
| Generation suite duration | 0.726 s | 0.990 s |

The total is 322 test methods executed per platform, 644 executions, not 644 unique tests. The new suite contains eight input/profile and eight composition methods, including subtests. Smoke checks, catalog integrity steps and [cross-platform parity](https://github.com/fran-eliot/github-framework/actions/runs/44513523780/job/135524113365) also succeeded. Main run success was checked separately; the detailed counts above refer to the inspected PR logs.

## Staged acceptance assessment

| Criterion | Unit A evidence | Remaining delivery work |
| --- | --- | --- |
| GEN-02 | Canonical resolver, full composition retained, exact ordered eight-reference selection | User-facing selection and omissions report in C |
| GEN-03 | Conflicts, selected conceptual references, version/path drift, source errors and empty artifacts rejected | Syntax/materialization contract check in B; CLI failure evidence in C |
| GEN-04 | Named VCL-HERO exception only, visual inputs rejected, dependency findings retained | Explicit plan/generate reporting in C; no full conformance claim |
| GEN-05 | Strict JSON shape, duplicate keys, types, bounds, defaults, ordered lists, literal text and invalid UTF-8 checks | Structural H1 constraint and output-context handling in B |
| GEN-14 | Existing Validator and Preview tests, smoke and parity pass without new dependency | Continue regression through final delivery |

The canonical test asserts 16 Resolved and 12 Conceptual references with zero composition conflicts, eight selected artifacts, and four direct dependency findings (VCL-HERO required conceptual, VCL-BANNER and VCL-BADGES recommended conceptual, README-HERO recommended resolved by README-OVERVIEW). This is an internal profile preflight, not full transitive dependency certification. Negative source scenarios include mocked source failures and record mutations; these do not establish general filesystem safety. No renderer, CLI, output writes, real consumer changes, user walkthrough or final delivery verification exists in this unit.

## Next gate

Unit A is implemented and verified within its staged responsibility; GEN-01–GEN-16 are not collectively accepted yet. Proceed to Unit B — Rendering & Assembly only after maintainer authorization under the existing gated plan. The proposed first increment is a bounded syntax parser and static scope audit with positive and negative tests, followed by canonical rendering and assembly. No new release, Sprint or milestone; v0.12.0 remains published. Only Film and UX-02 remain unchanged.
