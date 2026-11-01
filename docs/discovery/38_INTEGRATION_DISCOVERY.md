# 38 — Existing Repository Adoption Integration Discovery

## 1. Purpose

Este documento inicia Discovery sobre la siguiente frontera de Existing Repository Adoption:

```text
verified candidate state
    ↓
INTEGRATE
    ↓
stable consumer state
```

Application Core v0.8.0 termina deliberadamente antes de Integration.

La pregunta central es:

> ¿Qué condiciones mínimas permiten integrar de forma segura, revisable y verificable un candidate state ya verificado en el stable state de un consumer repository sin convertir Integration en automatic merge o repository automation prematura?

---

## 2. Starting Point

Existing Repository Adoption dispone actualmente de:

```text
Assessment Core
    RELEASED

Application Core
    RELEASED
```

El flujo soportado llega hasta:

```text
ANALYZE
    ↓
ASSESS
    ↓
REVIEW
    ↓
DECIDE
    ↓
REPORT
    ↓
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

Resultado:

```text
verified candidate state
```

---

## 3. Current Explicit Boundary

Application Core v0.8.0 excluye expresamente:

```text
INTEGRATE
merge policy
merge strategy
required approvals
branch protection behavior
release interaction
post-merge verification
post-merge rollback
```

También permanecen fuera:

```text
automatic merge
automatic remediation
automatic conflict resolution
```

Integration Discovery parte exactamente de esta frontera.

---

## 4. Evidence Base

### Consumer

```text
fran-eliot/dental-back-spring
```

### Candidate A

Pull Request:

```text
#1
docs(readme): align backend execution instructions
```

State:

```text
OPEN
NOT MERGED
MERGEABLE
```

Base:

```text
main
```

Candidate branch:

```text
experiment/adoption-application-quick-start
```

Shape:

```text
1 commit
1 changed file
```

### Candidate B

Pull Request:

```text
#2
docs(changelog): añade historial inicial de cambios
```

State:

```text
OPEN
NOT MERGED
MERGEABLE
```

Base:

```text
main
```

Candidate branch:

```text
experiment/adoption-application-changelog
```

Shape:

```text
2 commits
1 changed file
```

Both candidates were produced during Application Discovery and remain intentionally outside stable consumer state.

---

## 5. Initial Observation

Application already demonstrated:

```text
candidate creation
scope preservation
verification
refinement
```

but did not demonstrate:

```text
candidate acceptance into stable state
```

Therefore:

```text
Application Verification
    ≠
Integration Completion
```

---

## 6. Core Distinction — APPLY vs INTEGRATE

```text
APPLY
    creates candidate state

VERIFY
    evaluates candidate state

INTEGRATE
    accepts candidate state into stable consumer state
```

These are separate lifecycle events.

A verified candidate may still not be appropriate to integrate immediately.

---

## 7. Core Distinction — Mergeable vs Integrable

GitHub may report:

```text
mergeable = true
```

This only indicates that the platform can currently construct a merge.

It does not prove:

```text
semantic readiness
policy readiness
review readiness
release readiness
post-merge safety
```

Therefore:

```text
Git Mergeability
    ≠
Integration Readiness
```

---

## 8. Candidate Integration Questions

Integration must answer at least:

```text
Is the candidate still based on current stable state?

Has the candidate remained verified?

Are approvals required?

Are branch protections satisfied?

Which merge strategy is appropriate?

Does integration interact with release state?

What must be verified after merge?

How can a bad integration be recovered?
```

---

## 9. Integration Intent

Candidate hypothesis:

> Integration should preserve the verified Application Intent while transitioning candidate state into stable consumer state under the consumer repository's own governance.

This implies:

```text
Application Intent
    remains relevant

Consumer Governance
    becomes authoritative
```

---

## 10. Consumer Governance over Framework Preference

Integration must not impose a universal merge strategy.

Consumer repository may define:

```text
merge commit
squash merge
rebase merge
required reviews
required checks
branch protection
release branch policy
```

Therefore:

```text
Framework Integration
    must reconcile with
