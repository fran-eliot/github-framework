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
