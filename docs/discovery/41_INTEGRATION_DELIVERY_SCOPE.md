# 41 — Existing Repository Adoption Integration Delivery Scope

## 1. Propósito

Definir el primer Delivery Scope reusable para:

```text
Existing Repository Adoption
    Integration Core
```

a partir de la evidencia de:

```text
38_INTEGRATION_DISCOVERY.md
39_INTEGRATION_DISCOVERY_SYNTHESIS.md
40_INTEGRATION_REPEATABILITY_EXPERIMENT.md
```

---

## 2. Delivery Scope Question

La pregunta de scope es:

> ¿Cuál es el mínimo Integration Core respaldado por evidencia que permite llevar un verified candidate state hasta stable consumer state de forma human-reviewed y verificable sin introducir automation, recovery orchestration o representación formal prematura?

---

## 3. Starting Point

Input:

```text
Verified Candidate State
```

producido por Application Core.

Output candidate:

```text
Verified Stable Consumer State
```

o un safe stop outcome.

---

## 4. Core Boundary

```text
APPLICATION CORE

APPLY IN ISOLATION
    ↓
VERIFY
    ↓
Verified Candidate State

────────────────────────────

INTEGRATION CORE

REFRESH STABLE BASE
    ↓
EVALUATE DRIFT
    ↓
CHECK INTEGRATION CONDITIONS
    ↓
REVIEW
    ↓
INTEGRATE
    ↓
VERIFY STABLE STATE
    ↓
CONFIRM
```

---

## 5. Integration Core Objective

Convertir un verified candidate state en:

```text
stable integrated state
```

o:

```text
DEFER
REPLAN
REJECT
RECOVERY REQUIRED
```

de forma:

```text
governance-aware
reviewable
traceable
preserving
verifiable
```

---

## 6. In Scope

```text
Verified Candidate selection
Stable Base Refresh
Drift Impact Evaluation
Integration Conditions
Consumer Governance Constraints
Human Review
Integration Decision
Integration Method recording
Integration Evidence
Stable-State Verification
Recovery Required representation
Final Integration State
```

---

## 7. Supported Integration Decision

Directly supported:

```text
INTEGRATE
```

Supported safe-stop outcomes:

```text
DEFER
REPLAN
REJECT
```

---

## 8. Supported Final States

Stable candidate vocabulary:

```text
INTEGRATED
DEFERRED
REPLAN REQUIRED
REJECTED
RECOVERY REQUIRED
```

`RECOVERY REQUIRED` represents failed stable-state verification without prescribing recovery execution.

---

## 9. Merge Strategy Boundary

The Integration Core does not prescribe:

```text
merge commit
squash merge
rebase merge
```

The consumer repository determines the allowed strategy.

The Integration Record stores the actual method used.

---

## 10. Pull Request Boundary

Pull Requests are:

```text
supported Integration surface
```

but are not:

```text
mandatory universal mechanism
```

The conceptual model remains broader than GitHub Pull Requests.

---

## 11. Stable Base Refresh

Before Integration, current stable state must be checked.

Record:

```text
Stable Base Reference
Current Stable Reference
Base Drift
Relevant Stable Changes
```

---

## 12. Drift Impact

When drift exists, evaluate:

```text
target overlap
Intent validity
Preservation validity
governance changes
release constraints
```

Outcomes:

```text
COMPATIBLE
INVALIDATING
UNCERTAIN
```

This vocabulary is descriptive and not a schema contract.

---

## 13. Integration Conditions

Integration conditions may include:

```text
mergeability
required reviews
required checks
branch protection
base freshness
release constraints
```

No fixed universal checklist is imposed.

---

## 14. Consumer Governance

Principle:

```text
Consumer Governance
    over
Framework Merge Preference
```

The Framework records and respects observed constraints.

It does not configure them in this delivery.

---

## 15. Human Review

Before stable mutation, review:

```text
candidate still verified
stable base current enough
drift impact understood
Intent still valid
Preservation still valid
conditions satisfied
governance satisfied
```

---

## 16. Integration Review Result

Candidate review results:

```text
PROCEED
DEFER
REPLAN
REJECT
```

Only `PROCEED` permits Integration.

---

## 17. Integration Method

When Integration occurs, record:

```text
merge method
stable target
integration reference
```

No method is mandatory across consumers.

