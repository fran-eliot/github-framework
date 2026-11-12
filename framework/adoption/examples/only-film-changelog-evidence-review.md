# Only Film — Pinned Changelog and Release Evidence Review

## 1. Contexto y objetivo

Esta revisión **E2 de calidad de evidencia** se centra en `DOC-CHANGELOG`, Responsibility `Required` de `TPL-BACKEND` 0.1.0. No supone una nueva clasificación semántica ni una decisión de adopción.

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Responsibility | `DOC-CHANGELOG` (`Required`) |
| Método | Inspección read-only del árbol Git, README, POM, commits accesibles y GitHub Releases |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |

**Pregunta:** ¿Existe una fuente de cambios *publicados entre versiones* que desempeñe la función documental de `DOC-CHANGELOG`, aunque no se llame `CHANGELOG.md`?

El [Component DOC-CHANGELOG](../../components/documentation/changelog/README.md) diferencia expresamente un Changelog del historial exhaustivo de Git, PRs, Issues, release notes y estado del proyecto. No puede resolverse esta Responsibility simplemente buscando un archivo canónico.

## 2. Comprobaciones realizadas y fuentes

| Comprobación | Resultado observado | Alcance y límites |
| --- | --- | --- |
| Árbol Git del SHA fijado | No se identificaron rutas cuyo nombre incluyese `changelog`, `changes`, `history` o `release` | Evidencia de **nombres de rutas** en el commit, no evaluación exhaustiva de todo el contenido |
| README del SHA | Describe evolución técnica, contexto académico y futuras líneas de trabajo; remite al historial Git y a PR para atribución de cambios | No muestra una cronología de cambios **publicados entre versiones** |
| POM del SHA | Versión del proyecto `0.0.1-SNAPSHOT`; parent Spring Boot `4.0.5` | Una versión de artefacto de desarrollo y la versión de una dependencia **no son un historial de releases** |
| Auditoría funcional | Existe `docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md` con roadmap y revisión de cambios/hallazgos históricos | Documenta evolución y propuestas, pero no se ha acreditado su condición de fuente oficial de cambios publicados |
| Historial Git hasta el SHA | Commits de features, tests y PRs fusionadas, incluidos #493, #491 y #489, identificados en los 30 commits recientes consultados | Evidencia de actividad de desarrollo; no demuestra por sí sola publicación de versiones |
| GitHub Releases | La consulta al endpoint de releases del repositorio devolvió **lista vacía en el momento de la revisión** | Consulta del estado del endpoint; no demuestra por sí sola que jamás existieron releases ni prueba el estado histórico exacto de una referencia Git |
| Tags | **No verificados:** la consulta de tags fue rechazada por las restricciones del acceso disponible | **No concluir que no existen tags**; pendiente comprobación independiente |

**Fuentes fijadas al commit**

- [README.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [Auditoría funcional y roadmap](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md)
- [Árbol de Only Film en el SHA](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)
- [Historial hasta el commit evaluado](https://github.com/fran-eliot/only_film/commits/28d75a50e0a178954dd46acc23300d9dd327843c/)
- [Página de releases del repositorio](https://github.com/fran-eliot/only_film/releases) — recurso **mutable**, consultado en esta revisión; no es evidencia versionada en el SHA

## 3. Interpretación acotada

Los archivos versionados y el historial Git **sí permiten rastrear cambios individuales**. Sin embargo, en las fuentes inspeccionadas **no se ha identificado** una secuencia consolidada que comunique a usuarios y mantenedores qué cambios relevantes fueron publicados por versión.

Esto **no equivale** a declarar `State: Missing`, porque siguen abiertas al menos dos cuestiones:

1. **Fuentes alternativas:** podrían existir tags, notas de release externas, documentación equivalente o una política de versionado no incluida en los artefactos inspeccionados.
2. **Adecuación y aplicabilidad:** el reviewer debe definir el contexto real del consumidor y valorar si un mecanismo de registro de cambios es necesario y qué evidencia satisface la Responsibility `Required` del Template.

No sería válido reconstruir una lista de releases a partir de los commits y presentarla como si esos cambios se hubieran publicado formalmente. Tampoco procede recomendar automáticamente añadir `CHANGELOG.md` antes de terminar la evaluación.

## 4. Verificaciones necesarias para una revisión semántica

| Gate | Acción de revisión | Criterio observable |
| --- | --- | --- |
| C1 — Tags | Consultar tags alcanzables desde el commit fijado, incluyendo fechas y destinos de referencia | Registro verificable de existencia/ausencia **con alcance limitado al snapshot** |
| C2 — Releases | Reconfirmar publicaciones y notas de release, distinguiendo consulta actual de historia al SHA | Evidencia de fechas, versiones, contenido y vínculo al commit cuando existan |
| C3 — Fuente equivalente | Localizar documentación o registros distintos de Git history / PR list | Una fuente legible que resuma cambios relevantes publicados y sus versiones, o constancia de que aún no se ha identificado |
| C4 — Política de versiones | Revisar si `0.0.1-SNAPSHOT` representa solo desarrollo o si hay un procedimiento de publicación formal | Conclusión explícita sustentada en evidencias, sin deducir releases del POM |
| C5 — Contexto de uso | Determinar destinatarios y necesidades de comunicación de cambios | Justificación documentada de Applicability y expectativas de la Responsibility |
| C6 — Evaluación individual | Registrar en el Assessment `State`, `Applicability`, `Evidence`, `Evaluation Rationale`, `Uncertainty`, `Decision Status` | Reviewer identificado y razonamiento trazable; decisión solo cuando corresponda |

Si se obtienen nuevos datos sobre tags, releases o fuentes equivalentes, se deben registrar con **fecha de consulta y referencia comprobable** antes de evaluar la Responsibility.

## 5. Resultado para el Assessment

| Campo | Resultado |
| --- | --- |
| `DOC-CHANGELOG` — requirement level | `Required`, confirmado en TPL-BACKEND 0.1.0 |
| Archivo canónico de Changelog | No identificado en las rutas del árbol consultado |
| Historia de cambios técnicos | Existe en commits y PRs accesibles |
| Cambios publicados por versión | No acreditados en las fuentes inspeccionadas |
| GitHub Releases | Lista vacía al consultar el endpoint |
| Tags | Sin comprobar |
| State y Applicability | Pendientes de evaluación semántica |
| Decision Status | `Needs Further Evaluation` |
| Adoption Decision | `—` |
| Assessment Status | `In Progress` |

**Conclusión:** esta verificación reduce y delimita la incertidumbre sobre las fuentes, pero **no resuelve `DOC-CHANGELOG`**, no autoriza modificar Only Film y no convierte el Assessment en `Complete`.
