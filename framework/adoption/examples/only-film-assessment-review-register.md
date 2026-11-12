# Only Film — Assessment Evidence-Gap and Human Review Register

## 1. Objetivo, fuentes y estado

Este documento consolida los siguientes pasos de revisión del Assessment de `fran-eliot/only_film` según `TPL-BACKEND` 0.1.0. No añade nuevas exploraciones: convierte los resultados ya documentados en un registro de **verificaciones pendientes, prioridades de revisión y condiciones para tomar decisiones justificadas**.

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Exploration Coverage | 28/28 Responsibilities |
| Semantic Review Completed | **No acreditada** |
| Operational Verification | **No ejecutada en este Assessment** |
| Adoption Decisions | **Ninguna resuelta** |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |

**Primera verificación E2:** [Quick Start y CI en el commit fijado](only-film-pinned-quickstart-ci-verification.md). Incluye revisión de Docker/Compose/variables y una ejecución GitHub Actions satisfactoria del SHA evaluado; no cierra el Quick Start reproducible ni las decisiones semánticas.

**Fuentes de partida:** [matriz de cobertura](only-film-assessment-coverage.md), [walkthrough de Quick Start y Testing](only-film-two-responsibilities.md), [lotes Required](only-film-required-readme-batch-1.md), [lote Required restante](only-film-required-readme-batch-2.md), [Recommended README](only-film-recommended-readme-batch.md), [Recommended Documentation](only-film-recommended-documentation-batch.md), [Optional governance](only-film-optional-readme-governance.md), [Optional showcase](only-film-optional-showcase-diagrams.md) y [Optional technical](only-film-optional-technical-batch.md).

El inventario al 100 % **solo significa que hay un punto de partida documental para cada Responsibility**. No es un resultado de conformidad ni permite escribir `State: Satisfied` para ninguna de ellas.

## 2. Distinción entre niveles de evidencia

| Nivel | Pregunta | Situación |
| --- | --- | --- |
| **E0 — Contract inventory** | ¿Se ha identificado cada Responsibility y su requirement level? | 28/28 inventariadas |
| **E1 — Documentary exploration** | ¿Existen Detected Facts y enlaces a fuentes del consumer? | 28/28 exploradas |
| **E2 — Evidence quality review** | ¿Se han comprobado suficiencia, trazabilidad, actualidad y límites por Responsibility? | Pendiente de revisión explícita |
| **E3 — Semantic assessment** | ¿Se han razonado `State`, `Applicability` e `Evaluation Rationale` con un reviewer? | No acreditado |
| **E4 — Adoption Decision review** | ¿Hay decisión y justificación humana cuando `Decision Status: Resolved`? | No realizado; pueden quedar decisiones sin resolver |
| **E5 — Application/Integration** | ¿Existe autorización para cambios y posterior integración? | Fuera de alcance; **no autorizado** |

E2/E3 no exigen ejecutar el software para **todas** las Responsibilities. Sí exigen identificar cuándo una afirmación sobre operatividad o seguridad depende de resultados técnicos que no están disponibles. El `Assessment Template` permite `Complete` con decisiones todavía `Needs Further Evaluation`, siempre que la evaluación exigida y las razones de la incertidumbre estén documentadas para cada Responsibility.

## 3. Review gates transversales

Antes de incorporar un resultado semántico al [Assessment Template](../assessment-template.md), el reviewer debe comprobar:

