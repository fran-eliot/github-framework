# Only Film — Provisional Semantic Review: Architecture and Project Status

## 1. Contexto

Este lote prepara la evaluación semántica E3 de las dos Responsibilities `Recommended` que faltaban en `TPL-BACKEND` 0.1.0. Se basa en fuentes documentales versionadas de Only Film y en los contratos de Component del Framework. **No representa una evaluación aprobada por una persona ni una decisión de adopción.**

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Collection Scope | `DOC-ARCHITECTURE`, `DOC-PROJECT-STATUS` |
| Assessment Status | `In Progress` |
| Review Status | `Proposal — pending human review` |
| Reviewer / Approval | Sin asignar / sin aprobar |
| Consumer Mutation | `NONE` |

El análisis evalúa **responsabilidades documentales**, no la calidad absoluta de la arquitectura ni la conveniencia de cada prioridad de negocio. Las auditorías previas tienen referencias temporales distintas de la referencia fijada para el Assessment.

## 2. Resumen de propuestas

| Responsibility | Requirement Level | Proposed State | Proposed Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `DOC-ARCHITECTURE` | `Recommended` | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `DOC-PROJECT-STATUS` | `Recommended` | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |

La hipótesis `Partial` identifica una **incertidumbre de suficiencia o vigencia**; no equivale a defecto demostrado. Una revisión humana podrá confirmar `Satisfied`, `Partial` o `Missing`, según el contexto y la evidencia final.

## 3. Responsibility — DOC-ARCHITECTURE

**Requirement Level:** `Recommended`.

**Proposed State:** `Partial` — sin aprobación.

**Proposed Applicability:** `Applicable` — sin aprobación.

**Implementation Characteristics (proposed):** `Own`, `Specialized`, `Distributed`: resumen MVC/JPA en README y auditoría de arquitectura/mantenibilidad en `docs/`, basada en un estado histórico.

### Detected Facts

- El [Component DOC-ARCHITECTURE](../../components/documentation/architecture/README.md) exige comunicar **arquitectura vigente**, propósito, contexto, principales componentes, relaciones y restricciones; no exige un diagrama por formalismo ni una reproducción de clases.
- El [README fijado](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) presenta el flujo nominal `Controlador MVC → servicio / reglas de negocio → repositorio JPA → base de datos` y entidades de dominio `Movie`, `Room`, `Session`, `Ticket`, `Review` y `User`.
- La [auditoría de arquitectura y mantenibilidad](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md), fechada **2026-10-10**, declara como referencia `main` después de PR #23 (`b6cf52c9`). Identifica casos de uso que en ese momento accedían directamente a repositorios y propone mejoras incrementales de DTOs, servicio transaccional y política de errores.
- La [auditoría funcional posterior](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md), basada en `df63353564485eb6d2d60c982032e5d3c4facbf2`, documenta que determinados hallazgos anteriores ya no debían reabrirse automáticamente; por ejemplo, el formulario administrativo de tickets, las invariantes de sesiones y una restricción de unicidad de butacas.
- El conjunto de documentos permite reconocer la arquitectura nominal y su evolución, pero **no se ha consolidado ni comprobado una representación arquitectónica completa para el SHA evaluado**. El README resume; la auditoría histórica se centra en riesgos, no en describir sistemáticamente todos los componentes vigentes.

### Evidence

- [Component DOC-ARCHITECTURE](../../components/documentation/architecture/README.md)
- [README — Tecnologías y arquitectura](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Auditoría de arquitectura — base histórica](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md)
- [Auditoría funcional F3 — base posterior distinta](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md)
- [Exploración documental original](only-film-recommended-documentation-batch.md)
- [Propuesta E3 de README-ARCHITECTURE](only-film-recommended-readme-semantic-review.md)

### Evaluation Rationale — propuesta

La Responsibility no está necesariamente ausente: el README comunica capas y un flujo, y la auditoría complementa con riesgos y límites. El Component, sin embargo, enfatiza una **descripción mantenible del estado arquitectónico actual**. Una auditoría de defectos históricos y un esquema de flujo nominal no garantizan por sí solos esa visión. Se propone `Partial` como punto de discusión, sin extrapolar la persistencia de antiguos defectos al commit fijado y sin imponer una arquitectura distinta.

### Uncertainty

- ¿Qué componentes, límites, relaciones y flujos están realmente vigentes en el SHA, incluidos los accesos directos a repositorios cuando existan?
- ¿Las fuentes existentes bastan para que un colaborador entienda la arquitectura sin leer todo el código?
- ¿Deben documentarse restricciones y decisiones técnicas estables en una fuente más consolidada o bastan README + documentos especializados?
- ¿Qué hallazgos de la auditoría de 2026-10-10 están ya corregidos, y qué prueba lo acredita para el commit elegido?
- ¿Qué nivel de abstracción requiere este proyecto, evitando forzar diagramas y ADR innecesarios?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** no hay aprobación sobre suficiencia arquitectónica ni razón firme para `PRESERVE`, `ADAPT` o `ADD`. No se modifica el consumer.

## 4. Responsibility — DOC-PROJECT-STATUS

**Requirement Level:** `Recommended`.

**Proposed State:** `Partial` — sin aprobación.

**Proposed Applicability:** `Applicable` — sin aprobación, por la evolución iterativa observable del repositorio.

**Implementation Characteristics (proposed):** `Own`, `Specialized`, `Distributed`: informe de madurez, roadmap funcional y próximos pasos del README; no se identifica un snapshot operativo único que abarque todos los bloques del Component.

### Detected Facts

