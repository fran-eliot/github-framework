# GitHub Framework Roadmap

Este roadmap describe la evolución prevista del proyecto.

Las versiones podrán ajustarse conforme evolucione el Framework.

---

# v0.2.0 — Open Source Readiness

**Estado:** ✅ Released

## Objetivos

* README oficial del Framework.
* LICENSE.
* Documentación de gobierno.
* Preparación de `.github/`.
* Consolidación de la estructura del repositorio.

---

# v0.3.0 — Documentation Framework

**Estado:** ✅ Released

## Objetivos

* Documentation Component Architecture.
* Core Documentation Components.
* Documentation Reference Implementation.
* Documentation Writing Standards.
* Validación mediante dogfooding.

---

# v0.4.0 — Repository Templates

**Estado:** ✅ Released

## Objetivos

* Repository Template Architecture.
* Core Repository Templates.
* Repository Template Reference Implementation.
* Repository Template Standards.
* Validación mediante dogfooding.

---

# v0.5.0 — Workflow Framework

**Estado:** ✅ Released

## Objetivos

* Definir la Workflow Component Architecture.
* Implementar los Core Workflow Components.
* Validar los Core Workflow Components mediante Reference Implementation y dogfooding.
* Consolidar los Workflow Component Standards.
* Preparar una primera Workflow Component Library reutilizable.

---

# v0.6.0 — Framework Automation

**Estado:** ✅ Released

## Objetivo

Introducir capacidades de automatización deterministas sobre el modelo de componentes de GitHub Framework, partiendo de un contrato de metadata común y validando el propio Framework mediante sus herramientas.

## Alcance

### Component Metadata Standard

* Definir un contrato común de metadata para los Framework Components implementados.
* Establecer un núcleo compartido entre las familias README, Documentation y Workflow.
* Preservar extensiones específicas de cada familia.
* Normalizar la representación de valores comunes sin alterar su semántica.

### Component Metadata Normalization

* Migrar los componentes implementados al contrato común de metadata.
* Eliminar diferencias estructurales innecesarias entre formatos existentes.
* Preservar estados de lifecycle, prioridades y semántica específica de cada componente.
* Validar la normalización antes de construir tooling sobre ella.

### Framework Validator

* Descubrir los componentes implementados desde `framework/components/`.
* Validar metadata mediante reglas deterministas.
* Aplicar reglas comunes y reglas específicas por familia.
* Validar estructura física y artefactos declarados.
* Detectar identificadores duplicados, referencias inválidas e inconsistencias estructurales.
* Producir resultados legibles y códigos de salida deterministas.

### Automation Reference Implementation

* Ejecutar el Framework Validator sobre el propio repositorio GitHub Framework.
* Validar mediante dogfooding el contrato de metadata normalizado.
* Proporcionar un punto de entrada CLI mínimo para la validación.
* Documentar los patrones de automatización demostrados y sus límites.

## Fuera de alcance

* Generadores de componentes o repositorios.
* Reescritura automática de documentación libre.
* Publicación automática de releases.
* Orquestación compleja mediante GitHub Actions.
* Bots o mantenimiento autónomo de repositorios.
* Sistemas de plugins o plataformas extensibles de reglas.
* Interfaces gráficas o servicios de automatización.
* Automatización de decisiones arquitectónicas o de diseño.

## Principio de la Release

> Automation follows demonstrated architecture: normalize established contracts first, then automate deterministic operations over them.

---

## Resultado — Sprint 8

**Estado:** Completed.

Las cuatro historias previstas para `v0.6.0` fueron implementadas y cerradas:

| Issue | Entregable                          | Estado |
| ----- | ----------------------------------- | ------ |
| #23   | Component Metadata Standard         | Done   |
| #24   | Component Metadata Normalization    | Done   |
| #25   | Framework Validator                 | Done   |
| #26   | Automation Reference Implementation | Done   |

### Evidencias de validación

* Los 21 Components implementados fueron normalizados y validados.
* El Framework Validator dispone de reglas deterministas para el Common Core, la identidad, la unicidad, la madurez, las dependencias y las extensiones Workflow.
* El CLI proporciona informes legibles y códigos de salida `0` y `1`.
* La batería completa de 109 tests finalizó correctamente.
* La Automation Reference Implementation fue validada mediante dogfooding sobre GitHub Framework.

La implementación de referencia y sus limitaciones están documentadas en `docs/implementation/22_AUTOMATION_REFERENCE_IMPLEMENTATION.md`.

### Integración y publicación

