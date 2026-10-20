# 14 - PRODUCT BACKLOG

| Campo                    | Valor            |
| ------------------------ | ---------------- |
| **Proyecto**             | GitHub Framework |
| **Versión publicada**    | v0.6.0           |
| **Versión objetivo**     | Por definir      |
| **Estado**               | Activo           |
| **Última actualización** | 2026-10-20       |

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

El siguiente Sprint solo se definirá después de completar y revisar el Delivery Scope del próximo incremento funcional del Framework.

---

## Product Backlog

No existen todavía historias funcionales comprometidas para el siguiente incremento.

Discovery ha identificado un único candidate con evidencia suficiente para avanzar a **Delivery Scope Definition**:

```text
Existing Repository Adoption
    Assessment Core
```

Esto no constituye todavía una historia priorizada, Sprint commitment, milestone ni versión objetivo.

Las capacidades diferidas permanecen fuera del Product Backlog comprometido hasta que exista evidencia específica que justifique su promoción.

---

## Discovery Actual

La investigación de Existing Repository Adoption ha completado:

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
```

La Discovery Synthesis consolida la evidencia de los documentos:

- `23_BACKEND_ADOPTION_DISCOVERY.md`;
- `24_ADOPTION_MODEL_DISCOVERY.md`;
- `25_MANUAL_ADOPTION_ASSESSMENT_DISCOVERY.md`;
- `26_ADOPTION_SOLUTION_SHAPING_DISCOVERY.md`;
- `27_ADOPTION_REPEATABILITY_EXPERIMENT.md`;
- `28_ADOPTION_DISCOVERY_SYNTHESIS.md`.

El resultado del Repeatability Experiment fue:

```text
MODEL HOLDS
```

La representación:

```text
Minimal Adoption Guide
    +
Structured Markdown Assessment
        including
            Summary Table
            Responsibility Detail
```

pudo reutilizarse sobre un consumer adicional sin rediseño material, tooling obligatorio ni workarounds.

La Discovery Synthesis evaluó:

- Core Model Findings;
- los 15 Requirement Candidates;
- las 11 Solution Hypotheses;
- los refinamientos pendientes;
- la frontera entre Assessment y Application;
- Delivery Readiness del núcleo mínimo.

El resultado es:

```text
Existing Repository Adoption
    Assessment Core
        READY FOR DELIVERY SCOPE DEFINITION
```

El núcleo respaldado corresponde a:

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

Las Solution Hypotheses con soporte suficiente para conformar un candidate mínimo son:

```text
SH-01 Manual Adoption Guide
        +
SH-02 Adoption Checklist / Assessment
        +
SH-04 Adoption Report
        as outcome of the assessment
        +
SH-11 Staged Adoption Process
        limited to assessment stages
```

Esto converge en una única capability candidate y no en cuatro entregables separados.

Se mantienen como refinamientos explícitos y no bloqueantes:

- semántica de `EVALUATE`;
- papel independiente de `JUSTIFY`;
- vocabulario exacto de Implementation Characteristics.

Quedan diferidos:

- `APPLY` / `VERIFY`;
- Assisted Repository Analyzer;
- Adoption Manifest;
- Framework Validator Extension;
- Adoption CLI;
- Selective Component Application;
- GitHub Actions Integration;
- Structured Data;
- generated report tooling;
- continuous reassessment.

`Repository Generator` continúa siendo una hipótesis de baja adecuación para Existing Repository Adoption, aunque podría tener sentido futuro en el escenario distinto de Initialization.

La siguiente etapa es:

```text
Delivery Scope Definition
```

y deberá responder:

> ¿Cuál es el Delivery Scope mínimo del Existing Repository Adoption Assessment Core y cómo debe integrarse en GitHub Framework sin formalizar prematuramente las capacidades diferidas?

Todavía no existe:

- Sprint activo;
- milestone del siguiente incremento;
- versión objetivo;
- Delivery Scope aprobado;
- Implementation Architecture seleccionada.

---

## Roadmap Alignment

| Milestone                        |                    Estado                   |
| -------------------------------- | :-----------------------------------------: |
| v0.3.0 — Documentation Framework |                  ✅ Released                 |
| v0.4.0 — Repository Templates    |                  ✅ Released                 |
| v0.5.0 — Workflow Framework      |                  ✅ Released                 |
| v0.6.0 — Framework Automation    |                  ✅ Released                 |
| v1.0.0 — Stable Release          |                  ⚪ Planned                  |

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

---

# Definition of Ready

Una tarea podrá incorporarse a un Sprint cuando:

* exista una necesidad real;
* tenga un objetivo claro;
* pueda completarse dentro del Sprint;
* aporte valor al Framework.

---

# Historial

| Versión | Fecha      | Descripción                                                                                                                     |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| v0.1.0  | 2026-08-07 | Primera versión del Product Backlog.                                                                                            |
| v0.2.0  | 2026-08-09 | Planificación Sprint 5 y reorganización del Product Backlog.                                                                    |
| v0.2.1  | 2026-08-11 | Cierre funcional de Sprint 5 y actualización del Product Backlog.                                                               |
| v0.3.0  | 2026-08-13 | Publicación de Documentation Framework y cierre de Sprint 5.                                                                    |
| v0.4.0  | 2026-08-13 | Planificación de Sprint 6 y adopción de GitHub Issue IDs para el trabajo nuevo.                                                 |
| v0.4.1  | 2026-08-18 | Cierre funcional de Sprint 6 y actualización del estado de Repository Templates.                                                |
| v0.4.2  | 2026-08-18 | Cierre de Sprint 6 y preparación de la release v0.4.0.                                                                          |
| v0.5.0  | 2026-08-19 | Planificación de Sprint 7 — Workflow Framework.                                                                                 |
| v0.5.1  | 2026-09-14 | Cierre funcional del alcance de Sprint 7 y actualización del Product Backlog tras completar Workflow Component Standards.       |
| v0.5.2  | 2026-09-14 | Cierre de Sprint 7 y preparación final de la release v0.5.0.                                                                    |
| v0.5.3  | 2026-09-17 | Definición del alcance de v0.6.0 — Framework Automation tras la fase de discovery.                                              |
| v0.5.4  | 2026-09-17 | Apertura de Sprint 8 — Framework Automation y asignación de las Issues #23–#26.                                                 |
| v0.5.5  | 2026-09-21 | Cierre funcional de Sprint 8: cuatro historias completadas, 109 tests superados y Automation Reference Implementation validada. |
| v0.5.6  | 2026-09-21 | Integración de Framework Automation en `main` mediante el PR #27 y preparación documental de la release v0.6.0. |
| v0.6.0  | 2026-09-25 | Publicación de Framework Automation, cierre de Sprint 8 y transición del Product Backlog al discovery del siguiente incremento. |
| v0.6.1 | 2026-10-04 | Actualización del Product Backlog tras Existing Repository Adoption Discovery y transición a Solution Shaping Discovery. |
| v0.6.2 | 2026-10-18 | Solution Shaping identifica una representación mínima candidata y mantiene el trabajo en Discovery pendiente de validación de repetibilidad. |
| v0.6.3 | 2026-10-19 | Repeatability Experiment completa un assessment de 28 Responsibilities con `MODEL HOLDS` y mueve Existing Repository Adoption hacia Discovery Synthesis. |
| v0.6.4 | 2026-10-20 | Discovery Synthesis consolida el Assessment Core y lo declara listo para Delivery Scope Definition, sin abrir todavía Sprint, milestone ni versión objetivo. |
