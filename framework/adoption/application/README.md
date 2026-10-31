# Existing Repository Adoption — Application Guide

La capability **Existing Repository Adoption — Application Core** proporciona una guía reutilizable para aplicar de forma selectiva, segura, revisable y verificable una Adoption Decision ya resuelta sobre un repositorio existente.

Application es una capability downstream del Assessment Core.

No sustituye:

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

sino que parte de su resultado.

---

## 1. Propósito

Application responde a una pregunta distinta del Assessment.

Assessment responde:

> ¿Cómo está cubierta actualmente una Responsibility y qué Adoption Decision corresponde?

Application responde:

> ¿Cómo puede llevarse una Adoption Decision resuelta a un candidate state verificable sin destruir implementaciones válidas ni introducir cambios no justificados?

El objetivo es producir Application:

```text
evidence-backed
bounded
reviewable
preserving
verifiable
```

No es un mecanismo de:

```text
automatic remediation
repository normalization
canonical replacement
automatic merge
```

---

## 2. Relación con Assessment

El Assessment Core produce, entre otros:

```text
Responsibility
Requirement Level
State
Applicability
Implementation Characteristics
Evidence
Evaluation Rationale
Decision Status
Adoption Decision
Decision Rationale
```

Application consume una Responsibility cuya decisión está:

```text
Decision Status
    Resolved
```

La relación conceptual es:

```text
Assessment
    produces understanding and decision
        ↓
Application
    plans and applies justified change
```

Por tanto:

```text
Assessment Outcome
    ≠
Application Plan

Adoption Decision
    ≠
repository mutation
```

---

## 3. Application es opcional

Un Assessment puede completarse sin ejecutar Application.

```text
Assessment Complete
    does not require
Application
```

Application es una capability:

```text
optional downstream capability
```

y no una condición para considerar completo el Assessment Core.

---

## 4. Boundary del Application Core

El proceso soportado es:

```text
Resolved Adoption Decision
    ↓
SELECT
    ↓
REFRESH EVIDENCE
    ↓
CONFIRM DECISION
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

La frontera del Application Core termina en:

```text
verified candidate state
```

No incluye:

```text
INTEGRATE
```

Por tanto, mergear un Pull Request o convertir el candidate state en stable consumer state pertenece a una fase posterior y queda fuera de este delivery.

---

## 5. Core Principles

### 5.1 Evidence before Mutation

Antes de mutar un consumer debe comprobarse su estado actual.

```text
Assessment-time Evidence
    may become stale
before
Application-time mutation
```

Por tanto:

```text
REFRESH EVIDENCE
    before
APPLY
```

### 5.2 Reconciliation over Replacement

Application debe preservar las implementaciones válidas del consumer y aplicar el cambio mínimo necesario.

```text
reconcile
    before
replace
```

La existencia de una implementación no canónica no justifica por sí sola reemplazarla.

### 5.3 Responsibility over Artifact

La unidad semántica sigue siendo:

```text
Responsibility
```

No:

```text
File
```

Application puede modificar uno o varios artifacts para satisfacer una única Responsibility.

### 5.4 Bounded Change

Toda mutación debe estar limitada por un:

```text
Change Set
```

que identifique qué puede cambiar.

### 5.5 Preservation

El estado válido fuera del Change Set debe preservarse.

### 5.6 Human Review

La revisión humana permanece explícita antes de mutar y antes de considerar válido el candidate state.

### 5.7 No Mutation is a Valid Outcome

Application segura puede terminar en:

```text
NO CHANGE
```

cuando la Evidence actual no justifique una mutación.

---

## 6. SELECT

SELECT identifica qué Responsibility y qué Adoption Decision resuelta se desea llevar a Application.

Application no debe asumir:

```text
apply all resolved Decisions
```

La selección puede ser:

```text
one Responsibility
one bounded Application scope
```

Esto permite adopción incremental y revisable.

---

## 7. REFRESH EVIDENCE

Antes de planificar una mutación debe compararse el estado actual del consumer con la Evidence del Assessment.

Debe registrarse, como mínimo:

```text
Current Facts
Current Evidence
Differences from Assessment
Evidence Freshness Result
```

El objetivo es responder:

> ¿Sigue siendo válida la base factual sobre la que se tomó la Adoption Decision?

---

## 8. Current State takes precedence

Si current Evidence contradice assumptions históricas:

```text
STOP
    ↓
