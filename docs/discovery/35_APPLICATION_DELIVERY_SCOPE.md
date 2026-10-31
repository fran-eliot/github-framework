# 35 — Application Delivery Scope

## 1. Propósito

Este documento define el Delivery Scope mínimo para:

```text
Existing Repository Adoption
    Application Core
```

a partir de:

```text
32_APPLICATION_DISCOVERY.md
33_APPLICATION_DISCOVERY_SYNTHESIS.md
34_APPLICATION_REPEATABILITY_EXPERIMENT.md
```

Resultado previo:

```text
Application Core Candidate
    READY FOR DELIVERY SCOPE DEFINITION
```

---

## 2. Delivery Scope Question

> ¿Cuál es el Delivery Scope mínimo del Existing Repository Adoption Application Core y cómo debe integrarse con el Assessment Core sin introducir automatización, structured representation o mutation capabilities no respaldadas por Discovery?

---

## 3. Starting Point

Assessment Core v0.7.0 soporta:

```text
ANALYZE
    ↓
ASSESS
    ↓
REVIEW
    ↓
DECIDE
    ↓
REPORT
```

Application comienza después de una Adoption Decision resuelta.

---

## 4. Core Boundary

```text
ASSESSMENT CORE

ANALYZE
    ↓
ASSESS
    ↓
REVIEW
    ↓
DECIDE
    ↓
REPORT

────────────────────────────

APPLICATION CORE

SELECT
    ↓
REFRESH EVIDENCE
    ↓
DEFINE APPLICATION INTENT
    ↓
PLAN
    ↓
REVIEW PLAN
    ↓
APPLY IN ISOLATION
    ↓
VERIFY
    ↓
REVIEW RESULT
```

`INTEGRATE` queda fuera del Core Delivery Scope inicial.

---

## 5. Application Core Objective

Convertir una Resolved Adoption Decision en:

```text
candidate repository change
```

o:

```text
NO CHANGE
REPLAN
DEFER
```

de forma:

```text
evidence-backed
bounded
reviewable
preserving
verifiable
```

---

## 6. In Scope

```text
Application Selection
Evidence Refresh
Application Intent
Application Planning
Bounded Change Set
Preservation Scope
Human Review before Apply
Apply in Isolation
Verification
NO CHANGE
REPLAN
DEFER
DISCARD
```

---

## 7. Supported Operation Types

Supported:

```text
CREATE
MODIFY
```

Not supported as stable operations:

```text
DELETE
MOVE
RENAME
```

Operation type is derived from Application Plan, not directly from Assessment State.

---

## 8. Valid Non-Mutation Outcomes

```text
NO CHANGE
REPLAN
DEFER
REJECTED
```

These are valid outcomes, not technical errors.

---

## 9. Out of Scope

```text
DELETE
MOVE
RENAME
automatic merge
automatic conflict resolution
post-integration rollback
repository-wide normalization
multi-repository mutation
continuous synchronization
CLI
GitHub Actions
custom mutation engine
automatic remediation
fully autonomous Application
```

---

## 10. Structured Representation — Out of Scope

No requirement for:

```text
JSON
YAML
Schema
Manifest
typed Application Plan
machine-readable Change Set
```

Representation remains human-readable Markdown.

---

## 11. Automation — Out of Scope

No:

```text
automatic Evidence Refresh
automatic Adoption Decision execution
automatic Pull Request creation
automatic semantic verification
automatic merge
```

Principle:

```text
Human Review before Mutation
```

---

## 12. Integration — Deferred

Delivery may produce:

```text
verified candidate state
```

but does not define how that candidate becomes stable state.

Deferred:

```text
merge policy
merge strategy
required approvals
branch protection interaction
release interaction
post-merge verification
post-merge rollback
```

---

## 13. Recovery Boundary

```text
DISCARD
    IN SCOPE

ROLLBACK after Integration
    OUT OF SCOPE
```

---

## 14. Conflict Handling Boundary

The Core may detect or record conflicts.

It does not automatically resolve semantic conflicts.

Expected outcome:

```text
conflict
    ↓
REPLAN
or
DEFER
```

---

## 15. Consumer Convention Preservation

Preservation may include:

```text
language
terminology
documentation conventions
repository-local organization
```

when observable and compatible with Application Intent.

---

## 16. Idempotency Boundary

Desired safety property:

> Reapplying an already-satisfied bounded intent should not introduce duplicate or unintended changes.

Universal idempotency is not claimed.

---

## 17. Relationship with Assessment Core

