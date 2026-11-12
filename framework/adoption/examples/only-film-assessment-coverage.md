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
| `README-HERO` | `Required` | Not assessed | — | Not started |
| `README-OVERVIEW` | `Required` | Not assessed | — | Not started |
| `README-FEATURES` | `Required` | Not assessed | — | Not started |
| `README-TECH-STACK` | `Required` | Not assessed | — | Not started |
| `README-QUICK-START` | `Required` | Explored — provisional | [Evidence and provisional interpretation](only-film-two-responsibilities.md) | Pending verification |
| `README-DOCUMENTATION` | `Required` | Not assessed | — | Not started |
| `README-FOOTER` | `Required` | Not assessed | — | Not started |
| `DOC-CHANGELOG` | `Required` | Not assessed | — | Not started |
| `README-STATUS` | `Recommended` | Not assessed | — | Not started |
| `README-ARCHITECTURE` | `Recommended` | Not assessed | — | Not started |
| `README-REPOSITORY-STRUCTURE` | `Recommended` | Not assessed | — | Not started |
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
| `Required` | 8 | 1 | 7 |
| `Recommended` | 7 | 1 | 6 |
| `Optional` | 13 | 0 | 13 |
| **Total** | **28** | **2** | **26** |

Las dos Responsibilities exploradas son `README-QUICK-START` y `README-TESTING`, procedentes del [walkthrough de Only Film](only-film-two-responsibilities.md). Ambas conservan `State: Partial` **provisional**, `Applicability: Applicable`, `Decision Status: Needs Further Evaluation` y `Adoption Decision: —` en aquel ejemplo. No se añaden aquí nuevos resultados semánticos.

**Cobertura de inventario:** 28/28 Responsibilities enumeradas según el contrato.

**Cobertura de exploración documental:** 2/28 Responsibilities (no equivale a cumplimiento).

**Cobertura de evaluación concluida:** no demostrada; ninguna Adoption Decision se considera resuelta mediante esta matriz.

## 4. Protocolo para continuar el Assessment

### Fase A — Required

Recorrer las siete Responsibilities `Required` todavía no exploradas. Para cada una:

1. Confirmar el requirement level contra el Template fijado.
2. Definir el ámbito de inspección y localizar fuentes del consumer en el SHA de referencia, señalando también las fuentes no accesibles.
3. Registrar `Detected Facts` y referencias mínimas a `Evidence`, sin interpretar la presencia de un archivo como cumplimiento.
4. Documentar `State`, `Applicability`, `Implementation Characteristics`, `Uncertainty` y `Evaluation Rationale` solo cuando exista evidencia suficiente para una interpretación explícita.
5. Registrar `Decision Status` y, únicamente si corresponde y existe revisión humana, la `Adoption Decision` y su justificación.

### Fase B — Recommended

Aplicar el mismo procedimiento a las seis `Recommended` pendientes y revisar las incertidumbres de `README-TESTING`. Las responsabilidades recomendadas no se convierten en obligatorias por la presencia de un archivo relacionado.

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
