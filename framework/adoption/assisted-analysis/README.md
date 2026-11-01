# Existing Repository Adoption — Assisted Analysis Guide

La capability **Existing Repository Adoption — Assisted Analysis Core** proporciona una guía reutilizable para recopilar Evidence determinista, bounded, source-traceable y read-only que pueda utilizarse durante Assessment, Application e Integration sin sustituir la evaluación semántica ni las decisiones humanas.

Assisted Analysis no es una nueva fase del lifecycle.

Su posición es transversal:

```text
                 Assisted Analysis
                 ┌──────┼──────┐
                 ↓      ↓      ↓
Assessment    Application    Integration
```

Su función es apoyar la recopilación de Evidence.

No decide por el reviewer.

---

## 1. Propósito

Assisted Analysis responde a una pregunta limitada:

> ¿Qué hechos observables y deterministas pueden recopilarse de forma consistente para apoyar una revisión humana posterior?

El objetivo es reducir trabajo mecánico repetitivo relacionado con:

```text
repository inspection
artifact lookup
reference lookup
release lookup
Pull Request metadata
workflow/status evidence
comparison evidence
governance evidence
```

sin automatizar:

```text
semantic assessment
Adoption Decision
Application Result
Drift Impact
Integration Review
Integration Decision
```

---

## 2. Principios

El Core se basa en:

```text
Facts before Evaluation

Evidence before Decision

Read-Only before Mutation

Explicit Collection Scope

Source Traceability

Collection Gaps are Visible

Human Review owns Semantic Meaning

Representation before Tooling
```

---

## 3. Assisted Analysis no es un lifecycle stage

Existing Repository Adoption mantiene:

```text
Assessment Core
    ↓
optional Application Core
    ↓
optional Integration Core
```

Assisted Analysis puede apoyar cualquiera de las tres capabilities.

No añade una transición nueva.

---

## 4. Relación con Assessment

Assessment necesita:

```text
Detected Facts
Evidence
```

antes de producir:

```text
Responsibility State
Applicability
Evaluation Rationale
Adoption Decision
```

Assisted Analysis puede recopilar los primeros.

No produce los segundos.

---

## 5. Relación con Application

Application comienza con:

```text
REFRESH EVIDENCE
```

Assisted Analysis puede ayudar a recopilar:

```text
current artifacts
current refs
current configuration evidence
current release evidence
```

pero no decide:

```text
PROCEED
NO CHANGE
REPLAN
DEFER
REJECTED
```

---

## 6. Relación con Integration

Integration requiere:

```text
REFRESH STABLE BASE
CHECK INTEGRATION CONDITIONS
```

Assisted Analysis puede recopilar:

```text
stable reference
candidate reference
changed files
Pull Request metadata
reviews
workflow runs
statuses
branch protection evidence
comparison evidence
```

pero no decide:

```text
Drift Impact
Integration Review
Integration Decision
```

---

## 7. Core Boundary

Assisted Analysis puede:

```text
inspect
collect
reference
compare
summarize
record
```

No puede:

```text
reinterpret automatically
decide automatically
mutate
merge
rollback
remediate
```

---

## 8. Read-Only

La primera delivery es estrictamente:

```text
READ ONLY
```

El consumer repository no debe modificarse como parte de Assisted Analysis.

---

## 9. Collection Sequence

Proceso recomendado:

```text
DEFINE CONTEXT
    ↓
DEFINE COLLECTION SCOPE
    ↓
RECORD CONSUMER REFERENCE
    ↓
COLLECT DETERMINISTIC EVIDENCE
    ↓
RECORD SOURCES
    ↓
RECORD COLLECTION GAPS
    ↓
HUMAN REVIEW NOTES
    ↓
CONCLUDE SNAPSHOT
```

---

## 10. Evidence Context

Toda colección debe declarar el contexto.

Ejemplos:

```text
Assessment baseline
Assessment selected Responsibility
Application Evidence Refresh
Integration Stable Base Refresh
Integration condition review
```

