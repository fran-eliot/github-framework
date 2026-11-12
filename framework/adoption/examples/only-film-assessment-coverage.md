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
| `DOC-ARCHITECTURE` | `Recommended` | Not assessed | — | Not started |
| `DOC-PROJECT-STATUS` | `Recommended` | Not assessed | — | Not started |
| `DOC-TESTING` | `Recommended` | Not assessed | — | Not started |
| `README-ROADMAP` | `Optional` | Not assessed | — | Not started |
| `README-CONTRIBUTING` | `Optional` | Not assessed | — | Not started |
| `README-DEMO` | `Optional` | Not assessed | — | Not started |
| `README-AUTHOR` | `Optional` | Not assessed | — | Not started |
| `README-HIGHLIGHTS` | `Optional` | Not assessed | — | Not started |
| `README-LICENSE` | `Optional` | Not assessed | — | Not started |
| `DOC-ADR` | `Optional` | Not assessed | — | Not started |
| `DOC-API` | `Optional` | Not assessed | — | Not started |
| `DOC-DATABASE` | `Optional` | Not assessed | — | Not started |
| `DOC-DEPLOYMENT` | `Optional` | Not assessed | — | Not started |
| `DOC-SECURITY` | `Optional` | Not assessed | — | Not started |
| `DOC-DIAGRAMS` | `Optional` | Not assessed | — | Not started |
| `DOC-REFERENCES` | `Optional` | Not assessed | — | Not started |

## 3. Cobertura actual

| Requirement Level | Total del contrato | Explored — provisional | Not assessed |
| --- | ---: | ---: | ---: |
| `Required` | 8 | 8 | 0 |
| `Recommended` | 7 | 4 | 3 |
| `Optional` | 13 | 0 | 13 |
| **Total** | **28** | **12** | **16** |

Las doce Responsibilities exploradas documentalmente comprenden las dos del [walkthrough inicial](only-film-two-responsibilities.md), las tres del [primer lote Required](only-film-required-readme-batch-1.md), las cuatro del [segundo lote Required](only-film-required-readme-batch-2.md) y las tres del [primer lote Recommended](only-film-recommended-readme-batch.md). Quick Start y Testing conservan `State: Partial` y `Applicability: Applicable` como interpretaciones provisionales en su ejemplo; las diez restantes mantienen `State` y `Applicability` pendientes de revisión semántica. Todas conservan `Decision Status: Needs Further Evaluation` y `Adoption Decision: —`. **Exploración no equivale a cumplimiento.**

**Cobertura de inventario:** 28/28 Responsibilities enumeradas según el contrato.

**Cobertura de exploración documental:** 12/28 Responsibilities (no equivale a cumplimiento).

**Cobertura de evaluación concluida:** no demostrada; ninguna Adoption Decision se considera resuelta mediante esta matriz.

## 4. Protocolo para continuar el Assessment

### Fase A — Required

Revisar semánticamente las ocho Responsibilities `Required` exploradas, con sus incertidumbres y fuentes pendientes de comprobar. Para cada una:

1. Confirmar el requirement level contra el Template fijado.
2. Definir el ámbito de inspección y localizar fuentes del consumer en el SHA de referencia, señalando también las fuentes no accesibles.
3. Registrar `Detected Facts` y referencias mínimas a `Evidence`, sin interpretar la presencia de un archivo como cumplimiento.
4. Documentar `State`, `Applicability`, `Implementation Characteristics`, `Uncertainty` y `Evaluation Rationale` solo cuando exista evidencia suficiente para una interpretación explícita.
5. Registrar `Decision Status` y, únicamente si corresponde y existe revisión humana, la `Adoption Decision` y su justificación.

### Fase B — Recommended

Aplicar el mismo procedimiento a las tres `Recommended` pendientes y revisar las incertidumbres de `README-TESTING`. Las responsabilidades recomendadas no se convierten en obligatorias por la presencia de un archivo relacionado.

### Fase C — Optional

Revisar individualmente las trece `Optional` desde el punto de vista de `Applicability`, evitando asignar `Not Applicable` por defecto. El carácter opcional del Template no es una conclusión automática sobre su aplicabilidad.

### Fase D — Revisión transversal

Comprobar cobertura, trazabilidad a referencias inmutables, vigencia de evidencias, incertidumbres y coherencia entre `State`, `Applicability`, `Decision Status` y `Adoption Decision`. Si el consumer ha cambiado desde el SHA fijado, repetir o refrescar las observaciones relevantes antes de tomar decisiones sobre un estado nuevo.

## 5. Criterios para avanzar

| Check | Condición | Situación actual |
| --- | --- | --- |
| Contract inventory | Todas las Responsibilities enumeradas con requirement levels correctos | **Completado documentalmente** |
| Evidence coverage | Fuentes examinadas y trazadas por cada Responsibility requerida para el Assessment | **Pendiente** — solo dos exploradas |
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
