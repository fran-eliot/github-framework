# Existing Repository Adoption

The **Existing Repository Adoption** capability provides reusable guidance for assessing an existing repository against the Responsibilities defined by a GitHub Framework Repository Template. Optionally, a resolved Adoption Decision can progress to a verified candidate state and then be integrated into the consumer's stable state.

The current release provides three lifecycle capabilities and one optional, cross-cutting Evidence support capability:

```text
Existing Repository Adoption
    Assessment Core
        ↓
    optional Application Core
        ↓
    optional Integration Core

Assisted Analysis
    optional evidence support
    across Assessment / Application / Integration
```

Assessment Core supports analyzing, assessing, reviewing, and documenting Adoption Decisions.

Application Core supports planning, applying bounded changes in isolation, and verifying justified changes.

Integration Core supports reviewing and integrating a verified candidate into the consumer's stable state, following the consumer's governance and verifying the resulting stable state.

Assisted Analysis supports deterministic, bounded, source-traceable, read-only Evidence collection across these stages. It does not replace semantic evaluation or human decisions.

### Your First Assessment: Minimal Walkthrough

To get started with an existing repository **without modifying it**:

1. **Choose a Template.** Explore the [Repository Template Library](../templates/repositories/README.md) and select one that matches the consumer. For example, [TPL-BACKEND](../templates/repositories/backend/README.md) may fit a backend service.
2. **Pin the contract.** Read the Template's guidance and obtain its `id` and `version` from canonical metadata (for example, [TPL-BACKEND metadata](../templates/repositories/backend/metadata.yml)). The Template version is distinct from the Framework's release version.
3. **Pin the consumer.** Record the repository URL and an exact commit SHA. A mutable branch name alone is insufficient for reproducible Evidence.
4. **Create a working record.** Copy the [Assessment Template](assessment-template.md) to your own working file. Fill in `Consumer Repository`, `Consumer Reference`, `Repository Template`, `Template Version`, date, and `Assessment Status: In Progress`.
5. **Start with facts.** Choose one Responsibility declared by the Template, inspect relevant artifacts, and record `Detected Facts` and commit-pinned `Evidence` references. Do not infer a Decision from the presence or absence of a particular filename.
6. **Evaluate explicitly.** Record `State`, `Applicability`, `Implementation Characteristics`, `Uncertainty`, and `Evaluation Rationale`. If Evidence or review is insufficient, keep `Decision Status: Needs Further Evaluation` and `Adoption Decision: —`.
7. **Save the partial result.** Documenting one Responsibility is a **starting point**, not a complete Assessment. Before setting `Complete`, cover and review the Responsibilities required by the selected Template under this Guide's completion rules.

**What's next?** Only a reviewed, resolved Adoption Decision may proceed to [Application](application/README.md), which refreshes Evidence and requires a plan and verification before isolated changes. [Integration](integration/README.md) subsequently requires a verified candidate and stable-base review. [Assisted Analysis](assisted-analysis/README.md) optionally supports read-only Evidence collection, not automated decisions.

**Worked example:** see the [first Assessment example](examples/first-assessment-example.md), which uses Evidence from a real consumer and remains `In Progress`. It covers one Responsibility, not a complete Assessment.

This walkthrough is guidance only. It does not generate repositories, execute assessments, or replace human review.
---

## 1. Purpose

Existing Repository Adoption addresses a different problem from creating a new repository.

An existing repository may:

- already implement a Responsibility through a canonical artifact;
- satisfy it through an equivalent implementation;
- distribute it across several artifacts;
- cover it only partially;
- not implement it;
- not require it in its specific context.

Existing Repository Adoption therefore emphasizes:

```text
reconciliation
```

rather than:

```text
generation
replacement
automatic remediation
```

Assessment Core aims to produce an evaluation that is:

```text
usable
repeatable
traceable
reviewable
persistent
```

while explicitly retaining human review.

---

## 2. Scope

The supported process is:

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
```

The outcome is a persistent Markdown Assessment preserving:

```text
Detected Facts
Evidence
Evaluation
Uncertainty
Adoption Decisions
Rationale
```

Assessment Core does not modify the consumer repository.

Once an Adoption Decision is resolved, Application Core may optionally continue with:

```text
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

