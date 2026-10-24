# 30 — Adoption Implementation Plan

| Field | Value |
|---|---|
| **Project** | GitHub Framework |
| **Capability** | Existing Repository Adoption — Assessment Core |
| **Phase** | Implementation Planning |
| **Delivery Scope** | Defined |
| **Status** | Proposed |
| **Sprint** | Not yet assigned |
| **Milestone** | Not yet assigned |
| **Target Version** | Not yet assigned |

---

## 1. Propósito

Este documento transforma el Delivery Scope definido en:

```text
docs/discovery/29_ADOPTION_DELIVERY_SCOPE.md
```

en un plan de implementación ejecutable para:

```text
Existing Repository Adoption
    Assessment Core
```

El objetivo ya no es determinar:

```text
what capability should exist
```

sino:

```text
how the approved capability
should be implemented
through bounded work units
```

sin ampliar su frontera funcional.

---

## 2. Planning Input

Implementation Planning parte de un Delivery Scope ya cerrado.

El delivery aprobado consiste en dos reusable artifacts:

```text
framework/adoption/README.md

framework/adoption/assessment-template.md
```

que soportan:

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

y mantienen el proceso:

```text
manual
human-readable
human-editable
human-reviewed
non-destructive
low-coupling
```

---

## 3. Planning Boundary

Implementation Planning puede decidir:

```text
implementation units
issue decomposition
dependencies
sequencing
review points
effort
Sprint suitability
milestone suitability
target version suitability
```

pero no puede modificar implícitamente:

```text
capability boundary
artifact count
assessment process
automation boundary
application boundary
componentization boundary
```

La regla de control es:

```text
no additional capability
without explicit scope review
```

---

## 4. Confirmed Physical Integration

La estructura actual del repositorio contiene:

```text
framework/
    components/
    templates/
```

Existing Repository Adoption no pertenece actualmente a:

```text
Component family
```

ni a:

```text
Repository Template family
```

Por tanto, el namespace definido durante Delivery Scope:

```text
framework/adoption/
```

se considera coherente con la estructura real del Framework.

La forma física prevista es:

```text
framework/
└── adoption/
    ├── README.md
    └── assessment-template.md
```

---

## 5. Why Adoption Remains Outside Components

El primer delivery debe proporcionar una capability reusable.

Eso no implica:

```text
Reusable Artifact
    =
Component
```

La promoción inmediata a:

```text
framework/components/adoption/
```

introduciría:

```text
Component family
metadata contract
Catalog integration
Validator implications
```

sin evidencia suficiente.

Por tanto:

```text
Componentization
    Deferred
```

continúa siendo una restricción activa de implementación.

---

## 6. Implementation Units

El trabajo se descompone en tres unidades.

```text
Unit A
    Adoption Guide

Unit B
    Assessment Template

Unit C
    Verification and Integration
```

Las unidades A y B producen los artifacts del capability.

Unit C valida ambos conjuntamente y completa su integración dentro del Framework.

---

# Unit A — Adoption Guide

## 7. Objective

Implementar:

```text
framework/adoption/README.md
```

como Guidance oficial y reusable para Existing Repository Adoption Assessment.

---

## 8. Primary Responsibility

La Guide debe responder:

> ¿Cómo debe una persona ejecutar correctamente Existing Repository Adoption Assessment?

Debe explicar:

```text
how
+
why
```

mientras el Assessment Template se limita principalmente a:

```text
what to record
```

---

## 9. Required Guide Scope

La Guide debe cubrir como mínimo:

```text
Purpose
Scope
Inputs
Core Principles
Assessment Unit
Assessment Model
Assessment Process
Evidence Rules
Evaluation Rules
Applicability Rules
Non-Canonical Implementation Handling
Uncertainty Handling
Decision Status
Adoption Decision Rules
Evaluation Rationale
Decision Rationale
Assessment Completion
Human Review
Out of Scope
Using the Assessment Template
```

---

## 10. Assessment Inputs

La Guide debe establecer como inputs conceptuales:

```text
Existing Consumer Repository

Repository Template

Repository Template Version

Consumer Reference
```

El Repository Template actúa como:

```text
assessment baseline
```

y el consumer como:

```text
evidence source
```

---

## 11. Assessment Unit

La Guide debe declarar explícitamente:

```text
Assessment Unit
    Responsibility
```

y no:

```text
Assessment Unit
    File
```

Por tanto:

