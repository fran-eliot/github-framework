# 44 — Existing Repository Adoption Assisted Analysis Discovery

## 1. Propósito

Investigar si Existing Repository Adoption necesita una capability reusable de **Assisted Analysis** para reducir trabajo manual repetitivo sin automatizar evaluación semántica, decisiones de adopción o mutaciones del consumer.

El objetivo de esta fase es estudiar específicamente:

```text
repository scanning
deterministic evidence collection
```

antes de decidir si existe evidencia suficiente para definir un Delivery Scope.

Esta fase no abre Sprint, no compromete versión y no autoriza implementación.

---

## 2. Contexto

Existing Repository Adoption dispone ya de tres capabilities publicadas:

```text
Assessment Core
    ↓
optional Application Core
    ↓
optional Integration Core
```

Publicadas en:

```text
v0.7.0
    Assessment Core

v0.8.0
    Application Core

v0.9.0
    Integration Core
```

Las tres capabilities son deliberadamente:

```text
manual
human-reviewed
evidence-backed
Markdown-based
```

La siguiente pregunta no es si debe automatizarse Existing Repository Adoption en general.

La pregunta es más limitada:

> ¿Existen pasos deterministas y repetidos de recopilación de Evidence que puedan asistirse sin sustituir interpretación, evaluación o decisión humana?

---

## 3. Evidence Base

La investigación previa ha utilizado múltiples consumer repositories y distintos stacks.

Assessment trabajó con consumers como:

```text
Only Film
Dental Back
Aula Robótica Platform
Apitimebank
Dental Back Spring
```

Application y Integration añadieron Evidence operacional sobre:

```text
current repository state
file presence
runtime configuration
Git tags
GitHub Releases
Pull Requests
branches
commits
mergeability
reviews
workflow runs
status checks
stable-base drift
changed artifacts
post-integration stable state
```

Estos datos fueron recopilados manualmente durante los experimentos.

---

## 4. Existing Backlog Signal

El Product Backlog mantiene deferred:

```text
Assisted Analysis

repository scanning
deterministic evidence collection
```

con la condición:

```text
requires evidence of operational need
```

Por tanto, esta Discovery debe probar o refutar esa necesidad.

---

## 5. Important Boundary

Assisted Analysis no debe confundirse con:

```text
semantic assessment
Adoption Decision
Application planning
Integration Decision
automatic remediation
repository mutation
automatic merge
```

El candidato investigado se limita a:

```text
collect observable facts
normalize deterministic observations
present Evidence for human review
```

---

## 6. Candidate Problem

Los experimentos muestran que una parte relevante del trabajo manual consiste en localizar y comprobar hechos repetibles.

Ejemplos:

```text
Does README.md exist?

Does CHANGELOG.md exist?

Which documentation paths exist?

Which Git tags exist?

Which GitHub Releases exist?

What branch or commit is current?

Which files changed?

Does a configured port match documentation?

Are workflow runs present?

Are status checks present?

Is a Pull Request mergeable?

Has stable main advanced since candidate creation?

Did expected stable artifacts appear after Integration?
```

Estas preguntas son distintas de:

```text
Is the Responsibility satisfied?

Is the implementation equivalent?

Is ADAPT preferable to PRESERVE?

Is drift semantically compatible?

Should this candidate be integrated?
```

Las primeras pueden ser deterministas.

Las segundas requieren interpretación humana.

---

## 7. Discovery Question

Pregunta principal:

> ¿Puede una capa de Assisted Analysis recopilar y presentar Evidence determinista de forma reusable sin colapsar Facts, Evaluation y Decision?

---

## 8. Candidate Value Proposition

Una capability Assisted Analysis sería útil únicamente si reduce:

```text
repeated repository inspection
manual evidence transcription
reference lookup
basic factual verification
```

sin reducir:

```text
human review
semantic judgment
contextual interpretation
consumer-specific reasoning
```

---

## 9. Candidate Inputs

Posibles inputs:

```text
consumer repository
consumer reference
selected Repository Template
selected Responsibility
optional Application / Integration context
```

No todos deben ser obligatorios.

Discovery debe determinar el mínimo necesario.

---

## 10. Candidate Outputs

Posibles outputs:

```text
Detected Facts
Evidence References
Repository Structure Snapshot
Relevant Artifact Presence
Git Reference Evidence
Pull Request Evidence
Workflow / Status Evidence
Stable Base Comparison Evidence
```

