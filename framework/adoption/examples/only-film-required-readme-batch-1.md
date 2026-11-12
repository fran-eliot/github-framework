# Only Film — Assessment Batch 1: Hero, Overview y Features

## 1. Contexto

Este documento amplía el recorrido de Existing Repository Adoption de Only Film con un primer lote de tres Responsibilities `Required` de `TPL-BACKEND` `0.1.0`. La inspección es documental, read-only y limitada al README del consumer fijado al commit `28d75a50e0a178954dd46acc23300d9dd327843c`.

| Campo | Valor |
| --- | --- |
| Consumer Repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Responsibilities | `README-HERO`, `README-OVERVIEW`, `README-FEATURES` |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |

Se utilizan las descripciones de los Components [Hero](../../components/readme/hero/README.md), [Overview](../../components/readme/overview/README.md) y [Features](../../components/readme/features/README.md). Este lote no altera el [walkthrough anterior de Quick Start y Testing](only-film-two-responsibilities.md).

## 2. Resumen provisional

| Responsibility | Requirement Level | Cobertura | State | Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- | --- |
| `README-HERO` | `Required` | Explored — provisional | Pendiente de revisión | Pendiente de revisión | `Needs Further Evaluation` | `—` |
| `README-OVERVIEW` | `Required` | Explored — provisional | Pendiente de revisión | Pendiente de revisión | `Needs Further Evaluation` | `—` |
| `README-FEATURES` | `Required` | Explored — provisional | Pendiente de revisión | Pendiente de revisión | `Needs Further Evaluation` | `—` |

**Distinción:** `Explored — provisional` es un indicador interno de cobertura de inspección; **no** es un `State` válido del Assessment Template. Los campos semánticos que no se han revisado por una persona responsable permanecen pendientes, sin forzar `Satisfied`, `Partial`, `Missing` o `Not Applicable`.

## 3. README-HERO

**Requirement Level:** `Required`.

**Detected Facts:**

- El README comienza con el H1 `# 🎬 Only Film`.
- Bajo el título hay una descripción breve de la aplicación y su stack (Java, Spring Boot, Spring MVC, Spring Security y Thymeleaf).
- Incluye otra frase que identifica el origen académico colaborativo y la evolución del proyecto.
- Se muestran cinco badges de Java 25, Spring Boot 4.0.5, PostgreSQL 17, Flyway y Docker Compose.

**Evidence:** [README.md, cabecera y badges en el commit fijado](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md).

**Evaluation Rationale (pendiente):** La cabecera ofrece elementos observables relacionados con el propósito de Hero (identidad, descripción y badges), pero su adecuación a las reglas editoriales y de composición del Framework no se ha revisado formalmente. No se ha verificado presentación visual en dispositivos o temas.

**Uncertainty:** ¿Es suficiente la distinción entre tagline y descripción para este consumer? ¿Se conserva una única cabecera principal y una composición legible en todas las condiciones previstas?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

## 4. README-OVERVIEW

**Requirement Level:** `Required`.

**Detected Facts:**

- El primer párrafo presenta Only Film como aplicación web de gestión cinematográfica.
- Describe actividades principales del producto: cartelera, proyecciones, butacas, entradas y administración con permisos por rol.
- El segundo párrafo explica su origen como proyecto académico colaborativo y líneas posteriores de evolución.
- No se observa un encabezado literal `## Overview` al principio del README; la explicación está integrada en la introducción.

**Evidence:** [README.md, introducción en el commit fijado](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md).

**Evaluation Rationale (pendiente):** El README contiene contenido descriptivo compatible con el propósito de Overview. Una etiqueta de sección diferente o ausente no equivale automáticamente a falta de Responsibility; se necesita evaluar la claridad y suficiencia del contenido.

**Uncertainty:** ¿La introducción comunica suficientemente el propósito y problema que resuelve al público previsto? ¿La distribución actual entre cabecera y explicación evita duplicación innecesaria?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

## 5. README-FEATURES

**Requirement Level:** `Required`.

**Detected Facts:**

- El README contiene el apartado `## Funcionalidades`.
- Las funcionalidades están agrupadas por rol: visitantes, usuarios y administradores.
- Se enumeran acciones de cartelera, registro e inicio de sesión, entradas, reseñas y administración.
- Un párrafo adicional explica protección de concurrencia en la compra de entradas y controles de acceso.

**Evidence:** [README.md, sección Funcionalidades en el commit fijado](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md).

**Evaluation Rationale (pendiente):** Hay una enumeración explícita de capacidades, acorde con el objetivo documental de Features. El alcance de cada función y su correspondencia con el comportamiento real de la aplicación no se han probado en este Assessment.

**Uncertainty:** ¿Todas las capacidades descritas corresponden al comportamiento verificable del commit? ¿La sección diferencia suficientemente funcionalidades públicas, restricciones y detalles de implementación?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Revisión semántica posterior:** la [propuesta E3 de Hero, Overview y Features](only-film-required-identity-semantic-review.md) incorpora States y Applicability provisionales, justificaciones por Responsibility y gates de revisión. Esta exploración original permanece como evidencia histórica y no acredita aprobación humana.

## 6. Resultado del lote y próximos pasos

| Check | Resultado |
| --- | --- |
| Tres Responsibilities del contrato identificadas | Completado |
| Detected Facts separados de interpretación | Completado |
| Evidence enlazada al commit inmutable | Completado |
| Incertidumbres y necesidad de revisión explícitas | Completado |
| Conformidad semántica confirmada por reviewer | Pendiente |
| Verificación funcional de las capacidades mencionadas | No realizada |
| Adoption Decisions resueltas | Ninguna |

En la [matriz de cobertura de Only Film](only-film-assessment-coverage.md), este lote amplía la exploración documental de 2/28 a **5/28** Responsibilities. Siguen **23/28 sin explorar**. Dentro de las ocho `Required`, existen ahora cuatro exploradas (incluida `README-QUICK-START`) y cuatro pendientes.

No se ejecutaron builds, tests ni despliegues; no se editó el repositorio consumidor. El Assessment global se mantiene `In Progress` y este documento no autoriza Application ni Integration.