REPLAN
```

La realidad actual del consumer prevalece sobre el Assessment histórico.

Application no debe:

```text
blindly execute stale plan
```

---

## 9. Evidence Refresh Outcomes

Evidence Refresh puede concluir:

```text
current state still supports Application
```

o:

```text
NO CHANGE
REPLAN
DEFER
```

También puede recomendar un nuevo Assessment cuando la realidad actual contradiga materialmente el Assessment utilizado como origen.

---

## 10. Application Intent

Toda Application debe declarar un:

```text
Application Intent
```

antes de definir cambios físicos.

Application Intent responde:

> ¿Qué resultado debe producir esta Application si se ejecuta correctamente?

Ejemplo:

```text
Align backend execution documentation
with current runtime configuration
while preserving valid README content.
```

No es suficiente:

```text
Edit README.md
```

porque describe una acción física, no el outcome esperado.

---

## 11. Intent vs Change Set

Debe mantenerse:

```text
Application Intent
    ≠
Change Set
```

Application Intent es semántico.

Change Set es operacional.

---

## 12. Application Plan

Antes de APPLY debe existir un plan explícito.

Como mínimo:

```text
Application Context
Selected Responsibility
Current Assessment Outcome
Evidence Refresh
Application Intent
Candidate Change Set
Preservation Scope
Risk / Conflict Notes
Verification Plan
```

El plan debe poder revisarse sin ejecutar todavía ninguna mutación.

---

## 13. Change Set

Change Set representa:

```text
approved operational mutation boundary
```

Debe permitir distinguir:

```text
what may change

from

what must remain unchanged
```

Puede contener una o varias modificaciones físicas.

---

## 14. Supported Operations

El Application Core soporta como operaciones evidenciadas:

```text
CREATE
MODIFY
```

### CREATE

Crear un artifact ausente cuando exista Evidence suficiente y una Adoption Decision que justifique añadirlo.

### MODIFY

Modificar de forma bounded un artifact existente para alinear su contenido con Application Intent.

---

## 15. Unsupported Operations

No forman parte del Application Core actual:

```text
DELETE
MOVE
RENAME
```

Tampoco:

```text
automatic replacement
repository-wide normalization
```

Estas operaciones requieren Evidence y Delivery Scope adicionales antes de poder considerarse soportadas.

---

## 16. No automatic mapping Decision → Operation

No existe una regla automática:

```text
ADAPT
    ⇒
MODIFY

ADD
    ⇒
CREATE
```

Aunque esas combinaciones hayan aparecido en Evidence real, la operación se determina durante Application Planning.

Debe mantenerse:

```text
Adoption Decision
    ≠
physical operation
```

---

## 17. Preservation Scope

Preservation Scope registra qué debe permanecer sin cambios.

Puede incluir:

```text
unrelated content
repository structure
valid consumer implementation
artifact location
language
terminology
documentation style
verified historical information
```

Preservation Scope debe ser compatible con Application Intent.

No puede proteger exactamente aquello que Application Intent necesita cambiar.

---

## 18. Consumer Conventions

Application debe preservar convenciones observables del consumer cuando sean relevantes.

Ejemplos:

```text
language
terminology
naming
documentation style
repository-local organization
```

La preservación de convenciones no implica convertirlas en un schema formal.

Se documentan dentro de Preservation Scope cuando resulten materialmente relevantes.

---

## 19. Risk / Conflict Notes

El Application Plan debe disponer de un espacio para registrar riesgos o conflictos.

Ejemplos:

```text
stale assumptions
target changed since Assessment
equivalent implementation appeared
unsupported historical information
consumer convention mismatch
overlapping Change Set
```

---

## 20. Conflict Handling

Un conflicto no equivale automáticamente a error.

Debe distinguirse:

```text
conflict detected
    ≠
