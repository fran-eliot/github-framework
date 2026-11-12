# Only Film — Pinned Quick Start and CI Evidence Verification

## 1. Alcance y criterio

Primera comprobación **E2 — calidad de evidencias** posterior a la exploración de las 28 Responsibilities de `TPL-BACKEND` 0.1.0. Se centra en `README-QUICK-START`, `README-TESTING` y fuentes relacionadas con `DOC-TESTING` y `DOC-DEPLOYMENT`.

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Método | Inspección read-only de archivos y resultados identificados de GitHub Actions |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |
| Fecha de registro | 2026-11-12 |

**Diferencia esencial:** un archivo que define una prueba es **configuración**, una ejecución GitHub Actions identificada y finalizada es **evidencia de ejecución**, y una verificación completa del Quick Start desde clon limpio exigiría reproducir dicho procedimiento. No se confunden estos niveles.

## 2. Consistencia estática del Quick Start

Se inspeccionaron directamente el README y las siguientes fuentes **en el mismo SHA**, no solo su existencia en el árbol:

| Elemento | Observación verificada en los archivos | Fuente |
| --- | --- | --- |
| Procedimiento README | Copia de `.env.example`, asignación privada de contraseña, `docker compose up --build -d`, `docker compose ps`, URL local `/movies` | [README.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) |
| Compilación del contenedor | Dockerfile multi-stage Maven 3.9 + Temurin 25; runtime Temurin 25 JRE; `mvn -DskipTests package`; ejecución de `onlyfilm.jar` | [Dockerfile](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/Dockerfile) |
| Versión Java de proyecto | `java.version=25`, parent Spring Boot `4.0.5` | [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) |
| Servicios | Compose declara `app` y `postgres` con `postgres:17-alpine`, healthcheck y dependencia `service_healthy` | [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) |
| Configuración PostgreSQL | Compose activa `SPRING_PROFILES_ACTIVE=postgres`; define `DB_URL`, `DB_USERNAME`, `DB_PASSWORD` en el servicio de aplicación | [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) |
| Perfil Spring | `application-postgres.properties` consume las tres variables, activa Flyway y fija Hibernate `ddl-auto=validate` | [application-postgres.properties](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/resources/application-postgres.properties) |
| Almacenamiento | `postgres_data` y `uploads_data` definidos en Compose; puertos de aplicación y DB vinculados a `127.0.0.1` | [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) |
| Configuración local | `.env.example` incluye `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_PORT`, `APP_PORT` | [.env.example](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.env.example) |

**Resultado estático:** la combinación documentada resulta **coherente en esos parámetros concretos**. No se detecta en estos archivos un conflicto de versiones Java, perfil Spring o variables de conexión. **Esto no equivale a haber compilado, arrancado o validado la aplicación.**

**Limitaciones y precauciones:**

- `.env.example` contiene un valor demostrativo de contraseña que el README exige reemplazar; debe utilizarse una credencial privada antes de arrancar.
- El comando del README fija `localhost:8080` como valor por defecto; si se redefine `APP_PORT`, debe utilizarse el puerto configurado.
- `Dockerfile` emplea `-DskipTests` al crear el artefacto. Una imagen construida no acredita por sí sola que se haya ejecutado toda la batería de pruebas.
- No se ha ejecutado `docker compose config`, build ni arranque en esta inspección. Tampoco se ha inspeccionado una respuesta HTTP emitida por una instancia levantada aquí.

## 3. Ejecución real localizada en el SHA fijado

La consulta de ejecuciones de GitHub Actions asociadas al **head SHA exacto** identificó:

| Campo | Evidencia |
| --- | --- |
| Workflow | `PostgreSQL schema and regression validation` |
| Run ID | `39283862407` |
| Event | `push` |
| Head SHA | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Created at (UTC) | `2026-10-19T16:14:15Z` |
| Run status | `completed` |
| Run conclusion | `success` |
| Enlace | [GitHub Actions — run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) |

Los **tres jobs** retornados para esa ejecución fueron:

| Job | Job ID | Status | Conclusion | Alcance declarado en el workflow |
| --- | --- | --- | --- | --- |
| `h2-regression` | `118164215980` | `completed` | `success` | Selección de tests H2 de repositorios, servicios, controladores y regresiones; intenta publicar artefactos JaCoCo |
| `postgres-schema` | `118164215920` | `completed` | `success` | Paquetizado, arranque del JAR contra PostgreSQL de CI, migraciones Flyway, persistencia y reinicio |
| `PostgreSQL JPA and concurrent checkout` | `118164215844` | `completed` | `success` | `PostgresPersistenceIntegrationTest` con PostgreSQL 17 |

