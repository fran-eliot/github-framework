# 53 — First-Time User Experience Discovery

**Proyecto:** GitHub Framework  
**Fecha:** 2026-11-07  
**Estado:** Discovery exploratorio — síntesis preliminar  
**Versión de referencia:** `v0.10.0`  
**Experimento:** `UX-01 — First-Time Adoption Journey`  
**Consumer:** `fran-eliot/seniormeet`  
**Consumer reference:** `b84b0de246d459caf594a5cdacbe8fccfa68698a` (`master`)  
**Repository Template candidato:** `TPL-BACKEND v0.1.0` (pendiente de comprobar contra su artefacto canónico actual)

> Este documento registra observaciones de navegación y preparación de un assessment. No constituye un assessment completo del consumer, un estudio con usuarios externos, una decisión arquitectónica, un Delivery Scope ni un compromiso de implementación.

---

## 1. Propósito

Investigar si una persona con conocimientos de desarrollo de software, pero sin conocimiento previo de GitHub Framework, puede descubrir los artefactos apropiados y preparar su primer **Existing Repository Adoption Assessment** a partir de la documentación publicada.

Pregunta de investigación:

> ¿Puede un desarrollador nuevo identificar el caso de uso, encontrar un Repository Template, localizar el Assessment Template y preparar evidencia inicial de un consumer real sin acompañamiento específico?

El alcance incluye la experiencia de descubrimiento y preparación, no la ejecución completa de las 28 Responsibilities ni la modificación del consumer.

## 2. Contexto y límites

La versión `v0.10.0` incorpora las siguientes capabilities:

- **Assessment Core:** evaluación estructurada de Responsibilities mediante Evidence y revisión humana.
- **Application Core:** cambios acotados en aislamiento, seguidos de verificación.
- **Integration Core:** incorporación controlada de un candidate state verificado al estado estable.
- **Assisted Analysis Core:** recopilación opcional, read-only, acotada y trazable de Evidence; no automatiza evaluación semántica ni decisiones.

El Framework dispone asimismo de Standards, Components, Repository Templates y un Framework Validator determinista. El Validator no sustituye la evaluación semántica ni genera automáticamente repositorios.

Los resultados se obtuvieron mediante una **simulación documental asistida**, basada en la inspección de GitHub. No se observó a un usuario externo y no se midieron tiempos, tasa de éxito ni esfuerzo subjetivo. Las conclusiones de usabilidad deben interpretarse en consecuencia.

## 3. Escenario y selección del consumer

