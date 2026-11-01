# 51 — Assisted Analysis Implementation Plan

## 1. Purpose

Translate the bounded Delivery Scope defined in:

```text
50_ASSISTED_ANALYSIS_DELIVERY_SCOPE.md
```

into an implementation plan for the first reusable **Existing Repository Adoption — Assisted Analysis** capability.

This plan defines:

```text
physical artifacts
implementation units
work items
verification sequence
Definition of Done
Sprint suitability
```

It does not open Sprint 12, create a milestone, create implementation Issues or select a target version.

---

## 2. Delivery Input

Implementation must remain constrained by:

```text
AC-01 through AC-73
```

from the approved Delivery Scope.

No implementation detail outside those Acceptance Criteria is committed by this plan.

---

## 3. Delivery Shape

The first delivery consists of:

```text
framework/adoption/
├── README.md
├── assessment-template.md
├── application/
│   ├── README.md
│   └── application-template.md
├── integration/
│   ├── README.md
│   └── integration-template.md
└── assisted-analysis/
    ├── README.md
    └── evidence-snapshot-template.md

docs/implementation/
└── 52_ASSISTED_ANALYSIS_CORE_VERIFICATION.md
```

---

## 4. Capability Position

Assisted Analysis is implemented as:

```text
optional evidence-support capability
```

for:

```text
Assessment
Application
Integration
```

It is not implemented as a new lifecycle stage.

---

## 5. Implementation Unit A — Assisted Analysis Guide

Primary artifact:

```text
framework/adoption/assisted-analysis/README.md
```

Purpose:

```text
explain how to collect
bounded deterministic Evidence
for later human review
```

---

## 6. Unit A — Required Guide Content

The Guide must cover:

1. purpose;
2. positioning;
3. Assessment relationship;
4. Application relationship;
5. Integration relationship;
6. Collection Sequence;
7. deterministic observation types;
8. semantic decision boundary;
9. Collection Scope;
10. Consumer Reference;
11. source traceability;
12. Collection Gaps;
13. Human Review Notes;
14. Evidence freshness;
15. read-only boundary;
16. canonical artifact boundary;
17. drift boundary;
18. governance boundary;
19. platform boundary;
20. Evidence Snapshot usage;
21. verification expectations;
22. explicit Out of Scope.

---

## 7. Unit A — Stable Principles

The Guide must preserve:

```text
Facts before Evaluation

Evidence before Decision

Read-Only before Mutation

Explicit Collection Scope

Source Traceability

Collection Gaps are Visible

Human Review owns Semantic Meaning

Representation before Tooling
```

---

## 8. Unit A — Collection Sequence

The Guide should define:

```text
DEFINE CONTEXT
    ↓
DEFINE COLLECTION SCOPE
    ↓
RECORD CONSUMER REFERENCE
    ↓
COLLECT DETERMINISTIC EVIDENCE
    ↓
RECORD SOURCES
    ↓
RECORD COLLECTION GAPS
    ↓
HUMAN REVIEW NOTES
    ↓
CONCLUDE SNAPSHOT
```

---

## 9. Unit A — Required Safety Boundaries

The Guide must explicitly state:

```text
canonical artifact absence
    ≠
Responsibility Missing
```

and:

```text
no direct path overlap
    ≠
Drift Impact COMPATIBLE
```

and:

```text
no observed reviews/checks
    ≠
Integration ready
```

---

## 10. Unit A — Read-Only Boundary

The Guide must allow only:

```text
inspect
collect
reference
compare
summarize
record
```

and exclude:

```text
create
modify
delete
move
rename
merge
revert
rollback
remediate
```

against the consumer repository.

---

## 11. Implementation Unit B — Evidence Snapshot Template

Primary artifact:

```text
framework/adoption/assisted-analysis/evidence-snapshot-template.md
```

Purpose:

> Provide one reusable Structured Markdown representation for deterministic Evidence across Assessment, Application and Integration.

---

## 12. Unit B — Template Sections

The Template must contain the stable structure:

```text
1. Evidence Context
2. Consumer Reference
3. Collection Scope
4. Repository Structure Evidence
5. Artifact Evidence
6. Git Reference Evidence
7. Release Evidence
8. Pull Request Evidence
9. Workflow / Status Evidence
10. Comparison Evidence
11. Governance Evidence
12. Collection Gaps
13. Human Review Notes
14. Conclusion
```

---

## 13. Unit B — Mandatory Information

The Template must make clear that every completed snapshot identifies:

```text
Evidence Context
Consumer Repository
Consumer Reference
Collection Scope
Observed Facts
Evidence Sources
Collection Gaps
Conclusion
```

---