1. **Contrato fijado:** `TPL-BACKEND` 0.1.0 y requirement level exacto; no confundirlo con la prioridad de la metadata de un Component.
2. **Fuente concreta:** ruta o URL enlazada al commit `28d75a50e0a178954dd46acc23300d9dd327843c`; indicar si solo se inspeccionó la existencia del archivo o también su contenido.
3. **Hechos vs. inferencias:** distinguir lo observado de lo declarado por el README, una auditoría histórica o una configuración sin ejecutar.
4. **Freshness:** comprobar la fecha/base de auditorías internas y no trasladar automáticamente sus conclusiones al commit evaluado ni a `main` actual.
5. **Equivalencia:** comprobar responsabilidad implementada de forma distribuida o alternativa antes de concluir `Missing` por ausencia de un nombre canónico.
6. **Revisión semántica:** registrar `State`, `Applicability`, `Implementation Characteristics`, `Uncertainty`, `Evidence` y `Evaluation Rationale` con justificación explícita.
7. **Decisión:** solo registrar `PRESERVE / ADAPT / ADD / ACCEPT / OMIT` cuando la decisión esté revisada; si no, `Needs Further Evaluation` y `—`, con incertidumbre y razón.
8. **Cierre global:** no marcar `Assessment Complete` hasta revisar todas las Responsibilities conforme a la guía y plantilla. `28/28` de exploración **no cumple esta condición**.

**Actualización Quick Start:** la [comprobación específica de Compose](only-film-compose-evidence-gap.md) delimita qué verifica `postgres-schema` y qué queda sin acreditar del smoke `docker compose up --build`, con criterios Q1–Q8 de reproducción. La laguna sigue abierta.

**Verificación E2 de DOC-CHANGELOG:** el [examen de versiones, historial Git y fuentes de releases](only-film-changelog-evidence-review.md) confirma que no hay Changelog identificable por nombre en el árbol inspeccionado, el endpoint de Releases devolvió una lista vacía y los tags **no pudieron comprobarse**. La revisión semántica de la Responsibility continúa pendiente.

**Reconciliación E2 de Testing y seguridad:** la [revisión de código fijado y checks CI](only-film-security-testing-reconciliation.md) contrasta los hallazgos de auditorías históricas con controladores, configuración y tests disponibles en el SHA del consumidor, distinguiendo patrones corregidos de verificación operativa todavía no acreditada.

**Actualización E2 de casos negativos:** el [registro de pruebas de seguridad y selectores](only-film-negative-security-test-evidence.md) concreta casos de autorización, CSRF, validación de archivos y su inclusión en el job H2, dejando pendiente la verificación individual de Surefire y la evaluación semántica.

**Nueva evidencia E2 de Testing:** la [lectura de logs Surefire y Sonar del SHA fijado](only-film-verified-surefire-sonar-logs.md) confirma 329 tests H2 sin fallos/errores/omisiones, resultados por clase, generación y publicación histórica de JaCoCo y análisis Sonar ejecutado. Los artefactos no aparecen ahora disponibles, no hay porcentaje de cobertura verificado y Quality Gate/Selenium permanecen pendientes. Las lagunas del registro se interpretan conforme a esta comprobación más reciente.

**Inicio de revisión semántica E3:** la [propuesta de evaluación de README-TESTING y DOC-TESTING](only-film-testing-semantic-review.md) conserva `Partial`/`Applicable` como hipótesis sujetas a reviewer y registra el identificador CE de SonarCloud sin fingir un Quality Gate histórico. Los 329 tests H2 verificados no implican aprobación del Assessment.

**Propuesta E3 para DOC-SECURITY:** la [revisión semántica provisional](only-film-security-semantic-review.md) reúne fuentes históricas, código del commit fijado y resultados individuales de pruebas de seguridad. Propone `Partial` / `Applicable` como hipótesis explícitamente pendiente de reviewer, sin resolver la Adoption Decision.

**Revisión semántica E3 de Required:** la [propuesta para README-QUICK-START y DOC-CHANGELOG](only-film-required-semantic-review.md) evalúa evidencias y límites; Quick Start conserva `Partial` provisional, mientras que Changelog requiere discriminar `Missing` frente a `Partial` tras verificar fuentes alternativas y tags. Ninguna hipótesis está aprobada ni resuelve Adoption Decisions.