El contexto explica para qué se recopila Evidence.

---

## 11. Consumer Reference

Debe registrarse una referencia reproducible cuando esté disponible.

Ejemplos:

```text
repository
branch
commit SHA
tag
Pull Request
candidate SHA
stable SHA
```

Una referencia reproducible permite saber exactamente qué estado se observó.

---

## 12. Collection Scope

Collection Scope define qué se pretende observar.

Ejemplos:

```text
repository baseline
selected Responsibility
selected artifacts
Application refresh
Integration base/candidate comparison
Integration conditions
```

La colección debe ser bounded.

---

## 13. Scope Completeness

Completeness significa:

```text
declared Collection Scope
    represented
```

No significa:

```text
entire repository
    exhaustively understood
```

---

## 14. Observable Fact

Un Observable Fact debe ser verificable desde Evidence.

Ejemplo:

```text
Fact
    root CHANGELOG.md absent

Source
    repository root listing
```

---

## 15. Deterministic Observation

Una observación determinista debe producir el mismo resultado sobre el mismo estado de entrada.

Ejemplos:

```text
file exists
file absent
directory exists
literal exists
configuration key exists
branch exists
commit exists
tag exists
release exists
```

---

## 16. Repository Structure Evidence

Puede incluir:

```text
root entries
known directories
known files
artifact paths
repository tree
```

Su finalidad es describir estructura observable.

---

## 17. Artifact Evidence

Puede incluir:

```text
artifact path
presence
absence
file SHA
literal signal
configuration key
```

Artifact Evidence no equivale a Responsibility evaluation.

---

## 18. Git Reference Evidence

Puede incluir:

```text
branch
commit SHA
tag
merge commit
base SHA
head SHA
```

Debe registrarse la referencia exacta cuando esté disponible.

---

## 19. Release Evidence

Puede incluir:

```text
Git tags
GitHub Releases
release references
published dates
target references
```

Solo deben registrarse hechos observados.

---

## 20. Pull Request Evidence

Cuando aplique, puede incluir:

```text
PR number
state
base ref
head ref
mergeability
merged state
merge commit
```

---

## 21. Workflow Evidence

Puede incluir:

```text
workflow presence
workflow run count
workflow run status
workflow conclusion
```

La ausencia de runs no implica automáticamente que Integration esté permitida.

---

## 22. Commit Status Evidence

Puede incluir:

```text
status contexts
combined status
check presence
check absence
```

El significado governance-aware debe revisarse humanamente.

---

## 23. Review Evidence

Puede incluir:

```text
review count
review state
requested reviewers
review threads
```

No debe convertirse automáticamente en aprobación semántica.

---

## 24. Comparison Evidence

Puede incluir:

```text
base/head comparison
ahead/behind counts
changed files
additions
deletions
path overlap
```

---

## 25. Governance Evidence

Puede incluir:

```text
branch protection flag
required status contexts
repository rules
review requirements
mergeability metadata
```

cuando sea accesible.

---

## 26. Source Traceability

Cada observación material debe poder señalar su source.

Ejemplos:

```text
repository path
file SHA
branch
commit SHA
tag
GitHub Release
Pull Request
workflow run
commit status
comparison
repository metadata
```

---

## 27. Evidence Source Format

No se exige un formato único.

Debe ser suficiente para responder:

```text
What was checked?
Where did the Evidence come from?
What was observed?
At which repository state?
```

---

## 28. Canonical Artifact Boundary

Debe mantenerse:

```text
canonical artifact absence
    ≠
Responsibility Missing
```

Ejemplo:

```text
root CHANGELOG.md
    ABSENT
```

no autoriza:

```text
DOC-CHANGELOG
    Missing
```

---

## 29. Non-Canonical Implementations

El reviewer debe considerar que una Responsibility puede estar cubierta por:

```text
equivalent implementation
distributed implementation
specialized implementation
non-canonical path
```

Assisted Analysis puede ayudar a descubrir candidatos.