- El [Component DOC-PROJECT-STATUS](../../components/documentation/project-status/README.md) solicita estado general, avance por áreas, próximo hito y objetivos inmediatos; distingue un estado operativo de un backlog, roadmap o changelog y exige mantenerlo actualizado cuando cambie significativamente el proyecto.
- La [evaluación de madurez técnica](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md), fechada **2026-10-10**, declara como referencia el commit `9f2a31e927df105d14e3d30d4d8277fa61883deb`. Describe en aquella base un proyecto académico evolucionado de portfolio, no listo para publicación en producción, e identifica prioridades de integridad de negocio, CI, E2E y operaciones.
- El documento reconoce expresamente que **no** era una nueva medición de cobertura, pentest ni análisis SonarCloud reciente. Esa limitación corresponde a su fecha y no debe trasladarse sin matices al SHA evaluado.
- La [auditoría funcional F3](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) se apoya en el commit `df63353564485eb6d2d60c982032e5d3c4facbf2`; presenta una hoja de ruta F3.002–F3.008 y la intención inicial de abordar el descubrimiento del dashboard. **Su lista de iniciativas no prueba que todas sigan pendientes ni que hayan sido completadas para el SHA fijado.**
- El [README del SHA](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) presenta `Próximas líneas de evolución`, menciona API REST, integración de pago real, observabilidad y automatización de despliegue como **posibles** mejoras, no como funcionalidades terminadas.
- La evidencia de [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) demuestra tres checks satisfactorios del commit evaluado, incluido un job H2 con 329 tests sin fallos. **No equivale a una fotografía global de prioridades, riesgos y hitos del proyecto.**

### Evidence

- [Component DOC-PROJECT-STATUS](../../components/documentation/project-status/README.md)
- [Evaluación de madurez histórica](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md)
- [Auditoría funcional / roadmap F3](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md)
- [README — próximas líneas de evolución](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Run CI fijado](https://github.com/fran-eliot/only_film/actions/runs/39283862407)
- [Exploración documental original](only-film-recommended-documentation-batch.md)

### Evaluation Rationale — propuesta

El informe de madurez, el roadmap y el README permiten reconstruir parte del contexto y de los objetivos; su existencia evita concluir `Missing` por no disponer de un archivo `PROJECT_STATUS.md`. Sin embargo, el Component exige una **fotografía operativa mantenida**, con estado por áreas, hito siguiente y objetivos inmediatos. Dadas las referencias distintas y las mejoras ocurridas entre auditorías, no se ha demostrado que esos documentos constituyan una fuente suficientemente actualizada para el SHA evaluado. `Partial` es una propuesta conservadora, no un mandato de crear otro documento si bastara con actualizar y enlazar la información existente.

### Uncertainty

- ¿Qué iniciativas F3 se han completado, siguen abiertas o han cambiado de alcance en el SHA evaluado?
- ¿Qué documento o mecanismo comunica de forma mantenible el estado operativo actual y el próximo hito, diferenciándolo del roadmap?
- ¿Basta la combinación de documentos existentes para el público objetivo o convendría una actualización/consolidación de estado?
- ¿Qué riesgos históricos aún aplican y cuáles se resolvieron antes del commit fijado?
- ¿Qué nivel de frecuencia de actualización resulta apropiado para un repositorio portfolio en evolución?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** hace falta validar la vigencia y utilidad de la visión operativa antes de seleccionar `PRESERVE`, `ADAPT` o `ADD`.

## 5. Gates de revisión humana

| Gate | Criterio | Estado |
| --- | --- | --- |
| RDA-1 | Confirmar alcance y aplicabilidad real de ambas Responsibilities de documentación | Pendiente |
| RDA-2 | Comparar las descripciones arquitectónicas con código del SHA cuando se necesite | Pendiente |
| RDA-3 | Separar riesgos históricos de decisiones, límites y relaciones arquitectónicas vigentes | Evidencia histórica disponible; revisión pendiente |
| RDA-4 | Reconstruir estado por áreas, último hito y siguientes objetivos a partir de fuentes fechadas y verificables | Pendiente |
| RDA-5 | Evitar confundir roadmap F3 con resultados implementados en el commit evaluado | Criterio documentado; revisión pendiente |
| RDA-6 | Aprobar o corregir `State`, `Applicability`, características, incertidumbre y rationale por Responsibility | Pendiente |
| RDA-7 | Resolver o mantener pendiente cada Adoption Decision con justificación explícita | Pendiente |

## 6. Cobertura semántica propuesta: siete Recommended

| Responsibility Recommended | Propuesta E3 | ¿Aprobada? |
| --- | --- | --- |
| `README-STATUS` | [Status, Architecture, Repository Structure](only-film-recommended-readme-semantic-review.md) | No |
| `README-ARCHITECTURE` | [Status, Architecture, Repository Structure](only-film-recommended-readme-semantic-review.md) | No |
| `README-REPOSITORY-STRUCTURE` | [Status, Architecture, Repository Structure](only-film-recommended-readme-semantic-review.md) | No |
| `README-TESTING` | [Testing](only-film-testing-semantic-review.md) | No |
| `DOC-ARCHITECTURE` | Este documento | No |
| `DOC-PROJECT-STATUS` | Este documento | No |
| `DOC-TESTING` | [Testing](only-film-testing-semantic-review.md) | No |

Las siete Responsibilities `Recommended` tienen ahora **propuestas semánticas E3 documentadas**, no evaluaciones aprobadas. La cobertura documental global es **28/28**, sin que ello implique cumplimiento, decisiones resueltas ni finalización del Assessment.

## 7. Conclusión

El lote registra contexto, fuentes con referencias históricas separadas, interpretaciones propuestas e incertidumbres específicas. Mantiene `Decision Status: Needs Further Evaluation` y `Adoption Decision: —` para ambas Responsibilities.

**Assessment Status: In Progress.** No se ha modificado Only Film, ejecutado nuevos tests ni certificado la arquitectura o el estado operativo.