```text
Assessment
    produces
        Evidence
        State
        Applicability
        Decision

Application
    consumes
        resolved Decision
        relevant Evidence
```

Evidence Refresh may recommend REPLAN or reassessment but must not silently rewrite Assessment history.

---

## 18. Assessment remains independently useful

```text
Application
    OPTIONAL downstream capability
```

Assessment remains complete without APPLY.

---

## 19. Proposed Application Representation

```text
Structured Markdown
```

Properties:

```text
human-readable
human-editable
reviewable in Git
usable without tooling
```

---

## 20. Candidate Application Record

```text
Application Context
Selected Responsibility
Current Assessment Outcome
Evidence Refresh
Application Intent
Candidate Change Set
Preservation Scope
Risk / Conflict Notes
Verification Plan
Application Result
Verification Result
```

Optional/provisional:

```text
Application Readiness
Consumer Conventions
Refinement Notes
Discard Outcome
```

---

## 21. Application Result Vocabulary

```text
APPLIED
NO CHANGE
REPLAN
DEFER
REJECTED
```

---

## 22. Verification Result Vocabulary

```text
PASS
REFINE
FAIL
```

---

## 23. Candidate Application Flow

```text
Resolved Adoption Decision
    ↓
SELECT
    ↓
REFRESH EVIDENCE
    ↓
CONFIRM DECISION
    ↓
DEFINE APPLICATION INTENT
    ↓
PLAN
    ↓
REVIEW PLAN
    ↓
    ├── NO CHANGE
    ├── REPLAN
    ├── DEFER
    └── APPLY IN ISOLATION
            ↓
         VERIFY
            ↓
         ├── PASS
         ├── REFINE → VERIFY
         └── FAIL / DISCARD
```

Delivery boundary:

```text
verified candidate state
```

---

## 24. Reusable Artifact Candidates

```text
framework/adoption/application/README.md

framework/adoption/application/application-template.md
```

Minimal update:

```text
framework/adoption/README.md
```

---

## 25. Non-Goals

Not intended to:

```text
make GitHub Framework a migration tool
enforce canonical repository structure
rewrite existing repositories
automatically satisfy Templates
replace developer judgment
normalize all documentation
create unsupported release history
infer semantic intent autonomously
```

---

## 26. Delivery Principles

```text
Evidence before Mutation
Reconciliation over Replacement
Responsibility over File
Bounded Change over Broad Rewrite
Human Review before Stable Integration
No Change is a valid Application outcome
```

---

## 27. Delivery Scope Summary

### In Scope

```text
Application Guide
Application Template
Evidence Refresh
Application Intent
Bounded Change Set
Preservation Scope
Plan Review
Isolated Application guidance
Verification
NO CHANGE
REPLAN
DEFER
DISCARD
```

### Supported Operations

```text
CREATE
MODIFY
```

### Out of Scope

```text
DELETE
MOVE
RENAME
INTEGRATE
post-integration rollback
automatic conflict resolution
automation
CLI
GitHub Actions
schema
manifest
structured data
continuous reassessment
```

---

## 28. Delivery Boundary

```text
Assessment Outcome
    ↓
Application Plan
    ↓
reviewed candidate change
    ↓
verified candidate state
```

Not:

```text
Assessment Outcome
    ↓
automatically merged repository
```

---

# Acceptance Criteria

## 29. Scope Acceptance Criteria

### AC-01 — Application begins from a resolved Adoption Decision

Application consumes a Resolved Adoption Decision from Assessment Core.

### AC-02 — Application remains optional

Assessment can finish without Application.

### AC-03 — Application Core has an explicit end boundary

Delivery ends at verified candidate state and excludes INTEGRATE.

### AC-04 — Supported mutation operations are bounded

Only CREATE and MODIFY are documented as supported.

### AC-05 — Non-mutation outcomes are valid

NO CHANGE, REPLAN, DEFER and REJECTED are valid.

---

## 30. Evidence Acceptance Criteria

### AC-06 — Evidence Refresh is mandatory before mutating Application

Current consumer state must be reviewed before mutation.

### AC-07 — Current evidence takes precedence

Current repository reality overrides stale assumptions.

### AC-08 — Unsupported facts must not be invented

No unsupported versions, dates, historical events, config values or repository facts.

### AC-09 — Evidence may prevent mutation

Evidence Refresh may correctly conclude NO CHANGE.

---

## 31. Application Intent Acceptance Criteria

### AC-10 — Every Application has explicit intent

Application Intent exists before physical change planning.

