# Only Film — Provisional Semantic Review of Testing Responsibilities

## 1. Contexto y límites de la revisión

Este documento **propone** una interpretación semántica de dos Responsibilities de `TPL-BACKEND` 0.1.0 con la evidencia E2 ya recopilada. **No representa una aprobación humana realizada** ni sustituye el [Assessment Template](../assessment-template.md).

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Collection Scope | `README-TESTING`, `DOC-TESTING` |
| Assessment Status | `In Progress` |
| Review Status | **Proposal — pending human review** |
| Reviewer / Approval Date | **Not assigned / not approved** |
| Mutation | `NONE` |

Las propuestas de `State` sirven para que el reviewer pueda confirmarlas, corregirlas o rechazarlas. La presencia de tests verdes, guías y CI no demuestra por sí sola cumplimiento de todas las expectativas de documentación, ni cobertura total del software.

## 2. Resumen de propuestas pendientes de revisión

| Responsibility | Requirement Level | Proposed State | Proposed Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-TESTING` | Recommended | `Partial` (**provisional**) | `Applicable` (**provisional**) | `Needs Further Evaluation` | `—` |
| `DOC-TESTING` | Recommended | `Partial` (**provisional**) | `Applicable` (**provisional**) | `Needs Further Evaluation` | `—` |

La clasificación `Partial` se mantiene como **hipótesis conservadora** para revisión: existen instrucciones y evidencias funcionales, pero también hay límites documentales y operativos que el reviewer debe valorar. **No** se introduce una conclusión de `Satisfied` o `Missing` sin esa evaluación.

## 3. Responsibility: README-TESTING

**Requirement Level:** `Recommended`.

**Proposed State:** `Partial` (pendiente de aprobación).

**Proposed Applicability:** `Applicable` (pendiente de aprobación).

**Implementation Characteristics (proposed):** `Own`, `Distributed`: una sección de Testing en README enlaza a workflows y guías técnicas especializadas.

**Detected Facts:**

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) tiene el apartado `Pruebas y CI`, con `./mvnw test`, ejemplos de filtros y una tabla de workflows que distingue la suite manual de los checks habituales de PR.
- [`tests.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/tests.yml) define jobs manuales y un job Selenium que también puede activarse cuando un PR modifica ese workflow.
- [`postgres-migration.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml) configura regresión H2, esquema PostgreSQL e integración JPA/concurrencia.
- En el [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407), fijado al SHA evaluado, el log de `h2-regression` registra **329 tests, 0 failures, 0 errors, 0 skipped** y `BUILD SUCCESS`.
- Las clases `ReviewControllerTest` (20), `MutationCsrfSecurityTest` (3), `TicketSecurityRegressionTest` (3), `EnvironmentHardeningTest` (5) y `FileServiceTest` (9) tienen resultados individuales `0/0/0` en el log.
- Los otros dos jobs del run, `postgres-schema` y `PostgreSQL JPA and concurrent checkout`, constan como `success`.

**Evidence:**

- [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [tests.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/tests.yml)
- [postgres-migration.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml)
- [Registro de Surefire y Sonar verificado](only-film-verified-surefire-sonar-logs.md)
- [Verificación de Quick Start y CI](only-film-pinned-quickstart-ci-verification.md)

**Evaluation Rationale — propuesta, no decisión:**

Las instrucciones de testing son visibles, están conectadas con archivos versionados y existe una ejecución exitosa de pruebas concretas sobre el commit evaluado. Esto refuerza que la sección no se limita a afirmaciones sin evidencia. Sin embargo, la ruta rápida `./mvnw test` no equivale necesariamente a la selección H2 del CI, que ejecuta `-Dtest` con clases específicas; la suite Selenium y el smoke Compose no están acreditados para ese mismo SHA en este conjunto de evidencias. Un reviewer debe decidir si las advertencias y enlaces del README describen suficientemente esos límites para el público objetivo.

**Uncertainty:**

- ¿Las instrucciones locales son reproducibles desde un clon limpio con servicios y versiones documentados?
- ¿Son claras las diferencias entre el comando general, los filtros, la regresión H2 y los workflows manuales?
- ¿El README satisface la responsabilidad de orientar al contribuidor sin exigir cobertura completa del software?
- ¿Debe actualizarse algún enlace o explicación para evitar que se interprete `tests.yml` como obligatorio en todos los PR?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** no se ha revisado y aprobado la suficiencia semántica de la sección de testing. `PRESERVE` o `ADAPT` requerirían una justificación humana vinculada a estas evidencias.

## 4. Responsibility: DOC-TESTING

**Requirement Level:** `Recommended`.

**Proposed State:** `Partial` (pendiente de aprobación).

**Proposed Applicability:** `Applicable` (pendiente de aprobación).

**Implementation Characteristics (proposed):** `Own`, `Specialized`, `Distributed`: guías especializadas de integración PostgreSQL, JaCoCo y CI SonarCloud.

**Detected Facts:**

- [POSTGRESQL_INTEGRATION_TESTS.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md) identifica el entorno y pruebas de integración con PostgreSQL.
- [JACOCO_COVERAGE_BASELINE.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/JACOCO_COVERAGE_BASELINE.md) limita la interpretación de cobertura a la selección H2 y describe cómo consultar XML/HTML.
- [SONARCLOUD_PR_CI.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SONARCLOUD_PR_CI.md) describe el análisis asociado al job H2 y advierte que el secreto `SONAR_TOKEN` puede no estar disponible.
- El log del run del commit confirma generación de informe JaCoCo y subida exitosa en aquel momento del artefacto `jacoco-h2-regression` (artifact ID `12201642997`); la consulta posterior de artefactos devolvió lista vacía.
- El paso Sonar del mismo run registra `ANALYSIS SUCCESSFUL`, con importación de JaCoCo. Este hecho **no acredita** la aprobación del Quality Gate.
- La ejecución H2 proporciona un total de 329 tests satisfactorios y resultados individuales de las clases clave; no se dispone aquí de un porcentaje JaCoCo verificado.

**Evidence:**

- [POSTGRESQL_INTEGRATION_TESTS.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md)
- [JACOCO_COVERAGE_BASELINE.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/JACOCO_COVERAGE_BASELINE.md)
- [SONARCLOUD_PR_CI.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SONARCLOUD_PR_CI.md)
- [Run 39283862407 / h2-regression](https://github.com/fran-eliot/only_film/actions/runs/39283862407/job/118164215980)
- [Registro de Surefire y Sonar verificado](only-film-verified-surefire-sonar-logs.md)

**Evaluation Rationale — propuesta, no decisión:**

Las guías especializadas y los resultados de un run inmutable permiten reconstruir parte del protocolo de testing, distinguir capas de pruebas y vincular afirmaciones a datos reales. Aun así, la documentación se reparte entre varias guías y no está acreditada una ejecución completa de todas las suites. La calidad documental no debe evaluarse automáticamente a partir de tests verdes; el reviewer necesita valorar claridad, suficiencia, mantenimiento, límites y audiencia antes de registrar un `State` definitivo.

**Uncertainty:**

- ¿Están documentadas todas las dependencias requeridas para reproducir PostgreSQL, Selenium, Compose y análisis opcionales?
- ¿Se entiende que un porcentaje JaCoCo derivado del job H2 **no es** cobertura global?
- ¿Las instrucciones de Sonar distinguen análisis enviado y Quality Gate procesado?
- ¿Es suficiente el conjunto de guías distribuidas para la finalidad de esta Responsibility?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** las fuentes especializadas aportan evidencias, pero falta decidir su suficiencia global como documentación de pruebas. Un cambio documental no se propone automáticamente.

## 5. SonarCloud: tarea histórica identificada, Quality Gate pendiente

El log de [h2-regression / run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407/job/118164215980) registra la aceptación del análisis con `ANALYSIS SUCCESSFUL` y proporciona la URL de procesamiento:

```text
https://sonarcloud.io/api/ce/task?id=AaFU8vS6n_jCCWP5LQvY
```

| Elemento | Estado observado |
| --- | --- |
| CE Task ID | `AaFU8vS6n_jCCWP5LQvY` |
| Origen | Log del scanner el 2026-10-19 |
| Resultado de envío | `ANALYSIS SUCCESSFUL` |
| Estado final de procesamiento de la CE Task | **No consultable con las fuentes disponibles** |
| Analysis ID asociado | **No obtenido** |
| Quality Gate histórico | **No verificado** |
| Dashboard actual de `main` | No constituye evidencia de aquel Quality Gate |

Se intentó consultar la tarea Sonar y la búsqueda histórica de análisis; ambas URLs resultaron inaccesibles desde los medios disponibles. Por ello **no se ha supuesto** que la tarea termine con `SUCCESS` ni que el Quality Gate esté aprobado. La secuencia de revisión, si existe acceso autorizado, es:

1. Recuperar el estado y `analysisId` del procesamiento correspondiente a la CE Task identificada.
2. Con ese identificador exacto, consultar el Quality Gate del **análisis histórico**, y registrar fuente y fecha.
3. Conservar por separado el estado del scanner, de la tarea de procesamiento y del Quality Gate; un `ANALYSIS SUCCESSFUL` del scanner no es un `Quality Gate: OK`.

## 6. Checklist de aprobación humana

| Gate | Criterio | Estado |
| --- | --- | --- |
| SR-1 | Evidence de README-TESTING examinada y contrastada con propósito de la Responsibility | Pendiente de reviewer |
| SR-2 | Scope y reproducibilidad de instrucciones de pruebas delimitados | Parcial; falta revisión |
| SR-3 | Evidence DOC-TESTING examinada, vigencia y suficiencia valoradas | Pendiente de reviewer |
| SR-4 | `State` y `Applicability` de ambas Responsibilities aprobados o corregidos | Pendiente |
| SR-5 | `Evaluation Rationale` y `Uncertainty` registrados en Assessment de forma individual | Pendiente |
| SR-6 | `Decision Status` y eventual `Adoption Decision` justificados | Pendiente |
| SR-7 | Si se requiere para el alcance, Quality Gate histórico verificado o incertidumbre explícita | Pendiente |

El reviewer puede confirmar `Partial` o cambiarlo a `Satisfied`/`Missing` con un razonamiento explícito. No hay aprobación humana registrada en este documento.

## 7. Conclusión

Estas dos Responsibilities cuentan ya con una **propuesta semántica estructurada y evidencias E2 más fuertes**. Los campos siguen en calidad de propuesta; no se alteran los valores definitivos del Assessment ni se declara conformidad o autorización de Application/Integration.

`Assessment Status: In Progress` — `Decision Status: Needs Further Evaluation` — `Adoption Decision: —`.
