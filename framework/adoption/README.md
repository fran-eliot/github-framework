# Existing Repository Adoption

La capability **Existing Repository Adoption** proporciona una guía reutilizable para evaluar un repositorio existente frente a las Responsibilities definidas por un Repository Template de GitHub Framework y, opcionalmente, llevar una Adoption Decision resuelta hasta un candidate state verificado.

El delivery actual se divide en dos capabilities:

```text
Existing Repository Adoption
    Assessment Core
        ↓
    optional Application Core
```

El Assessment Core permite analizar, evaluar, revisar y documentar decisiones de adopción.

El Application Core permite planificar, aplicar de forma aislada y verificar cambios justificados sin convertir la capability en un mecanismo de automatic remediation o Integration.

---

## 1. Propósito

Existing Repository Adoption responde a un problema distinto de la creación de un repositorio nuevo.

Un repositorio existente puede:

- implementar ya una Responsibility mediante un artifact canónico;
- satisfacerla mediante una implementación equivalente;
- distribuirla entre varios artifacts;
- cubrirla parcialmente;
- no implementarla;
- no necesitarla en su contexto.

Por tanto, Existing Repository Adoption se basa en:

```text
reconciliation
```

y no en:

```text
generation
replacement
automatic remediation
```

El objetivo del Assessment Core es producir una evaluación:

```text
usable
repeatable
traceable
reviewable
persistent
```

manteniendo explícita la revisión humana.

---

## 2. Alcance

El proceso soportado es:

```text
ANALYZE
    ↓
ASSESS
    ↓
REVIEW
    ↓
DECIDE
    ↓
REPORT
```

El resultado es un assessment Markdown persistente que conserva:

```text
Detected Facts
Evidence
Evaluation
Uncertainty
Adoption Decisions
Rationale
```

El Assessment Core no modifica el consumer repository.

Cuando una Adoption Decision está resuelta, el Application Core puede utilizarse opcionalmente para continuar con:

```text
SELECT
    ↓
REFRESH EVIDENCE
    ↓
DEFINE APPLICATION INTENT
    ↓
PLAN
    ↓
REVIEW PLAN
    ↓
APPLY IN ISOLATION
    ↓
VERIFY
    ↓
REVIEW RESULT
```

La frontera del Application Core termina en un verified candidate state. `INTEGRATE` permanece fuera del alcance actual.

---

## 3. Inputs del Assessment

Todo assessment parte de cuatro inputs conceptuales:

```text
Existing Consumer Repository

Repository Template

Repository Template Version

Consumer Reference
```

### Existing Consumer Repository

Es el repositorio que se desea evaluar.

Actúa como:

```text
evidence source
```

### Repository Template

Es el Repository Template seleccionado como referencia para el assessment.

Actúa como:

```text
assessment baseline
```

### Repository Template Version

Identifica la versión concreta del Template utilizada.

El assessment debe interpretarse siempre respecto a esa versión.

### Consumer Reference

Identifica el estado concreto del consumer evaluado.

Puede ser, por ejemplo:

```text
branch
commit SHA
tag
```

La referencia debe ser suficientemente precisa para evitar interpretar un assessment histórico como válido automáticamente para cualquier estado futuro del repositorio.

---

## 4. Principios del Assessment

### 4.1 Evidence before Automation

El Assessment Core prioriza evidencia explícita y revisión humana antes de cualquier automatización futura.

```text
Evidence
    before
Automation
```

### 4.2 Responsibility over File

La unidad de evaluación es:

```text
Responsibility
```

y no:

```text
File
```

Por tanto:

```text
Canonical Artifact Missing
    ≠
Responsibility Missing
```

Una Responsibility puede estar satisfecha mediante una implementación no canónica.

### 4.3 Human Review remains explicit

El assessment mantiene separadas las observaciones, la evaluación y la decisión:

```text
Detected Fact
    ≠
Evaluated State
    ≠
Adoption Decision
```

Una comprobación determinista puede aportar Evidence, pero no sustituye la evaluación semántica.