## 14. Unit B — Conditional Information

The Template must support conditional use of:

```text
Repository Structure Evidence
Git Reference Evidence
Release Evidence
Pull Request Evidence
Workflow Evidence
Status Evidence
Review Evidence
Comparison Evidence
Branch Governance Evidence
```

---

## 15. Unit B — Gap Vocabulary

The Template must support exactly the stable gap vocabulary:

```text
NOT CHECKED
NOT ACCESSIBLE
NOT APPLICABLE
UNKNOWN
REQUIRES SEMANTIC REVIEW
```

No additional stable gap value should be introduced without explicit scope review.

---

## 16. Unit B — Negative Evidence

The Template must distinguish:

```text
ABSENT
```

from:

```text
NOT CHECKED
NOT ACCESSIBLE
UNKNOWN
```

to prevent false absence claims.

---

## 17. Unit B — Evidence Source Traceability

Each material observation must be able to point to a source such as:

```text
repository path
file SHA
branch
commit SHA
tag
GitHub Release
Pull Request
workflow run
commit status
comparison
repository metadata
```

---

## 18. Unit B — Semantic Field Exclusions

The Template must not define authoritative fields for:

```text
Responsibility State
Applicability
Adoption Decision
Application Result
Drift Impact
Integration Review
Integration Decision
Final Integration State
```

Human Review Notes may mention related questions but must remain separate from deterministic facts.

---

## 19. Implementation Unit C — Root Adoption Integration

Artifact:

```text
framework/adoption/README.md
```

Required change:

```text
minimal integration only
```

The root document should explain Assisted Analysis as optional evidence support without restructuring:

```text
Assessment
    ↓
optional Application
    ↓
optional Integration
```

---

## 20. Unit C — Root Integration Model

Recommended conceptual representation:

```text
                    Assisted Analysis
                    ┌──────┼──────┐
                    ↓      ↓      ↓
Assessment Core  Application Core  Integration Core
```

The exact visual representation may vary if semantics remain equivalent.

---

## 21. Unit C — Backward Compatibility

Root integration must not change existing stable semantics of:

```text
Assessment Core
Application Core
Integration Core
```

Existing manual usage remains valid without Assisted Analysis.

---

## 22. Implementation Unit D — Verification

Primary artifact:

```text
docs/implementation/52_ASSISTED_ANALYSIS_CORE_VERIFICATION.md
```

Purpose:

```text
verify AC-01 through AC-73
verify replay compatibility
verify scope preservation
verify backward compatibility
```

---

## 23. Unit D — Structural Verification

Verify:

```text
Guide exists
Template exists
root Adoption integration exists
verification document exists
expected paths are correct
no unrelated implementation artifact added
```

---

## 24. Unit D — Guide Verification

Verify the Guide covers:

```text
purpose
positioning
collection sequence
deterministic boundary
semantic boundary
read-only boundary
source traceability
collection gaps
evidence freshness
platform boundary
out-of-scope automation
```

---

## 25. Unit D — Template Verification

Verify:

```text
14 stable sections
mandatory information
conditional information
gap vocabulary
negative Evidence distinction
source traceability
Human Review Notes separation
Conclusion
```

---

## 26. Unit D — Semantic Safety Verification

Verify the delivered representation does not define authoritative fields for:

```text
Responsibility State
Applicability
Adoption Decision
Application Result
Drift Impact
Integration Review
Integration Decision
Final Integration State
```

---

## 27. Unit D — Scope Preservation Verification

Verify absence of:

```text
CLI
GitHub Actions
Schema
Manifest
JSON/YAML Evidence contract
automatic decisions
consumer mutation
automatic PR creation
automatic merge
automatic rollback
automatic recovery
Componentization
Framework Validator extension
```

---

## 28. Unit D — Replay A

Replay:

```text
Assessment
fran-eliot/only_film
```

Expected:

```text
PASS
```

The delivered Guide and Template must represent the deterministic Evidence from Experiment A without material workaround.

---

## 29. Unit D — Replay B

Replay:

```text
Application
fran-eliot/aula-robotica-platform
```

Expected:

```text
PASS
```

The representation must support Evidence Refresh without encoding Application Result.

---

## 30. Unit D — Replay C

Replay:

```text
Integration
fran-eliot/dental-back-spring
```

Expected:

```text
PASS
```

The representation must support Stable Base Refresh Evidence without encoding Drift Impact or Integration Decision.

---

## 31. Unit D — Acceptance Criteria Verification

The verification artifact must explicitly cover:

```text
AC-01
    through
AC-73
```

Expected:

```text
73 PASS
```

No Acceptance Criterion may be omitted, duplicated or silently reinterpreted.

