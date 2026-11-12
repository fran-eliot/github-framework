# Only Film — Assessment Batch 7: Optional Technical Documentation

## 1. Contexto

Este último lote explora las seis responsabilidades `Optional` todavía pendientes de `TPL-BACKEND` 0.1.0. El ámbito de inspección es **read-only**, limitado a fuentes del commit inmutable de Only Film indicado abajo; no se ejecutan comandos sobre el consumidor.

| Campo | Valor |
| --- | --- |
| Consumer Repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Scope | `DOC-ADR`, `DOC-API`, `DOC-DATABASE`, `DOC-DEPLOYMENT`, `DOC-SECURITY`, `DOC-REFERENCES` |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |

Las seis Responsibilities son `Optional` **en el Template**. Su aplicabilidad debe revisarse por separado; no se deduce `Not Applicable` por ser opcionales. `Explored — provisional` indica únicamente cobertura documental, no un `State` contractual.

## 2. Resumen provisional

| Responsibility | Requirement Level | Cobertura | State / Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `DOC-ADR` | Optional | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `DOC-API` | Optional | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `DOC-DATABASE` | Optional | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `DOC-DEPLOYMENT` | Optional | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `DOC-SECURITY` | Optional | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `DOC-REFERENCES` | Optional | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |

## 3. DOC-ADR

**Detected Facts**

- El árbol del commit incluye auditorías y documentos sobre decisiones técnicas, como `docs/FLYWAY_V2_SEAT_UNIQUENESS.md`, `docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md` y `docs/DEPENDENCY_MAINTENANCE.md`.
- El documento de Flyway V2 registra la regla de unicidad de butacas por sesión, la justificación de conservar V1 y las condiciones de migración.
- En la inspección del árbol no se identificó un directorio denominado `adr` ni archivos con un prefijo `ADR-`. La ausencia de ese nombre no demuestra por sí sola ausencia de decisiones documentadas.

**Evidence**

- [Flyway V2 — unicidad de butacas](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md)
- [Auditoría histórica de arquitectura](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md)
- [Mantenimiento de dependencias](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md)

**Evaluation Rationale (pendiente):** existen documentos que reflejan reglas y elecciones técnicas, pero no se ha verificado un registro de decisiones arquitectónicas con contexto, alternativas, consecuencias y vigencia. No es correcto asignar `Missing` automáticamente por el nombre del archivo.

**Uncertainty:** ¿qué decisiones siguen vigentes en el SHA evaluado? ¿existe un historial de decisiones explícito y revisable? ¿aportaría valor un formato ADR diferenciado?

**State / Applicability:** pendientes de revisión semántica. **Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 4. DOC-API

**Detected Facts**

- El README presenta la aplicación como web MVC con Thymeleaf, y describe sus funcionalidades y rutas de inicio para usuario.
- El apartado `Próximas líneas de evolución` indica «API REST» como **posible ampliación**, no como capacidad ya implantada.
- El árbol inspeccionado incluye controladores MVC bajo `src/main/java/com/demo/controller/`, pero su mera presencia no establece un contrato de API pública.
- No se identificó por nombre un contrato OpenAPI/Swagger en el árbol inspeccionado; tampoco se auditaron todos los endpoints o rutas de aplicación.

**Evidence**

- [README.md — tecnología, funcionalidades y evolución](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Directorio de controladores en el commit](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller)

**Evaluation Rationale (pendiente):** puede haber interfaces HTTP para la aplicación MVC, pero aún se desconoce si el consumidor necesita documentación de una API pública o de integraciones. No debe deducirse que hay una REST API operativa por observar controladores Spring.

**Uncertainty:** ¿la responsabilidad aplica a una aplicación server-rendered sin API pública documentada? ¿qué interfaces contractuales justificarían documentación adicional?

**State / Applicability:** pendientes de revisión semántica. **Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 5. DOC-DATABASE

**Detected Facts**

