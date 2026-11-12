# Only Film — Consolidated Assessment Human Review Matrix

## 1. Contexto, finalidad y distinciones

Esta matriz **consolida** las 28 propuestas E3 existentes para `TPL-BACKEND` 0.1.0 en un punto único de revisión. Se ha obtenido de las fichas previas **sin elevar hipótesis a Estados evaluados ni registrar aprobación humana**. Facilita seleccionar qué evidencia falta, quién debe valorar cada caso y qué resultado registrar después en un [Assessment Template](../assessment-template.md) conforme a su contrato.

| Field | Value |
| --- | --- |
| Consumer Repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Proposals consolidated | `28/28` — **not approved** |
| Human-reviewed States and Applicability | **0 approved in these records** |
| Resolved Adoption Decisions | `0` |
| Assessment Status | `In Progress` |
| Consumer Mutation | `NONE` |

**Leyenda:**

- `Proposed State` y `Proposed Applicability` son **hipótesis para el reviewer** y no campos de un Assessment aprobado. Donde aparece `Missing / Partial` son alternativas no discriminadas, **no** un valor contractual `State`. `Uncertain` para Applicability representa correctamente una incertidumbre aún abierta, no una resolución de Not Applicable.
- `P1/P2/P3` son prioridades **de revisión de evidencia**, no severidades de seguridad, defectos confirmados ni tareas que obliguen a modificar Only Film.
- `E3` enlaza la ficha detallada que contiene Detected Facts, Evidence, Evaluation Rationale, Uncertainty y Decision Status. Las propuestas originales mantienen `Needs Further Evaluation` y `Adoption Decision: —`.
- El orden de filas y Requirement Levels procede de la [metadata canónica del Template](../../templates/repositories/backend/metadata.yml), no de los niveles de prioridad de los Components.

## 2. Matriz única de propuestas y próximo gate

