# 57 — Documentation Consumer License Responsibility Case Study

| Campo | Valor |
|---|---|
| Proyecto | GitHub Framework |
| Fecha | 2026-11-11 |
| Estado | Discovery — bounded evidence review |
| Experimento precedente | [56 — Documentation Template Materialization Reality Check](56_DOCUMENTATION_TEMPLATE_MATERIALIZATION_REALITY_CHECK.md) |
| Consumer | [github/docs](https://github.com/github/docs) |
| Consumer Reference | `2b4f2c7398e04ee8d02adca7440e4286d20c78b9` (`main`) |
| Repository Template | `TPL-DOCUMENTATION` |
| Template Version | `0.1.0` |
| Responsibility observada | `README-LICENSE` (`Required`) |
| Cobertura de Assessment | Una Responsibility; no es Assessment completo |
| Consumer mutation | Ninguna |

> Los resultados de este caso solo se aplican a la evidencia observada en la referencia fijada. El consumer se utiliza como ejemplo documental independiente; no se sostiene que adopte formalmente GitHub Framework.

---

## 1. Objetivo y pregunta

Continuar la investigación de #56 con evidencia de un repositorio cuyo producto principal es documentación y que no haya sido construido explícitamente para satisfacer los contratos de GitHub Framework.

Pregunta:

> ¿Puede observarse en un consumer documental real una implementación propia de la responsabilidad `README-LICENSE` pese a que el Framework Component permanezca clasificado como `Conceptual`?

No se intenta determinar la conformidad global del consumer, ni el cumplimiento de las otras 20 Responsibilities del Template, ni las obligaciones jurídicas de las licencias.

## 2. Criterio de selección

Se selecciona [github/docs](https://github.com/github/docs), repositorio abierto de documentación de GitHub, porque:

- El [README](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/README.md) declara expresamente que contiene documentación abierta a contribuciones.
- La estructura de la raíz contiene `content/`, `data/`, `assets/` y también código de publicación en `src/`.
- Es un caso **documentation-first**, aunque no exclusivamente documental: la presencia de tooling y código requiere mantener explícito ese matiz.
- Dispone de información observable sobre licencias tanto de documentación como de código.

La selección se fundamenta en la orientación del producto y los artefactos publicados. No implica una asignación formal del Template al consumer.

## 3. Baselines y contrato

La referencia del consumer es el commit inmutable:

```text
github/docs
2b4f2c7398e04ee8d02adca7440e4286d20c78b9
```

El contrato de comparación es `TPL-DOCUMENTATION v0.1.0`:

- [metadata canónica](../../framework/templates/repositories/documentation/metadata.yml).
- [README canónico](../../framework/templates/repositories/documentation/README.md).
- [definición conceptual de README-LICENSE](../design-system/09_COMPONENT_CATALOG.md), sección 48.

La metadata del Template declara `README-LICENSE` entre los 9 Components `Required`. El catálogo lo clasifica como `Conceptual`; la responsabilidad reconocida es **comunicar desde el README la licencia aplicable al proyecto**.

## 4. Detected Facts y Evidence

| ID | Detected Fact | Evidence fijada |
|---|---|---|
| E-01 | El README presenta el repositorio como documentación de GitHub, abierta a contribuciones. | [`README.md`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/README.md), inicio |
| E-02 | El README contiene una sección `License`. | [`README.md`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/README.md), sección final |
| E-03 | La sección `License` distingue una licencia Creative Commons Attribution 4.0 para documentación/contenido y MIT para código. | [`README.md`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/README.md), sección `License` |
| E-04 | El README enlaza explícitamente a `LICENSE` y `LICENSE-CODE`. | [`README.md`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/README.md), enlaces relativos |
| E-05 | `LICENSE` contiene el texto de Creative Commons Attribution 4.0 International. | [`LICENSE`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/LICENSE), encabezado |
| E-06 | `LICENSE-CODE` contiene el texto de la licencia MIT. | [`LICENSE-CODE`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/LICENSE-CODE), encabezado |

No se reproduce el texto de las licencias: los enlaces son las fuentes revisables.

## 5. Evaluación acotada de la Responsibility

| Campo | Evaluación del caso |
|---|---|
| Responsibility | `README-LICENSE` |
| Requirement Level | `Required` |
| Applicability | `Applicable` |
| State provisional | `Satisfied` — solo para la responsabilidad de comunicar la licencia desde README |
| Implementation Characteristics | `Own`, `Specialized`, `Distributed` (descriptivas) |
| Decision Status | `Needs Further Evaluation` |
| Adoption Decision | `—` |
| Framework Component availability | `Conceptual` |
| Full Template conformance | **No evaluada** |

### Evaluation Rationale

El README comunica explícitamente las licencias aplicables a dos conjuntos de artefactos y proporciona enlaces a las fuentes correspondientes. Para el propósito acotado de `README-LICENSE` descrito por el catálogo, esa evidencia **sustenta una evaluación provisional `Satisfied`**, aunque no exista un componente canónico reutilizable dentro del Framework.

Se registra `Applicable` por la distribución declarada de contenido y código bajo licencias explícitas. La implementación es `Own` al estar definida en el consumer, `Specialized` por distinguir tipos de artefactos y `Distributed` por repartir comunicación y textos jurídicos entre README y archivos de licencia.

La evaluación es **documental, no legal**: no verifica exhaustivamente titularidad, licencias de recursos de terceros ni suficiencia jurídica de cada declaración.

### Uncertainty y revisión

- No se ha realizado una revisión humana formal dentro de un Assessment completo.
- No se ha comprobado si el consumer presenta otros mecanismos complementarios de información sobre licencias.
- No se han contrastado todas las condiciones de `TPL-DOCUMENTATION`.
- Las características descriptivas no constituyen una clasificación contractual cerrada.
- No consta decisión del equipo de `github/docs` de adoptar GitHub Framework.

Por estos motivos, **no se elige `PRESERVE`, `ACCEPT` ni otra Adoption Decision**. La evidencia del caso no debe utilizarse para autorizar cambios en el repositorio consumidor.

## 6. Contraste de hipótesis

| Hipótesis de #56 | Resultado del caso | Límite |
|---|---|---|
| Un consumer puede cubrir `README-LICENSE` mediante implementación propia. | **Respaldada** por evidencia concreta de comunicación de licencias en README. | Se ha revisado una sola Responsibility y un consumer. |
| La clasificación `Conceptual` implica `Missing` en todo consumer. | **No respaldada**: el caso proporciona cobertura documental observable. | No sustituye el Assessment del consumer. |
| Es necesario materializar ahora el Component canónico. | **No demostrado**. | No se observó a un usuario intentando adoptar este Template. |
| Conviene rebajar `README-LICENSE` de Required. | **No demostrado**. | La exigencia de comunicar licencia tiene utilidad observable; cambiar requirement level requiere evidencia propia. |
| El gap canónico impide utilizar el Template. | **No demostrado**. | El caso muestra evidencia de una Responsibility, no una adopción completa. |

## 7. Hallazgos

**LC-F01 — La cobertura de una Responsibility no depende exclusivamente de la biblioteca materializada.** El caso muestra una comunicación propia y diferenciada de licencias en el README.

**LC-F02 — La implementación observada puede ser distribuida y especializada.** README, `LICENSE` y `LICENSE-CODE` desempeñan funciones distintas y complementarias.

**LC-F03 — La disponibilidad de un Component y el State de un consumer son ejes independientes.** La evidencia es compatible con `Conceptual` a nivel Framework y `Satisfied` provisional a nivel consumer.

**LC-F04 — No se ha observado fricción de adopción.** Una inspección documental puede demostrar que existe una implementación; no mide la dificultad de consumirla ni de producirla desde el Framework.

## 8. Decisión de Discovery y próximos pasos

Se conserva el contrato actual:

```text
TPL-DOCUMENTATION v0.1.0
    README-LICENSE: Required
    Component classification: Conceptual
```

No se propone automáticamente crear `README-LICENSE`, reclasificarlo, alterar el Template o declarar un nuevo release.

**Siguiente comprobación útil:** estudiar cómo un usuario de `TPL-DOCUMENTATION` interpretaría la coexistencia de `Required` y `Conceptual`, o contrastar un segundo consumer documental si aparece una incertidumbre específica. La inexistencia de una implementación canónica solo se convierte en necesidad de producto cuando hay evidencia de fricción, repetibilidad o beneficio de reutilización.

No se modifica `github/docs`, ni el Framework fuera de este documento. No hay Sprint ni versión comprometida.

## 9. Conclusión

En `github/docs`, la evidencia visible del README y sus dos archivos de licencia respalda **provisionalmente** la cobertura de `README-LICENSE` mediante una implementación propia, especializada y distribuida.

Esto distingue **conformance de un consumer** de **materialización canónica disponible en GitHub Framework** y evita inferir un nuevo desarrollo a partir de un gap de catálogo.

**Resultado:** evidencia de un consumer documental real, acotada a una Responsibility y sin decisión de implementación.
