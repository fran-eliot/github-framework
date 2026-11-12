# Only Film — Provisional Semantic Review: Hero, Overview and Features

## 1. Contexto y alcance

Este lote propone la interpretación semántica de tres Responsibilities `Required` de `TPL-BACKEND` 0.1.0. La fuente principal es el [README de Only Film](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) fijado a un commit inmutable. Se contrastan criterios de los Components, **sin inferir validación funcional ni aprobación editorial**.

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Scope | `README-HERO`, `README-OVERVIEW`, `README-FEATURES` |
| Assessment Status | `In Progress` |
| Review Status | **Proposal — pending human review** |
| Reviewer / Approval Date | **No asignado / sin aprobar** |
| Mutation | `NONE` |

El nivel `Required` procede de la metadata del **Repository Template**, no de un campo de prioridad de Components. Los States siguientes son **hipótesis de revisión** y no registros aprobados en el Assessment.

## 2. Resumen provisional

| Responsibility | Requirement Level | Proposed State | Proposed Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-HERO` | Required | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `README-OVERVIEW` | Required | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `README-FEATURES` | Required | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |

Se propone `Partial` de forma **conservadora**, no porque se haya demostrado una deficiencia material. El reviewer podrá confirmar `Satisfied`, `Partial` o `Missing` según los criterios de contenido y la evidencia adecuada; no hace falta exigir ejecución de la aplicación para evaluar cada atributo puramente documental.

## 3. Responsibility: README-HERO

**Requirement Level:** `Required`.

**Proposed State:** `Partial` — pendiente de revisión.

**Proposed Applicability:** `Applicable` — pendiente de revisión.

**Implementation Characteristics (proposed):** `Own`, `Canonical`: cabecera con identidad, descripción y badges en el README principal.

**Detected Facts:**

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) comienza con un único encabezado principal visible en el contenido inspeccionado: `# 🎬 Only Film`.
- El primer párrafo explica en una frase la naturaleza del proyecto y tecnologías principales; el siguiente contextualiza su origen académico y evolución posterior.
- Aparecen cinco badges identificando Java 25, Spring Boot 4.0.5, PostgreSQL 17, Flyway y Docker Compose.
- El Component [README-HERO](../../components/readme/hero/README.md) exige claridad de nombre, tagline, badges y estructura, mientras que el banner es opcional y recomienda limitar badges y verificar modo claro/oscuro.

**Evidence:** [README.md — encabezado, descripción y badges](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md); [Component Hero](../../components/readme/hero/README.md); [exploración original](only-film-required-readme-batch-1.md).

**Evaluation Rationale — propuesta:** los elementos de identidad están presentes y el propósito general puede reconocerse sin navegar a otra sección. El hecho de que no haya un tagline separado o banner no demuestra incumplimiento; hay que valorar la legibilidad, la duplicación de descripción con Overview y la presentación de badges. No se verificó renderizado en temas o tamaños de pantalla.

**Uncertainty:** ¿Se distingue una presentación breve de la explicación extensa? ¿La cabecera resulta legible en dispositivos y temas previstos? ¿Los badges reflejan versiones realmente usadas? Solo algunas versiones se contrastaron con [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) y [Compose](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml).

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** no se ha aprobado si mantener la cabecera como está o ajustar la composición; no se deduce `PRESERVE` o `ADAPT` automáticamente.

## 4. Responsibility: README-OVERVIEW

**Requirement Level:** `Required`.

**Proposed State:** `Partial` — pendiente de revisión.

**Proposed Applicability:** `Applicable` — pendiente de revisión.

**Implementation Characteristics (proposed):** `Own`, `Distributed`: el resumen funcional aparece en la introducción, sin un apartado literal `## Overview`.

**Detected Facts:**

- La introducción del [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) define Only Film como una aplicación web de gestión cinematográfica y explica cartelera, proyecciones, selección de butacas, entradas y administración por roles.
- Un segundo párrafo aclara que la base procede de un proyecto académico colaborativo y describe áreas de evolución técnica.
- El [Component Overview](../../components/readme/overview/README.md) pide explicar proyecto, objetivo y problema que resuelve, evitar detalles técnicos extensos y no incluir instalación. Su organización sugerida no convierte un título literal en requisito material automático.

