# Repository Template Composition Preview — Implementation Plan

**Status:** Proposed implementation plan; delivery scope and implementation authorization pending maintainer approval  
**Date:** 2026-11-18  
**Baseline:** [`3ff8def154f0f5165442b47afe5bba852699416b`](https://github.com/fran-eliot/github-framework/commit/3ff8def154f0f5165442b47afe5bba852699416b) (PR #385 merged)  
**Published Framework:** v0.12.0

## 1. Contract and dependencies

This plan decomposes the [proposed Delivery Scope](repository-template-composition-preview-delivery-scope.md), AC-01–AC-17, without widening it. It assumes Alternative A and the proposed independent Python command; these are not yet formally approved. Merging a planning record does not constitute implementation authorization.

Python 3.11 and the existing PyYAML 6.0.2 dependency are sufficient candidates. The existing Component Validator and its CLI, JSON contracts, artifact handling and parity checker remain unchanged.

The production design should separate source acquisition, pure resolution and rendering. The adapter should use the existing registry as the classification source, not duplicate a list of its IDs. Internal interfaces may receive explicit source roots for isolated fixtures; the public command must not expose arbitrary paths or inspect consumer repositories.

## 2. Proposed package structure

```text
scripts/template_composition_preview/
    __init__.py
    sources.py
    registry.py
    resolution.py
    report.py
    __main__.py          # introduced only when the complete CLI is available
tests/template_composition_preview/
    test_sources.py
    test_registry.py
    test_resolution.py
    test_report.py
    test_cli.py
```

Names are proposed organizational choices, not new public APIs. A common source-error representation and small typed records may be shared internally. No external dependency, schema version, public library API or JSON format is introduced.

## 3. Delivery units

### Unit A — Strict source acquisition and registry adapter

Implement safe local source readers with fixture-driven regressions. Select the three canonical Template locations by stable ID and verify metadata identity; preserve the three ordered lists. Reject duplicate YAML keys before mapping construction, wrong required-field types, invalid IDs, duplicate references and malformed inputs. Inspect actual immediate directories in the supported physical families, checking required metadata and family consistency. Retain duplicate valid physical matches for subsequent diagnosis. Check expected roots and traversed path links before reading, and reject unsupported physical Visual discovery. Do not treat failed reads as absent implementations.

Read only the four delimited Component Catalog registry tables. Verify exact section and table structure, header, separators, nonempty rows, family prefixes and global ID uniqueness. Ignore matching rows outside the selected sections. Report a clear source error when the adapter contract fails; structural validation does not establish completeness.

**Candidate files:** `sources.py`, `registry.py`, isolated source and registry tests.

**Allocated acceptance:** AC-08, AC-09, AC-10, AC-11 (unit evidence); contributions to AC-03, AC-13 and AC-14.

**Exit gate:** focused fixtures execute on both supported platforms; input acquisition is read-only; all accepted records retain portable source evidence. No public preview command or claim of delivery.

### Unit B — Pure resolution model

Join the Template references, registry records and physical match groups by exact ID. Model Resolved, Conceptual, Unknown, Inconsistent and Ambiguous as distinct outcomes; keep requirement level and registry classification independent. Multiple physical matches take precedence and retain all evidence in deterministic path order. Include a reason and source evidence for each result; never infer Conceptual from absence.

**Candidate files:** `resolution.py`, resolution tests.

**Allocated acceptance:** AC-06; resolution portion of AC-03, AC-05, AC-07 and AC-12. Exercise all nine matrix combinations and empty levels, order and duplicate matches.

**Exit gate:** pure tests pass without repository traversal or writes; input errors are distinct from valid unresolved outcomes; no consumer conformance inference.

### Unit C — Report and command integration

Compose the readers and resolver into the proposed independent command. Render all entries and zero-inclusive counts in stable order. Use only relative portable source paths in successful stdout; include the limitations of the preview. Parse exactly one canonical ID and standard help; return 0/1/2 per Delivery Scope, with explicit stderr and no partial preview on source errors. Resolve sources relative to the module checkout. Do not expose root overrides or silently change the Validator interface.

**Candidate files:** `report.py`, `__main__.py`, report and command tests.

**Allocated acceptance:** AC-01, AC-02, AC-03, AC-05, AC-07, AC-12 and CLI portion of AC-13. Add executable regressions for clean, conflicting and source-error outcomes rather than relying only on mocks.

**Exit gate:** the command operates against real canonical sources and isolated fixtures, and the existing Validator still passes. It is not yet a completed delivery. Include minimal invocation and limitations alongside the first public command.

### Unit D — End-to-end verification and documentation

Verify all three actual Template commands and pinned reference counts, repeatability and input-tree no-write behavior (disable Python bytecode writes; compare source paths and bytes before/after). Run source-error and conflicting-resolution cases end to end. Test from a working directory different from the checkout using the module import path explicitly, without adding a public root option. Run the preview tests and real Template commands on the existing Ubuntu/Windows Python 3.11 CI matrix, preserving existing Validator tests, smoke, catalog artifacts and parity checks.

Document the command, examples, outcome meanings, exit codes, source errors, structural adapter dependence and unsupported completeness/conformance claims. Update both top-level README navigation as appropriate, CHANGELOG Unreleased and governance only to reflect verified facts. Record AC-by-AC evidence against the exact tested revision; obtain maintainer review before closing delivery.

**Allocated acceptance:** AC-04, AC-13, AC-14, AC-15, AC-16, AC-17 and integrated confirmation of AC-01–AC-12.

**Exit gate:** executable evidence for all 17 criteria, existing workflow green, no modified consumers, no unapproved release or Sprint commitment.

## 4. Dependency and acceptance traceability

```text
A — Sources and registry
           |
           v
B — Resolution model
           |
           v
C — Report and command
           |
           v
D — Verification and documentation
```

| Criterion | Primary evidence | Integrated confirmation |
| --- | --- | --- |
| AC-01 | C: canonical argument and help tests | D: three real commands |
| AC-02 | C: argument failure tests | D: subprocess exit/stdout/stderr |
| AC-03 | A/B/C: ordered lists and explicit empty groups | D: real and empty fixtures |
| AC-04 | D: pinned baseline counts | D: real commands on both OSs |
| AC-05 | B/C: required Conceptual result | D: Documentation replay |
| AC-06 | B: nine-case resolution matrix | D: reviewed regression evidence |
| AC-07 | B/C: conflicting outcomes and complete report | D: subprocess exit 1 |
| AC-08 | A: bounded registry reader negative cases | D: malformed source subprocess |
| AC-09 | A: strict YAML and references | D: malformed source subprocess |
| AC-10 | A: missing/unreadable/link/Visual cases | D: OS evidence and documented skips |
| AC-11 | A: runtime metadata identity discovery | D: real checkout and isolated fixtures |
| AC-12 | B/C: evidence and reconciled counts | D: real output inspection |
| AC-13 | A/B/C: stable resolution and output | D: repeated subprocesses |
| AC-14 | A: read-only source design | D: byte/path snapshots, no generated files |
| AC-15 | D: existing Validator regression and smoke | D: existing CI |
| AC-16 | D: Ubuntu/Windows preview execution | D: tested revision and CI evidence |
| AC-17 | C/D: invocation, limitations and guides | D: documentation review |

Implement each unit on a separate reviewable branch and PR. Where necessary, add a preview test step to the existing matrix when the first testable unit lands, then extend it with real commands once available. This does not authorize changing existing Validator logic or parity behavior. A failing check should be corrected within the relevant PR before starting the dependent unit. The last unit consolidates evidence; it must not retroactively mark unexecuted tests as passed.

## 5. Open details and safeguards

- Define the bounded registry table grammar carefully: unexpected content inside the table fails, but a well-formed deleted row is not necessarily detectable. Do not introduce an independent static registry to make the parser appear complete.
- Reject malformed required metadata rather than coercing types. Confirm actual YAML scalar/collection forms and safe loader behavior with real and synthetic fixtures.
- Verify family prefixes and canonical family/location rules against current metadata. Distinguish source errors from multiple valid matches; ambiguous records are reportable outcomes, not arbitrary first-match resolution.
- Document platform-dependent permissions and symbolic-link test limitations. Do not claim atomic source snapshots or hardened containment against concurrent filesystem mutation.
- No fixed production counts, test-generated source modifications, public custom input roots, or new command flags outside the proposed scope.

## 6. Readiness and approval

The plan identifies four candidate units and their dependency order, with every proposed criterion allocated. No production implementation or acceptance test has been executed by this planning document. The existing Validator CI success at PR #385 is a baseline, not preview verification.

**Next gate:** maintainer approval of Alternative A, the proposed Delivery Scope (AC-01–AC-17) and this Implementation Plan before Unit A. No release target, Sprint, GitHub milestone or consumer work is committed. Only Film and UX-02 remain unchanged.
