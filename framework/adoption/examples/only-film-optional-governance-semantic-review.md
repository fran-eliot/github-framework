# Only Film — Provisional Semantic Review: Optional README Governance

## 1. Assessment Context

Propuesta E3 de cuatro Responsibilities `Optional` de `TPL-BACKEND` 0.1.0. Las fuentes están vinculadas a un commit inmutable de Only Film. **No equivale a aprobación humana, licencia otorgada ni autorización para modificar el repositorio consumidor.**

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Scope | `README-ROADMAP`, `README-CONTRIBUTING`, `README-AUTHOR`, `README-LICENSE` |
| Assessment Status | `In Progress` |
| Review Status | `Proposal — pending human review` |
| Reviewer / Approval | Sin asignar / no aprobado |
| Mutation | `NONE` |

`Optional` **no implica** `Not Applicable`, pero tampoco obliga a añadir un archivo. La aplicabilidad debe decidirse según el contexto real del consumer.

## 2. Resumen de hipótesis, no de estados aprobados

| Responsibility | Level | Proposed State | Proposed Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-ROADMAP` | Optional | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `README-CONTRIBUTING` | Optional | `Missing` / `Partial` — hipótesis no discriminadas | **Por decidir**: depende de política real de colaboración | `Needs Further Evaluation` | `—` |
| `README-AUTHOR` | Optional | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `README-LICENSE` | Optional | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |

`README-CONTRIBUTING` no tiene un State elegido: las instrucciones de desarrollo existentes podrían considerarse cobertura parcial solo si el reviewer acredita que satisfacen una política de colaboración relevante. La hipótesis `Partial` de las otras tres no representa una deficiencia demostrada.

## 3. Responsibility — README-ROADMAP

**Implementation Characteristics (proposed):** `Own`, `Distributed`. Apartado de evolución futura en README y documento F3 con otra fecha de referencia.

**Detected Facts:**

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) contiene `Próximas líneas de evolución`, con posibles API REST, proveedor real de pagos, observabilidad y automatización de despliegue; distingue expresamente propuestas de funcionalidades ya implantadas.
- [F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) define iniciativas F3.002–F3.008 y declara como base un commit histórico `df63353564485eb6d2d60c982032e5d3c4facbf2`. Su secuencia no acredita el estado de ejecución de esas iniciativas en el SHA evaluado.
- El [Component README-ROADMAP](../../components/readme/roadmap/README.md) pide resumir las próximas fases sin sustituir un roadmap detallado.

**Evidence:** [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [F3](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md), [exploración inicial](only-film-optional-readme-governance.md).

**Evaluation Rationale — propuesta:** existen próximos pasos comunicados al lector, que satisfacen al menos la finalidad introductoria de Roadmap. Sin embargo, el reviewer debe determinar qué iniciativas siguen realmente siendo futuras y si el resumen es suficientemente útil; el documento F3 histórico no actualiza automáticamente el README.

**Uncertainty:** ¿Las propuestas representan las prioridades reales del commit fijado? ¿El texto basta para una orientación breve, sin imponer un roadmap separado? ¿Cómo se evita mantener futuras funcionalidades ya completadas como pendientes?

**Proposed State:** `Partial`; **Proposed Applicability:** `Applicable`. Ambos pendientes de aprobación.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 4. Responsibility — README-CONTRIBUTING

**Implementation Characteristics (proposed):** posible `Distributed`; no se ha acreditado un flujo editorial autónomo de contribuciones.

**Detected Facts:**

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) contiene requisitos para desarrollar, ejecutar pruebas, conocer CI y localizar el código; estas instrucciones ayudan a contribuir técnicamente, pero **no equivalen necesariamente a política de colaboración**.
- El árbol del SHA inspeccionado no presenta un archivo `CONTRIBUTING.md`; la ausencia de ese nombre no acredita que no existan reglas externas o equivalentes.
- No se han comprobado reglas para colaboradores externos, plantillas de PR, políticas de review, convenciones de commits o gobernanza de aceptación.
- En el catálogo `framework/components/readme/` inspeccionado no se identificó un Component autónomo `README-CONTRIBUTING`. La Responsibility sí está enumerada como `Optional` en [TPL-BACKEND metadata](../../templates/repositories/backend/metadata.yml). **Esta asimetría afecta al Framework, no prueba una carencia del consumer.**

**Evidence:** [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [árbol del consumer](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c), [exploración inicial](only-film-optional-readme-governance.md).

**Evaluation Rationale — propuesta:** sin confirmar si se reciben contribuciones externas o si hay reglas documentadas en otra fuente, no corresponde elegir automáticamente entre `Missing`, `Partial` o `Not Applicable`. El nivel `Optional` da margen a decidir con criterios de valor y mantenimiento, no a inventar procesos.

**Uncertainty:** ¿Quién puede contribuir y con qué condiciones? ¿Existe política escrita en GitHub u otra documentación? ¿Las instrucciones técnicas del README cubren lo que realmente necesita la audiencia? ¿Es deseable crear o enlazar una guía de contribución?

**Proposed State:** sin elegir entre `Missing` y `Partial`. **Proposed Applicability:** sin decidir entre `Applicable` y `Not Applicable` hasta confirmar el propósito real; no se registra ninguno como valor definitivo.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 5. Responsibility — README-AUTHOR

**Implementation Characteristics (proposed):** `Own`, `Equivalent`: créditos y atribución en README, sin un bloque etiquetado `Author`.

**Detected Facts:**

- `Origen, créditos y evolución` del [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) reconoce cuatro integrantes del proyecto académico, enlaza sus perfiles y el [repositorio original](https://github.com/certidevs/g1_testing).
- El texto diferencia el origen colaborativo de la evolución posterior en `fran-eliot/only_film` y no atribuye en exclusiva el trabajo de formación a un único mantenedor.
- El [Component README-AUTHOR](../../components/readme/author/README.md) permite identificar a un autor o equipo mediante nombre y enlaces; no obliga a titular literalmente la sección `Author`.

**Evidence:** [README — créditos](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [Component Author](../../components/readme/author/README.md), [exploración inicial](only-film-optional-readme-governance.md).

**Evaluation Rationale — propuesta:** la atribución está expresamente documentada y es compatible con el propósito de la Responsibility. Su clasificación `Partial` es una hipótesis conservadora hasta que un reviewer valore la claridad de la separación entre autores originales, responsables actuales y contribuciones posteriores. **No** se ha verificado exhaustivamente la titularidad del código.

**Uncertainty:** ¿Hay créditos incompletos u omisiones significativas? ¿Distingue la sección suficientemente entre autoría original y mantenimiento posterior? ¿Son necesarias referencias adicionales sin convertir el README en un dictamen de propiedad intelectual?

**Proposed State:** `Partial`; **Proposed Applicability:** `Applicable`. Ambos pendientes de aprobación.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 6. Responsibility — README-LICENSE

**Implementation Characteristics (proposed):** `Own`, `Equivalent` **solo como aviso documental**; no se acredita licencia válida ni concesión de derechos.

**Detected Facts:**

- La última línea del [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) contiene una nota de licencia que remite a la procedencia académica y advierte expresamente que ese texto **no establece otra licencia**.
- En el árbol inspeccionado no se identificó un archivo `LICENSE`, `LICENCE` o `COPYING` en la raíz.
- El [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) contiene `<licenses><license/></licenses>` sin valores que definan términos de uso.
- En el catálogo de componentes README inspeccionado no se identificó un Component autónomo `README-LICENSE`, aunque [TPL-BACKEND metadata](../../templates/repositories/backend/metadata.yml) enumera la Responsibility como Optional.

**Evidence:** [README — nota final](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml), [árbol del SHA](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c), [exploración inicial](only-film-optional-readme-governance.md).

**Evaluation Rationale — propuesta:** existe un aviso prudente que evita presentar una licencia no verificada como vigente, pero no proporciona un régimen claro de reutilización. Evaluar la calidad de la nota del README **no es** validar los permisos jurídicos del proyecto original ni autoriza elegir una licencia sin la intervención de los titulares pertinentes.

**Uncertainty:** ¿Qué derechos y autorizaciones permiten reutilizar y publicar el código académico? ¿Debe el README explicar más claramente la situación o enlazar a una fuente jurídica comprobada? ¿Se necesita asesoramiento específico antes de anunciar permisos?

**Proposed State:** `Partial`; **Proposed Applicability:** `Applicable`. Ambos pendientes de aprobación.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 7. Gates de revisión humana

| Gate | Condición | Estado |
| --- | --- | --- |
| OG-1 | Confirmar contexto de portfolio, mantenimiento y audiencia de las cuatro Responsibilities | Pendiente |
| OG-2 | Contrastar actualidad de roadmap F3 y del README con el SHA de referencia | Pendiente |
| OG-3 | Determinar política efectiva de contribución, Applicability y State justificables | Pendiente |
| OG-4 | Revisar créditos originales y actuales sin inferir titularidad no comprobada | Pendiente |
| OG-5 | Aclarar información de licencias con fuentes/autoridades pertinentes, sin otorgar derechos no acreditados | Pendiente |
| OG-6 | Evaluar por separado la asimetría entre metadata de TPL-BACKEND y Components CONTRIBUTING/LICENSE | Pendiente del Framework, no del consumer |
| OG-7 | Aprobar/corregir State, Applicability y rationale individualmente y resolver decisiones solo con autorización | Pendiente |

## 8. Cobertura Optional y conclusión

Este lote aporta **cuatro nuevas propuestas E3 Optional**. Sumadas a la propuesta anterior de `DOC-SECURITY`, existen ahora **cinco propuestas Optional de trece**, sin aprobación.

Todas las hipótesis permanecen en `Needs Further Evaluation`, con `Adoption Decision: —`. El Assessment completo sigue `In Progress`; **28/28** representa exploración documental, no conformidad. No se modificó Only Film ni se ejecutaron tests o revisiones legales.