The Application Core boundary is a verified candidate state.

When a verified candidate state exists, Integration Core may optionally continue with:

```text
REFRESH STABLE BASE
    ↓
EVALUATE DRIFT
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

The Integration Core boundary is a verified stable state or a safe-stop / recovery-required state.

---

## 3. Assessment Inputs

Every Assessment starts with four conceptual inputs:

```text
Existing Consumer Repository

Repository Template

Repository Template Version

Consumer Reference
```

### Existing Consumer Repository

The repository to be assessed.

It serves as the:

```text
evidence source
```

### Repository Template

The Repository Template selected as the Assessment reference.

For selection, consult the [Repository Template Library](../templates/repositories/README.md) and the intended usage criteria of the chosen Template. For example, [TPL-BACKEND](../templates/repositories/backend/README.md) targets backend services and applications. The project type alone does not establish that the Template's Responsibilities have been satisfied.

It serves as the:

```text
assessment baseline
```

### Repository Template Version

Identifies the specific Template version used.

Confirm the ID and version in the selected Template's canonical metadata. For the backend example, see [`TPL-BACKEND/metadata.yml`](../templates/repositories/backend/metadata.yml). The Template version is independent of the published GitHub Framework version.

The Assessment must always be interpreted against that version.

### Consumer Reference

Identifies the exact consumer state being evaluated.

For example:

```text
branch
commit SHA
tag
```

The reference must be precise enough to avoid treating a historical Assessment as automatically valid for any future state of the repository.

---

## 4. Assessment Principles

### 4.1 Evidence before Automation

Assessment Core prioritizes explicit Evidence and human review over any future automation.

```text
Evidence
    before
Automation
```

### 4.2 Responsibility over File

The evaluation unit is:

```text
Responsibility
```

not:

```text
File
```

Therefore:

```text
Canonical Artifact Missing
    ≠
Responsibility Missing
```

A Responsibility may be satisfied by a non-canonical implementation.

### 4.3 Human Review Remains Explicit

The Assessment keeps observation, evaluation, and decision separate:

```text
Detected Fact
    ≠
Evaluated State
    ≠
Adoption Decision
```

A deterministic check may provide Evidence, but it cannot replace semantic evaluation.

### 4.4 Reconciliation over Replacement

Existing Repository Adoption must first interpret what the consumer already does.

The absence of a canonical structure does not, by itself, require replacing an existing solution.

---

## 5. Assessment Model

For each Responsibility, the following dimensions are recorded and evaluated:

```text
Responsibility
Requirement Level
Detected Facts
Evidence
State
Applicability
Implementation Characteristics
Uncertainty
Evaluation Rationale
Decision Status
Adoption Decision
Decision Rationale
```

These dimensions must not be collapsed into one another.

In particular:

```text
State
    ≠
Applicability
    ≠
Adoption Decision
```

---

## 6. Process

### 6.1 ANALYZE

The purpose of ANALYZE is to identify observable information about the consumer.

Record:

```text
Detected Facts
Evidence
```

without deciding which Adoption action is appropriate yet.

Examples of Detected Facts:

```text
README.md exists

docs/ directory is absent

OpenAPI configuration exposes API documentation

repository-level LICENSE file is not present
```

A Detected Fact must be verifiable.

It must not contain a semantic conclusion.

```text
Fact
    ≠