- `docs/POSTGRESQL_SETUP.md` explica perfiles H2/PostgreSQL, variables de entorno, conexión local, Flyway, Hibernate `validate` y límites de datos demo.
- `docs/FLYWAY_V2_SEAT_UNIQUENESS.md` documenta la regla de unicidad por `(session_id, fila, seat)`, una consulta previa de duplicados y condiciones de despliegue.
- El README incluye una tabla de persistencia local y duradera, e identifica las principales entidades.
- El árbol incluye migraciones SQL en `src/main/resources/db/migration/`; su existencia no demuestra por sí sola la consistencia de un esquema desplegado.

**Evidence**

- [Guía de PostgreSQL y configuración](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)
- [Regla Flyway V2 y validación](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md)
- [README.md — persistencia y entidades](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Directorio de migraciones](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/resources/db/migration)

**Evaluation Rationale (pendiente):** existe documentación técnica sustantiva, pero no se ha comprobado la suficiencia de un modelo conceptual, relaciones entre entidades, política de migración completa y recuperación. No se han aplicado migraciones.

**Uncertainty:** ¿qué visión del modelo de datos necesitan los nuevos contribuidores? ¿las reglas documentadas corresponden al esquema efectivo del commit y a todos sus perfiles?

**State / Applicability:** pendientes de revisión semántica. **Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 6. DOC-DEPLOYMENT

**Detected Facts**

- El README presenta un arranque local con `docker compose up --build -d`, variables privadas en `.env` y una URL en `localhost`.
- `docs/POSTGRESQL_SETUP.md` describe la ejecución de aplicación y PostgreSQL, puertos publicados en `127.0.0.1`, volúmenes persistentes y comportamiento de Flyway.
- El README advierte que la configuración de Compose está concebida para desarrollo local y **no** debe tratarse como un despliegue endurecido de producción.
- `Dockerfile`, `compose.yaml` y `.env.example` aparecen en el árbol raíz del commit.

**Evidence**

