# Only Film — Verified Surefire and Sonar Log Evidence

## 1. Alcance y procedencia

Esta comprobación E2 utiliza **logs reales de GitHub Actions**, no únicamente selectores de Maven, código fuente de tests o estados agregados de jobs. Se mantiene el Assessment de `TPL-BACKEND` 0.1.0 en `In Progress`, sin modificar el repositorio consumidor.

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer commit | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Related Responsibilities | `README-TESTING`, `DOC-TESTING`, `DOC-SECURITY` |
| GitHub Actions run | [39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) |
| Job | [h2-regression — 118164215980](https://github.com/fran-eliot/only_film/actions/runs/39283862407/job/118164215980) |
| Fecha del run | 2026-10-19 |
| Fuente de resultados | Log textual completo del job |
| Assessment Status | `In Progress` |
| Consumer Mutation | `NONE` |

Los resultados que siguen corresponden al **subconjunto seleccionado para ese job H2 del SHA indicado**. No deben presentarse como el resultado de toda la batería de tests, especialmente Selenium y verificaciones manuales.

## 2. Resultados Maven Surefire verificados en el log

En el paso `Run existing H2 regression tests`, Maven registra:

```text
Tests run: 329, Failures: 0, Errors: 0, Skipped: 0
BUILD SUCCESS
```

Se localizaron además líneas individuales `Tests run` para estas clases relevantes:

| Clase | Tests | Failures | Errors | Skipped |
| --- | ---: | ---: | ---: | ---: |
| `com.demo.controller.ReviewControllerTest` | 20 | 0 | 0 | 0 |
| `com.demo.controller.MutationCsrfSecurityTest` | 3 | 0 | 0 | 0 |
| `com.demo.controller.TicketSecurityRegressionTest` | 3 | 0 | 0 | 0 |
| `com.demo.config.EnvironmentHardeningTest` | 5 | 0 | 0 | 0 |
| `com.demo.service.FileServiceTest` | 9 | 0 | 0 | 0 |
| **Subtotal de estas cinco clases** | **40** | **0** | **0** | **0** |

El subtotal de 40 pruebas no debe confundirse con las **329 del job**. También constan otras clases (por ejemplo, `TicketServiceTest` y `TicketControllerTest`) incluidas en el total.

**Interpretación verificable:** estas cinco clases **se ejecutaron** dentro del job y el log informa que sus respectivas pruebas terminaron sin fallos, errores ni omisiones. Esto amplía la evidencia previa, que se limitaba a la existencia de asertos y a la selección configurada del workflow. No equivale a una garantía de ausencia de vulnerabilidades.

## 3. JaCoCo: generación y publicación histórica, artefacto no disponible ahora

El mismo log registra `jacoco:0.8.13:prepare-agent` y `jacoco:0.8.13:report`, incluida la lectura del archivo `target/jacoco.exec`.

El paso de subida informa:

```text
Artifact jacoco-h2-regression.zip successfully finalized.
Artifact jacoco-h2-regression has been successfully uploaded!
```

- Nombre: `jacoco-h2-regression`.
- Artifact ID registrado: `12201642997`.
- La consulta actual de artefactos del run devolvió **cero artefactos**.
- La configuración de [postgres-migration.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml) fija `retention-days: 14`.

**Conclusión limitada:** existe evidencia textual de generación y subida del informe en aquella ejecución, pero **no se ha inspeccionado el XML/HTML de JaCoCo**. La falta de artefactos en la consulta actual es compatible con la retención configurada, pero no se asigna una causa definitiva sin otra verificación. **No se atribuye ningún porcentaje de cobertura.**

## 4. SonarCloud: análisis enviado, Quality Gate no verificado

En el paso `Analizar PR y rama main con SonarQube Cloud`, el log muestra que se ejecutó el scanner, incluidas las fases de importación de JaCoCo, y registra:

```text
ANALYSIS SUCCESSFUL, you can find the results at:
https://sonarcloud.io/dashboard?id=fran-eliot_only_film&branch=main
BUILD SUCCESS
```

A diferencia de la advertencia genérica de que el job puede omitir el scanner sin `SONAR_TOKEN`, **para este run concreto sí hay evidencia de ejecución y finalización del análisis**.

Esto **no acredita** por sí mismo un `Quality Gate: Passed`, ausencia de incidencias o estado actual de SonarCloud. Se necesitaría comprobar el resultado del Quality Gate asociado a ese análisis, distinguiéndolo del dashboard actual.

## 5. Progresión de evidencia

| Pregunta | Antes de consultar logs | Tras la comprobación |
| --- | --- | --- |
| ¿El job H2 terminó satisfactoriamente? | Sí, check `success` | Sí, y Maven reporta 329/0/0/0 |
| ¿Corrieron las cinco clases clave? | Selección nominal verificada | Sí, resultados por clase registrados en el log |
| ¿Se generó un informe JaCoCo? | Configuración y paso `success` | Log confirma generación y subida |
| ¿Se ha inspeccionado el contenido de JaCoCo? | No | **No**, artefacto no disponible en consulta actual |
| ¿Se ejecutó SonarCloud? | No acreditado a nivel de logs | **Sí**, `ANALYSIS SUCCESSFUL` en ese run |
| ¿Se aprobó el Quality Gate? | Sin verificar | **Sin verificar** |
| ¿Pasó Selenium en ese SHA? | No acreditado | **No acreditado** |
| ¿Se reprodujo Docker Compose Quick Start? | No | **No** |
| `State` / `Applicability` definitivos | Pendientes | **Pendientes de revisión semántica** |
| `Adoption Decision` | `—` | `—` |

**Trazabilidad posterior del procesamiento Sonar:** la [revisión semántica preliminar de Testing](only-film-testing-semantic-review.md) documenta el CE Task ID `AaFU8vS6n_jCCWP5LQvY` extraído del log y deja explícita la imposibilidad de consultar la tarea histórica y su Quality Gate con el acceso disponible.

## 6. Siguientes pasos

1. Para `README-TESTING` y `DOC-TESTING`, incorporar estos datos en la evaluación humana de suficiencia y alcance, incluyendo las diferencias entre regresión H2, PostgreSQL, Selenium y Compose.
2. Si se necesita porcentaje de cobertura, regenerar un informe JaCoCo sobre el SHA evaluado en un entorno autorizado o localizar una copia verificable del artefacto histórico; nunca calcularlo con recuentos Surefire.
3. Consultar el Quality Gate correspondiente al análisis de SonarCloud de 2026-10-19 si existe evidencia histórica trazable. No confundir el dashboard mutable de `main` con ese resultado histórico.
4. Para `DOC-SECURITY`, mantener la evidencia de pruebas negativas y su ejecución acotada; no extrapolar a un pentest, cobertura exhaustiva de endpoints ni estado global de vulnerabilidades.
5. Registrar por Responsibility `State`, `Applicability` y `Evaluation Rationale` solo cuando se realice la revisión semántica; resolver una Adoption Decision únicamente con justificación y autorización pertinentes.

**Resultado:** mejor calidad E2 para Testing y controles de seguridad examinados. El Assessment permanece `In Progress`; no se han ejecutado pruebas nuevas ni modificado Only Film.