Consumer Governance
```

not replace it.

---

## 11. Candidate Integration Flow

Initial candidate:

```text
Verified Candidate State
    ↓
REFRESH STABLE BASE
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

Failure paths:

```text
REPLAN
DEFER
REJECT
RECOVER
```

---

## 12. Refresh Stable Base

Before Integration, verify that stable state has not changed in a way that invalidates the candidate.

Potential checks:

```text
base branch advanced
target artifact changed
conflicting edit introduced
policy changed
required checks changed
release state changed
```

Candidate principle:

> Integration must revalidate the relationship between candidate state and current stable state.

---

## 13. Candidate Drift

Between VERIFY and INTEGRATE:

```text
stable branch may change
candidate branch may change
repository policy may change
```

Therefore:

```text
Verified at T1
    does not automatically mean
Integrable at T2
```

---

## 14. Integration Conditions

Candidate categories:

### Technical Conditions

```text
mergeability
base freshness
required checks
conflict state
```

### Governance Conditions

```text
required approvals
branch protection
merge strategy
repository policy
```

### Semantic Conditions

```text
Application Intent still valid
Preservation Scope still valid
candidate still represents approved change
```

### Release Conditions

```text
release freeze
release branch
version interaction
deployment timing
```

These categories are provisional.

---

## 15. Human Review before Integration

Application Core already requires human review before mutation.

Integration likely requires another explicit review boundary because:

```text
candidate accepted into stable state
    has broader consequences
than
candidate verified in isolation
```

Candidate principle:

```text
Human Review before Stable Integration
```

---

## 16. Pull Request as Integration Surface

Current evidence uses Pull Requests as:

```text
reviewable candidate state
```

Integration Discovery should test whether PRs provide a sufficient surface for:

```text
review
policy enforcement
mergeability
approval
integration evidence
```

without making GitHub Pull Requests a universal architectural requirement.

---

## 17. Integration Decision Candidate

A verified candidate may produce:

```text
INTEGRATE
DEFER
REPLAN
REJECT
```

before any stable mutation.

This vocabulary is provisional.

It should not be stabilized before experiment evidence.

---

## 18. Merge Strategy

Integration should not assume:

```text
merge commit
```

or:

```text
squash
```

or:

```text
rebase
```

as universal.

Merge strategy belongs first to:

```text
consumer repository governance
```

Framework may only record the strategy actually used when relevant.

---

## 19. Required Approvals

A repository may require:

```text
zero approvals
one approval
multiple approvals
CODEOWNERS
team review
```

Integration Discovery must distinguish:

```text
platform requirement
repository policy
Framework recommendation
```

These must not be conflated.

---

## 20. Required Checks

Checks may include:

```text
tests
lint
build
security scanning
quality gates
documentation validation
```

Not every candidate requires the same checks.

Candidate rule:

> Required checks are consumer-contextual evidence, not a fixed Framework checklist.

---

## 21. Branch Protection

Branch protection can provide deterministic Integration constraints.

Possible evidence:

```text
direct push prohibited
required status checks
required reviews
linear history
signed commits
```

The Framework should observe and respect these constraints rather than attempt to configure them automatically in the initial Integration Core candidate.

---

## 22. Release Interaction

Integration may occur:

```text
outside a release
inside release preparation
on release branch
before tagging
after tagging
```

This suggests release interaction is distinct from merge mechanics.

Candidate question:

> Does the first Integration delivery need release-aware behavior, or only the ability to record that release constraints exist?

---

## 23. Post-Merge Verification

A successful merge operation does not prove stable state is correct.

Therefore:

```text
Merge Success
    ≠
Integration Verified
```

Candidate flow:

```text
INTEGRATE
    ↓
VERIFY STABLE STATE
```

---

## 24. Stable-State Verification

Candidate verification dimensions:

```text
Physical Verification
Intent Verification
Preservation Verification
Repository Health Verification
```

Potential Repository Health Evidence:

```text
required checks still pass
stable branch contains expected change
no unintended files changed
repository remains buildable
```

