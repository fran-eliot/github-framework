# 56 — Documentation Template Materialization Reality Check

| Campo | Valor |
|---|---|
| Proyecto | GitHub Framework |
| Fecha | 2026-11-11 |
| Estado | Discovery — bounded reality check |
| Framework baseline | v0.10.0 |
| Template | `TPL-DOCUMENTATION v0.1.0` |
| Template status / maturity | `Experimental` / `L2` |
| Referencia previa | [55 — Framework Functional Maturity Discovery](55_FRAMEWORK_FUNCTIONAL_MATURITY_DISCOVERY.md) |
| Delivery / Sprint / milestone | No comprometidos |

> Este documento comprueba la distinción entre disponibilidad canónica de Components y satisfacción de Responsibilities por parte de un consumer. No es una evaluación completa de conformidad, un Delivery Scope ni una autorización para cambiar el Template o materializar Components.

---

## 1. Pregunta de investigación

El análisis funcional #55 observó un gap en `TPL-DOCUMENTATION`: uno de sus nueve Components `Required` figura como `Conceptual`. Se investiga:

> ¿Impide realmente el estado conceptual de `README-LICENSE` utilizar `TPL-DOCUMENTATION` en un repositorio documental existente, o solo limita la reutilización de una implementación canónica desde el Framework?

**Hipótesis:** el gap corresponde a la disponibilidad de un Component canónico, no necesariamente a la satisfacción de la responsabilidad por cualquier consumer.

## 2. Fuentes revisadas

- [TPL-DOCUMENTATION metadata](../../framework/templates/repositories/documentation/metadata.yml) — fuente canónica del contrato.
- [TPL-DOCUMENTATION README](../../framework/templates/repositories/documentation/README.md) — alcance, disponibilidad y límites.
- [Repository Template Library](../../framework/templates/repositories/README.md) — clasificación, versión y conformance.
- [Component Catalog](../design-system/09_COMPONENT_CATALOG.md), secciones 19 y 48 — distinción conceptual y definición de `README-LICENSE`.
- [Framework README](../../README.md), sección `License`, y [LICENSE](../../LICENSE) — ejemplo observable dentro del propio Framework.
- [Adoption Assessment Guide](../../framework/adoption/README.md) — principios `Responsibility over File` y revisión humana.

Estos son resultados de **inspección documental de los artefactos publicados**, no de ejecución del Framework Validator o de un Assessment externo.

## 3. Contrato canónico de TPL-DOCUMENTATION

La metadata declara:

```yaml
id: TPL-DOCUMENTATION
version: 0.1.0
status: Experimental
project_type: Documentation
maturity: L2
```

Su composición incluye **9 Required, 7 Recommended y 5 Optional** (21 Responsibilities / Components referenciados). La sección de disponibilidad de su README registra:

| Requirement level | Implemented | Declarados |
|---|---:|---:|
| Required | 8 | 9 |
| Recommended | 2 | 7 |
| Optional | 1 | 5 |
| **Total** | **11** | **21** |

El único gap identificado entre los Required es:

```text
README-LICENSE → Conceptual
```

La clasificación no modifica automáticamente el requirement level `Required`; tampoco significa que el Template completo esté ausente o no se pueda utilizar para razonar sobre Responsibilities.

## 4. Significado de README-LICENSE

El catálogo define `README-LICENSE` como **responsabilidad de comunicar desde el README la licencia aplicable al proyecto**.

Su clasificación publicada es:

```text
Family: README
Implementation: Conceptual
```

El catálogo precisa que un archivo `LICENSE` en un consumer cubre una responsabilidad relacionada, pero **no constituye por sí solo la implementación canónica reutilizable** del Component `README-LICENSE`.

No se deben equiparar las siguientes afirmaciones:

```text
LICENSE file exists
    ≠
README communicates applicable license
    ≠
Framework provides a canonical reusable README-LICENSE Component
```

El contrato de `TPL-DOCUMENTATION` exige la responsabilidad correspondiente; la disponibilidad de un Component físico reusable constituye otra dimensión.

## 5. Caso observable: el propio GitHub Framework

El repositorio `fran-eliot/github-framework` incluye:

- Una sección `## 📄 License` en el [README](../../README.md), con la frase que comunica que el proyecto se distribuye bajo licencia MIT.
- Un archivo [LICENSE](../../LICENSE) que contiene el texto de la licencia MIT y su copyright.

Estos son **Detected Facts** obtenidos directamente de la documentación. Apoyan la hipótesis de que un consumer puede comunicar su licencia sin materializar previamente `README-LICENSE` como Framework Component.

### Límites del ejemplo