**Revisión semántica E3 de identidad y funcionalidades:** la [propuesta para README-HERO, README-OVERVIEW y README-FEATURES](only-film-required-identity-semantic-review.md) contrasta las descripciones del consumer con los Components del Framework y formula hipótesis editoriales sujetas a aprobación, sin resolver Adoption Decisions.

**Último lote E3 de Required:** la [propuesta semántica de Tech Stack, Documentation y Footer](only-film-required-final-semantic-review.md) completa las fichas de interpretación de las ocho Required, todas pendientes de reviewer. El caso DOC-CHANGELOG sigue con hipótesis de State por discriminar; no hay decisiones aprobadas.

**Propuesta E3 de Recommended README:** la [revisión semántica de Status, Architecture y Repository Structure](only-film-recommended-readme-semantic-review.md) distingue badges tecnológicos de estado/madurez, contrasta el flujo arquitectónico con una auditoría histórica y evalúa el árbol resumido, dejando todas las hipótesis pendientes de reviewer.

## 4. Bloqueos prioritarios de evidencia

La prioridad indica **orden sugerido para revisar incertidumbres**, no severidad comprobada del proyecto ni obligación de aplicar un cambio.

| Prioridad | Responsibility | Laguna concreta | Próxima verificación / evidencia suficiente para revisión |
| --- | --- | --- | --- |
| P1 | `README-QUICK-START` (Required) | El ejemplo conserva `State: Partial` provisional; no se ha reproducido el arranque | Ejecutar en **entorno aislado y desechable** el procedimiento de Docker/Maven para el SHA fijado, registrar versiones, pasos, salida y restricciones; decidir si la evidencia es suficiente |
| P1 | `DOC-CHANGELOG` (Required) | No aparece nombre canónico en el árbol; se desconoce fuente equivalente de cambios publicados | Examinar releases/tags y otros registros históricos de ese estado; identificar la fuente oficial y su alcance, sin inferir `Missing` solo por el nombre |
| P1 | `README-TESTING` (Recommended) y `DOC-TESTING` (Recommended) | Guías y workflows localizados, pero no hay resultados reproducidos en este Assessment | Asociar a SHA una ejecución identificada o reproducir un conjunto representativo; separar H2, PostgreSQL, Selenium y cobertura JaCoCo sin extrapolar métricas |
| P1 | `DOC-SECURITY` (Optional) | La auditoría de octubre se refiere a un commit anterior; no prueba el estado del SHA evaluado | Reconciliar hallazgos históricos con código y verificaciones fechadas; no etiquetar riesgos como vigentes ni cerrar hallazgos sin nueva evidencia |
| P2 | `DOC-ARCHITECTURE` (Recommended) | Auditorías de arquitectura y fases con bases históricas distintas | Identificar la descripción arquitectónica vigente en el SHA; contrastar al menos las fronteras declaradas con fuentes de código relevantes |
| P2 | `DOC-PROJECT-STATUS` (Recommended) y `README-STATUS` (Recommended) | Madurez y estado provienen de auditorías históricas y badges de tecnología | Localizar la fuente operativa de estado/hitos en ese momento; diferenciar indicadores vigentes, planes y auditorías históricas |
| P2 | `README-LICENSE` (Optional) y `README-AUTHOR` (Optional) | Referencia a proyecto académico original, permisos sin dictamen | Revisar procedencia, atribuciones y condiciones autorizadas; no asignar licencias ni hacer afirmaciones jurídicas sin autorización |
| P2 | `DOC-DEPLOYMENT` (Optional) | Se observó Compose local, no un procedimiento de operación de producción | Determinar primero entorno objetivo y aplicabilidad; diferenciar pruebas de arranque local y requisitos de despliegue real |
| P2 | `DOC-API` (Optional) | El README anuncia REST API futura; hay controladores MVC | Confirmar si existe interfaz contractual pública que documentar; no confundir controladores MVC con una REST API publicada |

