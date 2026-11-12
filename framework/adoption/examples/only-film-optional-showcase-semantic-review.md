# Only Film — Provisional Semantic Review: Demo, Highlights and Diagrams

## 1. Contexto y alcance

Propuesta de evaluación semántica E3 de tres Responsibilities `Optional` de `TPL-BACKEND` 0.1.0. Se trabaja sobre el commit inmutable del consumer y se mantiene **separada la evidencia documental de la evaluación aprobada**.

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Scope | `README-DEMO`, `README-HIGHLIGHTS`, `DOC-DIAGRAMS` |
| Assessment Status | `In Progress` |
| Review Status | `Proposal — pending human review` |
| Reviewer / Approval | No asignado / no aprobado |
| Mutation | `NONE` |

En el catálogo inspeccionado de Components de `framework/components/` **no se identificaron componentes autónomos** para estos tres IDs, aunque se declaran `Optional` en la metadata del Template. Se aplica el propósito literal de las Responsibilities sin inventar restricciones ni reglas de diseño de un componente inexistente.

## 2. Summary of Proposed Evaluations

| Responsibility | Level | Proposed State | Proposed Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-DEMO` | Optional | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `README-HIGHLIGHTS` | Optional | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `DOC-DIAGRAMS` | Optional | **`Missing` / `Partial` — hipótesis no discriminadas** | **Por decidir**, según la utilidad real | `Needs Further Evaluation` | `—` |

La propuesta `Partial` no significa que se haya demostrado un defecto. La ausencia de un diagrama como fichero visible tampoco obliga a elegir `Missing` o `Not Applicable`.

## 3. Responsibility — README-DEMO

**Implementation Characteristics (proposed):** `Own`, `Distributed`: capturas de pantalla en README y procedimientos de arranque local.

**Detected Facts:**

- El [README fijado](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) contiene `Capturas de la aplicación` con imágenes referenciadas de cartelera, detalle de película, selección de butacas y ticket QR.
- El [directorio de capturas](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c/docs/screenshots) incluye además otras rutas de interfaz. Se ha comprobado su presencia versionada, **no** su calidad visual, actualidad ni exactitud.
- El README ofrece un procedimiento Docker Compose y la URL `http://localhost:8080/movies` que se ejecutaría **en el equipo local**. No es un enlace a una demo pública.
- La [revisión de lagunas de Compose](only-film-compose-evidence-gap.md) señala que los checks directamente asociados a este SHA no incluyen un smoke de Compose ejecutado, aunque sí otros jobs H2/PostgreSQL.

**Evidence:** [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [árbol de capturas](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c/docs/screenshots), [lote exploratorio](only-film-optional-showcase-diagrams.md), [verificación de Compose](only-film-compose-evidence-gap.md).

**Evaluation Rationale — propuesta:** existen recursos capaces de mostrar al lector qué aspecto tiene la aplicación. La propuesta `Partial` invita a valorar si esas capturas cumplen la finalidad comunicativa de `Demo` o si para el público objetivo se requiere un flujo reproducible, vídeo o demo accesible. No se debe exigir despliegue público por ser Optional; tampoco puede declararse una demostración ejecutada.

**Uncertainty:** ¿Las imágenes representan el SHA fijado? ¿Bastan las capturas para el objetivo de portfolio? ¿Cómo se comunicaría al lector la ausencia de demo online y los requisitos de datos demo locales?

**Proposed State:** `Partial`; **Proposed Applicability:** `Applicable`, ambos pendientes de revisión.

**Decision Status:** `Needs Further Evaluation`; **Adoption Decision:** `—`.

## 4. Responsibility — README-HIGHLIGHTS

**Implementation Characteristics (proposed):** `Own`, `Distributed`: argumentos de valor incluidos en `Funcionalidades` y `Seguridad y límites actuales`, sin bloque titulado Highlights.

**Detected Facts:**

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) destaca protección de butacas frente a doble venta, checkout transaccional, control de acceso por roles, seguridad de reseñas, imágenes verificadas y migraciones PostgreSQL/Flyway.
- La sección `Funcionalidades` distingue capacidades de visitantes, usuarios y administradores. `Seguridad y límites actuales` aclara que el checkout es simulado y no existe pasarela de pago real.
- La ejecución [GitHub Actions 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) registra 329 tests H2 correctos y tres checks satisfactorios, incluidos escenarios de seguridad. Son **evidencias acotadas**, no prueba de todas las capacidades ni validación de experiencia de usuario.
- El README no tiene un encabezado literal `Highlights`; ese título no es por sí mismo requisito de la metadata de `TPL-BACKEND`.

