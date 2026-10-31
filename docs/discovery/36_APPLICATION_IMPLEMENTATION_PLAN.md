# 36 — Application Implementation Plan

## 1. Propósito

Este documento transforma:

```text
35_APPLICATION_DELIVERY_SCOPE.md
```

en un plan concreto de implementación para:

```text
Existing Repository Adoption
    Application Core
```

sin ampliar el alcance aprobado.

---

## 2. Starting Point

```text
Assessment Core
    RELEASED

Application Discovery
    COMPLETED

Application Repeatability
    MODEL HOLDS

Application Delivery Scope
    DEFINED

Acceptance Criteria
    77

Application Implementation
    NOT STARTED
```

Este documento no reabre Discovery ni introduce nuevas capabilities.

---

## 3. Implementation Objective

Entregar un Application Core:

```text
human-readable
human-editable
Git-reviewable
usable without tooling
```

capaz de representar y guiar:

```text
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

con outcomes:

```text
APPLIED
NO CHANGE
REPLAN
DEFER
REJECTED
```

y Verification Results:

```text
PASS
REFINE
FAIL
```

---

## 4. Proposed Physical Structure

```text
framework/
└── adoption/
    ├── README.md
    ├── assessment-template.md
    └── application/
        ├── README.md
        └── application-template.md
```

Rationale:

```text
preserve Assessment artifacts
keep Application inside Adoption
express Assessment/Application separation
avoid new Component family
allow future evolution without restructuring Assessment
```

---

## 5. Existing Artifact Changes

Minimal update:

```text
framework/adoption/README.md
```

Purpose:

```text
Assessment Core
    ↓
optional Application Core
```

No rewrite of Assessment Guide, fields, vocabulary or flow.

---

## 6. No Functional Change to Assessment Template

Expected:

```text
framework/adoption/assessment-template.md
    PRESERVED
```

Existing Assessment Outcome already provides Decision, Evidence and Rationale.

---

## 7. Implementation Unit A — Application Guide

Artifact:

```text
framework/adoption/application/README.md
```

Responsibility:

> Explicar cómo aplicar de forma selectiva, segura, revisable y verificable una Adoption Decision ya resuelta sobre un consumer existente.

Coverage:

```text
purpose
relationship with Assessment
scope
out-of-scope
Application Flow
Evidence Refresh
Application Intent
Change Set
Preservation Scope
Plan Review
Apply in Isolation
Verification
Application Results
Verification Results
NO CHANGE
REPLAN
DEFER
DISCARD
supported operations
unsupported operations
integration boundary
safety principles
```

---

## 8. Guide Structure Candidate

```text
# Existing Repository Adoption — Application Guide

1. Purpose
2. Relationship with Assessment
3. Application Boundary
4. Core Principles
5. Application Flow
6. Select
7. Refresh Evidence
8. Application Intent
9. Application Plan
10. Change Set
11. Preservation Scope
12. Risk and Conflict Notes
13. Review Plan
14. Apply in Isolation
15. Verification
16. Application Results
17. Verification Results
18. Refinement
19. No Change / Replan / Defer
20. Discard
21. Supported Operations
22. Unsupported Operations
23. Integration Boundary
24. Worked Examples
25. Safety Checklist
```

---

## 9. Guide Content Principle

Guide must be procedural, not a replay of Discovery chronology.

Historical evidence remains in:

```text
docs/discovery/
```

---

## 10. Implementation Unit B — Application Template

Artifact:

```text
framework/adoption/application/application-template.md
```

Responsibility:

> Proporcionar una representación repetible para planificar, ejecutar y verificar una Application concreta.

It must represent:

```text
mutation
non-mutation
refinement
failure
```

without structural redesign.

---

## 11. Template Structure Candidate

```text
# Existing Repository Adoption — Application Record

## 1. Application Context
## 2. Selected Responsibility
## 3. Current Assessment Outcome
## 4. Evidence Refresh
## 5. Application Intent
## 6. Application Readiness
## 7. Candidate Change Set
## 8. Preservation Scope
## 9. Risk / Conflict Notes
## 10. Verification Plan
## 11. Plan Review
## 12. Application Result
## 13. Applied Change Evidence
## 14. Verification Result
## 15. Refinement Notes
## 16. Final Candidate State
## 17. Conclusion
```

---

## 12. Mandatory vs Conditional Fields

Mandatory:

```text
Application Context
Selected Responsibility
Current Assessment Outcome
Evidence Refresh
Application Intent
Preservation Scope
Risk / Conflict Notes
Verification Plan
Application Result
```

Conditional:

```text
Candidate Change Set
    when mutation is planned

Applied Change Evidence
    when Result = APPLIED

Verification Result
    after APPLY

Refinement Notes
    when Verification = REFINE
