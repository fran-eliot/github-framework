# 12 - PROJECT STATUS

| Campo                    | Valor                                      |
| ------------------------ | ------------------------------------------ |
| **Proyecto**             | GitHub Framework                           |
| **Versión actual**       | v0.6.0                                     |
| **Estado**               | En desarrollo                              |
| **Fase**                 | Solution Shaping Discovery — Existing Repository Adoption         |
| **Sprint actual**        | Ninguno                                    |
| **Versión objetivo**     | Por definir                                |
| **Última actualización** | 2026-10-04                                 |

---

# Estado General

GitHub Framework ha completado las fases de arquitectura, Open Source Readiness, Documentation Framework, Repository Templates y Workflow Framework.

El Framework dispone de una arquitectura formal, estándares de repositorio, un sistema de Components reutilizables, mecanismos de gobierno, una biblioteca de Documentation Components, tres Repository Templates y una primera familia de Core Workflow Components.

Las versiones `v0.1.0` a `v0.6.0` han sido publicadas. La última versión publicada es **`v0.6.0 — Framework Automation`**.

## Existing Repository Adoption Discovery

La investigación sobre Existing Repository Adoption ha completado una primera fase de Problem Discovery y un experimento adicional de Manual Adoption Assessment.

El trabajo se documenta en:

- `docs/discovery/23_BACKEND_ADOPTION_DISCOVERY.md`;
- `docs/discovery/24_ADOPTION_MODEL_DISCOVERY.md`;
- `docs/discovery/25_MANUAL_ADOPTION_ASSESSMENT_DISCOVERY.md`.

La investigación ha contrastado `TPL-BACKEND v0.1.0` sobre cuatro consumers backend con tecnologías diferentes:

- Java / Spring Boot;
- TypeScript / NestJS;
- Python / FastAPI;
- PHP / Symfony.

El modelo provisional distingue actualmente:

- Detected Facts;
- Evidence;
- Responsibility State;
- Applicability;
- Implementation Characteristics;
- Uncertainty;
- Evaluation Rationale;
- Adoption Decision;
- Decision Rationale.

El Manual Adoption Assessment ha resultado operacionalmente viable y trazable durante el experimento, aunque su repetibilidad no ha sido validada de forma independiente.

El resultado del Experimento #4 es `REFINEMENT NEEDED`: no se ha identificado una contradicción fundamental del modelo, pero el papel de `EVALUATE` y `JUSTIFY` requiere mayor refinamiento.

La investigación entra ahora en **Solution Shaping Discovery** para comparar representaciones mínimas del assessment.

No existe todavía:

- Solution seleccionada;
- Delivery Scope;
- Sprint;
- milestone;
- versión objetivo.

---

## Public Release

El 2026-09-26 GitHub Framework pasó oficialmente de repositorio privado a repositorio público tras completar una revisión específica de Public Release Readiness.

La revisión confirmó la ausencia de secretos o archivos sensibles detectables en el árbol actual y en el historial auditado, retiró del repositorio actual el material local de `legacy/` y verificó nuevamente el Framework Validator y sus 109 tests automatizados.

Como parte de la preparación pública se configuraron la descripción y los topics del repositorio, se estableció un ruleset activo sobre `main` y se habilitó un baseline de seguridad compuesto por Dependency Graph, Dependabot Alerts, Dependabot Security Updates, Secret Protection y Push Protection.

La publicación pública no introduce una nueva versión funcional del Framework. `v0.6.0` continúa siendo la última release publicada y el proyecto se encuentra actualmente en Solution Shaping Discovery del siguiente incremento, sin Sprint ni versión objetivo activos.

---

# Estado por Áreas

| Área                                         | Estado |
| -------------------------------------------- | :----: |
| Arquitectura del Framework                   |    ✅   |
| GitHub Repository Standards (GRS)            |    ✅   |
| Repository Design System (RDS)               |    ✅   |
| Component Catalog                            |    ✅   |
| Componentes README                           |    ✅   |
| Open Source Readiness                        |    ✅   |
| Documentation Component Architecture         |    ✅   |
| Core Documentation Components                |    ✅   |
| Documentation Reference Implementation       |    ✅   |
| Documentation Writing Standards              |    ✅   |
| Repository Template Architecture             |    ✅   |
| Core Repository Templates                    |    ✅   |
| Repository Template Reference Implementation |    ✅   |
| Repository Template Standards                |    ✅   |
| Workflow Component Architecture              |    ✅   |
| Core Workflow Components                     |    ✅   |
| Workflow Reference Implementation            |    ✅   |
| Workflow Component Standards                 |    ✅   |
| Component Metadata Standard                  |    ✅   |
| Component Metadata Normalization             |    ✅   |
| Framework Validator                          |    ✅   |
| Automation Reference Implementation          |    ✅   |
| Integración de Framework Automation en `main` |    ✅   |
| Publicación de v0.6.0                         |    ✅   |
| Publicación pública del repositorio           |    ✅   |

---

# Sprint Actual

No existe actualmente un Sprint activo.

Sprint 8 — Framework Automation finalizó con la publicación de `v0.6.0`.

Las cuatro historias (#23–#26), su integración, la documentación de release y la milestone correspondiente están completadas y cerradas.

El siguiente Sprint se definirá después del discovery y priorización del próximo incremento funcional.

---

# Próximo Hito

## Solution Shaping Discovery — Existing Repository Adoption

¿Cuál es la representación mínima que permite ejecutar y conservar un adoption assessment sin introducir acoplamiento técnico prematuro?

---

# Riesgos

Los principales riesgos para la evolución del Framework son:

* Sobrearquitectura y crecimiento de Components sin casos de uso reales.
* Duplicidad documental e incremento innecesario de complejidad.
* Divergencia entre los Components reutilizables y sus implementaciones reales.
* Automatización de inconsistencias históricas en lugar de normalizar previamente los contratos.
* Introducción de tooling más complejo que los problemas deterministas que pretende resolver.
* Interpretación de una validación automatizada satisfactoria como sustituto de la revisión arquitectónica.

La implementación de `v0.6.0` limita deliberadamente la automatización a reglas deterministas y evita introducir generación, corrección automática u orquestación CI.

---

# Principios Activos

Durante la evolución del proyecto se mantendrán los siguientes principios:

* Simplicidad.
* Reutilización.
* Modularidad.
* Dogfooding.
* Versionado continuo.
* Documentación como soporte, no como fin.
* Automatización posterior a la validación de los contratos arquitectónicos.

---

# Próximos Objetivos

1. Comparar representaciones mínimas para ejecutar y conservar un adoption assessment.
2. Evaluar las Solution Hypotheses relevantes sin seleccionar prematuramente una implementación.
3. Refinar el papel de `EVALUATE` y `JUSTIFY` dentro del modelo provisional.
4. Validar posteriormente la repetibilidad del assessment antes de promover una solución a Delivery Scope.

---

# Historial de Versiones

| Versión | Fecha      | Estado                                                             |
| ------- | ---------- | ------------------------------------------------------------------ |
| v0.1.0  | 2026-08-07 | Arquitectura completada                                            |
| v0.2.0  | 2026-08-09 | Open Source Readiness completado                                   |
| v0.3.0  | 2026-08-13 | Documentation Framework completado                                 |
| v0.4.0  | 2026-08-18 | Repository Templates completado                                    |
| v0.5.0  | 2026-09-14 | Workflow Framework publicado                                       |
| v0.6.0  | 2026-09-25 | Framework Automation publicado                                     |
