# Only Film — Provisional Semantic Review: Final Optional Technical Responsibilities

## 1. Contexto

Este lote propone la evaluación semántica E3 de las cinco Responsibilities `Optional` que faltaban de `TPL-BACKEND` 0.1.0. El consumer se estudia **read-only**, en su commit inmutable. Todas las propuestas permanecen **pendientes de aprobación humana**, sin resolver Adoption Decisions.

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Scope | `DOC-ADR`, `DOC-API`, `DOC-DATABASE`, `DOC-DEPLOYMENT`, `DOC-REFERENCES` |
| Assessment Status | `In Progress` |
| Review Status | `Proposal — pending human review` |
| Reviewer / Approval Date | Sin asignar / sin aprobar |
| Mutation | `NONE` |

El catálogo inspeccionado contiene un [Component DOC-REFERENCES](../../components/documentation/references/README.md), pero no se localizaron componentes autónomos de DOC-ADR, DOC-API, DOC-DATABASE ni DOC-DEPLOYMENT en las rutas esperadas del Framework. Se emplean sus IDs y nivel Optional declarados en la metadata del Template y el propósito de las responsabilidades, **sin atribuir requisitos de Component inexistentes**.

## 2. Propuestas resumidas

| Responsibility | Level | Proposed State | Proposed Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `DOC-ADR` | Optional | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `DOC-API` | Optional | **Por decidir entre `Missing` / `Partial`** | **Por decidir** | `Needs Further Evaluation` | `—` |
| `DOC-DATABASE` | Optional | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `DOC-DEPLOYMENT` | Optional | `Partial` — provisional | `Applicable` al entorno local documentado — provisional | `Needs Further Evaluation` | `—` |
| `DOC-REFERENCES` | Optional | `Partial` — provisional | **Por decidir** según necesidad de centralización | `Needs Further Evaluation` | `—` |

Un `State` provisional no representa una deficiencia demostrada. En las filas sin hipótesis seleccionada, la incertidumbre no se rellena con un valor arbitrario: el reviewer deberá escoger un valor contractual tras confirmar su contexto y evidencia.

## 3. Responsibility — DOC-ADR

**Implementation Characteristics (proposed):** `Own`, `Distributed`: registros temáticos de decisiones y restricciones sin repositorio ADR formal acreditado.

**Detected Facts:**

- [FLYWAY_V2_SEAT_UNIQUENESS.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md) explica la regla `UNIQUE(session_id, fila, seat)`, la preservación de V1, una consulta previa de duplicados, precauciones con `NULL` y el tratamiento no destructivo de colisiones.
- [DEPENDENCY_MAINTENANCE.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md) describe decisiones operativas sobre Dependabot semanal, separación de actualizaciones mayores y ausencia de auto-merge.
- La [auditoría histórica de arquitectura](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) presenta alternativas de mejora y riesgos, pero su referencia de partida no es el SHA evaluado.
- El árbol explorado no identificó una ruta `adr/` o archivos `ADR-*`. Esto **no descarta** decisiones documentadas en otras rutas.

**Evidence:** [documento Flyway V2](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md), [mantenimiento de dependencias](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md), [lote E1 original](only-film-optional-technical-batch.md).

**Evaluation Rationale — propuesta:** hay justificaciones de decisiones técnicas y consecuencias reales (por ejemplo, no reescribir V1 y auditar antes de V2). Sin embargo, no se ha acreditado un registro homogéneo de *contexto, alternativas, decisión, consecuencias y vigencia* de las decisiones arquitectónicas principales. El nivel Optional permite ponderar si un ADR formal aporta valor frente a la información ya disponible.

**Uncertainty:** ¿Qué decisiones relevantes son duraderas y no están explicadas? ¿Conviene un índice ADR o enlazar documentos existentes? ¿Las alternativas históricas siguen vigentes?

**Proposed State:** `Partial`; **Proposed Applicability:** `Applicable`, pendientes de reviewer.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 4. Responsibility — DOC-API

**Implementation Characteristics (proposed):** no acreditadas como contrato de API pública; interfaces HTTP MVC no implican automáticamente API REST documentada.

**Detected Facts:**

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) define Only Film como aplicación MVC con Thymeleaf, rutas de interfaz y autenticación por sesión.
- `API REST` aparece en el README bajo **`Próximas líneas de evolución`**, descrita como ampliación potencial y no como prestación implementada en el SHA.
- El árbol muestra controladores Spring MVC, sin que su existencia por sí sola pruebe un contrato HTTP público para integradores.
- La inspección previa no identificó rutas con nombre `openapi` o `swagger`; **no es** una auditoría exhaustiva de todas las rutas ni prueba definitiva de ausencia de API.

