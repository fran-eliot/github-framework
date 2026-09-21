# 14 - PRODUCT BACKLOG

| Campo                    | Valor            |
| ------------------------ | ---------------- |
| **Proyecto**             | GitHub Framework |
| **Versión publicada**    | v0.5.0           |
| **Versión objetivo**     | v0.6.0           |
| **Estado**               | Activo           |
| **Última actualización** | 2026-09-21       |

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

Las historias de `v0.6.0` están implementadas y cerradas. Su inclusión en esta tabla no implica que la versión se haya publicado.

---

## Sprint Actual

### Sprint 8 — Framework Automation

**Milestone:** `v0.6.0 — Framework Automation`

**Estado:** implementación completada e integrada en `main`; publicación de `v0.6.0` pendiente.

**Objetivo**

Introducir capacidades de automatización deterministas sobre el modelo de Components de GitHub Framework, partiendo de un contrato común de metadata, normalizando los Components implementados y validando el propio Framework mediante su primer Framework Validator.

### Resultado funcional

| Issue | Historia                            | Prioridad | Estado |
| ----- | ----------------------------------- | :-------: | :----: |
| #23   | Component Metadata Standard         |    Alta   |  Done  |
| #24   | Component Metadata Normalization    |    Alta   |  Done  |
| #25   | Framework Validator                 |    Alta   |  Done  |
| #26   | Automation Reference Implementation |   Media   |  Done  |

**Evidencias de validación:**

* 21 Components implementados descubiertos y validados.
* 109 tests automatizados superados.
* Framework Validator ejecutado satisfactoriamente sobre el propio repositorio.
* Código de salida `0` en la validación real.
* Pruebas negativas representativas superadas mediante directorios temporales.
* Automation Reference Implementation documentada y validada.

La implementación se integró en `main` mediante el Pull Request #27, con el commit de merge `4b357d8`.

La publicación de `v0.6.0` permanece pendiente. La documentación de release se está preparando en `chore/v0.6.0-post-merge`.

---

## Product Backlog

No existen actualmente historias funcionales priorizadas fuera del alcance completado de Sprint 8.

El siguiente incremento funcional se definirá después de la publicación de `v0.6.0`.

Las actividades de preparación de la release no constituyen nuevas historias funcionales.

---

## Roadmap Alignment

| Milestone                        |                    Estado                   |
| -------------------------------- | :-----------------------------------------: |
| v0.3.0 — Documentation Framework |                  ✅ Released                 |
| v0.4.0 — Repository Templates    |                  ✅ Released                 |
| v0.5.0 — Workflow Framework      |                  ✅ Released                 |
| v0.6.0 — Framework Automation    | ⏳ Integrated into main; release pending |
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