### AC-11 — Intent describes desired outcome

Intent is semantic, not merely "edit file X".

### AC-12 — Intent remains separate from Change Set

Application Intent ≠ Change Set.

---

## 32. Change Set Acceptance Criteria

### AC-13 — Mutating Application requires a bounded Change Set

Every mutation declares what may change.

### AC-14 — Change Set may include multiple physical edits

One Responsibility may require multiple physical edits.

### AC-15 — Change Set is operational, not semantic identity

Responsibility is semantic; Change Set is operational.

### AC-16 — No Change Set is valid when mutation is unjustified

Change Set = NONE is valid.

---

## 33. Preservation Acceptance Criteria

### AC-17 — Preservation Scope is explicit

Mutating Application records Preservation Scope.

### AC-18 — Unrelated state must remain unchanged

State outside the approved Change Set should be preserved.

### AC-19 — Valid implementations must not be replaced unnecessarily

Canonical replacement is not default behavior.

### AC-20 — Consumer conventions may belong to Preservation Scope

Language, terminology, style and local organization may be preserved.

### AC-21 — Preservation must not block intended change

Preservation does not protect the exact state Application Intent must change.

---

## 34. Planning and Review Acceptance Criteria

### AC-22 — Application Plan precedes mutation

PLAN occurs before APPLY.

### AC-23 — Plan is human-reviewable

Plan can be reviewed manually.

### AC-24 — Plan contains minimum required information

It includes Context, Responsibility, Assessment Outcome, Evidence Refresh, Intent, Change Set, Preservation Scope, Risk/Conflict Notes and Verification Plan.

### AC-25 — Review may stop Application

Plan Review may conclude NO CHANGE, REPLAN, DEFER or REJECTED.

---

## 35. Isolation Acceptance Criteria

### AC-26 — Mutating Application uses isolated candidate state

APPLY does not directly mutate stable consumer state.

### AC-27 — Branch-based isolation is supported

Git branch is a valid isolation mechanism.

### AC-28 — Direct stable-branch mutation is not default

Direct `main` mutation is not promoted.

### AC-29 — Candidate state can be discarded

DISCARD is possible before Integration.

---

## 36. Verification Acceptance Criteria

### AC-30 — APPLY does not imply success

Applied Change ≠ Verified Outcome.

### AC-31 — Verification checks expected changes

VERIFY checks intended mutation occurred.

### AC-32 — Verification checks preservation

VERIFY checks unrelated state remained unchanged.

### AC-33 — Verification checks Application Intent

Verification is not limited to physical file existence or diff application.

### AC-34 — Verification may include semantic reassessment

Affected Responsibility may be re-evaluated.

### AC-35 — Verification supports PASS

PASS is represented.

### AC-36 — Verification supports REFINE

REFINE is represented.

### AC-37 — Verification supports FAIL

FAIL is represented.

### AC-38 — Refinement may return to verification

VERIFY → REFINE → VERIFY AGAIN is supported.

---

## 37. Conflict Acceptance Criteria

### AC-39 — Conflict awareness is represented

Application Plan contains Risk / Conflict Notes.

### AC-40 — Stale state is treated as conflict signal

Relevant consumer changes stop blind execution.

### AC-41 — Automatic semantic conflict resolution is excluded

No automatic semantic winner selection.

### AC-42 — Conflict may produce REPLAN or DEFER

Conflicts may stop or defer execution.

---

## 38. Application Result Acceptance Criteria

### AC-43 — APPLIED is represented

APPLIED records executed candidate Change Set.

### AC-44 — NO CHANGE is represented

NO CHANGE is a valid successful outcome.

### AC-45 — REPLAN is represented

REPLAN exists when Evidence invalidates the plan.

### AC-46 — DEFER is represented

DEFER exists when execution is not currently justified.

### AC-47 — REJECTED is represented

REJECTED exists when Application Plan should not continue.

---

## 39. Idempotency Acceptance Criteria

### AC-48 — Repeated Application must be considered

Guide asks what happens when same Intent is evaluated again.

### AC-49 — Unintended repeated changes should be avoided

Already-satisfied bounded intents should not duplicate changes.

### AC-50 — Universal idempotency is not claimed

No universal idempotency contract.

---

## 40. Integration Boundary Acceptance Criteria

### AC-51 — INTEGRATE is explicitly outside current scope

Delivery boundary is before INTEGRATE.

### AC-52 — Pull Request may represent the boundary

PR may be used as example candidate state.

### AC-53 — Merge policy remains undefined

