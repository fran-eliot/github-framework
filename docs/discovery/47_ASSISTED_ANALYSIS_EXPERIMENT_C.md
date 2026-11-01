# 47 — Assisted Analysis Experiment C — Integration Stable Base Refresh

## 1. Purpose

Evaluate whether the deterministic Evidence model validated in Assessment and Application can also support Existing Repository Adoption Integration during:

```text
REFRESH STABLE BASE
```

without automating Drift Impact, Integration Review or Integration Decision.

---

## 2. Consumer

```text
fran-eliot/dental-back-spring
```

Historical Integration evidence:

```text
PR #1
    README-QUICK-START
    MODIFY

PR #2
    DOC-CHANGELOG
    CREATE
```

---

## 3. Experiment Focus

Experiment C replays the Stable Base Refresh conditions around PR #2.

Historical facts:

```text
PR #2 original base
    e17b009602f25da0d6f32920180254eb9392fee2

PR #1 merge commit
    c61829ff27f1e6cb6fffc4210e224bd275c00139

PR #2 candidate head
    c209c82965f4510fef8a60df5210ce75c7689439

PR #2 final merge commit
    ddd09369b98d11da25525ae09bfdb840c3f4ce50
```

The experiment tests whether deterministic collection can surface enough Evidence for a human reviewer to evaluate drift.

---

## 4. Experiment Boundary

Deterministic collection may identify:

```text
stable reference
candidate reference
base advancement
changed files
mergeability metadata
reviews
workflow runs
status checks
branch protection state
```

It must not decide:

```text
Drift Impact
    COMPATIBLE
    INVALIDATING
    UNCERTAIN

Integration Review
    PROCEED
    DEFER
    REPLAN
    REJECT

Integration Decision
    INTEGRATE
    DEFER
    REPLAN
    REJECT
```

---

## 5. Stable Base Refresh Evidence

PR #2 was created from:

```text
e17b009602f25da0d6f32920180254eb9392fee2
```

Before PR #2 Integration, stable `main` had advanced to:

```text
c61829ff27f1e6cb6fffc4210e224bd275c00139
```

Deterministic comparison result:

```text
stable base
    AHEAD BY 2 COMMITS
```

Result:

```text
BASE DRIFT
    PRESENT
```

This is a factual observation.

---

## 6. Stable Base Changed Files

Comparison:

```text
e17b009602f25da0d6f32920180254eb9392fee2
    →
c61829ff27f1e6cb6fffc4210e224bd275c00139
```

Observed changed artifact:

```text
README.md
    MODIFIED
```

Change stats:

```text
additions
    2

deletions
    3

changes
    5
```

Result:

```text
STABLE DRIFT ARTIFACT SET
    DETERMINISTICALLY COLLECTED
```

---

## 7. Candidate Changed Files

PR #2 candidate comparison:

```text
e17b009602f25da0d6f32920180254eb9392fee2
    →
c209c82965f4510fef8a60df5210ce75c7689439
```

Observed changed artifact:

```text
CHANGELOG.md
    ADDED
```

Change stats:

```text
additions
    5

deletions
    0

changes
    5
```

Result:

```text
CANDIDATE ARTIFACT SET
    DETERMINISTICALLY COLLECTED
```

---

## 8. Apparent File Overlap

Observed:

```text
stable drift artifact
    README.md

candidate artifact
    CHANGELOG.md
```

Direct file-path overlap:

```text
NONE
```

This is deterministic.

However:

```text
no direct file overlap
    ≠
Drift Impact COMPATIBLE
```

Semantic compatibility remains a human judgment.

---

## 9. Pull Request Evidence

PR #2 historical state:

```text
state
    CLOSED

merged
    true

base SHA
    e17b009602f25da0d6f32920180254eb9392fee2

head SHA
    c209c82965f4510fef8a60df5210ce75c7689439

merge commit
    ddd09369b98d11da25525ae09bfdb840c3f4ce50
```

This Evidence is deterministic.

---

## 10. Review Evidence

Observed PR #2 reviews:

```text
reviews
    0
```

This records consumer governance evidence.

It does not imply:

```text
review unnecessary
```

or:

```text
Integration ready
```

