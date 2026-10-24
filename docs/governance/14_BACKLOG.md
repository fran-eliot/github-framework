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

El siguiente Sprint solo se definirá después de completar la planificación del incremento:

```text id="h1a7os"
Existing Repository Adoption
    Assessment Core
```

---

## Product Backlog

No existen todavía historias funcionales comprometidas para el siguiente incremento.

Existe una capability con Discovery y Delivery Scope completados:

```text id="rqmio8"
Existing Repository Adoption
    Assessment Core
```

Su estado es:

```text id="2l5geq"
READY FOR IMPLEMENTATION PLANNING
```

Esto significa que existe suficiente definición para:

```text id="98um83"
implementation task decomposition
issue creation
dependency analysis
Sprint suitability assessment
milestone evaluation
target version evaluation
```

pero no implica todavía:

```text id="j9kvsy"
Sprint commitment
milestone commitment
release commitment
implementation started
```

La planificación deberá respetar estrictamente el alcance definido en:

```text id="8kbq0o"
docs/discovery/29_ADOPTION_DELIVERY_SCOPE.md
```

---

## Existing Repository Adoption — Assessment Core

El Delivery Scope define un incremento mínimo compuesto por dos reusable artifacts:

```text id="meu8dn"
framework/adoption/README.md
    reusable Adoption Guide

framework/adoption/assessment-template.md
    reusable Structured Markdown Assessment Template
```

El proceso respaldado es:

```text id="kk3vwj"
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

```text id="1t06yr"
manual
human-readable
human-editable
human-reviewed
non-destructive
low-coupling
```

### Stable Responsibility State

```text id="nx4ut4"
Satisfied
Partial
Missing
```

### Stable Applicability

```text id="3abns3"
Applicable
Not Applicable
Uncertain
```

### Decision Status

```text id="q71kqp"
Resolved
Needs Further Evaluation
```

### Stable Adoption Decisions

```text id="emr3zu"
PRESERVE
ADAPT
ADD
ACCEPT
OMIT
```

`EVALUATE` no forma parte del stable Adoption Decision vocabulary del delivery.

La necesidad de evaluación adicional se representa mediante:

```text id="wy9x4p"
Decision Status
    Needs Further Evaluation
```

`JUSTIFY` tampoco forma parte del stable Adoption Decision vocabulary.

La justificación se conserva mediante:

```text id="gv2f8t"
Evaluation Rationale
+
Decision Rationale
```

Implementation Characteristics permanece como vocabulario provisional y descriptivo.

---

## Delivery Scope Completed

La secuencia de investigación y definición ha completado:

```text id="7r9vq1"
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
```

La documentación principal es:

- `23_BACKEND_ADOPTION_DISCOVERY.md`;
- `24_ADOPTION_MODEL_DISCOVERY.md`;
- `25_MANUAL_ADOPTION_ASSESSMENT_DISCOVERY.md`;
- `26_ADOPTION_SOLUTION_SHAPING_DISCOVERY.md`;
- `27_ADOPTION_REPEATABILITY_EXPERIMENT.md`;
- `28_ADOPTION_DISCOVERY_SYNTHESIS.md`;
- `29_ADOPTION_DELIVERY_SCOPE.md`.

La Discovery Synthesis concluyó:

```text id="7kzida"
Existing Repository Adoption
    Assessment Core
        READY FOR DELIVERY SCOPE DEFINITION
```

El Delivery Scope posterior concluyó:

```text id="4mgdad"
Existing Repository Adoption
    Assessment Core

Delivery Scope
    DEFINED

Next Step
    Implementation Planning
```

---

## In-Scope Capability

El incremento incluye:

```text id="f7xsrk"
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

```text id="t0mdpd"
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

```text id="dl6h3x"
Reusable Framework Capability
        +
Discovery Evidence
```

La capability reusable se integrará en:

```text id="0f5xv4"
framework/adoption/
```

La evidencia histórica permanece en:

```text id="p5e6fa"
docs/discovery/
```

No se requiere:

```text id="xov3uv"
new Component family
Component metadata
Component Catalog update
Framework Validator integration
```

para completar el primer delivery.

---

## Candidate Implementation Units

El Delivery Scope sugiere tres unidades naturales de planificación.

### Unit A — Adoption Guide

Objetivo:

```text id="p4zkkm"
implement reusable guidance
```

Artifact principal:

```text id="ms37k9"
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