---

## 25. Post-Integration Failure

Possible state:

```text
merge completed
    ↓
stable verification FAIL
```

This introduces a different recovery problem from Application DISCARD.

---

## 26. DISCARD vs ROLLBACK

Application Core:

```text
candidate not integrated
    ↓
DISCARD
```

Integration:

```text
candidate already integrated
    ↓
RECOVERY
```

Possible recovery mechanisms:

```text
revert commit
revert merge
follow-up fix
branch reset
release rollback
```

These mechanisms have materially different risk.

No single recovery method is yet supported.

---

## 27. Recovery Boundary

Initial hypothesis:

```text
record recovery requirement
    may be in scope

automatic rollback
    out of scope
```

A first Integration Core should not automatically mutate history to recover failed Integration.

---

## 28. Idempotency after Integration

Once candidate state is integrated:

```text
re-integrating same candidate
should not duplicate change
```

But Git merge topology may make idempotency different from Application-level idempotency.

This requires evidence.

---

## 29. Candidate Evidence Chain

Integration should preserve traceability:

```text
Assessment Outcome
    ↓
Application Record
    ↓
Verified Candidate State
    ↓
Integration Review
    ↓
Integration Action
    ↓
Stable-State Verification
```

---

## 30. Candidate Integration Record

Possible representation:

```text
Integration Context
Candidate Reference
Stable Base Reference
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

This is a representation hypothesis only.

No schema or manifest is implied.

---

## 31. Candidate Final States

Provisional:

```text
INTEGRATED
DEFERRED
REPLAN REQUIRED
REJECTED
RECOVERY REQUIRED
```

These should not be stabilized before experiments.

---

## 32. Integration Success

Candidate definition:

> Integration succeeds when the verified candidate is accepted into stable consumer state under repository governance and the resulting stable state is re-verified.

Therefore:

```text
successful merge alone
    is insufficient
```

---

## 33. Initial Requirement Candidates

### RC-I01

Integration begins only from a verified candidate state.

### RC-I02

Stable base must be refreshed before Integration.

### RC-I03

Consumer repository governance takes precedence over Framework merge preference.

### RC-I04

Integration conditions must be reviewable before stable mutation.

### RC-I05

Technical mergeability must remain distinct from Integration readiness.

### RC-I06

Integration must preserve Application Intent.

### RC-I07

Integration must preserve applicable Preservation Scope.

### RC-I08

Integration must record the actual stable-state mutation.

### RC-I09

Stable state must be verified after Integration.

### RC-I10

Post-integration failure must be representable without requiring automatic rollback.

### RC-I11

Automatic merge remains out of scope unless separately evidenced.

### RC-I12

Automatic recovery remains out of scope unless separately evidenced.

---

## 34. Initial Solution Hypotheses

### SH-I01

A human-reviewed Markdown Integration Record may be sufficient for the first reusable capability.

### SH-I02

A Git Pull Request can be used as an experimental Integration surface without becoming a mandatory universal implementation.

### SH-I03

Integration does not initially require Structured Data.

### SH-I04

Integration does not initially require GitHub Actions automation.

### SH-I05

Stable-state verification is a required lifecycle step, not an optional postscript.

---

## 35. Candidate Experiment A

Consumer:

```text
dental-back-spring
```

Candidate:

```text
PR #1
README-QUICK-START
ADAPT / MODIFY
```

Experiment questions:

```text
Can current base be refreshed?

Does candidate remain semantically valid?

What Integration conditions exist?

Can the change be merged under current repository governance?

Does stable-state verification pass?