---

## 32. Unit D — Final Verification Verdict

Expected final state:

```text
Existing Repository Adoption
    Assisted Analysis Core

IMPLEMENTATION VERIFIED
```

Only after all required checks pass.

---

## 33. Implementation Work Item 1

Title candidate:

```text
Implement Existing Repository Adoption Assisted Analysis Guide
```

Primary artifact:

```text
framework/adoption/assisted-analysis/README.md
```

Scope:

```text
Unit A
```

---

## 34. Work Item 1 — Done When

Done when:

- Guide exists at the expected path;
- collection sequence is documented;
- Facts/Evaluation boundary is explicit;
- Evidence/Decision boundary is explicit;
- read-only boundary is explicit;
- Collection Scope is documented;
- source traceability is documented;
- Collection Gaps are documented;
- Evidence freshness is documented;
- Assessment/Application/Integration usage is documented;
- canonical artifact and drift boundaries are explicit;
- out-of-scope tooling and automation remain excluded.

---

## 35. Implementation Work Item 2

Title candidate:

```text
Implement Existing Repository Adoption Evidence Snapshot Template
```

Primary artifact:

```text
framework/adoption/assisted-analysis/evidence-snapshot-template.md
```

Scope:

```text
Unit B
```

---

## 36. Work Item 2 — Done When

Done when:

- 14 stable sections are represented;
- mandatory fields are clear;
- conditional sections are clear;
- gap vocabulary is represented;
- ABSENT differs from collection gaps;
- source traceability is supported;
- semantic decision fields remain absent;
- Template is human-readable and Git-reviewable;
- Template can represent all three historical replays.

---

## 37. Implementation Work Item 3

Title candidate:

```text
Validate and integrate Existing Repository Adoption Assisted Analysis Core
```

Artifacts:

```text
framework/adoption/README.md

docs/implementation/52_ASSISTED_ANALYSIS_CORE_VERIFICATION.md
```

Scope:

```text
Unit C
+
Unit D
```

---

## 38. Work Item 3 — Done When

Done when:

- root Adoption guide integrates Assisted Analysis;
- Assessment/Application/Integration semantics remain unchanged;
- replay A passes;
- replay B passes;
- replay C passes;
- AC-01 through AC-73 pass;
- out-of-scope checks pass;
- final verification verdict is IMPLEMENTATION VERIFIED.

---

## 39. Dependency Model

Recommended dependency:

```text
Guide ───────────────┐
                     ├──► Verification & Integration
Template ────────────┘
```

Guide and Template may be implemented independently but both must be complete before final verification.

---

## 40. Suggested Execution Sequence

```text
1. Assisted Analysis Guide
2. Evidence Snapshot Template
3. Root Adoption Integration
4. Verification Replay A
5. Verification Replay B
6. Verification Replay C
7. AC-01 through AC-73 audit
8. Scope audit
9. Final verification verdict
```

---

## 41. Commit Boundary Guidance

Prefer commits aligned to implementation units.

Candidate commit sequence:

```text
docs(adoption): add assisted analysis guide

docs(adoption): add evidence snapshot template

docs(adoption): integrate assisted analysis capability

docs(implementation): verify assisted analysis core
```

Exact commit count is not a Delivery requirement.

---

## 42. Branching Boundary

Implementation should begin from the latest stable `main`.

Recommended branch pattern:

```text
feature/assisted-analysis-guide

feature/assisted-analysis-template

feature/assisted-analysis-core-verification
```

A different branch organization is acceptable if scope isolation remains clear.

---

## 43. Review Boundary

Before merging each implementation work item, review:

```text
scope
terminology
backward compatibility
out-of-scope leakage
unrelated changes
```

Final verification must not compensate for unresolved scope drift in earlier work items.

---

## 44. Testing Model

This delivery does not require executable tests.

Verification consists of:

```text
document structure checks
terminology checks
Acceptance Criteria audit
representative replay
scope audit
backward compatibility review
```

---

## 45. Replay Test Principle

The three replays validate that the delivered representation supports:

```text
Assessment
Application
Integration
```

without lifecycle-specific redesign.

They are representation tests, not consumer mutation tests.

---

## 46. Scope Audit

Final scope audit must confirm:

```text
no CLI
no GitHub Actions
no scanner executable
no Schema
no Manifest
no JSON/YAML Evidence contract
no decision automation
no mutation
no automatic merge
no automatic rollback
no Componentization
no Validator extension
```

---

## 47. Backward Compatibility Audit

Confirm:

```text
Assessment manual flow
    remains valid

Application manual flow
    remains valid

Integration manual flow
    remains valid
```

Assisted Analysis remains optional.

