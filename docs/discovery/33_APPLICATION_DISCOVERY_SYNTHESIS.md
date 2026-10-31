# 33 — Application Discovery Synthesis

## 1. Propósito

Este documento sintetiza la investigación de Existing Repository Adoption Application desarrollada en:

```text
32_APPLICATION_DISCOVERY.md
```

La pregunta central es:

> ¿Existe evidencia suficiente para promover una parte mínima de Existing Repository Adoption Application desde Discovery hacia Delivery Scope sin introducir automatización, formalización o capacidad operacional no respaldada?

---

## 2. Evidence Base

Consumer principal:

```text
fran-eliot/dental-back-spring
```

Casos reales:

```text
README-QUICK-START
    Partial
    ADAPT
    MODIFY

DOC-CHANGELOG
    Missing
    ADD
    CREATE
```

---

## 3. Experimental Results

### ADAPT / MODIFY

```text
Evidence Refresh
    PASS

Application Planning
    PASS

Scope Preservation
    PASS

APPLY in isolated branch
    PASS

VERIFY
    PASS

Operational Idempotency
    PASS

INTEGRATE
    PENDING
```

### ADD / CREATE

```text
Evidence Refresh
    PASS

Application Planning
    PASS

Scope Preservation
    PASS

APPLY in isolated branch
    PASS

VERIFY
    PASS

Consumer Convention Review
    REFINE → PASS

Operational Idempotency
    PASS

INTEGRATE
    PENDING
```

---

## 4. Core Finding — Decision is not Application

```text
Adoption Decision
    ≠
Application Plan

Application Plan
    ≠
Applied Change

Applied Change
    ≠
Verified Outcome
```

A resolved Decision still requires Application Intent, current Evidence, Change Set, Preservation Scope and Verification.

---

## 5. Core Finding — Current Evidence matters

```text
Assessment Time
    T1

Application Time
    T2
```

State may change between T1 and T2.

Therefore:

> A mutating Application Plan should be validated against current consumer state before execution.

---

## 6. Core Finding — Responsibility remains semantic

```text
Responsibility
    semantic unit

Change Set
    operational unit candidate
```

Application may require several physical edits for one semantic Responsibility.

---

## 7. Core Finding — Change Set is useful

Change Set identifies:

```text
what may change
what must remain unchanged
physical targets
verification targets
```

Current status:

```text
Change Set
    operationally supported

formal representation
    not established
```

---

## 8. Core Finding — Reconciliation over Replacement

Application must preserve valid consumer implementations and make the minimum justified change.

```text
existing consumer state
    +
resolved Decision
    +
current Evidence
    +
bounded Intent
        ↓
minimum justified change
```

---

## 9. Core Finding — Preservation is broader than content

Preservation may include:

```text
language
terminology
naming
documentation style
repository-local organization
```

when those conventions are observable and compatible with the approved Intent.

---

## 10. Core Finding — Verification is multi-dimensional

```text
Physical Verification

Intent Verification

Preservation Verification

Semantic Verification
```

Therefore:

```text
file changed
    ≠
Application verified
```

---

## 11. Core Finding — Verification may trigger refinement

Observed flow:

```text
APPLY
    ↓
VERIFY
    ↓
REVIEW
    ↓
REFINE
    ↓
VERIFY AGAIN
```

A physically correct change may still not be integration-ready.

---

## 12. Core Finding — APPLY and INTEGRATE are distinct

```text
APPLY
    produce isolated candidate state

VERIFY
    inspect resulting state

INTEGRATE
    accept verified state into stable branch
```

Both experiments completed APPLY and VERIFY but not INTEGRATE.

---

## 13. Core Finding — DISCARD differs from ROLLBACK

```text
pre-integration recovery
    DISCARD

post-integration recovery
    ROLLBACK / REVERT
```

Only pre-integration discard has direct evidence so far.

---

## 14. Core Finding — Bounded idempotency is feasible

Both bounded operations produced:

```text
second equivalent application
    NO CHANGE
```

This supports idempotency for deterministic bounded changes, not universal idempotency.

---

## 15. Provisional Application Requirements

```text
AR-01
    Refresh Evidence before mutation

AR-02
    Current state overrides stale assumptions

AR-03
    Define explicit Application Intent

AR-04
    Use bounded Change Sets

AR-05
    Preserve state outside approved Change Set

AR-06
    Preserve relevant consumer conventions

AR-07
    Review before stable integration

AR-08
    Verify intended and unintended effects

AR-09
    Allow bounded refinement before integration

AR-10
    Prefer idempotent operations where practical
```

---

## 16. Evidence Confidence

