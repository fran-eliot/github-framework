# 59 — Existing Repository Adoption End-to-End Feasibility Check

| Campo | Valor |
|---|---|
| Proyecto | GitHub Framework |
| Fecha | 2026-11-11 |
| Fase | Discovery — bounded workflow check |
| Consumer | [fran-eliot/seniormeet](https://github.com/fran-eliot/seniormeet) |
| Consumer reference | `b84b0de246d459caf594a5cdacbe8fccfa68698a` |
| Template | `TPL-BACKEND v0.1.0` |
| Responsibility | `README-QUICK-START` (`Required`) |
| Assessment status | `In Progress`; solo una Responsibility explorada |
| Application | Not Started — blocked by unresolved Decision and unverified runtime facts |
| Integration | Not Started — no verified candidate |
| Consumer mutation | **NONE** |

> Este trabajo recorre la lógica de las puertas de decisión entre Assessment, Application e Integration, pero no simula una Application completada ni una integración inexistente. No es un Assessment completo ni prueba de ejecución del consumer.

---

## 1. Pregunta experimental

¿Puede una adopción acotada detectar qué falta para avanzar desde evidencia objetiva hacia una Application revisable, y detenerse con seguridad antes de mutar un repositorio sin decisiones suficientes?

El objetivo es comprobar los **hand-offs y safe-stops** del Framework, no cumplir todas las Responsibilities de `TPL-BACKEND` ni corregir SeniorMeet.

Se utilizan:

- [TPL-BACKEND](../../framework/templates/repositories/backend/README.md) y [metadata](../../framework/templates/repositories/backend/metadata.yml).
- [Assessment Guide](../../framework/adoption/README.md) y [Assessment Template](../../framework/adoption/assessment-template.md).
- [Application Guide](../../framework/adoption/application/README.md) y [Application Record](../../framework/adoption/application/application-template.md).
- [Integration Guide](../../framework/adoption/integration/README.md) y [Integration Record](../../framework/adoption/integration/integration-template.md).
- [Assisted Analysis Guide](../../framework/adoption/assisted-analysis/README.md) y [Evidence Snapshot Template](../../framework/adoption/assisted-analysis/evidence-snapshot-template.md).

## 2. Consumer baseline y alcance

Se fija el estado de SeniorMeet en el commit:

```text
b84b0de246d459caf594a5cdacbe8fccfa68698a
```

No se utiliza el estado mutable de `master` para inferir cómo se encuentra hoy el proyecto.

El Template seleccionado es `TPL-BACKEND v0.1.0`, estado `Experimental`, madurez mínima recomendada `L2`. Su composición identifica `README-QUICK-START` entre los 8 Required Components.

En su README, la responsabilidad corresponde a permitir una primera ejecución documentada. Evaluamos únicamente esta responsabilidad; la idoneidad completa de `TPL-BACKEND` para SeniorMeet y el grado real de madurez del consumer no se determinan aquí.

## 3. Assessment — Detected Facts y Evidence

| ID | Hecho verificado | Evidence |
|---|---|---|
| A-01 | `README.md` tiene el nombre `SENIOR MEET` y la descripción `Red Social para personas mayores`; no contiene pasos de instalación o ejecución. | [README del consumer](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/README.md) |
| A-02 | `pom.xml` define un proyecto Maven/Spring Boot 3.2.2 con `java.version=21`. | [pom.xml](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/pom.xml) |
| A-03 | `Dockerfile` utiliza `maven:3.8.3-openjdk-17` y contiene comentarios con ejemplos de `docker build` / `docker run`. | [Dockerfile](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/Dockerfile) |
| A-04 | El mismo Dockerfile hace referencia a `target/backend-0.0.1-SNAPSHOT.jar`, mientras la metadata Maven declara `artifactId=seniormeet` y `version=0.0.1`. | [Dockerfile](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/Dockerfile) y [pom.xml](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/pom.xml) |
| A-05 | `docker-compose.yml` declara servicios `mysql` y `spring-app`, pero el README no referencia ese archivo ni explica cómo utilizarlo. | [docker-compose.yml](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/docker-compose.yml) y [README](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/README.md) |

Estos hechos son observaciones estáticas. Ni el build de Maven ni Docker fueron ejecutados. Las diferencias de Java y del nombre del artefacto son **riesgos a verificar**, no pruebas de que todos los caminos de ejecución fallen.

## 4. Assessment — Evaluación limitada

| Campo | Valor |
|---|---|
| Responsibility | `README-QUICK-START` |
| Requirement Level | `Required` |
| State | `Partial` — provisional |
| Applicability | `Applicable` |
| Implementation Characteristics | `Distributed`, `Own` (características descriptivas) |
| Uncertainty | Comandos efectivos, prerequisites, compatibilidad de JDK y artifact de build, resultado reproducible |
| Decision Status | `Needs Further Evaluation` |
| Adoption Decision | `—` |

**Evaluation Rationale.** El README no ofrece una vía de inicio rápido. Existen indicios de ejecución en artefactos técnicos y comentarios, lo que constituye cobertura documental fragmentaria, pero no un Quick Start completo ni verificado. `Partial` se utiliza de manera **provisional** bajo el principio Responsibility over File; una revisión humana podría confirmar `Missing` si esos indicios no aportan cobertura utilizable.

La existencia de un `Dockerfile` no garantiza que los comandos funcionen, y la ausencia de instrucciones en README no autoriza por sí sola una decisión automática `ADD` o `ADAPT`.

**Uncertainty pendiente:** identificar el método de ejecución soportado y verificarlo en entorno aislado antes de proponer instrucciones al consumer.

### Decisión de Assessment

El estado es `In Progress` para este ensayo acotado. La decisión permanece `Needs Further Evaluation` y no se crea un registro de Assessment completo de las 28 Responsibilities, ni una aprobación humana ficticia.

## 5. Assisted Analysis — Alcance efectivo

Para esta comprobación se han recopilado datos **read-only** con referencias a los archivos y commit del consumer.

La Evidence se presenta en una tabla de hechos y fuentes, pero **no se afirma haber ejecutado una herramienta automática de Assisted Analysis ni haber completado un Evidence Snapshot formal**.

Limitación detectada: pasar desde hechos observables a instrucciones de ejecución exige verificación técnica y evaluación semántica. El Framework permite preservar ambas como pendientes sin traducirlas a conclusiones automáticas.

## 6. Application — Gate de entrada

El Application Core requiere una **Adoption Decision resuelta** para la Responsibility seleccionada y recomienda refrescar Evidence antes de planificar operaciones.

En este caso:

```text
README-QUICK-START
    State: Partial (provisional)
    Decision Status: Needs Further Evaluation
    Adoption Decision: —
              ↓
        Application gate
              ↓
       STOP / DEFER
```

No procede seleccionar `CREATE` ni `MODIFY` aún.

Un eventual Application Intent podría plantearse, **solo como hipótesis para revisión futura**, en términos de documentar un procedimiento de arranque reproducible compatible con el estado técnico real y preservando el README existente. No constituye un Change Set aprobado.

### Evidencia necesaria antes de retomar Application

1. Determinar el flujo de ejecución recomendado por quien mantiene SeniorMeet.
2. Verificar prerequisitos Java, base de datos y herramientas.
3. Validar si el build produce el artefacto referenciado por Docker.
4. Confirmar las instrucciones en una ejecución aislada, sin usar credenciales ni datos reales.
5. Completar la Evaluation Rationale y resolver humanamente la Adoption Decision.
6. Refrescar Evidence respecto al estado del consumer sobre el que se plantearía actuar.

No se creó rama en SeniorMeet y no existe Application Result, verified candidate ni patch de adopción.

## 7. Integration — Gate de entrada

El Integration Core necesita un `VERIFIED` candidate, Application Outcome, Candidate Reference y evidencias suficientes de verificación.

Aquí:

```text
Application not started
    ↓
No candidate branch / commit
    ↓
No Application verification
    ↓
Integration: NOT STARTED
```

No procede consultar mergeability ni emitir una declaración de `INTEGRATED`, `VERIFIED STABLE STATE` o `RELEASE READY`.

Este **safe-stop** es un resultado válido del ensayo: la arquitectura impide dar por completada una integración sin su entrada verificable.

## 8. Fricciones y hallazgos

| ID | Observación | Implicación |
|---|---|---|
| E2E-F01 | El modelo permite conservar hechos, interpretación provisional y decisión no resuelta de forma separada. | Fortaleza de trazabilidad |
| E2E-F02 | Las instrucciones de ejecución no pueden inferirse de forma segura de comentarios Docker, metadata Maven o compose sin validación. | Necesidad de revisión técnica previa |
| E2E-F03 | Una evaluación parcial no habilita Application. | Gate respetado; no autorizar mutaciones |
| E2E-F04 | Sin candidate verificado no existe Integration válida. | Gate respetado |
| E2E-F05 | Sigue sin existir evidencia empírica sobre tiempo o dificultad de uso para desarrolladores externos. | No justificar tooling únicamente por esta prueba |
| E2E-F06 | La progresión práctica desde un Assessment incompleto puede terminar legítimamente en `STOP / DEFER`. | Resultado de investigación, no fallo de la capability |

## 9. Resultado y próxima comprobación

**Resultado obtenido:** se ejecutó un análisis read-only acotado sobre un consumer real, se registró una evaluación provisional para una Responsibility Required y se aplicaron conceptualmente los gates de Application e Integration, que **detienen el recorrido correctamente por falta de precondiciones**.

**No se completó** un Adoption end-to-end con cambios reales, candidate y verificación estable. Tampoco se demuestra que todo usuario pueda completar ese recorrido de forma autónoma.

El siguiente experimento útil requerirá un caso con Decision `Resolved` revisada y una Application suficientemente pequeña y segura para poder comprobar **plan → isolated change → verify → integration review**. Antes deberá acordarse expresamente la frontera de mutación del consumer y la disponibilidad de pruebas.

No se abre Sprint, milestone, versión ni Delivery Scope. No se altera SeniorMeet.

## 10. Conclusión

La investigación encuentra valor operativo en los safe-stops y la trazabilidad del modelo de Adoption, pero no aporta todavía evidencia de eficiencia end-to-end.

La cuestión prioritaria ya no es redactar una nueva Guide genérica sino **conseguir un caso de Application verdaderamente verificable**, sin convertir una decisión provisional en automatización ni forzar una modificación de repositorio.
