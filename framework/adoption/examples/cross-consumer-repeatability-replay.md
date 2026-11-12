# Existing Repository Adoption — Cross-Consumer Repeatability Replay

## 1. Propósito y alcance

Este replay compara el uso del **Assessment Core** para una misma Responsibility en dos repositorios backend diferentes. Su objetivo es comprobar que la secuencia de representación y revisión es repetible aunque las evidencias del consumer sean distintas.

El replay **no reevalúa los consumidores**, no reabre sus decisiones ni afirma que la Responsibility esté satisfecha. Es una verificación documental basada en los dos ejemplos registrados; los Estados `Partial` siguen siendo provisionales y sujetos a revisión humana.

| Campo | Consumer A | Consumer B |
| --- | --- | --- |
| Repositorio | [fran-eliot/seniormeet](https://github.com/fran-eliot/seniormeet) | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Commit fijado | `b84b0de246d459caf594a5cdacbe8fccfa68698a` | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` | `TPL-BACKEND` |
| Template Version | `0.1.0` | `0.1.0` |
| Responsibility comparada | `README-QUICK-START` | `README-QUICK-START` |
| Requirement Level | `Required` | `Required` |
| Assessment Status | `In Progress` | `In Progress` |

El contrato de `TPL-BACKEND` procede de su [metadata canónica](../../templates/repositories/backend/metadata.yml). Ambos ejemplos se basan en referencias inmutables, no en ramas que puedan avanzar.

**Fuentes internas del replay:**

- [SeniorMeet — First Assessment Example](first-assessment-example.md).
- [Only Film — Two Backend Responsibilities](only-film-two-responsibilities.md).
- [Assessment Template](../assessment-template.md) y [Adoption Guide](../README.md).

## 2. Secuencia de replay

Para cada consumer se comprueba la existencia documental de la secuencia:

```text
Pin Template and Consumer Reference
    ↓
Select the same Responsibility
    ↓
Record Detected Facts
    ↓
Attach source-traceable Evidence
    ↓
Record provisional State / Applicability
    ↓
Describe Uncertainty and Evaluation Rationale
    ↓
Leave Decision unresolved when not justified
    ↓
Keep Assessment In Progress
```

Esta secuencia permite comparar el método, no igualar artificialmente los resultados.

## 3. Detected Facts y Evidence: diferencias observadas

| Dimensión | SeniorMeet (consumer A) | Only Film (consumer B) |
| --- | --- | --- |
| README Quick Start | El ejemplo registra ausencia de instrucciones de instalación/arranque en el README inspeccionado | El ejemplo registra una sección «Inicio rápido» con Docker Compose y alternativas Maven |
| Artefactos asociados | `Dockerfile`, `docker-compose.yml`, `pom.xml` | `Dockerfile`, `compose.yaml`, `.env.example`, `pom.xml`, guía PostgreSQL |
| Contexto técnico explícito | `pom.xml`: Spring Boot `3.2.2`, Java `21`; Dockerfile descrito con JDK `17` | `pom.xml`: Spring Boot `4.0.5`, Java `25` |
| Principal incertidumbre | Procedimiento de arranque recomendado, discrepancia de JDK y referencias de artefactos | Reproducibilidad real del arranque documentado y suficiencia de configuración |
| Evidencia funcional ejecutada en estos ejemplos | Ninguna | Ninguna |

**Fuentes específicas (commits fijados):**

- SeniorMeet: [README](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/README.md), [pom.xml](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/pom.xml), [Dockerfile](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/Dockerfile) y [docker-compose.yml](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/docker-compose.yml).
- Only Film: [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml), [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) y [POSTGRESQL_SETUP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md).

El hecho de que un README incluya instrucciones y otro no las incluya **no determina por sí solo** la satisfacción de `README-QUICK-START`. Los artefactos de otros archivos pueden tener relevancia; su eficacia necesita evaluación.

## 4. Comparación de evaluación provisional

| Campo | SeniorMeet | Only Film |
| --- | --- | --- |
| State | `Partial` — provisional; el reviewer podría concluir `Missing` | `Partial` — provisional, sujeto a verificación |
| Applicability | `Applicable` | `Applicable` |
| Implementation Characteristics | `Own`, `Distributed` | `Own`, documentación distribuida |
| Decision Status | `Needs Further Evaluation` | `Needs Further Evaluation` |
| Adoption Decision | `—` | `—` |
| Decision Rationale | Falta confirmar el arranque y las instrucciones antes de elegir `ADD` o `ADAPT` | Falta reproducir el Quick Start antes de elegir `PRESERVE` o `ADAPT` |

La coincidencia en `Partial` **no implica equivalencia funcional**. Tampoco equivale a una regla automática que asigne ese Estado al detectar una ruta o una sección del README.

## 5. Criterios de repetibilidad y resultados

| ID | Criterio de verificación documental | Resultado |
| --- | --- | --- |
| RR-01 | Se aplica el mismo Template y versión, con Requirement Level idéntico | **PASS** — ambos usan `TPL-BACKEND 0.1.0`, `Required` |
| RR-02 | Cada consumer dispone de referencia Git inmutable | **PASS** — SHA completo documentado en ambos ejemplos |
| RR-03 | Cada consumer registra Detected Facts diferenciados de Evidence | **PASS** — ambas secciones están documentadas |
| RR-04 | Las fuentes de Evidence pueden trazarse hasta el commit del consumer | **PASS** — enlaces fijados al SHA en ambos casos |
| RR-05 | Se conservan diferencias entre los hechos de los consumers sin imponer el mismo resultado técnico | **PASS** — hechos y dudas específicas en la sección 3 |
| RR-06 | Se documentan State, Applicability y Evaluation Rationale con carácter provisional | **PASS** — en ambos ejemplos |
| RR-07 | Uncertainties y Decision Status no se transforman en una Adoption Decision sin revisión | **PASS** — `Needs Further Evaluation`, decisión `—` |
| RR-08 | El Assessment parcial no se declara completo ni habilita Application/Integration | **PASS** — ambos continúan `In Progress` |
| RR-09 | El procedimiento de arranque se ha reproducido y verificado operacionalmente | **NOT VERIFIED** — no se ejecutaron builds, contenedores ni tests |
| RR-10 | Se han cubierto todas las Responsibilities del Template | **NOT VERIFIED** — uno y dos ejemplos parciales respectivamente |

**Resultado:** se cumplen los criterios **documentales RR-01 a RR-08** en los ejemplos revisados. RR-09 y RR-10 permanecen expresamente **NOT VERIFIED**. Este resultado no constituye un certificado de conformidad de ningún consumer ni una verificación completa del Adoption Assessment.

## 6. Repeatability vs. Semantic Evaluation

La repetibilidad demostrada es de **representación y trazabilidad del proceso de evaluación**: misma estructura, diferentes Evidence y preguntas abiertas.

No se ha demostrado:

- que las instrucciones de arranque funcionen;
- que el Estado `Partial` sea el resultado definitivo en ambos casos;
- que una herramienta pueda inferir automáticamente Applicability, State o Adoption Decision;
- que el consumer satisfaga todas las Responsibilities del Template;
- que se cumplan los criterios para marcar el Assessment `Complete`.

Las discrepancias entre documentación, runtime y dependencias deben tratarse como cuestiones de verificación, no como fallos afirmados sin ejecución.

## 7. Próximos pasos para alcanzar una verificación más completa

1. Reproducir en un entorno aislado el procedimiento de inicio de cada consumer, registrando herramientas, versiones y resultados.
2. Solicitar revisión humana sobre la suficiencia de Evidence y confirmar o corregir el State provisional de `README-QUICK-START`.
3. Aplicar el Assessment Template a **todas** las Responsibilities correspondientes al `TPL-BACKEND`, sin inventar resultados para las todavía no inspeccionadas.
4. Mantener `Needs Further Evaluation` y `Adoption Decision: —` cuando no exista suficiente evidencia.
5. Revisar por separado las condiciones de Application e Integration; este replay **no autoriza** ninguna de esas fases.

## 8. Límites

Este replay compara **documentos de ejemplo existentes**. No se ejecutan pruebas, no se modifica el estado de los consumers y no se añaden automáticamente decisiones al Assessment.

El estado de ambos assessments sigue siendo `In Progress`.
