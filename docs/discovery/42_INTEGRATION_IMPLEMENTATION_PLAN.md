# 42 — Existing Repository Adoption Integration Implementation Plan

## 1. Purpose

Definir el plan de implementación del:

```text
Existing Repository Adoption
    Integration Core
```

a partir del Delivery Scope establecido en:

```text
docs/discovery/41_INTEGRATION_DELIVERY_SCOPE.md
```

Este plan no abre Sprint ni compromete versión.

---

## 2. Planning Input

Evidence chain:

```text
38_INTEGRATION_DISCOVERY.md
    ↓
39_INTEGRATION_DISCOVERY_SYNTHESIS.md
    ↓
40_INTEGRATION_REPEATABILITY_EXPERIMENT.md
    ↓
41_INTEGRATION_DELIVERY_SCOPE.md
```

Current result:

```text
Integration Core
    READY FOR IMPLEMENTATION PLANNING
```

---

## 3. Physical Structure Candidate

Recommended structure:

```text
framework/adoption/
├── README.md
├── assessment-template.md
├── application/
│   ├── README.md
│   └── application-template.md
└── integration/
    ├── README.md
    └── integration-template.md

docs/implementation/
└── 43_INTEGRATION_CORE_VERIFICATION.md
```

This preserves the existing capability hierarchy:

```text
Assessment
    ↓
Application
    ↓
Integration
```

---

## 4. Why a Nested Integration Namespace

Integration is:

```text
part of Existing Repository Adoption
```

but distinct from:

```text
Assessment
Application
```

A dedicated namespace:

```text
framework/adoption/integration/
```

keeps lifecycle responsibilities explicit without creating a new Component family.

---

## 5. Existing Artifact Impact

Expected changes:

```text
framework/adoption/README.md
    minimal Integration reference

new:
    framework/adoption/integration/README.md
    framework/adoption/integration/integration-template.md
    docs/implementation/43_INTEGRATION_CORE_VERIFICATION.md
```

No functional migration is required for:

```text
assessment-template.md
application-template.md
historical assessments
historical application records
```

---

## 6. Implementation Unit A — Integration Guide

Artifact:

```text
framework/adoption/integration/README.md
```

Responsibility:

> Explicar cómo y por qué un verified candidate state puede integrarse de forma segura y verificable en stable consumer state.

---

## 7. Integration Guide Candidate Sections

```text
Purpose
Relationship with Application
Integration boundary
Core principles
Verified Candidate input
Stable Base Refresh
Drift Impact
Integration Conditions
Consumer Governance
Integration Review
Integration Decision
Integration Method
Integration Evidence
Stable-State Verification
Recovery Required
Final Integration State
Safe stop outcomes
Pull Request boundary
Merge strategy boundary
Branch protection boundary
Release boundary
Automation boundary
Representation boundary
Examples
Safety checklist
```

---

## 8. Guide Stable Principles

The Guide should preserve:

```text
Verified Candidate before Integration
Refresh Stable Base
Evaluate Drift Impact
Consumer Governance over Framework Preference
Mergeability is not Integration Readiness
Human Review before Stable Integration
Verify Stable State after Integration
Represent Recovery without automating it
```

---

## 9. Implementation Unit B — Integration Template

Artifact:

```text
framework/adoption/integration/integration-template.md
```

Responsibility:

> Proporcionar una representación repetible para revisar, ejecutar y verificar una Integration concreta.

---

## 10. Integration Template Candidate Structure

```text
# Existing Repository Adoption — Integration Record

## 1. Integration Context
## 2. Candidate Reference
## 3. Application Outcome
## 4. Stable Base Reference
## 5. Stable Base Refresh
## 6. Drift Impact
## 7. Integration Conditions
## 8. Governance Constraints
## 9. Integration Review
## 10. Integration Decision
## 11. Integration Method
## 12. Integration Evidence
## 13. Stable-State Verification
## 14. Recovery Notes
## 15. Final Integration State
## 16. Conclusion
```

---

## 11. Mandatory Template Fields

Mandatory:

```text
Integration Context
Candidate Reference
Application Outcome
Stable Base Reference
Stable Base Refresh
Integration Conditions
Integration Review
Integration Decision
Stable-State Verification
Final Integration State
Conclusion
```

---

## 12. Conditional Template Fields

Conditional:

```text
Drift Impact
    when drift exists

Integration Method
Integration Evidence
    when Integration occurs

Recovery Notes
    when verification fails
    or recovery is required
```

---

## 13. Contextual Template Fields

Contextual / provisional:

```text
Governance Constraints
Release Constraints
Repository Health Evidence
```

These must not become mandatory without evidence.

---

## 14. Integration Decision Vocabulary

Delivery candidate:

```text
INTEGRATE
DEFER
REPLAN
REJECT
```

Directly evidenced:

```text
INTEGRATE
```

Others remain safe-stop outcomes supported by the model.

---

