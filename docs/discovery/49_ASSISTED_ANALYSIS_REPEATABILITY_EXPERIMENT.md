# 49 — Assisted Analysis Repeatability Experiment

## 1. Purpose

Validate whether a single minimal Assisted Analysis representation can support deterministic Evidence collection across:

```text
Assessment
Application
Integration
```

without introducing:

```text
new mandatory dimensions
semantic leakage
consumer-specific structural workarounds
tooling dependency
material redesign
```

This experiment validates representation stability.

It does not validate production tooling.

---

## 2. Starting Point

Discovery Synthesis identified the provisional minimal representation candidate:

```text
Assisted Analysis Guide
    +
Structured Markdown Evidence Snapshot
```

Operational need is already confirmed.

What remains unvalidated is:

```text
representation repeatability
```

---

## 3. Success Condition

Success result:

```text
MODEL HOLDS
```

when one representation supports all three replay cases without material redesign.

---

## 4. Failure Condition

Failure result:

```text
MATERIAL REDESIGN REQUIRED
```

if any lifecycle stage forces:

- a new mandatory conceptual dimension;
- semantic decisions into deterministic fields;
- a consumer-specific structural branch;
- mandatory tooling;
- a fundamentally different snapshot format.

---

## 5. Experiment Boundary

The experiment does not introduce:

```text
CLI
GitHub Actions
Schema
Manifest
JSON contract
YAML contract
database
automatic Assessment
automatic Application
automatic Integration
mutation
continuous reassessment
```

---

## 6. Minimal Evidence Collection Guide — Version 0

The Guide has one purpose:

> Collect bounded, deterministic, source-traceable repository Evidence for later human review.

Stable principles:

```text
Facts before Evaluation
Evidence before Decision
Read-Only before Mutation
Explicit Scope
Source Traceability
Collection Gaps are Visible
Human Review owns Semantic Meaning
```

---

## 7. Guide — Collection Sequence

Use:

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

## 8. Guide — Allowed Observation Types

Examples:

```text
file exists
file absent
directory exists
literal exists
configuration key exists
branch exists
commit reference exists
tag exists
release exists
Pull Request state
review count
workflow run presence
status presence
changed-file list
base/head comparison
branch protection flag
```

---

## 9. Guide — Forbidden Automatic Conclusions

Do not automatically derive:

```text
Responsibility State
Applicability
semantic equivalence
Adoption Decision
Application Intent
Application Result
Drift Impact
Integration Review
Integration Decision
Final Integration State
```

---

## 10. Evidence Snapshot — Version 0

The candidate structure is:

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

## 11. Mandatory vs Conditional Sections

Mandatory:

```text
Evidence Context
Consumer Reference
Collection Scope
Artifact / Observation Evidence
Evidence Sources
Collection Gaps
Conclusion
```

Conditionally populated:

```text
Repository Structure Evidence
Git Reference Evidence
Release Evidence
Pull Request Evidence
Workflow / Status Evidence
Comparison Evidence
Governance Evidence
```

Human Review Notes are optional but structurally available.

---

## 12. Collection Gap Vocabulary

Allowed gap states:

```text
NOT CHECKED
NOT ACCESSIBLE
NOT APPLICABLE
UNKNOWN
REQUIRES SEMANTIC REVIEW
```

These states prevent silent inference.

---

## 13. Replay A — Assessment Case

Consumer:

```text
fran-eliot/only_film
```

Reference:

```text
main
28d75a50e0a178954dd46acc23300d9dd327843c
```

Purpose:

```text
Assessment Evidence Collection
```

---

## 14. Replay A — Evidence Context

```text
Lifecycle Stage
    Assessment

Evidence Purpose
    collect repository facts
    support later Responsibility evaluation

Mutation
    NONE
```

Result:

```text
REPRESENTABLE
```

---

## 15. Replay A — Collection Scope

```text
root repository structure
documentation artifacts
build/runtime artifacts
GitHub automation artifacts
release evidence
stable reference
branch governance evidence
```

Result:

```text
REPRESENTABLE
```

---

## 16. Replay A — Artifact Evidence

Observed:

```text
README.md
    PRESENT

CHANGELOG.md
    ABSENT

pom.xml
    PRESENT

application.properties
    PRESENT

application.yml
    ABSENT

docs/
    PRESENT
```

Result:

```text
REPRESENTABLE
```

---

## 17. Replay A — Git / Release / Automation Evidence

Observed:

```text
Git tags
    0

GitHub Releases
    0

GitHub workflows
    7

Dependabot configuration
    PRESENT
```

Result:

```text
REPRESENTABLE
```

---

## 18. Replay A — Governance Evidence

Observed:

```text
main protected
    false

required status contexts
    none
```

Result:

```text
REPRESENTABLE
```

---

## 19. Replay A — Human Review Notes

Required semantic caution:

```text
root CHANGELOG.md absent
    ≠
DOC-CHANGELOG Responsibility Missing
```

The deterministic snapshot does not assign State.

Result:

```text
SEMANTIC BOUNDARY
    PRESERVED
```

---

## 20. Replay A — Conclusion

```text
Snapshot Complete
    YES

Deterministic Evidence
    REPRESENTED

Semantic Decision
    NOT INCLUDED
```

Replay A result:

```text
PASS
```

---

## 21. Replay B — Application Case

Consumer:

```text
fran-eliot/aula-robotica-platform
```

Reference:

```text
main
92db31aabe0d9ea2ec53974b802d617ca9a250fe
```

Purpose:

```text
Application Evidence Refresh
```

---

## 22. Replay B — Evidence Context

```text
Lifecycle Stage
    Application

Responsibility
    DOC-CHANGELOG

Historical Adoption Decision
    ADAPT

Evidence Purpose
    refresh current consumer state before mutation
```

Historical decision is context, not an output of Assisted Analysis.

Result:

```text
REPRESENTABLE
```

---

## 23. Replay B — Artifact Evidence

Observed:

```text
root CHANGELOG.md
    ABSENT

docs/14_STATUS/55_CHANGELOG.md
    PRESENT

existing changelog SHA
    35b048a59ed741d9f777bc7f2927b71c3befe384
```

Literal signals observed:

```text
Unreleased
Semantic Versioning
release
version
publication/date semantics
```

Result:

```text
REPRESENTABLE
```

---

## 24. Replay B — Release Evidence

Observed:

```text
Git tags
    0

GitHub Releases
    0

README semantic-version claim
    NOT OBSERVED
```

Result:

```text
REPRESENTABLE
```

---

## 25. Replay B — Collection Gaps

Deterministic collection cannot conclude:

```text
Changelog Governance
    STRONG

State
    Partial

Application Readiness
    NOT READY

Application Result
    NO CHANGE
```

Gap classification:

```text
REQUIRES SEMANTIC REVIEW
```

Result:

```text
REPRESENTABLE
```

---

## 26. Replay B — Human Review Notes

Human reviewer may use the snapshot to decide whether:

```text
Partial remains valid
release history is sufficient
mutation is justified
NO CHANGE is appropriate
REPLAN is appropriate
```

Those outcomes remain outside deterministic fields.

Result:

```text
SEMANTIC BOUNDARY
    PRESERVED
```

---

## 27. Replay B — Conclusion

```text
Snapshot Complete
    YES

Evidence Refresh
    REPRESENTED

Application Decision
    NOT INCLUDED
```

Replay B result:

```text
PASS
```

---

## 28. Replay C — Integration Case

Consumer:

```text
fran-eliot/dental-back-spring
```

Purpose:

```text
Integration Stable Base Refresh
```

Candidate:

```text
PR #2
DOC-CHANGELOG
CREATE
```

---

## 29. Replay C — Consumer Reference

Original stable base:

```text
e17b009602f25da0d6f32920180254eb9392fee2
```

Refreshed stable base:

```text
c61829ff27f1e6cb6fffc4210e224bd275c00139
```

Candidate head:

```text
c209c82965f4510fef8a60df5210ce75c7689439
```

Result:

```text
REPRESENTABLE
```

---

## 30. Replay C — Comparison Evidence

Stable base advancement:

```text
ahead by
    2 commits

stable changed file
    README.md
```

Candidate changed file:

```text
CHANGELOG.md
```

Direct path overlap:

```text
NONE
```

Result:

```text
REPRESENTABLE
```

---

## 31. Replay C — Pull Request / Workflow / Status Evidence

Observed:

```text
PR #2
    merged historically

reviews
    0

workflow runs
    0

commit statuses
    0
```

Result:

```text
REPRESENTABLE
```

---

## 32. Replay C — Governance Evidence

Observed:

```text
main protected
    false

branch protection enabled
    false

required status contexts
    none
```

Result:

```text
REPRESENTABLE
```

---

## 33. Replay C — Collection Gaps

Deterministic collection cannot conclude:

```text
Drift Impact
    COMPATIBLE

Integration Review
    PROCEED

Integration Decision
    INTEGRATE
```

Gap classification:

```text
REQUIRES SEMANTIC REVIEW
```

Result:

```text
REPRESENTABLE
```

---

## 34. Replay C — Human Review Notes

Important semantic caution:

```text
no direct file overlap
    ≠
Drift Impact COMPATIBLE
```

Result:

```text
SEMANTIC BOUNDARY
    PRESERVED
```

---

## 35. Replay C — Conclusion

```text
Snapshot Complete
    YES

Stable Base Refresh Evidence
    REPRESENTED

Integration Decision
    NOT INCLUDED
```

Replay C result:

```text
PASS
```

---

## 36. Cross-Replay Structural Comparison

| Section | Assessment | Application | Integration |
| --- | :---: | :---: | :---: |
| Evidence Context | Used | Used | Used |
| Consumer Reference | Used | Used | Used |
| Collection Scope | Used | Used | Used |
| Repository Structure Evidence | Used | Contextual | Contextual |
| Artifact Evidence | Used | Used | Used |
| Git Reference Evidence | Used | Used | Used |
| Release Evidence | Used | Used | Contextual |
| Pull Request Evidence | N/A | N/A | Used |
| Workflow / Status Evidence | Used | Contextual | Used |
| Comparison Evidence | N/A | N/A | Used |
| Governance Evidence | Used | Contextual | Used |
| Collection Gaps | Used | Used | Used |
| Human Review Notes | Used | Used | Used |
| Conclusion | Used | Used | Used |

No lifecycle stage required a new structural section.

---

## 37. Mandatory Field Stability

Across all replays, the following remained stable:

```text
Evidence Context
Consumer Reference
Collection Scope
Observed Facts
Evidence Sources
Collection Gaps
Conclusion
```

Result:

```text
MANDATORY FIELD STABILITY
    PASS
```

---

## 38. Conditional Field Stability

Conditional evidence sections allowed lifecycle-specific data without structural redesign.

Examples:

```text
Release Evidence
    used strongly in Application

Pull Request Evidence
    used strongly in Integration

Repository Structure Evidence
    used strongly in Assessment
```

Result:

```text
CONDITIONAL FIELD MODEL
    PASS
```

---

## 39. Source Traceability

All replay observations can point to source types such as:

```text
repository path
file SHA
branch
commit SHA
GitHub Release query
tag query
Pull Request
comparison
workflow runs
statuses
repository metadata
```

Result:

```text
SOURCE TRACEABILITY
    PASS
```

---

## 40. Collection Gaps Stability

All three replays require explicit gaps.

The vocabulary:

```text
NOT CHECKED
NOT ACCESSIBLE
NOT APPLICABLE
UNKNOWN
REQUIRES SEMANTIC REVIEW
```

is sufficient for the observed cases.

Result:

```text
COLLECTION GAP MODEL
    PASS
```

---

## 41. Semantic Leakage Check

No replay required deterministic fields for:

```text
Responsibility State
Adoption Decision
Application Result
Drift Impact
Integration Review
Integration Decision
```

Result:

```text
SEMANTIC LEAKAGE
    NONE REQUIRED
```

---

## 42. Consumer-Specific Workaround Check

Consumers differ substantially:

```text
only_film
    Java / Spring Boot

aula-robotica-platform
    Python / FastAPI

dental-back-spring
    Java / Spring Boot
```

and lifecycle needs differ.

Yet no consumer-specific structural branch was required.

Result:

```text
CONSUMER-SPECIFIC STRUCTURAL WORKAROUND
    NO
```