**Evidence:** [README — Funcionalidades y seguridad](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [registro Surefire/Sonar](only-film-verified-surefire-sonar-logs.md), [exploración inicial](only-film-optional-showcase-diagrams.md).

**Evaluation Rationale — propuesta:** las características diferenciadoras se comunican mediante contenido distribuido y algunas cuentan con respaldo técnico parcial. Un reviewer debe decidir si aportaría valor una selección breve de Highlights para visitantes del repositorio o si duplicaría Features, especialmente tratándose de un Component Optional. No se infiere `Missing` por ausencia de un apartado propio.

**Uncertainty:** ¿Qué tres o cuatro capacidades resumen mejor el valor del portfolio? ¿Están las afirmaciones principales suficientemente contrastadas? ¿Un bloque adicional duplicaría contenido sin aportar claridad?

**Proposed State:** `Partial`; **Proposed Applicability:** `Applicable`, ambos pendientes de revisión.

**Decision Status:** `Needs Further Evaluation`; **Adoption Decision:** `—`.

## 5. Responsibility — DOC-DIAGRAMS

**Implementation Characteristics (proposed):** no acreditadas como artefacto técnico específico; el README aporta solo un flujo **textual** de arquitectura.

**Detected Facts:**

- En `Tecnologías y arquitectura`, el [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) describe el flujo `Controlador MVC → servicio / reglas de negocio → repositorio JPA → base de datos`, pero no representa un diagrama explícito de componentes, entidades o despliegue.
- El árbol Git del SHA contiene capturas de interfaz en `docs/screenshots/` y `src/main/resources/static/images/avatar.svg`. **Ninguno de esos nombres implica un diagrama técnico.**
- La exploración previa no localizó ficheros con nombres de diagramas ni extensiones `.drawio`, `.puml` o Mermaid. No ha inspeccionado exhaustivamente documentos Markdown en busca de diagramas embebidos.
- El [Component DOC-ARCHITECTURE](../../components/documentation/architecture/README.md) señala que los diagramas deben tener finalidad, representar la arquitectura vigente y ser mantenibles; también declara que los diagramas son **opcionales** para describir arquitectura.

**Evidence:** [README — flujo de capas](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [árbol Git del SHA](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c), [exploración inicial](only-film-optional-showcase-diagrams.md), [criterios generales DOC-ARCHITECTURE](../../components/documentation/architecture/README.md).

**Evaluation Rationale — propuesta:** no existe evidencia suficiente para afirmar que el consumer tenga diagramas técnicos mantenidos; tampoco se ha comprobado que su complejidad exija crearlos. Un flujo textual no equivale necesariamente a un diagrama, pero puede resolver adecuadamente una necesidad de explicación simple. Antes de elegir entre `Missing`, `Partial` y `Not Applicable` debe valorarse el propósito real y buscar posibles diagramas incrustados. No se genera ningún diagrama por formalismo.

**Uncertainty:** ¿Existen diagramas embebidos en documentación Markdown? ¿La relación entre entidades, flujo de compra o despliegue se entendería mejor con diagramas versionables? ¿La Responsibility resulta útil o sería duplicación innecesaria?

**Proposed State:** sin elegir entre `Missing` y `Partial`; **Proposed Applicability:** sin decidir entre `Applicable` y `Not Applicable`.

**Decision Status:** `Needs Further Evaluation`; **Adoption Decision:** `—`.

## 6. Human Review Gates

| Gate | Verificación | Estado |
| --- | --- | --- |
| SH-1 | Confirmar audiencia y valor concreto de Demo, Highlights y Diagrams | Pendiente |
| SH-2 | Comprobar correspondencia de capturas con funcionalidades y versión del consumer | Pendiente |
| SH-3 | Determinar si la demo local reproducible es necesaria para la finalidad documental | Pendiente |
| SH-4 | Valorar si Highlights aportaría claridad sin duplicar Features | Pendiente |
| SH-5 | Buscar diagramas embebidos y evaluar utilidad de un diagrama mantenible | Pendiente |
| SH-6 | Registrar State, Applicability, Rationale, Uncertainty y Decision Status aprobados individualmente | Pendiente |
| SH-7 | Si se requiere, resolver cualquier discrepancia del catálogo de Components **en el Framework**, no en el consumer | Pendiente |

## 7. Resultado y continuación

Este lote añade **tres propuestas E3 Optional**. Junto a la revisión previa de `DOC-SECURITY` y las cuatro propuestas Optional de gobernanza, existen **8/13 Optional con propuesta semántica**, aún sin aprobación humana.

La exploración documental global sigue en **28/28**. Las Adoption Decisions no se han resuelto y el Assessment permanece `In Progress`. No se ha modificado Only Film ni ejecutado una demo, tests, despliegue o verificación visual de capturas.