## 15. Final Integration State Vocabulary

Candidate:

```text
INTEGRATED
DEFERRED
REPLAN REQUIRED
REJECTED
RECOVERY REQUIRED
```

The Template must allow all without requiring automation.

---

## 16. Drift Impact Representation

Candidate descriptive vocabulary:

```text
NONE
COMPATIBLE
INVALIDATING
UNCERTAIN
```

This remains human-readable descriptive vocabulary, not a schema enum.

---

## 17. Integration Conditions Representation

The Template should allow recording:

```text
mergeability
reviews
status checks
workflow runs
branch protection
release constraints
other consumer-specific conditions
```

without making all fields mandatory.

---

## 18. Governance Constraints Representation

Record only observed constraints.

Examples:

```text
required approval
CODEOWNERS
required checks
linear history
merge method restrictions
release freeze
```

Do not invent controls absent from the consumer repository.

---

## 19. Integration Review

Candidate results:

```text
PROCEED
DEFER
REPLAN
REJECT
```

Only:

```text
PROCEED
```

permits stable mutation.

---

## 20. Integration Method

When Integration occurs, record actual method.

Examples:

```text
merge commit
squash merge
rebase merge
equivalent platform operation
```

The Framework does not select a universal default.

---

## 21. Integration Evidence

When Integration occurs, record:

```text
stable target
merge/integration reference
changed artifacts
integration summary
```

No GitHub-specific identifier is mandatory conceptually.

---

## 22. Stable-State Verification

Required after Integration.

Candidate dimensions:

```text
Physical Verification
Intent Verification
Preservation Verification
Repository Health Verification
```

The first three are core candidates.

Repository Health is contextual.

---

## 23. Stable-State Verification Result

Candidate:

```text
PASS
FAIL
```

When:

```text
FAIL
```

the final state may be:

```text
RECOVERY REQUIRED
```

without executing recovery.

---

## 24. Recovery Notes

Recovery Notes should allow:

```text
failure evidence
impact
recommended manual next step
known recovery options
```

but must not prescribe or execute automatic recovery.

---

## 25. Implementation Unit C — Adoption Guide Integration

Artifact:

```text
framework/adoption/README.md
```

Minimal update:

```text
Assessment Core
    ↓
optional Application Core
    ↓
optional Integration Core
```

The Assessment and Application representations remain valid.

---

## 26. Root Adoption Boundary

The root guide should clarify:

```text
Assessment
    independently useful

Application
    optional downstream

Integration
    optional downstream of verified Application
```

No stage becomes mandatory merely because a later capability exists.

---

## 27. Implementation Unit D — Verification and Replay

Artifact:

```text
docs/implementation/43_INTEGRATION_CORE_VERIFICATION.md
```

Responsibility:

> Verify Guide + Template + Adoption integration against the 73 Delivery Scope Acceptance Criteria and representative replay.

---

## 28. Verification Replay A

```text
Consumer
    dental-back-spring

Candidate
    PR #1

Operation
    MODIFY

Drift
    NONE

Integration
    PASS

Stable Verification
    PASS
```

Expected:

```text
REPRESENTATION PASS
```

---

## 29. Verification Replay B

```text
Consumer
    dental-back-spring

Candidate
    PR #2

Operation
    CREATE

Application history
    REFINE → PASS

Drift
    COMPATIBLE

Integration
    PASS

Stable Verification
    PASS
```

Expected:

```text
REPRESENTATION PASS
```

---

## 30. Verification of Safe-Stop Outcomes

The Template must represent without mutation:

```text
DEFER
REPLAN
REJECT
```

and after failed stable verification:

```text
RECOVERY REQUIRED
```

No fictitious merge evidence should be required for non-integration outcomes.

---

## 31. Acceptance Criteria Gate

Verification must explicitly cover:

```text
AC-01 through AC-73
```

Expected:

```text
73 PASS
0 FAIL
```

N/A should only be used where an Acceptance Criterion is explicitly conditional and evidence justifies it.

---

## 32. Scope Audit

Verify absence of:

```text
automatic merge
automatic approval
automatic rollback
automatic conflict resolution
branch protection configuration
release orchestration
Structured Data
Schema
Manifest
CLI
GitHub Actions
```

---

## 33. Backward Compatibility Gate

Confirm:

```text
Assessment Guide
    valid

Assessment Template
    valid

Application Guide
    valid

Application Template
    valid

historical records
    no migration
```

---

## 34. Implementation Dependency Graph

```text
Integration Guide ─────────┐
                           ├──► Verification & Integration
Integration Template ──────┤
                           │
Adoption Guide Update ─────┘
```

---

## 35. Recommended Implementation Sequence

```text
1. Integration Guide
2. Integration Template
3. Adoption Guide Integration
4. Verification & Replay
```

Guide before Template mirrors the validated delivery pattern.

---

## 36. Candidate Work Items

If formally selected as an implementation increment:

### Work Item 1

