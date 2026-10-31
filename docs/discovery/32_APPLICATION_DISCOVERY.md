# 32 — Application Discovery

## 1. Propósito

Este documento investiga cómo extender Existing Repository Adoption más allá del Assessment Core entregado en v0.7.0.

La pregunta central es:

> ¿Qué condiciones debe cumplir GitHub Framework para aplicar de forma selectiva, segura y verificable una Adoption Decision sobre un repositorio existente sin destruir implementaciones válidas ni introducir automatización prematura?

Este documento es Discovery. No define todavía arquitectura final, Delivery Scope, Sprint, milestone ni target version.

---

## 2. Contexto

v0.7.0 soporta:

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

Application Discovery comienza después de esa frontera.

---

## 3. Boundary heredado

La nueva investigación considera:

```text
REPORT
    ↓
APPLY
    ↓
VERIFY
```

sin asumir todavía que APPLY deba significar mutación directa de `main`.

Assessment sigue siendo útil de forma independiente.

---

## 4. Initial Discovery Scope

Se investigan:

```text
APPLY

VERIFY

selective application

safe modification

conflict handling

rollback

idempotency
```

Quedan fuera de esta Discovery inicial:

```text
CLI
GitHub Actions
automatic remediation
continuous synchronization
schema
manifest
repository generation
```

---

## 5. Assessment vs Application

Hipótesis inicial:

```text
Assessment produces understanding

Application produces change
```

Por tanto:

```text
Assessment Result
    ≠
Applied Change

Adoption Decision
    ≠
repository mutation
```

---

## 6. Candidate Application Flow

Primer flujo candidato:

```text
ASSESS
    ↓
DECIDE
    ↓
REPORT
    ↓
SELECT
    ↓
PLAN
    ↓
REVIEW
    ↓
APPLY
    ↓
VERIFY
```

---

## 7. Selective Application

Application no debe asumir:

```text
apply every Adoption Decision
```

Debe permitir seleccionar una Responsibility concreta y aplicar solamente el cambio justificado.

---

## 8. Safe Modification

Principio candidato:

> Minimum necessary change over canonical replacement.

Application debe reconciliar el consumer con la Responsibility esperada, no convertir automáticamente el repository a una forma física canónica.

---

## 9. Candidate Physical Operations

Clasificación inicial:

```text
CREATE
MODIFY
EXTEND
REORGANIZE
NO CHANGE
```

Operaciones potencialmente más riesgosas:

```text
DELETE
REPLACE
MOVE
RENAME
```

Estas últimas no se consideran inicialmente respaldadas.

---

## 10. Responsibility vs Physical Change

Se mantiene:

```text
Responsibility
    semantic unit
```

pero Application necesita una unidad operacional.

Hipótesis:

```text
Application Intent
    ↓
Change Set
        ↓
individual physical Changes
```

---

## 11. Conflict Handling

Un conflicto no equivale automáticamente a fallo.

Debe distinguirse:

```text
detectable conflict
    ≠
automatically resolvable conflict
```

Los conflictos semánticos requieren revisión humana.

---

## 12. Verification

VERIFY debe comprobar al menos:

```text
intended effect

unintended effect

preservation
```

y, cuando proceda, volver a evaluar la Responsibility afectada.

---

## 13. Rollback

Rollback no implica necesariamente un motor propio del Framework.

Antes de mutar debe existir un camino de recuperación conocido.

Debe distinguirse entre:

```text
discard candidate state
```

y:

```text
post-integration rollback
```

---

## 14. Idempotency

Propiedad candidata:

> Repeating the same bounded Application Intent should not duplicate or corrupt state.

Todavía no se considera requisito universal.

---

## 15. Preliminary Safety Properties

```text
selective
scope-bounded
reviewed
conflict-aware
verifiable
recoverable
idempotent where appropriate
non-destructive by default
```

Hipótesis:

```text
Adoption Decision
    ≠
Application Plan

Application Plan
    ≠
Applied Change

Applied Change
    ≠
Verified Outcome
```

---

## 16. Consumer Experiment Design

Consumer seleccionado:

```text
fran-eliot/dental-back-spring
```

Motivo:

- assessment completo previo;
- 28 Responsibilities evaluadas;
- incluye casos ADAPT y ADD;
- permite reutilizar Evidence ya disponible.

---

