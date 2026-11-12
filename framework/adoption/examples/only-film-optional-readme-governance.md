# Only Film — Assessment Batch 5: Optional README Governance

## 1. Contexto

Inspección documental **read-only** de cuatro responsabilidades `Optional` de `TPL-BACKEND` 0.1.0, a partir del repositorio `fran-eliot/only_film` en el commit inmutable `28d75a50e0a178954dd46acc23300d9dd327843c`.

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Scope | `README-ROADMAP`, `README-CONTRIBUTING`, `README-AUTHOR`, `README-LICENSE` |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |

El requirement level `Optional` procede del Template. **No implica automáticamente `Not Applicable` ni autoriza omitir una revisión de Applicability**. `Explored — provisional` indica trabajo documental y no es un estado contractual de conformidad.

## 2. Resumen de cobertura

| Responsibility | Level | Cobertura documental | State / Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-ROADMAP` | Optional | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `README-CONTRIBUTING` | Optional | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `README-AUTHOR` | Optional | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `README-LICENSE` | Optional | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |

## 3. README-ROADMAP

**Detected Facts**

- El README incluye una sección llamada `Próximas líneas de evolución`.
- Menciona API REST, integración de pagos, observabilidad, despliegue automatizado y mejoras de mantenibilidad como posibles ampliaciones, diferenciadas de capacidades existentes.
- El árbol inspeccionado contiene `docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md`, que declara como base un commit histórico de octubre de 2026, no el SHA completo de este Assessment.
- No se observó un archivo raíz con nombre `ROADMAP.md` en el árbol inspeccionado.

**Evidence**

- [README.md — Próximas líneas de evolución](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Documento histórico de auditoría y roadmap](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md)
- [Árbol fijado del consumer](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)

**Evaluation Rationale (pendiente):** existen líneas de evolución explícitas, pero no se ha comprobado si sus prioridades, dependencias y vigencia son suficientes para la finalidad de un roadmap. La ausencia de un archivo con nombre canónico no determina el cumplimiento.

**Uncertainty:** ¿hay un roadmap operativo actualizado en Issues o Projects? ¿Se necesita una representación más detallada para los contribuidores?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 4. README-CONTRIBUTING

**Detected Facts**

- El README documenta cómo ejecutar la aplicación y consultar pruebas, CI y organización del repositorio.
- El árbol completo inspeccionado no incluye un archivo llamado `CONTRIBUTING.md` o una ruta de contribución con ese nombre.
- Las instrucciones de ejecución no equivalen necesariamente a una política de contribución, revisiones o aceptación de PR.
- No se han auditado Issues, configuraciones o normas externas que pudieran explicar cómo colaborar.

**Evidence**

- [README.md — Inicio rápido, pruebas y organización](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Árbol Git del commit](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)

**Evaluation Rationale (pendiente):** la ausencia de un archivo canónico es una observación de estructura, no una asignación automática de `Missing`. Es necesario identificar la política efectiva de contribución y si esta Responsibility resulta aplicable a un repositorio académico evolucionado.

**Uncertainty:** ¿se aceptan contribuciones externas? ¿existe un flujo documentado para Issues, pruebas y PR? ¿debe explicitarse alguna norma por el origen colaborativo?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 5. README-AUTHOR

**Detected Facts**

- El apartado `Origen, créditos y evolución` reconoce explícitamente cuatro personas del proyecto académico original, con enlaces individuales a GitHub.
- El README enlaza el repositorio de origen `certidevs/g1_testing` y diferencia el trabajo académico del desarrollo posterior realizado en `fran-eliot/only_film`.
- El README declara que el historial y las Pull Requests permiten atribuir cambios, sin afirmar autoría exclusiva del código original.

**Evidence**

- [README.md — Origen, créditos y evolución](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Repositorio de procedencia mencionado](https://github.com/certidevs/g1_testing) (fuente externa para futura comprobación; no se revisa aquí su historial)

**Evaluation Rationale (pendiente):** hay información de autoría y créditos observable y contextualizada. Queda por revisar la suficiencia y exactitud de las atribuciones, sin introducir una afirmación de propiedad intelectual no verificada.

**Uncertainty:** ¿la sección distingue con suficiente claridad colaboradores originales, mantenedor actual y evolución posterior? ¿existe alguna contribución relevante no reflejada en esa atribución?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 6. README-LICENSE

**Detected Facts**

- La última línea del README contiene una nota titulada `Licencia`: se describe el origen académico y se remite al repositorio original y su documentación para conocer las condiciones de uso.
- La propia nota indica que ese README no establece por sí solo una licencia adicional.
- El árbol completo del commit no contiene un archivo raíz llamado `LICENSE`, `LICENCE` o `COPYING`.
- En el `pom.xml` se observó un elemento `<licenses><license/></licenses>` sin detalles. No constituye una licencia de uso por sí mismo.

**Evidence**

- [README.md — Nota final de licencia](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [pom.xml — declaración de licencias](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [Árbol Git del commit](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)

**Evaluation Rationale (pendiente):** existe una advertencia explícita, pero no se ha determinado qué permisos jurídicos rigen el software. Ni la ausencia de archivo LICENSE ni el texto de crédito son suficientes para emitir un dictamen de licencias.

**Uncertainty:** ¿qué condiciones impone la procedencia del código original? ¿hay permisos de los participantes o políticas de la institución? ¿qué información conviene comunicar sin establecer una licencia que no se ha verificado?

**State / Applicability:** pendientes de revisión semántica y, si procede, de autorización de los titulares pertinentes.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

**Propuesta E3 posterior:** la [revisión semántica de Roadmap, Contributing, Author y License](only-film-optional-governance-semantic-review.md) incorpora hipótesis y criterios de decisión específicos. CONTRIBUTING conserva State y Applicability sin discriminar, y LICENSE se trata como aviso informativo, no como permisos jurídicos otorgados. Ninguna propuesta está aprobada.

## 7. Resultado del lote

| Comprobación | Resultado |
| --- | --- |
| Cuatro Responsibilities Optional identificadas en el Template | Documentado |
| Detected Facts vinculados al consumer fijado | Documentados |
| Interpretaciones separadas de Evidence | Documentadas |
| Review semántica y de licencias cuando proceda | Pendiente |
| Ejecución de builds/tests o modificación del consumer | No realizada |
| Adoption Decisions | Ninguna resuelta |

La [matriz de cobertura](only-film-assessment-coverage.md) pasa de **15/28 a 19/28 Responsibilities exploradas documentalmente**: 8 Required, 7 Recommended y 4 Optional. Las nueve Optional restantes continúan sin explorar.

Este resultado no demuestra conformidad; el Assessment permanece `In Progress`. No se autoriza Application ni Integration, y no se ha modificado el repositorio consumidor.