---

## 18. Integration Evidence

When integrated, preserve:

```text
stable mutation reference
merge commit or equivalent
changed artifacts
integration summary
```

---

## 19. Stable-State Verification

After Integration verify at least:

```text
expected stable change
Application Intent
Preservation Scope
```

Repository health may also be verified when relevant.

---

## 20. Verification Dimensions

Supported:

```text
Physical Verification
Intent Verification
Preservation Verification
Repository Health Verification
```

Not all dimensions must be equally deep in every consumer.

---

## 21. Stable-State Verification Result

Candidate vocabulary:

```text
PASS
FAIL
```

A failed stable-state verification produces:

```text
RECOVERY REQUIRED
```

without prescribing a recovery mechanism.

---

## 22. Recovery Boundary

In scope:

```text
detect failure
record failure
mark RECOVERY REQUIRED
preserve evidence
```

Out of scope:

```text
automatic revert
automatic rollback
branch reset
release rollback
recovery orchestration
```

---

## 23. Conflict Boundary

In scope:

```text
detect conflict
record conflict
DEFER
REPLAN
REJECT
```

Out of scope:

```text
automatic semantic conflict resolution
```

---

## 24. Branch Protection Boundary

Integration may observe:

```text
required reviews
required checks
linear history
direct push restrictions
```

It does not configure branch protection.

---

## 25. Release Boundary

Integration may record:

```text
release freeze
release branch
version constraint
timing constraint
```

It does not implement:

```text
release orchestration
tagging
deployment
release rollback
```

---

## 26. Automation — Out of Scope

No:

```text
automatic merge
automatic approval
automatic PR creation
automatic conflict resolution
automatic rollback
continuous Integration remediation
```

Human Review remains explicit.

---

## 27. Structured Representation — Out of Scope

No requirement for:

```text
JSON
YAML
Schema
Manifest
typed Integration Plan
machine API
```

Representation remains Markdown.

---

## 28. Relationship with Application Core

```text
Application
    produces
        verified candidate

Integration
    consumes
        verified candidate
```

Integration does not silently rewrite Application history.

---

## 29. Relationship with Assessment Core

Traceability remains:

```text
Assessment
    ↓
Application
    ↓
Integration
```

Integration does not reassess the original Responsibility unless new evidence requires REPLAN.

---

## 30. Proposed Integration Representation

```text
Structured Markdown
```

Properties:

```text
human-readable
human-editable
Git-reviewable
usable without tooling
```

---

## 31. Candidate Integration Record

```text
Integration Context
Candidate Reference
Application Outcome
Stable Base Reference
Stable Base Refresh
Drift Impact
Integration Conditions
Governance Constraints
Integration Review
Integration Decision
Integration Method
Integration Evidence
Stable-State Verification
Recovery Notes
Final Integration State
Conclusion
```

---

## 32. Mandatory Fields

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

## 33. Conditional Fields

Conditional:

```text
Drift Impact
    when drift exists

Integration Method
Integration Evidence
    when Integration occurs

Recovery Notes
    when failure or recovery requirement exists
```

---

## 34. Contextual Fields

Contextual / provisional:

```text
Governance Constraints
Release Constraints
Repository Health Evidence
```

---

## 35. Reusable Artifact Candidates

Candidate artifacts:

```text
framework/adoption/integration/README.md
framework/adoption/integration/integration-template.md
```

Minimal integration update:

```text
framework/adoption/README.md
```

Verification candidate:

```text
docs/implementation/43_INTEGRATION_CORE_VERIFICATION.md
```

Artifact names remain candidates until Implementation Planning.

---

## 36. Non-Goals

This delivery is not:

```text
merge bot
release system
branch-protection manager
rollback engine
conflict resolver
deployment orchestrator
```

---

## 37. Delivery Principles

```text
Verified Candidate before Integration
Refresh Stable Base
Evaluate Drift Impact
Consumer Governance over Framework Preference
Human Review before Stable Integration
Mergeability is not Readiness
Verify Stable State after Integration
Represent Recovery without automating it
```

---

## 38. Delivery Scope Summary

In scope:

```text
manual Integration
human review
consumer governance observation
stable-base refresh
drift evaluation
stable mutation
post-integration verification
failure representation
```

Out of scope:

```text
automation
automatic recovery
release orchestration
branch protection configuration
Structured Data
```

---

## 39. Delivery Boundary

The first Integration Core ends at:

```text
verified stable state
```

or:

```text
safe stopped / recovery-required state
```

It does not manage later release or deployment lifecycle.

---

## 40. Acceptance Criteria

### AC-01 — Integration begins from a verified candidate state

Result expected:

```text
PASS
```

### AC-02 — Integration remains downstream from Application

Result expected:

```text
PASS
```

### AC-03 — Stable base refresh is required before Integration

Result expected:

```text
PASS
```

### AC-04 — Base drift must be evaluated rather than automatically rejected

Result expected:

```text
PASS
```

### AC-05 — Mergeability remains distinct from Integration readiness

Result expected:

```text
PASS
```

### AC-06 — Integration conditions must be reviewable

Result expected:

```text
PASS
```

### AC-07 — Consumer governance takes precedence over Framework merge preference

Result expected:

```text
PASS
```

### AC-08 — Application Intent must remain valid at Integration time

Result expected:

```text
PASS
```

### AC-09 — Preservation Scope must remain valid at Integration time

Result expected:

```text
PASS
```

### AC-10 — Unsupported facts must not be invented during Integration

Result expected:

```text
PASS
```

### AC-11 — Human review occurs before stable mutation

Result expected:

```text
PASS
```

### AC-12 — Integration Decision is explicit

Result expected:

```text
PASS
```

### AC-13 — INTEGRATE is directly supported

Result expected:

```text
PASS
```

### AC-14 — DEFER is a valid non-integration outcome

Result expected:

```text
PASS
```

### AC-15 — REPLAN is a valid non-integration outcome

Result expected:

```text
PASS
```

### AC-16 — REJECT is a valid non-integration outcome

Result expected:

```text
PASS
```

### AC-17 — Integration Method is recorded when Integration occurs

Result expected:

```text
PASS
```

### AC-18 — Stable mutation evidence is recorded

Result expected:

```text
PASS
```

### AC-19 — Stable-state verification is required after Integration

Result expected:

```text
PASS
```

### AC-20 — Merge success alone is insufficient

Result expected:

```text
PASS
```

### AC-21 — Physical stable-state verification is supported

Result expected:

```text
PASS
```

### AC-22 — Intent stable-state verification is supported

Result expected:

```text
PASS
```

### AC-23 — Preservation stable-state verification is supported

Result expected:

```text
PASS
```

### AC-24 — Repository health evidence may be recorded when relevant

Result expected:

```text
PASS
```

### AC-25 — Stable-state verification result is explicit

Result expected:

```text
PASS
```

### AC-26 — Successful Integration produces INTEGRATED state

Result expected:

```text
PASS
```

### AC-27 — Failed stable-state verification can produce RECOVERY REQUIRED

Result expected:

```text
PASS
```

### AC-28 — Recovery requirement can be represented without recovery execution

Result expected:

```text
PASS
```

### AC-29 — Automatic rollback is excluded

Result expected:

```text
PASS
```

### AC-30 — Automatic merge is excluded

Result expected:

```text
PASS
```

### AC-31 — Automatic conflict resolution is excluded

Result expected:

```text
PASS
```

### AC-32 — Branch protection is observed and respected, not configured

Result expected:

```text
PASS
```

### AC-33 — Required reviews are consumer-contextual

Result expected:

```text
PASS
```

### AC-34 — Required checks are consumer-contextual

Result expected:

```text
PASS
```

### AC-35 — Merge strategy is consumer-governance controlled

Result expected:

```text
PASS
```

### AC-36 — Pull Requests are a valid Integration surface but not mandatory

Result expected:

```text
PASS
```

### AC-37 — Release constraints may be recorded when present

Result expected:

```text
PASS
```

### AC-38 — Release orchestration is excluded

Result expected:

```text
PASS
```

### AC-39 — Application refinement history does not require a different Integration lifecycle

Result expected:

```text
PASS
```

### AC-40 — CREATE and MODIFY use the same Integration lifecycle

Result expected:

```text
PASS
```

### AC-41 — Integration representation remains Markdown

Result expected:

```text
PASS
```

### AC-42 — Integration record remains human-readable

Result expected:

```text
PASS
```

### AC-43 — Integration record remains human-editable

