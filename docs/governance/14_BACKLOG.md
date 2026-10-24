# 14 - PRODUCT BACKLOG

| Campo                    | Valor            |
| ------------------------ | ---------------- |
| **Proyecto**             | GitHub Framework |
| **Versión publicada**    | v0.6.0           |
| **Versión objetivo**     | Por definir      |
| **Estado**               | Activo           |
| **Última actualización** | 2026-10-24       |

---

# Objetivo

Este documento recoge el Product Backlog del proyecto.

Su finalidad es priorizar el trabajo pendiente y servir como referencia para la planificación de futuros Sprints.

El backlog está vivo y evolucionará conforme madure el Framework.

---

## Historias Completadas

| ID     | Historia                                     | Versión | Estado |
| ------ | -------------------------------------------- | ------- | ------ |
| GF-001 | Complete Framework README                    | v0.2.0  | Done   |
| GF-002 | Add Project License                          | v0.2.0  | Done   |
| GF-003 | Prepare GitHub Community Files               | v0.2.0  | Done   |
| GF-004 | Create CONTRIBUTING Guide                    | v0.2.0  | Done   |
| GF-005 | Documentation Component Architecture         | v0.3.0  | Done   |
| GF-006 | Core Documentation Components                | v0.3.0  | Done   |
| GF-007 | Documentation Reference Implementation       | v0.3.0  | Done   |
| GF-008 | Documentation Writing Standards              | v0.3.0  | Done   |
| #11    | Repository Template Architecture             | v0.4.0  | Done   |
| #12    | Core Repository Templates                    | v0.4.0  | Done   |
| #13    | Repository Template Reference Implementation | v0.4.0  | Done   |
| #14    | Repository Template Standards                | v0.4.0  | Done   |
| #17    | Workflow Component Architecture              | v0.5.0  | Done   |
| #18    | Core Workflow Components                     | v0.5.0  | Done   |
| #19    | Workflow Reference Implementation            | v0.5.0  | Done   |
| #20    | Workflow Component Standards                 | v0.5.0  | Done   |
| #23    | Component Metadata Standard                  | v0.6.0  | Done   |
| #24    | Component Metadata Normalization             | v0.6.0  | Done   |
| #25    | Framework Validator                          | v0.6.0  | Done   |
| #26    | Automation Reference Implementation          | v0.6.0  | Done   |

Las historias de `v0.6.0` están implementadas, integradas y publicadas como parte de Framework Automation.

---

## Sprint Actual

No existe actualmente un Sprint activo.

Sprint 8 — Framework Automation finalizó con la publicación de `v0.6.0`.

