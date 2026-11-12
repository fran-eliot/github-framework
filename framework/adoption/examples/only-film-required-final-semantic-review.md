# Only Film — Provisional Semantic Review: Tech Stack, Documentation and Footer

## 1. Contexto

Propuesta E3 para las tres Responsibilities `Required` que faltaban por tratar semánticamente en `TPL-BACKEND` 0.1.0. La evidencia documental se compara con el README fijado de Only Film y con los criterios publicados de los Components. **No constituye una revisión humana aprobada, validación de licencia ni una decisión de adopción.**

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Collection Scope | `README-TECH-STACK`, `README-DOCUMENTATION`, `README-FOOTER` |
| Assessment Status | `In Progress` |
| Review Status | `Proposal — pending human review` |
| Reviewer / Approval Date | Sin asignar / no aprobada |
| Consumer Mutation | `NONE` |

## 2. Resumen de propuestas

| Responsibility | Requirement Level | Proposed State | Proposed Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-TECH-STACK` | Required | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `README-DOCUMENTATION` | Required | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `README-FOOTER` | Required | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |

`Partial` expresa una **hipótesis conservadora** en espera del criterio editorial y contextual del reviewer. **No se ha demostrado que las tres sean deficientes**. Un reviewer podrá justificar `Satisfied` cuando las fuentes y requisitos documentales lo respalden; ninguna clasificación se convierte automáticamente en definitiva.

## 3. Responsibility: README-TECH-STACK

**Requirement Level:** `Required`.

**Proposed State:** `Partial` — sin aprobación.

**Proposed Applicability:** `Applicable` — sin aprobación.

**Implementation Characteristics (proposed):** `Own`, `Canonical`: sección explícita de tecnologías con tabla por capas en el README principal.

### Detected Facts

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) contiene `## Tecnologías y arquitectura`, con categorías Backend, Seguridad, Frontend, Persistencia local rápida, Persistencia duradera, Pruebas e Infraestructura.
- La tabla enumera Java 25, Spring Boot 4.0.5, Spring MVC, Spring Data JPA, Hibernate, Spring Security, BCrypt, Thymeleaf, Bootstrap 5, H2, PostgreSQL 17, Flyway, JUnit 5, Mockito, MockMvc, Selenium, Docker Compose, GitHub Actions y JaCoCo, entre otros.
- El [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) fija `java.version=25` y parent `spring-boot-starter-parent` 4.0.5, compatible con la declaración de Java y Spring Boot del README.
- El [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) usa `postgres:17-alpine` y define servicios `app`/`postgres`, aportando soporte estático a las afirmaciones sobre persistencia PostgreSQL y Docker Compose.
- El [Component Tech Stack](../../components/readme/tech-stack/README.md) recomienda agrupar por categorías Backend, Frontend, Database, Cloud, DevOps y Testing, sin imponer exactamente esos encabezados.

### Evidence

- [README — Tecnologías y arquitectura](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml)
- [Component Tech Stack](../../components/readme/tech-stack/README.md)
- [Exploración documental original](only-film-required-readme-batch-2.md)

### Evaluation Rationale — propuesta

La sección cumple una finalidad evidente de presentación tecnológica y utiliza categorías comprensibles que se corresponden funcionalmente con las recomendadas en el Framework. Las versiones Java, Spring Boot y PostgreSQL se contrastaron contra las fuentes versionadas; **no se ha efectuado una auditoría exhaustiva de todas las dependencias y usos**. Su clasificación `Partial` se ofrece para revisión, sin convertir la ausencia de un apartado Cloud en un defecto de un proyecto que no declara infraestructura cloud.

### Uncertainty

- ¿Las tecnologías de la tabla se utilizan efectivamente como se describen en el SHA fijado, y está clara la distinción entre dependencias de desarrollo, ejecución y testing?
- ¿La combinación de Tech Stack y descripción arquitectónica es suficientemente legible o mezcla responsabilidades editoriales?
- ¿Qué categorías se necesitan para la audiencia real, sin añadir infraestructura no utilizada solo para satisfacer una lista orientativa?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** no se ha aprobado si la sección se conserva tal como está o se reorganiza; ambas opciones requieren una evaluación explícita de exactitud y usabilidad.

