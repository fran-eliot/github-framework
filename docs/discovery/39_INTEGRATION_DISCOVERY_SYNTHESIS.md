# 39 — Existing Repository Adoption Integration Discovery Synthesis

## 1. Purpose

Este documento sintetiza la evidencia obtenida durante:

```text
Existing Repository Adoption
    Integration Discovery
```

documentada en:

```text
docs/discovery/38_INTEGRATION_DISCOVERY.md
```

El objetivo es determinar:

```text
what is supported
what is provisional
what remains deferred
whether Recovery blocks first delivery
whether Integration Core is ready
for Delivery Scope Definition
```

---

## 2. Evidence Base

Consumer:

```text
fran-eliot/dental-back-spring
```

Experiment A:

```text
PR #1
README-QUICK-START
ADAPT
MODIFY
direct PASS
```

Experiment B:

```text
PR #2
DOC-CHANGELOG
ADD
CREATE
REFINE → PASS
```

Both candidates were integrated into stable `main` and verified after merge.

---

## 3. Cross-Experiment Result

Observed lifecycle:

```text
Verified Candidate
    ↓
Refresh Stable Base
    ↓
Evaluate Drift Impact
    ↓
Check Integration Conditions
    ↓
Review
    ↓
Integrate
    ↓
Verify Stable State
```

Result:

```text
INTEGRATION DISCOVERY MODEL
    HOLDS
```

No new mandatory lifecycle dimension was required between Experiment A and Experiment B.

---

## 4. Supported Finding — Integration is distinct from Application

The evidence supports:

```text
APPLY
    creates candidate state

VERIFY
    validates candidate state

INTEGRATE
    accepts candidate into stable state
```

Therefore:

```text
Application Completion
    ≠
Integration Completion
```

---

## 5. Supported Finding — Verified Candidate is the Integration Input

Both experiments began from candidates already verified during Application.

Therefore:

> Integration should begin from a verified candidate state, not directly from an Adoption Decision or unverified change.

Supported chain:

```text
Assessment Outcome
    ↓
Application Record
    ↓
Verified Candidate
    ↓
Integration
```

---

## 6. Supported Finding — Stable Base must be refreshed

Experiment A:

```text
stable base drift
    NONE
```

Experiment B:

```text
stable base drift
    PRESENT
```

Both required checking current `main` before Integration.

Therefore:

> Stable base refresh is required before Integration.

---

## 7. Supported Finding — Base Drift is contextual

Experiment B demonstrated:

```text
base advanced
    YES

candidate overlap
    NO

Intent invalidated
    NO

Preservation invalidated
    NO
```

Therefore:

```text
base drift
    ≠
automatic REPLAN
```

Supported decision logic:

```text
drift
    ↓
evaluate impact
        ├── compatible → continue
        └── invalidating → REPLAN / DEFER
```

---

## 8. Supported Finding — Mergeability is insufficient

Both Pull Requests were:

```text
mergeable = true
```

but Integration readiness also required checking:

```text
base freshness
drift impact
candidate scope
current Evidence
Application Intent validity
Preservation Scope
repository conditions
```

Therefore:

```text
Git Mergeability
    ≠
Integration Readiness
```

---

## 9. Supported Finding — Consumer Governance is authoritative

Observed repository governance was minimal:

```text
formal approvals
    NONE

required workflow runs
    NONE

status checks
    NONE
```

This does not justify universal absence of controls.

Instead:

> Integration must observe and respect consumer repository governance rather than impose a Framework-specific merge policy.

Supported principle:

```text
Consumer Governance
    over
Framework Merge Preference
```

---

## 10. Supported Finding — Integration Conditions are contextual

Potential Integration conditions may include:

```text
mergeability
required reviews
required checks
branch protection
base freshness
release constraints
```

The exact set is repository-specific.

Therefore a reusable Integration model should provide:

```text
place to record conditions
```

not:

```text
fixed universal checklist
```

---

## 11. Supported Finding — Stable-State Verification is mandatory

Both experiments explicitly verified stable `main` after merge.

Experiment A:

```text
README corrected
runtime config aligned
```

Experiment B:

```text
CHANGELOG created
prior README fix preserved
```

Therefore:

```text
Merge Success
    ≠
Integration Verified
```

Supported chain:

```text
INTEGRATE
    ↓
VERIFY STABLE STATE
```

---

## 12. Supported Finding — Verification remains multi-dimensional

Observed stable-state verification covered:

```text
Physical Verification
Intent Verification
Preservation Verification
```

Repository Health Verification remains a contextual candidate when relevant.

The evidence does not support making every possible verification dimension mandatory in every repository.

