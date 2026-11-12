# Only Film — TPL-BACKEND Assessment Coverage Matrix

## 1. Contexto y límites

Este documento prepara la cobertura de **todas** las Responsibilities definidas por el Template `TPL-BACKEND` `0.1.0` sobre un repositorio consumidor real, sin inventar los resultados que todavía no han sido evaluados.

| Field | Value |
| --- | --- |
| Consumer Repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Repository Template | `TPL-BACKEND` |
| Template Version | `0.1.0` |
| Contract Source | [backend/metadata.yml](../../templates/repositories/backend/metadata.yml) |
| Assessment Status | `In Progress` |
| Scope | 28 Responsibilities del Template |
| Mutation | `NONE` |

Esta matriz **no es un resultado de validación**. Registra únicamente si una Responsibility se ha explorado documentalmente en el ejemplo existente o si su revisión está pendiente. `Not assessed` y `Explored — provisional` son **etiquetas de cobertura de trabajo**, no valores del campo `State` del Assessment Template. En particular, `Not assessed` no significa `Missing` ni `Not Applicable`.

## 2. Inventario completo del contrato

La lista se transcribe del bloque `components` de la metadata canónica de `TPL-BACKEND` `0.1.0` y conserva sus requirement levels. El requisito `Required` se aplica al Template, no debe deducirse de `priority` en la metadata de un Component.

| Responsibility | Requirement Level | Cobertura documental | Referencia / Evidence | Próxima acción |
| --- | --- | --- | --- | --- |
| `README-HERO` | `Required` | Explored — provisional | [Read-only Evidence](only-film-required-readme-batch-1.md) | Pending semantic review |
| `README-OVERVIEW` | `Required` | Explored — provisional | [Read-only Evidence](only-film-required-readme-batch-1.md) | Pending semantic review |
| `README-FEATURES` | `Required` | Explored — provisional | [Read-only Evidence](only-film-required-readme-batch-1.md) | Pending semantic review |
| `README-TECH-STACK` | `Required` | Explored — provisional | [Read-only Evidence](only-film-required-readme-batch-2.md) | Pending semantic review |
| `README-QUICK-START` | `Required` | Explored — provisional | [Evidence and provisional interpretation](only-film-two-responsibilities.md) | Pending verification |
| `README-DOCUMENTATION` | `Required` | Explored — provisional | [Read-only Evidence](only-film-required-readme-batch-2.md) | Pending semantic review |
| `README-FOOTER` | `Required` | Explored — provisional | [Read-only Evidence](only-film-required-readme-batch-2.md) | Pending semantic review |
| `DOC-CHANGELOG` | `Required` | Explored — provisional | [Read-only Evidence](only-film-required-readme-batch-2.md) | Pending semantic review |
| `README-STATUS` | `Recommended` | Explored — provisional | [Read-only Evidence](only-film-recommended-readme-batch.md) | Pending semantic review |
| `README-ARCHITECTURE` | `Recommended` | Explored — provisional | [Read-only Evidence](only-film-recommended-readme-batch.md) | Pending semantic review |
| `README-REPOSITORY-STRUCTURE` | `Recommended` | Explored — provisional | [Read-only Evidence](only-film-recommended-readme-batch.md) | Pending semantic review |
| `README-TESTING` | `Recommended` | Explored — provisional | [Evidence and provisional interpretation](only-film-two-responsibilities.md) | Pending verification |
| `DOC-ARCHITECTURE` | `Recommended` | Explored — provisional | [Read-only Evidence](only-film-recommended-documentation-batch.md) | Pending semantic review |
| `DOC-PROJECT-STATUS` | `Recommended` | Explored — provisional | [Read-only Evidence](only-film-recommended-documentation-batch.md) | Pending semantic review |
| `DOC-TESTING` | `Recommended` | Explored — provisional | [Read-only Evidence](only-film-recommended-documentation-batch.md) | Pending semantic review |
| `README-ROADMAP` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-readme-governance.md) | Pending semantic review |
| `README-CONTRIBUTING` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-readme-governance.md) | Pending semantic review |
| `README-DEMO` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-showcase-diagrams.md) | Pending semantic review |
| `README-AUTHOR` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-readme-governance.md) | Pending semantic review |
| `README-HIGHLIGHTS` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-showcase-diagrams.md) | Pending semantic review |
| `README-LICENSE` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-readme-governance.md) | Pending semantic review |
| `DOC-ADR` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-technical-batch.md) | Pending semantic review |
| `DOC-API` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-technical-batch.md) | Pending semantic review |
| `DOC-DATABASE` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-technical-batch.md) | Pending semantic review |
| `DOC-DEPLOYMENT` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-technical-batch.md) | Pending semantic review |
| `DOC-SECURITY` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-technical-batch.md) | Pending semantic review |
| `DOC-DIAGRAMS` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-showcase-diagrams.md) | Pending semantic review |
| `DOC-REFERENCES` | `Optional` | Explored — provisional | [Read-only Evidence](only-film-optional-technical-batch.md) | Pending semantic review |