## 4. Responsibility: README-DOCUMENTATION

**Requirement Level:** `Required`.

**Proposed State:** `Partial` — sin aprobación.

**Proposed Applicability:** `Applicable` — sin aprobación.

**Implementation Characteristics (proposed):** `Own`, `Distributed`: enlaces a documentación repartidos por las secciones temáticas, acompañados de un árbol de organización del repositorio.

### Detected Facts

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) enlaza `docs/screenshots/`, `docs/POSTGRESQL_SETUP.md`, `docs/SECURITY_HARDENING_AUDIT.md` y `docs/POSTGRESQL_INTEGRATION_TESTS.md`, además de varios workflows de CI.
- La sección `Organización del repositorio` explica mediante un árbol la ubicación general de `src/main`, `src/test`, `docs/`, `.github/workflows/`, Dockerfile, Compose y configuración local.
- Los documentos [POSTGRESQL_SETUP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) y [POSTGRESQL_INTEGRATION_TESTS.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md) están versionados en el commit inspeccionado.
- El [Component Documentation](../../components/readme/documentation/README.md) describe la función de agrupar documentos importantes, con ejemplos de Architecture, ADR, Roadmap, API y Deployment; son ejemplos, no una prueba de que todos esos tipos deban existir en cualquier proyecto.
- No se identificó un apartado literal `## Documentation`; los enlaces están distribuidos entre los apartados técnicos del README. La falta de ese título por sí sola **no demuestra ausencia** de la Responsibility.

### Evidence

- [README — enlaces y organización](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Guía PostgreSQL](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)
- [Guía de integración PostgreSQL](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md)
- [Component Documentation](../../components/readme/documentation/README.md)
- [Exploración documental original](only-film-required-readme-batch-2.md)

### Evaluation Rationale — propuesta

El README ofrece rutas concretas y referencias útiles en sus secciones temáticas. Esta distribución puede funcionar para lectores que avanzan por tareas, pero todavía se necesita valorar si resulta **localizable y suficientemente completa** para lectores nuevos. No se verificaron todos los enlaces internos y externos ni se evaluó toda la documentación del árbol para establecer un inventario exhaustivo. La clasificación `Partial` permanece como propuesta.

### Uncertainty

- ¿Puede un colaborador localizar con rapidez arquitectura, configuración, pruebas, seguridad y políticas del repositorio?
- ¿Existen enlaces obsoletos, documentos importantes sin referencia o duplicidades que afecten al uso?
- ¿La navegación por secciones temáticas es suficiente o convendría un índice de documentos?
- ¿Los tipos de documentación que no existen corresponden a necesidades reales del proyecto o son solo ejemplos genéricos del Component?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** todavía no se ha revisado la suficiencia de navegación y enlaces; ni el título no canónico ni la distribución justifican por sí solos `ADD` o `ADAPT`.

## 5. Responsibility: README-FOOTER

**Requirement Level:** `Required`.

**Proposed State:** `Partial` — sin aprobación.

**Proposed Applicability:** `Applicable` — sin aprobación.

**Implementation Characteristics (proposed):** `Own`, `Equivalent`: material de créditos, origen y licencia distribuido en los últimos apartados y la línea final del README.

### Detected Facts