```

Optional / provisional:

```text
Application Readiness
Consumer Convention Notes
```

---

## 13. Application Context

Minimum:

```text
Consumer
Repository Template
Assessment Reference
Application Date
Application Scope
```

No schema version or machine identifier required.

---

## 14. Selected Responsibility

Reuse:

```text
Responsibility
Requirement Level
Applicability
State
Adoption Decision
Decision Status
```

No full reassessment required before Application.

---

## 15. Evidence Refresh Section

Record:

```text
Current Facts
Current Evidence
Differences from Assessment
Evidence Freshness Result
```

Candidate values:

```text
CURRENT
STALE
INSUFFICIENT
```

These are not a formal schema contract.

---

## 16. Application Intent

Must answer:

> ¿Qué resultado debe producir esta Application si se ejecuta correctamente?

Valid example:

```text
Align backend execution documentation
with current runtime configuration
while preserving valid README content.
```

Insufficient:

```text
Edit README.md
```

---

## 17. Application Readiness

Provisional concept.

Candidate values:

```text
READY
NOT READY
DEFERRED
```

with explicit rationale.

---

## 18. Candidate Change Set

For mutation:

```text
Change ID
Target
Operation
Expected Change
```

Supported Operations:

```text
CREATE
MODIFY
```

Do not present as supported:

```text
DELETE
MOVE
RENAME
```

---

## 19. Preservation Scope

Record what must remain unchanged.

Examples:

```text
unrelated README sections
existing repository structure
consumer language
valid implementation
verified historical content
```

---

## 20. Risk / Conflict Notes

Allow documentation of:

```text
stale assumptions
target changes
equivalent implementation
unsupported historical information
consumer convention mismatch
overlapping change
```

No automatic resolution.

---

## 21. Verification Plan

Defined before APPLY.

Questions:

```text
What should change?
What should remain unchanged?
How will Intent be checked?
What evidence indicates PASS?
What requires REFINE or FAIL?
```

---

## 22. Plan Review

Values:

```text
PROCEED
NO CHANGE
REPLAN
DEFER
REJECTED
```

Only PROCEED moves to APPLY.

---

## 23. Application Result

```text
APPLIED
NO CHANGE
REPLAN
DEFER
REJECTED
```

Plan Review decides whether to proceed; Application Result records what occurred.

---

## 24. Applied Change Evidence

When APPLIED, record:

```text
branch / candidate state
commit or equivalent reference
changed artifacts
diff summary
```

No GitHub automation dependency.

---

## 25. Verification Result

```text
PASS
REFINE
FAIL
```

Justification must use expected change, preservation, Intent and current Evidence.

---

## 26. Refinement Loop

```text
Verification Result
    REFINE
        ↓
bounded adjustment
        ↓
VERIFY AGAIN
```

No new Adoption Decision unless Evidence materially changes the original problem.

---

## 27. Final Candidate State

Candidate values:

```text
VERIFIED
DISCARDED
DEFERRED
REPLAN REQUIRED
```

These describe candidate state, not stable integration.

---

## 28. Implementation Unit C — Adoption Guide Integration

Artifact:

```text
framework/adoption/README.md
```

Minimal integration:

```text
Assessment Core
    ↓
optional Application Core
```

with links to:

```text
assessment-template.md
application/README.md
application/application-template.md
```

---

## 29. Implementation Unit D — Verification and Replay

Replay three real scenarios.

### Replay A — MODIFY

```text
dental-back-spring
README-QUICK-START
ADAPT
```

Must represent:

```text
Evidence Refresh
Application Intent
MODIFY Change Set
Preservation Scope
APPLIED
Verification PASS
```

### Replay B — CREATE

```text
dental-back-spring
DOC-CHANGELOG
ADD
```

Must represent:

```text
CREATE Change Set
consumer convention preservation
APPLIED
REFINE
VERIFY AGAIN
PASS
```

### Replay C — NO CHANGE

```text
aula-robotica-platform
DOC-CHANGELOG
ADAPT
```

Must represent:

```text
Evidence Refresh
insufficient release evidence
no justified Change Set
NO CHANGE / REPLAN
```

---

## 30. Verification Artifact

Create:

```text
docs/implementation/37_APPLICATION_CORE_VERIFICATION.md
```

to record:

```text
Acceptance Criteria verification
Replay A
Replay B
Replay C
Scope boundary checks
Final implementation verdict
```

---

## 31. Acceptance Criteria Verification

All:

```text
AC-01 ... AC-77
```

must have explicit result:

```text
PASS
FAIL
NOT APPLICABLE
```

Expected completion:

```text
AC-01 ... AC-77
    PASS
```

---

## 32. Implementation Units Summary

```text
Unit A
    framework/adoption/application/README.md

Unit B
    framework/adoption/application/application-template.md

Unit C
    framework/adoption/README.md

Unit D
    docs/implementation/37_APPLICATION_CORE_VERIFICATION.md
```

---

## 33. Recommended Implementation Sequence

```text
Unit A
    Application Guide
        ↓
Unit B
    Application Template
        ↓
Unit C
    Adoption Guide Integration
        ↓