| Responsibility | Level | Proposed State | Proposed Applicability | Prioridad | Ficha de evidencia | Gate de revisión concreto |
| --- | --- | --- | --- | --- | --- | --- |
| `README-HERO` | Required | `Partial` | `Applicable` | **P3** | [E3](only-film-required-identity-semantic-review.md) | Contrastar encabezado, badges y legibilidad; decidir suficiencia de identidad. |
| `README-OVERVIEW` | Required | `Partial` | `Applicable` | **P3** | [E3](only-film-required-identity-semantic-review.md) | Evaluar claridad del propósito y diferenciación frente a Hero. |
| `README-FEATURES` | Required | `Partial` | `Applicable` | **P2** | [E3](only-film-required-identity-semantic-review.md) | Validar afirmaciones de capacidades y separar detalles de implementación. |
| `README-TECH-STACK` | Required | `Partial` | `Applicable` | **P3** | [E3](only-film-required-final-semantic-review.md) | Contrastar tecnologías clave y contextos de uso con POM/Compose. |
| `README-QUICK-START` | Required | `Partial` | `Applicable` | **P1** | [E3](only-film-required-semantic-review.md) | Reproducir Compose desde clon limpio o justificar umbral documental; gates Q1–Q8. |
| `README-DOCUMENTATION` | Required | `Partial` | `Applicable` | **P2** | [E3](only-film-required-final-semantic-review.md) | Comprobar enlaces principales y localización de documentación útil. |
| `README-FOOTER` | Required | `Partial` | `Applicable` | **P2** | [E3](only-film-required-final-semantic-review.md) | Valorar créditos y nota de licencia sin atribuir permisos jurídicos. |
| `DOC-CHANGELOG` | Required | `Missing / Partial` | `Applicable` | **P1** | [E3](only-film-required-semantic-review.md) | Verificar tags, releases y fuentes equivalentes; seleccionar State conforme a evidencia. |
| `README-STATUS` | Recommended | `Partial` | `Applicable` | **P2** | [E3](only-film-recommended-readme-semantic-review.md) | Definir estado/madurez del repositorio en el SHA, no confundir badges de tecnología. |
| `README-ARCHITECTURE` | Recommended | `Partial` | `Applicable` | **P2** | [E3](only-film-recommended-readme-semantic-review.md) | Reconciliar resumen MVC/JPA con código y auditoría histórica. |
| `README-REPOSITORY-STRUCTURE` | Recommended | `Partial` | `Applicable` | **P3** | [E3](only-film-recommended-readme-semantic-review.md) | Verificar árbol, facilidad de navegación y precisión del resumen. |
| `README-TESTING` | Recommended | `Partial` | `Applicable` | **P1** | [E3](only-film-testing-semantic-review.md) | Contrastar comandos locales y CI; delimitar H2, PostgreSQL, Selenium y JaCoCo. |
| `DOC-ARCHITECTURE` | Recommended | `Partial` | `Applicable` | **P2** | [E3](only-film-recommended-docs-semantic-review.md) | Identificar estructura vigente; no trasladar defectos de auditorías históricas. |
| `DOC-PROJECT-STATUS` | Recommended | `Partial` | `Applicable` | **P2** | [E3](only-film-recommended-docs-semantic-review.md) | Reconstruir hitos y estado por áreas con referencias fechadas. |
| `DOC-TESTING` | Recommended | `Partial` | `Applicable` | **P1** | [E3](only-film-testing-semantic-review.md) | Evaluar suficiencia de guías, CI Surefire y límites de cobertura y Sonar. |
| `README-ROADMAP` | Optional | `Partial` | `Applicable` | **P3** | [E3](only-film-optional-governance-semantic-review.md) | Verificar vigencia de propuestas F3; valorar si resumen es suficiente. |
| `README-CONTRIBUTING` | Optional | `Missing / Partial` | `Uncertain` | **P2** | [E3](only-film-optional-governance-semantic-review.md) | Determinar política de colaboración y fuentes; decidir Applicability y State. |
| `README-DEMO` | Optional | `Partial` | `Applicable` | **P3** | [E3](only-film-optional-showcase-semantic-review.md) | Comprobar representatividad de capturas y necesidad de demo reproducible. |
| `README-AUTHOR` | Optional | `Partial` | `Applicable` | **P2** | [E3](only-film-optional-governance-semantic-review.md) | Revisar atribución del equipo y evolución posterior sin inferir titularidad. |
| `README-HIGHLIGHTS` | Optional | `Partial` | `Applicable` | **P3** | [E3](only-film-optional-showcase-semantic-review.md) | Valorar valor editorial y evidencia de destacados sin duplicar Features. |
| `README-LICENSE` | Optional | `Partial` | `Applicable` | **P1** | [E3](only-film-optional-governance-semantic-review.md) | Aclarar información de derechos/uso con fuentes apropiadas, sin conceder licencia. |
| `DOC-ADR` | Optional | `Partial` | `Applicable` | **P3** | [E3](only-film-optional-final-semantic-review.md) | Valorar decisiones documentadas y utilidad de registro ADR frente a redundancia. |
| `DOC-API` | Optional | `Missing / Partial` | `Uncertain` | **P2** | [E3](only-film-optional-final-semantic-review.md) | Verificar si hay contrato API pública; no confundir MVC con REST. |
| `DOC-DATABASE` | Optional | `Partial` | `Applicable` | **P2** | [E3](only-film-optional-final-semantic-review.md) | Valorar modelo de datos, invariantes y migraciones contra fuentes del SHA. |
| `DOC-DEPLOYMENT` | Optional | `Partial` | `Applicable` | **P2** | [E3](only-film-optional-final-semantic-review.md) | Delimitar uso local; aclarar advertencia de uploads y evidencia Compose. |
| `DOC-SECURITY` | Optional | `Partial` | `Applicable` | **P1** | [E3](only-film-security-semantic-review.md) | Contrastar guía vigente y controles; no generalizar 329 tests a seguridad total. |
| `DOC-DIAGRAMS` | Optional | `Missing / Partial` | `Uncertain` | **P3** | [E3](only-film-optional-showcase-semantic-review.md) | Buscar diagramas embebidos y valorar aplicabilidad antes de recomendar crearlos. |
| `DOC-REFERENCES` | Optional | `Partial` | `Uncertain` | **P3** | [E3](only-film-optional-final-semantic-review.md) | Decidir si referencias dispersas bastan o si índice añade valor. |

**Resumen de hipótesis**, que no deben copiarse como recuentos de Estados evaluados:

| Aspecto | Conteo |
| --- | ---: |
| Propuestas E3 referenciadas | **28/28** |
| State `Partial` como hipótesis única | **24** |
| State alternativo `Missing / Partial` sin discriminar | **4** |
| Applicability `Applicable` como hipótesis | **24** |
| Applicability pendiente / `Uncertain` | **4** |
| States formalmente aprobados | **0 acreditados** |
| Adoption Decisions resueltas | **0 acreditadas** |

`0` aprobados se refiere al **registro de este Assessment**, no a la inexistencia de revisiones externas no incorporadas aquí.

## 3. Hallazgos consolidados de calidad de evidencia

### E0/E1 — Inventario y exploración documental