```text
Canonical Artifact Missing
    ≠
Responsibility Missing
```

---

## 12. Assessment Process

La Guide debe documentar:

### ANALYZE

Identificar:

```text
Detected Facts
Evidence
```

sin realizar todavía una decisión de adopción.

### ASSESS

Evaluar:

```text
State
Applicability
Implementation Characteristics
Uncertainty
Evaluation Rationale
```

### REVIEW

Revisar:

```text
evidence sufficiency
semantic interpretation
non-canonical implementations
uncertainty
applicability
```

### DECIDE

Registrar:

```text
Decision Status
Adoption Decision
Decision Rationale
```

### REPORT

Conservar el assessment como:

```text
persistent Markdown outcome
```

---

## 13. Stable State Vocabulary

La Guide debe documentar:

```text
Satisfied
Partial
Missing
```

State representa:

```text
current responsibility coverage
```

y no:

```text
future action
applicability
priority
```

---

## 14. Stable Applicability Vocabulary

La Guide debe documentar:

```text
Applicable
Not Applicable
Uncertain
```

Applicability debe permanecer independiente de State.

Por ejemplo:

```text
State
    Missing

Applicability
    Not Applicable

Decision
    OMIT
```

es un resultado válido.

---

## 15. Implementation Characteristics

La Guide debe permitir describir:

```text
Canonical
Own
Equivalent
Specialized
Distributed
```

como vocabulario:

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

La Guide no debe presentar esta taxonomía como contrato definitivo.

---

## 16. Documentation Evaluation Rule

La Guide debe mantener:

```text
Documentation Exists
    ≠
Responsibility Satisfied
```

La evaluación podrá requerir:

```text
presence
correctness
coverage
current relevance
```

según la Responsibility.

---

## 17. Uncertainty

La Guide debe explicar cómo registrar:

```text
what is unknown
why it cannot currently be resolved
what evidence would resolve it
```

No se introduce:

```text
confidence score
probability
Low / Medium / High
```

---

## 18. Evaluation Rationale

Debe explicar:

> ¿Por qué la Evidence observada conduce al State, Applicability e interpretación registrados?

Debe permanecer separado de:

```text
Decision Rationale
```

---

## 19. Decision Status

La Guide debe definir:

```text
Resolved

Needs Further Evaluation
```

Decision Status describe:

```text
whether an Adoption Decision
can currently be closed
```

No representa una Adoption Decision.

---

## 20. Stable Adoption Decisions

La Guide debe documentar exclusivamente:

```text
PRESERVE
ADAPT
ADD
ACCEPT
OMIT
```

No incluye:

```text
EVALUATE
JUSTIFY
```

como Adoption Decisions estables.

---

## 21. EVALUATE Replacement

Cuando una decisión no puede cerrarse de forma segura:

```text
Decision Status
    Needs Further Evaluation
```

debe permitir conservar:

```text
Evidence
Uncertainty
Evaluation Rationale
reason for unresolved decision
```

sin forzar una Adoption Decision ficticia.

---

## 22. JUSTIFY Handling

`JUSTIFY` no se implementará como Adoption Decision.

La justificación debe quedar representada mediante:

```text
Evaluation Rationale
+
Decision Rationale
```

---

## 23. Decision Rationale

Decision Rationale responde:

> ¿Por qué esta Adoption Decision es apropiada dado el assessment?

Debe permitir casos como:

```text
Satisfied
+
Equivalent
+
ACCEPT
```

o:

```text
Missing
+
Not Applicable
+
OMIT
```

sin reglas automáticas.

---

## 24. Completion Rules

Un assessment puede considerarse:

```text
Complete
```

cuando todas las Responsibilities del Template hayan sido evaluadas.

Cada Responsibility debe disponer de:

```text
State
Applicability
Evidence
Evaluation Rationale
Decision Status
```

Si:

```text
Decision Status
    Resolved
```

deberán existir:

```text
Adoption Decision
Decision Rationale
```

Si:

```text
Decision Status
    Needs Further Evaluation
```

deberán existir:

```text
Uncertainty
rationale explaining
why the decision remains unresolved
```

---

## 25. Complete Does Not Mean Fully Resolved

La Guide debe mantener:

```text
Assessment Complete
    ≠
All Adoption Decisions Resolved
```

Un assessment puede ser completo aunque contenga Responsibilities con:

```text
Needs Further Evaluation
```

si la incertidumbre está correctamente documentada.

---

