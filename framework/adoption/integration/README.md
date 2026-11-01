# Existing Repository Adoption — Integration Guide

La capability **Existing Repository Adoption — Integration Core** proporciona una guía reutilizable para integrar de forma manual, revisable y verificable un verified candidate state en el stable state de un consumer repository.

Integration es una capability downstream del Application Core.

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
APPLY IN ISOLATION
    ↓
VERIFY
```

sino que parte de su resultado.

---

## 1. Propósito

Integration responde a una pregunta distinta de Assessment y Application.

Assessment responde:

> ¿Cómo está cubierta actualmente una Responsibility y qué Adoption Decision corresponde?

Application responde:

> ¿Cómo puede llevarse una Adoption Decision resuelta a un candidate state verificable?

Integration responde:

> ¿Cómo puede aceptarse ese verified candidate state en el stable consumer state respetando la governance del repositorio y verificando después el resultado estable?

El objetivo es producir una Integration:

```text
governance-aware
reviewable
traceable
preserving
verifiable
```

No es un mecanismo de:

```text
automatic merge
automatic approval
automatic conflict resolution
automatic rollback
release orchestration
```

---

## 2. Relación con Application

Application Core produce:

```text
verified candidate state
```

Integration consume ese resultado.

La relación conceptual es:

```text
Application
    produces
        verified candidate
            ↓
Integration
    evaluates and accepts
        stable mutation
```

Por tanto:

```text
Applied Change
    ≠
Integrated Change

Verified Candidate
    ≠
Verified Stable State
```

---

## 3. Integration es opcional

Application puede completarse sin ejecutar Integration.

```text
Application Complete
    does not require
Integration
```

Integration es:

```text
optional downstream capability
```

y no una condición para considerar completo el Application Core.

---

## 4. Boundary del Integration Core

El proceso soportado es:

```text
Verified Candidate State
    ↓
REFRESH STABLE BASE
    ↓
EVALUATE DRIFT
    ↓
CHECK INTEGRATION CONDITIONS
    ↓
REVIEW
    ↓
INTEGRATE
    ↓
VERIFY STABLE STATE
    ↓
CONFIRM
```

La frontera termina en:

```text
verified stable state
```

o en un estado seguro de parada:

```text
DEFERRED
REPLAN REQUIRED
REJECTED
RECOVERY REQUIRED
```

No incluye release o deployment lifecycle posterior.

---

## 5. Core Principles

### 5.1 Verified Candidate before Integration

Integration comienza únicamente desde un candidate state ya verificado.

```text
unverified candidate
    must not
enter Integration
```

### 5.2 Refresh Stable Base

Antes de integrar debe comprobarse el estado actual del stable target.

### 5.3 Evaluate Drift Impact

Que el stable base haya avanzado no implica automáticamente REPLAN.

Debe evaluarse el impacto real.

### 5.4 Consumer Governance over Framework Preference

La governance del consumer repository prevalece sobre cualquier preferencia del Framework.

### 5.5 Mergeability is not Integration Readiness

```text
mergeable = true
    ≠
ready to integrate
```

### 5.6 Human Review before Stable Integration

Toda mutación estable requiere revisión humana explícita.

### 5.7 Verify Stable State after Integration

Un merge exitoso no completa Integration por sí solo.

### 5.8 Represent Recovery without Automating it

Un fallo post-integration puede representarse como:

```text
RECOVERY REQUIRED
```

sin automatizar rollback o recovery.

---

## 6. Verified Candidate Input

Integration debe identificar el candidate que se desea aceptar.

Como mínimo:

```text
Candidate Reference
Application Outcome
Verification Result
Candidate State
```

El candidate debe estar:

```text
VERIFIED
```

antes de continuar.

---

## 7. Candidate Reference

Candidate Reference debe permitir identificar de forma inequívoca el estado evaluado.

Puede incluir:

```text
branch
commit
Pull Request
patch
equivalent platform reference
```

No se requiere un mecanismo GitHub-specific universal.

---

## 8. Application Outcome

Integration conserva la trazabilidad del resultado de Application.

Puede registrar:

```text
Application Result
Application Verification
Application Intent
Preservation Scope
```

Integration no reescribe el Application Record.

---

## 9. Stable Base Reference

Debe registrarse el stable target sobre el que se pretende integrar.

Ejemplos:

```text
main
master
release branch
equivalent stable branch
```

También debe registrarse una referencia concreta cuando sea posible.

---

## 10. REFRESH STABLE BASE

Antes de Integration debe comprobarse si el stable target ha cambiado desde la creación o verificación del candidate.

Registrar:

```text
Original Stable Base
Current Stable Reference
Base Drift
Relevant Stable Changes
```

---

## 11. Base Drift

Base Drift puede ser:

```text
NONE
PRESENT
```

La presencia de drift no constituye por sí sola un error.

---

## 12. EVALUATE DRIFT

Cuando exista drift debe evaluarse:

```text
target overlap
Application Intent validity
Preservation Scope validity
governance changes
release constraints
```

---

## 13. Drift Impact

Vocabulario descriptivo candidato:

```text
COMPATIBLE
INVALIDATING
UNCERTAIN
```

### COMPATIBLE

El stable base cambió pero no invalida el candidate.

### INVALIDATING

El drift hace que el candidate ya no sea seguro o correcto.

### UNCERTAIN

No existe Evidence suficiente para continuar.

---

## 14. Drift does not automatically mean REPLAN

Debe mantenerse:

```text
base drift
    ↓