### 4.4 Reconciliation over Replacement

Existing Repository Adoption debe interpretar primero lo que el consumer ya hace.

No debe asumir que la ausencia de una estructura canónica obliga a reemplazar una solución existente.

---

## 5. Modelo del Assessment

Por cada Responsibility se registran y evalúan las siguientes dimensiones:

```text
Responsibility
Requirement Level
Detected Facts
Evidence
State
Applicability
Implementation Characteristics
Uncertainty
Evaluation Rationale
Decision Status
Adoption Decision
Decision Rationale
```

Estas dimensiones no deben colapsarse entre sí.

En particular:

```text
State
    ≠
Applicability
    ≠
Adoption Decision
```

---

## 6. Proceso

### 6.1 ANALYZE

El objetivo de ANALYZE es identificar información observable del consumer.

Se registran:

```text
Detected Facts
Evidence
```

sin decidir todavía qué acción de adopción corresponde.

Ejemplos de Detected Facts:

```text
README.md exists

docs/ directory is absent

OpenAPI configuration exposes API documentation

repository-level LICENSE file is not present
```

Un Detected Fact debe ser verificable.

No debe contener una conclusión semántica.

```text
Fact
    ≠
Evaluation
```

### 6.2 ASSESS

El objetivo de ASSESS es interpretar la Evidence respecto a la Responsibility.

Se evalúan:

```text
State
Applicability
Implementation Characteristics
Uncertainty
Evaluation Rationale
```

### 6.3 REVIEW

El objetivo de REVIEW es comprobar que la evaluación es defendible.

La revisión debe considerar:

```text
evidence sufficiency
semantic interpretation
non-canonical implementations
uncertainty
applicability
```

La revisión es especialmente importante cuando una Responsibility está implementada mediante estructuras distintas de las previstas canónicamente por el Template.

### 6.4 DECIDE

El objetivo de DECIDE es registrar si puede cerrarse una decisión y, cuando sea posible, cuál es la disposición adecuada.

Se registran:

```text
Decision Status
Adoption Decision
Decision Rationale
```

### 6.5 REPORT

El assessment completo se conserva como:

```text
persistent Markdown outcome
```

El mismo artifact puede funcionar como:

```text
working assessment
+
review artifact
+
persistent report
```

No se requiere un Generated Report separado.

---

## 7. Detected Facts

Detected Facts contienen observaciones verificables sobre el consumer.

Deben describir:

```text
what exists
what does not exist
what configuration is present
what repository structure is observable
```

No deben expresar:

```text
whether the Responsibility is satisfied
what should be changed
which Adoption Decision should be selected
```

---

## 8. Evidence

Evidence vincula el assessment con material observable del consumer.

Puede referenciar:

```text
file paths
repository sections
configuration
source code
generated documentation
repository structure
```

La regla general es:

```text
minimal sufficient evidence
```

Debe conservarse evidencia suficiente para que otra persona pueda revisar la evaluación sin copiar innecesariamente grandes cantidades de contenido del consumer.

---

## 9. Responsibility State

State representa únicamente:

```text
current responsibility coverage
```

El vocabulario estable es:

### `Satisfied`

La Responsibility está suficientemente cubierta en el consumer.

Esto puede ocurrir mediante una implementación canónica o no canónica.

### `Partial`

La Responsibility está cubierta solo parcialmente.

Puede existir implementación relevante, pero falta parte de la cobertura necesaria.

### `Missing`

La Responsibility no está cubierta por la Evidence observada.

State no representa:

```text
future action
applicability
priority
```

---

## 10. Applicability

Applicability indica si una Responsibility resulta pertinente para el consumer concreto.

El vocabulario estable es:

### `Applicable`

La Responsibility es relevante para el consumer.

### `Not Applicable`

La Responsibility no resulta necesaria en el contexto evaluado.

### `Uncertain`

No existe evidencia o contexto suficiente para determinar todavía su aplicabilidad.

Applicability debe evaluarse independientemente de State.

