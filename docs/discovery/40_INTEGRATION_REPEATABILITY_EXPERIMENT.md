# 40 — Existing Repository Adoption Integration Repeatability Experiment

## 1. Purpose

Este documento prueba la repetibilidad de una representación Markdown mínima para:

```text
Existing Repository Adoption
    Integration
```

El objetivo no es ampliar capacidad.

El objetivo es comprobar si los dos experimentos reales de Integration pueden representarse mediante la misma estructura sin:

```text
new mandatory dimension
structural workaround
material redesign
```

---

## 2. Evidence Source

Primary Discovery:

```text
38_INTEGRATION_DISCOVERY.md
```

Synthesis:

```text
39_INTEGRATION_DISCOVERY_SYNTHESIS.md
```

Consumer:

```text
fran-eliot/dental-back-spring
```

---

## 3. Replay Cases

### Replay A

```text
PR #1
README-QUICK-START
ADAPT
MODIFY
direct PASS
no base drift
```

### Replay B

```text
PR #2
DOC-CHANGELOG
ADD
CREATE
REFINE → PASS
base drift present
compatible drift
```

---

## 4. Minimal Integration Record — Version 0

Candidate reusable structure:

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

This structure is intentionally:

```text
Markdown
human-readable
human-editable
Git-reviewable
```

No schema or parser is assumed.

---

## 5. Mandatory Candidate Fields

Candidate mandatory fields:

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

Conditional:

```text
Drift Impact
    when stable base changed

Integration Method
Integration Evidence
    when Integration occurs

Recovery Notes
    when verification fails
    or recovery is required
```

Provisional / contextual:

```text
Governance Constraints
Release Constraints
Repository Health Evidence
```

---

## 6. Replay A — Integration Context

```text
Consumer
    fran-eliot/dental-back-spring

Candidate
    PR #1

Responsibility
    README-QUICK-START

Adoption Decision
    ADAPT

Application Operation
    MODIFY
```

Result:

```text
REPRESENTABLE
```

---

## 7. Replay A — Candidate Reference

```text
Candidate Branch
    experiment/adoption-application-quick-start

Candidate Commit
    6706d6dd6d9c4952fe7f8192eb07922b2ac82f4f

Pull Request
    #1
```

Result:

```text
REPRESENTABLE
```

---

## 8. Replay A — Application Outcome

```text
Application Result
    APPLIED

Verification Result
    PASS

Candidate State
    VERIFIED
```

Result:

```text
REPRESENTABLE
```

---

## 9. Replay A — Stable Base Reference

```text
Stable Branch
    main

Stable Base
    e17b009602f25da0d6f32920180254eb9392fee2
```

Result:

```text
REPRESENTABLE
```

---

## 10. Replay A — Stable Base Refresh

```text
Base Drift
    NONE

Current Stable State
    identical to candidate base
```

Result:

```text
REPRESENTABLE
```

No Drift Impact section is required beyond recording:

```text
N/A
```

---

## 11. Replay A — Integration Conditions

```text
Mergeable
    YES

Reviews
    NONE

Review Threads
    NONE

Workflow Runs
    NONE

Status Checks
    NONE
```

Result:

```text
REPRESENTABLE
```

---

## 12. Replay A — Governance Constraints

Observed:

```text
No additional repository constraint
blocked Integration
```

Result:

```text
REPRESENTABLE
```

The record does not need to invent approvals or checks.

---

## 13. Replay A — Integration Review

Review confirms:

```text
candidate still verified
base current
Intent still valid
Preservation Scope still valid
candidate bounded
```

Review Result:

```text
PROCEED
```

Result:

```text
REPRESENTABLE
```

---

## 14. Replay A — Integration Decision

```text
INTEGRATE
```

Result:

```text
REPRESENTABLE
```

---

## 15. Replay A — Integration Method

```text
merge commit
```

Result:

```text
REPRESENTABLE
```

---

## 16. Replay A — Integration Evidence

```text
Merge Commit
    c61829ff27f1e6cb6fffc4210e224bd275c00139
```

Result:

```text
REPRESENTABLE
```

---

## 17. Replay A — Stable-State Verification

```text
README cd backend
    ABSENT

README localhost:3000
    ABSENT

README localhost:8080
    PRESENT

runtime server.port=8080
    PRESENT
```

Verification:

```text
Physical
    PASS

Intent
    PASS

Preservation
    PASS
```

Result:

```text
REPRESENTABLE
```

---

## 18. Replay A — Recovery Notes

```text
Recovery Required
    NO
```

Result:

```text
REPRESENTABLE
```

---

## 19. Replay A — Final Integration State

```text
INTEGRATED
```

Conclusion:

```text
REPLAY A
    PASS
```

---