What evidence is needed to prove Integration?
```

---

## 36. Candidate Experiment B

Consumer:

```text
dental-back-spring
```

Candidate:

```text
PR #2
DOC-CHANGELOG
ADD / CREATE / REFINE
```

Additional question:

> Does a candidate with prior refinement require any different Integration representation?

---

## 37. Experiment Safety Boundary

Experiments must not introduce:

```text
automatic merge
automatic conflict resolution
automatic rollback
branch protection changes
repository policy changes
release automation
```

The first experiment should remain human-reviewed and reversible through normal repository mechanisms.

---

## 38. Initial Delivery Readiness

Current evidence:

| Criterion | Initial Result |
| --- | :---: |
| Observed Need | PASS |
| Candidate States Available | PASS |
| Repeated Integration Evidence | FAIL |
| Stable Representation | FAIL |
| Recovery Evidence | FAIL |
| Proportional Complexity | UNKNOWN |

Therefore:

```text
Integration Core Candidate
    NOT READY
    FOR DELIVERY SCOPE DEFINITION
```

---

## 39. Evidence Gaps

Need evidence for:

```text
actual integration
stable-base refresh
governance interaction
stable-state verification
post-integration outcome
recovery boundary
repeatability
```

---

## 40. Recommended Next Step

Run controlled Integration Experiment A using:

```text
dental-back-spring
PR #1
```

Success condition:

```text
candidate integrated
stable state verified
no scope expansion required
evidence captured
```

Failure condition:

```text
integration reveals missing lifecycle dimension
or unsafe assumptions
```

Do not open:

```text
Sprint 11
milestone
target version
implementation issues
```

until Integration Discovery produces sufficient evidence.

---

## 41. Discovery State

```text
Assessment Core
    RELEASED

Application Core
    RELEASED

Integration Discovery
    STARTED

Integration Core Candidate
    NOT READY

Next Version
    NOT COMMITTED

Next Sprint
    NOT OPENED
```


---

## 42. Integration Experiment A — Execution

Consumer:

```text
fran-eliot/dental-back-spring
```

Pull Request:

```text
#1
docs(readme): align backend execution instructions
```

Pre-integration state:

```text
PR
    OPEN
    MERGEABLE

base
    main

base drift
    NONE

reviews
    NONE

review threads
    NONE

workflow runs
    NONE

status checks
    NONE
```

Candidate scope:

```text
1 commit
1 changed file
README.md
```

Current Evidence refresh confirmed:

```text
src/main/resources/application.properties
    server.port=8080
```

Candidate remained aligned with Application Intent.

Result:

```text
Integration Decision
    INTEGRATE

Integration Method
    merge commit

Merge Result
    SUCCESS

Merge Commit
    c61829ff27f1e6cb6fffc4210e224bd275c00139
```

---

## 43. Stable-State Verification — Experiment A

After Integration:

```text
main
    points to merge commit
```

README verification:

```text
cd backend
    ABSENT

localhost:3000
    ABSENT

localhost:8080
    PRESENT
```

Runtime configuration verification:

```text
server.port=8080
    PRESENT
```

Therefore:

```text
Physical Verification
    PASS

Intent Verification
    PASS

Preservation Verification
    PASS

Stable-State Verification
    PASS
```

---

## 44. Finding — Stable Base Refresh is Operationally Necessary

The PR base remained identical to current `main` before Integration.

This allowed Integration without candidate drift.

Observed rule:

> A verified candidate should not be integrated without checking whether the stable base has changed since candidate verification.

Requirement Candidate RC-I02 receives direct experimental support.

---

## 45. Finding — Mergeability is Necessary but Insufficient

Experiment A had:

```text
mergeable = true
```

but Integration readiness was established only after also checking:

```text
base freshness
candidate scope
current runtime Evidence
absence of conflicting review/check state
Application Intent validity
```

Therefore:

```text
Git Mergeability
    ≠
Integration Readiness
```

RC-I05 receives direct support.

---

## 46. Finding — Stable-State Verification is Required

The merge operation succeeded, but Integration was not considered verified until stable `main` was inspected.

Observed chain:

```text
MERGE
    ↓
VERIFY STABLE STATE
    ↓