## 26. Guide Out of Scope

La Guide no debe documentar procedimientos de implementación para:

```text
APPLY
VERIFY
repository mutation
automatic remediation
component installation
CLI
schema
manifest
parser
Framework Validator integration
GitHub Actions integration
repository generation
continuous reassessment
drift detection
```

---

# Unit B — Assessment Template

## 27. Objective

Implementar:

```text
framework/adoption/assessment-template.md
```

como estructura Markdown reusable para:

```text
copy
complete
review
preserve
```

un assessment.

---

## 28. Primary Responsibility

El template debe responder:

> ¿Qué información debe registrarse durante Existing Repository Adoption Assessment?

No debe duplicar toda la explicación semántica de la Guide.

---

## 29. Required Template Sections

La estructura mínima será:

```text
Assessment Context

Assessment Summary

Responsibility Details

Assessment Conclusion
```

Los aggregate counts podrán incluirse como bloque opcional.

---

## 30. Assessment Context

Debe permitir registrar:

```text
Consumer Repository
Consumer Reference
Repository Template
Template Version
Assessment Date
Assessment Status
```

---

## 31. Assessment Status

El template debe soportar:

```text
In Progress
Complete
```

No se introduce un lifecycle más amplio.

Por tanto, quedan fuera:

```text
Draft
Reviewed
Approved
Archived
Superseded
```

---

## 32. Assessment Summary

La Summary deberá incluir:

| Field | Requirement |
|---|---|
| Responsibility | Required |
| Requirement Level | Required |
| State | Required |
| Applicability | Required |
| Decision Status | Required |
| Adoption Decision | Required when `Decision Status = Resolved` |

La Summary debe permitir visualizar tanto:

```text
resolved decisions
```

como:

```text
Responsibilities requiring further evaluation
```

---

## 33. Responsibility Detail

Cada Responsibility debe poder registrar:

```text
Responsibility
Requirement Level
State
Applicability
Implementation Characteristics
Uncertainty
Detected Facts
Evidence
Evaluation Rationale
Decision Status
Adoption Decision
Decision Rationale
```

Esta estructura es:

```text
human-readable contract
```

y no:

```text
machine-readable schema
```

---

## 34. Detected Facts

Debe existir espacio para observaciones verificables.

Ejemplos:

```text
README.md exists

docs/ directory absent

OpenAPI configuration exposes documentation

repository-level LICENSE not detected
```

Detected Facts no deben contener evaluación.

---

## 35. Evidence

El template debe permitir referencias suficientes hacia:

```text
file paths
repository sections
configuration
source code
generated documentation
repository structure
```

La expectativa es:

```text
minimal sufficient evidence
```

y no copia extensa del contenido del consumer.

---

## 36. Implementation Characteristics Field

El template debe permitir:

```text
none
one
multiple
```

Implementation Characteristics.

Debe evitar cualquier mecanismo que convierta la taxonomía provisional en schema cerrado.

---

## 37. Unresolved Decision Representation

Cuando:

```text
Decision Status
    Needs Further Evaluation
```

el campo:

```text
Adoption Decision
```

puede permanecer sin valor final.

El template debe permitir explicar por qué.

---

## 38. Assessment Conclusion

La sección final debe permitir registrar:

```text
Assessment Status
Major Findings
Open Uncertainties
Recommended Next Review
```

sin transformarse en:

```text
implementation backlog
```

ni en:

```text
application plan
```

---

## 39. Optional Aggregate Counts

El template puede incluir:

```text
State Totals
Applicability Totals
Decision Totals
```

como información opcional.

Su ausencia no invalida el assessment.

---

## 40. Template Exclusions

No debe incluir:

```text
Observation Log
machine-readable metadata
schema
consumer storage policy
mandatory completed-assessment filename
automatic calculations
automation hooks
```

---

# Unit C — Verification and Integration

## 41. Objective

Verificar conjuntamente:

```text
Adoption Guide
+
Assessment Template
```

contra:

```text
Delivery Scope
+
existing Discovery evidence
```

y completar su integración documental dentro del Framework.

---

## 42. Verification Strategy

La validación se realizará mediante:

```text
artifact inspection
+
representative replay
+
scope compliance review
+
Guide / Template consistency review
```

No requiere:

```text
new consumer
new Discovery experiment
automated behavioral tests
```

---

## 43. Representative Replay

Replay significa:

```text
previously observed case
        ↓
represent using final Guide + Template
        ↓
verify no information loss
```

Debe cubrir al menos:

```text
canonical implementation

equivalent implementation

distributed implementation

partial implementation

missing applicable responsibility

missing non-applicable responsibility

uncertain responsibility

inaccurate documentation
```

---

## 44. Semantic Consistency Review

Debe comprobarse que Guide y Template utilizan de forma consistente:

```text
State
Applicability
Implementation Characteristics
Uncertainty
Evaluation Rationale
Decision Status
Adoption Decision
Decision Rationale
Assessment Status
```

No debe existir vocabulario equivalente con nombres distintos entre ambos artifacts.

---

## 45. Scope Compliance Review

La revisión debe confirmar la ausencia de:

```text
APPLY
VERIFY
repository transformation
automatic remediation
automatic semantic assessment
automatic decisions
CLI
parser
schema
Structured Data
Manifest
Framework Validator integration
GitHub Actions integration
continuous reassessment
drift detection
Repository Generator
new Component family
mandatory metadata
```

---

## 46. Framework Integration Review

La capability deberá resultar localizable dentro de:

```text
framework/adoption/
```

y claramente diferenciada de:

```text
docs/discovery/
```

La documentación histórica continúa en Discovery.

Los artifacts finales constituyen la capability reusable.

---

## 47. Documentation Integration

Unit C deberá determinar si los artifacts requieren enlaces desde documentación general del Framework.

Los candidatos naturales son:

```text
README.md
README_es.md
ROADMAP.md
```

pero su modificación solo deberá realizarse cuando aporte discoverability real.

No debe actualizarse:

```text
Component Catalog
```

porque Adoption no es todavía un Component formal.

---

# Acceptance Criteria Allocation

## 48. Unit A — Adoption Guide

Responsabilidad primaria sobre:

```text
AC-01
AC-02
AC-03
AC-04

AC-12

AC-17
AC-18
AC-19
AC-20

semantic part of AC-35
```

También proporciona semantics necesarias para interpretar correctamente los AC del Template.

---

## 49. Unit B — Assessment Template

Responsabilidad primaria sobre:

```text
AC-05
AC-06
AC-07
AC-08
AC-09
AC-10
AC-11

AC-13
AC-14
AC-15
AC-16

AC-31
AC-33

structural part of AC-35
```

---

## 50. Unit C — Verification and Integration

Responsabilidad primaria sobre:

```text
AC-21
AC-22
AC-23
AC-24
AC-25
AC-26
AC-27
AC-28
AC-29
AC-30

AC-32
AC-34
```

y verificación final de:

```text
AC-01
through
AC-35
```

---

## 51. Acceptance Criteria Ownership Rule

La asignación anterior representa:

```text
primary implementation ownership
```

y no:

```text
exclusive semantic ownership
```

Algunos AC dependen de coherencia entre varias unidades.

Ejemplo:

```text
Evidence
Evaluation
Decision
```

deben estar correctamente explicados en Guide y correctamente representados en Template.

---

# Dependencies

## 52. Dependency Model

La dependencia conceptual es:

```text
Adoption Guide ───────┐
                      ├──► Verification and Integration
Assessment Template ──┘
```

Unit C depende de A y B.

---

## 53. Guide / Template Dependency

Guide y Template comparten semántica.

Sin embargo:

```text
Guide complete
```

no es un requisito técnico absoluto para comenzar Template.

Ambas unidades pueden desarrollarse parcialmente en paralelo.

---

## 54. Recommended Execution Order

Para el flujo actual del proyecto se recomienda:

```text
Unit A
    ↓
Unit B
    ↓
Unit C
```

Motivo:

```text
define semantics
    ↓
encode structure
    ↓
verify both
```

Esto reduce el riesgo de:

```text
template-driven semantics
```

o:

```text
Guide / Template semantic drift
```

---

# Issue Decomposition

## 55. Planning Decision

Las tres unidades se consideran suficientemente independientes y verificables para convertirse directamente en tres GitHub Issues.

No se recomienda una subdivisión adicional.

Por tanto:

```text
3 Implementation Units
    =
3 GitHub Issues
```

---

## 56. Issue A Candidate

### Title

```text
Implement Existing Repository Adoption Guide
```

### Primary Artifact

```text
framework/adoption/README.md
```

### Scope

Implementar la Guidance reusable del Assessment Core conforme al Delivery Scope.

### Dependency

```text
None
```

---