evaluate impact
        ├── COMPATIBLE → continue
        ├── INVALIDATING → REPLAN / REJECT
        └── UNCERTAIN → DEFER / REPLAN
```

---

## 15. CHECK INTEGRATION CONDITIONS

Integration Conditions representan las condiciones actuales que deben satisfacerse antes de stable mutation.

Pueden incluir:

```text
mergeability
required reviews
required checks
branch protection
base freshness
release constraints
```

No existe un checklist universal obligatorio.

---

## 16. Mergeability

Mergeability es Evidence técnica útil.

Pero:

```text
mergeable
    ≠
semantically ready
```

Integration Readiness requiere más contexto.

---

## 17. Required Reviews

Los reviews requeridos dependen del consumer repository.

Pueden existir:

```text
zero approvals
one approval
multiple approvals
CODEOWNERS
team review
```

El Framework observa estas condiciones; no las inventa.

---

## 18. Required Checks

Los checks pueden incluir:

```text
tests
lint
build
security scanning
quality gates
documentation validation
```

Solo se registran los checks relevantes para el consumer.

---

## 19. Branch Protection

Integration puede observar restricciones como:

```text
required reviews
required checks
linear history
direct push restrictions
```

No configura branch protection.

---

## 20. Release Constraints

Cuando sean observables, pueden registrarse:

```text
release freeze
release branch
version constraint
timing constraint
```

Integration Core no orquesta releases.

---

## 21. Consumer Governance

Principio:

```text
Consumer Governance
    over
Framework Merge Preference
```

El Framework debe:

```text
observe
record
respect
```

No debe:

```text
override
reconfigure
normalize automatically
```

---

## 22. Merge Strategy

Integration Core no impone:

```text
merge commit
squash merge
rebase merge
```

La estrategia real depende del consumer repository.

Integration únicamente registra la utilizada.

---

## 23. Pull Request Boundary

Pull Request es una superficie válida para:

```text
review
policy enforcement
mergeability
integration evidence
```

pero no es un requisito conceptual universal.

---

## 24. REVIEW

Antes de stable mutation debe revisarse:

```text
candidate still verified
stable base refreshed
drift impact understood
Application Intent still valid
Preservation Scope still valid
Integration Conditions satisfied
Consumer Governance satisfied
```

---

## 25. Integration Review Result

Resultados soportados:

```text
PROCEED
DEFER
REPLAN
REJECT
```

Solo:

```text
PROCEED
```

permite ejecutar Integration.

---

## 26. DEFER

Use DEFER cuando:

```text
candidate may remain valid
but
current conditions do not allow safe Integration
```

Ejemplos:

```text
pending approval
release freeze
required check unavailable
temporary policy constraint
```

---

## 27. REPLAN

Use REPLAN cuando Evidence actual invalide el plan de Integration.

Ejemplos:

```text
target artifact changed materially
candidate assumptions stale
Preservation Scope no longer valid
stable base drift invalidates candidate
```

REPLAN no reescribe silenciosamente Application history.

---

## 28. REJECT

Use REJECT cuando el candidate no deba integrarse.

Puede ocurrir por:

```text
invalid candidate
unacceptable semantic outcome
governance rejection
scope violation
```

No requiere crear Integration Evidence ficticia.

---

## 29. INTEGRATE

INTEGRATE acepta el verified candidate en stable consumer state.

Debe realizarse únicamente después de:

```text
Integration Review
    PROCEED
```

---

## 30. Integration Method

Cuando Integration ocurre, registrar:

```text
method
stable target
integration reference
```

Ejemplos:

```text
merge commit
squash merge
rebase merge
equivalent platform operation
```

---

## 31. Integration Evidence

Debe conservar Evidence de la mutación estable.

Puede incluir:

```text
merge commit
integration reference
changed artifacts
diff summary
stable target
```

---

## 32. Integration Evidence is not Verification

Debe mantenerse:

```text
Integration Evidence
    proves mutation occurred

Stable-State Verification
    evaluates resulting stable state