Evaluation
```

### 6.2 ASSESS

The purpose of ASSESS is to interpret Evidence against the Responsibility.

Evaluate:

```text
State
Applicability
Implementation Characteristics
Uncertainty
Evaluation Rationale
```

### 6.3 REVIEW

The purpose of REVIEW is to determine whether the evaluation can be justified.

The review must consider:

```text
evidence sufficiency
semantic interpretation
non-canonical implementations
uncertainty
applicability
```

Review is particularly important when a Responsibility is implemented using structures that differ from those defined canonically by the Template.

### 6.4 DECIDE

The purpose of DECIDE is to record whether a decision can be resolved and, when possible, which disposition is appropriate.

Record:

```text
Decision Status
Adoption Decision
Decision Rationale
```

### 6.5 REPORT

Preserve the completed Assessment as a:

```text
persistent Markdown outcome
```

The same artifact can serve as:

```text
working assessment
+
review artifact
+
persistent report
```

No separate Generated Report is required.

---

## 7. Detected Facts

Detected Facts contain verifiable observations about the consumer.

They must describe:

```text
what exists
what does not exist
what configuration is present
what repository structure is observable
```

They must not express:

```text
whether the Responsibility is satisfied
what should be changed
which Adoption Decision should be selected
```

---

## 8. Evidence

Evidence connects the Assessment to observable consumer material.

It may reference:

```text
file paths
repository sections
configuration
source code
generated documentation
repository structure
```

The general rule is:

```text
minimal sufficient evidence
```

Preserve enough Evidence for another person to review the evaluation without unnecessarily copying large amounts of consumer content.

---

## 9. Responsibility State

State represents only:

```text
current responsibility coverage
```

The stable vocabulary is:

### `Satisfied`

The Responsibility is sufficiently covered in the consumer.

This may be achieved through a canonical or non-canonical implementation.

### `Partial`

The Responsibility is only partially covered.

A relevant implementation may exist, but some required coverage is missing.

### `Missing`

The Responsibility is not covered by the observed Evidence.

State does not represent:

```text
future action
applicability
priority
```

---

## 10. Applicability

Applicability indicates whether a Responsibility is relevant to the specific consumer.

The stable vocabulary is:

### `Applicable`

The Responsibility is relevant to the consumer.

### `Not Applicable`

The Responsibility is not needed in the evaluated context.

### `Uncertain`

There is insufficient Evidence or context to determine applicability yet.

Applicability must be evaluated independently from State.

For example:

```text
State
    Missing

Applicability
    Not Applicable

Decision
    OMIT
```

is a valid outcome.

---

## 11. Implementation Characteristics

Implementation Characteristics permite describir implementaciones no canónicas cuando esta información ayuda a interpretar correctamente una Responsibility.

El vocabulario provisional observado durante Discovery es:

```text
Canonical
Own
Equivalent
Specialized
Distributed
```

Este vocabulario es:

```text
provisional
descriptive
non-exclusive
```

Una Responsibility puede presentar:

```text
zero
one
or several
```

Implementation Characteristics.

Estas categorías ayudan a describir cómo está materializada una Responsibility, especialmente cuando la implementación difiere de la materialización canónica esperada por el Repository Template.

No constituyen una taxonomía cerrada ni un contrato de conformance.

Por tanto:

```text
Implementation Characteristic
    supports interpretation
```

pero no determina por sí sola:

```text
State
Applicability
Adoption Decision
```

La Evidence y el Evaluation Rationale deben conservar el contexto necesario para interpretar cualquier Implementation Characteristic utilizada.

---

## 12. Evaluación de Documentación

La presencia física de documentación no demuestra por sí sola que una Responsibility esté satisfecha.

Debe mantenerse la regla:

```text
Documentation Exists
    ≠
Responsibility Satisfied
```

Según la Responsibility, la evaluación puede requerir revisar:

```text
presence
correctness
coverage
current relevance
```

Un archivo existente pero incorrecto, incompleto u obsoleto puede producir un State distinto de `Satisfied`.

---

## 13. Uncertainty

Uncertainty debe registrar, cuando corresponda:

```text
what is unknown
why it cannot currently be resolved
what evidence would resolve it
```

No se utilizan:

```text
confidence score
probability
Low / Medium / High
```

La incertidumbre debe expresarse mediante información concreta y revisable.

---

## 14. Evaluation Rationale

Evaluation Rationale responde:

> ¿Por qué la Evidence observada conduce al State, Applicability e interpretación registrados?

Debe explicar la evaluación sin anticipar la acción futura.

Por tanto:

```text
Evaluation Rationale
    explains the assessment
```

mientras:

```text
Decision Rationale
    explains the adoption decision
