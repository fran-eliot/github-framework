# Only Film — Provisional Semantic Review of Required Quick Start and Changelog

## 1. Contexto

Este documento prepara una propuesta E3 para dos Responsibilities **Required** de `TPL-BACKEND` 0.1.0, utilizando evidencias E2 trazadas al commit fijado de Only Film. **No constituye aprobación humana ni decisión de adopción**.

| Campo | Valor |
| --- | --- |
| Consumer Repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Scope | `README-QUICK-START` y `DOC-CHANGELOG` |
| Review Status | `Proposal — pending human review` |
| Reviewer / Approval | Sin asignar / no aprobada |
| Assessment Status | `In Progress` |
| Consumer Mutation | `NONE` |

La obligatoriedad deriva del Template; **no** impone automáticamente `State: Missing` cuando una ruta canónica no existe. La presencia de un archivo tampoco acredita `Satisfied`.

## 2. Resumen de propuestas

| Responsibility | Requirement Level | Proposed State | Proposed Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-QUICK-START` | `Required` | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `DOC-CHANGELOG` | `Required` | **`Missing` o `Partial` — hipótesis alternativas aún no discriminadas** | `Applicable` — provisional | `Needs Further Evaluation` | `—` |

Para `DOC-CHANGELOG`, no se asigna un `State` definitivo ni se afirma una fuente equivalente no identificada. El reviewer debe completar la investigación de tags y publicaciones y determinar qué fuentes cumplen realmente la Responsibility antes de elegir entre las hipótesis. La ausencia de datos no debe ocultarse con un `Partial` arbitrario.

## 3. Responsibility — README-QUICK-START

**Requirement Level:** `Required`.

**Proposed State:** `Partial` (hipótesis inicial, requiere confirmación).

**Proposed Applicability:** `Applicable` (hipótesis inicial).

**Implementation Characteristics (proposed):** `Own`, `Distributed` — README con instrucciones propias y soporte en guías de PostgreSQL y Docker.

### Detected Facts

- [README.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) contiene una secuencia de `git clone`, `cp .env.example .env`, definición de contraseña privada, `docker compose up --build -d`, `docker compose ps` y URL local `/movies`.
- [Dockerfile](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/Dockerfile) usa build Maven/Temurin 25 y JRE Temurin 25; [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) fija Java 25 y parent Spring Boot 4.0.5.
- [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) incluye `app` + PostgreSQL 17, perfil `postgres`, volúmenes para base y uploads, dependencia de healthcheck y puertos en `127.0.0.1`; [application-postgres.properties](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/resources/application-postgres.properties) utiliza `DB_URL`, `DB_USERNAME` y `DB_PASSWORD`.
- [`.env.example`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.env.example) declara variables de puerto, usuario y contraseña; el README advierte que hay que reemplazar el valor de ejemplo y que Compose está destinado al desarrollo local.
- El job `postgres-schema` de [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) terminó `success` para el SHA evaluado. Según [postgres-migration.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml), prueba el arranque del **JAR** sobre PostgreSQL de CI, migraciones y reinicio: **no** ejecuta el Quick Start Compose.
- Existe un workflow [compose-smoke.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/compose-smoke.yml) con `docker compose config`, build, arranque y comprobaciones HTTP y persistencia; **no se localizó un check Compose directamente asociado al SHA fijado** en los checks consultados.

### Evidence

- [Verificación de configuración y CI](only-film-pinned-quickstart-ci-verification.md)
- [Laguna y gates Q1–Q8 de Compose](only-film-compose-evidence-gap.md)
- [Walkthrough inicial](only-film-two-responsibilities.md)
- [README y guía de PostgreSQL](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)

### Evaluation Rationale — propuesta

Existe un procedimiento de arranque identificable, con versiones, variables, perfiles y restricciones de seguridad que resultan coherentes en las fuentes examinadas. El arranque de un JAR en CI aporta confianza limitada sobre el código, pero **no verifica la reproducibilidad** del flujo Docker documentado. La propuesta `Partial` mantiene abierta la cuestión de si las instrucciones son suficientes y reproducibles para el público objetivo. No es un fallo de ejecución demostrado.

### Uncertainty

- ¿El Quick Start funciona desde clon limpio, con credenciales sintéticas y entorno desechable, según gates Q1–Q8?
- ¿El usuario puede verificar fácilmente que la aplicación está lista y dispone de datos o cuentas demo cuando las necesita?
- ¿Las instrucciones alternativas con JDK/Maven y cambios de puerto explican las diferencias de entorno suficientemente?
- ¿Qué umbral de reproducibilidad exige esta Responsibility **documental** para ser `Satisfied`?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** antes de elegir `PRESERVE` o `ADAPT` el reviewer debe comprobar la suficiencia de las instrucciones e interpretar la evidencia operativa pendiente. Una ejecución de CI distinta del procedimiento documentado no resuelve por sí sola la cuestión.

## 4. Responsibility — DOC-CHANGELOG

**Requirement Level:** `Required`.

**Proposed State:** **sin seleccionar** entre `Missing` y `Partial`, ambas hipótesis de trabajo pendientes de comprobación de fuentes equivalentes; no representa un `State` formal aprobado.

**Proposed Applicability:** `Applicable` (provisional; el Template lo declara Required, sin asumir que todas las políticas de publicación del consumer estén definidas).

**Implementation Characteristics (proposed):** `Distributed` como **posible** trazabilidad de cambios mediante commits y PRs; no se acredita que constituyan una implementación equivalente a un changelog orientado a versiones.

### Detected Facts

- En el árbol del commit no se identificaron **rutas por nombre** de Changelog, Changes, History o Release. No equivale a una revisión exhaustiva de cualquier contenido documental.
- [README.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) describe la evolución del proyecto y remite al historial Git/PRs para atribución de cambios. No expone una lista de cambios publicados por versión en las secciones examinadas.
- [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) declara `0.0.1-SNAPSHOT`: esto no es por sí solo una prueba de publicaciones.
- El historial alcanzable desde el SHA registra cambios y PRs, incluidos #489, #491 y #493; historial granular de commits **no equivale** automáticamente a notas de release o changelog.
- La consulta al endpoint de GitHub Releases devolvió lista vacía **en el momento de la revisión**; no demuestra la inexistencia histórica de releases. La consulta de **tags no pudo completarse**, de modo que su ausencia **no está acreditada**.
- [F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) documenta hallazgos y planes, no una fuente de cambios publicados confirmada.

### Evidence

- [Revisión de Changelog y fuentes de publicación](only-film-changelog-evidence-review.md)
- [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [Historial Git hasta el SHA](https://github.com/fran-eliot/only_film/commits/28d75a50e0a178954dd46acc23300d9dd327843c/)
- [Página actual de Releases](https://github.com/fran-eliot/only_film/releases) — recurso **mutable**, no un snapshot del commit evaluado

### Evaluation Rationale — propuesta

No se ha encontrado en las fuentes inspeccionadas un registro de cambios **orientado a versiones publicadas** que desempeñe claramente `DOC-CHANGELOG`. No obstante, una conclusión de `Missing` requeriría descartar fuentes alternativas relevantes o documentar de manera explícita los límites de la investigación. Tampoco puede atribuirse `Partial` automáticamente a un historial Git/PRs que no se haya validado como fuente equivalente.

Por ello el trabajo semántico útil **es acotar dos hipótesis y definir qué evidencia permite decidir**, en vez de inventar un estado final. Una vez comprobadas las fuentes, el reviewer elegirá un valor admitido por el Assessment Template (`Satisfied`, `Partial` o `Missing`) y lo justificará.

### Uncertainty

- ¿Existen tags, notas de release u otra fuente oficial y accesible que resuma cambios por versión?
- ¿Hay un procedimiento de publicación real o el repositorio utiliza únicamente builds de desarrollo?
- ¿Qué información sobre cambios relevantes necesitan los destinatarios del repositorio?
- ¿La Responsibility exige un changelog incluso sin releases formales y qué política de secciones `Unreleased` sería razonable?
- ¿Puede justificarse `Missing` tras completar las comprobaciones C1–C6, o hay una implementación alternativa `Partial`/`Satisfied`?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** la evidencia no autoriza todavía decidir entre `ADD`, `ADAPT`, `ACCEPT`, `PRESERVE` u otra opción. No se genera un changelog ni se inventan versiones históricas.

## 5. Gates de revisión humana

| Gate | Criterio | Estado |
| --- | --- | --- |
| RQ-1 | Confirmar el contexto del consumidor y propósito de ambas Responsibilities Required | Pendiente |
| RQ-2 | Reproducir el Quick Start Compose o justificar con evidencia equivalente el umbral documental | Pendiente |
| RQ-3 | Corroborar versiones, variables y advertencias vigentes en el SHA | Evidencia estática preparada; pendiente de reviewer |
| RQ-4 | Verificar tags, releases y fuentes alternativas de historial de cambios según C1–C6 | Pendiente |
| RQ-5 | Seleccionar `State` válido para cada Responsibility, con `Applicability` y rationale | Pendiente |
| RQ-6 | Mantener `Needs Further Evaluation` si hay incertidumbres materiales | Preparado; pendiente de reviewer |
| RQ-7 | Resolver Adoption Decision solo con rationale y autorización humana | Pendiente |

## 6. Conclusión

Se han preparado propuestas semánticas para dos Responsibilities `Required` de Only Film con evidencia versionada y límites explícitos. `README-QUICK-START` mantiene una hipótesis `Partial` y `DOC-CHANGELOG` exige discriminar `Missing` frente a `Partial` antes de registrar un `State` formal.

**No se ha completado una evaluación E3 aprobada**, no hay Adoption Decision resuelta y el Assessment permanece `In Progress`. No se ejecuta Docker ni se modifica el repositorio consumidor.