---

## 43. Tooling Dependency Check

The representation can be completed without:

```text
CLI
GitHub Action
parser
schema
database
generated report
```

Result:

```text
TOOLING DEPENDENCY
    NO
```

---

## 44. Verbosity and Review Friction

Observed risk:

```text
Evidence Snapshot
    can become verbose
```

Mitigation:

```text
bounded Collection Scope
conditional sections
concise factual observations
explicit gaps
no duplicated semantic conclusions
```

This is a representation refinement, not a structural failure.

---

## 45. Proportional Complexity Check

The Guide + Snapshot pair provides:

```text
standardization
traceability
cross-lifecycle reuse
human review support
```

without requiring production tooling.

Result:

```text
PROPORTIONAL COMPLEXITY
    PASS
```

---

## 46. Requirement Candidate Status after Repeatability

| Requirement | Status |
| --- | :---: |
| RC-AA01 — facts distinct from evaluation | SUPPORTED |
| RC-AA02 — source traceability | SUPPORTED |
| RC-AA03 — bounded scanning | SUPPORTED |
| RC-AA04 — deterministic semantics | SUPPORTED |
| RC-AA05 — human review mandatory | SUPPORTED |
| RC-AA06 — non-canonical implementations discoverable | SUPPORTED |
| RC-AA07 — Assessment decisions human-owned | SUPPORTED |
| RC-AA08 — Application decisions human-owned | SUPPORTED |
| RC-AA09 — Integration decisions human-owned | SUPPORTED |
| RC-AA10 — read-only operation | SUPPORTED |
| RC-AA11 — cross-stage reuse | SUPPORTED |
| RC-AA12 — proportional tooling complexity | SUPPORTED |

All initial Requirement Candidates now have supporting evidence.

---

## 47. Representation Stability Result

The same minimal structure supports:

```text
Assessment Replay
    PASS

Application Replay
    PASS

Integration Replay
    PASS
```

without:

```text
new mandatory dimension
material redesign
semantic leakage
tooling dependency
consumer-specific structural workaround
```

Therefore:

```text
ASSISTED ANALYSIS REPRESENTATION
    MODEL HOLDS
```

---

## 48. What MODEL HOLDS Means

It means:

```text
Assisted Analysis Guide
    +
Structured Markdown Evidence Snapshot
```

are sufficiently stable to continue Discovery toward a bounded Delivery Scope.

It does not mean:

```text
implementation approved
CLI approved
scanner approved
automation approved
target version selected
Sprint opened
```

---

## 49. Delivery Readiness

Criteria:

| Criterion | Result |
| --- | :---: |
| Operational Need | PASS |
| Repeated Deterministic Work | PASS |
| Cross-Lifecycle Reuse | PASS |
| Human Semantic Boundary | PASS |
| Read-Only Boundary | PASS |
| Source Traceability | PASS |
| Collection Gap Representation | PASS |
| Representation Stability | PASS |
| Proportional Complexity | PASS |
| Structured Representation Required | NO |
| Production Tooling Required | NO |

Result:

```text
Assisted Analysis Candidate
    READY FOR DELIVERY SCOPE DEFINITION
```

---

## 50. Recommended Next Step

Create:

```text
50_ASSISTED_ANALYSIS_DELIVERY_SCOPE.md
```

The Delivery Scope should define:

```text
minimal reusable capability
Guide scope
Evidence Snapshot scope
stable evidence categories
collection boundaries
human review boundaries
read-only boundary
explicit out-of-scope automation
Acceptance Criteria
```

Do not yet open:

```text
Sprint 12
milestone
target version
implementation Issues
```

until Delivery Scope and Implementation Planning are complete.

---

## 51. Current State

```text
v0.9.0
    RELEASED

Assisted Analysis Discovery
    COMPLETED THROUGH REPEATABILITY

Operational Need
    CONFIRMED

Representation
    MODEL HOLDS

Assisted Analysis Candidate
    READY FOR DELIVERY SCOPE DEFINITION

Delivery Scope
    NEXT

Implementation
    NOT COMMITTED

Sprint 12
    NOT OPENED

Target Version
    NONE
```
