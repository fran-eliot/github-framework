# 55 — Framework Functional Maturity Discovery

| Campo | Valor |
|---|---|
| Proyecto | GitHub Framework |
| Fecha | 2026-11-11 |
| Versión publicada de referencia | `v0.10.0` |
| Estado | Discovery — baseline documental y de código, no Delivery Scope |
| Objeto | Repository Templates, Framework Validator y Existing Repository Adoption |
| Investigación precedente | [54 — First-Time Usability Validation Protocol](54_FIRST_TIME_USABILITY_VALIDATION_PROTOCOL.md) |
| Decisión de implementación | Ninguna |
| Sprint / milestone / nueva versión | Ninguno comprometido |

> Este documento examina la **capacidad realmente observable en los artefactos publicados**, separándola de los contratos conceptuales y de las opciones futuras. La revisión de código es estática: no se ejecutó aquí la batería de tests ni el CLI.

---

## 1. Objetivo

Establecer una baseline contrastable para responder:

> ¿Qué puede utilizar realmente un desarrollador externo en GitHub Framework v0.10.0, qué requiere intervención humana y qué queda todavía como contrato conceptual?

Las tres áreas examinadas son:

1. Repository Templates y disponibilidad material de Components.
2. Framework Validator, cobertura y límites de ejecución.
3. Existing Repository Adoption, desde Assessment hasta Integration, con soporte de Assisted Analysis.

La auditoría no presupone que deba crearse una CLI de adopción, un generador, un nuevo Template, un manifest o un sistema de remediación.

## 2. Método y fuentes

Se examinaron archivos públicos de la rama `main` posterior a la PR #91, incluyendo:

- [Repository Template Library](../../framework/templates/repositories/README.md).
- [Backend Template](../../framework/templates/repositories/backend/README.md) y su [metadata](../../framework/templates/repositories/backend/metadata.yml).
- [FullStack Template](../../framework/templates/repositories/fullstack/README.md) y su [metadata](../../framework/templates/repositories/fullstack/metadata.yml).
- [Documentation Template](../../framework/templates/repositories/documentation/README.md) y su [metadata](../../framework/templates/repositories/documentation/metadata.yml).
- [Framework Validator, entry point](../../scripts/framework_validator/__main__.py).
- [Automation Reference Implementation](../implementation/22_AUTOMATION_REFERENCE_IMPLEMENTATION.md).
- [Assessment Guide](../../framework/adoption/README.md) y [Assessment Template](../../framework/adoption/assessment-template.md).
- [Application Guide](../../framework/adoption/application/README.md) y [Application Record](../../framework/adoption/application/application-template.md).
- [Integration Guide](../../framework/adoption/integration/README.md) y [Integration Record](../../framework/adoption/integration/integration-template.md).
- [Assisted Analysis Guide](../../framework/adoption/assisted-analysis/README.md) y [Evidence Snapshot Template](../../framework/adoption/assisted-analysis/evidence-snapshot-template.md).
- [Assisted Analysis Core Verification](../implementation/52_ASSISTED_ANALYSIS_CORE_VERIFICATION.md).

**Alcance de verificación:** existen y se han leído los artefactos indicados. Los resultados históricos de tests y replays se citan como evidencia previamente documentada, no como ejecuciones realizadas en esta auditoría.

## 3. Repository Templates: capacidades y límites

### 3.1 Disponibilidad comprobada

La biblioteca canónica está en `framework/templates/repositories/` y define tres Templates:

```text
TPL-BACKEND
TPL-FULLSTACK
TPL-DOCUMENTATION
```

Cada uno dispone de `README.md` y `metadata.yml`. La metadata identifica el Template, versión, estado, tipo de proyecto, madurez y Components clasificados en `required`, `recommended` y `optional`.

Los Templates son **composiciones declarativas** de Components, no repositorios finalizados ni generadores ejecutables. El directorio físico `template/` es opcional y no debe crearse si no existen artefactos propios del Template que lo requieran.

### 3.2 Disponibilidad material comunicada

| Template | Required implementados | Recommended implementados | Optional implementados | Total implementados |
|---|---:|---:|---:|---:|
| `TPL-BACKEND` | 8/8 | 5/7 | 3/13 | 16/28 |
| `TPL-FULLSTACK` | 9/9 | 4/8 | 3/11 | 16/28 |
| `TPL-DOCUMENTATION` | 8/9 | 2/7 | 1/5 | 11/21 |

**Procedencia:** secciones de disponibilidad declaradas en los README canónicos de los respectivos Templates. La cifra no equivale a ejecución actual del Validator ni a un recuento independiente de todo el inventario.