```

Ambos conceptos deben permanecer separados.

---

## 15. Decision Status

Decision Status indica si una Adoption Decision puede cerrarse en el momento del assessment.

El vocabulario estable es:

### `Resolved`

Existe evidencia y contexto suficiente para registrar una Adoption Decision.

### `Needs Further Evaluation`

La decisión no puede cerrarse de forma segura con la información disponible.

Decision Status:

```text
is not
an Adoption Decision
```

Cuando una Responsibility requiere evaluación adicional, deben conservarse:

```text
Evidence
Uncertainty
Evaluation Rationale
reason for unresolved decision
```

sin forzar una Adoption Decision ficticia.

---

## 16. Adoption Decisions

El vocabulario estable de Adoption Decision es:

```text
PRESERVE
ADAPT
ADD
ACCEPT
OMIT
```

### `PRESERVE`

Mantener la implementación existente porque satisface adecuadamente la Responsibility y no requiere modificación para el propósito evaluado.

### `ADAPT`

Modificar una implementación existente para cubrir adecuadamente la Responsibility.

### `ADD`

Añadir una implementación o artifact necesario porque la Responsibility requiere cobertura adicional.

### `ACCEPT`

Aceptar conscientemente una implementación existente no canónica cuando resulta adecuada para la Responsibility y el contexto.

### `OMIT`

No incorporar la materialización esperada porque la Responsibility no resulta aplicable o existe una razón explícita y revisada para omitirla.

---

## 17. No existe mapeo automático State → Decision

Una misma combinación de State y Applicability puede conducir a distintas decisiones según:

```text
Requirement Level
Implementation Characteristics
Evidence
Context
Rationale
```

Por tanto:

```text
State
    +
Requirement Level
    +
Applicability
    +
Implementation Characteristics
    +
Evidence
    +
Context
    +
Rationale
        ↓
Adoption Decision
```

No deben aplicarse reglas automáticas como:

```text
Satisfied → PRESERVE

Partial → ADAPT

Missing → ADD
```

sin evaluación contextual.

---

## 18. `EVALUATE`

`EVALUATE` no forma parte del vocabulario estable de Adoption Decision.

La necesidad que anteriormente representaba se expresa mediante:

```text
Decision Status
    Needs Further Evaluation
```

Esto permite conservar una Responsibility evaluada sin inventar una disposición final.

---

## 19. `JUSTIFY`

`JUSTIFY` tampoco forma parte del vocabulario estable de Adoption Decision.

La necesidad de conservar justificación queda cubierta mediante:

```text
Evaluation Rationale
+
Decision Rationale
```

No se requiere una decisión adicional para representar que una conclusión necesita estar razonada.

---

## 20. Decision Rationale

Decision Rationale responde:

> ¿Por qué esta Adoption Decision es apropiada dado el assessment?

Debe relacionar la decisión con:

```text
State
Applicability
Implementation Characteristics
Evidence
context
```

sin convertir esas dimensiones en reglas automáticas.

Ejemplos válidos:

```text
Satisfied
+
Equivalent
+
ACCEPT
```

y:

```text
Missing
+
Not Applicable
+
OMIT
```

---

## 21. Assessment Completion

Un assessment puede marcarse:

```text
Complete
```

cuando todas las Responsibilities definidas por el Repository Template seleccionado hayan sido evaluadas.

Cada Responsibility debe disponer de:

```text
State
Applicability
Evidence
Evaluation Rationale
Decision Status
```

Cuando:

```text
Decision Status
    Resolved
```

deben existir además:

```text
Adoption Decision
Decision Rationale
```

Cuando:

```text
Decision Status
    Needs Further Evaluation
```

deben existir:

```text
Uncertainty
rationale explaining
why the decision remains unresolved
```

---

## 22. Complete no significa Fully Resolved

Debe mantenerse:

```text
Assessment Complete
    ≠