---

## 13. Supported Finding — CREATE and MODIFY share one lifecycle

Evidence:

```text
Experiment A
    MODIFY

Experiment B
    CREATE
```

Both integrated using the same lifecycle.

Therefore the first Integration Core does not require operation-specific Integration flows for:

```text
CREATE
MODIFY
```

---

## 14. Supported Finding — Prior refinement does not alter Integration lifecycle

Experiment B included:

```text
CREATE
    ↓
VERIFY
    ↓
REFINE
    ↓
VERIFY AGAIN
    ↓
PASS
```

No new Integration phase was needed.

Therefore:

> Application refinement history is evidence, not a separate Integration workflow.

---

## 15. Supported Finding — Integration should preserve traceability

The evidence supports retaining the chain:

```text
Assessment
    ↓
Application
    ↓
Candidate
    ↓
Integration Review
    ↓
Integration Action
    ↓
Stable-State Verification
```

This enables review of:

```text
why the change existed
what candidate was approved
how it entered stable state
whether stable state remained correct
```

---

## 16. Candidate Integration Record

A minimal human-readable record may need:

```text
Integration Context
Candidate Reference
Stable Base Reference
Stable Base Refresh
Drift Impact
Integration Conditions
Governance Constraints
Review Result
Integration Decision
Integration Method
Integration Evidence
Stable-State Verification
Recovery Notes
Final Integration State
```

Current evidence supports the need for these concepts.

Their exact field names and required/optional status remain provisional until repeatability of representation is tested.

---

## 17. Candidate Integration Decision Vocabulary

Observed successful outcome:

```text
INTEGRATE
```

Evidence also supports the need to represent safe non-integration outcomes:

```text
DEFER
REPLAN
REJECT
```

These outcomes are logically supported by the lifecycle but were not all directly executed during experiments.

Therefore:

```text
INTEGRATE
    directly observed

DEFER / REPLAN / REJECT
    supported but provisional
```

---

## 18. Candidate Final Integration States

Potential states:

```text
INTEGRATED
DEFERRED
REPLAN REQUIRED
REJECTED
RECOVERY REQUIRED
```

Directly observed:

```text
INTEGRATED
```

Others remain provisional.

---

## 19. Recovery Evidence Gap

No experiment produced:

```text
merge succeeds
    ↓
stable-state verification fails
```

Therefore no direct evidence exists for:

```text
revert commit
revert merge
follow-up fix
branch reset
release rollback
```

This gap is real.

---

## 20. Does Recovery block the first Integration Core?

The first Integration capability can be scoped around:

```text
successful reviewed Integration
+
stable-state verification
```

without claiming support for:

```text
automatic rollback
specific recovery mechanism
history rewriting
release rollback
```

A failed post-integration verification can still be represented as:

```text
RECOVERY REQUIRED
```

without prescribing how recovery occurs.

Therefore:

> Recovery evidence does not need to block the first Integration Core if recovery execution remains explicitly out of scope.

---

## 21. Recovery Boundary Candidate

In scope candidate:

```text
detect failed stable-state verification
record failure
mark RECOVERY REQUIRED
preserve evidence
```

Out of scope candidate:

```text
automatic revert
automatic rollback
branch reset
release rollback
recovery orchestration
```

This boundary is proportional to current evidence.

---

## 22. Merge Strategy Boundary

Experiments used:

```text
merge commit
```

This does not prove merge commit should be mandatory.

Therefore:

```text
merge commit
squash
rebase
```

must remain consumer-governance choices.

The Integration Core should record the actual method used, not prescribe a universal method.

---

## 23. Pull Request Boundary

Both experiments used GitHub Pull Requests.

This supports PRs as:

```text
valid Integration surface
```

but not as:

```text
mandatory universal Integration implementation
```

The conceptual model should remain repository-platform agnostic where practical.

---

## 24. Automation Boundary

No experiment required:

```text
automatic merge
automatic PR creation
automatic approval
automatic conflict resolution
automatic rollback
```

Therefore Automation remains deferred.

Principle:

```text
Human Review before Stable Integration
```

---

## 25. Structured Representation Boundary

The experiments did not require:

```text
JSON
YAML
Schema
Manifest
typed Integration Plan
machine API
```

Markdown remains sufficient for Discovery representation.

Structured Representation remains deferred.

---

## 26. Branch Protection Boundary

No restrictive branch protection behavior was exercised in the consumer experiments.

Therefore:

```text
observe branch protection
respect branch protection
```

is supported conceptually.

But:

```text
configure branch protection
standardize branch protection
```

is not supported by evidence and remains out of scope.

