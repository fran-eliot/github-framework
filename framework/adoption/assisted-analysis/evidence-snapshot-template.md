# Existing Repository Adoption — Evidence Snapshot Template

Este Template proporciona una representación reusable de **Structured Markdown** para registrar Evidence determinista y source-traceable durante Existing Repository Adoption.

Puede utilizarse para:

```text
Assessment Evidence
Application Evidence Refresh
Integration Stable Base Refresh Evidence
```

sin convertir la recopilación de Evidence en evaluación semántica ni decisión automática.

---

## 1. Evidence Context

### Lifecycle Stage

```text
Assessment / Application / Integration
```

### Evidence Purpose

```text
Describe why this Evidence is being collected.
```

### Collection Moment / Context

```text
Describe when or under which review context the snapshot was collected.
```

### Mutation

```text
NONE
```

Assisted Analysis is read-only.

---

## 2. Consumer Reference

### Consumer Repository

```text
owner/repository
```

### Repository Platform

```text
GitHub / other / unknown
```

### Primary Reference

```text
branch / tag / commit / Pull Request / candidate reference
```

### Commit SHA

```text
<sha or NOT APPLICABLE / UNKNOWN>
```

### Additional References

```text
stable SHA
candidate SHA
base SHA
head SHA
tag
release
Pull Request
```

Record only references relevant to Collection Scope.

---

## 3. Collection Scope

### Declared Scope

```text
repository baseline
selected Responsibility
selected artifact set
Application Evidence Refresh
Integration stable-base comparison
Integration condition review
other bounded scope
```

### Included Sources

```text
List source types or paths included in this collection.
```

### Excluded Sources

```text
List deliberately excluded sources, or NOT APPLICABLE.
```

### Completeness Statement

```text
Collection is complete for the declared scope only.
```

Do not interpret scoped completeness as exhaustive repository understanding.

---

## 4. Repository Structure Evidence

Use when repository structure is relevant.

### Observations

| Observation | Result | Evidence Source |
| --- | --- | --- |
| Root entries |  |  |
| Known directories |  |  |
| Known files |  |  |
| Relevant artifact paths |  |  |

### Section State

```text
USED / NOT APPLICABLE / NOT CHECKED / NOT ACCESSIBLE
```

---

## 5. Artifact Evidence

Record deterministic artifact observations.

| Artifact / Path | Observation | Evidence Source | Notes |
| --- | --- | --- | --- |
|  | PRESENT / ABSENT / UNKNOWN |  |  |
|  | PRESENT / ABSENT / UNKNOWN |  |  |

Possible observation types include:

```text
PRESENT
ABSENT
literal exists
literal absent
configuration key exists
configuration key absent
file SHA observed
```

### Semantic Boundary

```text
artifact present
    ≠
Responsibility Satisfied

canonical artifact absent
    ≠
Responsibility Missing
```

---

## 6. Git Reference Evidence

Use when Git references are relevant.

| Reference Type | Value | Evidence Source |
| --- | --- | --- |
| Default branch |  |  |
| Current branch |  |  |
| Commit SHA |  |  |
| Base SHA |  |  |
| Head SHA |  |  |
| Merge commit |  |  |
| Tag |  |  |

### Section State

```text
USED / NOT APPLICABLE / NOT CHECKED / NOT ACCESSIBLE
```

---

## 7. Release Evidence

Use when release information is relevant.

| Observation | Result | Evidence Source |
| --- | --- | --- |
| Git tags |  |  |
| Published releases |  |  |
| Release target |  |  |
| Published date |  |  |

### Notes

```text
Record observed release facts only.
Do not infer release governance quality from presence or absence alone.
```

### Section State

```text
USED / NOT APPLICABLE / NOT CHECKED / NOT ACCESSIBLE
```

---

## 8. Pull Request Evidence

Use when a Pull Request is part of Collection Scope.

| Observation | Result | Evidence Source |
| --- | --- | --- |
| PR number |  |  |
| State |  |  |
| Base ref / SHA |  |  |
| Head ref / SHA |  |  |
| Mergeability |  |  |
| Merged |  |  |
| Merge commit |  |  |
| Requested reviewers |  |  |
| Reviews |  |  |

### Section State

```text
USED / NOT APPLICABLE / NOT CHECKED / NOT ACCESSIBLE
```

---

## 9. Workflow / Status Evidence

### Workflow Evidence

| Observation | Result | Evidence Source |
| --- | --- | --- |
| Workflow definitions present |  |  |
| Workflow runs present |  |  |
| Relevant run state |  |  |
| Relevant run conclusion |  |  |

### Commit Status Evidence

| Observation | Result | Evidence Source |
| --- | --- | --- |
| Status contexts present |  |  |
| Combined status |  |  |
| Checks present |  |  |

### Governance Caution