```

Una no sustituye a la otra.

---

## 33. VERIFY STABLE STATE

Después de Integration debe verificarse el estado estable.

Como mínimo:

```text
expected stable change
Application Intent
Preservation Scope
```

---

## 34. Physical Verification

Comprueba que el stable state contiene los cambios físicos esperados.

Ejemplos:

```text
artifact exists
expected line changed
stable branch contains merge
unintended artifact absent
```

---

## 35. Intent Verification

Comprueba que el resultado estable satisface el Application Intent.

```text
physical merge
    ≠
semantic success
```

---

## 36. Preservation Verification

Comprueba que el contenido y comportamiento que debían preservarse siguen intactos.

Puede incluir:

```text
unrelated content
repository structure
consumer conventions
previously verified changes
```

---

## 37. Repository Health Verification

Cuando sea relevante puede registrarse:

```text
tests
build
lint
required checks
quality gates
repository-specific health evidence
```

Es contextual, no universalmente obligatorio.

---

## 38. Stable-State Verification Result

Resultados:

```text
PASS
FAIL
```

### PASS

El stable state cumple Intent y Preservation.

### FAIL

El stable state requiere atención posterior.

---

## 39. CONFIRM

Cuando Stable-State Verification resulta:

```text
PASS
```

la Integration puede confirmarse como:

```text
INTEGRATED
```

---

## 40. RECOVERY REQUIRED

Si Stable-State Verification resulta:

```text
FAIL
```

el estado final puede ser:

```text
RECOVERY REQUIRED
```

Esto registra un problema post-integration sin imponer cómo resolverlo.

---

## 41. Recovery Boundary

In scope:

```text
detect failure
record failure
preserve evidence
mark RECOVERY REQUIRED
```

Out of scope:

```text
automatic revert
automatic rollback
branch reset
release rollback
recovery orchestration
```

---

## 42. DISCARD vs RECOVERY

Application puede descartar un candidate antes de Integration.

```text
candidate not integrated
    ↓
DISCARD
```

Después de Integration:

```text
stable state already changed
    ↓
RECOVERY
```

Son problemas distintos.

---

## 43. Conflict Boundary

Integration puede:

```text
detect conflict
record conflict
DEFER
REPLAN
REJECT
```

No puede:

```text
automatically resolve semantic conflict
```

---

## 44. Traceability

Debe preservarse:

```text
Assessment Outcome
    ↓
Application Record
    ↓
Verified Candidate
    ↓
Integration Review
    ↓
Integration Action
    ↓
Stable-State Verification
```

---

## 45. Relationship with Assessment

Integration no reevalúa silenciosamente el Assessment original.

Si aparece Evidence materialmente contradictoria:

```text
REPLAN
or
new Assessment
```

---

## 46. Relationship with Application

Integration no modifica retrospectivamente:

```text
Application Intent
Application Result
Application Verification
```

Puede registrar que el candidate dejó de ser integrable.

---

## 47. Supported Application Histories

El mismo Integration lifecycle soporta candidates con:

```text
direct PASS
REFINE → PASS
```

El refinement previo no requiere un lifecycle distinto.

---

## 48. Supported Application Operations

La evidencia actual cubre:

```text
CREATE
MODIFY
```

Ambas comparten el mismo Integration lifecycle.

---

## 49. Safe-Stop Outcomes

Integration puede terminar sin stable mutation mediante:

```text
DEFER
REPLAN
REJECT
```

Estos resultados son válidos.

No son fallos técnicos por definición.

---

## 50. Final Integration States

Estados soportados por la representación:

```text
INTEGRATED
DEFERRED
REPLAN REQUIRED
REJECTED
RECOVERY REQUIRED
```

---

## 51. Integration Record

La representación reusable asociada al Guide debe permitir registrar:

```text
Integration Context
Candidate Reference
Application Outcome
Stable Base Reference
Stable Base Refresh
Drift Impact
Integration Conditions
Governance Constraints
Integration Review
Integration Decision
Integration Method
Integration Evidence
Stable-State Verification
Recovery Notes
Final Integration State
Conclusion
```

---

## 52. Mandatory Record Information

Debe existir siempre:

```text
Integration Context
Candidate Reference
Application Outcome
Stable Base Reference
Stable Base Refresh
Integration Conditions
Integration Review
Integration Decision
Stable-State Verification
Final Integration State
Conclusion
```

---

## 53. Conditional Record Information

Solo cuando aplique:

```text
Drift Impact
    when drift exists

Integration Method
Integration Evidence
    when Integration occurs

Recovery Notes
    when recovery is required