No decide equivalencia.

---

## 30. Presence Boundary

También debe mantenerse:

```text
artifact present
    ≠
Responsibility Satisfied
```

La existencia física no certifica calidad, suficiencia ni adecuación semántica.

---

## 31. Facts vs Evaluation

Regla central:

```text
Detected Fact
    ≠
Evaluation
```

Ejemplo:

```text
Fact
    README.md present

Evaluation
    README responsibility satisfied
```

La segunda afirmación requiere revisión.

---

## 32. Evidence vs Decision

Regla central:

```text
Evidence
    ≠
Decision
```

Evidence puede informar una decisión.

No la sustituye.

---

## 33. Semantic Outcomes Excluded

Assisted Analysis no debe producir automáticamente:

```text
Responsibility State
Applicability
semantic equivalence
documentation quality
governance adequacy
Adoption Decision
Application Intent
Application Result
Drift Impact
Integration Review
Integration Decision
Final Integration State
risk acceptance
decision correctness
```

---

## 34. Collection Gaps

Toda colección debe permitir registrar gaps.

Stable vocabulary:

```text
NOT CHECKED
NOT ACCESSIBLE
NOT APPLICABLE
UNKNOWN
REQUIRES SEMANTIC REVIEW
```

---

## 35. NOT CHECKED

Usar cuando una fuente o dimensión estaba potencialmente dentro del dominio, pero no fue inspeccionada.

No equivale a:

```text
ABSENT
```

---

## 36. NOT ACCESSIBLE

Usar cuando la fuente no puede inspeccionarse.

Ejemplo:

```text
branch protection rule
    NOT ACCESSIBLE
```

No debe inferirse un estado alternativo.

---

## 37. NOT APPLICABLE

Usar cuando una sección condicional no corresponde al Collection Scope.

Ejemplo:

```text
Pull Request Evidence
    NOT APPLICABLE
```

para un baseline repository-only.

---

## 38. UNKNOWN

Usar cuando el estado no puede determinarse con la Evidence disponible.

```text
UNKNOWN
    ≠
ABSENT
```

---

## 39. REQUIRES SEMANTIC REVIEW

Usar cuando los hechos son observables pero insuficientes para una conclusión semántica.

Ejemplo:

```text
root CHANGELOG.md absent
specialized changelog exists elsewhere

Conclusion
    REQUIRES SEMANTIC REVIEW
```

---

## 40. Negative Evidence

Debe distinguirse:

```text
ABSENT
```

de:

```text
NOT CHECKED
NOT ACCESSIBLE
UNKNOWN
```

ABSENT solo debe usarse cuando la ausencia fue realmente observada dentro del scope.

---

## 41. Human Review Notes

El snapshot puede incluir:

```text
Human Review Notes
```

para registrar:

```text
questions
uncertainty
possible relevance
semantic follow-up
review observations
```

---

## 42. Notes are not Facts

Human Review Notes deben mantenerse separadas de deterministic observations.

```text
Human Review Note
    ≠
Detected Fact
```

---

## 43. Evidence Freshness

Evidence representa un estado temporal.

Puede quedar stale cuando:

```text
branch advances
candidate changes
files change
releases appear
governance changes
workflow state changes
```

---

## 44. Refresh Rule

Cuando el repository state relevante cambie:

```text
refresh Evidence
    before
semantic reuse
```

No asumir que un snapshot histórico sigue vigente.

---

## 45. Snapshot Reuse

Un snapshot puede reutilizarse si:

```text
consumer reference remains relevant
collection scope remains relevant
Evidence remains sufficiently fresh
sources remain traceable
```

---

## 46. Assessment Usage Flow

```text
Assisted Analysis
    ↓
Detected Facts
    ↓
Evidence
    ↓
Human Assessment
    ↓
State / Applicability / Decision
```

---

## 47. Assessment Example

Observed:

```text
README.md
    PRESENT

CHANGELOG.md
    ABSENT

docs/
    PRESENT
```

