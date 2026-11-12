# Only Film — Provisional Semantic Review of DOC-SECURITY

## 1. Contexto y límites

Propuesta de evaluación individual de la Responsibility `DOC-SECURITY` de `TPL-BACKEND` 0.1.0. Emplea la evidencia E2 recopilada anteriormente sobre un commit inmutable; **no constituye una aprobación humana, una auditoría de seguridad independiente ni una decisión de adopción**.

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Repository Template | `TPL-BACKEND` |
| Template Version | `0.1.0` |
| Requirement Level | `Optional` |
| Assessment Status | `In Progress` |
| Review Status | `Proposal — pending human review` |
| Reviewer / Approval | Sin asignar / no aprobado |
| Mutation | `NONE` |

Un nivel `Optional` **no equivale** a `Applicability: Not Applicable`. El propósito real de documentación de seguridad debe juzgarse en relación con la aplicación, sus usuarios y su entorno objetivo.

## 2. Assessment Summary — propuesta

| Responsibility | Requirement Level | Proposed State | Proposed Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `DOC-SECURITY` | `Optional` | `Partial` (**provisional**) | `Applicable` (**provisional**) | `Needs Further Evaluation` | `—` |

`Partial` es una **hipótesis semántica**, no una constatación de incumplimiento ni una certificación de estado. La suficiencia de las guías y auditorías debe ser revisada por una persona.

## 3. Responsibility Details — DOC-SECURITY

**Requirement Level:** `Optional`.

**Proposed State:** `Partial`, pendiente de revisión humana.

**Proposed Applicability:** `Applicable`, pendiente de revisión humana, porque el consumer administra autenticación, roles, datos de usuarios, compras simuladas, reseñas y archivos subidos.

**Implementation Characteristics (proposed):** `Own`, `Specialized`, `Distributed`. En vez de un documento canónico único, el consumer tiene auditorías, guías de credenciales, documentación de perfiles y notas de CI repartidas en `docs/` y README.

### Detected Facts