All Adoption Decisions Resolved
```

Un assessment puede estar completo aunque contenga Responsibilities con:

```text
Needs Further Evaluation
```

si la incertidumbre y el motivo de la decisión no resuelta están correctamente documentados.

`Complete` describe que el assessment ha recorrido todas las Responsibilities previstas.

No certifica que todas las decisiones estén cerradas.

---

## 23. Human Review

Existing Repository Adoption Assessment registra una evaluación humana trazable.

No constituye:

```text
automated certification
```

La revisión debe comprobar especialmente:

- suficiencia de Evidence;
- coherencia entre Evidence y State;
- independencia entre State y Applicability;
- reconocimiento de implementaciones equivalentes o distribuidas;
- incertidumbre no resuelta;
- coherencia entre evaluación y Adoption Decision;
- suficiencia de Evaluation Rationale y Decision Rationale.

Una validación futura podrá asistir en comprobaciones deterministas, pero no sustituye la revisión semántica definida por este Assessment Core.

---

## 24. Uso del Assessment Template

El artifact reutilizable para registrar el assessment es:

```text
framework/adoption/assessment-template.md
```

La relación entre ambos artifacts es:

```text
Guide
    explains
        how and why

Template
    records
        what was assessed
```

Flujo recomendado:

```text
1. Copy the Assessment Template
        ↓
2. Complete Assessment Context
        ↓
3. ANALYZE each Responsibility
        ↓
4. ASSESS State and Applicability
        ↓
5. REVIEW Evidence and interpretation
        ↓
6. DECIDE or mark Needs Further Evaluation
        ↓
7. Complete the Assessment Conclusion
        ↓
8. Preserve the assessment as the reviewable outcome
```

El Framework no impone en este delivery:

```text
consumer storage path
mandatory completed-assessment filename
```

---

## 25. Resultado Persistente

El assessment completado debe conservar suficiente contexto para ser interpretado posteriormente.

Como mínimo debe poder identificarse:

```text
Consumer Repository
Consumer Reference
Repository Template
Template Version
Assessment Date
Assessment Status
```

El resultado persistente documenta:

```text
what was observed
how it was evaluated
what remains uncertain
what decisions were made
why those decisions were made
```

---

## 25.1 Application Core

El Application Core reutilizable se documenta en:

```text
framework/adoption/application/README.md
```

El artifact para registrar una Application concreta es:

```text
framework/adoption/application/application-template.md
```

La relación entre ambos cores es:

```text
Assessment Core
    understands and decides
        ↓
optional Application Core
    plans, applies in isolation and verifies
```

Application consume una Adoption Decision con:

```text
Decision Status
    Resolved
```

y conserva como principios:

```text
Evidence before Mutation
Reconciliation over Replacement
Responsibility over Artifact
Bounded Change
Preservation
Human Review
No Mutation is a Valid Outcome
```

El Application Core soporta:

```text
CREATE
MODIFY
NO CHANGE
REPLAN
DEFER
REJECTED
```

y Verification Results:

```text
PASS
REFINE
FAIL
```

---


## 25.2 Integration Core

El Integration Core reutilizable se documenta en:

```text
framework/adoption/integration/README.md
```

El artifact para registrar una Integration concreta es:

```text
framework/adoption/integration/integration-template.md
```

La relación entre las tres capabilities es:

```text
Assessment Core
    understands and decides
        ↓
optional Application Core
    plans, applies in isolation and verifies
        ↓
optional Integration Core
    accepts into stable state and verifies
```

Integration consume:

```text
verified candidate state
```

y conserva como principios:

```text
Verified Candidate before Integration
Refresh Stable Base
Evaluate Drift Impact
Consumer Governance over Framework Merge Preference
Mergeability is not Integration Readiness
Human Review before Stable Integration
Verify Stable State after Integration
Represent Recovery without Automating it
```

El Integration Core soporta decisiones:

```text
INTEGRATE
DEFER
REPLAN
REJECT
```

y final states:

```text
INTEGRATED
DEFERRED
REPLAN REQUIRED
REJECTED
RECOVERY REQUIRED
```

La capability no configura la governance del consumer, no prescribe una merge strategy universal y no automatiza recovery.


## 25.3 Assisted Analysis Core

El Assisted Analysis Core reutilizable se documenta en:

```text
framework/adoption/assisted-analysis/README.md
```

El artifact para registrar una Evidence Snapshot concreta es:

```text
framework/adoption/assisted-analysis/evidence-snapshot-template.md
```

Assisted Analysis no es una cuarta fase del lifecycle.

Su relación con Existing Repository Adoption es transversal:

```text
                 Assisted Analysis
                 ┌──────┼──────┐
                 ↓      ↓      ↓