El output no debe asignar automáticamente:

```text
State
Applicability
Adoption Decision
Application Result
Integration Decision
Final Integration State
```

---

## 11. Facts vs Evaluation Boundary

Debe preservarse:

```text
Detected Fact
    ≠
Evaluation

Evidence
    ≠
Decision
```

Ejemplo válido:

```text
Fact
    root CHANGELOG.md absent

Evidence
    repository tree
```

Ejemplo no permitido para una capa determinista:

```text
Responsibility
    Missing
```

porque podría existir una implementación equivalente en otra ubicación.

---

## 12. Candidate Deterministic Checks

Discovery puede investigar checks como:

```text
file exists
directory exists
path matches pattern
text literal exists
configuration key exists
Git tag exists
GitHub Release exists
branch exists
commit reference exists
Pull Request state
Pull Request mergeability
review count
workflow run presence
commit status presence
changed-file list
base/head comparison
```

Cada check debe demostrar:

```text
deterministic input
deterministic observation
reviewable evidence
```

---

## 13. Non-Deterministic Checks

No deben promocionarse como deterministic Assisted Analysis sin nueva evidencia:

```text
documentation quality
semantic equivalence
responsibility coverage
architectural suitability
risk acceptability
intent validity
preservation validity
semantic drift compatibility
decision correctness
```

---

## 14. Repository Scanning Boundary

Repository scanning candidate puede incluir:

```text
tree inspection
artifact discovery
known-path lookup
pattern lookup
metadata lookup
```

No debe asumir:

```text
canonical path absent
    ⇒
Responsibility missing
```

---

## 15. Evidence Collection Boundary

Deterministic Evidence Collection candidate puede:

```text
collect
reference
summarize
normalize presentation
```

pero no:

```text
reinterpret
decide
mutate
```

---

## 16. Human Review Boundary

Toda Evidence asistida debe permanecer:

```text
inspectable
traceable
challengeable
```

La persona revisora debe poder responder:

```text
What was checked?
Where did the Evidence come from?
What was observed?
What was not checked?
```

---

## 17. Candidate Interaction with Assessment

Potential flow:

```text
Assisted Analysis
    ↓
Detected Facts + Evidence
    ↓
Human Assessment
    ↓
State / Applicability / Decision
```

Assisted Analysis no completa Assessment automáticamente.

---

## 18. Candidate Interaction with Application

Potential flow:

```text
Assisted Analysis
    ↓
Evidence Refresh support
    ↓
Human Application Planning
```

Candidate assistance may collect:

```text
current files
current configuration
current refs
current releases
```

but does not decide whether mutation should occur.

---

## 19. Candidate Interaction with Integration

Potential flow:

```text
Assisted Analysis
    ↓
Stable Base Refresh evidence
    ↓
Human Drift Evaluation
    ↓
Human Integration Review
```

Assistance may collect:

```text
current stable SHA
candidate SHA
changed files
mergeability
reviews
checks
workflow runs
base/head comparison
```

but does not decide:

```text
COMPATIBLE
INVALIDATING
PROCEED
INTEGRATE
```

---

## 20. Initial Requirement Candidates

### RC-AA01 — Observable facts remain distinct from evaluation

Assisted Analysis must not convert observations directly into semantic conclusions.

### RC-AA02 — Evidence must preserve source traceability

Every collected observation should identify its source.

### RC-AA03 — Repository scanning must be bounded

Scanning should operate against an explicit consumer and reference.

### RC-AA04 — Deterministic checks must have deterministic semantics

The same input state should produce the same observation.

### RC-AA05 — Human review remains mandatory

Assisted output must remain reviewable before semantic use.

### RC-AA06 — Non-canonical implementations must remain discoverable

The model must not treat canonical-path absence as conclusive.

### RC-AA07 — Assessment decisions remain human-owned

No automatic State, Applicability or Adoption Decision.

### RC-AA08 — Application decisions remain human-owned

No automatic Application Intent, operation selection or mutation.

### RC-AA09 — Integration decisions remain human-owned

No automatic drift classification, Integration Review or merge.

### RC-AA10 — Consumer mutation remains out of scope

Assisted Analysis is read-only.

### RC-AA11 — Evidence output should be reusable across lifecycle stages

