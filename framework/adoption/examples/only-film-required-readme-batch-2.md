# Only Film — Assessment Batch 2: Remaining Required Responsibilities

## 1. Contexto

Este documento recoge una **exploración documental read-only** de las cuatro responsabilidades `Required` de `TPL-BACKEND` 0.1.0 pendientes de inspección tras el [primer lote](only-film-required-readme-batch-1.md).

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND metadata 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Responsibilities | `README-TECH-STACK`, `README-DOCUMENTATION`, `README-FOOTER`, `DOC-CHANGELOG` |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |

Se comparan hechos observables con las responsabilidades definidas por [Tech Stack](../../components/readme/tech-stack/README.md), [Documentation](../../components/readme/documentation/README.md), [Footer](../../components/readme/footer/README.md) y [Changelog](../../components/documentation/changelog/README.md). La presencia o ausencia de un nombre de archivo **no permite decidir por sí sola** si una Responsibility está satisfecha.

## 2. Resumen de cobertura del lote

| Responsibility | Requirement Level | Cobertura | State / Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-TECH-STACK` | `Required` | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `README-DOCUMENTATION` | `Required` | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `README-FOOTER` | `Required` | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `DOC-CHANGELOG` | `Required` | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |

`Explored — provisional` es una etiqueta de **cobertura del trabajo**, no un `State` del contrato de Assessment. No se han declarado valores definitivos para `Satisfied`, `Partial`, `Missing`, `Applicable` o `Not Applicable`.

## 3. README-TECH-STACK

**Detected Facts**

- El README contiene `## Tecnologías y arquitectura`, con una tabla por capas: Backend, Seguridad, Frontend, Persistencia local rápida, Persistencia duradera, Pruebas e Infraestructura.
- Entre las tecnologías declaradas figuran Java 25, Spring Boot 4.0.5, Spring Security, Thymeleaf, H2, PostgreSQL 17, Flyway, Docker Compose y GitHub Actions.
- El `pom.xml` del commit declara Java 25 y Spring Boot parent 4.0.5, coherentes con algunas referencias documentales. Esto no verifica el stack completo ni su funcionamiento.

**Evidence**