conflict automatically resolvable
```

El Application Core puede:

```text
detect
record
stop
replan
defer
```

pero no intenta:

```text
automatic semantic conflict resolution
```

---

## 21. REVIEW PLAN

Antes de APPLY, el plan debe revisarse.

Review debe comprobar al menos:

```text
current Evidence is sufficient
Intent is explicit
Change Set is bounded
Preservation Scope is clear
unsupported facts are not invented
risks are understood
Verification Plan is feasible
```

---

## 22. Plan Review Result

Plan Review puede terminar en:

```text
PROCEED
NO CHANGE
REPLAN
DEFER
REJECTED
```

Solo:

```text
PROCEED
```

permite continuar a APPLY.

---

## 23. Unsupported Facts must not be invented

Application no debe introducir hechos no respaldados por Evidence.

Esto incluye:

```text
versions
release dates
historical events
configuration values
repository structure
consumer conventions
```

La ausencia de Evidence no debe rellenarse mediante suposiciones.

---

## 24. APPLY IN ISOLATION

Cuando exista mutación, debe ejecutarse sobre:

```text
isolated candidate state
```

y no directamente sobre:

```text
stable consumer state
```

---

## 25. Branch-based isolation

Una Git branch es un mecanismo válido de aislamiento.

Ejemplo:

```text
main
    stable state

feature/application-change
    candidate state
```

El Application Core no obliga a una única implementación futura de isolation.

---

## 26. Direct mutation of stable state

No debe utilizarse como modelo normal:

```text
modify main directly
```

El objetivo de isolation es mantener el candidate state:

```text
reviewable
discardable
verifiable
```

antes de Integration.

---

## 27. Application Result

Después de Plan Review y, cuando corresponda, APPLY, debe registrarse:

```text
APPLIED
NO CHANGE
REPLAN
DEFER
REJECTED
```

### APPLIED

El Change Set fue ejecutado sobre candidate state.

### NO CHANGE

No se requiere o no se justifica mutación.

### REPLAN

La Evidence actual invalida materialmente el plan.

### DEFER

La Application puede seguir siendo válida, pero no puede ejecutarse todavía con seguridad.

### REJECTED

El plan no debe continuar.

---

## 28. APPLY does not imply success

Debe mantenerse:

```text
Applied Change
    ≠
Verified Outcome
```

Que un diff exista no demuestra que Application Intent se haya cumplido.

---

## 29. Verification Plan

Verification Plan debe definirse antes de APPLY.

Debe responder:

```text
What should change?
What should remain unchanged?
How will Application Intent be checked?
What Evidence indicates PASS?
What would require REFINE?
What would indicate FAIL?
```

---

## 30. VERIFY

VERIFY evalúa el candidate state después de APPLY.

Debe comprobar:

```text
expected changes
preservation
Application Intent
consumer fit
```

---

## 31. Physical Verification

Physical Verification comprueba:

```text
expected artifact exists
expected text changed
expected path changed
unexpected files did not change
```

Es necesaria, pero no suficiente.

---

## 32. Intent Verification

Intent Verification responde:

> ¿El candidate state produce realmente el outcome definido por Application Intent?

Ejemplo:

```text
backend documentation
    now matches
runtime configuration
```

---

## 33. Preservation Verification

Preservation Verification comprueba:

```text
state outside approved Change Set
    remained unchanged
```

y que las convenciones relevantes del consumer continúan preservadas.

---

## 34. Semantic Verification

Cuando resulte necesario, VERIFY puede re-evaluar la Responsibility afectada.

Ejemplo:

```text
Before
    State = Partial

Candidate State
    re-evaluated as Satisfied