```text
Implement Existing Repository Adoption Integration Guide
```

### Work Item 2

```text
Implement Existing Repository Adoption Integration Template
```

### Work Item 3

```text
Validate and integrate Existing Repository Adoption Integration Core
```

The root Adoption Guide update can be included in Work Item 3.

---

## 37. Issue Boundary

No implementation Issues should be created until:

```text
Implementation Plan
    CLOSED

next increment
    FORMALLY SELECTED
```

---

## 38. Milestone Boundary

Do not create a milestone until:

```text
target version selected
Sprint formally opened
```

---

## 39. Version Boundary

This plan does not decide:

```text
v0.9.0
v1.0.0
or any other target
```

Version selection is a separate governance decision.

---

## 40. Candidate Branch Strategy

Implementation candidate:

```text
feature/integration-core
```

or one feature branch per independent Work Item.

Final workflow choice should follow existing project practice at Sprint opening.

---

## 41. Commit Strategy

Candidate commits:

```text
docs(adoption): add integration guide

docs(adoption): add integration template

docs(adoption): integrate integration capability

docs(implementation): verify integration core
```

---

## 42. Pull Request Boundary

Preferred:

```text
one PR per major implementation Issue
```

to preserve reviewability.

---

## 43. Definition of Ready

Before implementation Sprint:

```text
Delivery Scope defined
Acceptance Criteria fixed
physical structure defined
Work Items defined
dependencies defined
verification replay defined
scope guardrails defined
target version selected
milestone created
Issues created
```

---

## 44. Definition of Done

Integration Core implementation is complete when:

1. Integration Guide exists.
2. Integration Template exists.
3. Root Adoption Guide references Integration correctly.
4. Guide and Template use consistent vocabulary.
5. Verified Candidate input is explicit.
6. Stable Base Refresh is explicit.
7. Drift Impact is representable.
8. Consumer Governance is respected.
9. Integration Review is explicit.
10. INTEGRATE / DEFER / REPLAN / REJECT are representable.
11. Integration Method and Evidence are recordable.
12. Stable-State Verification is required after Integration.
13. RECOVERY REQUIRED is representable.
14. Automatic recovery remains excluded.
15. Replay A passes.
16. Replay B passes.
17. AC-01 through AC-73 pass.
18. Scope audit passes.
19. Backward compatibility passes.
20. Verification verdict is IMPLEMENTATION VERIFIED.

---

## 45. Verification Verdict

Expected:

```text
Existing Repository Adoption
    Integration Core

IMPLEMENTATION VERIFIED
```

---

## 46. No Migration Required

No migration required for:

```text
framework/adoption/assessment-template.md
framework/adoption/application/application-template.md
historical Assessment records
historical Application records
Discovery documents
```

---

## 47. Documentation Language

Governance, Discovery and Implementation docs remain Spanish with English Framework vocabulary where appropriate.

New reusable artifacts should remain coherent with existing Adoption artifacts.

---

## 48. Scope Creep Guardrail

Do not introduce:

```text
automation
automatic merge
automatic rollback
automatic conflict resolution
release orchestration
branch protection configuration
CLI
GitHub Actions
Schema
Manifest
Structured Data
```

New needs return to Discovery/backlog.

---

## 49. Implementation Completion Condition

```text
Guide
    delivered

Template
    delivered

Adoption integration
    delivered

Replay A
    PASS

Replay B
    PASS

AC-01 through AC-73
    PASS

Out-of-Scope audit
    PASS

Integration Core
    IMPLEMENTATION VERIFIED
```

---

## 50. Single-Sprint Suitability

Implementation Units are:

```text
documentation-focused
low-coupling
bounded
sequentially clear
```

No runtime engine, CLI, schema or automation is required.

Therefore:

```text
Integration Core
    SUITABLE FOR A SINGLE SPRINT
```

---

## 51. Implementation Readiness

With physical structure, Work Items, dependency order, replay strategy, AC gate and scope guardrails defined:

```text
Integration Core
    READY FOR IMPLEMENTATION
```

---

## 52. What READY FOR IMPLEMENTATION Means

Repository implementation may begin after formal governance selection.

It does not yet mean:

```text
target version committed
milestone created
Sprint opened
Issues created
```

---

## 53. Recommended Governance Next Step

After this plan is reviewed and merged:

```text
select next increment
    ↓
select target version
    ↓
create milestone
    ↓
create implementation Issues
    ↓
open Sprint
```

No implementation should start before that decision.

---

## 54. Final Planning State

```text
Integration Discovery
    COMPLETED

Integration Discovery Synthesis
    COMPLETED

Integration Repeatability
    MODEL HOLDS

Integration Delivery Scope
    DEFINED

Integration Implementation Plan
    DEFINED

Integration Core
    READY FOR IMPLEMENTATION

Implementation
    NOT STARTED

Target Version
    NOT COMMITTED

Sprint
    NOT OPENED
```