- [README.md — inicio local y límites de Compose](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [POSTGRESQL_SETUP.md — perfiles y persistencia](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)
- [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml)
- [Dockerfile](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/Dockerfile)

**Evaluation Rationale (pendiente):** las instrucciones cubren un entorno local, pero no se ha evaluado si la responsabilidad exige procesos de staging/producción, backups, restauración, secretos, observabilidad o rollback. No se ha realizado despliegue real.

**Uncertainty:** ¿cuál es el entorno de uso objetivo del consumer? ¿qué información adicional es necesaria para una operación reproducible y segura?

**State / Applicability:** pendientes de revisión semántica. **Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 7. DOC-SECURITY

**Detected Facts**

- `docs/SECURITY_HARDENING_AUDIT.md` recoge una auditoría estática del 10/10/2026 basada en un commit histórico posterior a la PR #12, con riesgos priorizados. El documento aclara que no equivale a un pentest.
- `docs/DEPENDENCY_MAINTENANCE.md` documenta Dependabot para Maven y GitHub Actions, revisión manual y ausencia de auto-merge.
- El README declara medidas de seguridad (BCrypt, CSRF, autorización por roles y validación de imágenes), así como límites de los perfiles locales y del checkout.
- `docs/DEMO_CREDENTIALS_SECURITY.md` existe en el árbol; no se deduce de su nombre el estado actual de credenciales sin revisión del contenido y de la configuración.
- El resultado de una auditoría histórica **no demuestra** que sus hallazgos sigan abiertos ni que el commit actual sea seguro.

**Evidence**

- [Auditoría histórica de seguridad](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SECURITY_HARDENING_AUDIT.md)
- [Mantenimiento de dependencias](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md)
- [README.md — seguridad y límites](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Documento de credenciales demo](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEMO_CREDENTIALS_SECURITY.md) (fuente identificada, no auditada en este lote)

**Evaluation Rationale (pendiente):** hay documentación de riesgos, medidas y operaciones de mantenimiento, pero no se ha contrastado contra el estado efectivo de controles, CI, dependencias y despliegue del SHA fijado. No constituye una auditoría de seguridad nueva.

**Uncertainty:** ¿qué controles están efectivamente implementados y verificados? ¿cuáles de los hallazgos históricos han sido corregidos y cuáles permanecen? ¿qué prácticas de divulgación, configuración y respuesta a incidentes necesitan documentarse?

**State / Applicability:** pendientes de revisión semántica. **Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 8. DOC-REFERENCES

**Detected Facts**

- El README enlaza a guías del repositorio, a workflows y al proyecto de origen `certidevs/g1_testing`.
- Las guías técnicas especializadas enlazan o mencionan tecnologías y recursos operativos (PostgreSQL, Flyway, Maven, SonarCloud, Dependabot).
- En el árbol inspeccionado no se identificó un archivo o índice denominado `REFERENCES`; esto **no** implica ausencia de referencias útiles.
- No se ha auditado un inventario completo de fuentes externas ni su vigencia o autoridad.

**Evidence**

- [README.md — enlaces de contexto y documentación](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Guía PostgreSQL](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)
- [Mantenimiento de dependencias](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md)
- [Árbol del consumer](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)

**Evaluation Rationale (pendiente):** existen enlaces distribuidos, pero la conveniencia de un índice centralizado depende de necesidades de mantenimiento y de la calidad de las fuentes. La ausencia de un documento separado no resuelve `State` ni `Applicability`.

**Uncertainty:** ¿hay referencias externas críticas que deban centralizarse? ¿sería un índice de referencias una mejora real o duplicaría enlaces existentes?

**State / Applicability:** pendientes de revisión semántica. **Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

**Seguimiento de DOC-SECURITY:** la [reconciliación de seguridad y Testing](only-film-security-testing-reconciliation.md) compara directamente controles del commit fijado con hallazgos históricos, sin declarar una auditoría de seguridad nueva ni resolver la Adoption Decision.

**Propuesta de evaluación de DOC-SECURITY:** la [revisión semántica provisional](only-film-security-semantic-review.md) ofrece `State`, `Applicability`, Characteristics, Evidence, Evaluation Rationale, Uncertainty y gates de aprobación humana. Las propuestas no cambian la situación `In Progress` ni la decisión pendiente.

**Propuesta semántica E3 posterior:** la [revisión de ADR, API, Database, Deployment y References](only-film-optional-final-semantic-review.md) completa las fichas de propuesta para las 28 Responsibilities del Template. DOC-SECURITY ya tiene una [evaluación propuesta independiente](only-film-security-semantic-review.md). Persisten hipótesis sin discriminar, aprobaciones pendientes y Adoption Decisions no resueltas.

## 9. Resultado global de la exploración documental

| Comprobación | Resultado |
| --- | --- |
| Las seis responsabilidades Optional pendientes están exploradas documentalmente | Sí |
| Evidence ligada al commit y límites de fuentes históricas documentados | Sí |
| Las 28 Responsibilities del Template cuentan con un punto de exploración documental | Sí |
| Conformidad, Applicability y State resueltos por revisión humana | **No** |
| Ejecución de builds, pruebas o despliegues del consumer | **No realizada** |
| Adoption Decisions resueltas | **Ninguna** |
| Assessment Status | **In Progress** |

La [matriz de cobertura](only-film-assessment-coverage.md) alcanza **28/28 exploradas documentalmente**: 8 Required, 7 Recommended y 13 Optional. **Esto no equivale a 28 responsabilidades conformes.**

Para cerrar el Assessment se necesita revisar los estados provisionales, comprobar la adecuación de las evidencias, refrescar hechos cuando sea necesario y cumplir las reglas de [Assessment Template](../assessment-template.md) y [Adoption Guide](../README.md). Este documento no autoriza Application, Integration ni modificación del consumer.