Por ejemplo:

```text
State
    Missing

Applicability
    Not Applicable

Decision
    OMIT
```

es un resultado válido.

---

## 11. Implementation Characteristics

Implementation Characteristics permite describir implementaciones no canónicas cuando esta información ayuda a interpretar correctamente una Responsibility.

El vocabulario provisional observado durante Discovery es:

```text
Canonical
Own
Equivalent
Specialized
Distributed
```

Este vocabulario es:

```text
provisional
descriptive
non-exclusive
```

Una Responsibility puede presentar:

```text
zero
one
or several
```

Implementation Characteristics.

Estas categorías ayudan a describir cómo está materializada una Responsibility, especialmente cuando la implementación difiere de la materialización canónica esperada por el Repository Template.

No constituyen una taxonomía cerrada ni un contrato de conformance.

Por tanto:

```text
Implementation Characteristic
    supports interpretation
```

pero no determina por sí sola:

```text
State
Applicability
Adoption Decision
```

La Evidence y el Evaluation Rationale deben conservar el contexto necesario para interpretar cualquier Implementation Characteristic utilizada.

---

## 12. Evaluación de Documentación

La presencia física de documentación no demuestra por sí sola que una Responsibility esté satisfecha.

Debe mantenerse la regla:

```text
Documentation Exists
    ≠
Responsibility Satisfied
```

Según la Responsibility, la evaluación puede requerir revisar:

```text
presence
correctness
coverage
current relevance
```

Un archivo existente pero incorrecto, incompleto u obsoleto puede producir un State distinto de `Satisfied`.

---

## 13. Uncertainty

Uncertainty debe registrar, cuando corresponda:

```text
what is unknown
why it cannot currently be resolved
what evidence would resolve it
```

No se utilizan:

```text
confidence score
probability
Low / Medium / High
```

La incertidumbre debe expresarse mediante información concreta y revisable.

---

## 14. Evaluation Rationale

Evaluation Rationale responde:

> ¿Por qué la Evidence observada conduce al State, Applicability e interpretación registrados?

Debe explicar la evaluación sin anticipar la acción futura.

Por tanto:

```text
Evaluation Rationale
    explains the assessment
```

mientras:

```text
Decision Rationale
    explains the adoption decision
```

Ambos conceptos deben permanecer separados.

---

## 15. Decision Status

Decision Status indica si una Adoption Decision puede cerrarse en el momento del assessment.

El vocabulario estable es:

### `Resolved`

Existe evidencia y contexto suficiente para registrar una Adoption Decision.

### `Needs Further Evaluation`

La decisión no puede cerrarse de forma segura con la información disponible.

Decision Status:

```text
is not
an Adoption Decision
```

Cuando una Responsibility requiere evaluación adicional, deben conservarse:

```text
Evidence
Uncertainty
Evaluation Rationale
reason for unresolved decision
```

sin forzar una Adoption Decision ficticia.

---

## 16. Adoption Decisions

El vocabulario estable de Adoption Decision es:

```text
PRESERVE
ADAPT
ADD
ACCEPT
OMIT
```

### `PRESERVE`

Mantener la implementación existente porque satisface adecuadamente la Responsibility y no requiere modificación para el propósito evaluado.

### `ADAPT`

Modificar una implementación existente para cubrir adecuadamente la Responsibility.

### `ADD`

Añadir una implementación o artifact necesario porque la Responsibility requiere cobertura adicional.

### `ACCEPT`

Aceptar conscientemente una implementación existente no canónica cuando resulta adecuada para la Responsibility y el contexto.

### `OMIT`

No incorporar la materialización esperada porque la Responsibility no resulta aplicable o existe una razón explícita y revisada para omitirla.

---

## 17. No existe mapeo automático State → Decision

Una misma combinación de State y Applicability puede conducir a distintas decisiones según:

```text
Requirement Level
Implementation Characteristics
Evidence
Context
Rationale
```

Por tanto:

```text
State
    +
Requirement Level
    +
Applicability
    +
Implementation Characteristics
    +
Evidence
    +
Context
    +
Rationale
        ↓
Adoption Decision
```

No deben aplicarse reglas automáticas como:

```text
Satisfied → PRESERVE

Partial → ADAPT

Missing → ADD
```

sin evaluación contextual.

---

## 18. `EVALUATE`

`EVALUATE` no forma parte del vocabulario estable de Adoption Decision.

La necesidad que anteriormente representaba se expresa mediante:

```text
Decision Status
    Needs Further Evaluation
```

Esto permite conservar una Responsibility evaluada sin inventar una disposición final.

---

## 19. `JUSTIFY`

`JUSTIFY` tampoco forma parte del vocabulario estable de Adoption Decision.

La necesidad de conservar justificación queda cubierta mediante:

```text
Evaluation Rationale
+
Decision Rationale
```

No se requiere una decisión adicional para representar que una conclusión necesita estar razonada.

---

## 20. Decision Rationale

Decision Rationale responde:

> ¿Por qué esta Adoption Decision es apropiada dado el assessment?

Debe relacionar la decisión con:

```text
State
Applicability
Implementation Characteristics
Evidence
context
```

sin convertir esas dimensiones en reglas automáticas.

Ejemplos válidos:

```text
Satisfied
+
Equivalent
+
ACCEPT
```

y:

```text
Missing
+
Not Applicable
+
OMIT
```

---

## 21. Assessment Completion

Un assessment puede marcarse:

```text
Complete
```

cuando todas las Responsibilities definidas por el Repository Template seleccionado hayan sido evaluadas.

Cada Responsibility debe disponer de:

```text
State
Applicability
Evidence
Evaluation Rationale
Decision Status
```

Cuando:

```text
Decision Status
    Resolved
```

deben existir además:

```text
Adoption Decision
Decision Rationale
```

Cuando:

```text
Decision Status
    Needs Further Evaluation
```

deben existir:

```text
Uncertainty
rationale explaining
why the decision remains unresolved
```

---

## 22. Complete no significa Fully Resolved

Debe mantenerse:

```text
Assessment Complete
    ≠
All Adoption Decisions Resolved
```

Un assessment puede estar completo aunque contenga Responsibilities con:

```text
Needs Further Evaluation
```

si la incertidumbre y el motivo de la decisión no resuelta están correctamente documentados.

`Complete` describe que el assessment ha recorrido todas las Responsibilities previstas.

No certifica que todas las decisiones estén cerradas.

---

## 23. Human Review

Existing Repository Adoption Assessment registra una evaluación humana trazable.

No constituye:

```text
automated certification
```

La revisión debe comprobar especialmente:

- suficiencia de Evidence;
- coherencia entre Evidence y State;
- independencia entre State y Applicability;
- reconocimiento de implementaciones equivalentes o distribuidas;
- incertidumbre no resuelta;
- coherencia entre evaluación y Adoption Decision;
- suficiencia de Evaluation Rationale y Decision Rationale.

Una validación futura podrá asistir en comprobaciones deterministas, pero no sustituye la revisión semántica definida por este Assessment Core.

---

## 24. Uso del Assessment Template

El artifact reutilizable para registrar el assessment es:

```text
framework/adoption/assessment-template.md
```

La relación entre ambos artifacts es:

```text
Guide
    explains
        how and why

Template
    records
        what was assessed
```

Flujo recomendado:

```text
1. Copy the Assessment Template
        ↓
2. Complete Assessment Context
        ↓
3. ANALYZE each Responsibility
        ↓
4. ASSESS State and Applicability
        ↓
5. REVIEW Evidence and interpretation
        ↓
6. DECIDE or mark Needs Further Evaluation
        ↓
7. Complete the Assessment Conclusion
        ↓
8. Preserve the assessment as the reviewable outcome
```

El Framework no impone en este delivery:

```text
consumer storage path
mandatory completed-assessment filename
```

---

## 25. Resultado Persistente

El assessment completado debe conservar suficiente contexto para ser interpretado posteriormente.