## 17. Experiment Case A — README-QUICK-START

Assessment histórico:

```text
Responsibility
    README-QUICK-START

State
    Partial

Applicability
    Applicable

Adoption Decision
    ADAPT
```

Evidence histórica:

- `cd backend`;
- backend documentado en `localhost:3000`;
- configuración real `server.port=8080`.

---

## 18. Experiment Case B — DOC-CHANGELOG

Assessment histórico:

```text
Responsibility
    DOC-CHANGELOG

State
    Missing

Applicability
    Applicable

Adoption Decision
    ADD
```

No existía `CHANGELOG.md` ni equivalente observado.

---

## 19. Evidence Freshness

Discovery introduce una nueva necesidad:

```text
assessment-time evidence
    may become stale
before
application-time mutation
```

Por tanto, Application debe refrescar Evidence antes de mutar.

---

## 20. RC-A01 — Refresh Evidence before mutation

> Before mutating Application, refresh relevant consumer evidence enough to confirm the planned change still applies.

---

## 21. RC-A02 — Current state overrides stale assumptions

Si current Evidence contradice Application Plan:

```text
STOP
    ↓
REPLAN
```

La realidad actual del consumer prevalece.

---

## 22. RC-A03 — Scope follows semantic outcome

El scope físico debe seguir el resultado semántico de la Responsibility, no límites arbitrarios de sección o archivo.

---

## 23. Refined Candidate Flow

```text
Resolved Adoption Decision
    ↓
SELECT
    ↓
REFRESH EVIDENCE
    ↓
CONFIRM DECISION STILL APPLIES
    ↓
DEFINE APPLICATION INTENT
    ↓
BUILD CHANGE SET
    ↓
CHECK CONFLICTS
    ↓
REVIEW
    ↓
APPLY
    ↓
VERIFY
```

Posibles salidas:

```text
NO CHANGE
DEFER
REPLAN
REJECT
ROLLBACK
```

---

## 24. Evidence Refresh — README-QUICK-START

Estado actual confirmado antes de mutación:

```text
main
    e17b009602f25da0d6f32920180254eb9392fee2

README
    contains "cd backend"

README
    contains localhost:3000 twice

application.properties
    server.port=8080
```

También se confirmó que el backend está en la raíz y no existe directorio `backend/`.

---

## 25. Application Plan A

Application Intent:

> Align documented backend execution instructions with current repository structure and runtime configuration while preserving valid consumer documentation.

Candidate Change Set:

```text
A1
    remove "cd backend"

A2
    localhost:3000
        →
    localhost:8080

A3
    localhost:3000/swagger-ui/index.html
        →
    localhost:8080/swagger-ui/index.html
```

Risk:

```text
LOW
documentation-only
```

---

## 26. Plan A Preservation Scope

Preservar:

```text
all unrelated README content
requirements
frontend instructions
source code
runtime configuration
repository structure
```

---

## 27. Plan A Review Result

```text
READY FOR EXPERIMENTAL APPLY
```

sujeto a una última comprobación del estado actual.

---

## 28. Application Plan B

Responsibility:

```text
DOC-CHANGELOG
```

Intent:

> Add a minimal evidence-backed changelog without inventing historical releases.

Problema detectado:

```text
ADD
    does not answer
what initial history is justified
```

---

## 29. Application Readiness

Discovery introduce:

```text
Application Readiness
```

distinto de:

```text
Decision Status
```

Un Decision Status resuelto no implica automáticamente una Application lista para ejecutar.

---

## 30. Experimental APPLY — Case A

Rama:

```text
experiment/adoption-application-quick-start
```

Commit:

```text
6706d6dd6d9c4952fe7f8192eb07922b2ac82f4f
```

Mensaje:

```text
docs(readme): align backend execution instructions
```

---

## 31. Case A Physical Result

Diff:

```diff
-cd backend

-http://localhost:3000
+http://localhost:8080

-http://localhost:3000/swagger-ui/index.html
+http://localhost:8080/swagger-ui/index.html
```

Resultado:

```text
1 file changed
2 additions
3 deletions
```

Solo cambió `README.md`.

---

## 32. Case A Verification

```text
"cd backend"
    absent

"localhost:3000"
    0 occurrences

"localhost:8080"
    2 occurrences
```

Además:

```text
README backend port
    =
application.properties server.port
    =
8080
```

