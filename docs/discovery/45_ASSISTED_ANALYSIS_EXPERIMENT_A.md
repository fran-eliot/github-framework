# 45 — Assisted Analysis Experiment A — Assessment Evidence Collection

## 1. Purpose

Evaluate whether a bounded set of deterministic repository checks can reduce repeated manual Evidence collection during Existing Repository Adoption Assessment without replacing semantic review.

The experiment tests:

```text
repository scanning
    +
deterministic evidence collection
```

against a real consumer repository.

---

## 2. Consumer

```text
fran-eliot/only_film
```

Reference:

```text
branch
    main

commit
    28d75a50e0a178954dd46acc23300d9dd327843c
```

Repository characteristics observed:

```text
Java
Spring Boot
Maven
Docker
GitHub Actions
documentation directory
```

---

## 3. Experiment Boundary

This experiment collects only observable facts.

It does not assign:

```text
Responsibility State
Applicability
Adoption Decision
Application Result
Integration Decision
```

It does not mutate the consumer.

---

## 4. Checks Executed

The bounded check set was:

```text
root repository listing
README.md presence
CHANGELOG.md presence
pom.xml presence
application.properties presence
application.yml presence
docs/ directory presence
.github/ presence
workflow directory listing
Dependabot configuration presence
Git tags
GitHub Releases
main branch reference
branch protection state
required status-check contexts
```

---

## 5. Root Structure Evidence

Observed root entries:

```text
20 total
13 files
7 directories
```

Observed root files include:

```text
README.md
pom.xml
Dockerfile
compose.yaml
compose.sonar.yaml
.env.example
```

Observed root directories include:

```text
.github/
docs/
src/
sonar/
uploads/
```

Result:

```text
DETERMINISTIC EVIDENCE
    COLLECTED
```

---

## 6. Documentation Evidence

Observed:

```text
README.md
    PRESENT

CHANGELOG.md
    ABSENT

docs/
    PRESENT

docs entries
    31
```

A filename-oriented scan found one documentation artifact whose name may be historically relevant:

```text
docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md
```

Important boundary:

```text
root CHANGELOG.md absent
    ≠
DOC-CHANGELOG Responsibility Missing
```

The absence of the canonical artifact is a fact.

Responsibility coverage remains a semantic Assessment question.

---

## 7. Build and Runtime Evidence

Observed:

```text
pom.xml
    PRESENT

src/main/resources/application.properties
    PRESENT

src/main/resources/application.yml
    ABSENT
```

The properties file identifies:

```text
spring.application.name
spring.application.version
spring.application.title
datasource configuration
Flyway enablement state
```

These observations can support later Assessment questions but do not determine semantic conformance by themselves.

---

## 8. GitHub Automation Evidence

Observed:

```text
.github/
    PRESENT

.github/dependabot.yml
    PRESENT

.github/workflows/
    PRESENT
```

Workflow count:

```text
7
```

Observed workflows:

```text
compose-smoke.yml
postgres-demo-seed.yml
postgres-migration.yml
selenium-review.yml
sonar.yml
tests.yml
ticket-regression.yml
```

This evidence supports the fact that repository automation exists.

It does not by itself prove any specific Framework Responsibility is satisfied.

---

## 9. Release Evidence

Observed:

```text
Git tags
    0

GitHub Releases
    0
```

This is deterministic release evidence.

It may inform Assessment but must not be converted automatically into:

```text
release governance missing
changelog missing
versioning missing
```

without semantic review.

---

## 10. Stable Reference Evidence

Observed:

```text
default branch
    main

current main commit
    28d75a50e0a178954dd46acc23300d9dd327843c
```

This gives a reproducible consumer reference for the Evidence snapshot.

---

## 11. Branch Governance Evidence

Observed:

```text
main protected
    false

branch protection enabled
    false

required status-check contexts
    none
```

This is repository-state Evidence only.

It does not imply that:

```text
branch governance
    is semantically inadequate
```

---

## 12. Deterministic vs Semantic Boundary

The experiment produced deterministic observations such as:

```text
file exists
file absent
directory exists
workflow count
tag count
release count
branch SHA
branch protection flag
```