## 57. Issue B Candidate

### Title

```text
Implement Existing Repository Adoption Assessment Template
```

### Primary Artifact

```text
framework/adoption/assessment-template.md
```

### Scope

Implementar la estructura Markdown reusable del assessment conforme a la semántica establecida.

### Dependency

```text
semantic alignment with Issue A
```

Puede comenzar antes de que Issue A esté completamente cerrada, pero su revisión final debe realizarse contra la Guide.

---

## 58. Issue C Candidate

### Title

```text
Validate and integrate Existing Repository Adoption Assessment Core
```

### Scope

```text
representative replay
Guide / Template consistency review
scope compliance
Framework discoverability
governance synchronization
```

### Dependency

```text
Issue A
+
Issue B
```

---

# Effort

## 59. Relative Effort

La estimación relativa inicial es:

| Unit | Relative Effort |
|---|:---:|
| Adoption Guide | Medium |
| Assessment Template | Small / Medium |
| Verification and Integration | Small |

No existe tooling nuevo ni código de producción.

---

## 60. Complexity Drivers

### Adoption Guide

Mayor coste por:

```text
semantic precision
scope explanation
model consistency
decision rules
completion rules
```

### Assessment Template

Mayor coste por:

```text
usability
low duplication
field completeness
clean reusable structure
```

### Verification and Integration

Mayor coste por:

```text
cross-artifact consistency
representative replay
scope compliance
documentation synchronization
```

---

# Sprint Suitability

## 61. Single-Sprint Assessment

El incremento presenta:

```text
2 reusable Markdown artifacts
+
1 verification / integration unit
```

y no incluye:

```text
code
schema
CLI
validator
workflow
consumer mutation
```

Por tanto, el incremento se considera:

```text
SUITABLE FOR A SINGLE SPRINT
```

desde el punto de vista de tamaño y dependencia.

---

## 62. Sprint Decision Boundary

La conclusión anterior significa:

```text
single-Sprint viability
    supported
```

pero todavía no significa:

```text
Sprint opened
```

El Sprint deberá abrirse después de:

```text
Issues created
Acceptance Criteria assigned
milestone selected
target version selected
```

---

# Milestone and Target Version

## 63. Milestone Readiness

El incremento ya dispone de:

```text
bounded scope
defined artifacts
defined implementation units
defined dependencies
defined Acceptance Criteria allocation
single-Sprint suitability
```

Por tanto, después de crear las Issues puede definirse una milestone específica para Existing Repository Adoption Assessment Core.

---

## 64. Target Version Decision Rule

La versión objetivo no debe derivarse únicamente de:

```text
next numeric version
```

Debe reflejar:

```text
delivered capability
+
release significance
+
Roadmap coherence
```

La selección de versión se realizará después de:

```text
Issue creation
+
milestone definition
```

---

## 65. No Automatic Version Promotion

Este planning no selecciona automáticamente:

```text
v0.7.0
```

ni ninguna otra versión.

La versión objetivo permanece:

```text
TO BE DEFINED
```

hasta la decisión posterior de release planning.

---

# Risks

## 66. IP-01 — Semantic Drift

Riesgo:

```text
Guide
    ≠
Template
```

Mitigación:

```text
shared vocabulary
joint review
Unit C verification
```

---

## 67. IP-02 — Scope Expansion

Riesgo:

una Issue introduzca tooling o Application porque parezca técnicamente conveniente.

Mitigación:

```text
every Issue inherits
29_ADOPTION_DELIVERY_SCOPE.md
Out of Scope
```

---

## 68. IP-03 — Premature Componentization

Riesgo:

convertir la capability en nueva Component family durante implementación.

Mitigación:

```text
framework/adoption/
without metadata.yml
without Catalog integration
```

---

## 69. IP-04 — Template Overload

Riesgo:

duplicar toda la Guide dentro del Template.

Mitigación:

```text
Guide explains
Template records
```

---

## 70. IP-05 — False Conformance

Riesgo:

presentar un completed assessment como certificación automática.

Mitigación:

la Guide debe indicar explícitamente:

```text
Assessment
    records human evaluation
```

y no:

```text
automated certification
```

---

# Definition of Ready

## 71. Issue Ready Conditions

Cada Issue podrá incorporarse al Sprint cuando disponga de:

```text
clear objective
bounded artifact or responsibility
Delivery Scope reference
Acceptance Criteria
known dependency
Out-of-Scope boundary
reviewable completion condition
```