```

Esto no debe convertirse en una certificación automática.

---

## 35. Verification Result

VERIFY produce:

```text
PASS
REFINE
FAIL
```

### PASS

Candidate state satisface Application Intent dentro de la Evidence disponible.

### REFINE

El cambio es esencialmente válido pero requiere un ajuste bounded.

### FAIL

Application Intent no se satisface o Preservation Scope ha sido violado.

---

## 36. Refinement Loop

Cuando Verification Result sea:

```text
REFINE
```

puede ejecutarse:

```text
VERIFY
    ↓
REFINE
    ↓
VERIFY AGAIN
```

El refinement debe permanecer:

```text
bounded
consistent with original Intent
inside approved scope
```

No requiere una nueva Adoption Decision salvo que nueva Evidence cambie materialmente el problema original.

---

## 37. NO CHANGE

NO CHANGE es un resultado válido.

Puede producirse cuando:

```text
current state already satisfies Intent
```

o:

```text
current Evidence
does not justify mutation
```

NO CHANGE no significa:

```text
Application failed
```

---

## 38. REPLAN

REPLAN indica que la base del plan ya no es válida.

Ejemplos:

```text
consumer changed
target no longer exists
equivalent implementation appeared
assumption was incorrect
```

REPLAN debe ocurrir antes de forzar una mutación basada en información obsoleta.

---

## 39. DEFER

DEFER se utiliza cuando:

```text
Intent remains potentially valid
```

pero falta Evidence o una condición necesaria para ejecutar con seguridad.

Ejemplo:

```text
release history should be completed
but no published release evidence exists
```

---

## 40. REJECTED

REJECTED se utiliza cuando el Application Plan no debe continuar.

Puede deberse a:

```text
unsupported scope
unsafe operation
invalid assumption
conflict with current Delivery Scope
```

---

## 41. DISCARD

Antes de Integration, el candidate state puede descartarse.

```text
APPLY IN ISOLATION
    ↓
VERIFY
    ↓
FAIL
    ↓
DISCARD
```

Esto es distinto de:

```text
post-integration rollback
```

---

## 42. Integration Boundary

El Application Core no define:

```text
merge policy
merge strategy
required approvals
branch protection behavior
release interaction
post-merge verification
post-merge rollback
```

Puede utilizarse un Pull Request como ejemplo de:

```text
reviewable candidate state
```

pero mergear ese Pull Request pertenece a:

```text
INTEGRATE
```

y queda fuera de este delivery.

---

## 43. Idempotency

Application debe considerar qué ocurriría si el mismo Intent se evaluara de nuevo sobre el estado resultante.

Safety property:

> Reapplying an already-satisfied bounded intent should not introduce duplicate or unintended changes.

El Core no afirma:

```text
all Application operations
are universally idempotent
```

---

## 44. Application Readiness

Application Readiness puede utilizarse como concepto descriptivo para indicar si existe suficiente Evidence para continuar.

Valores candidatos:

```text
READY
NOT READY
DEFERRED
```

Este vocabulario permanece provisional y no constituye un schema formal.

---

## 45. Application Template

El artifact reutilizable para registrar una Application es:

```text
framework/adoption/application/application-template.md
```

La relación es:

```text
Application Guide
    explains
        how and why

Application Template
    records
        what is planned
        what was applied
        what was verified
```

---

## 46. Recommended Application Flow

```text
1. Select one resolved Responsibility
        ↓
2. Refresh current Evidence
        ↓
3. Confirm the Decision still applies
        ↓
4. Define Application Intent
        ↓
5. Build bounded Change Set
        ↓
6. Define Preservation Scope
        ↓
7. Record Risks / Conflicts
        ↓
8. Define Verification Plan
        ↓
9. Review Plan
        ↓
10. PROCEED or stop safely
        ↓
11. APPLY in isolated candidate state
        ↓
12. VERIFY
        ↓
13. PASS / REFINE / FAIL
        ↓
14. Preserve verified candidate state
```

---

## 47. Example A — ADAPT / MODIFY

Assessment:

```text
Responsibility
    README-QUICK-START

State
    Partial

Decision Status
    Resolved

Adoption Decision
    ADAPT
```

Current Evidence:

```text
README
    contains stale backend instructions

