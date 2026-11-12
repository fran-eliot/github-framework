# Only Film — Compose Smoke Evidence Gap and Reproduction Criteria

## 1. Assessment Context

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer commit | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Target Responsibility | `README-QUICK-START` (`Required`) |
| Related Responsibilities | `README-TESTING`, `DOC-TESTING`, `DOC-DEPLOYMENT` |
| Method | Read-only review of commit check-runs, workflow definitions and earlier Evidence |
| Assessment status | `In Progress` |
| Consumer mutation | `NONE` |

Esta revisión se apoya en la [verificación de configuración y CI](only-film-pinned-quickstart-ci-verification.md). Su objetivo es distinguir **ejecución efectivamente acreditada** de **workflow definido pero no acreditado en el SHA objetivo**.

## 2. Evidencia concreta comprobada

La consulta de GitHub Actions para el commit fijado devuelve **una ejecución** identificada:

| Propiedad | Valor |
| --- | --- |
| Workflow | `PostgreSQL schema and regression validation` |
| Run ID | `39283862407` |
| Evento | `push` |
| Inicio UTC | `2026-10-19T16:14:15Z` |
| Estado y resultado | `completed`, `success` |
| Fuente | [Run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) |

Los **tres check-runs directamente asociados a ese commit** son:

| Check | Job ID | Resultado |
| --- | --- | --- |
| `h2-regression` | `118164215980` | `success` |
| `postgres-schema` | `118164215920` | `success` |
| `PostgreSQL JPA and concurrent checkout` | `118164215844` | `success` |

[Archivo de definición del workflow que produjo los checks](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml).

**Conclusión limitada:** GitHub confirma esos tres jobs satisfactorios. **No aparece un check `compose-smoke` entre los checks asociados directamente al commit.** Esta constatación no prueba que Compose no se haya ejecutado en otros commits, en un merge SHA de PR, en otra ejecución manual o fuera de GitHub Actions; tampoco acredita que los logs detallados o artefactos sigan conservados.

## 3. Por qué los checks existentes no sustituyen el smoke de Compose

En `postgres-migration.yml`, el job `postgres-schema` construye un artefacto Java con Maven, lanza `java -jar` con el perfil `postgres`, realiza comprobaciones HTTP y SQL sobre el servicio PostgreSQL de CI, y verifica persistencia tras reinicio. Es una evidencia valiosa de arranque **del JAR sobre PostgreSQL**.

En cambio, [`compose-smoke.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/compose-smoke.yml) describe otra ruta de ejecución:

1. `docker compose config --quiet`;
2. `docker compose up --build --wait -d`;
3. comprobación HTTP de `/movies`;
4. comprobación de historial Flyway;
5. comprobación de persistencia de datos y uploads tras reinicio/recreación.

La definición de ese segundo workflow se inspeccionó, **pero no hay una ejecución positiva del mismo asociada directamente al SHA dentro de los checks consultados**. No es válido sustituirla por el resultado `postgres-schema`, pues no construye ni pone en marcha la aplicación mediante el Compose documentado en el Quick Start.

La [guía de arranque](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [Dockerfile](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/Dockerfile) y [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) ya se contrastaron estáticamente en la revisión anterior.

## 4. Criterio de aceptación para reproducir el Quick Start

La evidencia necesaria para resolver esta **laguna de ejecución** debe corresponder al código del SHA fijado o a una fuente cuyo contenido se pueda verificar como equivalente. Si se reproduce manualmente, hacerlo solo en un **entorno aislado y desechable**, con credenciales sintéticas y sin datos reales.

| Gate | Evidencia que debe conservarse | Estado en esta revisión |
| --- | --- | --- |
| Q1 — Reference | Commit exacto, entorno y versiones de Docker/Compose | Pendiente |
| Q2 — Configuration | Resultado de `docker compose config --quiet` después de preparar `.env` privado | Pendiente |
| Q3 — Build/start | Resultado de `docker compose up --build --wait -d` y estado de servicios | Pendiente |
| Q4 — Web | Respuesta HTTP esperada de `/movies` y comprobación básica de navegación | Pendiente |
| Q5 — Schema | Evidencia de Flyway y esquema bajo PostgreSQL del Compose | Pendiente |
| Q6 — Persistence | Resultado de reinicio/recreación y conservación de datos/archivos según el alcance del smoke | Pendiente |
| Q7 — Cleanup | Limpieza controlada, especificando explícitamente si se preservaron o eliminaron volúmenes desechables | Pendiente |
| Q8 — Traceability | Run ID o registro de ejecución con salida, timestamp y commit; observaciones de fallos si los hay | Pendiente |

**Nota de seguridad:** `docker compose down -v` destruye volúmenes. Utilizarlo solo tras confirmar que el entorno y sus datos son desechables; no debe proponerse como limpieza genérica para una instalación existente.

En una ejecución de GitHub Actions sobre otro SHA, el reviewer debe comprobar qué commit y qué artefactos se ensayaron. Un resultado exitoso de un commit distinto **no se puede atribuir automáticamente** al commit fijado.

## 5. Impacto en el Assessment

| Campo / cuestión | Situación |
| --- | --- |
| `README-QUICK-START` — presencia de instrucciones | Observada documentalmente |
| Coherencia estática de variables, Java, perfiles y Compose | Contrastada en los parámetros examinados |
| Arranque del JAR con PostgreSQL en CI del mismo SHA | Evidencia de job `postgres-schema: success` |
| Quick Start de Compose reproducido en el SHA | **No demostrado** |
| `State` y `Applicability` finales | Pendientes de evaluación semántica |
| `Decision Status` | `Needs Further Evaluation` |
| `Adoption Decision` | `—` |
| Assessment global | `In Progress` |

**Resultado:** la laguna queda delimitada y cuenta con criterios de aceptación observables, pero **no se declara cerrada**. No se ha lanzado ningún workflow, ejecutado Docker ni modificado el repositorio consumidor. Una eventual ejecución satisfactoria solo aportaría nueva Evidence; la interpretación y la decisión siguen requiriendo revisión.
