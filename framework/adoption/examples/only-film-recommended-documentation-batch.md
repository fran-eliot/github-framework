# Only Film — Assessment Batch 4: Recommended Documentation Responsibilities

## 1. Contexto y alcance

Este lote explora documentalmente las tres Responsibilities `Recommended` de documentación que permanecían sin inspeccionar bajo `TPL-BACKEND` 0.1.0: `DOC-ARCHITECTURE`, `DOC-PROJECT-STATUS` y `DOC-TESTING`. Se mantiene el repositorio consumidor en modo **read-only** y se fija el mismo commit que en los ejemplos anteriores.

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Commit SHA | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Collection Scope | `DOC-ARCHITECTURE`, `DOC-PROJECT-STATUS`, `DOC-TESTING` |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |

Se leen fuentes versionadas en ese commit, no se extrapolan a la rama actual de Only Film. Una auditoría histórica documenta lo observado cuando se redactó, **no** el estado operativo actual sin una nueva verificación.

## 2. Resumen provisional

| Responsibility | Requirement Level | Cobertura | State / Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `DOC-ARCHITECTURE` | `Recommended` | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `DOC-PROJECT-STATUS` | `Recommended` | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `DOC-TESTING` | `Recommended` | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |

`Explored — provisional` expresa solamente la cobertura de inspección documental; no es un valor de `State` del Assessment Template.

## 3. DOC-ARCHITECTURE

**Contrato:** [DOC-ARCHITECTURE](../../components/documentation/architecture/README.md) busca explicar la arquitectura vigente, componentes, relaciones, flujos y restricciones a nivel superior al detalle de implementación.

**Detected Facts**

- Existe `docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md`, titulado «Revisión de arquitectura y mantenibilidad — Only Film», fechado el 10/10/2026.
- La auditoría declara como base una referencia histórica posterior a la PR #23 (`b6cf52c9`) y utiliza inspección estática.
- El documento describe el flujo nominal MVC como controladores → servicios → repositorios, e identifica en esa revisión rutas que eludían algunas fronteras mediante acceso directo a repositorios.
- El README del commit fija un resumen por capas y un flujo principal MVC/JPA.
- Existe también `docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md` basado en un commit posterior a aquella auditoría; las observaciones entre documentos corresponden a momentos diferentes y no deben reconciliarse automáticamente.

**Evidence**

- [Auditoría de arquitectura y mantenibilidad](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md)
- [Auditoría funcional y roadmap — distinta referencia histórica](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md)
- [README.md — resumen de arquitectura](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)

**Evaluation Rationale (pendiente)**

Hay contenido técnico relevante sobre límites arquitectónicos y problemas de mantenibilidad. Sin embargo, una auditoría de riesgos fechada no equivale necesariamente a un documento consolidado que describa la **arquitectura vigente en el commit evaluado**. Los hallazgos históricos pueden haber cambiado. No se ha comprobado la arquitectura directamente contra el código del commit.

**Uncertainty**

- ¿Qué descripciones corresponden a la arquitectura efectiva del SHA fijado?
- ¿Existe una visión arquitectónica estable, independiente de las auditorías de incidencias?
- ¿Qué hallazgos históricos están ya corregidos y qué evidencia permite distinguirlos?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 4. DOC-PROJECT-STATUS

**Contrato:** [DOC-PROJECT-STATUS](../../components/documentation/project-status/README.md) resume situación actual, progreso, trabajo en curso, próximos hitos, riesgos y objetivos inmediatos.

**Detected Facts**

- Existe `docs/TECHNICAL_MATURITY_ASSESSMENT.md`, titulado «Evaluación de madurez técnica — Only Film», con fecha 10/10/2026.
- Su base declarada es el commit histórico `9f2a31e927df105d14e3d30d4d8277fa61883deb`, anterior al commit fijado para este Assessment.
- El documento recoge una valoración cualitativa del proyecto como portfolio backend evolucionado y declara expresamente limitaciones: no se trata de un pentest, análisis SonarCloud reciente ni medición de cobertura.
- El README del commit ofrece un apartado «Próximas líneas de evolución», distinguiendo posibles ampliaciones de funcionalidades ya implantadas.
- `docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md` presenta objetivos de evolución de fase 3 y una auditoría funcional con referencia propia; no es por sí solo una fotografía operativa actualizada automáticamente.

**Evidence**

- [Evaluación histórica de madurez técnica](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md)
- [Auditoría funcional y roadmap](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md)
- [README.md — líneas de evolución](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)

**Evaluation Rationale (pendiente)**