Como mínimo debe poder identificarse:

```text
Consumer Repository
Consumer Reference
Repository Template
Template Version
Assessment Date
Assessment Status
```

El resultado persistente documenta:

```text
what was observed
how it was evaluated
what remains uncertain
what decisions were made
why those decisions were made
```

---

## 25.1 Application Core

El Application Core reutilizable se documenta en:

```text
framework/adoption/application/README.md
```

El artifact para registrar una Application concreta es:

```text
framework/adoption/application/application-template.md
```

La relación entre ambos cores es:

```text
Assessment Core
    understands and decides
        ↓
optional Application Core
    plans, applies in isolation and verifies
```

Application consume una Adoption Decision con:

```text
Decision Status
    Resolved
```

y conserva como principios:

```text
Evidence before Mutation
Reconciliation over Replacement
Responsibility over Artifact
Bounded Change
Preservation
Human Review
No Mutation is a Valid Outcome
```

El Application Core soporta:

```text
CREATE
MODIFY
NO CHANGE
REPLAN
DEFER
REJECTED
```

y Verification Results:

```text
PASS
REFINE
FAIL
```

---

## 26. Out of Scope

Existing Repository Adoption no documenta ni implementa procedimientos estables para:

```text
INTEGRATE

automatic merge
automatic remediation
automatic semantic assessment
automatic Adoption Decisions
automatic semantic conflict resolution

DELETE
MOVE
RENAME

component installation

CLI
parser
schema
Structured Data contract
Adoption Manifest

Framework Validator integration
GitHub Actions integration

repository generation

continuous reassessment
drift detection

post-integration rollback
```

Tampoco convierte Existing Repository Adoption en una nueva Component family.

Este delivery no requiere:

```text
metadata.yml
Component Catalog integration
mandatory metadata contract
```

Las capacidades excluidas podrán volver a Discovery si aparece evidencia suficiente que justifique su incorporación.

---

## 27. Límites de Interpretación

Existing Repository Adoption Assessment debe evitar las siguientes inferencias automáticas:

```text
file exists
    ⇒
Responsibility Satisfied
```

```text
canonical file missing
    ⇒
Responsibility Missing
```

```text
State
    ⇒
Adoption Decision
```

```text
assessment complete
    ⇒
all decisions resolved
```

```text
assessment result
    ⇒
automatic conformance certification
```

Cada conclusión debe permanecer respaldada por Evidence y rationale explícitos.

---

## 28. Resumen Operativo

El Assessment Core puede resumirse como:

```text
Existing Consumer Repository
        +
Repository Template
        ↓
ANALYZE
        ↓
ASSESS
        ↓
REVIEW
        ↓
DECIDE
        ↓
REPORT
        ↓
Persistent Human-Reviewed Assessment
```

La secuencia conceptual por Responsibility es:

```text
Detected Facts
        ↓
Evidence
        ↓
State
+
Applicability
+
Implementation Characteristics
+
Uncertainty
        ↓
Evaluation Rationale
        ↓
Decision Status
        ↓
Adoption Decision
        ↓
Decision Rationale
```

cuando la decisión puede resolverse.

Si no puede resolverse:

```text
Decision Status
    Needs Further Evaluation

+
Uncertainty

+
Rationale
```

sin forzar una Adoption Decision.

---

## 29. Referencias

La definición y planificación del Assessment Core se encuentran en:

```text
docs/discovery/29_ADOPTION_DELIVERY_SCOPE.md
docs/implementation/30_ADOPTION_IMPLEMENTATION_PLAN.md
```

La definición y planificación del Application Core se encuentran en:

```text
docs/discovery/35_APPLICATION_DELIVERY_SCOPE.md
docs/discovery/36_APPLICATION_IMPLEMENTATION_PLAN.md
```

La evidencia experimental que fundamenta esta capability permanece en:

```text
docs/discovery/
```

Los artifacts reutilizables de Existing Repository Adoption se integran en:

```text
framework/adoption/
```