La milestone `v0.6.0 — Framework Automation` está cerrada y las cuatro historias previstas (#23–#26) están completadas.

La planificación del siguiente incremento:

```text
Existing Repository Adoption
    Assessment Core
```

ya está definida.

El siguiente Sprint solo se abrirá después de:

```text
crear las tres Issues de implementación
        ↓
asignar Acceptance Criteria
        ↓
definir la milestone
        ↓
seleccionar la versión objetivo
```

---

## Product Backlog

No existen todavía historias funcionales creadas y comprometidas para el siguiente incremento.

Existe una capability con Discovery, Delivery Scope e Implementation Planning completados:

```text
Existing Repository Adoption
    Assessment Core
```

Su estado es:

```text
IMPLEMENTATION PLANNING
    DEFINED
```

La planificación se documenta en:

```text
docs/implementation/30_ADOPTION_IMPLEMENTATION_PLAN.md
```

y define:

```text
3 implementation units
3 GitHub Issues
dependency flow
Acceptance Criteria allocation
relative effort
single-Sprint suitability
Definition of Ready
Definition of Done
```

Esto significa que existe suficiente definición para:

```text
formal Issue creation
milestone definition
target version evaluation
Sprint opening
```

pero todavía no implica:

```text
Sprint commitment
milestone commitment
release commitment
implementation started
```

La implementación deberá respetar estrictamente el alcance definido en:

```text
docs/discovery/29_ADOPTION_DELIVERY_SCOPE.md
```

y la descomposición definida en:

```text
docs/implementation/30_ADOPTION_IMPLEMENTATION_PLAN.md
```

---

## Existing Repository Adoption — Assessment Core

El Delivery Scope define un incremento mínimo compuesto por dos reusable artifacts:

```text
framework/adoption/README.md
    reusable Adoption Guide

framework/adoption/assessment-template.md
    reusable Structured Markdown Assessment Template
```

El proceso respaldado es:

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

La capability debe permanecer:

```text
manual
human-readable
human-editable
human-reviewed
non-destructive
low-coupling
```

### Stable Responsibility State

```text
Satisfied
Partial
Missing
```

### Stable Applicability

```text
Applicable
Not Applicable
Uncertain
```

### Decision Status

```text
Resolved
Needs Further Evaluation
```

### Stable Adoption Decisions

```text
PRESERVE
ADAPT
ADD
ACCEPT
OMIT
```

`EVALUATE` no forma parte del stable Adoption Decision vocabulary del delivery.

La necesidad de evaluación adicional se representa mediante:

```text
Decision Status
    Needs Further Evaluation
```

`JUSTIFY` tampoco forma parte del stable Adoption Decision vocabulary.

La justificación se conserva mediante:

```text
Evaluation Rationale
+
Decision Rationale
```

Implementation Characteristics permanece como vocabulario provisional y descriptivo.

---

## Delivery Scope and Implementation Planning Completed

La secuencia de investigación, definición y planificación ha completado:

```text
Problem Discovery
        ↓
Adoption Model Discovery
        ↓
Manual Adoption Assessment
        ↓
Solution Shaping
        ↓
Repeatability Experiment
        ↓
Discovery Synthesis
        ↓
Delivery Scope Definition
        ↓
Implementation Planning
```

La documentación principal es:

- `23_BACKEND_ADOPTION_DISCOVERY.md`;
- `24_ADOPTION_MODEL_DISCOVERY.md`;
- `25_MANUAL_ADOPTION_ASSESSMENT_DISCOVERY.md`;
- `26_ADOPTION_SOLUTION_SHAPING_DISCOVERY.md`;
- `27_ADOPTION_REPEATABILITY_EXPERIMENT.md`;
- `28_ADOPTION_DISCOVERY_SYNTHESIS.md`;
- `29_ADOPTION_DELIVERY_SCOPE.md`;
- `30_ADOPTION_IMPLEMENTATION_PLAN.md`.

La Discovery Synthesis concluyó:

```text
Existing Repository Adoption
    Assessment Core
        READY FOR DELIVERY SCOPE DEFINITION
```

El Delivery Scope posterior concluyó:

```text
Existing Repository Adoption
    Assessment Core

Delivery Scope
    DEFINED
```

El Implementation Plan concluye:

```text
Existing Repository Adoption
    Assessment Core

Implementation Planning
    DEFINED

Implementation Units
    3

Issue Decomposition
    DEFINED

Dependencies
    DEFINED

Acceptance Criteria Allocation
    DEFINED

Single-Sprint Suitability
    SUPPORTED
```

---

## In-Scope Capability

El incremento incluye:

```text
Adoption Guide

Assessment Template

Assessment Context

Summary Table

Responsibility Detail

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

Assessment Status

Assessment Conclusion

Human Review

Persistent Markdown Outcome
```

---

## Out-of-Scope Capability

El incremento excluye expresamente:

```text
APPLY
VERIFY

repository transformation

automatic remediation

automatic semantic assessment

automatic adoption decisions

CLI

parser

schema

Structured Data

Adoption Manifest

Framework Validator integration

GitHub Actions integration

continuous reassessment

drift detection

Repository Generator

new Component family

mandatory metadata contract

consumer storage standard

completed assessment filename standard
```

Estas capacidades no deben aparecer incidentalmente en las Issues de implementación salvo revisión explícita del Delivery Scope.

---

## Integration Model

El modelo seleccionado es híbrido:

```text
Reusable Framework Capability
        +
Discovery Evidence
```

La capability reusable se integrará en:

```text
framework/adoption/
```

La evidencia histórica permanece en:

```text
docs/discovery/
```

No se requiere:

```text
new Component family
Component metadata
Component Catalog update
Framework Validator integration
```

para completar el primer delivery.

---

## Planned Implementation Units

El Implementation Plan define tres unidades de trabajo.

### Unit A — Adoption Guide

Objetivo:

```text
implement reusable guidance
```

Artifact principal:

```text
framework/adoption/README.md
```

Responsabilidad:

- explicar propósito y alcance;
- documentar inputs;
- documentar el assessment model;
- describir `ANALYZE → ASSESS → REVIEW → DECIDE → REPORT`;
- explicar State, Applicability, Decision Status y Adoption Decision;
- documentar Evidence, Uncertainty y Rationales;
- establecer completion rules;
- dejar explícito el Out of Scope;
- explicar cómo utilizar el Assessment Template.

Esfuerzo relativo:

```text
Medium
```

Issue prevista:

```text
Implement Existing Repository Adoption Guide
```

---

### Unit B — Assessment Template

Objetivo:

```text
implement reusable Markdown assessment template
```

Artifact principal:

```text
framework/adoption/assessment-template.md
```

Debe incluir como mínimo:

```text
Assessment Context
Assessment Summary
Responsibility Details
Assessment Conclusion
```

y permitir registrar:

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

Esfuerzo relativo:

```text
Small / Medium
```

Issue prevista:

```text
Implement Existing Repository Adoption Assessment Template
```

---

### Unit C — Verification and Integration

Objetivo:

```text
validate final reusable artifacts
against existing evidence
```

Debe incluir:

```text
representative replay
scope compliance review
Guide / Template consistency review
Framework documentation integration
governance synchronization
```

El representative replay debe cubrir al menos:

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

Esta unidad no constituye un nuevo Discovery experiment.

Esfuerzo relativo:

```text
Small
```

Issue prevista:

```text
Validate and integrate Existing Repository Adoption Assessment Core
```

---

## Implementation Dependency Flow

La dependencia definida es:

```text
Adoption Guide ───────┐
                      ├──► Verification and Integration
Assessment Template ──┘
```

Unit C depende de A y B.

Guide y Template pueden desarrollarse parcialmente en paralelo, pero deben revisarse conjuntamente para evitar semantic drift.

El orden recomendado para el flujo actual del proyecto es:

```text
Unit A
    ↓
Unit B
    ↓
Unit C
```

La secuencia responde a:

```text
define semantics
    ↓
encode structure
    ↓
verify both
```

---

## Issue Decomposition Decision

Las tres unidades se consideran suficientemente independientes y verificables para convertirse directamente en:

```text
3 Implementation Units
    =
3 GitHub Issues
```

No se recomienda subdivisión adicional.

La planificación prevista es:

```text
Issue A
    Implement Existing Repository Adoption Guide

Issue B
    Implement Existing Repository Adoption Assessment Template

Issue C
    Validate and integrate Existing Repository Adoption Assessment Core
```

Dependencias:

```text
Issue A ───────┐
               ├──► Issue C
Issue B ───────┘
```

---

## Acceptance Criteria Allocation

### Issue A — Adoption Guide

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

### Issue B — Assessment Template

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

### Issue C — Verification and Integration

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

Esta asignación representa primary implementation ownership y no exclusive semantic ownership.

---

## Sprint Suitability

El incremento incluye:

```text
2 reusable Markdown artifacts
+
1 verification / integration unit
```

y no incorpora:

```text
code
schema
CLI
validator
workflow
consumer mutation
```

Por tanto:

```text
Existing Repository Adoption
    Assessment Core

SUITABLE FOR A SINGLE SPRINT
```

La viabilidad en un único Sprint está respaldada por tamaño, cohesión y dependencias.

Esto no significa todavía que exista un Sprint abierto.

---

## Release Planning Pending

Implementation Planning ya ha respondido las preguntas de descomposición, dependencias, esfuerzo y Sprint suitability.

Permanecen pendientes únicamente:

```text
formal Issue creation
        ↓
milestone definition
        ↓
target version evaluation
        ↓
Sprint opening
```

No se seleccionará una versión únicamente por ser el siguiente número disponible.

La target version deberá reflejar:

```text
delivered capability
+
release significance
+
Roadmap coherence
```

---

## Deferred Capabilities

Las capacidades excluidas no se consideran rechazadas permanentemente.

### Application

```text
APPLY
VERIFY
Selective Component Application
```

requieren Application Discovery.

### Assisted Analysis

```text
repository scanning
deterministic evidence collection
```

requieren evidencia de necesidad operacional.

### Automation

```text
CLI
GitHub Actions
continuous reassessment
```

requieren evidencia suficiente para justificar automatización.

### Formal Representation

```text
Structured Data
Schema
Manifest
```

requieren una necesidad real de procesamiento machine-readable.

### Componentization

La promoción futura de Adoption artifacts a Components requiere evidencia de que:

```text
Component contracts
metadata
catalog integration
validator integration
```

aportan valor proporcional.

---

## Roadmap Alignment

| Milestone                        | Estado      |
| -------------------------------- | :---------: |
| v0.3.0 — Documentation Framework | ✅ Released |
| v0.4.0 — Repository Templates    | ✅ Released |
| v0.5.0 — Workflow Framework      | ✅ Released |
| v0.6.0 — Framework Automation    | ✅ Released |
| v1.0.0 — Stable Release          | ⚪ Planned  |

No se añade todavía una nueva milestone al Roadmap.

Implementation Planning no implica por sí solo un compromiso de release.

---

# Icebox

Ideas identificadas pero no priorizadas.

* Generador de componentes.
* Generador de repositorios.
* Integración con GitHub Actions.
* Plantillas específicas por lenguaje.
* Generación de diagramas.
* Marketplace de componentes.

Su presencia en el Icebox no supone un compromiso de implementación ni su asignación automática al siguiente Sprint.

---

# Priorización

Las prioridades se revisarán al comienzo de cada Sprint.

No se desarrollarán funcionalidades sin un caso de uso real.

El próximo incremento deberá mantener como restricción principal:

```text
no additional capability
without explicit scope review
```

---

# Definition of Ready

Una tarea podrá incorporarse a un Sprint cuando:

* exista una necesidad real;
* tenga un objetivo claro;
* esté vinculada al Delivery Scope aprobado;
* tenga Acceptance Criteria verificables;
* tenga dependencias conocidas;
* pueda completarse dentro del Sprint;
* aporte valor al Framework;
* no introduzca capabilities Out of Scope sin revisión explícita.

Para el Assessment Core, cada una de las tres Issues deberá además cumplir las condiciones específicas definidas en `30_ADOPTION_IMPLEMENTATION_PLAN.md`.

---

# Definition of Done — Assessment Core

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

# Historial

| Versión | Fecha       | Descripción |
| ------- | ----------- | ----------- |
| v0.1.0  | 2026-08-07  | Primera versión del Product Backlog. |
| v0.2.0  | 2026-08-09  | Planificación Sprint 5 y reorganización del Product Backlog. |
| v0.2.1  | 2026-08-11  | Cierre funcional de Sprint 5 y actualización del Product Backlog. |
| v0.3.0  | 2026-08-13  | Publicación de Documentation Framework y cierre de Sprint 5. |
| v0.4.0  | 2026-08-13  | Planificación de Sprint 6 y adopción de GitHub Issue IDs para el trabajo nuevo. |
| v0.4.1  | 2026-08-18  | Cierre funcional de Sprint 6 y actualización del estado de Repository Templates. |
| v0.4.2  | 2026-08-18  | Cierre de Sprint 6 y preparación de la release v0.4.0. |
| v0.5.0  | 2026-08-19  | Planificación de Sprint 7 — Workflow Framework. |
| v0.5.1  | 2026-09-14  | Cierre funcional del alcance de Sprint 7 y actualización del Product Backlog tras completar Workflow Component Standards. |
| v0.5.2  | 2026-09-14  | Cierre de Sprint 7 y preparación final de la release v0.5.0. |
| v0.5.3  | 2026-09-17  | Definición del alcance de v0.6.0 — Framework Automation tras la fase de discovery. |
| v0.5.4  | 2026-09-17  | Apertura de Sprint 8 — Framework Automation y asignación de las Issues #23–#26. |
| v0.5.5  | 2026-09-21  | Cierre funcional de Sprint 8: cuatro historias completadas, 109 tests superados y Automation Reference Implementation validada. |
| v0.5.6  | 2026-09-21  | Integración de Framework Automation en `main` mediante el PR #27 y preparación documental de la release v0.6.0. |
| v0.6.0  | 2026-09-25  | Publicación de Framework Automation, cierre de Sprint 8 y transición del Product Backlog al discovery del siguiente incremento. |
| v0.6.1  | 2026-10-04  | Actualización del Product Backlog tras Existing Repository Adoption Discovery y transición a Solution Shaping Discovery. |
| v0.6.2  | 2026-10-18  | Solution Shaping identifica una representación mínima candidata y mantiene el trabajo en Discovery pendiente de validación de repetibilidad. |
| v0.6.3  | 2026-10-19  | Repeatability Experiment completa un assessment de 28 Responsibilities con `MODEL HOLDS` y mueve Existing Repository Adoption hacia Discovery Synthesis. |
| v0.6.4  | 2026-10-20  | Discovery Synthesis consolida el Assessment Core y lo declara listo para Delivery Scope Definition, sin abrir todavía Sprint, milestone ni versión objetivo. |
| v0.6.5  | 2026-10-24  | Delivery Scope Definition completa el alcance del Assessment Core y lo declara listo para Implementation Planning, sin abrir todavía Sprint, milestone ni versión objetivo. |
| v0.6.6  | 2026-10-24  | Implementation Planning define tres Issues, dependencias, Acceptance Criteria, esfuerzo relativo y viabilidad en un único Sprint; milestone, target version y apertura del Sprint permanecen pendientes. |