Consumer seleccionado: [`fran-eliot/seniormeet`](https://github.com/fran-eliot/seniormeet).

Evidencia estructural observada en el commit de referencia:

| Fuente | Hecho observado |
|---|---|
| `README.md` | Dos líneas: identifica `SENIOR MEET` como red social para personas mayores. |
| `pom.xml` | Proyecto Maven, Spring Boot 3.2.2, Java 21; dependencias Spring Web, Spring Data JPA y testing. |
| `Dockerfile` | Contiene una etapa de build con una imagen de Maven/OpenJDK 17. |
| `docker-compose.yml` | Declara servicios MySQL y aplicación Spring. |

La naturaleza backend del proyecto está suficientemente respaldada para considerarlo **candidato** a una prueba con `TPL-BACKEND`; ello no demuestra satisfacción de las Responsibilities del Template.

La diferencia Java 21 (`pom.xml`) / Java 17 (imagen de build) es un hecho de configuración que requeriría verificación específica para extraer conclusiones de ejecución. No es un finding de usabilidad del Framework y no se ha corregido.

## 4. Recorrido UX-01 y resultados

### UX-01.1 — Consumer suitability

**Resultado:** elegibilidad estructural favorable para un escenario backend. No se realizó evaluación de responsabilidades.

### UX-01.2 — First-time navigation

Recorrido simulado:

```text
GitHub Framework README
    ↓
Existing Repository Adoption Guide
    ↓
Identify Repository Template and version
    ↓
Assessment Template
    ↓
Prepare Assessment Context
```

Observaciones:

- El README principal ofrece un enlace a Existing Repository Adoption.
- `Getting Started` propone explorar el README, la documentación, los Components, la arquitectura y el roadmap, sin llevar explícitamente a un primer resultado práctico.
- La Adoption Guide describe las cuatro entradas conceptuales del Assessment, pero la sección inicial no ofrece una ruta directa hacia un catálogo de Templates.
- El README principal enlaza el Assessment Template.
- El usuario debe reconstruir la relación entre el caso de uso backend, el Template, su versión y el registro de Responsibilities.

### UX-01.3 — Repository Template discoverability

La documentación de Discovery anterior identifica `TPL-BACKEND v0.1.0` como Template experimental de madurez L2, con:

- 8 responsabilidades `Required`;
- 7 responsabilidades `Recommended`;
- 13 responsabilidades `Optional`.

**Límite de evidencia:** durante este recorrido no se localizó ni verificó la ubicación física actual del artefacto canónico. Ello **no** demuestra que el Template falte; demuestra que la navegación seguida no permitió localizarlo y verificarlo.

La selección formal debe permanecer pendiente hasta consultar el Template canónico.

### UX-01.4 — First Assessment Readiness

Se puede preparar parcialmente el bloque `Assessment Context`:

| Campo | Valor provisional | Evidencia/estado |
|---|---|---|
| Consumer Repository | `fran-eliot/seniormeet` | Verificado |
| Consumer Reference | `b84b0de246d459caf594a5cdacbe8fccfa68698a` | Verificado |
| Repository Template | `TPL-BACKEND` | Candidato |
| Template Version | `0.1.0` | Documentada en Discovery anterior; comprobar definición vigente |
| Assessment Date | `2026-11-07` | Fecha del ejercicio |
| Assessment Status | `In Progress` | Valor previsto por el Template |

Detected Facts iniciales:

1. Existe un README mínimo que identifica el proyecto.
2. Existe un `pom.xml` con información de framework, lenguaje y dependencias.

Estos hechos **no** permiten asignar `Satisfied`, `Partial` o `Missing` a una Responsibility. Se preserva:

```text
Detected Fact ≠ Evidence ≠ Evaluated State ≠ Adoption Decision ≠ Applied Change
```

No se ejecutó la evaluación de las 28 Responsibilities, no se emitió conformidad global y no se tomó ninguna Adoption Decision.

## 5. Registro de observaciones UX-F01…UX-F10

Los identificadores son **locales al experimento**, no Issues ni requisitos comprometidos.

| ID | Observación | Clasificación | Confianza / límite |
|---|---|---|---|
| UX-F01 | `Getting Started` se centra en explorar documentos, no en producir un primer resultado. | Fricción documental observada | Alta para el texto publicado; impacto real en usuarios no medido |
| UX-F02 | No se presenta un acceso inicial directo a selección/catálogo de Repository Templates desde el recorrido Adoption. | Fricción de navegación observada | Parcial; ubicación canónica no verificada |
| UX-F03 | La Adoption Guide es extensa y requiere manejar numerosos conceptos. | Hipótesis de carga cognitiva | No validada con usuarios |
| UX-F04 | El Assessment Template está enlazado desde el README principal. | Fortaleza observada | Alta |
| UX-F05 | `Getting Started` no enlaza un ejemplo breve de primer Assessment. | Fricción documental observada | Alta para esa sección; otros ejemplos en el repositorio no descartados |
| UX-F06 | El bloque Assessment Context permite registrar los datos del consumer y la situación del ejercicio. | Fortaleza observada | Alta, con selección formal del Template pendiente |
| UX-F07 | El proceso requiere identificar una referencia estable del consumer. | Requisito metodológico explícito | Confirmado en la Guide; su dificultad práctica no medida |
| UX-F08 | En la simulación no se localizó el artefacto canónico actual del Template. | Límite de trazabilidad observado | No equivale a ausencia del artefacto |
| UX-F09 | La separación Fact / Evidence / Evaluation / Decision está documentada. | Fortaleza arquitectónica observada | Alta en documentación; no se evaluó aplicación completa |
| UX-F10 | Iniciar el Assessment exige comprender varios campos y vocabularios. | Hipótesis de carga cognitiva | No validada con usuarios |

## 6. Interpretación y hallazgos preliminares

### H-UX-01 — La navegación inicial está orientada a conocimiento, no a resultado

El Framework presenta su arquitectura y capacidades, pero el recorrido inicial deja al usuario la composición de sus primeros pasos operativos. Es una posible barrera de incorporación, no una carencia demostrada del modelo de adopción.

### H-UX-02 — La trazabilidad del Template es un punto de comprobación necesario

Se puede identificar un Template candidato a través del material histórico, pero la definición canónica no fue localizada en el recorrido. Antes de concluir que existe una necesidad de diseño o documentación, se debe localizar el artefacto y comprobar rutas y enlaces reales.

### H-UX-03 — El modelo mantiene separaciones útiles

La Guide y el Assessment Template diferencian hechos, evidencia, evaluación y decisiones. No debe perderse esa distinción por simplificar la experiencia inicial.

### H-UX-04 — La carga cognitiva requiere validación externa

La longitud documental y el número de conceptos sugieren una hipótesis razonable, pero no permiten inferir que personas nuevas no puedan completar el proceso.

## 7. Necesidades candidatas, todavía no demostradas

Se registran como **candidatos a investigar**, sin promoción al Product Backlog:

- RN-UX-01: Comprender si hace falta orientar por **caso de uso** (nuevo repositorio frente a adopción de existente).
- RN-UX-02: Comprobar si la selección y fijación de versión de Repository Template necesita una ruta documental más visible.
- RN-UX-03: Determinar si un ejemplo mínimo de Assessment reduce ambigüedad sin ocultar el modelo de responsabilidades.
- RN-UX-04: Evaluar con usuarios reales la claridad de términos y el esfuerzo para iniciar el proceso.

**No se selecciona solución**: Quick Start, tutorial, índice, wizard, CLI, generación, catálogo interactivo o cambio del Validator permanecen como respuestas posibles, no como entregables decididos.

## 8. Límites y riesgos de interpretación

- La simulación la realizó alguien que conocía el contexto previo del proyecto; no es una evaluación independiente de usabilidad.
- La inspección de contenido no equivale a ejecutar código ni validar workflows.
- Una ruta no localizada en un intento de búsqueda no demuestra que el artefacto no exista.
- Un README corto en el consumer no significa que el Framework haya fallado.
- `Component availability ≠ Consumer responsibility satisfaction`.
- `File present ≠ Responsibility satisfied`.
- No se debe convertir el resultado de UX-01 en una justificación automática de automatización, nuevas features o Release Planning.

## 9. Estado del experimento y próximos controles

| Trabajo | Estado |
|---|---|
| UX-01.1 — Consumer suitability | Completado (estructural) |
| UX-01.2 — First-time navigation | Completado (simulación) |
| UX-01.3 — Template discoverability | Parcial: falta definición canónica |
| UX-01.4 — First Assessment Readiness | Completado con incertidumbres explícitas |
| UX-01.5 — Discovery Synthesis | Este documento, síntesis preliminar |

**Siguiente comprobación prioritaria:** localizar el artefacto canónico de `TPL-BACKEND`, verificar su versión y evaluar si la navegación pública llega a él sin depender de Discovery histórico.

Después, definir una prueba observacional acotada con un desarrollador ajeno al Framework. No repetir el Assessment completo salvo que una pregunta experimental lo exija.

No existe Sprint activo, nueva milestone o versión objetivo comprometida para esta línea de trabajo.

## 10. Referencias verificables

### GitHub Framework

- [README principal](https://github.com/fran-eliot/github-framework/blob/main/README.md)
- [Adoption Guide](https://github.com/fran-eliot/github-framework/blob/main/framework/adoption/README.md)
- [Assessment Template](https://github.com/fran-eliot/github-framework/blob/main/framework/adoption/assessment-template.md)
- [Backend Adoption Discovery — 23](https://github.com/fran-eliot/github-framework/blob/main/docs/discovery/23_BACKEND_ADOPTION_DISCOVERY.md)
- [Adoption Model Discovery — 24](https://github.com/fran-eliot/github-framework/blob/main/docs/discovery/24_ADOPTION_MODEL_DISCOVERY.md)
- [Roadmap](https://github.com/fran-eliot/github-framework/blob/main/ROADMAP.md)

### Consumer

- [SeniorMeet, commit de referencia](https://github.com/fran-eliot/seniormeet/tree/b84b0de246d459caf594a5cdacbe8fccfa68698a)
- [`README.md`](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/README.md)
- [`pom.xml`](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/pom.xml)
- [`Dockerfile`](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/Dockerfile)
- [`docker-compose.yml`](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/docker-compose.yml)

---

## 11. Conclusión provisional

UX-01 muestra que existe una experiencia documental que permite encontrar Adoption y comenzar a preparar Evidence, pero también posibles fricciones entre el `Getting Started`, la elección del Template y el primer resultado útil. La separación semántica del Assessment constituye una fortaleza que debe preservarse.

El modelo no se declara conforme ni no conforme en su totalidad; tampoco se propone una implementación.

**Resultado:** evidencia preliminar apta para continuar Discovery; **no** Delivery Scope ni compromiso de implementación.