Result expected:

```text
PASS
```

### AC-44 — Integration record remains Git-reviewable

Result expected:

```text
PASS
```

### AC-45 — No schema is required

Result expected:

```text
PASS
```

### AC-46 — No manifest is required

Result expected:

```text
PASS
```

### AC-47 — No parser dependency is required

Result expected:

```text
PASS
```

### AC-48 — No machine contract is required

Result expected:

```text
PASS
```

### AC-49 — Assessment artifacts remain valid

Result expected:

```text
PASS
```

### AC-50 — Application artifacts remain valid

Result expected:

```text
PASS
```

### AC-51 — Integration does not rewrite Assessment history

Result expected:

```text
PASS
```

### AC-52 — Integration does not rewrite Application history

Result expected:

```text
PASS
```

### AC-53 — Integration evidence preserves traceability

Result expected:

```text
PASS
```

### AC-54 — Stable Base Reference is recorded

Result expected:

```text
PASS
```

### AC-55 — Candidate Reference is recorded

Result expected:

```text
PASS
```

### AC-56 — Stable Base Refresh outcome is recorded

Result expected:

```text
PASS
```

### AC-57 — Drift Impact is recorded when drift exists

Result expected:

```text
PASS
```

### AC-58 — Integration Conditions are recorded

Result expected:

```text
PASS
```

### AC-59 — Governance Constraints can be recorded

Result expected:

```text
PASS
```

### AC-60 — Integration Review result is recorded

Result expected:

```text
PASS
```

### AC-61 — Integration Decision is recorded

Result expected:

```text
PASS
```

### AC-62 — Integration Method is recorded when applicable

Result expected:

```text
PASS
```

### AC-63 — Integration Evidence is recorded when applicable

Result expected:

```text
PASS
```

### AC-64 — Stable-State Verification is recorded

Result expected:

```text
PASS
```

### AC-65 — Recovery Notes are conditional

Result expected:

```text
PASS
```

### AC-66 — Final Integration State is recorded

Result expected:

```text
PASS
```

### AC-67 — Integration Conclusion is recorded

Result expected:

```text
PASS
```

### AC-68 — Replay A must remain representable

Result expected:

```text
PASS
```

### AC-69 — Replay B must remain representable

Result expected:

```text
PASS
```

### AC-70 — Out-of-scope audit must pass

Result expected:

```text
PASS
```

### AC-71 — Delivery remains compatible with manual operation

Result expected:

```text
PASS
```

### AC-72 — Automation remains deferred

Result expected:

```text
PASS
```

### AC-73 — Structured Representation remains deferred

Result expected:

```text
PASS
```


---

## 41. Replay Scenarios

Replay A:

```text
ADAPT
MODIFY
no drift
INTEGRATE
PASS
INTEGRATED
```

Replay B:

```text
ADD
CREATE
REFINE → PASS
compatible drift
INTEGRATE
PASS
INTEGRATED
```

Both must be representable without structural redesign.

---

## 42. Acceptance Criteria Count

```text
AC-01 through AC-73

Total
    73
```

---

## 43. Delivery Verification

Before implementation planning:

```text
Lifecycle consistency
    PASS

Replay A
    PASS

Replay B
    PASS

Representation stability
    PASS

Scope audit
    PASS

Automation exclusion
    PASS

Structured Representation exclusion
    PASS
```

---

## 44. Delivery Readiness for Implementation Planning

Evidence status:

```text
Observed Need
    PASS

Repeated Integration
    PASS

Cross-operation Evidence
    PASS

Drift Handling
    PASS

Stable-State Verification
    PASS

Representation Stability
    PASS

Proportional Complexity
    PASS
```

Therefore:

```text
Integration Core
    READY FOR IMPLEMENTATION PLANNING
```

---

## 45. Final Delivery Scope State

```text
Integration Discovery
    COMPLETED

Integration Repeatability
    MODEL HOLDS

Integration Delivery Scope
    DEFINED

Integration Core
    READY FOR IMPLEMENTATION PLANNING

Next Version
    NOT COMMITTED

Next Sprint
    NOT OPENED
```

---

## 46. Next Step

Create:

```text
42_INTEGRATION_IMPLEMENTATION_PLAN.md
```

Do not yet create:

```text
implementation issues
milestone
target version
Sprint 11
```