`TPL-DOCUMENTATION` identifica expresamente `README-LICENSE` como Required todavía `Conceptual`. Su contrato mínimo no es plenamente materializable solo con Components implementados. Los niveles `Required`, `Recommended` y `Optional` no deben confundirse con la clasificación física `Implemented` / `Conceptual`.

### 3.3 Valor utilizable y límites

**Disponible:** selección manual de composición según tipo de proyecto, consulta de contrato/versionado y referencia de Responsibilities para evaluación o construcción consciente.

**No implementado como herramienta:** generación automática de esqueleto, instanciación guiada y parametrización automática. Tampoco se ha observado un validador ejecutable específico para conformidad de Repository Templates en este análisis.

**Cuestión de madurez:** ¿es suficiente la composición declarativa para el público objetivo actual o existe una necesidad repetible de materialización/adopción más directa? No se decide aún.

## 4. Framework Validator: capacidades y límites

### 4.1 Comportamiento verificable por código

El entry point `scripts/framework_validator/__main__.py` define:

```text
REPOSITORY_ROOT = path of this Framework checkout
COMPONENTS_ROOT = REPOSITORY_ROOT / "framework" / "components"
```

Su función `main()` descubre directorios de Component, lee `metadata.yml` y ejecuta validaciones de:

- Common Core y campos opcionales;
- identidad y unicidad de Component IDs;
- maturity y dependencies;
- extensiones Workflow: materialization, artifacts, artifact files, adoption y validation.

El CLI imprime resultados y devuelve `0` cuando no encuentra errores, o `1` cuando encuentra errores. Se invoca desde la raíz del Framework mediante `python -m scripts.framework_validator`.

La Reference Implementation de v0.6.0 documenta una distribución de **21 Components físicos**: 4 Documentation, 12 README y 5 Workflow, junto con pruebas aisladas y dogfooding histórico.

### 4.2 Límite estructural

El `COMPONENTS_ROOT` codificado apunta al propio checkout de GitHub Framework. El CLI no recibe en este entry point un consumer repository arbitrario como target de evaluación y **no** calcula automáticamente la satisfacción semántica de las Responsibilities de un consumer.

Tampoco genera contenido, aplica cambios de Adoption ni valida Evidence Snapshots: este último límite se confirma en el documento de verificación del Assisted Analysis Core.

**No inferir:** que el Validator esté defectuoso por no cumplir funciones que nunca pertenecieron a su alcance. Es una herramienta implementada de consistencia del catálogo del Framework, no un asesor automatizado de adopción.

## 5. Existing Repository Adoption: capacidades y límites

| Capacidad | Artifact principal | Trabajo que soporta | Boundary |
|---|---|---|---|
| Assessment Core | Guide + Structured Markdown Assessment Template | ANALYZE → ASSESS → REVIEW → DECIDE → REPORT | Resultado persistente, sin modificación del consumer |
| Application Core | Guide + Application Record | SELECT, refresh Evidence, plan, review, apply in isolation y verify | Termina en verified candidate state; cambio humano y acotado |
| Integration Core | Guide + Integration Record | Refresh stable base, drift, governance checks, review, integrate, verify stable state | Verified stable state o safe-stop/recovery-required state |
| Assisted Analysis Core | Guide + Evidence Snapshot Template | Evidence determinista, bounded, source-traceable y read-only para las otras tres capabilities | No ejecuta evaluación semántica ni adopta decisiones |

### 5.1 Estado de la implementación

La documentación de implementación y verificación establece los cuatro Cores como entregados en las versiones publicadas, incluido el Assisted Analysis Core en v0.10.0. La verificación anterior registra replays A/B/C y AC-01…AC-73 como `PASS`.

**Naturaleza de los entregables:** son guías y representaciones Markdown reutilizables. No hay un motor de ejecución de Assessment, Application o Integration demostrado por estos artifacts. El desarrollo humano debe recopilar evidencia, interpretarla y efectuar las operaciones permitidas respetando las condiciones de cada Guide.

`Application` puede contemplar cambios materiales **ejecutados por personas bajo revisión**; no debe describirse como necesariamente read-only. `Assisted Analysis` sí es explícitamente read-only.

### 5.2 Valor y fricción potencial

**Valor actual:** modelo trazable, revisable, no destructivo por defecto, compatible con implementaciones no canónicas, decisiones humanas y gobierno del consumer.

**Fricción candidata, no validada:** el tránsito manual entre cuatro Guides y sus registros puede exigir esfuerzo significativo para una primera adopción. UX-01 trató solo el punto de entrada; UX-02 tiene protocolo aprobado pero todavía no se ha ejecutado con participantes independientes.

**No asumir** que la longitud de las Guides demuestra por sí sola un fallo de usabilidad o justifica un motor automatizado.