* Framework Automation se integró en `main` mediante el Pull Request #27.
* La documentación de release se integró mediante el Pull Request #28.
* El tag `v0.6.0` fue creado y publicado.
* `v0.6.0 — Framework Automation` fue publicada como GitHub Release.
* La milestone `v0.6.0 — Framework Automation` fue cerrada.
* Las ramas de trabajo de Sprint 8 fueron eliminadas tras verificar su integración.

La release `v0.6.0` cerró Sprint 8 y fue la versión publicada del Framework hasta la publicación de `v0.7.0`.

---

# v0.7.0 — Existing Repository Adoption

**Estado:** ✅ Released

## Objetivo

Introducir la primera capability reusable de **Existing Repository Adoption** mediante un Assessment Core manual, trazable y human-reviewed que permita reconciliar repositorios existentes con las Responsibilities definidas por los Repository Templates sin sustituir automáticamente sus implementaciones.

## Alcance

La release está limitada al **Existing Repository Adoption — Assessment Core**.

El proceso soportado es:

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

El delivery se materializa mediante:

```text
framework/adoption/README.md
    reusable Adoption Guide

framework/adoption/assessment-template.md
    reusable Structured Markdown Assessment Template
```

### Adoption Guide

* Explicar propósito, alcance e inputs del assessment.
* Establecer Responsibility como unidad de evaluación.
* Documentar State, Applicability, Implementation Characteristics y Uncertainty.
* Separar Detected Facts, Evidence, Evaluation Rationale y Adoption Decision.
* Documentar Decision Status y Decision Rationale.
* Explicar completion rules y human review.
* Mantener explícitos los límites del Assessment Core.

### Assessment Template

* Proporcionar una representación Markdown reutilizable y human-editable.
* Incluir Assessment Context, Assessment Summary, Responsibility Details y Assessment Conclusion.
* Permitir registrar Requirement Level, State, Applicability, Implementation Characteristics y Uncertainty.
* Permitir registrar Detected Facts, Evidence, Evaluation Rationale, Decision Status, Adoption Decision y Decision Rationale.
* Mantener la representación libre de schema, parser o Structured Data obligatorio.

### Verification and Integration

* Validar conjuntamente Guide y Template.
* Ejecutar representative replay sobre casos ya observados durante Discovery.
* Verificar consistencia semántica y cumplimiento de AC-01 a AC-35.
* Confirmar que no se introduce capability fuera del Delivery Scope.
* Integrar la capability reusable bajo `framework/adoption/`.
* Mantener la evidencia histórica y experimental bajo `docs/discovery/`.
* Sincronizar la documentación general y governance necesaria.

## Vocabulario estable

### Responsibility State

```text
Satisfied
Partial
Missing
```

### Applicability

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

### Adoption Decision

```text
PRESERVE
ADAPT
ADD
ACCEPT
OMIT
```

`EVALUATE` no forma parte del stable Adoption Decision vocabulary.

`JUSTIFY` tampoco constituye una Adoption Decision independiente.

La justificación permanece representada mediante:

```text
Evaluation Rationale
+
Decision Rationale
```

Implementation Characteristics permanece como vocabulario provisional y descriptivo.

## Fuera de alcance

La release no incluye:

* `APPLY`;
* `VERIFY`;
* repository transformation;
* automatic remediation;
* automatic semantic assessment;
* automatic Adoption Decisions;
* CLI;
* parser;
* schema;
* Structured Data contract;
* Adoption Manifest;
* Framework Validator integration;
* GitHub Actions integration;
* continuous reassessment;
* drift detection;
* Repository Generator;
* nueva Component family;
* mandatory metadata contract;
* consumer storage standard;
* completed assessment filename standard.

Estas capacidades podrán evaluarse en incrementos posteriores únicamente si existe evidencia suficiente.

## Principio de la Release

> Reconciliation before automation: assess existing repositories through explicit evidence and human review before introducing repository modification or automated decisions.

---

## Sprint 9 — Existing Repository Adoption

**Estado:** Completed.

Milestone:

```text
v0.7.0 — Existing Repository Adoption
```

Issues comprometidas:

| Issue | Entregable                                                    | Estado |
| ----- | ------------------------------------------------------------- | :----: |
| #40   | Existing Repository Adoption Guide                            |  Done  |
| #41   | Existing Repository Adoption Assessment Template              |  Done  |
| #42   | Existing Repository Adoption Assessment Core Verification     |  Done  |

Dependencias:

```text
#40 ───────┐
           ├──► #42
#41 ───────┘
```

Secuencia recomendada:

```text
#40 Adoption Guide
        ↓
#41 Assessment Template
        ↓
#42 Verification and Integration
```

El Sprint está respaldado por:

* `docs/discovery/29_ADOPTION_DELIVERY_SCOPE.md`;
* `docs/implementation/30_ADOPTION_IMPLEMENTATION_PLAN.md`;
* `docs/implementation/31_ADOPTION_CORE_VERIFICATION.md`.

Estado funcional actual:

```text
#40 Adoption Guide
    DONE

#41 Assessment Template
    DONE

#42 Verification and Integration
    DONE

Assessment Core
    IMPLEMENTED
    VERIFIED
    INTEGRATED
```

El representative replay y la revisión semántica confirman:

```text
Representative Replay
    PASS

Guide / Template Consistency
    PASS

Scope Compliance
    PASS

AC-01 through AC-35
    PASS
```

Sprint 9 ha completado su alcance funcional. El tag `v0.7.0` y la GitHub Release `v0.7.0 — Existing Repository Adoption` han sido publicados.

La apertura de Sprint 9 no amplía la frontera funcional definida por esos documentos.

La milestone `v0.7.0 — Existing Repository Adoption` se cierra tras completar las Issues #40–#42 y publicar la release.

---

# v0.8.0 — Existing Repository Adoption Application Core

**Estado:** ✅ Released

## Objetivo

Extender Existing Repository Adoption con un **Application Core** manual, bounded, human-reviewed y verificable que permita llevar una Adoption Decision resuelta hasta un candidate state verificado sin introducir automatización prematura.

## Alcance

Proceso objetivo:

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

Reusable artifacts previstos:

```text
framework/adoption/application/README.md
framework/adoption/application/application-template.md
```

Integración mínima:

```text
framework/adoption/README.md
```

Verification artifact previsto:

```text
docs/implementation/37_APPLICATION_CORE_VERIFICATION.md
```

## Sprint 10

Issues comprometidas:

| Issue | Entregable                                                  | Estado |
| ----- | ----------------------------------------------------------- | :----: |
| #50   | Existing Repository Adoption Application Guide             |  Done  |
| #51   | Existing Repository Adoption Application Template          |  Done  |
| #52   | Existing Repository Adoption Application Core Verification |  Done  |

Dependencia:

```text
#50 ───────┐
           ├──► #52
#51 ───────┘
```

## Resultado — Sprint 10

```text
Application Guide
    IMPLEMENTED

Application Template
    IMPLEMENTED

Application Core Verification
    PASS

AC-01 through AC-77
    PASS

Representative Replay
    PASS

Application Core
    IMPLEMENTED
    VERIFIED
    INTEGRATED
```

La versión `v0.8.0 — Existing Repository Adoption Application Core` ha sido publicada.

## Fuera de alcance

- `INTEGRATE`;
- automatic remediation;
- automatic conflict resolution;
- CLI y GitHub Actions para Application;
- Structured Data, schema o manifest;
- `DELETE / MOVE / RENAME`;
- post-integration rollback.

## Evidencia

El incremento está respaldado por:

- `32_APPLICATION_DISCOVERY.md`;
- `33_APPLICATION_DISCOVERY_SYNTHESIS.md`;
- `34_APPLICATION_REPEATABILITY_EXPERIMENT.md`;
- `35_APPLICATION_DELIVERY_SCOPE.md`;
- `36_APPLICATION_IMPLEMENTATION_PLAN.md`.

---

# v0.9.0 — Existing Repository Adoption Integration Core

**Estado:** ✅ Released

## Objetivo

Extender Existing Repository Adoption con un **Integration Core** manual, governance-aware, human-reviewed y verificable que permita llevar un verified candidate state hasta stable consumer state.

## Alcance

Proceso objetivo:

```text
Verified Candidate
    ↓
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

Reusable artifacts previstos:

```text
framework/adoption/integration/README.md
framework/adoption/integration/integration-template.md
```

Integración mínima:

```text
framework/adoption/README.md
```

Verification artifact previsto:

```text
docs/implementation/43_INTEGRATION_CORE_VERIFICATION.md
```

## Sprint 11

Issues comprometidas:

| Issue | Entregable                                                   | Estado |
| ----- | ------------------------------------------------------------ | :----: |
| #61   | Existing Repository Adoption Integration Guide              |  Done  |
| #62   | Existing Repository Adoption Integration Template           |  Done  |
| #63   | Existing Repository Adoption Integration Core Verification  |  Done  |

Dependencia:

```text
#61 ───────┐
           ├──► #63