- [README.md — Tecnologías y arquitectura](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [pom.xml — versiones declaradas](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)

**Evaluation Rationale:** el contenido observado se relaciona con la presentación del stack tecnológico por categorías. Su exactitud y suficiencia para los consumidores del README requiere revisión; la coincidencia entre algunas versiones documentadas y el POM no valida todas las dependencias.

**Uncertainty:** ¿se representan correctamente las tecnologías realmente usadas? ¿se distinguen las dependencias de ejecución, desarrollo, test e infraestructura sin generar expectativas erróneas?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 4. README-DOCUMENTATION

**Detected Facts**

- El README incluye enlaces a `docs/screenshots/`, `docs/POSTGRESQL_SETUP.md`, `docs/SECURITY_HARDENING_AUDIT.md` y `docs/POSTGRESQL_INTEGRATION_TESTS.md`.
- Incluye referencias a workflows de GitHub Actions y a documentación de arquitectura, guías, auditorías y pruebas mediante la sección `Organización del repositorio`.
- El árbol del commit contiene `docs/` con documentos técnicos y subdirectorios, como `docs/security/` y `docs/testing/`.
- No se observa en el README una sección única con título literal `Documentation`, pero hay referencias distribuidas en varias secciones.

**Evidence**

- [README.md — enlaces de documentación y organización](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [docs/POSTGRESQL_SETUP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)
- [docs/POSTGRESQL_INTEGRATION_TESTS.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md)

**Evaluation Rationale:** existe una navegación distribuida hacia documentos relevantes. Hace falta una revisión humana para determinar si esa organización facilita suficientemente el acceso a la documentación prevista; la ausencia del encabezado literal no obliga a considerar ausente la Responsibility.

**Uncertainty:** ¿puede localizar un contribuidor nuevo los documentos principales? ¿existen enlaces obsoletos, omisiones o duplicidades importantes?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 5. README-FOOTER

**Detected Facts**

- El final del README contiene un apartado de origen, créditos y evolución que reconoce al equipo académico del proyecto original y enlaza al repositorio de procedencia.
- Incluye un apartado sobre líneas futuras de evolución, expresamente diferenciadas de las funcionalidades implantadas.
- La línea final contiene una nota de licencia que remite al repositorio original y aclara que el README por sí solo no establece otra licencia.
- No se observan condiciones de licencia completas en esa línea; la validez del régimen de licencias no ha sido evaluada.

**Evidence**

- [README.md — créditos, evolución y nota final de licencia](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Repositorio de origen citado en el README](https://github.com/certidevs/g1_testing) (referencia externa; no forma parte del commit inspeccionado)

**Evaluation Rationale:** aparecen contenidos típicos de un Footer (créditos, enlaces relacionados y nota de licencia), pero corresponde al reviewer valorar claridad, ubicación y suficiencia, especialmente ante la atribución del trabajo colaborativo.

**Uncertainty:** ¿es suficiente la referencia de licencia para el uso previsto? ¿conviene agrupar la información final sin perder atribución ni contexto?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 6. DOC-CHANGELOG

**Detected Facts**

- El árbol Git inspeccionado en el commit fijado **no contiene ningún archivo cuyo nombre incluya `CHANGELOG`, `CHANGES` o `HISTORY`**.
- El README alude a la evolución técnica posterior del proyecto, pero no presenta una cronología estructurada de cambios publicados entre versiones.
- El repositorio contiene numerosos documentos de auditoría técnica, cambios y decisiones. Su contenido no ha sido examinado aquí para determinar si alguno cumple una función equivalente a un Changelog.
- El contrato `DOC-CHANGELOG` pretende comunicar cambios relevantes publicados, no reproducir todo el historial de commits.

**Evidence**

- [Árbol del consumer fijado al commit](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)
- [README.md — origen y evolución](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Especificación del Component Changelog](../../components/documentation/changelog/README.md)

**Evaluation Rationale:** la ausencia de un archivo con nombre canónico es un hecho observable de esta inspección, **no una conclusión automática `Missing`**. Aún puede existir otra fuente oficial de cambios (por ejemplo, releases o documentación equivalente), cuya disponibilidad y suficiencia requieren comprobación.

**Uncertainty:** ¿se publican versiones diferenciadas y cómo se comunica su evolución? ¿hay release notes u otro registro oficial que cumpla la Responsibility? ¿es necesaria una adaptación documental?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

**Evidence follow-up — DOC-CHANGELOG:** el [examen específico de Changelog y versiones](only-film-changelog-evidence-review.md) contrasta README, POM, árbol, commits y GitHub Releases del consumidor, señalando expresamente que la consulta de tags no se pudo completar. No altera el `State` ni la `Adoption Decision` pendientes.

## 7. Conclusión y siguientes verificaciones

| Verificación | Resultado |
| --- | --- |
| Contrato de cuatro Responsibilities `Required` identificado | Documentado |
| Fuentes del README y árbol Git vinculadas a SHA fijo | Documentado |
| Evidencias separadas de interpretaciones | Documentado |
| Incertidumbres por Responsibility | Documentadas |
| Revisión semántica humana | Pendiente |
| Runtime/build/test verification | No realizada |
| Adoption Decisions resueltas | Ninguna |

Con este lote, la [matriz de cobertura](only-film-assessment-coverage.md) pasa de 5/28 a **9/28 Responsibilities exploradas documentalmente**, incluidas las **8/8 Required**. Las otras **19** siguen sin explorar (6 Recommended y 13 Optional).

**Cobertura documental de Required: 8/8 no significa cumplimiento 8/8.** Los Estados y las decisiones no se han resuelto. El Assessment sigue `In Progress`; este documento no autoriza Application, Integration ni modificación del consumer.