```text
no observed workflow runs
    ≠
Integration ready

no observed statuses
    ≠
approval granted
```

### Section State

```text
USED / NOT APPLICABLE / NOT CHECKED / NOT ACCESSIBLE
```

---

## 10. Comparison Evidence

Use when comparing two repository states.

### Comparison Context

```text
Base:
Head:
Purpose:
```

### Comparison Result

| Observation | Result | Evidence Source |
| --- | --- | --- |
| Ahead count |  |  |
| Behind count |  |  |
| Changed files |  |  |
| Additions |  |  |
| Deletions |  |  |
| Direct path overlap |  |  |

### Drift Boundary

```text
no direct path overlap
    ≠
Drift Impact COMPATIBLE
```

Comparison Evidence supports human Drift Impact evaluation.

It does not perform it.

### Section State

```text
USED / NOT APPLICABLE / NOT CHECKED / NOT ACCESSIBLE
```

---

## 11. Governance Evidence

Use when repository governance is relevant.

| Observation | Result | Evidence Source |
| --- | --- | --- |
| Branch protected |  |  |
| Required status contexts |  |  |
| Review requirements |  |  |
| Repository rules observed |  |  |
| Merge restrictions observed |  |  |

### Governance Boundary

Observed controls do not automatically determine:

```text
governance satisfied
approval granted
Integration ready
```

Contextual human review remains required.

### Section State

```text
USED / NOT APPLICABLE / NOT CHECKED / NOT ACCESSIBLE
```

---

## 12. Collection Gaps

Record every material gap explicitly.

Stable vocabulary:

```text
NOT CHECKED
NOT ACCESSIBLE
NOT APPLICABLE
UNKNOWN
REQUIRES SEMANTIC REVIEW
```

| Area / Question | Gap State | Evidence / Reason | Follow-up |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

### Gap Semantics

#### NOT CHECKED

A potentially relevant source or dimension was not inspected.

#### NOT ACCESSIBLE

The source could not be inspected.

#### NOT APPLICABLE

The section or source does not apply to the declared Collection Scope.

#### UNKNOWN

The state could not be determined from available Evidence.

#### REQUIRES SEMANTIC REVIEW

Facts were collected, but a semantic conclusion requires human review.

### Negative Evidence Rule

```text
ABSENT
    ≠
NOT CHECKED

ABSENT
    ≠
NOT ACCESSIBLE

ABSENT
    ≠
UNKNOWN
```

Use `ABSENT` only when absence was actually observed inside Collection Scope.

---

## 13. Human Review Notes

This section is intentionally separate from deterministic Evidence.

### Questions

```text
List semantic questions raised by the Evidence.
```

### Uncertainty

```text
Describe uncertainty that requires human interpretation.
```

### Possible Relevance

```text
Record possible relevance without presenting it as fact.
```

### Semantic Follow-Up

```text
Identify any semantic review needed.
```

### Boundary

```text
Human Review Note
    ≠
Detected Fact
```

Do not use this section to disguise automatic conclusions as Evidence.

---

## 14. Conclusion

### Collection Status

```text
COMPLETE FOR DECLARED SCOPE
INCOMPLETE
REFRESH REQUIRED
SEMANTIC REVIEW REQUIRED
```

### Evidence Freshness

```text
CURRENT FOR RECORDED REFERENCE
STALE
UNKNOWN
```

### Scope Statement

```text
State what this snapshot does and does not cover.
```

### Outstanding Gaps

```text
Summarize unresolved collection gaps.
```

### Final Boundary

The Conclusion must not assign authoritative values for:

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

Those belong to downstream human-reviewed lifecycle artifacts.

---

# Usage Rules

## Mandatory Information

Every completed snapshot must identify:

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

## Conditional Sections

Conditional sections may be:

```text
used
marked NOT APPLICABLE
omitted when the Guide permits
```

provided that the declared Collection Scope remains clear.

## Source Traceability

Every material observation should identify a source such as:

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

## Evidence Freshness

Refresh Evidence when relevant repository state changes.

Typical triggers include:

```text
branch advances
candidate changes
files change
releases appear
governance changes
workflow state changes
```

## Read-Only Boundary

This Template records Evidence.

It does not authorize:

```text
consumer mutation
automatic remediation
automatic PR creation
automatic merge
automatic rollback
automatic recovery
```

## Structured Markdown Boundary

This Template is intentionally:

```text
human-readable
human-editable
Git-reviewable
tool-independent
```

It is not a:

```text
JSON contract
YAML contract
Schema
Manifest
typed Evidence API
machine decision contract
```

## Semantic Safety

Do not convert observations directly into:

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

Use:

```text
REQUIRES SEMANTIC REVIEW
```

when the deterministic layer has reached its boundary.

## Backward Compatibility

This Template is optional evidence support.

Existing Assessment, Application and Integration flows remain valid without it.