- El [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) termina con una sección `Origen, créditos y evolución` que reconoce la procedencia del proyecto académico colaborativo [certidevs/g1_testing](https://github.com/certidevs/g1_testing), lista contribuyentes del equipo original y aclara que la evolución posterior no implica autoría exclusiva del trabajo original.
- A continuación presenta `Próximas líneas de evolución`, separando posibles ampliaciones de funcionalidades ya implantadas.
- La última línea contiene una nota de `Licencia` que remite a la documentación y repositorio original; afirma expresamente que este README no establece una licencia adicional por sí mismo.
- El [Component Footer](../../components/readme/footer/README.md) define el Footer como última sección y señala que **puede** incluir licencia, agradecimientos, enlaces relacionados y contacto. No exige incluir los cuatro elementos.
- La nota de licencia **no constituye** por sí misma un análisis de permisos de reutilización, licenciamiento del código o titularidad de derechos. No se ha realizado esa evaluación.

### Evidence

- [README — origen, créditos, evolución y nota final](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Component Footer](../../components/readme/footer/README.md)
- [Exploración documental original](only-film-required-readme-batch-2.md)
- [Repositorio académico referenciado](https://github.com/certidevs/g1_testing) — referencia externa, no inspeccionada como parte del commit fijado

### Evaluation Rationale — propuesta

El final del README contiene elementos propios de un Footer y reconoce correctamente **en el texto documental** la procedencia colaborativa sin atribución exclusiva. La nota sobre licencia es cautelosa, pero su existencia no demuestra la claridad jurídica para terceros ni resuelve condiciones de reutilización. Un reviewer debe valorar si la ubicación y estructura final son suficientes para la Responsibility documental, separando esa decisión de cualquier revisión legal.

### Uncertainty

- ¿Los créditos son completos, correctos y adecuados al contexto del proyecto?
- ¿La nota sobre licencia resulta comprensible para un visitante sin crear una apariencia de licencia concedida que no está acreditada?
- ¿El contenido final cumple la función de Footer o necesita una separación explícita respecto de roadmap y evolución?
- ¿Son necesarios otros enlaces o una vía de contacto para la audiencia del repositorio?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** aún no se ha validado la suficiencia editorial del bloque de cierre ni la situación de licencia; no se ejecuta ninguna modificación de créditos o avisos legales.

## 6. Revisión transversal del lote y gates de aprobación humana

| Gate | Condición de revisión | Estado |
| --- | --- | --- |
| RTF-1 | Confirmar el propósito y aplicabilidad de las tres responsabilidades Required al consumidor | Pendiente de reviewer |
| RTF-2 | Validar la exactitud de los principales elementos del stack y distinguir entornos | Parcial; se contrastaron Java, Spring Boot y PostgreSQL |
| RTF-3 | Comprobar usabilidad y vigencia de enlaces relevantes de documentación | Pendiente |
| RTF-4 | Evaluar crédito y función de Footer, sin equiparar nota de licencia a autorización de uso | Pendiente |
| RTF-5 | Aprobar o corregir `State`, `Applicability`, Implementation Characteristics y rationale por ficha | Pendiente |
| RTF-6 | Resolver `Decision Status` y eventual Adoption Decision solo con justificación humana | Pendiente |

## 7. Situación de las ocho Required

| Responsibility Required | Propuesta E3 disponible | ¿Aprobación E3? |
| --- | --- | --- |
| `README-HERO` | [Hero, Overview y Features](only-film-required-identity-semantic-review.md) | No |
| `README-OVERVIEW` | [Hero, Overview y Features](only-film-required-identity-semantic-review.md) | No |
| `README-FEATURES` | [Hero, Overview y Features](only-film-required-identity-semantic-review.md) | No |
| `README-TECH-STACK` | Este documento | No |
| `README-QUICK-START` | [Quick Start y Changelog](only-film-required-semantic-review.md) | No |
| `README-DOCUMENTATION` | Este documento | No |
| `README-FOOTER` | Este documento | No |
| `DOC-CHANGELOG` | [Quick Start y Changelog](only-film-required-semantic-review.md) — hipótesis sin discriminar | No |

Con este lote existen **propuestas E3 para las ocho responsabilidades Required**, pero `DOC-CHANGELOG` aún no cuenta con un `State` formal elegido. No se ha aprobado ninguna evaluación semántica ni una Adoption Decision.

## 8. Conclusión

El lote ofrece trazabilidad de los tres componentes, evidencias y criterios explícitos para el reviewer. La cobertura documental global permanece **28/28**, las decisiones de adopción permanecen pendientes y el Assessment continúa `In Progress`.

**No se ha ejecutado el proyecto, verificado jurídicamente su licencia ni modificado el repositorio consumidor.**
