# Only Film — Provisional Semantic Review: Status, Architecture and Repository Structure

## 1. Assessment Context

Propuesta de revisión E3 de tres Responsibilities `Recommended` de `TPL-BACKEND` 0.1.0, basadas en el commit fijo del consumidor. **No constituye aprobación humana ni confirma cumplimiento del Template.**

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Repository Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Collection Scope | `README-STATUS`, `README-ARCHITECTURE`, `README-REPOSITORY-STRUCTURE` |
| Review Status | `Proposal — pending human review` |
| Reviewer / Approval | Not assigned / not approved |
| Assessment Status | `In Progress` |
| Consumer Mutation | `NONE` |

## 2. Summary of Proposals

| Responsibility | Requirement Level | Proposed State | Proposed Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-STATUS` | Recommended | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `README-ARCHITECTURE` | Recommended | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `README-REPOSITORY-STRUCTURE` | Recommended | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |

Los tres `State` son hipótesis editoriales conservadoras **sin defecto material demostrado por esa etiqueta**. Una revisión podría concluir `Satisfied` o mantener `Partial` con razones precisas. No se equipara falta de una sección con título canónico a `Missing`.

## 3. Responsibility — README-STATUS

**Requirement Level:** `Recommended`.

**Proposed State:** `Partial`, pendiente de revisión.

**Proposed Applicability:** `Applicable`, pendiente de revisión.

**Implementation Characteristics (proposed):** `Own`, `Distributed` como posible representación de madurez y estado en el README y documentación especializada. No se ha acreditado una implementación canónica de `project_status` / `maturity` en el README.

### Detected Facts

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) tiene badges que indican **tecnologías y versiones** (Java 25, Spring Boot 4.0.5, PostgreSQL 17, Flyway, Docker Compose). **No son badges de salud de CI, estado del proyecto ni nivel de madurez.**
- La sección `Pruebas y CI` distingue workflows de regresión, migración, Compose, pruebas manuales y Sonar. `Próximas líneas de evolución` diferencia trabajo futuro de funcionalidades implantadas.
- La [evaluación histórica de madurez](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md), fechada 2026-10-10 y referida a `9f2a31e927df105d14e3d30d4d8277fa61883deb`, describe un portfolio backend técnicamente evolucionado con límites de producción; **no es** una declaración automática del estado del SHA evaluado.
- El [Component STATUS](../../components/readme/status/README.md) describe estado operativo y nivel de madurez, con entradas `project_status` y `maturity`, y ubicación sugerida inmediatamente después de Hero. No se identificó una declaración integrada de esos dos campos en el contenido README inspeccionado.
- Un [run de CI del SHA](https://github.com/fran-eliot/only_film/actions/runs/39283862407) acredita tres checks satisfactorios en 2026-10-19 y 329 tests H2 satisfactorios en uno de ellos. **Un run exitoso no establece por sí mismo el estado global del proyecto**.

### Evidence

- [README versionado](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Informe histórico de madurez](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md)
- [Resultados de CI/Surefire verificados](only-film-verified-surefire-sonar-logs.md)
- [Component STATUS](../../components/readme/status/README.md)
- [Lote exploratorio original](only-film-recommended-readme-batch.md)

### Evaluation Rationale — propuesta

Hay material sobre tecnologías, alcance, CI y planes, pero la finalidad de `README-STATUS` es comunicar claramente **estado y madurez**. No procede inferir un estado de producción a partir de badges ni copiar la auditoría de octubre como si reflejase el snapshot evaluado sin contrastarla. `Partial` se plantea por la **representación distribuida e incompleta para esa finalidad**, no por un requisito de badge visual particular.

### Uncertainty

- ¿Quién mantiene una declaración de madurez y estado operativo, con qué referencia temporal?
- ¿Necesita el lector distinguir `portfolio/demo`, `development` y `production-ready`, y con qué evidencia?
- ¿Una nota breve en README sería suficiente o existe otra fuente actualizada y navegable?

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

**Decision Rationale (unresolved):** no está aprobada la clasificación ni justificado `PRESERVE`, `ADAPT` o `ADD`; se requieren alcance y revisión editorial.

## 4. Responsibility — README-ARCHITECTURE

**Requirement Level:** `Recommended`.

**Proposed State:** `Partial`, pendiente de revisión.

**Proposed Applicability:** `Applicable`, pendiente de revisión.

**Implementation Characteristics (proposed):** `Own`, `Distributed`: resumen de stack y flujo MVC/JPA en README con referencia a documentación técnica en `docs/`.

### Detected Facts

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) resume el flujo `Controlador MVC → servicio / reglas de negocio → repositorio JPA → base de datos` y enumera entidades como `Movie`, `Room`, `Session`, `Ticket`, `Review` y `User`.
- El [Component ARCHITECTURE](../../components/readme/architecture/README.md) exige un **resumen general**, no una reproducción de la documentación técnica detallada.
- La [auditoría histórica de arquitectura](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md), fechada 2026-10-10 y basada en una referencia posterior a PR #23 (`b6cf52c9`), indica que algunos controladores accedían directamente a repositorios. No se ha revalidado esa observación contra todos los controladores del SHA fijado.
- El [informe de madurez técnica](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md) es de otra referencia anterior. Los documentos con fechas y referencias diferentes no constituyen automáticamente una representación consolidada de arquitectura actual.

### Evidence

- [README — Tecnologías y arquitectura](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Auditoría histórica de arquitectura](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md)
- [Component ARCHITECTURE](../../components/readme/architecture/README.md)
- [Lote exploratorio original](only-film-recommended-readme-batch.md)

### Evaluation Rationale — propuesta

El README contiene un resumen comprensible de las capas, apropiado para orientar a un nuevo lector sin profundizar en implementación. La fórmula lineal puede interpretarse como una regla universal y la auditoría histórica sugiere que esa representación era simplificada. Corresponde al reviewer valorar si es suficiente identificar un **flujo principal** y si necesita aclaraciones sobre excepciones o documentación de apoyo. No se afirma que exista un incumplimiento arquitectónico vigente.

### Uncertainty

- ¿El flujo nominal refleja suficientemente la arquitectura del commit o requiere matices?
- ¿Hay rutas críticas que eludan servicios y deban representarse sin convertir el README en un inventario de problemas?
- ¿La separación entre resumen README y documentación técnica es clara?

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

**Decision Rationale (unresolved):** no se ha aprobado conservar la descripción actual ni modificarla; se requiere revisión del contenido y del público objetivo.

## 5. Responsibility — README-REPOSITORY-STRUCTURE

**Requirement Level:** `Recommended`.

**Proposed State:** `Partial`, pendiente de revisión.

**Proposed Applicability:** `Applicable`, pendiente de revisión.

**Implementation Characteristics (proposed):** `Own`, `Canonical` en sentido funcional: el README incluye explícitamente un árbol de directorios; no se afirma conformidad con una especificación de componente no encontrada.

### Detected Facts

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) tiene una sección `Organización del repositorio`, con árbol resumido que recoge `src/main/java/com/demo`, `src/main/resources/templates`, `static`, `db/migration`, `src/test/java/com/demo`, `docs/`, `.github/workflows/`, `Dockerfile`, `compose.yaml` y `.env.example`.
- La inspección previa del árbol del commit confirmó la presencia de las principales rutas. El resumen no pretende enumerar todos los directorios y archivos.
- `README-REPOSITORY-STRUCTURE` se encuentra declarado `Recommended` en [TPL-BACKEND/metadata.yml](../../templates/repositories/backend/metadata.yml).
- En el catálogo de `framework/components/readme/` inspeccionado **no se localizó un Component README-REPOSITORY-STRUCTURE autónomo**, por lo que no se atribuyen a ese Component reglas editoriales inexistentes ni se deduce ausencia de la Responsibility en el consumer.

### Evidence

- [README — Organización del repositorio](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Árbol Git del SHA evaluado](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)
- [Metadata del Template](../../templates/repositories/backend/metadata.yml)
- [Exploración documental original](only-film-recommended-readme-batch.md)

### Evaluation Rationale — propuesta

El mapa de rutas ofrece orientación inicial y guarda relación directa con la Responsibility. Su nivel de detalle puede ser suficiente para un README conciso; la clasificación `Partial` se mantiene **solo provisionalmente**, sin presumir que falten subdirectorios concretos. Se necesita una valoración de usabilidad, vigencia y alcance para decidir si es `Satisfied`.

### Uncertainty

- ¿Un nuevo contribuidor puede localizar las capas, migraciones y workflows con el árbol actual?
- ¿La simplificación del árbol induce algún error sobre la organización vigente?
- ¿Es necesaria una especificación canónica del Component en el Framework? Esa es una cuestión **del Framework**, distinta de la valoración del consumer.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

**Decision Rationale (unresolved):** no hay aprobación humana ni evidencia de un cambio imprescindible. No se autoriza modificar Only Film.

## 6. Human Review Gates

| Gate | Criterio | Estado |
| --- | --- | --- |
| RR-1 | Acordar qué comunica estado operativo/madurez para un repo portfolio y con qué fuente | Pendiente |
| RR-2 | Validar que el resumen de arquitectura no presenta el flujo nominal como descripción exhaustiva | Pendiente |
| RR-3 | Revisar que el mapa de directorios sea navegable y no dé información engañosa | Pendiente |
| RR-4 | Aprobar o corregir State, Applicability, Implementation Characteristics y rationale de cada Responsibility | Pendiente |
| RR-5 | Resolver decisiones individualmente o mantener incertidumbre con justificación | Pendiente |
| RR-6 | Si se requiere, abordar la falta de especificación individual de `README-REPOSITORY-STRUCTURE` **en el propio Framework**, no en el consumer | Pendiente, fuera de alcance de este lote |

## 7. Conclusión

Este lote aporta tres propuestas E3 para las Responsibilities Recommended de Status, Architecture y Repository Structure. **No son evaluaciones aprobadas ni decisiones de adopción**. La exploración documental global continúa en **28/28** y el Assessment en `In Progress`.

No se ejecutaron builds, pruebas ni despliegues nuevos y no se modificó Only Film.