---

## 48. Definition of Done — Core Artifacts

Core artifacts exist:

```text
framework/adoption/assisted-analysis/README.md

framework/adoption/assisted-analysis/evidence-snapshot-template.md
```

---

## 49. Definition of Done — Root Integration

```text
framework/adoption/README.md
```

references Assisted Analysis correctly as optional evidence support.

---

## 50. Definition of Done — Verification

```text
docs/implementation/52_ASSISTED_ANALYSIS_CORE_VERIFICATION.md
```

exists and records:

```text
Replay A
    PASS

Replay B
    PASS

Replay C
    PASS

AC-01 through AC-73
    PASS
```

---

## 51. Definition of Done — Semantic Safety

No delivered artifact promotes deterministic Evidence into semantic decision authority.

---

## 52. Definition of Done — Scope Safety

No out-of-scope tooling, automation, mutation or Componentization is introduced.

---

## 53. Definition of Done — Backward Compatibility

Assessment, Application and Integration remain semantically backward compatible.

---

## 54. Definition of Done — Final State

The increment may be considered implementation-complete only when:

```text
Guide
    IMPLEMENTED

Template
    IMPLEMENTED

Root Adoption Integration
    IMPLEMENTED

Replay A
    PASS

Replay B
    PASS

Replay C
    PASS

AC-01 through AC-73
    PASS

Assisted Analysis Core
    IMPLEMENTATION VERIFIED
```

---

## 55. Sprint Suitability

The planned work contains:

```text
3 bounded work items
4 physical artifacts touched/created
73 explicit Acceptance Criteria
3 replay scenarios
no executable tooling
no consumer mutation
```

The work is cohesive and independently verifiable.

Result:

```text
SINGLE SPRINT SUITABILITY
    PASS
```

---

## 56. Release Increment Suitability

The capability is:

```text
new
reusable
cross-lifecycle
backward compatible
bounded
```

Therefore it is suitable for a new minor pre-1.0 increment rather than a patch.

This plan does not select the version number.

---

## 57. Remaining Governance Decision

After this plan is reviewed and merged, governance may decide whether to:

```text
open Sprint 12
create implementation Issues
create milestone
select next target version
```

That decision should use:

```text
Delivery Scope
Implementation Plan
current Roadmap
versioning strategy
remaining v1.0 readiness
```

---

## 58. Candidate Sprint Objective

If governance commits the work, a suitable Sprint objective is:

```text
Deliver the first reusable Assisted Analysis Core
for Existing Repository Adoption.
```

This wording is provisional until Sprint opening.

---

## 59. Candidate Issue Set

If governance commits the work, create three implementation Issues:

```text
1. Implement Existing Repository Adoption Assisted Analysis Guide

2. Implement Existing Repository Adoption Evidence Snapshot Template

3. Validate and integrate Existing Repository Adoption Assisted Analysis Core
```

No Issues should be created before the increment is formally committed.

---

## 60. Candidate Milestone

A milestone may be created only after target-version selection.

This plan intentionally leaves:

```text
Milestone
    UNDEFINED
```

---

## 61. Candidate Target Version

This plan intentionally leaves:

```text
Target Version
    UNDEFINED
```

Do not infer automatically:

```text
v1.0.0
```

or:

```text
v0.10.0
```

from the existence of this Implementation Plan alone.

---

## 62. Implementation Readiness

Evidence:

```text
Operational Need
    PASS

Discovery
    PASS

Repeatability
    PASS

Delivery Scope
    PASS

Acceptance Criteria
    PASS

Implementation Decomposition
    PASS

Verification Strategy
    PASS

Sprint Suitability
    PASS
```

Result:

```text
ASSISTED ANALYSIS CORE
    IMPLEMENTATION READY
```

---

## 63. What Implementation Ready Means

It means governance has enough evidence to make a release-planning decision.

It does not mean implementation has already been committed.

---

## 64. Recommended Next Step

After this document is merged:

```text
evaluate next increment
    ↓
select target version if justified
    ↓
open Sprint 12 if justified
    ↓
create milestone
    ↓
create three implementation Issues
    ↓
sync governance
```

Do not implement before that governance step.

---

## 65. Current State

```text
v0.9.0
    RELEASED

Assisted Analysis Discovery
    COMPLETED

Assisted Analysis Repeatability
    MODEL HOLDS

Assisted Analysis Delivery Scope
    DEFINED

Assisted Analysis Implementation Plan
    DEFINED

Assisted Analysis Core
    IMPLEMENTATION READY

Implementation
    NOT COMMITTED

Sprint 12
    NOT OPENED

Milestone
    NONE

Target Version
    NONE
```
