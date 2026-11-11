# 54 — First-Time Usability Validation Protocol

| Campo | Valor |
|---|---|
| Proyecto | GitHub Framework |
| Fecha de preparación | 2026-11-11 |
| Estado | Prepared — Not Executed |
| Experimento | UX-02 — First-Time Usability Validation |
| Referencia del Framework | `main` después de PR #90; fijar commit SHA al ejecutar |
| Discovery precedente | [53_FIRST_TIME_USER_EXPERIENCE_DISCOVERY.md](53_FIRST_TIME_USER_EXPERIENCE_DISCOVERY.md) |
| Consumer propuesto | [fran-eliot/seniormeet](https://github.com/fran-eliot/seniormeet) |
| Consumer reference | `b84b0de246d459caf594a5cdacbe8fccfa68698a` |
| Baseline de Template | `TPL-BACKEND v0.1.0` (`Experimental`, `L2`) |

> Este documento define un **protocolo de investigación**, no resultados de una prueba con participantes. No compromete Delivery Scope, Sprint, milestone, versión ni modificación del consumer.

---

## 1. Contexto y evidencia previa

UX-01 identificó una ruta de entrada poco explícita entre el README, la biblioteca de Repository Templates y el Assessment Template. También confirmó que los Templates y su metadata canónica existen.

La PR #90 incorporó enlaces y orientación en ambos README públicos y en la Adoption Guide. UX-02 pretende **comprobar el recorrido después de ese cambio** sin dar por supuesto que la fricción ha desaparecido para personas nuevas.

Referencias principales:

- [README (EN)](../../README.md) y [README (ES)](../../README_es.md)
- [Repository Template Library](../../framework/templates/repositories/README.md)
- [Existing Repository Adoption Guide](../../framework/adoption/README.md)
- [Assessment Template](../../framework/adoption/assessment-template.md)
- [TPL-BACKEND README](../../framework/templates/repositories/backend/README.md)
- [TPL-BACKEND metadata](../../framework/templates/repositories/backend/metadata.yml)
- [UX-01 Discovery](53_FIRST_TIME_USER_EXPERIENCE_DISCOVERY.md)

## 2. Preguntas de investigación

**RQ-01 — Descubrimiento.** ¿Distingue una persona nueva entre crear un repositorio y evaluar uno existente?

**RQ-02 — Navegación.** ¿Localiza, sin pistas del facilitador, la biblioteca de Templates y el camino hacia Existing Repository Adoption?

**RQ-03 — Selección.** ¿Elige un Repository Template justificadamente y obtiene su versión desde la metadata canónica?

**RQ-04 — Preparación.** ¿Puede iniciar correctamente el Assessment Context con una referencia reproducible del consumer?

**RQ-05 — Comprensión.** ¿Distingue Detected Facts, Evidence, Evaluated State y Adoption Decision?

**RQ-06 — Esfuerzo.** ¿Qué dudas, retrocesos o ayudas aparecen realmente durante el recorrido?

## 3. Diseño y límites

### 3.1 Método

Prueba observacional moderada, individual, con tareas basadas en un caso práctico. El participante navega por GitHub y explica qué está intentando hacer; el facilitador observa sin enseñarle rutas, respuestas o nombres de los archivos antes de completar las tareas.

**Muestra exploratoria propuesta:** 2–3 desarrolladores con experiencia general en repositorios GitHub pero sin participación previa en GitHub Framework. Una persona aporta evidencia cualitativa; esta muestra pequeña no permite estimar tasas poblacionales ni demostrar ausencia de problemas.

Si no se dispone de participantes externos, el experimento permanece **Not Executed**. Una simulación del autor, una inspección documental o una sesión asistida no se registrará como resultado de usuario independiente.

### 3.2 Preparación

- Fijar commit SHA de `github-framework/main` al comenzar cada sesión para impedir que cambios posteriores alteren el recorrido.
- Utilizar la misma versión pública de README y Adoption Guide para todos los participantes de una misma ronda.
- Dar al participante el enlace raíz `https://github.com/fran-eliot/github-framework` y la URL del consumer; **no** proporcionar la ruta al Template, su ID, versión ni el Assessment Template.
- Mantener `seniormeet` como consumer read-only y fijar su commit `b84b0de246d459caf594a5cdacbe8fccfa68698a`.
- Evitar acceso de escritura al consumer; si se necesita registrar el contexto, hacerlo en una copia temporal privada o una hoja de notas de la sesión, no mediante commits.
- Antes de participar, solicitar consentimiento para notas y, solo si se desea grabar, consentimiento adicional. No incluir nombres, datos personales o grabaciones en el repositorio público.

### 3.3 Exclusiones

No evaluar las 28 Responsibilities, ni realizar Application o Integration, ni ejecutar el Framework Validator como sustituto del Assessment. No medir calidad general del consumer. No modificar código, dependencias, README o configuración de SeniorMeet.

## 4. Guion del facilitador

### Contexto presentado al participante

> Quieres utilizar GitHub Framework para entender cómo mejorar un repositorio backend que ya existe, sin modificarlo todavía. El repositorio que vas a examinar es SeniorMeet. Partes de la página principal de GitHub Framework. Utiliza únicamente la documentación pública para identificar el punto de partida y preparar el contexto de una evaluación inicial.

No mencionar de antemano `TPL-BACKEND`, `metadata.yml` ni las rutas que se pretende que descubra.

### Tareas

| ID | Tarea para el participante | Evidencia de éxito |
|---|---|---|
| T1 | Identifica el recorrido adecuado para un repositorio ya existente. | Distingue Adoption de un recorrido para repositorios nuevos. |
| T2 | Encuentra las opciones de Repository Templates y elige una para SeniorMeet. | Localiza Library y justifica el tipo backend a partir de criterios del Template. |
| T3 | Indica el ID y la versión del Template seleccionado y muestra su fuente. | Consulta metadata canónica; no infiere versión desde la release global del Framework. |
| T4 | Encuentra el artefacto para registrar el assessment y describe los datos iniciales. | Localiza Assessment Template e identifica sus campos contextuales. |
| T5 | Registra, en notas de sesión, el consumer y una referencia reproducible. | Usa repo y commit SHA sin alterar el consumer. |
| T6 | Formula dos observaciones verificables del consumer sin decidir qué cambios harías. | Separa hechos/evidencia de State, Applicability y Adoption Decision. |

Las tareas pueden finalizar como completadas, completadas con ayuda, no completadas o no aplicables por un bloqueo anterior. Evitar introducir respuestas dentro de las instrucciones.

### Intervención del facilitador

- Permitir preguntas de aclaración del objetivo, sin indicar rutas.
- Ante un bloqueo, registrar primero la dificultad y la ayuda solicitada.
- Si es imprescindible dar una pista, indicar el momento y el contenido exactos de la ayuda; continuar marcando el resto de la sesión como **assisted**.
- No corregir silenciosamente las respuestas; preguntar en qué fuente se fundamentan.
- Al final, preguntar qué paso fue más confuso y qué documentación faltó, sin sugerir soluciones concretas.

## 5. Matriz de captura de evidencias

Repetir para cada sesión sin publicar información identificativa:

| Campo | Valor de sesión |
|---|---|
| Código de participante | `P01` / `P02` / `P03` |
| Fecha / idioma | Pendiente |
| Framework commit SHA | Pendiente |
| Experiencia GitHub | Descripción general no identificativa |
| Experiencia previa con Framework | Debe ser ninguna |
| Consentimiento para notas | Pendiente |
| ¿Se grabó? | No por defecto |
| Resultado global | Pendiente |

| Tarea | Estado (sin ayuda / con ayuda / bloqueo / N/A) | Ruta y evidencia observada | Duda / retroceso | Ayuda exacta | Comentarios |
|---|---|---|---|---|---|
| T1 | Pendiente | — | — | — | — |
| T2 | Pendiente | — | — | — | — |
| T3 | Pendiente | — | — | — | — |
| T4 | Pendiente | — | — | — | — |
| T5 | Pendiente | — | — | — | — |
| T6 | Pendiente | — | — | — | — |

Registrar citas breves solo cuando hayan sido realmente pronunciadas; nunca inventar testimonios, tiempos o participantes. El número de clics o minutos puede anotarse si se observa, pero no debe inferirse ni convertirse en umbral de éxito universal.

## 6. Criterios de interpretación

### 6.1 Clasificación de observaciones

- **Navigation:** no encuentra un recurso o elige una ruta errónea.
- **Terminology:** confunde conceptos o límites del Framework.
- **Task support:** entiende el objetivo pero no sabe qué hacer a continuación.
- **Artifact comprehension:** localiza un archivo pero interpreta incorrectamente su función.
- **No issue observed:** tarea completada sin dificultad observable; no equivale a garantía de usabilidad.

Cada observación debe incluir tarea, evidencia, contexto, intervención y grado de incertidumbre.

### 6.2 Separación de resultados

```text
Observed behavior
    ≠
Interpretation
    ≠
Validated need
    ≠
Selected solution
    ≠
Committed delivery
```

Una dificultad individual puede justificar investigación adicional. Su recurrencia en varias sesiones refuerza la hipótesis, pero no convierte automáticamente un cambio de documentación o código en requisito aprobado.

### 6.3 Comparación con UX-01

Contrastar principalmente UX-F01, UX-F02, UX-F03, UX-F05 y UX-F10. UX-F08 fue resuelto cuando se verificó la definición canónica del Template; no reabrirlo salvo evidencia nueva. La PR #90 resuelve el **enlace documental** observado, no demuestra por sí sola comprensión independiente del usuario.

## 7. Plantilla para síntesis posterior (vacía)

**Estado de ejecución:** `Not Executed`

**Sesiones realizadas:** `0`

**Evidencia disponible:** protocolo y hallazgos históricos UX-01; no hay observaciones de usuarios nuevos.

| Pregunta | Resultado | Evidencia | Confianza |
|---|---|---|---|
| RQ-01 | Pendiente | — | — |
| RQ-02 | Pendiente | — | — |
| RQ-03 | Pendiente | — | — |
| RQ-04 | Pendiente | — | — |
| RQ-05 | Pendiente | — | — |
| RQ-06 | Pendiente | — | — |

**Hallazgos nuevos:** pendiente.

**Necesidades validadas / no validadas / inciertas:** pendiente.

**Decisión posterior:** pendiente; no escoger soluciones antes de observar resultados.

## 8. Cierre y siguiente decisión

Este protocolo habilita una prueba pequeña y reproducible sin ampliar el alcance técnico de GitHub Framework. La ejecución exige contar realmente con participantes y conservar evidencias; el documento por sí solo **no valida la experiencia de usuario**.

En ausencia de participantes, se puede realizar por separado una revisión documental interna, etiquetada como tal, pero no presentar esa revisión como ejecución de UX-02.

No se abre Sprint, milestone, release ni Delivery Scope como consecuencia de este protocolo.