CONFIRM
```

This supports RC-I09 and SH-I05.

---

## 47. Finding — Consumer Governance may be Minimal

For Experiment A, observable repository governance required no:

```text
formal approval
review thread resolution
workflow run
status check
```

This does not imply those conditions are unnecessary generally.

It demonstrates instead:

> Integration conditions are consumer-contextual and may legitimately be minimal.

A Framework Integration model must represent both constrained and unconstrained repositories without inventing mandatory controls.

---

## 48. Experiment A Result

```text
Stable Base Refresh
    PASS

Integration Conditions Review
    PASS

Integration
    PASS

Stable-State Verification
    PASS

Recovery Required
    NO

Experiment A
    PASS
```

No new lifecycle dimension was required.

---

## 49. Delivery Readiness after Experiment A

| Criterion | Result |
| --- | :---: |
| Observed Need | PASS |
| Candidate States Available | PASS |
| Actual Integration Evidence | PASS |
| Stable-State Verification | PASS |
| Repeated Integration Evidence | PARTIAL |
| Stable Representation | PARTIAL |
| Recovery Evidence | NOT OBSERVED |
| Proportional Complexity | PASS |

Therefore:

```text
Integration Core Candidate
    NOT YET READY
    FOR DELIVERY SCOPE DEFINITION
```

Reason:

```text
repeat Integration
on a second candidate
with prior refinement
without material redesign
```

---

## 50. Recommended Next Experiment

Use:

```text
dental-back-spring
PR #2
DOC-CHANGELOG
ADD / CREATE / REFINE
```

Experiment B should test whether the same Integration model holds when:

```text
candidate has multiple commits
candidate required refinement before Verification
new artifact is being integrated
consumer conventions materially influenced Application
```

Success condition:

```text
same Integration lifecycle holds
without new mandatory dimension
```

Do not open Sprint 11, milestone or target version yet.


---

## 51. Integration Experiment B — Execution

Consumer:

```text
fran-eliot/dental-back-spring
```

Pull Request:

```text
#2
docs(changelog): añade historial inicial de cambios
```

Candidate characteristics:

```text
Adoption Decision
    ADD

Application Operation
    CREATE

Application History
    REFINE → PASS

Commits
    2

Changed Artifacts
    1

Target
    CHANGELOG.md
```

Pre-integration state:

```text
PR
    OPEN
    MERGEABLE

reviews
    NONE

review threads
    NONE

workflow runs
    NONE

status checks
    NONE
```

Unlike Experiment A, stable `main` had advanced since the PR base.

Observed stable-base drift:

```text
main
    +2 commits from original PR base

changed artifact
    README.md
```

Candidate artifact:

```text
CHANGELOG.md
```

The drift did not overlap the candidate target.

---

## 52. Evidence Refresh — Experiment B

Current stable state confirmed:

```text
CHANGELOG.md
    ABSENT
```

Candidate content:

```text
# Historial de cambios

## [Sin publicar]

Aún no hay cambios sin publicar documentados.
```

Consumer conventions:

```text
README language
    Spanish

Candidate language
    Spanish
```

Therefore:

```text
Application Intent
    STILL VALID

Consumer Convention Preservation
    PASS

Candidate Scope
    STILL BOUNDED
```

---

## 53. Finding — Base Drift does not Automatically Require REPLAN

Experiment B demonstrates:

```text
Stable Base Changed
    YES

Candidate Target Overlap
    NO

Application Intent Invalidated
    NO

Preservation Scope Invalidated
    NO

Integration
    STILL SAFE
```

Therefore:

> Stable-base drift must be evaluated semantically and operationally; drift alone is not sufficient reason to REPLAN.

Refined candidate rule:

```text
base drift
    ↓
evaluate impact
        ├── compatible → continue
        └── invalidating → REPLAN / DEFER
```

This refines RC-I02 without weakening it.

---

## 54. Integration Result — Experiment B

Integration Decision:

```text
INTEGRATE
```

Integration Method:

```text
merge commit
```

Merge Result:

```text
SUCCESS
```

Merge Commit:

```text
ddd09369b98d11da25525ae09bfdb840c3f4ce50
```

---

## 55. Stable-State Verification — Experiment B

After Integration:

```text
main
    points to merge commit