Allowed conclusion from Assisted Analysis:

```text
facts recorded
sources recorded
```

Not allowed:

```text
README responsibility
    Satisfied

DOC-CHANGELOG
    Missing
```

without semantic review.

---

## 48. Application Usage Flow

```text
Assisted Analysis
    ↓
Evidence Refresh
    ↓
Human Application Planning
```

---

## 49. Application Example

Historical decision:

```text
DOC-CHANGELOG
    ADAPT
```

Current Evidence:

```text
specialized changelog
    PRESENT

Git tags
    NONE OBSERVED

GitHub Releases
    NONE OBSERVED
```

Assisted Analysis stops there.

Human Application decides whether:

```text
PROCEED
NO CHANGE
REPLAN
DEFER
```

---

## 50. Integration Usage Flow

```text
Assisted Analysis
    ↓
Stable Base Refresh Evidence
    ↓
Human Drift Evaluation
    ↓
Human Integration Review
```

---

## 51. Integration Stable Base Evidence

Collect where applicable:

```text
original stable SHA
current stable SHA
candidate SHA
base advancement
changed files
reviews
workflow runs
statuses
branch governance evidence
```

---

## 52. Drift Boundary

Assisted Analysis puede observar:

```text
stable changed files
candidate changed files
direct path overlap
```

Debe mantenerse:

```text
no direct path overlap
    ≠
Drift Impact COMPATIBLE
```

---

## 53. Why Path Overlap is Insufficient

Dos cambios sin overlap físico pueden tener dependencia semántica.

Ejemplos:

```text
README references configuration changed elsewhere
release notes depend on version metadata
workflow behavior depends on project configuration
```

Por tanto, Drift Impact sigue siendo human-owned.

---

## 54. Governance Boundary

Assisted Analysis puede registrar:

```text
reviews = 0
workflow runs = 0
statuses = 0
branch protected = false
```

No debe inferir:

```text
governance satisfied
Integration approved
merge safe
```

---

## 55. Platform Boundary

Los experimentos han utilizado GitHub.

Por tanto, Evidence GitHub-specific está soportada.

Pero el Core debe permanecer:

```text
repository-platform aware
not GitHub-exclusive
```

---

## 56. GitHub-specific Conditional Evidence

Cuando exista GitHub pueden registrarse:

```text
Pull Requests
reviews
workflow runs
commit statuses
GitHub Releases
branch protection
repository metadata
```

Estas dimensiones son condicionales.

---

## 57. Structured Markdown

La representación requerida es:

```text
Structured Markdown
```

Debe ser:

```text
human-readable
human-editable
Git-reviewable
tool-independent
source-traceable
```

---

## 58. Evidence Snapshot Template

El reusable artifact para registrar Evidence es:

```text
framework/adoption/assisted-analysis/evidence-snapshot-template.md
```

El Guide explica:

```text
how
why
boundaries
review rules
```

El Template registra:

```text
what was checked
what was observed
where it came from
what remains unresolved
```

---

## 59. Stable Snapshot Sections

El Template utiliza:

```text
1. Evidence Context
2. Consumer Reference
3. Collection Scope
4. Repository Structure Evidence
5. Artifact Evidence
6. Git Reference Evidence
7. Release Evidence
8. Pull Request Evidence
9. Workflow / Status Evidence
10. Comparison Evidence
11. Governance Evidence
12. Collection Gaps
13. Human Review Notes
14. Conclusion
```

---

## 60. Mandatory Snapshot Information

Toda snapshot completada debe identificar:

```text
Evidence Context
Consumer Repository
Consumer Reference
Collection Scope
Observed Facts
Evidence Sources
Collection Gaps
Conclusion
```

---

## 61. Conditional Sections

Las secciones específicas pueden ser:

```text
used
NOT APPLICABLE
omitted according to Guide rules
```

cuando no formen parte del Collection Scope.

---

## 62. Snapshot Conclusion

Conclusion resume el estado de la colección.

Puede indicar:

