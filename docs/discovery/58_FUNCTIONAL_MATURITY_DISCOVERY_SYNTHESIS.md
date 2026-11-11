# 58 — Functional Maturity Discovery Synthesis

| Campo | Valor |
|---|---|
| Proyecto | GitHub Framework |
| Fecha | 2026-11-11 |
| Estado | Discovery Synthesis — Concluded for current evidence |
| Versión publicada | `v0.10.0` |
| Alcance | Functional maturity / Template materialization / `README-LICENSE` |
| Fuentes principales | [55 — Functional Maturity](55_FRAMEWORK_FUNCTIONAL_MATURITY_DISCOVERY.md), [56 — Materialization Reality Check](56_DOCUMENTATION_TEMPLATE_MATERIALIZATION_REALITY_CHECK.md), [57 — Documentation Consumer Case](57_DOCUMENTATION_LICENSE_CONSUMER_CASE_STUDY.md) |
| Solution Shaping | No iniciado |
| Delivery Scope | No definido |
| Sprint / milestone / versión objetivo | Ninguno comprometido |

> Esta síntesis cierra el ciclo de investigación acotado a la evidencia actual. Cerrar Discovery no convierte los hallazgos en requisitos de implementación ni implica que todos los aspectos de madurez funcional estén resueltos.

---

## 1. Objetivo

Consolidar lo aprendido sobre la diferencia entre:

- contratos y responsabilidades definidos por GitHub Framework;
- Components canónicos realmente disponibles;
- capacidad de un consumer para satisfacer responsabilidades con soluciones propias;
- automatización ejecutable frente a procesos manuales revisables.

La pregunta de decisión es:

> ¿Existe evidencia suficiente para promover la materialización de `README-LICENSE`, modificar `TPL-DOCUMENTATION` o extender las herramientas del Framework como siguiente incremento?

## 2. Evidencia sintetizada

### 2.1 Madurez funcional (Discovery #55)

- **Repository Templates:** la biblioteca dispone de composiciones versionadas `TPL-BACKEND`, `TPL-FULLSTACK` y `TPL-DOCUMENTATION`. Son contratos declarativos, no generadores automáticos.
- **Framework Validator:** su entry point en Python descubre y valida `metadata.yml` dentro de `framework/components/` del propio Framework; no ejecuta por sí solo un Assessment semántico de consumidores externos.
- **Existing Repository Adoption:** Assessment, Application e Integration proporcionan Guides y registros Markdown para operaciones humanas y revisables; Assisted Analysis ofrece soporte de Evidence read-only y source-traceable mediante Guide y Snapshot Template. No hay motor de adopción automatizada entregado por estos artefactos.

Los documentos de verificación de releases anteriores respaldan los límites y deliverables de esas capabilities. Esta síntesis no reproduce su ejecución ni afirma haber reejecutado tests.

### 2.2 Contrato de TPL-DOCUMENTATION (Discovery #56)

Según la definición canónica de `TPL-DOCUMENTATION v0.1.0`, estado `Experimental` y madurez `L2`:

| Requirement Level | Declarados | Implementados según README canónico |
|---|---:|---:|
| Required | 9 | 8 |
| Recommended | 7 | 2 |
| Optional | 5 | 1 |
| **Total** | **21** | **11** |

`README-LICENSE` es el único Component `Required` clasificado como `Conceptual`.

La ausencia de su materialización canónica significa que **no se puede materializar exclusivamente con Components implementados el contrato mínimo completo**. No significa que todo consumer documental incumpla su responsabilidad de comunicar licencias.

La biblioteca y el Component Catalog distinguen:

```text
Component availability
    ≠
Consumer responsibility coverage
    ≠
Consumer Adoption Decision
```

### 2.3 Consumer documental externo (Discovery #57)

El caso `github/docs`, fijado en el commit `2b4f2c7398e04ee8d02adca7440e4286d20c78b9`, muestra:

- sección `License` en el README;
- comunicación diferenciada de CC BY 4.0 para documentación/contenidos y MIT para código;
- enlaces a `LICENSE` y `LICENSE-CODE`, que incluyen sus textos correspondientes.

Para la Responsibility `README-LICENSE`, definida como comunicación de la licencia aplicable desde el README, se registró una cobertura **provisional `Satisfied`**, con Applicability `Applicable`, implementación `Own / Specialized / Distributed` y `Decision Status: Needs Further Evaluation`.

La evaluación es **parcial y documental**. No se realizó el Assessment completo de `TPL-DOCUMENTATION`, no hubo revisión formal del consumer, no se comprobó cumplimiento legal de licencias ni se seleccionó una Adoption Decision.

## 3. Hallazgos finales