Estos gates son **propuestas para el reviewer**, no tareas realizadas ni resultados de tests.

## 5. Registro de revisión del resto de Responsibilities

Para evitar que las responsabilidades con indicios favorables queden implícitamente aprobadas, se reservan revisiones explícitas:

| Grupo | Responsibilities | Pregunta de revisión principal |
| --- | --- | --- |
| Identidad y producto | `README-HERO`, `README-OVERVIEW`, `README-FEATURES`, `README-HIGHLIGHTS` | ¿Presentan el producto y sus capacidades con claridad y afirmaciones sustentadas? |
| Stack y navegación | `README-TECH-STACK`, `README-DOCUMENTATION`, `README-REPOSITORY-STRUCTURE` | ¿Coinciden con fuentes del commit y permiten orientarse sin omisiones materiales? |
| Final y contribución | `README-FOOTER`, `README-CONTRIBUTING`, `README-ROADMAP` | ¿Son adecuados los créditos, el acceso a contribuciones y la comunicación de cambios previstos para el consumidor objetivo? |
| Descripción arquitectónica | `README-ARCHITECTURE`, `DOC-ADR`, `DOC-DIAGRAMS` | ¿Es clara y actual la representación arquitectónica? ¿Aporta valor un registro de decisiones o un diagrama? |
| Demostración | `README-DEMO` | ¿Son suficientes las capturas o se requiere una demo reproducible? |
| Datos | `DOC-DATABASE` | ¿Están explicadas las migraciones, invariantes y relaciones necesarias, con evidencia vigente? |
| Referencias | `DOC-REFERENCES` | ¿Hay fuentes externas críticas que necesiten mantenimiento o índice centralizado? |

Cada fila agrupa preguntas para organizar la sesión, **no** sustituye el registro individual de cada Responsibility en el Assessment.

## 6. Secuencia sugerida para el reviewer

**Paso 1 — revisión de integridad (E2).** Comprobar enlaces, referencias inmutables, naturaleza de las fuentes y discrepancias de fecha. Dejar registradas las carencias sin reinterpretarlas como `Missing`.

**Paso 2 — decidir qué requiere verificación técnica.** Priorizar Quick Start y Testing por su dependencia de ejecución real. Para seguridad, arquitectura y persistencia, contrastar afirmaciones importantes con fuentes del SHA fijado antes de aceptar resultados heredados.

**Paso 3 — valorar cada Responsibility (E3).** Completar en el [Assessment Template](../assessment-template.md) `State`, `Applicability`, `Evidence`, `Evaluation Rationale` y `Decision Status`; mantener la incertidumbre cuando exista. Revisar `Optional` individualmente, sin declarar `Not Applicable` por defecto.

**Paso 4 — resolver solo lo justificado (E4).** Un reviewer puede seleccionar una Adoption Decision si existe evidencia suficiente y justificación. Las demás permanecen `Needs Further Evaluation` con decisión `—` y seguimiento explícito.

**Paso 5 — conclusión.** Reconciliar las 28 fichas con los criterios de cierre de la guía. Incluso si el Assessment llegase a `Complete`, ello no implica que todas las decisiones estén resueltas ni autoriza automáticamente Application/Integration.

## 7. Registro de revisión (para completar, sin aprobaciones implícitas)

| Campo | Valor actual |
| --- | --- |
| Reviewer | Pendiente de designación |
| Fecha de revisión | Pendiente |
| Evidence refresh / SHA | Pendiente de verificación adicional |
| E2 — Quality review | Pendiente |
| E3 — Semantic review | Pendiente |
| E4 — Resolved decisions | Ninguna acreditada |
| Siguiente sesión | Revisión de referencias y selección de pruebas reproducibles |
| Assessment Status | `In Progress` |

El documento es un **instrumento de revisión** del Framework; no modifica el consumidor, no crea por sí solo un plan de Application y no representa una revisión humana ya realizada.