---

## 27. Release Interaction Boundary

No experiment required release-aware Integration.

Therefore:

```text
record release constraints when present
```

may be useful.

But no evidence supports:

```text
release orchestration
tagging
deployment
release rollback
```

as part of the first Integration Core.

---

## 28. Initial Requirement Candidate Status

| Requirement Candidate | Status |
| --- | :---: |
| RC-I01 — verified candidate input | SUPPORTED |
| RC-I02 — stable base refresh | SUPPORTED |
| RC-I03 — consumer governance precedence | SUPPORTED |
| RC-I04 — reviewable Integration conditions | SUPPORTED |
| RC-I05 — mergeability distinct from readiness | SUPPORTED |
| RC-I06 — preserve Application Intent | SUPPORTED |
| RC-I07 — preserve Preservation Scope | SUPPORTED |
| RC-I08 — record stable mutation | SUPPORTED |
| RC-I09 — verify stable state | SUPPORTED |
| RC-I10 — represent post-integration failure | SUPPORTED, NOT OBSERVED |
| RC-I11 — automatic merge deferred | SUPPORTED |
| RC-I12 — automatic recovery deferred | SUPPORTED |

---

## 29. Solution Hypothesis Status

| Solution Hypothesis | Status |
| --- | :---: |
| SH-I01 — human-reviewed Markdown Integration Record | PROVISIONALLY SUPPORTED |
| SH-I02 — PR as experimental Integration surface | SUPPORTED |
| SH-I03 — Structured Data not required | SUPPORTED |
| SH-I04 — GitHub Actions not required | SUPPORTED |
| SH-I05 — stable-state verification required | SUPPORTED |

The main remaining representation question is whether a single Markdown record can represent Integration outcomes without structural redesign.

---

## 30. Delivery Readiness Criteria

| Criterion | Result |
| --- | :---: |
| Observed Need | PASS |
| Actual Integration Evidence | PASS |
| Repeated Integration Evidence | PASS |
| Cross-operation Evidence | PASS |
| Drift Handling Evidence | PASS |
| Stable-State Verification | PASS |
| Representation Stability | PARTIAL |
| Recovery Execution Evidence | NOT REQUIRED FOR INITIAL SCOPE |
| Proportional Complexity | PASS |

The remaining meaningful gap is:

```text
representation repeatability
```

not lifecycle feasibility.

---

## 31. Why Representation Repeatability remains partial

The lifecycle repeated successfully, but no explicit reusable Integration Record has yet been instantiated and replayed.

Therefore:

```text
Integration lifecycle
    repeated

Integration representation
    not yet repeated
```

This is the same type of gap that previously justified repeatability testing for Assessment and Application.

---

## 32. Integration Core Candidate

Current evidence supports a candidate composed of:

```text
Stable Base Refresh
Drift Impact Evaluation
Integration Conditions
Consumer Governance Constraints
Human Review
Integration Decision
Integration Action
Stable-State Verification
Recovery Required representation
```

with:

```text
automatic merge
automatic recovery
release automation
structured representation
```

deferred.

---

## 33. Delivery Readiness Result

Because the lifecycle itself is repeated but representation stability is not yet demonstrated:

```text
Integration Core Candidate
    NOT YET READY
    FOR DELIVERY SCOPE DEFINITION
```

Reason:

```text
repeat reusable Integration representation
without material redesign
```

---

## 34. Recommended Next Step

Create:

```text
40_INTEGRATION_REPEATABILITY_EXPERIMENT.md
```

The experiment should:

```text
materialize a minimal Markdown Integration Record

reconstruct Experiment A

reconstruct Experiment B

verify that both fit
without structural workaround

test direct PASS
and base-drift-compatible PASS
```

Success condition:

```text
MODEL HOLDS
```

Failure condition:

```text
MATERIAL REDESIGN REQUIRED
```

---

## 35. Scope Guardrail for Repeatability

Do not expand the experiment to:

```text
automatic merge
automatic conflict resolution
automatic rollback
release orchestration
branch protection configuration
DELETE
MOVE
RENAME
Structured Data
Schema
Manifest
CLI
GitHub Actions
```

The objective is representation stability, not capability expansion.

---

## 36. Current State

```text
Assessment Core
    RELEASED

Application Core
    RELEASED

Integration Discovery
    COMPLETED

Integration Discovery Model
    HOLDS

Integration Core Candidate
    PROVISIONALLY SUPPORTED

Representation Repeatability
    NOT YET ESTABLISHED

Delivery Scope
    NOT YET READY

Next Version
    NOT COMMITTED

Next Sprint
    NOT OPENED
```