runtime config
    exposes backend on port 8080
```

Application Intent:

```text
Align backend execution documentation
with current runtime configuration
while preserving unrelated README content.
```

Change Set:

```text
MODIFY
    README backend instructions only
```

Expected outcome:

```text
APPLIED
    ↓
VERIFY
    ↓
PASS
```

---

## 48. Example B — ADD / CREATE

Assessment:

```text
Responsibility
    DOC-CHANGELOG

State
    Missing

Decision Status
    Resolved

Adoption Decision
    ADD
```

Evidence:

```text
no changelog observed
no reliable historical releases available
```

Application Intent:

```text
Add a minimal forward-looking changelog
without inventing historical releases.
```

Change Set:

```text
CREATE
    CHANGELOG.md
```

Review may detect consumer conventions, such as language, and produce:

```text
APPLIED
    ↓
VERIFY
    ↓
REFINE
    ↓
VERIFY AGAIN
    ↓
PASS
```

---

## 49. Example C — ADAPT / NO CHANGE

Assessment:

```text
Responsibility
    DOC-CHANGELOG

State
    Partial

Decision Status
    Resolved

Adoption Decision
    ADAPT
```

Current Evidence:

```text
consumer already has
specialized changelog governance

no Git tags observed

no GitHub Releases observed

published version history
cannot be verified
```

Safe outcome:

```text
Change Set
    NONE

Application Result
    NO CHANGE / REPLAN
```

This is a valid Application result.

---

## 50. Safety Checklist

Antes de APPLY:

- [ ] Responsibility seleccionada explícitamente.
- [ ] Decision Status es `Resolved`.
- [ ] Evidence actualizada.
- [ ] Application Intent explícito.
- [ ] Change Set bounded o ausencia de Change Set justificada.
- [ ] Preservation Scope identificado.
- [ ] Riesgos y conflictos revisados.
- [ ] No se inventan facts.
- [ ] Verification Plan definido.
- [ ] Plan Review permite `PROCEED`.

Después de APPLY:

- [ ] Candidate state aislado.
- [ ] Expected changes verificados.
- [ ] Preservation verificada.
- [ ] Application Intent verificado.
- [ ] Consumer conventions revisadas cuando sean relevantes.
- [ ] Verification Result registrado.
- [ ] Refinement re-verificado si fue necesario.
- [ ] Candidate state descartable antes de Integration.

---

## 51. Out of Scope

El Application Core no implementa ni define procedimientos estables para:

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

CLI
GitHub Actions

parser
schema
Structured Data contract
Application Manifest

continuous reassessment
drift detection

post-integration rollback
repository generation
```

Tampoco convierte Existing Repository Adoption en una nueva Component family.

---

## 52. Representation Boundary

La representación del Application Core es:

```text
Markdown
```

y debe permanecer:

```text
human-readable
human-editable
Git-reviewable
usable without tooling
```

No constituye:

```text
formal schema
typed contract
machine API
```

---

## 53. Operational Summary

```text
Resolved Adoption Decision
        ↓
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
NO CHANGE / REPLAN / DEFER / REJECTED
        or
        ↓
APPLY IN ISOLATION
        ↓
VERIFY
        ↓
PASS / REFINE / FAIL
        ↓
Verified or Discarded Candidate State
```

---

## 54. References

La evidencia, Delivery Scope e Implementation Plan del Application Core se encuentran en:

```text
docs/discovery/32_APPLICATION_DISCOVERY.md
docs/discovery/33_APPLICATION_DISCOVERY_SYNTHESIS.md
docs/discovery/34_APPLICATION_REPEATABILITY_EXPERIMENT.md
docs/discovery/35_APPLICATION_DELIVERY_SCOPE.md
docs/discovery/36_APPLICATION_IMPLEMENTATION_PLAN.md
```

El Assessment Core permanece documentado en:

```text
framework/adoption/README.md
framework/adoption/assessment-template.md
```

El Application Template se implementa separadamente en:

```text
framework/adoption/application/application-template.md
```