1. La [auditoría de consolidación técnica](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SECURITY_HARDENING_AUDIT.md) está fechada **2026-10-10** y declara una base histórica (`main` tras PR #12, `0a7e03a0`). Identifica riesgos de autorización, mutaciones HTTP, uploads, configuración y documentación **para esa referencia histórica**. No es un pentest ni puede tomarse como diagnóstico actualizado del SHA evaluado.
2. El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) tiene una sección `Seguridad y límites actuales`: declara BCrypt, roles, CSRF, validación de imágenes y límites del checkout demo y del despliegue local. Son afirmaciones documentales que se contrastaron de forma acotada con el código.
3. [`ReviewController.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/ReviewController.java) comprueba rol admin o propietario antes de guardar ediciones, mediante `verifyEditPermission`. [`ReviewControllerTest.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/controller/ReviewControllerTest.java) contiene un test negativo de POST ajeno con expectativa HTTP 403 y verificación de que los datos persistidos no cambian.
4. [`MutationCsrfSecurityTest.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/controller/MutationCsrfSecurityTest.java) define comprobaciones explícitas para impedir mutaciones por GET, rechazar POST sin CSRF y bloquear la desactivación de sesiones por usuario no administrador.
5. [`FileService.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/service/FileService.java) valida bytes de imagen con ImageIO y aplica límites; [`FileServiceTest.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/service/FileServiceTest.java) contiene pruebas de nombres/MIME falsos, payloads añadidos, formatos no admitidos y tamaños inválidos.
6. [`application.properties`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/resources/application.properties) deshabilita consola H2 y show-sql por defecto. [`SecurityConfig.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/config/SecurityConfig.java) limita la excepción CSRF de consola al perfil local apropiado; [`EnvironmentHardeningTest.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/config/EnvironmentHardeningTest.java) comprueba propiedades de perfiles y configuración de contraseñas demo.
7. [`DEMO_CREDENTIALS_SECURITY.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEMO_CREDENTIALS_SECURITY.md) advierte de riesgos y configuración explícita del secreto demo. [`DataInitializer.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/config/DataInitializer.java) genera una contraseña aleatoria si no se configuró otra externamente.
8. En [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407), correspondiente al SHA fijado, el log de `h2-regression` registra **329 tests, 0 fallos, 0 errores y 0 omitidos**. Entre ellos: `ReviewControllerTest` (20), `FileServiceTest` (9), `MutationCsrfSecurityTest` (3), `TicketSecurityRegressionTest` (3) y `EnvironmentHardeningTest` (5), todos sin fallos.
9. El mismo log de CI registra un análisis Sonar enviado con `ANALYSIS SUCCESSFUL`, pero **no demuestra aprobación del Quality Gate**. No se verificó un pentest, escáner completo de dependencias, cobertura global ni una revisión exhaustiva de todas las rutas.

### Evidence

- [Auditoría histórica de seguridad](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SECURITY_HARDENING_AUDIT.md)
- [README — Seguridad y límites](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Guía de credenciales demo](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEMO_CREDENTIALS_SECURITY.md)
- [Reconciliación histórica frente al código fijado](only-film-security-testing-reconciliation.md)
- [Revisión de tests negativos](only-film-negative-security-test-evidence.md)
- [Resultados Surefire y Sonar comprobados en logs](only-film-verified-surefire-sonar-logs.md)
- [Run de GitHub Actions y job H2](https://github.com/fran-eliot/only_film/actions/runs/39283862407/job/118164215980)

### Evaluation Rationale — propuesta, no aprobación

Existe documentación específica sobre controles y riesgos de seguridad, respaldada por ejemplos concretos de código y pruebas que **se ejecutaron con éxito** en el commit evaluado. Por tanto, la responsabilidad no debe clasificarse como `Missing` solo por no existir un único archivo `SECURITY.md`.

La propuesta conservadora `Partial` refleja que la documentación actual mezcla fuentes históricas y vigentes, sin una revisión acreditada de suficiencia para el modelo de amenazas y la audiencia objetivo. La falta de un pentest **no implica automáticamente** que la documentación de seguridad sea parcial: el reviewer debe valorar la responsabilidad *documental* y no confundirla con la seguridad absoluta del sistema.

### Uncertainty

- ¿La documentación distingue suficientemente riesgos históricos, controles vigentes y advertencias de operación para el commit evaluado?
- ¿Hay instrucciones claras para secretos, exposición pública, reporting de vulnerabilidades y tratamiento de datos, según el contexto real del consumidor?
- ¿Es suficiente la documentación distribuida o necesita una guía consolidada y mantenible?
- ¿Qué hallazgos antiguos están cerrados mediante evidencias concretas, sin asumir el estado de sus issues?
- ¿Es necesario consultar Quality Gate, dependencias y otras pruebas para la evaluación **documental** específica, o solo para una auditoría técnica más amplia?
- ¿Qué modelo de amenazas y entorno de despliegue se consideran dentro del alcance?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** existen medidas, fuentes y resultados parciales verificables, pero todavía no hay revisión humana de la suficiencia documental ni del alcance aplicable. `PRESERVE`, `ADAPT`, `ADD`, `ACCEPT` u `OMIT` requerirían justificación específica; no se infieren de los tests verdes.

## 4. Gates para revisión humana

| Gate | Criterio | Estado |
| --- | --- | --- |
| SEC-1 | Confirmar contexto del consumer, audiencia, exposición y aplicabilidad de DOC-SECURITY | Pendiente |
| SEC-2 | Valorar si README + guías distribuidas cubren los temas de seguridad que necesita el consumidor | Pendiente |
| SEC-3 | Separar explícitamente hallazgos históricos y comprobaciones del SHA evaluado | Evidencia preparada; pendiente de reviewer |
| SEC-4 | Comprobar que los resultados de tests corresponden a los controles citados y que sus límites constan | Evidencia preparada; pendiente de reviewer |
| SEC-5 | Decidir si se precisan instrucciones de divulgación de vulnerabilidades, secretos o un documento consolidado | Pendiente |
| SEC-6 | Registrar `State`, `Applicability`, `Evaluation Rationale` y `Uncertainty` aprobados en el Assessment | Pendiente |
| SEC-7 | Resolver o mantener pendiente `Adoption Decision` con rationale humano | Pendiente |

Un reviewer puede confirmar `Partial` o proponer `Satisfied` o `Missing` tras evaluar la calidad documental. La aprobación de `DOC-SECURITY` no equivaldría a certificar que el software es seguro.

## 5. Resultado y siguientes pasos

- **E2:** evidencias documentales, controles y ejecución de pruebas relevantes verificadas, sin extrapolar seguridad global.
- **E3:** propuesta de interpretación semántica estructurada; **no aprobada**.
- **E4:** no se ha seleccionado ni justificado una Adoption Decision final.
- **Consumer:** no modificado; sin tests o scanners nuevos.
- **Assessment:** `In Progress`.

**Conclusión:** `DOC-SECURITY` dispone de una base probatoria específica para revisión humana, pero su clasificación definitiva y cualquier cambio de documentación permanecen abiertos.