**Evidence:** [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [directorio de controladores](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller), [exploración E1](only-film-optional-technical-batch.md).

**Evaluation Rationale — propuesta:** no se debe crear documentación de una API REST inexistente por una simple expectativa del Template. Tampoco se atribuye `Not Applicable` automáticamente, pues el reviewer puede determinar si contratos HTTP, integraciones o flujos de usuario justifican documentación de interfaz aunque la web esté renderizada en servidor. Hasta delimitar el concepto de API relevante, `State` y `Applicability` permanecen sin seleccionar.

**Uncertainty:** ¿Hay endpoints JSON/REST expuestos no recogidos en el README? ¿Es necesario documentar contratos MVC para contribuidores, o la navegación y pruebas son suficientes? ¿Cuándo se introduciría realmente una API pública?

**Proposed State:** sin elegir entre `Missing`/`Partial`; **Proposed Applicability:** sin decidir entre `Applicable`/`Not Applicable`.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 5. Responsibility — DOC-DATABASE

**Implementation Characteristics (proposed):** `Own`, `Specialized`, `Distributed` — guía de configuración PostgreSQL, documento de migración Flyway y esquema versionado.

**Detected Facts:**

- [POSTGRESQL_SETUP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) distingue H2, `dev`, `postgres`, `postgres,demo`, variables de conexión, Flyway y `ddl-auto=validate`.
- [FLYWAY_V2_SEAT_UNIQUENESS.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md) documenta una invariante de esquema, consulta SQL de auditoría de colisiones y restricciones del despliegue de V2.
- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) nombra entidades `Movie`, `Room`, `Session`, `Ticket`, `Review` y `User`, y diferencia persistencia H2 de PostgreSQL.
- La ejecución identificada [39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) tiene checks `postgres-schema` y `PostgreSQL JPA and concurrent checkout` con `success` para el SHA. No sustituye revisión de suficiencia documental del modelo de datos.