## 3. Cobertura actual

| Requirement Level | Total del contrato | Explored — provisional | Not assessed |
| --- | ---: | ---: | ---: |
| `Required` | 8 | 8 | 0 |
| `Recommended` | 7 | 7 | 0 |
| `Optional` | 13 | 13 | 0 |
| **Total** | **28** | **28** | **0** |

Las veintiocho Responsibilities cuentan con una exploración documental vinculada a sus fuentes: el [walkthrough inicial](only-film-two-responsibilities.md), los [lotes Required 1](only-film-required-readme-batch-1.md) y [2](only-film-required-readme-batch-2.md), los lotes [Recommended README](only-film-recommended-readme-batch.md) y [Recommended Documentation](only-film-recommended-documentation-batch.md), y los lotes [Optional governance](only-film-optional-readme-governance.md), [Optional showcase](only-film-optional-showcase-diagrams.md) y [Optional technical](only-film-optional-technical-batch.md). Quick Start y Testing conservan `State: Partial` y `Applicability: Applicable` como interpretaciones provisionales en el ejemplo inicial; las otras veintiséis mantienen `State` y `Applicability` pendientes de revisión semántica. Todas conservan `Decision Status: Needs Further Evaluation` y `Adoption Decision: —`. **La cobertura completa de exploración no equivale a cumplimiento ni Assessment Complete.**

**Cobertura de inventario:** 28/28 Responsibilities enumeradas según el contrato.

**Cobertura de exploración documental:** 28/28 Responsibilities (no equivale a cumplimiento).

**Cobertura de evaluación concluida:** no demostrada; ninguna Adoption Decision se considera resuelta mediante esta matriz.

**Consolidación de revisión:** el [registro de lagunas de evidencia y revisión humana](only-film-assessment-review-register.md) prioriza las verificaciones pendientes y define las condiciones necesarias para avanzar desde la exploración documental hacia una evaluación semántica. No añade decisiones ni da por concluido el Assessment.

**Propuesta E3 para las Required prioritarias:** [Quick Start y Changelog](only-film-required-semantic-review.md) documenta interpretaciones e incertidumbres pendientes de aprobación. No modifica la etiqueta de cobertura `Explored — provisional` ni convierte las propuestas en `State` formal.

**Propuesta E3 para Hero, Overview y Features:** la [revisión semántica de las tres Responsibilities Required](only-film-required-identity-semantic-review.md) presenta criterios, evidencias y clasificaciones pendientes de reviewer. Su existencia no cambia las 28 filas de cobertura documental a evaluaciones aprobadas.

**Ocho Required con propuesta E3:** el [lote de Tech Stack, Documentation y Footer](only-film-required-final-semantic-review.md) completa las propuestas de interpretación de las ocho Responsibilities Required. Todas siguen sin aprobación humana; el State de DOC-CHANGELOG continúa sin determinar y la cobertura 28/28 sigue siendo documental.

**Propuestas Recommended README:** la [revisión semántica de Status, Architecture y Repository Structure](only-film-recommended-readme-semantic-review.md) aporta tres propuestas E3 adicionales. La cobertura global continúa en 28/28 **exploradas**, sin aprobación de States ni Adoption Decisions.