- Las **28/28 Responsibilities** del Template están enumeradas y cuentan con fuentes inspeccionadas o identificadas con límites explícitos. Esto **no** equivale a conformidad.
- Para el mismo SHA del consumer hay un [run de GitHub Actions](https://github.com/fran-eliot/only_film/actions/runs/39283862407) con tres checks `success`. El log de `h2-regression` acredita **329 tests, 0 failures, 0 errors, 0 skipped**, y resultados individuales de clases relevantes de seguridad. La generación y publicación histórica de JaCoCo y un `ANALYSIS SUCCESSFUL` del scanner Sonar están registradas, **pero no** el porcentaje de cobertura ni la aprobación del Quality Gate. [Evidencia E2](only-film-verified-surefire-sonar-logs.md).
- El `postgres-schema` comprueba arranque de JAR + PostgreSQL del workflow; **no verifica el flujo Docker Compose del README**. No se identificó un check `compose-smoke` directamente asociado al commit en los resultados consultados. [Evidencia Quick Start](only-film-compose-evidence-gap.md).
- Las auditorías de arquitectura, seguridad, madurez y roadmap tienen **commits base distintos**: sus hallazgos no son automáticamente vigentes en el SHA evaluado.
- El [reconocimiento de cambios/release](only-film-changelog-evidence-review.md) no encontró una fuente inequívoca de changelog de versiones publicadas; los tags siguen **sin verificar**.
- El [aviso de licencia del README](only-film-optional-governance-semantic-review.md) no establece permisos de reutilización ni sustituye la determinación de derechos del trabajo académico.
- Algunas Responsibilities de `TPL-BACKEND` carecen de Component autónomo localizado en el catálogo inspeccionado. La discrepancia es un **asunto de definición del Framework** y no un incumplimiento automático del consumer.

### E2/E3 — Dónde está el trabajo pendiente

1. **P1 — Gates materiales:** `README-QUICK-START` (reproducibilidad Compose), `DOC-CHANGELOG` (tags, releases y fuentes equivalentes), `README-TESTING` y `DOC-TESTING` (suficiencia y límites de lo verificado), `DOC-SECURITY` (calidad documental frente a hallazgos históricos) y `README-LICENSE` (claridad jurídica sin licencias inventadas).
2. **P2 — Precisión y contexto:** contrato API o no aplicabilidad, política de contribución, vigencia de arquitectura y estado, integridad documental de datos, operaciones locales y navegación.
3. **P3 — Suficiencia editorial:** presentación, demos, destacados, diagramas, ADR y referencias, sin imponer nuevos documentos si lo existente es funcionalmente equivalente.

Estos grupos marcan **orden de revisión**, no un supuesto automatizado de que cualquier Responsibility P1 deba quedar `Partial` o recibir una decisión `ADD`.

## 4. Procedimiento para validar la matriz sin fabricar aprobaciones

1. **Fijar reviewer, fecha y referencia.** Confirmar quién aprueba cada Responsibility y que se está revisando el SHA concreto. Si se quiere evaluar `main` actual del consumer, iniciar refresco de Evidence, no reutilizar sin más conclusiones del snapshot histórico.
2. **Resolver los casos con State/Applicability alternativos.** Priorizar `DOC-CHANGELOG`, `README-CONTRIBUTING`, `DOC-API`, `DOC-DIAGRAMS` y la Applicability de `DOC-REFERENCES`. Un campo de Applicability `Uncertain` es válido en el contrato; `Missing / Partial` no es un `State` válido y **debe discriminarse** antes de completar una ficha formal.
3. **Valorar calidad documental y evidencia suficiente.** Confirmar que cada ficha cita fuentes pertinentes y que el rationale sustenta el `State` finalmente elegido, en vez de perpetuar `Partial` por precaución. Una Responsibility documental no necesita que se reproduzca cada test del sistema, pero sí límites explícitos cuando su afirmación es operativa.
4. **Registrar el resultado en el Assessment.** Elegir para cada Responsibility `State: Satisfied / Partial / Missing`, `Applicability: Applicable / Not Applicable / Uncertain`, `Evidence`, `Evaluation Rationale`, `Uncertainty` y `Decision Status`. Las sugerencias de esta matriz no se copian como si hubieran sido aprobadas.
5. **Resolver decisiones solamente donde esté justificado.** `Decision Status: Resolved` exige `Adoption Decision` estable y su rationale. Para `Needs Further Evaluation`, mantener `Adoption Decision: —` junto con incertidumbre y razón concreta.
6. **Aplicar Completion Check del Template.** El Assessment puede quedar `Complete` con decisiones no resueltas, pero **solo** después de registrar y revisar todos los campos requeridos por Responsibility. No autoriza automáticamente `Application` o `Integration`.

## 5. Registro de sesiones del reviewer

| Campo | Valor |
| --- | --- |
| Reviewer | Pendiente de asignación |
| Reference aceptada | `28d75a50e0a178954dd46acc23300d9dd327843c` (propuesta) |
| Fecha y alcance de aprobación | Pendiente |
| Responsabilidades con ficha E3 propuesta | `28` |
| Responsabilidades con evaluación aprobada | `0` acreditadas |
| Primer bloque recomendado | P1: Quick Start, Changelog, Testing, Security y License |
| Siguiente salida requerida | Actualizar registro real del [Assessment Template](../assessment-template.md) con aprobación y rationale por Responsibility |
| Assessment Status | `In Progress` |

**Resultado:** esta matriz reduce dispersión y prioriza la revisión de evidencia. **No sustituye el Assessment humano**, no constituye una decisión de aplicación y no modifica el repositorio consumidor.