- No se declara que `github-framework` sea un consumer formal de `TPL-DOCUMENTATION`; el repositorio combina documentación y tooling ejecutable.
- No se ha completado un Assessment de la Responsibility `README-LICENSE` en un consumer documental independiente.
- La presencia de una sección de licencia y de `LICENSE` constituye evidencia, no una decisión automática `Satisfied` ni una `Adoption Decision`.
- El ejemplo no demuestra que la implementación observada deba convertirse en el contenido canónico de un nuevo Component.

## 6. Distinción arquitectónica confirmada

El Component Catalog y la Template Library mantienen la regla:

```text
Component availability
    ≠
Consumer conformance
```

Un consumer puede satisfacer una Responsibility mediante una implementación propia, distribuida o equivalente mientras el Framework Component permanece `Conceptual`.

Por tanto, dos afirmaciones pueden ser simultáneamente verdaderas:

1. `TPL-DOCUMENTATION` **no es plenamente materializable usando únicamente Components canónicos implementados** del Framework en su versión actual.
2. Un consumer **podría cumplir la responsabilidad de comunicar la licencia** mediante artefactos propios sin esperar a que exista un Component canónico.

La conformidad concreta requiere evaluación frente a la Responsibility, Evidence y revisión humana. No se deduce de la presencia de un archivo aislado.

## 7. Revisión de alternativas, sin decisión de solución

| Alternativa | Qué resolvería | Qué falta demostrar |
|---|---|---|
| A. Mantener contrato y clasificación | Conserva el modelo actual y permite implementaciones propias | Que la limitación de disponibilidad sea aceptable para consumidores documentales reales |
| B. Materializar `README-LICENSE` como Component | Haría disponible una implementación canónica reusable y podría cerrar el gap de Required materializados | Necesidad real, definición de contrato, mínima composición, variabilidad de licencias y costes de mantenimiento |
| C. Revisar el requirement level de `README-LICENSE` | Cambiaría el mínimo contractual de `TPL-DOCUMENTATION` | Evidencia de que comunicar la licencia no sea Required para el tipo de repositorio; no basta con que falte una implementación |
| D. Documentar una vía de composición propia para consumidores | Aclara las opciones cuando la Responsibility existe sin Component canónico | Dudas observadas de usuarios y ausencia de información equivalente en las guías actuales |

Ninguna alternativa se selecciona aquí; en especial, **un gap de materialización no autoriza a rebajar un Requirement Level**.

## 8. Registro de hallazgos

| ID | Hallazgo | Estado |
|---|---|---|
| TM-F01 | `TPL-DOCUMENTATION v0.1.0` referencia `README-LICENSE` como Required y Conceptual. | Confirmado |
| TM-F02 | El Component Catalog diferencia explícitamente comunicar la licencia en README de poseer un archivo LICENSE. | Confirmado |
| TM-F03 | El Framework mismo contiene comunicación de licencia en README y un archivo LICENSE. | Confirmado como caso observable |
| TM-F04 | El estado `Conceptual` limita disponibilidad canónica, pero no determina automáticamente la conformidad de un consumer. | Confirmado en contratos publicados |
| TM-F05 | La falta de un Component canónico provoca una barrera significativa para consumidores documentales reales. | **No demostrado** |
| TM-F06 | Es necesario materializar `README-LICENSE` o cambiar su requirement level. | **No demostrado** |

## 9. Investigación pendiente

Antes de Solution Shaping o Product Backlog:

1. Seleccionar un repositorio **primariamente documental**, con identidad y reference inmutables, que no haya sido construido para satisfacer deliberadamente el contrato de este Template.
2. Registrar solo la Evidence necesaria para la responsabilidad `README-LICENSE` (sección del README, enlace o texto de licencia, archivo relacionado, aclaraciones y contexto), sin deducir conformidad de un nombre de archivo.
3. Clasificar la cobertura de la Responsibility mediante revisión humana, dejando incertidumbres explícitas.
4. Comprobar si la ausencia de Component canónico genera fricción real para adoptar el Template, independientemente de la cobertura observada.
5. Repetir o contrastar con otro consumer únicamente si el primer caso no permite distinguir las hipótesis.

Si no aparece una necesidad reproducible, **no materializar ni reclasificar por inercia**.

## 10. Resultado y frontera de decisión

**Resultado del Reality Check:** se ha confirmado un gap de **materialización canónica**, no una imposibilidad universal de uso ni un defecto probado del contrato de `TPL-DOCUMENTATION`.

El siguiente trabajo requiere evidencia específica de un consumer documental. No se han modificado Templates, Components, Validator ni consumers. No se ejecutó Assessment completo ni se realizó promoción a `Stable`.

**Decisión:** mantener abiertas las alternativas y continuar Discovery, sin comprometer implementación, Sprint, milestone o release.
