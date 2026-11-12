# Only Film — Negative Security Test Evidence Review

## 1. Contexto y método

Esta revisión E2 comprueba los **asertos versionados** en tests de seguridad de Only Film y los contrasta con los selectores del workflow ejecutado para el SHA fijado. La revisión es estática, **no** reproduce tests ni certifica la seguridad del producto.

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Related Responsibilities | `README-TESTING`, `DOC-TESTING`, `DOC-SECURITY` |
| Evidence | Código fuente y de tests, configuración del job y check-runs asociados al SHA |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |

Se distinguen tres afirmaciones diferentes: **(a)** el test existe y contiene asertos concretos, **(b)** su clase está incluida por el selector de un job de CI y **(c)** GitHub informa `success` del job. Sin Surefire/logs individualizados no se atribuye un resultado separado a cada test.

## 2. Autorización de reseñas: pruebas negativas y preservación de datos

El archivo [`ReviewControllerTest.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/controller/ReviewControllerTest.java) utiliza `@SpringBootTest`, `@AutoConfigureMockMvc` y `@Transactional`.

| Test | Condición y asertos observados en el código | Límite |
| --- | --- | --- |
| `saveReview_shouldRejectDirectPostByNonOwnerAndKeepOriginal` | POST `/reviews` con usuario diferente del propietario y CSRF válido; espera HTTP **403** y después compara título, rating y autor persistidos con valores originales | Prueba negativa definida, no ejecutada directamente en esta revisión |
| `saveReview_shouldAllowOwnerWithoutChangingMovieOrAuthor` | Propietario intenta alterar `movieId`, `user.id` y `creationDate`; se comprueba que esos campos no cambian, aunque sí se actualizan campos editables | Verifica el escenario implementado, no todos los tipos de manipulación posibles |
| `saveReview_shouldAllowAdminToEditWithoutChangingAuthor` | Administrador edita una reseña, se espera redirección y se verifica que permanece su autor original | Caso positivo de autorización; no implica una política completa de roles |
| `saveReview_shouldIgnoreInjectedIdentityAndMovieOnCreate` | POST de creación con `user.id` y `creationDate` inyectados; se verifica autor y película persistidos | Comprueba parámetros concretos del formulario |
| `saveReview_shouldRejectWithoutTicket` | Usuario sin entrada pagada intenta crear una reseña; verifica redirección y recuento de reseñas sin variación | Protege una regla de negocio en el escenario de prueba |
| `reviewDetail_shouldRejectExternalReturnUrls` | Proporciona URLs absolutas, `//host`, barras inversas y ruta relativa; espera que `returnUrl` sea `/reviews` | Inspecciona los casos definidos; no analiza todos los esquemas o codificaciones posibles |
| `saveReview_shouldRejectInvalidEditAndPreserveOriginal` | Edición con rating inválido; espera errores de validación y confirma que el registro persistido conserva título, descripción y rating | Test de validación e integridad sobre un caso concreto |

El [`ReviewController.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/ReviewController.java) del SHA evaluado llama a `verifyEditPermission` **antes de modificar los campos persistidos**; exige rol admin o coincidencia del ID de propietario y, de lo contrario, lanza `AccessDeniedException`. La relación entre código y asertos aporta una evidencia de diseño y regresión más específica que la auditoría histórica del 10/10/2026.

**No se infiere** que todos los endpoints de reseñas y sus variantes estén auditados, ni que se haya realizado un pentest.

## 3. CSRF, autorización de tickets y configuración

| Fuente | Test / cobertura observable | Evidencia |
| --- | --- | --- |
| `MutationCsrfSecurityTest` | `getNeverMutatesExistingResources` espera 405 en seis rutas de modificación con GET; `postWithoutCsrfIsForbiddenForAllStateMutations` espera 403 en esas seis rutas; `nonAdminCannotDeactivateSessionsEvenWithCsrf` espera 403 para usuario no administrador | [Código del test](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/controller/MutationCsrfSecurityTest.java) |
| `TicketSecurityRegressionTest` | Tests para acceso a ticket ajeno (403), checkout de ticket pagado (409) y creación de tickets por endpoint administrativo sin rol (403) | [Código del test](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/controller/TicketSecurityRegressionTest.java) |
| `EnvironmentHardeningTest` | Comprueba propiedades seguras del perfil base, restricciones de `dev` y `postgres`, generación de contraseñas demo diferentes y configuración externa explícita | [Código del test](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/config/EnvironmentHardeningTest.java) |

Estos asertos son evidencia precisa de **qué comportamiento espera el repositorio**; no sustituyen las comprobaciones de ejecución ni demuestran exhaustividad frente a rutas o escenarios no incluidos.

## 4. Validación de imágenes: pruebas definidas, fuera del selector H2 identificado

[`FileServiceTest.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/service/FileServiceTest.java) incluye, entre otros, los siguientes escenarios:

- Imágenes PNG/JPEG reales con nombres/extensiones y MIME falsos: la salida se guarda con formato normalizado, sin confiar en el nombre proporcionado.
- JPEG con contenido final añadido: comprueba que la salida recodificada no conserva el texto inyectado.
- Falso PNG cuyo contenido es HTML/script y BMP no admitido: espera `IllegalArgumentException`.
- Archivos superiores a 10 MiB e imágenes con dimensión 6001 píxeles: espera rechazo.
- Nulo/vacío y PNG con payload final añadido: comportamiento explícito de omisión o normalización.

El [`FileService.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/service/FileService.java) valida el contenido mediante `ImageIO`, limita el tamaño y normaliza el formato y nombre de salida.

**Selección del workflow:** aunque no se cita `FileServiceTest` por nombre, su nombre **coincide con el patrón `*ServiceTest`** incluido en el selector de `h2-regression`. Por tanto, la clase está comprendida en la selección configurada; los informes Surefire permitirían confirmar su ejecución individual y resultado.

## 5. Contraste con el job ejecutado

La definición de [`postgres-migration.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml) ejecuta `mvn test -Dtest=...` con los patrones `*RepositoryTest,*ServiceTest,*ControllerTest,*SecurityConfigTest` y nombres explícitos de regresiones, entre ellos `MutationCsrfSecurityTest`, `TicketSecurityRegressionTest` y `EnvironmentHardeningTest`.

| Test / clase | Selección nominal desde la configuración | ¿Ejecución individual confirmada? |
| --- | --- | --- |
| `ReviewControllerTest` | Sí, `*ControllerTest` | No: requiere reporte individual |
| `MutationCsrfSecurityTest` | Sí, clase explícita | No: requiere reporte individual |
| `TicketSecurityRegressionTest` | Sí, clase explícita | No: requiere reporte individual |
| `EnvironmentHardeningTest` | Sí, clase explícita | No: requiere reporte individual |
| `FileServiceTest` | **Sí, `*ServiceTest`** | No: requiere reporte individual |

**Ejecución verificada:** [GitHub Actions run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407), `head_sha=28d75a50e0a178954dd46acc23300d9dd327843c`, `completed/success`, con check `h2-regression: success` (además de `postgres-schema` y `PostgreSQL JPA and concurrent checkout`). Los selectores respaldan que estas clases están **incluidas en la selección configurada** del job; su ejecución efectiva o cualquier test omitido debe comprobarse en logs o reportes.

**Sonar/JaCoCo:** no se infieren porcentajes, Quality Gate aprobado ni ejecución de análisis Sonar a partir del estado del job. En el workflow, el scanner puede omitirse sin hacer fallar el job si no existe `SONAR_TOKEN`.

## 6. Evidencias aún necesarias para cerrar revisión E2/E3

| Gate | Verificación pendiente | Resultado requerido |
| --- | --- | --- |
| NT-1 | Abrir los reportes Surefire del run identificado si continúan disponibles | Confirmar nombres de tests ejecutados, éxitos/fallos y omisiones |
| NT-2 | Verificar los detalles de autorización y persistencia en pruebas de reseñas | Confirmar, al nivel de detalle necesario, los escenarios de lectura/escritura y los efectos en BD |
| NT-3 | Verificar CSRF y roles en rutas adicionales si el alcance del consumer lo exige | Evidencia de pruebas o justificación de limitación |
| NT-4 | Revisar informes JaCoCo reales, si existen, sin confundir H2 con cobertura global | Contadores y alcance explícitos, sin porcentajes estimados |
| NT-5 | Revisión semántica de `README-TESTING`, `DOC-TESTING` y `DOC-SECURITY` | `State`, `Applicability` y razones individuales revisadas por una persona |

No se ha corrido Maven ni accedido a una instancia ejecutada de Only Film en esta revisión.

## 7. Conclusión

Se verificaron **casos negativos de seguridad concretos en código fuente de tests** y su coincidencia con los patrones de selección del workflow H2 identificado. Esto mejora la evidencia de diseño y pruebas del Assessment sin equivaler a una certificación de ejecución individual, seguridad global o conformidad del Template.

`Assessment Status: In Progress`; `Decision Status: Needs Further Evaluation`; `Adoption Decision: —`. No se modifica el consumer ni se autoriza Application/Integration.