---

### Unit B — Assessment Template

Objetivo:

```text id="cw72ut"
implement reusable Markdown assessment template
```

Artifact principal:

```text id="jk5e0u"
framework/adoption/assessment-template.md
```

Debe incluir como mínimo:

```text id="c0rtrv"
Assessment Context
Assessment Summary
Responsibility Details
Assessment Conclusion
```

y permitir registrar:

```text id="dk0bk9"
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

---

### Unit C — Verification and Integration

Objetivo:

```text id="dm8j9f"
validate final reusable artifacts
against existing evidence
```

Debe incluir:

```text id="1d6vxm"
representative replay
scope compliance review
Guide / Template consistency review
Framework documentation integration
governance synchronization
```

El representative replay debe cubrir al menos:

```text id="tzf8er"
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

---

## Planning Boundary

Implementation Planning podrá convertir las unidades anteriores en Issues concretas.

La planificación deberá evaluar:

```text id="rv0zkq"
task boundaries
dependencies
sequencing
review points
estimated effort
Sprint suitability
```

sin rediseñar el Delivery Scope.

La regla de control será:

```text id="rawa0r"
If a planned task introduces
a capability currently Out of Scope

then
    scope review is required
before implementation
```

---

## Candidate Dependency Flow

La dependencia natural candidata es:

```text id="t5eq3e"
Adoption Guide
        ↘
          Verification and Integration
        ↗
Assessment Template
```

Guide y Template pueden desarrollarse parcialmente en paralelo porque comparten semántica, pero deben revisarse conjuntamente para evitar semantic drift.

La unidad de Verification and Integration depende de que ambos artifacts dispongan de una versión suficientemente completa.

---

## Planning Questions

Implementation Planning deberá responder:

1. ¿Deben Unit A, Unit B y Unit C convertirse directamente en tres GitHub Issues?
2. ¿Necesitan subdivisión adicional para mantener cada Issue pequeña y verificable?
3. ¿Qué dependencias reales existen entre Guide y Template?
4. ¿Cuál es el esfuerzo estimado de cada unidad?
5. ¿Puede completarse el incremento en un único Sprint?
6. ¿Qué milestone representa correctamente el incremento?
7. ¿Existe evidencia suficiente para asignar una target version?
8. ¿Qué Acceptance Criteria del Delivery Scope corresponden a cada Issue?
9. ¿Qué cambios de documentación general del Framework deben acompañar la implementación?
10. ¿Qué validación final debe completarse antes de considerar el incremento Done?

---

## Deferred Capabilities

Las capacidades excluidas no se consideran rechazadas permanentemente.

### Application

```text id="pd8xvt"
APPLY
VERIFY
Selective Component Application
```

requieren Application Discovery.

### Assisted Analysis

```text id="imsp3m"
repository scanning
deterministic evidence collection
```

requieren evidencia de necesidad operacional.

### Automation

```text id="u31ywj"
CLI
GitHub Actions
continuous reassessment
```

requieren evidencia suficiente para justificar automatización.

### Formal Representation

```text id="demlu0"
Structured Data
Schema
Manifest
```

requieren una necesidad real de procesamiento machine-readable.

### Componentization

La promoción futura de Adoption artifacts a Components requiere evidencia de que:

```text id="8lksgo"
Component contracts
metadata
catalog integration
validator integration
```

aportan valor proporcional.

---

## Roadmap Alignment

| Milestone                        | Estado     |
| -------------------------------- | :--------: |
| v0.3.0 — Documentation Framework | ✅ Released |
| v0.4.0 — Repository Templates    | ✅ Released |
| v0.5.0 — Workflow Framework      | ✅ Released |
| v0.6.0 — Framework Automation    | ✅ Released |
| v1.0.0 — Stable Release          | ⚪ Planned  |

No se añade todavía una nueva milestone al Roadmap.

La definición del Delivery Scope no implica por sí sola un compromiso de release.

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

```text id="8pbt5r"
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