Unit D
    Replay + Acceptance Criteria Verification
```

---

## 34. Proposed Work Items

```text
Work Item 1
    Application Guide

Work Item 2
    Application Template

Work Item 3
    Verification and Integration
```

This deliberately mirrors the v0.7.0 Assessment Core delivery pattern.

---

## 35. Work Item 1 — Application Guide

Create:

```text
framework/adoption/application/README.md
```

Cover Assessment boundary, Application flow, Evidence Refresh, Intent, Change Set, Preservation, Review, Isolation, Verification, vocabulary, supported operations and Integration boundary.

---

## 36. Work Item 2 — Application Template

Create:

```text
framework/adoption/application/application-template.md
```

It must represent all three replay scenarios without structural changes.

---

## 37. Work Item 3 — Verification and Integration

Update:

```text
framework/adoption/README.md
```

Create:

```text
docs/implementation/37_APPLICATION_CORE_VERIFICATION.md
```

Verify all 77 ACs, replay scenarios, Assessment compatibility and scope boundaries.

---

## 38. Dependency Order

```text
Guide
    before
Template finalization

Guide + Template
    before
Verification

Verification
    before
delivery completion
```

---

## 39. Branch Strategy

Implementation should start from:

```text
main
```

Candidate branch:

```text
feature/application-core
```

No `develop` branch is required.

---

## 40. Commit Strategy

Recommended:

```text
docs(adoption): add application guide

docs(adoption): add application template

docs(adoption): integrate application capability

docs(implementation): verify application core
```

---

## 41. Pull Request Boundary

Preferred delivery pattern:

```text
one PR per major Work Item
```

if formalized through independent Issues.

This is a project-management preference, not an Application Core contract.

---

## 42. Issue Structure Candidate

If formalized as the next Sprint:

```text
Application Guide

Application Template

Application Core Verification and Integration
```

Issues should not be created until Implementation Plan is closed and next increment is formally selected.

---

## 43. Verification Gate

Before completion:

```text
Guide
    complete

Template
    complete

Assessment integration
    complete

Replay A
    PASS

Replay B
    PASS

Replay C
    PASS

AC-01 ... AC-77
    PASS

Out-of-Scope audit
    PASS
```

Expected verdict:

```text
IMPLEMENTATION VERIFIED
```

---

## 44. Scope Creep Guardrail

Do not add:

```text
automation
CLI
schema
manifest
automatic repository scanning
automatic PR creation
automatic integration
DELETE
MOVE
RENAME
```

New needs return to future Discovery/backlog.

---

## 45. Documentation Language

Governance, Discovery and Implementation documentation remains Spanish with English technical terminology where it belongs to Framework vocabulary.

New artifacts under `framework/adoption/` must remain coherent with existing Assessment artifacts.

---

## 46. Backward Compatibility

```text
existing assessment records
    remain valid

Application
    consumes them optionally
```

No migration of historical assessments is required.

---

## 47. No Migration Required

No migration is required for:

```text
assessment-template.md
historical assessments
Discovery documents
```

---

## 48. Implementation Completion Condition

```text
Application Guide
    delivered

Application Template
    delivered

Assessment integration
    delivered

Application verification
    PASS

77 Acceptance Criteria
    PASS

three replay scenarios
    PASS
```

without scope creep.

---

## 49. Implementation Plan Result

Physical candidate:

```text
framework/adoption/
├── README.md
├── assessment-template.md
└── application/
    ├── README.md
    └── application-template.md

docs/implementation/
└── 37_APPLICATION_CORE_VERIFICATION.md
```

---

## 50. Implementation Readiness

With physical structure, work units, dependency order, replay strategy, verification strategy and scope guardrails defined:

```text
Application Core
    READY FOR IMPLEMENTATION
```

---

## 51. What READY FOR IMPLEMENTATION Means

Repository work may begin without more Discovery.

It does not yet mean:

```text
release target committed
Sprint opened
version selected
```

---

## 52. Recommended Delivery Shape

Use the validated v0.7.0 pattern:

```text
Issue 1
    Application Guide

Issue 2
    Application Template

Issue 3
    Verification & Integration
```

with a milestone only after formally selecting the next increment.

---

## 53. Final Implementation Plan State

```text
Assessment Core
    RELEASED

Application Discovery
    COMPLETED

Application Repeatability
    MODEL HOLDS

Application Delivery Scope
    DEFINED

Application Implementation Plan
    DEFINED

Application Core
    READY FOR IMPLEMENTATION

Implementation
    NOT STARTED

Sprint
    NOT OPENED

Milestone
    NOT CREATED

Target Version
    NOT COMMITTED
```

---

## 54. Next Decision

```text
Should Application Core
become the next delivery increment?
```

If yes:

```text
define target increment
    ↓
create milestone
    ↓
create implementation Issues
    ↓
open implementation branch
```

while preserving the scope defined in `35_APPLICATION_DELIVERY_SCOPE.md`.
