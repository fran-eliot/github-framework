# Only Film — Security and Testing Evidence Reconciliation

## 1. Contexto y alcance

Esta comprobación E2 contrasta hechos técnicos de `DOC-SECURITY`, `README-TESTING` y `DOC-TESTING` del Assessment `TPL-BACKEND` 0.1.0 con el código y los checks vinculados a un **commit inmutable** del consumidor.

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Evidence | Código fuente, configuración, documentos versionados y checks de GitHub Actions |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |

Una auditoría anterior describe el sistema en **su referencia original**; sus hallazgos no se pueden trasladar sin contraste al SHA actual de esta evaluación. Este ejercicio **no es** un pentest, un SAST nuevo, un análisis exhaustivo de CVE ni una ejecución de tests realizada en el contexto del Assessment.

## 2. Reconciliación de hallazgos de seguridad históricos

La [auditoría de consolidación técnica](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SECURITY_HARDENING_AUDIT.md), fechada **2026-10-10**, declara como base `main` tras PR #12 (`0a7e03a0`). La [evaluación de madurez](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md) también se refiere a un commit histórico distinto (`9f2a31e927df105d14e3d30d4d8277fa61883deb`). No son evaluaciones del SHA de este documento.

| Hallazgo histórico | Hechos observables directamente en el SHA fijado | Interpretación limitada / revisión pendiente |
| --- | --- | --- |
| #13 — escritura de reseñas sin comprobar autor o rol | `ReviewController.saveReview` usa `ReviewFormDTO` y delega la modificación en `saveExistingReview`, que llama a `verifyEditPermission` **antes** de modificar campos; comprueba admin o igualdad de ID de propietario y lanza `AccessDeniedException` | El patrón observado mitiga el hallazgo descrito en la auditoría antigua. Falta confirmar pruebas negativas y comportamiento HTTP integrado para concluir su resolución |
| #14 — mutaciones mediante GET y ausencia de CSRF | `ReviewController` emplea `@PostMapping` para eliminar reseñas; `SecurityConfig` delimita una excepción CSRF para H2-console al entorno `dev` local y declara reglas por rutas/roles | Se observan mejoras concretas, **no** se ha auditado exhaustivamente todo el mapa de rutas y acciones de todos los controladores |
| #15 — subida de archivos confiando en extensiones del cliente | `FileService.store` lee bytes con límite; `verifyAndNormalize` utiliza `ImageIO` y admite solo JPEG/PNG, con nombre de destino UUID y creación exclusiva | No se observa el mecanismo vulnerable basado en la extensión original en ese flujo. La inspección estática no sustituye pruebas de contenidos maliciosos, recursos ni rutas de exposición |
| #16 — consola H2, logs SQL y contraseña estática por defecto | `application.properties` declara `spring.h2.console.enabled=false` y `spring.jpa.show-sql=false`; `SecurityConfig` limita la excepción de H2-console al entorno local `dev` | Los valores versionados son más restrictivos que los descritos históricamente. Falta comprobar despliegues y variables efectivas |
| Credenciales de demo previsibles | `DataInitializer.demoPassword` genera UUID cuando no existe propiedad configurada; la clase se restringe con `@Profile("!test & (!postgres | demo)")` | El comportamiento descrito por el código y por `DEMO_CREDENTIALS_SECURITY.md` reduce exposición por credenciales literales, pero no demuestra una política de operación segura en todos los entornos |

**Evidence de código y configuración:**

- [ReviewController.java](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/ReviewController.java)
- [SecurityConfig.java](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/config/SecurityConfig.java)
- [FileService.java](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/service/FileService.java)
- [DataInitializer.java](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/config/DataInitializer.java)
- [application.properties](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/resources/application.properties)
- [DEMO_CREDENTIALS_SECURITY.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEMO_CREDENTIALS_SECURITY.md)

**Precaución:** la reconciliación no significa que todos los tickets históricos estén cerrados ni que el SHA sea inmune a nuevas vulnerabilidades. Solo delimita que algunas descripciones antiguas no representan fielmente los patrones observados ahora.

## 3. Testing: fuentes, selectores y ejecución

### 3.1 Fuentes comprobadas

El árbol Git del commit contiene:

- `src/test/java/com/demo/controller/ReviewControllerTest.java`
- `src/test/java/com/demo/controller/MutationCsrfSecurityTest.java`
- `src/test/java/com/demo/controller/TicketSecurityRegressionTest.java`
- `src/test/java/com/demo/config/EnvironmentHardeningTest.java`
- `src/test/java/com/demo/service/FileServiceTest.java`
- `src/test/java/com/demo/ui/ReviewSeleniumTest.java`

**Estas rutas confirman la existencia de archivos; no se ha auditado aquí todo su contenido ni declarado que cada caso de seguridad específico esté cubierto.**