---

## 33. Case A Idempotency

Una segunda aplicación equivalente produciría:

```text
NO CHANGE
```

Resultado:

```text
Operational Idempotency
    PASS
```

para este Change Set.

---

## 34. Case A Preservation

```text
Scope Preservation
    PASS
```

No se modificaron:

- source code;
- configuration;
- repository structure;
- contenido no relacionado.

---

## 35. Experimental PR Boundary

PR experimental:

```text
#1
docs(readme): align backend execution instructions
```

Estado observado:

```text
open
mergeable
not merged
```

Esto separa:

```text
candidate change
```

de:

```text
stable consumer state
```

---

## 36. RC-A04 — Preserve outside Change Set

> Application should preserve existing consumer content and repository state outside the explicitly approved Change Set.

Confidence:

```text
SUPPORTED
```

por primer experimento real.

---

## 37. RC-A05 — Review before stable integration

> Application should remain reviewable before affecting stable consumer state.

Git branch + commit + Pull Request demostraron una forma operacional de lograrlo.

---

## 38. APPLY vs INTEGRATE

Discovery introduce una separación:

```text
APPLY
    produce isolated candidate state

VERIFY
    inspect candidate state

INTEGRATE
    accept candidate into stable state
```

INTEGRATE queda todavía por investigar.

---

## 39. Recovery Refinement

Antes de Integration:

```text
DISCARD
```

puede eliminar candidate state sin revertir `main`.

Después de Integration:

```text
ROLLBACK / REVERT
```

sería otro problema distinto.

---

## 40. Evidence Refresh — DOC-CHANGELOG

Se comprobó:

- no `CHANGELOG.md`;
- no equivalente evidente;
- `pom.xml` en `0.0.1-SNAPSHOT`;
- historial de commits real, pero sin release history fiable.

Por tanto, no existe base para reconstruir releases pasadas.

---

## 41. Case B Safe Content Decision

La opción segura es:

```text
forward-looking changelog
without invented historical releases
```

Primera implementación experimental:

```markdown
# Changelog

## [Unreleased]

No unreleased changes documented yet.
```

---

## 42. Consumer Convention Finding

Review detectó que el consumer documenta predominantemente en español.

La primera versión del changelog, aunque físicamente correcta, no preservaba esa convención.

Se refinó a:

```markdown
# Historial de cambios

## [Sin publicar]

Aún no hay cambios sin publicar documentados.
```

---

## 43. RC-A06 — Preserve consumer conventions

> Application should preserve relevant observable conventions of the consumer unless the approved Application Intent explicitly requires changing them.

Puede incluir:

```text
language
terminology
artifact naming
documentation tone
repository-local structure
```

---

## 44. RC-A07 — Review may refine Application

> A successfully applied Change Set may still require bounded refinement when review identifies a consumer-specific mismatch not captured during planning.

Esto distingue:

```text
physical correctness
```

de:

```text
consumer fit
```

---

## 45. Experimental APPLY — Case B

Rama:

```text
experiment/adoption-application-changelog
```

Commits:

```text
f00fac8770fa70d455f51cf31dd10d6951732a81
c209c82965f4510fef8a60df5210ce75c7689439
```

El segundo commit alinea idioma y convenciones con el consumer.

---

## 46. Case B Verification

Resultado final:

```text
CHANGELOG.md
    present

other files changed
    none

invented historical releases
    no

consumer language
    preserved

second equivalent application
    NO CHANGE
```

---

## 47. Case B Outcome

```text
DOC-CHANGELOG

Before
    Missing

After
    candidate Satisfied
```

Resultado experimental:

```text
CREATE
    PASS

Scope Preservation
    PASS

Consumer Convention Preservation
    PASS

Operational Idempotency
    PASS
```

---

## 48. ADAPT vs ADD Comparison

```text
ADAPT / MODIFY
    existing implementation
    protect existing useful content

ADD / CREATE
    no implementation
    protect against invented or duplicate content
```

Ambos reutilizan:

```text
Evidence Refresh
Application Intent
Change Set
Preservation Scope
Review
APPLY
VERIFY
```

---

## 49. Multi-dimensional VERIFY

VERIFY no puede reducirse a:

```text
operation succeeded
```

Debe considerar:

```text
Physical Verification
Intent Verification
Preservation Verification
Semantic Verification
```

