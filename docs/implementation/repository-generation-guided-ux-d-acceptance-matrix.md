# Guided Experience UX-D — Provisional Acceptance Evidence Matrix

Date: 2026-11-21  
Status: **Technical evidence assembled; human acceptance and final delivery pending**  
Source baseline: `1d99eee80d42f05edc764ae567f565332e2210c7`  
[Integrated CI — 44935345596](https://github.com/fran-eliot/github-framework/actions/runs/44935345596): **success**, Ubuntu and Windows validation plus both cross-platform parity jobs.  
[Human retest protocol](repository-generation-guided-ux-d-first-use.md): prepared, **not yet executed**.

## Status conventions

- **Tech PASS**: integrated code and tests/CI support the criterion only within tested scenarios.
- **Human pending**: maintainer has not run the updated guided workflow and reported the outcome.
- **Final pending**: formal delivery acceptance has not been granted.
- **Partial**: source evidence exists but does not cover all failure or recovery claims.
- Do not upgrade statuses from this preparatory matrix merely because the PR merges.

## UXG-01–UXG-12

| Criterion | Evidence | Status |
| --- | --- | --- |
| UXG-01 | [UX-A verification](repository-generation-guided-ux-a-verification.md): unchanged legacy help/plan/generate, opt-in concise report, detailed default | Tech PASS |
| UXG-02 | [UX-B verification](repository-generation-guided-ux-b-verification.md): terminal-only guide, EOF/non-TTY, cancel tests | Tech PASS; human pending |
| UXG-03 | Strict existing input parser; guided required/optional field/review tests in UX-B | Tech PASS; human pending |
| UXG-04 | UX-B literal multiline/list/review-edit tests; [UX-C verification](repository-generation-guided-ux-c-verification.md) preserves author whitespace | Tech PASS; human pending |
| UXG-05 | Guided read-only review/plan and exact `yes` before writer, no-confirmation tests | Tech PASS; human pending |
| UXG-06 | Guided CLI calls existing parser, canonical resolver, assembly and exclusive writer; no second generator | Tech PASS |
| UXG-07 | UX-A summary distinguishes intended/written, 8/20 refs and named Conceptual VCL-HERO limitation | Tech PASS; human interpretation pending |
| UXG-08 | Existing target, malformed data and unsafe path tests; partial-write handling inherited from existing writer | **Partial**: no separately documented new guided injected partial-write fault/recovery replay |
| UXG-09 | CI 44935345596 exact `main` baseline; Python 3.11 Ubuntu/Windows, parity; relevant guided positive/negative tests | Tech PASS |
| UXG-10 | UX-C exact canonical list fragments, bounded Hero separator policy, author content preservation and parity | Tech PASS; human readability pending |
| UXG-11 | [UX-D first-use](repository-generation-guided-ux-d-first-use.md) prepared; no actual updated guided maintainer session | **Human pending** |
| UXG-12 | This matrix lists technical sources and pending limitations; no final delivery acceptance decision | **Final pending** |

## GEN-01–GEN-16

| Criterion | Technical / historical evidence to reconcile | Status now |
| --- | --- | --- |
| GEN-01 | Original Generator CLI help, strict profile/version tests; guide is separately opt-in | Tech PASS |
| GEN-02 | Canonical resolver, eight required selected, twenty unselected in report and UX-A summary | Tech PASS |
| GEN-03 | Existing source/composition failure guards and strict selected-source checks | Tech PASS within tested input/source cases |
| GEN-04 | Explicit Conceptual VCL-HERO warning in both summary and detailed report; no visual materialization | Tech PASS |
| GEN-05 | Strict JSON inputs; UX-B reuses parser and records explicit user facts | Tech PASS |
| GEN-06 | Supported syntax audited and source drift rejected; literal author input not re-evaluated | Tech PASS |
| GEN-07 | Eight selected references: seven README sections/fragments plus changelog; assembled order and H1 tests; UX-C compact output | Tech PASS |
| GEN-08 | Standalone Changelog with Unreleased-only changes supplied by author | Tech PASS |
| GEN-09 | Read-only plan tests, selected/omitted references and two intended digests; guide reuses same plan | Tech PASS |
| GEN-10 | Actual generated document byte parity on Ubuntu and Windows; SHA-256 derived from current document bytes | Tech PASS (current hashes replace historical values) |
| GEN-11 | Collision, invalid/link/path guard and preservation tests in original generator and guided integration | Tech PASS for tested cases |
| GEN-12 | Original injected write-failure tests and incomplete-output policy; inherited by guide | Tech PASS for original writer, guided-specific replay partial |
| GEN-13 | Current cross-platform CI 44935345596 plus prior actual generation tests | Tech PASS |
| GEN-14 | Validator + Composition Preview suites and Component catalog parity preserved in integrated CI | Tech PASS |
| GEN-15 | [First manual walkthrough](repository-generation-core-first-use.md) reported usability difficulty; improved guide not yet tried by maintainer | **Human pending; not accepted** |
| GEN-16 | Existing original technical verification and this integrated UX evidence; formal end-to-end delivery decision outstanding | **Final pending** |

## Remaining risks and exact next decisions

1. **Human-first-use evidence is absent.** Run UXD-01–11 using a fresh project, then record real outputs, confusion, improvement requests and optional measured time. This remains the primary blocker for GEN-15.
2. **Guided-specific injected partial-write recovery** is not separately evidenced here. Inherited writer tests establish the shared safe writer's policy, not that a real human has understood the message. Decide whether additional dedicated guided test coverage is required before final UXG-08/GEN-12 closure.
3. **Limited supported profile** remains `TPL-BACKEND 0.1.0` text-only, precisely two files. `VCL-HERO` remains Conceptual; neither required-Component coverage nor parity equals full Template conformance.
4. **Verification and usability limits:** Python 3.11/PyYAML 6.0.2 are the verified targets. Prior PowerShell Python 3.12.2/PyYAML 6.0.3 success is a compatibility observation only; no independent external participants or measured usability timing.
5. **No authorization to publish v0.13.0.** Before any release, an explicit final GEN-15/16 and UXG acceptance decision and a separate Release Scope, exact clean `main` SHA, release notes, tag and publication approval are required.

This is a provisional verification aid, not an acceptance certificate. Do not modify consumer repositories or treat a documentation-only merge as authorization for new functionality.