**Evidence:** [configuración PostgreSQL](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md), [Flyway V2](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md), [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [CI fijado](https://github.com/fran-eliot/only_film/actions/runs/39283862407), [lote E1](only-film-optional-technical-batch.md).

**Evaluation Rationale — propuesta:** existe documentación significativa de configuración, operación de migraciones e invariantes concretas. Falta determinar si ofrece al lector una visión adecuada de relaciones, ciclos de vida, restricciones y modelo conceptual sin depender solo de SQL o clases JPA. `Partial` es una hipótesis prudente, no una declaración de que el esquema falla.

**Uncertainty:** ¿Qué relaciones y reglas de dominio deben resumirse para un nuevo colaborador? ¿Los documentos reflejan V1/V2 y los perfiles del SHA sin contradicciones? ¿Es útil un ERD o basta una explicación textual?

**Proposed State:** `Partial`; **Proposed Applicability:** `Applicable`, pendientes de aprobación.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 6. Responsibility — DOC-DEPLOYMENT

**Implementation Characteristics (proposed):** `Own`, `Specialized`, `Distributed`: README, guía PostgreSQL, Dockerfile y Compose limitados al desarrollo local.

**Detected Facts:**

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) y [POSTGRESQL_SETUP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) describen `docker compose up --build -d`, `.env`, conexión PostgreSQL, precauciones con `docker compose down -v` y URL local.
- [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) define servicios `app` y `postgres`, healthcheck, volúmenes `postgres_data` y `uploads_data`, y puertos enlazados a `127.0.0.1`.
- El README afirma que Compose **no está preparado como configuración de producción expuesta a Internet**. No hay verificación de despliegue productivo, backup/restauración o rollback operativos.
- El [workflow compose-smoke.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/compose-smoke.yml) define comprobaciones de arranque y persistencia, pero en los checks consultados del SHA **no consta un smoke Compose asociado directamente**.
- **Posible discrepancia documental interna:** la sección `Seguridad y límites` de POSTGRESQL_SETUP aún dice que la aplicación «no cuenta con una estrategia definitiva de persistencia de ficheros subidos al contenedor», pese a que secciones anteriores del mismo documento describen explícitamente el volumen persistente `uploads_data`. Esta afirmación requiere revisión contextual: persistencia local por volumen no equivale a una estrategia productiva completa.

**Evidence:** [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [guía PostgreSQL](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md), [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml), [Dockerfile](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/Dockerfile), [laguna Compose E2](only-film-compose-evidence-gap.md).

**Evaluation Rationale — propuesta:** existen instrucciones técnicas claras para un entorno local y límites explícitos que evitan presentar el stack como apto para producción. La suficiencia de `DOC-DEPLOYMENT` debe juzgarse conforme al entorno **realmente soportado**; no imponer pipelines productivos que el consumer no ofrece. La aparente contradicción sobre uploads y la ausencia de smoke Compose acreditado justifican revisión, sin convertirla en fallo de ejecución probado.

**Uncertainty:** ¿Cuál es el escenario de operación soportado (solo local o demo online)? ¿La advertencia de uploads se refiere a durabilidad productiva o está desactualizada? ¿Qué verificación y recuperación necesita el usuario objetivo para ese escenario?

**Proposed State:** `Partial`; **Proposed Applicability:** `Applicable` al despliegue local documentado, ambos provisionales.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 7. Responsibility — DOC-REFERENCES

**Implementation Characteristics (proposed):** `Own`, `Distributed` — enlaces presentes en documentos temáticos, sin índice central acreditado.

**Detected Facts:**

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) enlaza al repositorio académico de origen, guías técnicas propias y workflows.
- Documentos especializados mencionan tecnologías e integraciones como PostgreSQL, Flyway, Maven, SonarCloud y Dependabot; ello **no prueba que todas tengan enlaces a fuentes oficiales externas** ni que sea útil centralizarlas.
- El [Component DOC-REFERENCES](../../components/documentation/references/README.md) recomienda referencias primarias, finalidad y contexto claros, y señala expresamente que **no es necesario** cuando son pocas o permanecen más claras junto a su uso.
- La inspección de rutas no identificó archivo separado `REFERENCES`, sin que ello demuestre ausencia de fuentes útiles.

**Evidence:** [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [guía PostgreSQL](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md), [mantenimiento de dependencias](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md), [Component References](../../components/documentation/references/README.md), [lote E1](only-film-optional-technical-batch.md).

**Evaluation Rationale — propuesta:** los enlaces contextuales pueden satisfacer las necesidades reales sin un índice global. El `Partial` propuesto refleja **solo** que la función de selección y mantenimiento de fuentes externas no ha sido valorada exhaustivamente. La aplicabilidad se mantiene abierta: un catálogo central podría añadir complejidad sin beneficio.

**Uncertainty:** ¿Existen estándares externos relevantes que requieren trazabilidad estable? ¿Hay URLs repetidas u obsoletas? ¿Para el público real, un índice mejoraría la navegación o duplicaría enlaces dispersos adecuados?

**Proposed State:** `Partial`; **Proposed Applicability:** por decidir entre `Applicable`/`Not Applicable`, pendiente de reviewer.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 8. Human Review Gates

| Gate | Revisión | Estado |
| --- | --- | --- |
| OT-1 | Determinar con evidencia contexto, alcance y Applicability de cada Optional | Pendiente |
| OT-2 | Contrastar documentación de decisiones técnicas con decisiones vigentes; evitar ADR por formalismo | Pendiente |
| OT-3 | Verificar si existe API pública relevante y qué contrato necesita documentación | Pendiente |
| OT-4 | Valorar suficiencia documental de modelo relacional, migraciones y entornos | Pendiente |
| OT-5 | Aclarar advertencia de uploads y umbral de reproducibilidad de Compose para entorno local | Pendiente |
| OT-6 | Valorar necesidad real de referencias externas centralizadas | Pendiente |
| OT-7 | Aprobar/corregir State y Applicability con Evaluation Rationale y Uncertainty por Responsibility | Pendiente |
| OT-8 | Resolver o mantener pendiente cada Adoption Decision con autorización y trazabilidad | Pendiente |

## 9. Cobertura semántica propuesta: 28/28

| Grupo | Responsibilities | Propuestas E3 documentadas | Evaluaciones humanas aprobadas |
| --- | ---: | ---: | ---: |
| Required | 8 | 8 | 0 acreditadas |
| Recommended | 7 | 7 | 0 acreditadas |
| Optional | 13 | 13 | 0 acreditadas |
| **TOTAL** | **28** | **28** | **0 acreditadas** |

**Rutas de propuestas E3:**

- Required: [Hero/Overview/Features](only-film-required-identity-semantic-review.md), [Quick Start/Changelog](only-film-required-semantic-review.md), [Tech Stack/Documentation/Footer](only-film-required-final-semantic-review.md).
- Recommended: [Status/Architecture/Structure](only-film-recommended-readme-semantic-review.md), [Testing](only-film-testing-semantic-review.md), [Architecture/Project Status](only-film-recommended-docs-semantic-review.md).
- Optional: [Security](only-film-security-semantic-review.md), [Governance](only-film-optional-governance-semantic-review.md), [Demo/Highlights/Diagrams](only-film-optional-showcase-semantic-review.md), y este lote técnico.

Las propuestas incluyen hipótesis no discriminadas, como `DOC-CHANGELOG`, `README-CONTRIBUTING`, `DOC-DIAGRAMS` y `DOC-API`. Por tanto, **28 propuestas no significan 28 States seleccionados o aprobados**. El trabajo posterior es validar, corregir, priorizar y registrar decisiones individualmente con revisión humana, no declarar automáticamente `Assessment Complete`.

## 10. Conclusión

Se prepararon interpretaciones E3 para las 28 Responsibilities del Template a partir de evidencia disponible y sus límites. La revisión semántica **aprobada** y las Adoption Decisions **continúan pendientes**. El Assessment sigue `In Progress` y no se ha modificado, desplegado ni ejecutado nuevamente el consumer.