## 20. Replay B — Integration Context

```text
Consumer
    fran-eliot/dental-back-spring

Candidate
    PR #2

Responsibility
    DOC-CHANGELOG

Adoption Decision
    ADD

Application Operation
    CREATE
```

Result:

```text
REPRESENTABLE
```

---

## 21. Replay B — Candidate Reference

```text
Candidate Branch
    experiment/adoption-application-changelog

Candidate Commit
    c209c82965f4510fef8a60df5210ce75c7689439

Pull Request
    #2
```

Result:

```text
REPRESENTABLE
```

---

## 22. Replay B — Application Outcome

```text
Application Result
    APPLIED

Verification History
    REFINE → PASS

Candidate State
    VERIFIED
```

Result:

```text
REPRESENTABLE
```

No new Integration-specific field is required to represent prior refinement.

---

## 23. Replay B — Stable Base Reference

Original PR base:

```text
e17b009602f25da0d6f32920180254eb9392fee2
```

Current stable branch before Integration:

```text
main
    advanced
```

Result:

```text
REPRESENTABLE
```

---

## 24. Replay B — Stable Base Refresh

Observed:

```text
Base Drift
    PRESENT

Stable Main Change
    README.md

Candidate Target
    CHANGELOG.md
```

Result:

```text
REPRESENTABLE
```

---

## 25. Replay B — Drift Impact

Evaluation:

```text
Target overlap
    NO

Application Intent invalidated
    NO

Preservation Scope invalidated
    NO

Current CHANGELOG.md
    ABSENT
```

Drift Result:

```text
COMPATIBLE
```

Result:

```text
REPRESENTABLE
```

This field is useful only when drift exists.

---

## 26. Replay B — Integration Conditions

```text
Mergeable
    YES

Reviews
    NONE

Review Threads
    NONE

Workflow Runs
    NONE

Status Checks
    NONE
```

Result:

```text
REPRESENTABLE
```

---

## 27. Replay B — Governance Constraints

Observed:

```text
Consumer language
    Spanish

Candidate language
    Spanish

No additional repository constraint
blocked Integration
```

Result:

```text
REPRESENTABLE
```

---

## 28. Replay B — Integration Review

Review confirms:

```text
candidate still verified
base drift compatible
Intent still valid
Preservation Scope valid
consumer conventions preserved
candidate bounded
```

Review Result:

```text
PROCEED
```

Result:

```text
REPRESENTABLE
```

---

## 29. Replay B — Integration Decision

```text
INTEGRATE
```

Result:

```text
REPRESENTABLE
```

---

## 30. Replay B — Integration Method

```text
merge commit
```

Result:

```text
REPRESENTABLE
```

No operation-specific method is required for CREATE.

---

## 31. Replay B — Integration Evidence

```text
Merge Commit
    ddd09369b98d11da25525ae09bfdb840c3f4ce50
```

Result:

```text
REPRESENTABLE
```

---

## 32. Replay B — Stable-State Verification

```text
CHANGELOG.md
    PRESENT

Spanish title
    PRESENT

[Sin publicar]
    PRESENT

unsupported historical releases
    ABSENT
```

Preservation of prior integrated state:

```text
README localhost:8080
    PRESENT

README localhost:3000
    ABSENT

README cd backend
    ABSENT
```

Verification:

```text
Physical
    PASS

Intent
    PASS

Preservation
    PASS
```

Result:

```text
REPRESENTABLE
```

---

## 33. Replay B — Recovery Notes

```text
Recovery Required
    NO
```

Result:

```text
REPRESENTABLE
```

---

## 34. Replay B — Final Integration State

```text
INTEGRATED
```

Conclusion:

```text
REPLAY B
    PASS
```

---

## 35. Representation Comparison

| Field | Replay A | Replay B |
| --- | :---: | :---: |
| Integration Context | PASS | PASS |
| Candidate Reference | PASS | PASS |
| Application Outcome | PASS | PASS |
| Stable Base Reference | PASS | PASS |
| Stable Base Refresh | PASS | PASS |
| Drift Impact | N/A | PASS |
| Integration Conditions | PASS | PASS |
| Governance Constraints | PASS | PASS |
| Integration Review | PASS | PASS |
| Integration Decision | PASS | PASS |
| Integration Method | PASS | PASS |
| Integration Evidence | PASS | PASS |
| Stable-State Verification | PASS | PASS |
| Recovery Notes | PASS | PASS |
| Final Integration State | PASS | PASS |
| Conclusion | PASS | PASS |

---

## 36. Structural Workaround Check

Replay A required:

```text
no extra section
no alternate structure
no hidden assumption
```

Replay B required:

```text
no extra section
no alternate structure
no operation-specific structure
```

The only conditional dimension was:

```text
Drift Impact
```

which is naturally absent when no drift exists.

Result:

```text
STRUCTURAL WORKAROUND
    NOT REQUIRED
```

---

## 37. Representation Stability

The same record represents:

```text
MODIFY
CREATE

direct PASS
REFINE → PASS

no drift
compatible drift

existing artifact mutation
new artifact creation
```

without material redesign.

Result:

```text
REPRESENTATION STABILITY
    PASS
```

---

## 38. Field Classification after Replay

### Stable Candidate Fields

```text
Integration Context
Candidate Reference
Application Outcome
Stable Base Reference
Stable Base Refresh
Integration Conditions
Integration Review
Integration Decision
Integration Method
Integration Evidence
Stable-State Verification
Final Integration State
Conclusion
```

### Conditional Candidate Fields

```text
Drift Impact
Recovery Notes
```

### Contextual / Provisional Fields

```text
Governance Constraints
Release Constraints
Repository Health Evidence
```

This classification remains a Discovery outcome, not a schema contract.

---

## 39. Recovery Representation

No recovery execution occurred.

However the record can represent:

```text
Recovery Required
    YES / NO

Recovery Notes
    descriptive
```

without prescribing:

```text
revert
rollback
reset
fix-forward
```

Therefore absence of recovery execution does not structurally block the first Integration representation.

---

## 40. Integration Decision Vocabulary after Replay

Directly evidenced:

```text
INTEGRATE
```

Representationally feasible but not executed:

```text
DEFER
REPLAN
REJECT
```

These should remain provisional until Delivery Scope decides whether they are included.

---

## 41. Final State Vocabulary after Replay

Directly evidenced:

```text
INTEGRATED
```

Representationally feasible:

```text
DEFERRED
REPLAN REQUIRED
REJECTED
RECOVERY REQUIRED
```

No evidence supports treating these as an exhaustive closed enum yet.

---

## 42. Automation Check

The representation required no:

```text
CLI
GitHub Actions
automatic merge
automatic PR creation
automatic rollback
automatic conflict resolution
```

Result:

```text
AUTOMATION REQUIRED
    NO
```

---

## 43. Structured Representation Check

The experiment required no:

```text
JSON
YAML
Schema
Manifest
parser
typed Integration Plan
```

Result:

```text
STRUCTURED REPRESENTATION REQUIRED
    NO
```

---

## 44. Delivery Readiness

| Criterion | Result |
| --- | :---: |
| Observed Need | PASS |
| Actual Integration Evidence | PASS |
| Repeated Integration Evidence | PASS |
| Cross-operation Evidence | PASS |
| Drift Handling Evidence | PASS |
| Stable-State Verification | PASS |
| Representation Stability | PASS |
| Recovery Execution Required for Initial Scope | NO |
| Proportional Complexity | PASS |

Result:

```text
Integration Core Candidate
    READY FOR DELIVERY SCOPE DEFINITION
```

---

## 45. Repeatability Result

The experiment demonstrates:

```text
one Integration representation

supports

Experiment A
    MODIFY
    no drift
    direct PASS

and

Experiment B
    CREATE
    compatible drift
    REFINE → PASS
```

without material redesign.

Therefore:

```text
INTEGRATION REPRESENTATION
    MODEL HOLDS
```

---

## 46. Supported Principles

```text
Verified Candidate before Integration

Refresh Stable Base before Integration

Evaluate Drift Impact

Consumer Governance over Framework Merge Preference

Mergeability is not Integration Readiness

Human Review before Stable Integration

Stable-State Verification after Integration

Recovery execution is separate from failure representation
```

---

## 47. Deferred Capabilities

Remain deferred:

```text
automatic merge
automatic conflict resolution
automatic rollback
release orchestration
branch protection configuration
Structured Data
Schema
Manifest
CLI
GitHub Actions
```

---

## 48. Recommended Next Step

Create:

```text
41_INTEGRATION_DELIVERY_SCOPE.md
```

The Delivery Scope should define:

```text
minimal Integration Core
supported lifecycle
required representation
stable vs provisional vocabulary
recovery boundary
consumer governance boundary
stable-state verification
explicit out-of-scope capabilities
Acceptance Criteria
```

Do not yet open:

```text
Sprint 11
milestone
target version
implementation issues
```

until Delivery Scope and Implementation Planning are complete.

---

## 49. Current State

```text
Assessment Core
    RELEASED

Application Core
    RELEASED

Integration Discovery
    COMPLETED

Integration Discovery Synthesis
    COMPLETED

Integration Repeatability
    MODEL HOLDS

Integration Core Candidate
    READY FOR DELIVERY SCOPE DEFINITION

Next Version
    NOT COMMITTED

Next Sprint
    NOT OPENED
```