**Fuente de alcance:** [postgres-migration.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml).

Los resultados de ejecución son **datos del proveedor GitHub Actions**; no se han leído ni reproducido los logs completos ni los artefactos Surefire/JaCoCo. El estado `success` confirma que los jobs finalizaron satisfactoriamente según sus checks en esa ejecución, pero **no revela por sí solo los recuentos, la cobertura o una aprobación de SonarCloud**. En particular, el paso Sonar puede omitir el análisis si falta `SONAR_TOKEN` y finalizar sin fallo del job.

## 4. Alcance real de los otros workflows

La inspección de archivos del **mismo commit** permite diferenciar qué trabajos están configurados para ejecutarse:

| Workflow | Trigger documentado | Qué no se puede inferir del run anterior |
| --- | --- | --- |
| [postgres-migration.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml) | `push` a ramas seleccionadas, `pull_request` a `main`, `workflow_dispatch` | El run identificado sí corresponde a este workflow, pero no acredita cobertura global |
| [ticket-regression.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/ticket-regression.yml) | `pull_request` a `main`, `push` a rama específica y manual | No se atribuye ejecución de este workflow al run PostgreSQL |
| [compose-smoke.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/compose-smoke.yml) | `pull_request` a `main`, `push` a ramas específicas y manual | No se ha verificado en el run identificado el **smoke de Docker Compose** de extremo a extremo |
| [tests.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/tests.yml) | `workflow_dispatch`; en PR a `main` solo al cambiar `tests.yml` | La mayoría de jobs solo corren manualmente; Selenium se ejecuta en PR que modifican ese workflow |
| [sonar.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/sonar.yml) | `workflow_dispatch` | No hay evidencia de ejecución del workflow Sonar manual asociada al run PostgreSQL |

El workflow `compose-smoke.yml` **sí contiene** instrucciones para `docker compose config`, build/arranque, comprobación HTTP `/movies`, migraciones y persistencia tras restart/recreate. **Que el workflow esté definido no demuestra que se haya ejecutado exitosamente para el SHA fijado.**

## 5. Qué cambia en el Assessment y qué no

| Aspecto | Antes de esta revisión | Ahora |
| --- | --- | --- |
| Quick Start — coherencia documental | README y rutas de archivos examinados | Variables, perfiles, Dockerfile, Compose, POM y Spring properties contrastados directamente |
| Testing — existencia de CI | Workflows identificados por nombre | Triggers y selectores inspeccionados; una ejecución real `success` del SHA y tres jobs identificados |
| Ejecución Compose desde clon limpio | No demostrada | **Sigue sin demostrarse** |
| Selenium y suites manuales del SHA | No demostradas | **Siguen sin demostrarse** |
| Porcentaje de cobertura actual | No comprobado | **Sigue sin comprobarse** |
| Semantic `State` / `Applicability` | Interpretaciones provisionales y pendientes | **No resueltos** |
| `Decision Status` | `Needs Further Evaluation` | **Sin cambios** |
| `Adoption Decision` | `—` | **Sin cambios** |
| `Assessment Status` | `In Progress` | **Sin cambios** |

La nueva evidencia refuerza la revisión de `README-QUICK-START` y `README-TESTING`, pero no obliga a reclasificar el provisional `Partial` ni autoriza una Adoption Decision sin revisión semántica.

## 6. Próxima revisión verificable

1. Examinar los logs y artefactos de [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) cuando estén disponibles, distinguiendo tests efectivamente ejecutados, información de cobertura y análisis Sonar opcional.
2. Identificar una ejecución **del mismo SHA** del workflow Compose smoke, o reproducir el Quick Start en clon limpio y entorno desechable, registrando salida de `docker compose config`, construcción, arranque, `/movies`, migraciones y limpieza segura.
3. Confirmar en revisión humana si las instrucciones y pruebas satisfacen la Responsibility esperada para el consumer; documentar `State`, `Applicability`, `Evaluation Rationale` y decisión justificada o incertidumbre persistente.
4. No extrapolar estos resultados al `main` actual de Only Film sin refrescar la referencia y las verificaciones.

**Límites:** no se modificó el repositorio consumidor, no se ejecutaron sus comandos desde este Assessment, no se generó candidato de Application ni se marcó `Assessment Complete`.