| ID | Conclusión | Nivel de apoyo | Implicación |
|---|---|---|---|
| FM-S01 | Hay una diferencia real entre contrato declarativo y disponibilidad material de Components. | Confirmada en los artefactos canónicos | Conservar la distinción al comunicar la madurez |
| FM-S02 | `TPL-DOCUMENTATION` tiene un gap de materialización canónica en `README-LICENSE`. | Confirmada | No presentarlo como totalmente materializable solo desde el catálogo |
| FM-S03 | Un consumer documental puede comunicar licencias sin un Component canónico del Framework. | Respaldada por un caso externo | No deducir State `Missing` de `Conceptual` |
| FM-S04 | El gap provoca un obstáculo significativo de adopción para usuarios reales. | No demostrado | Requiere observación específica |
| FM-S05 | Materializar `README-LICENSE` es la siguiente inversión de mayor valor. | No demostrado | No abrir Delivery Scope por inercia |
| FM-S06 | Rebajar `README-LICENSE` de Required sería correcto. | No demostrado | Conservar el contrato hasta disponer de evidencia contraria |
| FM-S07 | Hay que extender el Framework Validator o crear un generador para resolver el caso. | No demostrado | No ampliar tooling sin una necesidad repetible y acotada |

## 4. Decisión de Discovery

**Decisión propuesta:** concluir la investigación actual y **no promover** el gap de `README-LICENSE` a Solution Shaping ni al Product Backlog con la evidencia disponible.

Se preservan:

```text
TPL-DOCUMENTATION v0.1.0
    README-LICENSE
        Requirement Level: Required
        Framework Component Availability: Conceptual
```

No se crean nuevos Components, no se cambia metadata, no se modifica el Validator y no se alteran los consumers examinados.

Esta decisión es **reversible**. Concluir este experimento no significa prohibir la futura implementación del Component; significa no autorizarla todavía.

## 5. Criterios para reabrir la investigación

Reabrir este tema si aparece al menos una de las siguientes evidencias verificables:

1. Un consumer documental encuentra una dificultad concreta para aplicar el contrato por no existir `README-LICENSE` canónico.
2. Varios consumers necesitan resolver repetidamente el mismo problema y aparece un patrón reusable con límites claros.
3. Una prueba de uso muestra confusión recurrente entre `Required`, `Conceptual` y `Satisfied`.
4. Un caso de implementación representativo demuestra que materializar `README-LICENSE` aporta valor superior a conservar una solución propia del consumer.
5. Evidencia de diseño cuestiona justificadamente el requirement level actual, **independientemente** de la disponibilidad del Component.

En ese caso, iniciar **Solution Shaping** de forma explícita y comparar alternativas antes de comprometer un Delivery Scope.

## 6. Prioridad recomendada para la evolución del proyecto

Con esta investigación acotada, el siguiente esfuerzo debe buscar evidencia de **valor de uso del Framework**, no aumentar automáticamente el catálogo documental.

Candidatos de investigación, sin orden de implementación comprometido:

| Línea | Pregunta concreta | Posible evidencia |
|---|---|---|
| Adoption end-to-end | ¿Puede un consumer completar Assessment y, si procede, Application e Integration con registros trazables y coste razonable? | Recorrido observable sobre un caso pequeño; decisiones humanas explícitas |
| Templates en uso | ¿Qué trabajo manual debe repetir un usuario al partir de una composición existente? | Pasos reales, bloqueos, repetición y materiales consumidos |
| Validator y expectativas | ¿Los usuarios comprenden qué valida el CLI y sobre qué repositorio? | Lectura del entry point, ejecución controlada y tareas de comprensión |
| UX-02 pendiente | ¿La navegación inicial posterior a PR #90 funciona para personas nuevas? | Sesiones reales conforme al protocolo #54 |

La línea UX-02 permanece en estado **Prepared — Not Executed** hasta disponer de participantes independientes. No debe bloquear investigaciones técnicas distintas.

## 7. Estado de cierre

| Elemento | Estado |
|---|---|
| Discovery #55 — Functional maturity baseline | Completado |
| Discovery #56 — Materialization reality check | Completado |
| Discovery #57 — External consumer license case | Completado, acotado a una Responsibility |
| Discovery #58 — Synthesis and decision boundary | Completado |
| `README-LICENSE` materialización | No comprometida |
| `TPL-DOCUMENTATION` contract changes | No comprometidos |
| Nuevo Product Backlog item | No creado |
| Sprint / milestone / release | Ninguno abierto por este trabajo |

**Resultado final:** la evidencia justifica mantener la distinción entre disponibilidad de Components y cobertura de responsabilidades, pero **no justifica todavía ninguna modificación funcional**. El siguiente trabajo deberá proporcionar evidencia directa de una necesidad de uso antes de seleccionar solución.

Este documento es una síntesis y una frontera de decisión de Discovery; **no constituye un Delivery Scope, plan de implementación, verificación de código ni aprobación de release**.