**Siete Recommended con propuesta E3:** la [revisión de Architecture y Project Status](only-film-recommended-docs-semantic-review.md) completa las fichas propuestas para las siete Responsibilities Recommended. No se ha aprobado ninguna evaluación ni decisión; la cobertura de 28/28 sigue siendo documental.

## 4. Protocolo para continuar el Assessment

### Fase A — Required

Revisar semánticamente las ocho Responsibilities `Required` exploradas, con sus incertidumbres y fuentes pendientes de comprobar. Para cada una:

1. Confirmar el requirement level contra el Template fijado.
2. Definir el ámbito de inspección y localizar fuentes del consumer en el SHA de referencia, señalando también las fuentes no accesibles.
3. Registrar `Detected Facts` y referencias mínimas a `Evidence`, sin interpretar la presencia de un archivo como cumplimiento.
4. Documentar `State`, `Applicability`, `Implementation Characteristics`, `Uncertainty` y `Evaluation Rationale` solo cuando exista evidencia suficiente para una interpretación explícita.
5. Registrar `Decision Status` y, únicamente si corresponde y existe revisión humana, la `Adoption Decision` y su justificación.

### Fase B — Recommended

Revisar semánticamente las siete `Recommended` ya exploradas, en especial las incertidumbres de `README-TESTING` y la vigencia de las auditorías documentales. Las responsabilidades recomendadas no se convierten en obligatorias por la presencia de un archivo relacionado.

### Fase C — Optional

Revisar semánticamente las trece `Optional` exploradas desde el punto de vista de `Applicability`, evitando asignar `Not Applicable` por defecto. El carácter opcional del Template no es una conclusión automática sobre su aplicabilidad.

### Fase D — Revisión transversal

Comprobar cobertura, trazabilidad a referencias inmutables, vigencia de evidencias, incertidumbres y coherencia entre `State`, `Applicability`, `Decision Status` y `Adoption Decision`. Si el consumer ha cambiado desde el SHA fijado, repetir o refrescar las observaciones relevantes antes de tomar decisiones sobre un estado nuevo.

## 5. Criterios para avanzar

| Check | Condición | Situación actual |
| --- | --- | --- |
| Contract inventory | Todas las Responsibilities enumeradas con requirement levels correctos | **Completado documentalmente** |
| Evidence coverage | Fuentes examinadas y trazadas por cada Responsibility requerida para el Assessment | **28/28 exploradas documentalmente**; revisión E2/E3 y suficiencia pendientes |
| Semantic review | Evaluación explícita por Responsibility, con incertidumbres y justificaciones | **Pendiente** |
| Operational verification | Procedimientos de arranque y pruebas reproducidos cuando sea necesario | **No realizado** |
| Adoption Decisions | Resolución humana, o decisión expresamente pendiente si corresponde | **Sin decisiones resueltas en los ejemplos** |
| Assessment conclusion | Aplicar las reglas de cierre de la [guía de adopción](../README.md) y del [Assessment Template](../assessment-template.md) | **In Progress** |

`Assessment Complete` no implica necesariamente que todas las `Adoption Decisions` estén resueltas, pero exige una evaluación documentada de todas las Responsibilities aplicables según las reglas del Template y de la guía. Una matriz con 28 filas **no** sustituye ese trabajo.

## 6. Evidencia de partida y siguientes verificaciones

- [Only Film — Two Backend Responsibilities](only-film-two-responsibilities.md): Evidence para Quick Start y Testing; interpretaciones provisionales.
- [Cross-Consumer Repeatability Replay](cross-consumer-repeatability-replay.md): comparación con SeniorMeet sobre Quick Start.
- [Assessment Template](../assessment-template.md): estructura reutilizable para registrar los resultados reales.

La continuación recomendada consiste en completar un lote acotado de Responsibilities `Required` con evidencia concreta y revisión humana antes de extenderse a las demás. El consumer no se modifica durante este inventario y no se autoriza Application ni Integration.