---

## 50. Refinement Loop

El segundo experimento produjo:

```text
APPLY
    ↓
VERIFY
    ↓
REVIEW
    ↓
REFINE
    ↓
VERIFY AGAIN
```

sin necesidad de una nueva Adoption Decision.

---

## 51. Emerging Application Core

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
BUILD BOUNDED CHANGE SET
    ↓
IDENTIFY PRESERVATION SCOPE
    ↓
CHECK CONFLICTS
    ↓
REVIEW PLAN
    ↓
APPLY IN ISOLATION
    ↓
VERIFY
    ↓
REVIEW RESULT
    ↓
REFINE if necessary
    ↓
VERIFY AGAIN
    ↓
INTEGRATE
```

Posibles salidas:

```text
NO CHANGE
DEFER
REPLAN
REJECT
DISCARD
ROLLBACK
```

---

## 52. Supported by Current Evidence

Directamente soportado:

```text
Evidence Refresh
Application Intent
bounded Change Set
scope preservation
isolated Application
physical verification
preservation verification
review before integration
MODIFY
CREATE
```

---

## 53. Provisionally Supported

```text
Application Readiness
Consumer Convention Preservation
review-driven refinement
operational idempotency
Change Set as explicit operational concept
INTEGRATE as distinct stage
```

---

## 54. Conceptually Supported but Unvalidated

```text
conflict resolution
post-integration rollback
failed APPLY
failed VERIFY
concurrent modification
multi-file structural transformation
DELETE
MOVE
RENAME
```

---

## 55. Deferred

```text
CLI
GitHub Actions
automatic remediation
continuous reassessment
Structured Data
Schema
Manifest
fully autonomous application
repository generation
```

---

## 56. Preliminary Requirements

```text
AR-01
    Refresh Evidence before mutation

AR-02
    Current state overrides stale assumptions

AR-03
    Define explicit Application Intent

AR-04
    Use bounded Change Sets

AR-05
    Preserve state outside approved Change Set

AR-06
    Preserve relevant consumer conventions

AR-07
    Review before stable integration

AR-08
    Verify intended and unintended effects

AR-09
    Allow bounded refinement before integration

AR-10
    Prefer idempotent operations where practical
```

---

## 57. First Delivery Readiness Evaluation

Evaluation criteria:

```text
Observed Need
Repeated Evidence
Operational Feasibility
Representation Stability
Proportional Complexity
```

Initial result:

```text
Observed Need
    PASS

Repeated Evidence
    PARTIAL PASS

Operational Feasibility
    PASS

Representation Stability
    PARTIAL PASS

Proportional Complexity
    PASS
```

---

## 58. Initial Readiness Result

```text
Application Core Candidate
    NOT YET READY
    FOR DELIVERY SCOPE DEFINITION
```

Principal gap:

```text
2 operation types
1 consumer
```

---

## 59. Required Next Evidence

El gap mínimo es:

```text
repeat Application Core
on an additional consumer
without material redesign
```

Esto da lugar a:

```text
34_APPLICATION_REPEATABILITY_EXPERIMENT.md
```

---

## 60. Discovery Principle — No Mutation is valid

La investigación ya indica que safe Application no implica siempre mutación.

Un outcome:

```text
NO CHANGE
```

puede ser correcto cuando Evidence actual no justifique cambio.

Este principio será probado explícitamente en Repeatability.

---

## 61. Discovery Boundary

Application continúa siendo:

```text
optional downstream capability
```

Assessment no queda incompleto si Application no se ejecuta.

---

## 62. Discovery Status

```text
Application model
    HOLDS on first consumer

Delivery readiness
    NOT YET ESTABLISHED

Repeatability
    REQUIRED
```

---

## 63. Current Experimental PR State

En `dental-back-spring`:

```text
PR #1
    ADAPT / MODIFY
    open
    mergeable
    not integrated

PR #2
    ADD / CREATE
    open
    mergeable
    not integrated
```

Los PR se mantienen como Evidence experimental y no como cambios integrados.

---

## 64. Next Step

Crear:

```text
33_APPLICATION_DISCOVERY_SYNTHESIS.md
```

para separar:

```text
supported
provisional
unvalidated
deferred
```

y evaluar formalmente si el Application Core Candidate necesita Repeatability adicional antes de Delivery Scope.