```

---

## 54. Contextual Information

Puede registrarse cuando sea relevante:

```text
Governance Constraints
Release Constraints
Repository Health Evidence
```

No debe inventarse para completar el documento.

---

## 55. Representation

El Integration Core utiliza:

```text
Structured Markdown
```

La representación debe permanecer:

```text
human-readable
human-editable
Git-reviewable
usable without tooling
```

---

## 56. No Structured Data Requirement

No se requiere:

```text
JSON
YAML
Schema
Manifest
typed Integration Plan
machine API
parser
```

---

## 57. No Automation Requirement

No se requiere:

```text
CLI
GitHub Actions
automatic PR creation
automatic approval
automatic merge
automatic conflict resolution
automatic rollback
```

---

## 58. Example — MODIFY without Drift

Candidate:

```text
Responsibility
    README-QUICK-START

Operation
    MODIFY

Candidate State
    VERIFIED

Base Drift
    NONE
```

Review:

```text
PROCEED
```

Integration:

```text
INTEGRATE
merge commit
```

Stable Verification:

```text
PASS
```

Final State:

```text
INTEGRATED
```

---

## 59. Example — CREATE with Compatible Drift

Candidate:

```text
Responsibility
    DOC-CHANGELOG

Operation
    CREATE

Application History
    REFINE → PASS

Base Drift
    PRESENT

Drift Impact
    COMPATIBLE
```

Review:

```text
PROCEED
```

Integration:

```text
INTEGRATE
```

Stable Verification:

```text
PASS
```

Final State:

```text
INTEGRATED
```

---

## 60. Example — Safe Stop

Candidate:

```text
Candidate State
    VERIFIED

Base Drift
    PRESENT

Drift Impact
    INVALIDATING
```

Review:

```text
REPLAN
```

Integration:

```text
NOT EXECUTED
```

Final State:

```text
REPLAN REQUIRED
```

---

## 61. Example — Post-Integration Failure

Integration:

```text
INTEGRATE
```

Stable Verification:

```text
FAIL
```

Final State:

```text
RECOVERY REQUIRED
```

The Guide does not prescribe rollback.

---

## 62. Safety Checklist

Before Integration:

- candidate is verified;
- stable base is refreshed;
- drift impact is understood;
- Application Intent remains valid;
- Preservation Scope remains valid;
- consumer governance is known enough;
- Integration Conditions are reviewed;
- Integration Review is explicit.

After Integration:

- Integration Evidence is captured;
- stable state is verified;
- Intent is verified;
- Preservation is verified;
- final Integration state is recorded.

---

## 63. Completion Rules

Integration is complete only when one of these outcomes is explicit.

### Successful Integration

```text
Integration Decision
    INTEGRATE

Stable-State Verification
    PASS

Final Integration State
    INTEGRATED
```

### Safe Stop

```text
Integration Decision
    DEFER / REPLAN / REJECT

Final Integration State
    corresponding safe-stop state
```

### Post-Integration Failure

```text
Integration occurred

Stable-State Verification
    FAIL

Final Integration State
    RECOVERY REQUIRED
```

---

## 64. Out of Scope

El Integration Core no implementa:

```text
automatic merge
automatic approval
automatic conflict resolution
automatic rollback
branch protection configuration
release orchestration
tagging
deployment
release rollback
CLI
GitHub Actions
Structured Data
Schema
Manifest
```

---

## 65. Non-Goals

Este Guide no es:

```text
merge bot
release manager
branch protection manager
rollback engine
deployment orchestrator
conflict resolver
```

---

## 66. Backward Compatibility

La introducción de Integration no invalida:

```text
Assessment Guide
Assessment Template
Application Guide
Application Template
historical Assessment records
historical Application records
```

No se requiere migración.

---

## 67. Core Boundary Summary

```text
Assessment
    understand and decide
        ↓
Application
    plan, apply in isolation and verify
        ↓
Integration
    accept into stable state and verify
```

Cada capability permanece separable y opcional.

---

## 68. Integration Lifecycle Summary

```text
Verified Candidate
    ↓
REFRESH STABLE BASE
    ↓
EVALUATE DRIFT
    ↓
CHECK INTEGRATION CONDITIONS
    ↓
REVIEW
    ├── DEFER
    ├── REPLAN
    ├── REJECT
    └── PROCEED
            ↓
        INTEGRATE
            ↓
        VERIFY STABLE STATE
            ├── PASS → INTEGRATED
            └── FAIL → RECOVERY REQUIRED
```

---

## 69. Framework Principle

> Stable Integration follows verified Application, current stable-state evidence, consumer governance and explicit human review.

---

## 70. Delivery Boundary

El Guide cubre exclusivamente el Integration Core aprobado para v0.9.0.

Cualquier necesidad nueva relacionada con:

```text
automation
rollback execution
release orchestration
branch protection configuration
machine-readable representation
```

debe volver a Discovery o backlog antes de implementarse.