```text
collection complete for declared scope
collection incomplete
semantic review required
refresh required
```

No debe convertirse en semantic lifecycle decision.

---

## 63. No Executable Tooling Required

El Core debe ser utilizable sin:

```text
CLI
repository scanner executable
GitHub Action
parser
database
installer
package
```

---

## 64. No Structured Data Contract

No se requiere:

```text
JSON
YAML
Schema
Manifest
typed Evidence API
machine contract
```

Structured Markdown es suficiente para este delivery.

---

## 65. No Decision Automation

Fuera de alcance:

```text
automatic Assessment
automatic Applicability
automatic Adoption Decision
automatic Application planning
automatic Application Result
automatic Drift Impact
automatic Integration Review
automatic Integration Decision
```

---

## 66. No Mutation Automation

Fuera de alcance:

```text
automatic remediation
consumer file creation
consumer file modification
automatic PR creation
automatic merge
automatic rollback
automatic recovery
```

---

## 67. No Continuous Reassessment

El Core no ejecuta:

```text
scheduled scanning
continuous reassessment
automatic Evidence refresh
PR-triggered analysis
```

Refresh sigue siendo human-triggered.

---

## 68. Componentization Boundary

Los artifacts permanecen en:

```text
framework/adoption/assisted-analysis/
```

No se introduce:

```text
Component family
Component metadata
catalog registration
Component dependencies
```

---

## 69. Framework Validator Boundary

El Framework Validator no se extiende para validar Evidence Snapshots.

```text
representation stability
    validated

machine validation need
    not demonstrated
```

---

## 70. Backward Compatibility

Assisted Analysis no modifica las semánticas estables de:

```text
Assessment Core
Application Core
Integration Core
```

Los flujos manuales existentes siguen siendo válidos sin Assisted Analysis.

---

## 71. Recommended Review Checklist

Antes de aceptar un Evidence Snapshot:

- [ ] Evidence Context está claro.
- [ ] Consumer Reference es reproducible cuando es posible.
- [ ] Collection Scope está bounded.
- [ ] Cada observación material tiene source.
- [ ] ABSENT solo se usa cuando la ausencia fue comprobada.
- [ ] NOT CHECKED / NOT ACCESSIBLE / UNKNOWN se distinguen correctamente.
- [ ] REQUIRES SEMANTIC REVIEW se usa cuando corresponde.
- [ ] Human Review Notes están separadas de Facts.
- [ ] No se ha introducido una decisión semántica automática.
- [ ] Evidence Freshness es suficiente para su uso previsto.

---

## 72. Completion Rule

Assisted Analysis está completo para una colección cuando:

```text
declared Collection Scope
    represented

material observations
    source-traceable

collection gaps
    explicit

semantic boundary
    preserved

conclusion
    recorded
```

---

## 73. Non-Goals

Este Guide no es:

```text
semantic assessor
decision engine
repository mutator
merge bot
rollback engine
continuous scanner
release orchestrator
Component generator
```

---

## 74. Safety Summary

Siempre preservar:

```text
Fact
    before
Evaluation

Evidence
    before
Decision

Read-Only
    before
Mutation

Human Review
    for
Semantic Meaning
```

---

## 75. Delivery Scope

El Assisted Analysis Core actual se limita a:

```text
Assisted Analysis Guide
    +
Structured Markdown Evidence Snapshot
```

No debe ampliarse sin revisión explícita del Delivery Scope.

---

## 76. Final Boundary

El resultado de Assisted Analysis es:

```text
bounded deterministic Evidence
    ready for
human review
```

No:

```text
repository truth
semantic certification
automatic decision
automatic mutation
```

---

## 77. Summary

Assisted Analysis permite recopilar Evidence reusable en:

```text
Assessment
Application
Integration
```

mediante una representación:

```text
read-only
source-traceable
bounded
human-readable
human-reviewed
```

La capability mejora la consistencia de la Evidence sin sustituir la responsabilidad humana sobre evaluación y decisión.