---

## 72. Unit A Ready

Unit A se considera ready cuando la Issue:

```text
identifies framework/adoption/README.md
references applicable ACs
includes stable vocabulary
includes Decision Status rules
includes explicit Out of Scope
```

---

## 73. Unit B Ready

Unit B se considera ready cuando la Issue:

```text
identifies assessment-template.md
defines required sections
defines required fields
defines unresolved-decision handling
references applicable ACs
```

---

## 74. Unit C Ready

Unit C se considera ready cuando:

```text
Unit A and Unit B
exist as planned work
```

y la Issue define:

```text
replay cases
scope review
semantic consistency review
integration review
completion criteria
```

---

# Definition of Done

## 75. Increment Done Conditions

Existing Repository Adoption Assessment Core podrá considerarse implementado cuando:

1. exista `framework/adoption/README.md`;
2. exista `framework/adoption/assessment-template.md`;
3. ambos sean coherentes semánticamente;
4. Guide documente el proceso completo;
5. Template represente todos los campos requeridos;
6. `EVALUATE` no sea una Adoption Decision estable;
7. `JUSTIFY` no sea requerido;
8. Decision Status esté implementado;
9. stable vocabulary esté documentado;
10. provisional vocabulary esté identificado como provisional;
11. representative replay confirme suficiencia;
12. los AC-01 a AC-35 aplicables estén satisfechos;
13. no exista capability Out of Scope introducida;
14. documentación general necesaria esté sincronizada;
15. governance refleje correctamente el estado final.

---

# Planning Result

## 76. Implementation Plan Decision

Implementation Planning concluye:

```text
Existing Repository Adoption
    Assessment Core

Implementation Units
    3

Issue A
    Adoption Guide

Issue B
    Assessment Template

Issue C
    Verification and Integration
```

---

## 77. Dependency Decision

```text
Issue A ───────┐
               ├──► Issue C
Issue B ───────┘
```

Orden recomendado de ejecución:

```text
A
↓
B
↓
C
```

---

## 78. Scope Decision

No se modifica el Delivery Scope.

Continúan fuera:

```text
APPLY
VERIFY
automation
Structured Data
Componentization
repository mutation
CLI
schema
manifest
validator integration
GitHub Actions
continuous reassessment
```

---

## 79. Sprint Suitability Decision

El incremento es:

```text
SUITABLE FOR A SINGLE SPRINT
```

por tamaño, cohesión y dependencia.

Esto no abre todavía el Sprint.

---

## 80. Milestone Decision

La capability dispone ya de definición suficiente para crear una milestone después de materializar las tres Issues.

Estado:

```text
READY FOR MILESTONE DEFINITION
```

---

## 81. Target Version Decision

La target version no se selecciona en este documento.

Estado:

```text
READY FOR RELEASE VERSION EVALUATION
```

después de crear las Issues y definir la milestone.

---

## 82. Planning Status

```text
Delivery Scope
    DEFINED

Implementation Planning
    DEFINED

Implementation Units
    DEFINED

Issue Decomposition
    DEFINED

Dependencies
    DEFINED

Acceptance Criteria Allocation
    DEFINED

Single-Sprint Suitability
    SUPPORTED

Sprint
    NOT YET OPEN

Milestone
    NOT YET DEFINED

Target Version
    NOT YET DEFINED

Implementation
    NOT STARTED
```

---

## 83. Next Step

La siguiente etapa es:

```text
Create GitHub Issues
    ↓
assign Acceptance Criteria
    ↓
define milestone
    ↓
evaluate target version
    ↓
open Sprint
    ↓
begin implementation
```

---

## 84. Final Answer

Existing Repository Adoption Assessment Core debe implementarse mediante tres unidades:

```text
A — Adoption Guide

B — Assessment Template

C — Verification and Integration
```

que producen y validan:

```text
framework/adoption/README.md

framework/adoption/assessment-template.md
```

sin ampliar el Delivery Scope.

La descomposición es suficientemente pequeña, verificable y cohesionada para:

```text
3 GitHub Issues
```

y el incremento es adecuado para:

```text
1 Sprint
```

aunque Sprint, milestone y target version permanecen pendientes hasta completar la creación formal de las Issues y el release planning posterior.

Por tanto:

```text
Existing Repository Adoption
    Assessment Core

Implementation Planning
    DEFINED

Next Step
    GitHub Issue Creation
```