| Requirement | Evidence | Confidence |
|---|---|---|
| AR-01 Evidence Refresh | 2 experiments | High |
| AR-02 Current State precedence | derived + refreshes | Medium |
| AR-03 Explicit Intent | 2 experiments | High |
| AR-04 Bounded Change Set | 2 experiments | High |
| AR-05 Preserve outside scope | 2 experiments | High |
| AR-06 Consumer conventions | 1 direct experiment | Medium |
| AR-07 Review before integration | 2 PR experiments | High |
| AR-08 Multi-dimensional VERIFY | 2 experiments | High |
| AR-09 Refinement before integration | 1 direct experiment | Medium |
| AR-10 Idempotency | 2 bounded operations | Medium |

---

## 17. Provisional Application Flow

```text
Resolved Adoption Decision
    ↓
SELECT
    ↓
REFRESH EVIDENCE
    ↓
CONFIRM DECISION STILL APPLIES
    ↓
DEFINE APPLICATION INTENT
    ↓
BUILD BOUNDED CHANGE SET
    ↓
IDENTIFY PRESERVATION SCOPE
    ↓
CHECK CONFLICTS
    ↓
REVIEW PLAN
    ↓
APPLY IN ISOLATION
    ↓
VERIFY
    ↓
REVIEW RESULT
    ↓
REFINE if necessary
    ↓
VERIFY AGAIN
    ↓
INTEGRATE
```

Possible exits:

```text
NO CHANGE
DEFER
REPLAN
REJECT
DISCARD
ROLLBACK
```

---

## 18. Supported

Direct evidence exists for:

```text
Evidence Refresh
Application Intent
bounded Change Set
scope preservation
isolated Application
physical verification
preservation verification
review before integration
MODIFY
CREATE
```

---

## 19. Provisionally Supported

```text
consumer convention preservation
review-driven refinement
operational idempotency
Application Readiness
Change Set as explicit operational concept
```

---

## 20. Conceptually Supported but Unvalidated

```text
conflict resolution
post-integration rollback
failed APPLY
failed VERIFY
concurrent modification
multi-file structural transformation
DELETE
MOVE
RENAME
```

---

## 21. Deferred

```text
CLI
GitHub Actions
automatic remediation
continuous reassessment
Structured Data
Schema
Manifest
fully autonomous application
repository generation
```

---

## 22. Application Core Candidate

```text
Evidence Refresh
    +
Application Intent
    +
Bounded Change Set
    +
Preservation Scope
    +
Human Review
    +
Isolated Application
    +
Verification
```

No automation or machine-readable contract is required for this candidate.

---

## 23. Delivery Readiness — Observed Need

Resolved Adoption Decisions do not specify enough to execute safe Application.

Result:

```text
PASS
```

---

## 24. Delivery Readiness — Repeated Evidence

Current evidence:

```text
2 mutation experiments
1 consumer
```

Result:

```text
PARTIAL PASS
```

---

## 25. Delivery Readiness — Operational Feasibility

Manual Git-native execution is feasible without specialized tooling.

Result:

```text
PASS
```

---

## 26. Delivery Readiness — Representation Stability

The representation evolved materially during the first experiments:

```text
Application Intent
Application Readiness
Change Set
Preservation Scope
INTEGRATE
DISCARD
Consumer Convention Preservation
```

Result:

```text
PARTIAL PASS
```

---

## 27. Delivery Readiness — Proportional Complexity

A human-readable, Git-reviewable model is sufficient at this stage.

Result:

```text
PASS
```

---

## 28. Initial Delivery Readiness Result

| Criterion | Result |
|---|---|
| Observed Need | PASS |
| Repeated Evidence | PARTIAL PASS |
| Operational Feasibility | PASS |
| Representation Stability | PARTIAL PASS |
| Proportional Complexity | PASS |

Therefore:

```text
Application Core Candidate
    NOT YET READY
    FOR DELIVERY SCOPE DEFINITION
```

---

## 29. Remaining Evidence Gap

```text
repeat Application Core
on an additional consumer
without material redesign
```

---

## 30. Next Experiment Objective

A second consumer should test:

```text
Evidence Refresh
Application Intent
Bounded Change Set
Preservation Scope
Consumer Conventions
Review before Integration
VERIFY
```

without intentionally expanding operation coverage.

---

## 31. Current Boundary

```text
Assessment Core
    RELEASED

Application Discovery
    ACTIVE

Application Core Candidate
    PROVISIONALLY SUPPORTED

Delivery Scope
    NOT YET READY
```

---

## 32. Synthesis Conclusion

Application is a distinct downstream capability.

Two real experiments demonstrate:

```text
ADAPT / MODIFY
    feasible

ADD / CREATE
    feasible
```

but one consumer is not enough to establish representation stability.

Therefore:

```text
APPLICATION DISCOVERY MODEL
    HOLDS

DELIVERY READINESS
    NOT YET ESTABLISHED
```

---

## 33. Recommended Next Step

Create:

```text
34_APPLICATION_REPEATABILITY_EXPERIMENT.md
```

Success condition:

```text
MODEL HOLDS
```

Failure condition:

```text
MATERIAL REDESIGN REQUIRED
```