```

New artifact verification:

```text
CHANGELOG.md
    PRESENT
```

Content verification:

```text
Spanish title
    PRESENT

[Sin publicar]
    PRESENT

unsupported historical release claims
    ABSENT
```

Preservation verification for prior integrated change:

```text
README localhost:8080
    PRESENT

README localhost:3000
    ABSENT

README cd backend
    ABSENT
```

Therefore:

```text
Physical Verification
    PASS

Intent Verification
    PASS

Preservation Verification
    PASS

Stable-State Verification
    PASS
```

---

## 56. Finding — Prior Refinement does not Require a New Integration Model

Experiment B had prior Application refinement:

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

Integration required no additional mandatory lifecycle dimension.

The same Integration model held:

```text
Verified Candidate
    ↓
Refresh Stable Base
    ↓
Check Integration Conditions
    ↓
Review
    ↓
Integrate
    ↓
Verify Stable State
```

Therefore:

> Application refinement history may be relevant evidence, but it does not require a different Integration lifecycle.

---

## 57. Finding — CREATE and MODIFY both Integrate through the Same Lifecycle

Experiments now cover:

```text
Experiment A
    ADAPT / MODIFY

Experiment B
    ADD / CREATE / REFINE
```

Both use the same Integration lifecycle.

This provides initial cross-operation repeatability.

---

## 58. Experiment B Result

```text
Stable Base Refresh
    PASS

Drift Impact Evaluation
    PASS

Integration Conditions Review
    PASS

Consumer Convention Preservation
    PASS

Integration
    PASS

Stable-State Verification
    PASS

Recovery Required
    NO

Experiment B
    PASS
```

No new lifecycle dimension was required.

---

## 59. Cross-Experiment Repeatability

| Dimension | Experiment A | Experiment B |
| --- | :---: | :---: |
| Verified Candidate | PASS | PASS |
| Stable Base Refresh | PASS | PASS |
| Base Drift Present | NO | YES |
| Drift Impact Evaluation | N/A | PASS |
| Integration Conditions Review | PASS | PASS |
| Integration | PASS | PASS |
| Stable-State Verification | PASS | PASS |
| Preservation Verification | PASS | PASS |
| Recovery Required | NO | NO |

Operations represented:

```text
MODIFY
CREATE
```

Application histories represented:

```text
direct PASS
REFINE → PASS
```

Result:

```text
Integration Lifecycle
    MODEL HOLDS
```

---

## 60. Delivery Readiness after Experiment B

| Criterion | Result |
| --- | :---: |
| Observed Need | PASS |
| Candidate States Available | PASS |
| Actual Integration Evidence | PASS |
| Repeated Integration Evidence | PASS |
| Stable-State Verification | PASS |
| Stable Representation | PASS |
| Recovery Evidence | NOT OBSERVED |
| Proportional Complexity | PASS |

The only remaining evidence gap is post-integration failure and recovery.

However:

```text
automatic rollback
    already deferred

recovery mechanism
    not required
    to describe successful Integration
```

This raises a scope question rather than an immediate implementation requirement:

> Must Recovery be part of the first Integration Core, or can the first delivery stop at verified successful Integration while representing failure as RECOVERY REQUIRED?

---

## 61. Current Discovery Conclusion

The repeated experiments support:

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

Supported observations:

```text
mergeability
    necessary but insufficient

base drift
    must be evaluated
    not automatically rejected

consumer governance
    contextual

stable-state verification
    required

CREATE and MODIFY
    share Integration lifecycle

prior Application refinement
    does not require new lifecycle
```

Result:

```text
INTEGRATION DISCOVERY MODEL
    HOLDS
```

---

## 62. Recommended Next Step

Create:

```text
39_INTEGRATION_DISCOVERY_SYNTHESIS.md
```

The synthesis should determine:

```text
what is evidence-backed
what remains provisional
whether Recovery blocks first delivery
whether Integration Core is ready
for Delivery Scope Definition
```

Do not yet open:

```text
Sprint 11
milestone
target version
implementation issues
```