without context.

---

## 11. Workflow Evidence

Observed candidate workflow runs:

```text
workflow runs
    0
```

This is factual Evidence.

It does not automatically imply:

```text
checks not required
```

or:

```text
Integration ready
```

without consumer governance context.

---

## 12. Commit Status Evidence

Observed candidate commit statuses:

```text
statuses
    0
```

Again:

```text
no statuses
    ≠
approval to integrate
```

---

## 13. Current Stable State

Current `main` is:

```text
ddd09369b98d11da25525ae09bfdb840c3f4ce50
```

This matches the historical PR #2 merge commit.

Result:

```text
FINAL INTEGRATED STABLE REFERENCE
    VERIFIED
```

---

## 14. Branch Protection Evidence

Current `main` reports:

```text
protected
    false

branch protection enabled
    false

required status-check contexts
    none
```

This is contextual Evidence only.

It does not establish universal Integration policy.

---

## 15. Deterministic Stable Base Snapshot

A reusable deterministic snapshot can represent:

```text
Original Stable Base
    e17b009602f25da0d6f32920180254eb9392fee2

Refreshed Stable Base
    c61829ff27f1e6cb6fffc4210e224bd275c00139

Base Drift
    PRESENT

Stable Drift Files
    README.md

Candidate Head
    c209c82965f4510fef8a60df5210ce75c7689439

Candidate Files
    CHANGELOG.md

Direct File Overlap
    NONE

Reviews
    0

Workflow Runs
    0

Commit Statuses
    0
```

This snapshot is entirely factual.

---

## 16. Human Drift Evaluation Boundary

Historical Integration concluded:

```text
Drift Impact
    COMPATIBLE
```

The deterministic layer can support that review by showing:

```text
where stable state changed
where candidate state changed
whether file paths overlap
what repository conditions exist
```

But it cannot safely conclude:

```text
COMPATIBLE
```

because semantic dependencies may exist even without path overlap.

Therefore:

```text
Drift Evidence
    ≠
Drift Impact
```

---

## 17. Integration Review Boundary

The deterministic layer can provide:

```text
current refs
changed files
reviews
workflow runs
statuses
branch protection state
```

Human review still determines:

```text
Application Intent remains valid
Preservation Scope remains valid
consumer governance is satisfied
candidate remains within scope
PROCEED / DEFER / REPLAN / REJECT
```

Result:

```text
INTEGRATION REVIEW
    REMAINS HUMAN-OWNED
```

---

## 18. Integration Decision Boundary

The experiment does not produce:

```text
INTEGRATE
```

It produces Evidence that may support a human Integration Decision.

Therefore:

```text
Assisted Stable Base Refresh
    ≠
Automatic Integration
```

---

## 19. Reuse from Experiments A and B

Experiment A:

```text
Assessment
    Detected Facts + Evidence
```

Experiment B:

```text
Application
    Evidence Refresh
```

Experiment C:

```text
Integration
    Stable Base Refresh Evidence
```

The same conceptual model now spans all three lifecycle stages.

Result:

```text
CROSS-LIFECYCLE EVIDENCE REUSE
    OBSERVED
```

---

## 20. Stable Evidence Concepts Across Stages

Repeated concepts include:

```text
repository reference
artifact presence
artifact change
Git refs
GitHub metadata
workflow evidence
status evidence
source traceability
bounded consumer context
```

No new mandatory Evidence dimension was required for Integration.

---

## 21. Operational Need

Manual Integration review otherwise requires repeatedly collecting:

```text
current stable SHA
candidate SHA
base advancement
changed files
reviews
workflow runs
commit statuses
branch protection state
```

These are mechanical operations.

The semantic decision remains human.

Result:

```text
INTEGRATION EVIDENCE COLLECTION REPETITION
    OBSERVED
```

---

## 22. Requirement Candidate Check