**Evidence:** [README.md — introducción](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md); [Component Overview](../../components/readme/overview/README.md); [exploración original](only-film-required-readme-batch-1.md).

**Evaluation Rationale — propuesta:** existe un resumen reconocible del propósito y alcance. La ausencia de `## Overview` no significa ausencia de Responsibility. No obstante, la introducción mezcla definición de producto con stack y contexto histórico; el reviewer debe decidir si esa combinación proporciona al público objetivo una visión suficientemente clara y diferenciada del Hero.

**Uncertainty:** ¿Explica adecuadamente el problema/beneficio para usuarios y mantenedores, no solo las operaciones disponibles? ¿Conviene una separación editorial entre presentación, overview y antecedentes sin duplicar texto?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** no se dispone de una revisión editorial aceptada que justifique mantener intacta o adaptar la distribución del contenido.

## 5. Responsibility: README-FEATURES

**Requirement Level:** `Required`.

**Proposed State:** `Partial` — pendiente de revisión.

**Proposed Applicability:** `Applicable` — pendiente de revisión.

**Implementation Characteristics (proposed):** `Own`, `Equivalent`: sección funcional titulada `Funcionalidades`, con agrupación por rol en vez de un bloque con título inglés canónico.

**Detected Facts:**

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) contiene `## Funcionalidades` y distingue visitantes, usuarios y administradores.
- La lista incluye acceso a películas/sesiones, registro/login, reservas/compra demostrativa, consulta de tickets, reseñas y administración.
- Un párrafo adicional declara uso de control transaccional y bloqueo de base de datos para evitar venta duplicada de butacas; esta descripción de implementación va más allá de una enumeración estrictamente funcional.
- El [Component Features](../../components/readme/features/README.md) indica que la sección debe describir capacidades principales, no detalles de implementación.
- La evidencia previa de CI en el commit [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) acredita pruebas de regresión H2 y PostgreSQL, **pero no prueba cada afirmación de producto ni equivale a aceptación funcional completa**.

**Evidence:** [README.md — Funcionalidades](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md); [Component Features](../../components/readme/features/README.md); [exploración original](only-film-required-readme-batch-1.md).

**Evaluation Rationale — propuesta:** la organización por roles comunica capacidades al lector y se ajusta a la finalidad general de Features. El reviewer debe confirmar que todas las funcionalidades descritas corresponden al estado de la referencia evaluada y si la nota transaccional convendría trasladarla a arquitectura/seguridad. La propuesta `Partial` no implica que las capacidades estén ausentes ni que el software falle.

**Uncertainty:** ¿Es exacta la enumeración de funciones para este commit? ¿Debe destacarse que el checkout es de demostración y no una pasarela de pago real? ¿La sección prioriza capacidades frente a implementación?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** falta decidir, con revisión del contenido, si la sección se conserva o necesita ajustes. No se modifica la descripción del consumer.

## 6. Gates para el reviewer

| Gate | Condición observable | Estado |
| --- | --- | --- |
| ID-1 | Contrato y Component criteria contrastados con la referencia fijada | Evidencia preparada; pendiente de reviewer |
| ID-2 | Separación de propósito del Hero, Overview y Features sin repetición material | Pendiente |
| ID-3 | Badges, stack y afirmaciones de funcionalidades contrastados cuando sean relevantes | Parcial; pendiente |
| ID-4 | Legibilidad de la cabecera valorada sin asumir renderizado no comprobado | Pendiente |
| ID-5 | `State`, `Applicability`, `Evaluation Rationale` y `Uncertainty` confirmados o corregidos individualmente | Pendiente |
| ID-6 | `Decision Status` y eventual `Adoption Decision` sustentados por rationale humano | Pendiente |

## 7. Conclusión

Se dispone de **tres propuestas E3 estructuradas** para Responsibilities `Required`, basadas en evidencias documentales y criterios explícitos. Sus States y Applicability siguen provisionales, ninguna decisión de adopción está aprobada y el Assessment permanece `In Progress`. No se modificó Only Film ni se ejecutaron nuevas pruebas.