Assessment    Application    Integration
```

Puede apoyar:

```text
Assessment
    Detected Facts + Evidence

Application
    Evidence Refresh

Integration
    Stable Base Refresh Evidence
    Integration-condition Evidence
```

Conserva como principios:

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

La representación reusable es:

```text
Structured Markdown Evidence Snapshot
```

Assisted Analysis no produce automáticamente:

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

Tampoco introduce CLI, GitHub Actions, consumer mutation, Schema, Manifest, Componentization ni Framework Validator extension.


## 26. Out of Scope

Existing Repository Adoption no documenta ni implementa procedimientos estables para:

```text
automatic merge
automatic remediation
automatic semantic assessment
automatic Adoption Decisions
automatic semantic conflict resolution

DELETE
MOVE
RENAME

component installation

CLI
parser
schema
Structured Data contract
Adoption Manifest

Framework Validator integration
GitHub Actions integration

repository generation

continuous reassessment
drift detection

automatic post-integration rollback
```

Tampoco convierte Existing Repository Adoption en una nueva Component family.

Este delivery no requiere:

```text
metadata.yml
Component Catalog integration
mandatory metadata contract
```

Las capacidades excluidas podrán volver a Discovery si aparece evidencia suficiente que justifique su incorporación.

---

## 27. Límites de Interpretación

Existing Repository Adoption Assessment debe evitar las siguientes inferencias automáticas:

```text
file exists
    ⇒
Responsibility Satisfied
```

```text
canonical file missing
    ⇒
Responsibility Missing
```

```text
State
    ⇒
Adoption Decision
```

```text
assessment complete
    ⇒
all decisions resolved
```

```text
assessment result
    ⇒
automatic conformance certification
```

Cada conclusión debe permanecer respaldada por Evidence y rationale explícitos.

---

## 28. Resumen Operativo

El Assessment Core puede resumirse como:

```text
Existing Consumer Repository
        +
Repository Template
        ↓
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
Persistent Human-Reviewed Assessment
```

La secuencia conceptual por Responsibility es:

```text
Detected Facts
        ↓
Evidence
        ↓
State
+
Applicability
+
Implementation Characteristics
+
Uncertainty
        ↓
Evaluation Rationale
        ↓
Decision Status
        ↓
Adoption Decision
        ↓
Decision Rationale
```

cuando la decisión puede resolverse.

Si no puede resolverse:

```text
Decision Status
    Needs Further Evaluation

+
Uncertainty

+
Rationale
```

sin forzar una Adoption Decision.

---

## 29. Referencias

La definición y planificación del Assessment Core se encuentran en:

```text
docs/discovery/29_ADOPTION_DELIVERY_SCOPE.md
docs/implementation/30_ADOPTION_IMPLEMENTATION_PLAN.md
```

La definición y planificación del Application Core se encuentran en:

```text
docs/discovery/35_APPLICATION_DELIVERY_SCOPE.md
docs/discovery/36_APPLICATION_IMPLEMENTATION_PLAN.md
```

La definición y planificación del Integration Core se encuentran en:

```text
docs/discovery/41_INTEGRATION_DELIVERY_SCOPE.md
docs/discovery/42_INTEGRATION_IMPLEMENTATION_PLAN.md
```

La definición y planificación del Assisted Analysis Core se encuentran en:

```text
docs/discovery/50_ASSISTED_ANALYSIS_DELIVERY_SCOPE.md
docs/implementation/51_ASSISTED_ANALYSIS_IMPLEMENTATION_PLAN.md
```

La evidencia experimental que fundamenta esta capability permanece en:

```text
docs/discovery/
```

Los artifacts reutilizables de Existing Repository Adoption se integran en:

```text
framework/adoption/
```