Las fuentes contienen evaluación de madurez, riesgos y objetivos, pero fueron redactadas sobre referencias distintas y anteriores. No se ha comprobado si proporcionan una fotografía operativa vigente y suficientemente completa del estado de Only Film en el SHA del consumer. No se infiere `Missing` por no existir un archivo llamado `PROJECT_STATUS.md`.

**Uncertainty**

- ¿Qué fuente mantiene hoy las prioridades, los hitos y el estado operativo del repositorio?
- ¿Qué elementos de las auditorías históricas necesitan actualización respecto al SHA evaluado?
- ¿Basta la información del README y los documentos existentes, o hay una necesidad real de consolidación?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 5. DOC-TESTING

**Contrato:** `DOC-TESTING` figura como `Recommended` en la [metadata canónica de TPL-BACKEND](../../templates/repositories/backend/metadata.yml). Se inspecciona la documentación sobre estrategia, ejecución y límites de pruebas, sin deducir resultados de una ejecución no realizada.

**Detected Facts**

- `docs/POSTGRESQL_INTEGRATION_TESTS.md` explica la clase `PostgresPersistenceIntegrationTest`, los escenarios de persistencia y concurrencia y el uso del workflow `postgres-migration.yml`.
- Ese documento proporciona instrucciones locales con PostgreSQL y advierte que el test puede crear datos y no debe ejecutarse contra bases reales.
- `docs/JACOCO_COVERAGE_BASELINE.md` describe una selección de pruebas H2 y los artefactos JaCoCo; advierte que esa selección **no** es cobertura global y que deben extraerse porcentajes solo de informes reales.
- `docs/SONARCLOUD_PR_CI.md` describe el análisis en PR y `main`, incluida la dependencia del secreto `SONAR_TOKEN` y el caso en que el escáner se omite.
- El README incluye instrucciones de `./mvnw test`, variantes de filtrado y una tabla de workflows.

**Evidence**

- [Tests de integración PostgreSQL](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md)
- [Línea base de cobertura JaCoCo](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/JACOCO_COVERAGE_BASELINE.md)
- [Análisis SonarCloud en CI](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SONARCLOUD_PR_CI.md)
- [README.md — Pruebas y CI](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)

**Evaluation Rationale (pendiente)**

Se observan guías técnicas especializadas y distinciones útiles entre integración PostgreSQL, regresión H2, cobertura y análisis estático. La presencia de esas guías no prueba que la suite pase, que sus comandos sigan funcionando o que las métricas estén actualizadas en el commit. Tampoco se ha verificado si el conjunto cubre todas las necesidades de documentación de testing del consumer.

**Uncertainty**

- ¿Qué comandos y workflows se han reproducido con éxito sobre el commit fijado?
- ¿Qué cobertura actual está respaldada por un informe de JaCoCo identificado?
- ¿Es suficiente la organización de las guías para un nuevo colaborador?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

**Seguimiento de DOC-TESTING:** la [reconciliación de seguridad y Testing](only-film-security-testing-reconciliation.md) identifica archivos de tests y resultados de tres checks del SHA fijado, pero conserva pendientes Selenium, informes JaCoCo y evaluación semántica.

**Propuesta E3 posterior para Architecture y Project Status:** la [revisión semántica de las dos Responsibilities](only-film-recommended-docs-semantic-review.md) contrasta el propósito documental del Framework con fuentes históricas del consumer y conserva las interpretaciones provisionales, sin convertir auditorías antiguas en un estado vigente ni aprobar Adoption Decisions. `DOC-TESTING` ya tiene una [propuesta E3 propia](only-film-testing-semantic-review.md).

## 6. Resultado y continuación

| Check | Resultado |
| --- | --- |
| Tres Responsibilities Recommended identificadas | Documentado |
| Evidencia documental vinculada al commit del consumer | Documentada |
| Fechas y referencias históricas distinguidas | Documentadas |
| Incertidumbres y límites de interpretación | Documentados |
| Revisión semántica por reviewer | Pendiente |
| Verificación de tests, build y cobertura | No realizada |
| Adoption Decisions resueltas | Ninguna |

Con este lote, la [matriz de cobertura](only-film-assessment-coverage.md) pasa de **12/28 a 15/28 Responsibilities exploradas documentalmente**: 8/8 Required, 7/7 Recommended y 0/13 Optional. Las **13 Optional** permanecen sin explorar.

La cobertura documental completa de Required y Recommended **no significa conformidad**. El Assessment sigue `In Progress`, sin autorización para Application o Integration y sin modificaciones del repositorio consumidor.