But it could not determine without human interpretation:

```text
Responsibility satisfaction
semantic equivalence
documentation quality
governance adequacy
release maturity
Adoption Decision
```

Result:

```text
FACT / EVALUATION BOUNDARY
    PRESERVED
```

---

## 13. Repetition Observed

The same check categories appeared previously during Adoption, Application and Integration work:

```text
artifact presence
repository structure
Git reference lookup
release lookup
workflow presence
branch-state lookup
```

Experiment A confirms these checks can be executed as a reusable bounded collection step.

---

## 14. Manual Effort Signal

Without assistance, the reviewer must repeatedly:

```text
navigate repository structure
check known artifact paths
inspect GitHub metadata
record refs
count workflows
look up tags and releases
transcribe factual evidence
```

The collected data itself is mechanical.

The interpretation remains human.

Result:

```text
OPERATIONAL REPETITION
    OBSERVED
```

---

## 15. Evidence Reuse Potential

The same snapshot can support:

### Assessment

```text
Detected Facts
Evidence References
repository structure
artifact presence
automation presence
release evidence
```

### Application

```text
Evidence Refresh
current artifact state
current refs
current configuration
```

### Integration

```text
Stable Base Reference
current branch SHA
repository conditions
workflow / status evidence
```

Result:

```text
CROSS-STAGE REUSE POTENTIAL
    OBSERVED
```

---

## 16. Representation Finding

No Structured Data contract was required to execute or interpret the experiment.

A human-readable Evidence Snapshot remains sufficient at this stage.

Result:

```text
STRUCTURED REPRESENTATION REQUIRED
    NO
```

---

## 17. Tooling Finding

The experiment demonstrates useful deterministic collection, but does not yet prove that a production CLI or scanner is justified.

Current evidence supports:

```text
Assisted collection
    useful
```

but not yet:

```text
production scanner
    required
```

---

## 18. Requirement Candidate Check

| Requirement Candidate | Experiment A |
| --- | :---: |
| RC-AA01 — facts distinct from evaluation | SUPPORTED |
| RC-AA02 — source traceability | SUPPORTED |
| RC-AA03 — bounded repository scanning | SUPPORTED |
| RC-AA04 — deterministic semantics | SUPPORTED |
| RC-AA05 — human review mandatory | SUPPORTED |
| RC-AA06 — non-canonical implementations remain discoverable | SUPPORTED |
| RC-AA07 — Assessment decisions human-owned | SUPPORTED |
| RC-AA08 — Application decisions human-owned | NOT TESTED |
| RC-AA09 — Integration decisions human-owned | NOT TESTED |
| RC-AA10 — read-only operation | SUPPORTED |
| RC-AA11 — cross-stage reuse | PROVISIONALLY SUPPORTED |
| RC-AA12 — proportional tooling complexity | OPEN |

---

## 19. Experiment A Result

Evidence shows:

```text
repeated deterministic checks
    YES

bounded repository scanning
    YES

traceable factual evidence
    YES

semantic boundary preserved
    YES

read-only operation
    YES

cross-stage reuse potential
    YES

production tooling requirement
    NOT YET PROVEN
```

Therefore:

```text
ASSISTED ANALYSIS NEED
    PARTIAL CONFIRMATION
```

---

## 20. What Partial Confirmation Means

The experiment confirms an operational need for reusable evidence collection.

It does not yet establish:

```text
final representation
production scanner
CLI
schema
automation architecture
Delivery Scope
implementation readiness
```

---

## 21. Next Evidence Needed

Run:

```text
Experiment B
    Application Evidence Refresh
```

to test whether the same deterministic evidence model remains useful during current-state refresh before mutation.

Then run:

```text
Experiment C
    Integration Stable Base Refresh
```

to test cross-stage reuse and preserve human drift evaluation.

---

## 22. Current State

```text
Assisted Analysis Discovery
    ACTIVE

Experiment A
    COMPLETED

Need
    PARTIALLY CONFIRMED

Delivery Scope
    NOT DEFINED

Implementation
    NOT COMMITTED

Sprint 12
    NOT OPENED

Target Version
    NONE
```
