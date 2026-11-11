# 60 — Adoption End-to-End Evidence Reconciliation

| Campo | Valor |
|---|---|
| Proyecto | GitHub Framework |
| Fecha | 2026-11-11 |
| Estado | Discovery — historical evidence reconciliation |
| Framework version | v0.10.0 (published baseline) |
| Consumer histórico | [fran-eliot/dental-back-spring](https://github.com/fran-eliot/dental-back-spring) |
| Nuevo consumer examinado en #59 | [fran-eliot/seniormeet](https://github.com/fran-eliot/seniormeet) |
| Scope | Reconcile prior real Application/Integration evidence against current end-to-end research |
| Delivery / Sprint / Release | None committed |

> Este documento revisa evidencias históricas y los estados actuales de las PR originales. No constituye una nueva ejecución, un Assessment completo, una prueba con usuarios externos ni una autorización para alterar ningún consumer.

---

## 1. Pregunta y motivo

El [Discovery #59](59_ADOPTION_END_TO_END_FEASIBILITY_CHECK.md) examinó la responsabilidad `README-QUICK-START` de SeniorMeet. Las evidencias permitieron registrar una evaluación provisional, pero no una Adoption Decision resuelta ni un candidate verificado. El recorrido se detuvo antes de Application e Integration.

Antes de abrir otro experimento con mutación, hay que responder:

> ¿Disponemos ya en el historial del Framework de evidencia de Application e Integration ejecutadas realmente sobre un consumer?

**Respuesta:** sí, existen dos casos con cambios y PRs reales. La necesidad pendiente no es demostrar desde cero que las operaciones `MODIFY` y `CREATE` se pueden integrar, sino investigar el **valor y la autonomía del flujo completo** bajo condiciones nuevas.

## 2. Fuentes

Fuentes internas históricas:

- [32_APPLICATION_DISCOVERY.md](32_APPLICATION_DISCOVERY.md) — Cases A y B, cambios físicos, preservación y verificaciones.
- [38_INTEGRATION_DISCOVERY.md](38_INTEGRATION_DISCOVERY.md) — integración real, drift y verificación en stable state.
- [40_INTEGRATION_REPEATABILITY_EXPERIMENT.md](40_INTEGRATION_REPEATABILITY_EXPERIMENT.md) — replay de ambos casos y estabilidad de representación.
- [59_ADOPTION_END_TO_END_FEASIBILITY_CHECK.md](59_ADOPTION_END_TO_END_FEASIBILITY_CHECK.md) — safe-stop actual en SeniorMeet.

Fuentes verificadas de GitHub:

- [dental-back-spring PR #1](https://github.com/fran-eliot/dental-back-spring/pull/1).
- [dental-back-spring PR #2](https://github.com/fran-eliot/dental-back-spring/pull/2).

Se comprobaron el estado `merged` y los archivos cambiados de ambas PR con el conector de GitHub el 11 de noviembre de 2026. **No** se reejecutaron tests, build o verificación funcional independiente en este análisis.

## 3. Caso A — README-QUICK-START

| Dimensión | Evidencia |
|---|---|
| Consumer | `fran-eliot/dental-back-spring` |
| Responsibility | `README-QUICK-START` |
| Decision histórica | `ADAPT` |
| Application operation | `MODIFY` |
| Artifact modificado | `README.md` |
| Candidate commit documentado | `6706d6dd6d9c4952fe7f8192eb07922b2ac82f4f` |
| PR | [#1](https://github.com/fran-eliot/dental-back-spring/pull/1) |
| Merge commit | `c61829ff27f1e6cb6fffc4210e224bd275c00139` |
| GitHub PR state | `MERGED` |
| Integration verification | `PASS` en el Discovery histórico #38 |

### Evidencia operacional

Según #32, el cambio sustituyó referencias obsoletas al puerto 3000 por puerto 8080 y eliminó una instrucción no aplicable `cd backend`. La verificación comparó el README con la propiedad `server.port=8080` del consumer.

Según #38, la PR se integró después de revisar el estado de la base, y la comprobación posterior a la fusión registró `Physical`, `Intent`, `Preservation` y `Stable-State Verification` como `PASS`.

La consulta actual a GitHub confirma que la PR #1 está fusionada y que modificó solo `README.md`. Los resultados históricos de verificación se atribuyen a #32/#38; no se presentan como mediciones nuevas.

## 4. Caso B — DOC-CHANGELOG

| Dimensión | Evidencia |
|---|---|
| Consumer | `fran-eliot/dental-back-spring` |
| Responsibility | `DOC-CHANGELOG` |
| Decision histórica | `ADD` |
| Application operation | `CREATE` |
| Artifact creado | `CHANGELOG.md` |
| Commits candidatos documentados | `f00fac8770fa70d455f51cf31dd10d6951732a81`, `c209c82965f4510fef8a60df5210ce75c7689439` |
| PR | [#2](https://github.com/fran-eliot/dental-back-spring/pull/2) |
| Merge commit | `ddd09369b98d11da25525ae09bfdb840c3f4ce50` |
| GitHub PR state | `MERGED` |
| Integration verification | `PASS` en el Discovery histórico #38 |

### Evidencia operacional

El caso B documenta un ciclo `REFINE → PASS` para conservar convenciones de idioma y no inventar versiones históricas. Se creó un Changelog sin modificar otros archivos, según #32.

El experimento #38 registró que `main` había avanzado desde la base original de la PR, con cambios en README. La integración revisó ese drift y lo consideró compatible con la incorporación de `CHANGELOG.md`, en lugar de tratar cualquier drift como motivo automático para descartar el candidate.

La consulta actual confirma que la PR #2 está fusionada y que su archivo modificado fue `CHANGELOG.md`.

## 5. Qué demuestra el conjunto

| Pregunta | Evidencia | Conclusión |
|---|---|---|
| ¿Es posible planificar cambios acotados sobre una Responsibility? | #32: casos A/B | Sí, en los experimentos documentados |
| ¿Puede aplicarse `MODIFY` preservando otros artefactos? | #32 y PR #1 | Sí, en el caso observado |
| ¿Puede aplicarse `CREATE` con revisión de convenciones? | #32 y PR #2 | Sí, en el caso observado |
| ¿Puede revisarse drift antes de Integration? | #38, caso B | Sí, en la evidencia histórica |
| ¿Se produjo una Integration real? | PR #1 y PR #2, ambas `MERGED` | Confirmado por GitHub |
| ¿Se verificó stable state después? | #38, verificaciones históricas | Documentado; no reejecutado aquí |
| ¿El mismo registro admite ambas operaciones? | #40, replays A/B | Documentado como estable |
| ¿Puede frenarse una Application sin Decision? | #59, SeniorMeet | Sí, como análisis de precondiciones |
| ¿Una persona externa puede utilizar el flujo autónomamente? | Sin observación independiente | No demostrado |
| ¿Cuál es el coste de completar el proceso? | Sin medición comparable | No demostrado |

## 6. Distinción entre tipos de evidencia

```text
Historical real consumer changes
    PR #1 / PR #2 merged
        ≠
New execution of the Framework
        ≠
Independent usability or efficiency validation
```

Los cambios reales muestran viabilidad operacional en dos operaciones concretas. El examen de SeniorMeet #59, por su parte, muestra que un caso incompleto se puede detener sin forzar una mutación.

No resulta correcto afirmar que **ningún** flujo end-to-end ha sido ejecutado: sí hay integración histórica. Tampoco es correcto afirmar que la experiencia completa está validada para nuevos usuarios o para cualquier consumer.

## 7. Decisión para la siguiente iteración

**No repetir por defecto** una mutación sobre SeniorMeet solo para volver a demostrar `ADAPT / MODIFY` o `ADD / CREATE`.

En su lugar, centrar la investigación en una incertidumbre todavía no resuelta:

> ¿Puede un desarrollador que no conoce el Framework convertir un Assessment revisado en una Application acotada, verificarla e integrarla siguiendo los registros existentes, con un esfuerzo razonable?

Esta pregunta conecta con el [protocolo UX-02](54_FIRST_TIME_USABILITY_VALIDATION_PROTOCOL.md), pero implica un estudio distinto, más largo y con control explícito de mutaciones.

### Condiciones mínimas de ese estudio

1. Consumer y referencia fijados, con permiso de escritura solo si realmente se necesita.
2. Assessment y Adoption Decision revisados humanamente.
3. Application Plan y Preservation Scope aprobados antes de cualquier cambio.
4. Branch aislada, tests o verificaciones acordes a los artifacts afectados.
5. Integration respetando governance, sin merge automático o decisiones semánticas inferidas.
6. Medición observada de ayudas, pasos bloqueados, artefactos necesarios y retrabajo.
7. Posibilidad de terminar en `NO CHANGE`, `DEFER` o `REPLAN` sin considerar el experimento fallido.

**No se crea aquí ese estudio ni se compromete una nueva mutación**. Si no hay participantes disponibles, pueden investigarse otras capacidades reales, sin equiparar replays internos a validación independiente.

## 8. Cierre

La evidencia de Application e Integration sobre `dental-back-spring` ya está documentada y confirma dos PRs reales fusionadas. #59 complementa este historial al mostrar una puerta de entrada que legítimamente detiene el recorrido.

El gap de conocimiento prioritario pasa de **«¿se pueden realizar e integrar cambios acotados?»** a **«¿se puede usar el proceso de forma autónoma y con coste proporcionado?»**.

**Estado:** reconciliación completada; no hay nueva implementación, cambio de consumer, Delivery Scope, Sprint, milestone ni release comprometido.
