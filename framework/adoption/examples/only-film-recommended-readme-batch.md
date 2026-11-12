# Only Film — Assessment Batch 3: Recommended README Responsibilities

## 1. Contexto y alcance

Este lote amplía la inspección documental de `fran-eliot/only_film` con tres Responsibilities `Recommended` del Template `TPL-BACKEND` 0.1.0. Se utiliza exclusivamente la referencia inmutable `28d75a50e0a178954dd46acc23300d9dd327843c` y no se modifica el repositorio consumidor.

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Commit SHA | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Collection Scope | `README-STATUS`, `README-ARCHITECTURE`, `README-REPOSITORY-STRUCTURE` |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |

Las tres Responsibilities se han **explorado documentalmente**, no evaluado como conformes. `Explored — provisional` es una etiqueta de cobertura y no un `State` válido del Assessment Template.

## 2. Resumen del lote

| Responsibility | Requirement Level | Cobertura | State | Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- | --- |
| `README-STATUS` | `Recommended` | Explored — provisional | Pendiente de revisión | Pendiente de revisión | `Needs Further Evaluation` | `—` |
| `README-ARCHITECTURE` | `Recommended` | Explored — provisional | Pendiente de revisión | Pendiente de revisión | `Needs Further Evaluation` | `—` |
| `README-REPOSITORY-STRUCTURE` | `Recommended` | Explored — provisional | Pendiente de revisión | Pendiente de revisión | `Needs Further Evaluation` | `—` |

## 3. README-STATUS

**Responsabilidad del Framework:** [README-STATUS](../../components/readme/status/README.md) comunica estado operativo y nivel de madurez del repositorio.

**Detected Facts**

- La cabecera del README incluye badges que identifican tecnologías y versiones: Java 25, Spring Boot 4.0.5, PostgreSQL 17, Flyway y Docker Compose.
- El README contiene una sección `Pruebas y CI` que enumera workflows de regresión, migración, Compose y análisis estático.
- El texto distingue algunas funcionalidades presentes de futuras líneas de evolución.
- En el contenido inspeccionado no se identifica una declaración explícita y unificada de `project_status` o `maturity` como la prevista en el Component STATUS.
- Los badges citados identifican tecnologías; **no** acreditan por sí mismos el estado operativo, la salud de CI ni el nivel de madurez.

**Evidence**

- [README.md — cabecera, pruebas y evolución](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Directorio de workflows en el commit](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows)

**Evaluation Rationale (pendiente)**

Existen referencias a tecnologías, CI y evolución, pero no se ha examinado una declaración de madurez ni evidencia de ejecución de workflows para determinar si cumplen la Responsibility. No se debe inferir un resultado `Missing` por la ausencia de una sección literal STATUS.

**Uncertainty**

- ¿Cuál es la fuente oficial del estado operativo y de la madurez del consumer?
- ¿Hay badges de CI, indicadores o documentación equivalente en otros artefactos?
- ¿Se necesita un apartado específico o basta con una representación distribuida y revisada?

**State / Applicability:** pendientes de evaluación humana.

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

## 4. README-ARCHITECTURE

**Responsabilidad del Framework:** [README-ARCHITECTURE](../../components/readme/architecture/README.md) resume la arquitectura general sin sustituir la documentación técnica profunda.

**Detected Facts**

- En `Tecnologías y arquitectura`, el README identifica capas de backend, seguridad, frontend, persistencia, pruebas e infraestructura.
- Se describe un flujo principal: `Controlador MVC → servicio / reglas de negocio → repositorio JPA → base de datos`.
- Se citan las entidades `Movie`, `Room`, `Session`, `Ticket`, `Review` y `User`.
- El árbol del commit contiene documentación adicional, incluida `docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md`, cuyo contenido completo no forma parte de esta inspección.
- La presencia de una descripción arquitectónica no demuestra que el sistema ejecutado corresponda exactamente a ella.

**Evidence**

- [README.md — Tecnologías y arquitectura](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) (ruta observada; contenido no evaluado aquí)

**Evaluation Rationale (pendiente)**

La descripción de capas y del flujo MVC/JPA es una observación documental relevante. Falta revisar su precisión, legibilidad y alcance; tampoco se ha contrastado con el código ejecutado ni con la documentación técnica.

**Uncertainty**

- ¿La descripción refleja correctamente las dependencias entre módulos y las decisiones arquitectónicas actuales?
- ¿Es suficiente el nivel de abstracción del README para lectores nuevos?
- ¿Qué partes deben delegarse a documentos técnicos especializados?

**State / Applicability:** pendientes de evaluación humana.

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

## 5. README-REPOSITORY-STRUCTURE

**Responsabilidad del Template:** `README-REPOSITORY-STRUCTURE` aparece como `Recommended` en la [metadata canónica](../../templates/repositories/backend/metadata.yml).

**Detected Facts**

- El README contiene la sección `Organización del repositorio` con un árbol resumido de directorios y archivos.
- Se enumeran `src/main/java/com/demo/`, `src/main/resources/`, `src/test/java/com/demo/`, `docs/`, `.github/workflows/`, `Dockerfile`, `compose.yaml` y `.env.example`.
- La inspección del árbol Git fijado confirma la presencia de los directorios `src/`, `docs/`, `.github/workflows/` y los archivos raíz indicados.
- No se ha realizado una comprobación exhaustiva de todos los subdirectorios, ni se ha verificado que la explicación siga siendo suficiente para cada perfil de contribuidor.

**Evidence**

- [README.md — Organización del repositorio](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Árbol Git del commit inspeccionado](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)

**Evaluation Rationale (pendiente)**

La estructura descrita en el README puede ayudar a navegar el repositorio y se relaciona con la Responsibility. La existencia del árbol no prueba que el nivel de detalle sea adecuado o que no existan omisiones importantes.

**Uncertainty**

- ¿La estructura resumida representa suficientemente las partes relevantes para nuevos contribuidores?
- ¿Deben figurar rutas de migraciones, configuración y pruebas especializadas con mayor detalle?
- ¿Se conserva coherencia con la organización actual cuando avance el consumer?

**State / Applicability:** pendientes de evaluación humana.

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

## 6. Conclusión y siguientes pasos

| Check | Resultado |
| --- | --- |
| Tres Responsibilities Recommended identificadas | Documentado |
| Detected Facts y Evidence en referencia inmutable | Documentados |
| Interpretaciones e incertidumbres separadas | Documentadas |
| Conformidad semántica aprobada por reviewer | Pendiente |
| Builds, tests y despliegue del consumer | No ejecutados |
| Adoption Decisions | Ninguna resuelta |

La [matriz de cobertura](only-film-assessment-coverage.md) pasa de **9/28 a 12/28 Responsibilities exploradas**: 8/8 Required, 4/7 Recommended y 0/13 Optional. Siguen **16/28 sin explorar**, incluidas tres Recommended y trece Optional.

**La cobertura documental no implica conformidad con el Template.** El Assessment permanece `In Progress`; este lote no autoriza Application ni Integration ni altera el consumer.