## 6. Mapa de madurez observable

| Área | Contrato documentado | Artifact reutilizable | Ejecución automatizada específica | Evidencia de uso |
|---|---|---|---|---|
| Repository Templates | Sí | Sí (metadata y README) | No documentada para instanciación | Reference Implementations / Discovery anteriores |
| Framework Validator | Sí | Sí (código Python) | Sí, validación de Components del Framework | Tests y dogfooding de v0.6.0 documentados |
| Assessment | Sí | Sí (Guide + Template) | No, evaluación humana | Experimentos y verificación de v0.7.0 |
| Application | Sí | Sí (Guide + Record) | No, aplicación humana en aislamiento | Verificación de v0.8.0 |
| Integration | Sí | Sí (Guide + Record) | No, integración bajo governance humana | Verificación de v0.9.0 |
| Assisted Analysis | Sí | Sí (Guide + Snapshot) | No, recopilación documentada y humana | Replays y verificación de v0.10.0 |

Este mapa presenta la implementación **según lo leído**, no una certificación integral de ejecución de cada capability sobre cualquier repositorio externo.

## 7. Hallazgos preliminares

### FM-F01 — La composición y la materialización son dimensiones distintas

Los tres Repository Templates están especificados, pero no todos tienen disponibles todos sus Components. `TPL-DOCUMENTATION` contiene un gap material en Required. Esto no implica automáticamente falta de conformidad en un consumer con una implementación propia o equivalente.

### FM-F02 — El Validator tiene un límite de objetivo deliberado

El CLI inspecciona metadata de `framework/components/` del proyecto, no Responsibilities en un consumer arbitrario. Una eventual ampliación requeriría justificar caso de uso, contrato y frontera semántica, no reutilizar el nombre del Validator para prometer conformidad automática.

### FM-F03 — Adoption es reutilizable sin ejecución automática

La cadena Assessment → Application → Integration está documentada y Assisted Analysis puede aportar Evidence. El valor actual está en las prácticas y los registros verificables; la automatización no forma parte del delivery publicado.

### FM-F04 — Hay una diferencia entre verificación arquitectónica y adopción autónoma

Las verificaciones históricas demuestran los límites y criterios del delivery correspondiente. No bastan por sí solas para concluir que una persona nueva pueda ejecutar todo el flujo sin acompañamiento. UX-02 permanece pendiente de ejecución.

## 8. Hipótesis de investigación priorizadas

| Orden de investigación | Hipótesis | Evidencia necesaria antes de Solution Shaping |
|---|---|---|
| 1 | La disponibilidad incompleta de Components en algunos Templates afecta al primer uso. | Escenarios reales de `TPL-DOCUMENTATION` y distinción entre implementación canónica y equivalente |
| 2 | El recorrido manual de Adoption tiene puntos de fricción repetibles entre registros. | Observación de un consumer y trazabilidad entre Assessment, Application, Integration y Evidence Snapshot |
| 3 | Los usuarios interpretan erróneamente el alcance del Framework Validator. | Tareas/documentación que muestren expectativas reales sobre qué valida y sobre qué repositorio |
| 4 | Podría existir una necesidad de automatizar tareas deterministas concretas. | Repetición de operaciones, coste observado y límites semánticos; no derivarla solo de preferencias |

El orden es **de investigación**, no de implementación, y no implica escoger un próximo producto, release o backlog item.

## 9. Próxima comprobación recomendada

Antes de crear funcionalidades, realizar un **Template Materialization Reality Check** acotado:

1. Revisar `TPL-DOCUMENTATION` y su gap `README-LICENSE`.
2. Distinguir qué parte de ese gap afecta al Framework y cuál puede satisfacer un consumer con materialización propia.
3. Examinar evidencia de casos reales ya documentados para evitar repetir experimentos.
4. Determinar si aparece una necesidad reproducible de nuevo Component, cambio de requirement level o ninguna modificación.

La investigación debe mantenerse read-only respecto a los consumers y registrar cualquier incertidumbre. Si la evidencia apunta a un cambio, abrir Solution Shaping por separado antes de definir Delivery Scope.

## 10. Conclusión

GitHub Framework v0.10.0 cuenta con Templates estructurados, un Validator ejecutable orientado a su propio catálogo y un modelo completo de Adoption con artefactos Markdown revisables. La ausencia de ejecución automática en determinadas capacidades es un límite **de alcance**, no necesariamente un defecto.

La siguiente cuestión de madurez con evidencia tangible es la diferencia entre contrato conceptual y disponibilidad material de Components, especialmente en `TPL-DOCUMENTATION`.

**Estado:** Discovery inicial completado; sin aceptación de solución, sin Sprint y sin release comprometida.
