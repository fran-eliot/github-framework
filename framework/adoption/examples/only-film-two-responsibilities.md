# Worked Example — Two Backend Responsibilities in Only Film

Este ejemplo documenta una inspección **read-only** de un repositorio consumidor para probar la trazabilidad de Evidence y el uso del Assessment Core sobre más de una Responsibility.

No representa un Assessment completo, una validación funcional de la aplicación ni una autorización para modificar el consumer. Se conserva un estado parcial y las Adoption Decisions permanecen sin resolver.

## 1. Assessment Context

| Field | Value |
| --- | --- |
| Consumer Repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Repository Template | `TPL-BACKEND` |
| Template Version | `0.1.0` |
| Assessment Date | `2026-11-12` |
| Assessment Status | `In Progress` |
| Collection Scope | `README-QUICK-START` y `README-TESTING` |
| Mutation | `NONE` |

El Template y su versión proceden de [metadata canónica de TPL-BACKEND](../../templates/repositories/backend/metadata.yml). El commit del consumer es un identificador inmutable; **no** se ha utilizado el estado mutable actual de `main` como fuente de Evidence.

## 2. Assessment Summary (partial)

| Responsibility | Requirement Level | State | Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-QUICK-START` | `Required` | `Partial` (provisional, pendiente de verificación) | `Applicable` | `Needs Further Evaluation` | `—` |
| `README-TESTING` | `Recommended` | `Partial` (provisional, pendiente de verificación) | `Applicable` | `Needs Further Evaluation` | `—` |

Los Estados se utilizan exclusivamente como hipótesis de trabajo para ejemplificar el proceso de revisión. La mera presencia de instrucciones no acredita que funcionen. Un reviewer puede reclasificarlos tras verificar su alcance y eficacia.

## 3. Responsibility Details — README-QUICK-START

**Requirement Level:** `Required`

**State:** `Partial`, provisional.

**Applicability:** `Applicable`.

**Implementation Characteristics:** `Own`, con instrucciones distribuidas entre el README y guías técnicas.

**Uncertainty:**

- ¿El arranque con Docker Compose se ejecuta correctamente desde un clon limpio en un entorno compatible?
- ¿Están completas las condiciones de configuración necesarias y documentadas las limitaciones de seguridad para el usuario objetivo?
- ¿El flujo alternativo con Maven/JDK 25 produce la misma aplicación sin dependencias de entorno no declaradas?

**Detected Facts:**

- El README incluye una sección titulada «Inicio rápido: aplicación y PostgreSQL con Docker».
- El ejemplo de terminal incluye `git clone`, copia de `.env.example`, `docker compose up --build -d` y `docker compose ps`.
- El README indica la URL `http://localhost:8080/movies`, explica perfiles Spring y contiene instrucciones alternativas de desarrollo con Maven.
- El árbol del commit incluye `Dockerfile`, `compose.yaml`, `.env.example`, `mvnw`, `mvnw.cmd` y `docs/POSTGRESQL_SETUP.md`.
- El `pom.xml` define `java.version=25` y usa Spring Boot parent `4.0.5`.

**Evidence — consumer commit fijado:**

- [README.md — Inicio rápido y desarrollo](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [pom.xml — configuración Java/Spring Boot](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml)
- [docs/POSTGRESQL_SETUP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)

**Evaluation Rationale:**

Hay instrucciones de puesta en marcha observables y artefactos de soporte. Sin ejecución controlada no puede certificarse la suficiencia ni reproducibilidad del Quick Start. El Estado `Partial` se mantiene deliberadamente provisional y sujeto a revisión.

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale:** Falta comprobar las instrucciones en un entorno aislado antes de decidir `PRESERVE` o `ADAPT`. Ninguna de esas decisiones se infiere automáticamente de los archivos encontrados.

## 4. Responsibility Details — README-TESTING

**Requirement Level:** `Recommended`

**State:** `Partial`, provisional.

**Applicability:** `Applicable`.

**Implementation Characteristics:** `Own`, `Distributed`.

**Uncertainty:**

- ¿Qué conjunto de pruebas es reproducible con las dependencias y servicios disponibles?
- ¿Cuáles de los workflows se ejecutan automáticamente y cuáles son manuales en el commit revisado?
- ¿Qué cobertura o resultados vigentes pueden verificarse mediante ejecuciones identificadas, sin depender de cifras históricas?

**Detected Facts:**

- El README contiene «Pruebas y CI» e indica `./mvnw test` y ejemplos de filtrado de tests por categoría.
- El README advierte que algunas pruebas requieren servicios externos, entorno gráfico/headless o configuración específica.
- La tabla del README menciona workflows para regresión de tickets, migraciones PostgreSQL, smoke de Compose, datos demo, suite general y Sonar.
- El árbol del commit incluye `.github/workflows/tests.yml`, `ticket-regression.yml`, `postgres-migration.yml`, `compose-smoke.yml`, `postgres-demo-seed.yml` y `sonar.yml`.
- El `pom.xml` declara dependencias de test de Spring Boot y JUnit Platform. Estas declaraciones no son evidencia de que la suite completa pase.

**Evidence — consumer commit fijado:**

- [README.md — Pruebas y CI](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [tests.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/tests.yml)
- [ticket-regression.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/ticket-regression.yml)
- [docs/POSTGRESQL_INTEGRATION_TESTS.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md)

**Evaluation Rationale:**

Existen instrucciones y artefactos relacionados con testing. Queda por verificar si el conjunto documentado satisface la Responsibility en la práctica, y si las distinciones entre tests locales, integraciones y ejecuciones CI son suficientes para el público del repositorio. La clasificación `Partial` es provisional.

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale:** No se ha verificado ejecución alguna de la suite; por ello no se registra una decisión de conservación o adaptación de la documentación.

## 5. Assessment Conclusion (partial)

**Assessment Status:** `In Progress`.

**Major Findings:**

- En una referencia inmutable existen instrucciones documentadas de puesta en marcha y testing.
- La información puede vincularse a fuentes concretas sin editar el consumer.
- La existencia de artefactos no equivale a satisfacción demostrada de una Responsibility.

**Open Uncertainties:** reproducibilidad del Quick Start, verificabilidad de las pruebas, resultados de CI en el commit, y evaluación de las demás Responsibilities exigidas por `TPL-BACKEND`.

**Recommended Next Review:** reproducir el arranque y tests en entorno aislado, comprobar evidencia de los workflows del commit y completar la revisión del resto de Responsibilities del Template.

## 6. Límites y reproducibilidad

Se inspeccionaron contenido de `README.md` y `pom.xml`, y estructura de archivos de Git en el commit indicado. Las rutas adicionales se enlazan como referencias de consulta; no se afirma que se haya auditado íntegramente su contenido.

**No se ejecutaron builds ni tests, no se realizó despliegue, no se cambió ningún archivo del consumer, no se creó un candidato de Application ni se emitió una Adoption Decision.**

La inspección de dos Responsibilities no permite declarar `Assessment Complete`. Para continuar, utilizar el [Assessment Template](../assessment-template.md) y las reglas de cierre de la [guía de adopción](../README.md).