Where practical, the same deterministic observation model should support Assessment, Application and Integration.

### RC-AA12 — Tooling complexity must remain proportional

No CLI, schema or automation architecture should be selected before operational need is demonstrated.

---

## 21. Initial Solution Hypotheses

### SH-AA01 — Manual Assisted Analysis Checklist

A reusable Markdown checklist may be sufficient to standardize deterministic evidence collection.

### SH-AA02 — Scripted Repository Scanner

A small read-only scanner may reduce repeated repository inspection.

### SH-AA03 — GitHub Evidence Collector

A read-only collector may retrieve refs, Pull Requests, releases, reviews, checks and comparisons.

### SH-AA04 — Unified Evidence Snapshot

A single normalized snapshot may support multiple Adoption lifecycle stages.

### SH-AA05 — Structured Data may remain unnecessary

Human-readable Markdown may remain sufficient even if evidence gathering becomes partially assisted.

---

## 22. Hypothesis Boundary

Discovery must not assume that:

```text
tooling
    is required
```

Possible result:

```text
manual checklist sufficient
```

is valid.

Possible result:

```text
no reusable Assisted Analysis capability justified
```

is also valid.

---

## 23. Evidence Needed

Before Delivery Scope, Discovery should demonstrate:

1. repeated deterministic checks across real consumers;
2. measurable or clearly observable manual repetition;
3. stable check semantics across more than one repository;
4. clear separation between collected facts and semantic judgment;
5. usefulness across at least two Adoption lifecycle stages;
6. no requirement for automatic decision-making;
7. no requirement for mutation;
8. proportional implementation complexity.

---

## 24. Candidate Experiments

### Experiment A — Assessment Evidence Collection

Use a real consumer and collect deterministic Evidence for a bounded set of Responsibilities.

Observe:

```text
which checks repeat
which checks are consumer-specific
which facts are insufficient without semantic review
```

### Experiment B — Application Evidence Refresh

Reuse deterministic checks to support current-state Evidence Refresh.

Observe whether the same evidence model remains useful.

### Experiment C — Integration Stable Base Refresh

Reuse deterministic checks for:

```text
stable reference
candidate reference
drift presence
changed files
reviews
checks
workflow runs
```

Observe whether human drift interpretation remains clearly separate.

---

## 25. Success Signals

Assisted Analysis Discovery may advance if experiments show:

```text
repeated deterministic work
stable evidence semantics
cross-stage reuse
clear human judgment boundary
meaningful reduction of manual inspection
```

---

## 26. Failure / Deferral Signals

Remain deferred if:

```text
checks are mostly consumer-specific
manual effort is low
semantic interpretation dominates
tooling adds more complexity than value
evidence cannot be reused
structured representation becomes prerequisite
```

---

## 27. Automation Boundary

This Discovery does not authorize:

```text
automatic remediation
automatic Assessment
automatic Adoption Decision
automatic Application
automatic merge
continuous reassessment
autonomous repository maintenance
```

---

## 28. Structured Representation Boundary

This Discovery does not assume:

```text
JSON
YAML
Schema
Manifest
typed Evidence contract
database
```

If machine-readable representation becomes necessary, that requirement must be demonstrated separately.

---

## 29. Componentization Boundary

This Discovery does not promote Assisted Analysis to a Component family.

Componentization remains a separate decision requiring proportional-value evidence.

---

## 30. Version Boundary

This document does not select:

```text
v1.0.0
v0.10.0
or any other version
```

---

## 31. Sprint Boundary

Do not open:

```text
Sprint 12
milestone
implementation Issues
```

from this document alone.

---

## 32. Discovery Outcome Vocabulary

Possible outcomes:

```text
NEED CONFIRMED
NEED PARTIAL
NEED NOT CONFIRMED
MORE EVIDENCE REQUIRED
```

A confirmed need still does not imply implementation readiness.

---

## 33. Recommended Next Step

Run:

```text
Assisted Analysis Experiment A
    Assessment Evidence Collection
```

against a real consumer repository.

The experiment should identify:

```text
repeated deterministic checks
manual effort
semantic boundary
evidence reuse potential
representation friction
```

without implementing a production scanner.

---

## 34. Current State

```text
v0.9.0
    RELEASED

Sprint
    NONE

Target Version
    NONE

Assisted Analysis
    DISCOVERY STARTED

Implementation
    NOT COMMITTED
```