#62 ───────┘
```

## Resultado — Sprint 11

```text
Integration Guide
    IMPLEMENTED

Integration Template
    IMPLEMENTED

Root Adoption Integration
    IMPLEMENTED

Integration Core Verification
    PASS

AC-01 through AC-73
    PASS

Replay A
    PASS

Replay B
    PASS

Integration Core
    IMPLEMENTED
    VERIFIED
    INTEGRATED
```

La versión `v0.9.0 — Existing Repository Adoption Integration Core` ha sido publicada.

La milestone `v0.9.0 — Existing Repository Adoption Integration Core` se cierra tras completar las Issues #61–#63 y publicar la release.

## Evidencia

El incremento está respaldado por:

- `38_INTEGRATION_DISCOVERY.md`;
- `39_INTEGRATION_DISCOVERY_SYNTHESIS.md`;
- `40_INTEGRATION_REPEATABILITY_EXPERIMENT.md`;
- `41_INTEGRATION_DELIVERY_SCOPE.md`;
- `42_INTEGRATION_IMPLEMENTATION_PLAN.md`.

## Fuera de alcance

- automatic merge;
- automatic approval;
- automatic conflict resolution;
- automatic rollback;
- release orchestration;
- branch protection configuration;
- CLI / GitHub Actions;
- Structured Data, Schema o Manifest.

---

# v0.10.0 — Existing Repository Adoption Assisted Analysis Core

**Estado:** 🟠 In Progress

## Objetivo

Introducir una capability reusable de **Assisted Analysis** para recopilar Evidence determinista, bounded, source-traceable y read-only que pueda reutilizarse en Assessment, Application e Integration sin automatizar evaluación semántica ni decisiones.

## Alcance

Reusable artifacts previstos:

```text
framework/adoption/assisted-analysis/README.md
framework/adoption/assisted-analysis/evidence-snapshot-template.md
```

Integración mínima:

```text
framework/adoption/README.md
```

Verification artifact previsto:

```text
docs/implementation/52_ASSISTED_ANALYSIS_CORE_VERIFICATION.md
```

Principios del incremento:

```text
Facts before Evaluation
Evidence before Decision
Read-Only before Mutation
Source Traceability
Human Review owns Semantic Meaning
Representation before Tooling
```

## Sprint 12

Issues comprometidas:

| Issue | Entregable | Estado |
| ----- | ---------- | :----: |
| #78 | Existing Repository Adoption Assisted Analysis Guide | Open |
| #79 | Existing Repository Adoption Evidence Snapshot Template | Open |
| #80 | Existing Repository Adoption Assisted Analysis Core Verification | Open |

Dependencia:

```text
#78 ───────┐
           ├──► #80
#79 ───────┘
```

## Evidencia

El incremento está respaldado por:

- `44_ASSISTED_ANALYSIS_DISCOVERY.md`;
- `45_ASSISTED_ANALYSIS_EXPERIMENT_A.md`;
- `46_ASSISTED_ANALYSIS_EXPERIMENT_B.md`;
- `47_ASSISTED_ANALYSIS_EXPERIMENT_C.md`;
- `48_ASSISTED_ANALYSIS_DISCOVERY_SYNTHESIS.md`;
- `49_ASSISTED_ANALYSIS_REPEATABILITY_EXPERIMENT.md`;
- `50_ASSISTED_ANALYSIS_DELIVERY_SCOPE.md`;
- `51_ASSISTED_ANALYSIS_IMPLEMENTATION_PLAN.md`.

## Fuera de alcance

- CLI / repository scanner executable;
- GitHub Actions / continuous reassessment;
- Structured Data, Schema o Manifest;
- automatic Assessment, Application or Integration decisions;
- consumer mutation;
- automatic PR creation, merge, rollback or recovery;
- Componentization;
- Framework Validator extension.

---

# v1.0.0 — Stable Release

**Estado:** ⚪ Planned

## Objetivos

* Framework completamente funcional.
* Generación consistente de repositorios.
* Biblioteca estable de componentes.
* Documentación consolidada.
* Primera versión estable del Framework.

---

# Visión

GitHub Framework aspira a convertirse en un marco de referencia para diseñar, documentar y mantener repositorios profesionales mediante estándares de ingeniería, componentes reutilizables y una arquitectura consistente.

---

# Principios del Roadmap

El roadmap representa la dirección prevista del proyecto.

Las versiones podrán cambiar conforme evolucionen las necesidades del Framework.

Las prioridades vendrán determinadas por el Product Backlog.