Se inspeccionaron además la [guía de CI/SonarCloud](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SONARCLOUD_PR_CI.md) y la [línea base JaCoCo](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/JACOCO_COVERAGE_BASELINE.md). Ambas dejan claro que la cobertura del subconjunto H2 **no representa la cobertura global** y que la disponibilidad de secretos influye en la ejecución del scanner.

### 3.2 Ejecución verificada del commit

La consulta de GitHub Actions para `28d75a50e0a178954dd46acc23300d9dd327843c` devuelve [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407), ejecutada el **2026-10-19** con estado `completed` y resultado `success`.

| Check del commit | Resultado registrado | Alcance declarado por workflow |
| --- | --- | --- |
| `h2-regression` | `success` | Selección de pruebas H2, que incluye clases de regresión de controladores, configuración y seguridad |
| `postgres-schema` | `success` | JAR contra PostgreSQL, Flyway, persistencia y reinicio |
| `PostgreSQL JPA and concurrent checkout` | `success` | Test de integración PostgreSQL de persistencia y concurrencia |

[Workflow postgres-migration.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml).

**Límites de interpretación:**

- Un job `success` acredita su resultado final según GitHub, pero no expone por sí solo la lista de tests ejecutados ni sus recuentos. Los selectores documentan la intención del job.
- `h2-regression` intenta publicar JaCoCo/Surefire, pero no se descargaron ni auditaron aquí los informes; **no hay porcentaje verificable**.
- El paso Sonar en este workflow puede finalizar correctamente tras **omitir** el scanner si no está disponible `SONAR_TOKEN`. Un job verde no demuestra `ANALYSIS SUCCESSFUL` ni Quality Gate aprobado.
- No existe en esta evidencia un run de Selenium, un pentest, una ejecución Compose smoke del mismo SHA ni un escaneo de vulnerabilidades acreditado.

Véanse las revisiones de [Quick Start y CI](only-film-pinned-quickstart-ci-verification.md) y del [límite del smoke Compose](only-film-compose-evidence-gap.md) para el alcance operativo.

## 4. Preguntas y verificaciones prioritarias

| ID | Revisión pendiente | Criterio de salida |
| --- | --- | --- |
| ST-1 | Contrastar las rutas de modificación de reseñas con tests negativos de autorización | Identificar pruebas concretas en `ReviewControllerTest`/otras suites y sus resultados para el mismo SHA |
| ST-2 | Verificar alcance global de mutaciones HTTP/CSRF y reglas de roles | Matriz de métodos, rutas y controles de autorización con evidencia de tests, sin asumir cobertura universal |
| ST-3 | Contrastar validación real de imágenes y rutas de uploads | Tests sobre formatos admitidos, límites de tamaño y contenido inválido identificados por nombre y resultado |
| ST-4 | Confirmar diferencias entre perfiles de Spring y demo | Evidencias que distingan `dev`, `postgres` y `demo`, configuración efectiva y secretos locales |
| ST-5 | Consultar logs/artifacts de la ejecución H2 | Tests y recuentos efectivamente observados; JaCoCo solo con informe real, sin extrapolar globalmente |
| ST-6 | Verificar ejecución Sonar/Selenium separadamente | Run/logs o reportes inequívocos del SHA; no deducirlos de `h2-regression: success` |

Estas comprobaciones pueden generar más Evidence pero **no autorizan por sí solas** una Adoption Decision.

**Verificación adicional de pruebas negativas:** el [análisis de asertos y selectores del workflow](only-film-negative-security-test-evidence.md) examina directamente `ReviewControllerTest`, `MutationCsrfSecurityTest`, `TicketSecurityRegressionTest`, `EnvironmentHardeningTest` y `FileServiceTest`, sin confundir su selección en CI con resultados individuales auditados.

**Seguimiento con logs reales:** la [verificación de Surefire y Sonar](only-film-verified-surefire-sonar-logs.md) acredita 329 pruebas H2 satisfactorias y resultados concretos de cinco clases de seguridad, además de `ANALYSIS SUCCESSFUL` del scanner. Estos datos actualizan las incertidumbres anteriores sobre ejecución individual y Sonar para **ese run**; no prueban Quality Gate, cobertura global ni Selenium.

## 5. Impacto en el Assessment

| Aspecto | Resultado |
| --- | --- |
| Fuentes históricas identificadas y separadas del SHA actual | Sí |
| Contraste directo de cinco familias de hallazgos con archivos versionados | Sí, estático y limitado |
| Tres check-runs exitosos verificados para el SHA | Sí |
| Estado actual de todas las vulnerabilidades | **No determinado** |
| Testing completo, Selenium, Sonar y cobertura global | **No acreditados** |
| `State` / `Applicability` definitivos | Pendientes |
| `Decision Status` | `Needs Further Evaluation` |
| `Adoption Decision` | `—` |
| Assessment | `In Progress` |

**Conclusión:** esta reconciliación mejora la calidad de la evidencia y evita reutilizar diagnósticos históricos como si fueran hallazgos vigentes. No modifica Only Film, no ejecuta pruebas ni cierra formalmente la evaluación semántica.