| Requirement Candidate | Experiment A | Experiment B | Experiment C |
| --- | :---: | :---: | :---: |
| RC-AA01 — facts distinct from evaluation | SUPPORTED | SUPPORTED | SUPPORTED |
| RC-AA02 — source traceability | SUPPORTED | SUPPORTED | SUPPORTED |
| RC-AA03 — bounded repository scanning | SUPPORTED | SUPPORTED | SUPPORTED |
| RC-AA04 — deterministic semantics | SUPPORTED | SUPPORTED | SUPPORTED |
| RC-AA05 — human review mandatory | SUPPORTED | SUPPORTED | SUPPORTED |
| RC-AA06 — non-canonical implementations remain discoverable | SUPPORTED | SUPPORTED | PRESERVED |
| RC-AA07 — Assessment decisions human-owned | SUPPORTED | PRESERVED | PRESERVED |
| RC-AA08 — Application decisions human-owned | NOT TESTED | SUPPORTED | PRESERVED |
| RC-AA09 — Integration decisions human-owned | NOT TESTED | NOT TESTED | SUPPORTED |
| RC-AA10 — read-only operation | SUPPORTED | SUPPORTED | SUPPORTED |
| RC-AA11 — cross-stage reuse | PROVISIONALLY SUPPORTED | SUPPORTED | SUPPORTED |
| RC-AA12 — proportional tooling complexity | OPEN | OPEN | OPEN |

---

## 23. Structured Representation Finding

Experiment C required no:

```text
Schema
Manifest
database
typed Integration Evidence API
machine decision contract
```

Human-readable Evidence remains sufficient for Discovery.

Result:

```text
STRUCTURED REPRESENTATION REQUIRED
    NO
```

---

## 24. Automation Finding

The experiment supports deterministic collection.

It does not support:

```text
automatic drift classification
automatic Integration Review
automatic approval
automatic merge
automatic rollback
```

Result:

```text
DECISION AUTOMATION REQUIRED
    NO
```

---

## 25. Experiment C Result

Evidence now shows:

```text
Assessment reuse
    YES

Application reuse
    YES

Integration reuse
    YES

same evidence model
    YES

stable-base refresh support
    YES

human semantic boundary
    HOLDS

read-only boundary
    HOLDS
```

Therefore:

```text
ASSISTED ANALYSIS OPERATIONAL NEED
    CONFIRMED

CROSS-LIFECYCLE REUSE
    CONFIRMED
```

---

## 26. What Is Still Unproven

The experiments do not yet prove:

```text
production CLI required
repository scanner architecture
GitHub-specific collector required
single unified Evidence Snapshot required
Schema required
Manifest required
Componentization required
continuous reassessment required
```

These remain solution questions.

---

## 27. Proportional Complexity Question

The remaining key Discovery question is:

> What is the smallest reusable solution that materially reduces deterministic Evidence collection without creating unnecessary tooling architecture?

Candidate possibilities remain:

```text
manual evidence checklist
guided Markdown evidence snapshot
small read-only helper
GitHub evidence collector
combined approach
```

No option is selected yet.

---

## 28. Discovery Readiness

After Experiments A, B and C:

```text
Operational Need
    CONFIRMED

Repeated Deterministic Work
    CONFIRMED

Cross-Lifecycle Reuse
    CONFIRMED

Human Judgment Boundary
    CONFIRMED

Read-Only Boundary
    CONFIRMED

Structured Representation Requirement
    NOT OBSERVED

Decision Automation Requirement
    NOT OBSERVED
```

This is sufficient to proceed to:

```text
Assisted Analysis Discovery Synthesis
```

but not yet directly to Delivery Scope.

---

## 29. Recommended Next Step

Create:

```text
48_ASSISTED_ANALYSIS_DISCOVERY_SYNTHESIS.md
```

The Synthesis should determine:

```text
supported requirements
provisional requirements
solution candidates
proportional complexity
minimal representation candidate
remaining evidence gaps
whether a repeatability experiment is required
whether Delivery Scope Definition is justified
```

---

## 30. Current State

```text
Assisted Analysis Discovery
    ACTIVE

Experiment A
    COMPLETED

Experiment B
    COMPLETED

Experiment C
    COMPLETED

Operational Need
    CONFIRMED

Cross-Lifecycle Reuse
    CONFIRMED

Discovery Synthesis
    NEXT

Delivery Scope
    NOT DEFINED

Implementation
    NOT COMMITTED

Sprint 12
    NOT OPENED

Target Version
    NONE
```