No merge/squash/rebase/approval contract.

### AC-54 — Post-integration rollback remains excluded

No rollback engine or stable post-merge recovery model.

---

## 41. Representation Acceptance Criteria

### AC-55 — Representation remains Markdown-based

First delivery uses Markdown.

### AC-56 — Application Template is human-readable

No parser/CLI/schema required.

### AC-57 — Application Template is human-editable

Maintainers can edit directly.

### AC-58 — Application Template is Git-reviewable

Changes produce understandable Git diffs.

### AC-59 — No machine contract is introduced

Template is not formal schema or machine API.

---

## 42. Artifact Acceptance Criteria

### AC-60 — Application Guide exists

Reusable guide explains process, boundaries, safety and outcomes.

### AC-61 — Application Template exists

Reusable template supports planning and verification.

### AC-62 — Artifacts integrate with existing Adoption capability

Artifacts remain under `framework/adoption/`.

### AC-63 — Assessment artifacts remain valid

Existing Assessment Guide and Template remain compatible.

---

## 43. Documentation Acceptance Criteria

### AC-64 — Assessment and Application terminology is separated

Assessment understands/decides; Application plans/applies justified change.

### AC-65 — Responsibility remains the semantic unit

No return to file-based adoption.

### AC-66 — Reconciliation over Replacement is explicit

Principle remains documented.

### AC-67 — Evidence before Mutation is explicit

Operational principle is explicit.

### AC-68 — No Change is documented as valid

At least one example demonstrates safe non-mutation.

### AC-69 — Supported and unsupported operations are distinguishable

Readers can identify scope boundaries.

---

## 44. Automation Exclusion Acceptance Criteria

### AC-70 — CLI is not required

Delivery works without CLI.

### AC-71 — GitHub Actions are not required

Delivery works without Actions.

### AC-72 — Automatic semantic assessment is excluded

No automatic semantic Intent determination.

### AC-73 — Automatic mutation is excluded

No automatic repository remediation.

### AC-74 — Automatic integration is excluded

No automatic merge.

---

## 45. Structured Representation Exclusion Criteria

### AC-75 — No schema is introduced

No JSON/YAML/formal schema.

### AC-76 — No manifest is introduced

No stable Application Manifest.

### AC-77 — No parser dependency is introduced

Guide and Template work without tooling.

---

## 46. Delivery Verification

Verification must confirm at least:

```text
Guide exists
Template exists
required fields represented
Assessment boundary preserved
Application boundary explicit
CREATE supported
MODIFY supported
NO CHANGE supported
REPLAN supported
DEFER supported
Preservation represented
Verification represented
INTEGRATE excluded
automation excluded
structured representation excluded
```

---

## 47. Replay Scenarios

### Scenario A — ADAPT / MODIFY

```text
Existing implementation
    Partial

Decision
    ADAPT

Application
    bounded MODIFY

Result
    APPLIED

Verification
    PASS
```

### Scenario B — ADD / CREATE

```text
Existing implementation
    Missing

Decision
    ADD

Application
    bounded CREATE

Result
    APPLIED

Verification
    REFINE → PASS
```

### Scenario C — ADAPT / NO CHANGE

```text
Existing implementation
    Partial

Decision
    ADAPT

Evidence Refresh
    insufficient for safe mutation

Result
    NO CHANGE / REPLAN
```

The three cases must fit the same Guide and Template.

---

## 48. Acceptance Criteria Count

```text
77 Acceptance Criteria
```

These criteria intentionally protect both capability and scope boundaries.

---

## 49. Delivery Readiness for Implementation Planning

With In Scope, Out of Scope, Flow, Representation, Artifacts, Boundary and Acceptance Criteria defined:

```text
Existing Repository Adoption
    Application Core
        READY FOR IMPLEMENTATION PLANNING
```

---

## 50. Final Delivery Scope State

```text
Assessment Core
    RELEASED

Application Discovery
    COMPLETED

Application Repeatability
    MODEL HOLDS

Application Core
    DELIVERY SCOPE DEFINED

Acceptance Criteria
    DEFINED

Implementation Planning
    NEXT

Implementation
    NOT STARTED

Automation
    DEFERRED

Integration
    DEFERRED

Target Version
    NOT COMMITTED

Sprint
    NONE
```

---

## 51. Next Step

Create:

```text
36_APPLICATION_IMPLEMENTATION_PLAN.md
```

to transform this Delivery Scope and the 77 Acceptance Criteria into physical repository changes, work units, validation and delivery sequence.
