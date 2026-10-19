# 27 — Adoption Repeatability Experiment

## 1. Propósito

Este documento continúa la investigación de **Existing Repository Adoption** desarrollada en:

```text
23_BACKEND_ADOPTION_DISCOVERY.md
        ↓
24_ADOPTION_MODEL_DISCOVERY.md
        ↓
25_MANUAL_ADOPTION_ASSESSMENT_DISCOVERY.md
        ↓
26_ADOPTION_SOLUTION_SHAPING_DISCOVERY.md
```

La etapa anterior identificó provisionalmente como **Minimal Representation Candidate**:

```text
Markdown Guide
    +
Structured Markdown Assessment
        including
            Summary Table
            Responsibility Detail
```

La representación todavía no ha sido validada para repetibilidad.

Por tanto, este experimento investiga:

> ¿Puede una guía mínima y una plantilla Markdown estructurada utilizarse para ejecutar un nuevo adoption assessment completo sin modificar sustancialmente su estructura?

El objetivo no es validar una implementación técnica.

El objetivo es comprobar si la representación candidata puede reutilizarse de forma suficientemente estable sobre otro consumer real.

---

## 2. Estado de partida

El trabajo anterior ha demostrado provisionalmente que:

```text
Manual Assessment
    Operationally feasible
    Traceable
```

pero todavía:

```text
Repeatability
    Not independently validated
```

También se ha establecido que:

```text
Guidance
    ≠
Assessment Representation
    ≠
Assessment Summary
    ≠
Generated Presentation
```

y que la representación mínima candidata no necesita actualmente:

```text
schema
parser
CLI
generator
validator
structured data contract
```

El experimento debe preservar estas fronteras.

---

## 3. Hipótesis del experimento

La hipótesis principal es:

```text
A minimal Markdown Guide
+
a Structured Markdown Assessment Template
```

pueden utilizarse para evaluar un nuevo consumer sin necesidad de rediseñar sustancialmente:

```text
assessment dimensions
section structure
summary structure
decision representation
evidence representation
rationale representation
```

Si esto ocurre, existiría evidencia adicional de que la representación candidata es suficientemente repetible para continuar madurando.

---

## 4. Qué significa repeatability en este experimento

Repeatability no significa:

```text
two reviewers
    produce
identical semantic judgments
```

La evaluación contiene decisiones contextuales que pueden requerir interpretación humana.

En este experimento, repeatability significa principalmente que:

```text
the same representation
can support
another complete assessment
```

sin que el nuevo consumer obligue a modificar sustancialmente la forma de registrar el proceso.

Por tanto, la unidad principal de observación será:

```text
representation stability
```

y no:

```text
semantic outcome identity
```

---

## 5. Qué constituiría un rediseño sustancial

Para evitar interpretar cualquier pequeño ajuste como fallo, es necesario distinguir:

```text
Refinement
    ≠
Substantial Redesign
```

### 5.1 Refinement aceptable

Podrían considerarse refinamientos normales:

- aclarar una instrucción;
- mejorar wording;
- añadir un ejemplo;
- ajustar una etiqueta;
- reorganizar una explicación;
- mejorar una tabla sin alterar sus dimensiones;
- añadir una nota de uso;
- eliminar redundancia.

Estos cambios no implican necesariamente que la representación haya fallado.

---

### 5.2 Rediseño sustancial

Se consideraría señal de rediseño sustancial si el experimento obliga a:

- introducir nuevas dimensiones esenciales del assessment;
- eliminar dimensiones centrales porque resultan inaplicables;
- cambiar la separación entre Evidence, Evaluation y Decision;
- reemplazar la estructura por Responsibility;
- abandonar Summary Table + Responsibility Detail;
- introducir Structured Data para poder completar el assessment;
- introducir tooling obligatorio;
- redefinir significativamente el significado de State, Applicability o Adoption Decision;
- modificar el modelo únicamente para acomodar el nuevo consumer.

Conceptualmente:

```text
representation supports consumer
        ✓

representation must be rebuilt for consumer
        ✗
```

---

## 6. Objetivos de observación

El experimento debe observar explícitamente:

```text
repeatability
missing fields
redundant fields
review friction
verbosity
uncertainty handling
decision rationale
summary usefulness
```

Además deberá registrar:

```text
unexpected information needs
representation workarounds
consumer-specific pressure
template deviations
```

El objetivo no es evitar cualquier desviación.

El objetivo es comprender si las desviaciones son:

```text
local adaptation
```

o:

```text
evidence of structural weakness
```

---

## 7. Criterios de éxito

El experimento podrá considerarse favorable si:

1. todas las Responsibilities relevantes pueden evaluarse mediante la misma estructura;
2. Evidence puede registrarse sin crear un mecanismo alternativo;
3. State, Applicability, Implementation Characteristics y Uncertainty siguen siendo utilizables;
4. Evaluation Rationale y Decision Rationale siguen siendo distinguibles;
5. la Summary Table permite comprender el estado global;
6. los casos complejos pueden explicarse en Responsibility Detail;
7. no es necesario introducir tooling especializado;
8. no aparece una nueva dimensión conceptual indispensable;
9. las modificaciones realizadas durante el experimento son refinamientos locales y no un rediseño estructural.

El criterio no será:

```text
zero changes
```

sino:

```text
no material redesign required
```

---

## 8. Posibles resultados del experimento

Para mantener continuidad con los experimentos anteriores, el resultado debería clasificarse explícitamente.

### MODEL HOLDS

La representación candidata funciona sobre el nuevo consumer sin cambios estructurales materiales.

Puede haber refinamientos menores.

---

### REFINEMENT NEEDED

La representación sigue siendo utilizable, pero el experimento identifica ajustes relevantes que no contradicen su estructura central.

Por ejemplo:

```text
field clarification
summary refinement
guidance improvement
redundancy reduction
```

---

### MODEL CONTRADICTION

El nuevo consumer demuestra que la representación candidata no puede sostener un assessment completo sin cambios fundamentales.

Por ejemplo:

```text
new essential dimension required
core separation fails
summary/detail model insufficient
structured representation becomes mandatory
```

El resultado deberá derivarse de evidencia observada durante el experimento, no de preferencia por una solución más sofisticada.

---

## 9. Consumer Selection Protocol

El siguiente paso consiste en seleccionar un consumer que aporte evidencia nueva sobre la representación candidata.

La selección no partirá del conjunto completo de repositorios disponibles.

El universo de candidatos se limitará a repositorios que ya representen trabajo profesionalmente relevante dentro del portfolio público del usuario.

Esto evita introducir en el experimento:

```text
training repositories
primitive experiments
learning exercises
abandoned prototypes
repositories with little professional relevance
```

que podrían generar ruido y reducir la utilidad de las conclusiones.

El objetivo es comprobar la representación sobre un consumer que sea simultáneamente:

```text
real
representative
maintained enough
professionally relevant
compatible with TPL-BACKEND
```

---

## 10. Objetivo de la selección

El consumer debe permitir responder:

```text
Can the same assessment representation
support another professionally representative backend repository
without material redesign?
```

Los experimentos anteriores ya han proporcionado diversidad tecnológica mediante consumers basados en:

```text
Java / Spring Boot
TypeScript / NestJS
Python / FastAPI
PHP / Symfony
```

Por tanto, este experimento no necesita maximizar nuevamente:

```text
technology novelty
```

La prioridad pasa a ser:

```text
representation repeatability
+
professional relevance
+
repository responsibility diversity
```

---

## 11. Candidate Universe

El universo inicial se deriva de los proyectos actualmente destacados como representativos en el portfolio profesional.

Entre ellos se encuentran:

```text
only_film
aula-robotica-platform
cognitiva-ai
github-framework
dental-front
dental-back-spring
```

Además, `dental-back` continúa siendo relevante dentro del conjunto de proyectos destacados/pineados.

No todos estos repositorios son candidatos válidos para `TPL-BACKEND`.

Por tanto, la selección se realiza en dos etapas:

```text
Professional Portfolio Repositories
        ↓
TPL-BACKEND Eligibility
        ↓
Repeatability Experiment Candidate
```

---

## 12. TPL-BACKEND Eligibility

Los proyectos se clasifican inicialmente según su relación con `TPL-BACKEND`.

### 12.1 `only_film`

```text
Backend fit
    Very High
```

Java / Spring Boot con aplicación backend y responsabilidades suficientemente complejas.

Sin embargo, ya ha sido utilizado en Existing Repository Adoption Discovery.

Resultado:

```text
Exclude
Reason: previous assessment consumer
```

---

### 12.2 `aula-robotica-platform`

```text
Backend fit
    Very High
```

Python / FastAPI con APIs, persistencia, autenticación y capacidades real-time.

Ya ha sido utilizado durante Discovery.

Resultado:

```text
Exclude
Reason: previous assessment consumer
```

---

### 12.3 `dental-back`

```text
Backend fit
    Very High
```

TypeScript / NestJS.

También ha sido utilizado durante Discovery.

Resultado:

```text
Exclude
Reason: previous assessment consumer
```

---

### 12.4 `dental-back-spring`

```text
Backend fit
    Very High
```

Java / Spring Boot REST API con:

```text
Spring Security
JWT
MySQL
persistence
domain logic
API responsibilities
```

No ha sido utilizado como consumer en los assessments anteriores.

Resultado:

```text
Eligible
```

---

### 12.5 `dental-front`

La naturaleza principal del repositorio es frontend Angular.

Resultado:

```text
Exclude
Reason: not a TPL-BACKEND consumer
```

---

### 12.6 `cognitiva-ai`

El proyecto está orientado principalmente a Data / Machine Learning.

Aunque contiene software ejecutable y estructura técnica, no representa de forma natural un backend application repository equivalente a los consumers anteriores.

Resultado:

```text
Exclude
Reason: different repository responsibility profile
```

---

### 12.7 `github-framework`

Es el propio Framework.

Utilizarlo introduciría circularidad:

```text
Framework
    assessing adoption of
Framework expectations
```

Resultado:

```text
Exclude
Reason: framework repository, not external consumer
```

---

## 13. Candidate Result

Después de aplicar:

```text
professional relevance
+
TPL-BACKEND eligibility
+
previous consumer exclusion
```

queda un candidato principal:

```text
fran-eliot/dental-back-spring
```

Por tanto, no es necesario construir una matriz artificial entre repositorios con ajuste significativamente peor.

La selección resulta de restricciones explícitas, no de una puntuación competitiva.

---

## 14. Selected Consumer

El consumer seleccionado para el Repeatability Experiment es:

```text
Repository
    fran-eliot/dental-back-spring

Repository Template
    TPL-BACKEND v0.1.0
```

---

## 15. Selection Rationale

`dental-back-spring` es adecuado porque combina:

```text
professional portfolio relevance
+
strong TPL-BACKEND fit
+
real application responsibilities
+
sufficient implementation complexity
+
accessible repository evidence
+
no previous adoption assessment
```

Aunque reutiliza Java / Spring Boot, la novedad tecnológica no constituye el objetivo principal de esta fase.

Existing Repository Adoption Discovery ya ha demostrado que el modelo puede utilizarse sobre varios stacks.

Este experimento investiga otra propiedad:

```text
representation repeatability
```

Por tanto:

```text
Different Technology
    useful but not required

Different Real Consumer
    required

Reusable Assessment Representation
    primary concern
```

---

## 16. Diferencias respecto a Only Film

La coincidencia en Java / Spring Boot no implica que ambos consumers sean equivalentes.

`only_film` y `dental-back-spring` presentan perfiles distintos.

De forma preliminar:

```text
Only Film
    cinema management domain
    Spring MVC / backend application
    Thymeleaf integration
    PostgreSQL
    Flyway
    mature testing and quality evolution
    significant engineering hardening

Dental Back Spring
    dental scheduling domain
    REST API orientation
    Spring Security
    JWT authentication
    MySQL
    REST API–focused repository structure
```

Estas diferencias pueden ejercer presión sobre:

```text
README responsibilities
API documentation
architecture description
security documentation
database documentation
testing documentation
quick start
repository structure
```

sin cambiar el Repository Template utilizado.

---

## 17. Known Constraints

Antes de ejecutar el assessment se registran las siguientes restricciones.

### KC-01 — Technology repetition

Java / Spring Boot ya apareció en Discovery.

Esto reduce:

```text
technology novelty
```

pero no reduce de forma material:

```text
repeatability value
```

porque el objeto de estudio actual es la representación del assessment.

---

### KC-02 — Prior knowledge

Existe familiaridad previa con el proyecto y su dominio.

Esto puede facilitar la interpretación del repositorio.

Para limitar ese efecto:

```text
repository evidence
must remain
the basis of every assessment statement
```

El conocimiento previo no debe sustituir Evidence disponible en el consumer.

---

### KC-03 — Portfolio-oriented documentation

El repositorio forma parte del portfolio profesional y puede presentar un nivel de documentación distinto al de consumers anteriores.

Esto podría reducir algunos casos `Missing`.

No debe considerarse una ventaja ni una desventaja experimental.

El objetivo no es maximizar defectos, sino comprobar:

```text
representation reuse
```

sobre un consumer profesional diferente.

---

### KC-04 — Relationship with `dental-back`

Existe otro backend del mismo dominio desarrollado con NestJS.

Esto podría facilitar comparaciones conceptuales.

Sin embargo:

```text
dental-back
```

no debe utilizarse como fuente de Evidence para este assessment.

El consumer evaluado es exclusivamente:

```text
dental-back-spring
```

---

## 18. Expected Pressure Points

Antes de ejecutar el assessment se identifican los siguientes pressure points.

### PP-01 — REST API orientation

La arquitectura está centrada en una API backend.

Esto puede aumentar la relevancia de:

```text
DOC-API
README-ARCHITECTURE
README-QUICK-START
README-TESTING
```

y permitir comprobar si Summary + Detail representan adecuadamente responsabilidades con mucha Evidence técnica.

---

### PP-02 — Security

Spring Security y JWT pueden generar Evidence relevante distribuida entre:

```text
dependencies
configuration
security classes
controllers
authentication flows
README
```

Esto permitirá comprobar la capacidad de registrar:

```text
Distributed
Equivalent
Own
```

como Implementation Characteristics.

---

### PP-03 — Persistence

La integración con MySQL y la capa de persistencia pueden ejercer presión sobre:

```text
DOC-DATABASE
README-TECH-STACK
README-ARCHITECTURE
```

y sobre la separación entre:

```text
implementation capability
```

y:

```text
documented responsibility
```

---

### PP-04 — Documentation maturity

Algunas responsabilidades pueden estar bien cubiertas y otras solo parcialmente.

Esto debería producir una mezcla útil de:

```text
Satisfied
Partial
Missing
```

sin depender de un consumer deliberadamente incompleto.

---

### PP-05 — Decision Rationale

Al tratarse de un proyecto real y representativo del portfolio, ciertas decisiones pueden requerir distinguir con claridad:

```text
what exists
what is applicable
what should be preserved
what should be adapted
what should be added
```

Esto ejercerá presión directa sobre la separación:

```text
Evaluation Rationale
    ≠
Decision Rationale
```

---

### PP-06 — Summary usefulness

La combinación de responsabilidades satisfechas, parciales y ausentes permitirá comprobar si:

```text
Summary Table
```

es suficiente para comprender el assessment global sin sustituir:

```text
Responsibility Detail
```

---

## 19. Selection Result

La selección queda formalmente registrada como:

```text
Selected Consumer
    fran-eliot/dental-back-spring

Repository Template
    TPL-BACKEND v0.1.0

Primary Experimental Goal
    representation repeatability

Technology Novelty
    Low

Professional Relevance
    High

TPL-BACKEND Fit
    Very High

Repository / Responsibility Diversity
    Medium–High

Evidence Accessibility
    High

Experimental Value
    High
```

La ausencia de novedad tecnológica se acepta deliberadamente.

No se pretende demostrar nuevamente:

```text
cross-technology applicability
```

sino:

```text
repeatable use of the same assessment representation
```

---

## 20. Regla de control

Una vez seleccionado `dental-back-spring`:

```text
do not redesign first
```

La representación inicial debe definirse antes de realizar el assessment completo.

Durante la ejecución podrán registrarse:

```text
friction
missing information slots
redundancy
workarounds
template deviations
unexpected information needs
```

pero no deberán corregirse silenciosamente antes de haber sido observados.

Esto preserva la capacidad del experimento para distinguir:

```text
representation refinement
```

de:

```text
representation redesign
```

---

## 21. Representation Freeze

El siguiente paso consiste en materializar y congelar:

```text
Minimal Adoption Guide — Version 0
        +
Structured Markdown Assessment Template — Version 0
```

El orden experimental será:

```text
define guide
        ↓
define template
        ↓
freeze representation
        ↓
assess dental-back-spring
        ↓
record friction
        ↓
evaluate repeatability
        ↓
refine only when evidence justifies it
```

No debe comenzar todavía el assessment detallado de las 28 Responsibilities.

Primero debe existir una representación inicial explícita contra la que podamos observar desviaciones.

---

## 22. Minimal Adoption Guide — Version 0

La guía mínima tiene una función concreta:

```text
explain how to perform
an adoption assessment
```

No debe convertirse en:

```text
formal specification
implementation manual
tooling contract
schema definition
```

Su propósito es proporcionar instrucciones suficientes para que el assessment pueda ejecutarse de forma:

```text
consistent
traceable
reviewable
```

sin introducir acoplamiento técnico prematuro.

---

## 23. Assessment Unit

La unidad de evaluación es:

```text
Responsibility
```

No:

```text
file
directory
artifact name
```

La existencia o ausencia de un archivo concreto no determina por sí sola el resultado.

Por tanto:

```text
File Presence
    ≠
Responsibility Satisfaction
```

y:

```text
File Absence
    ≠
Responsibility Missing
```

Una Responsibility puede estar satisfecha mediante una implementación:

```text
Canonical
Own
Equivalent
Specialized
Distributed
```

si la Evidence demuestra que cumple razonablemente la responsabilidad esperada.

---

## 24. Assessment Sequence

Cada Responsibility debe evaluarse siguiendo la misma secuencia:

```text
1. Detect Facts
2. Collect Evidence
3. Evaluate State
4. Evaluate Applicability
5. Identify Implementation Characteristics
6. Record Uncertainty
7. Write Evaluation Rationale
8. Select Adoption Decision
9. Write Decision Rationale
```

Esta secuencia preserva la separación entre:

```text
what exists
what it means
what should be done
```

---

## 25. Detected Facts

Los Detected Facts son observaciones verificables obtenidas directamente del repository consumer.

Ejemplos:

```text
README.md exists
README contains installation instructions
pom.xml declares Spring Security
docs/ directory does not exist
OpenAPI configuration is present
tests are present under src/test
```

Los Detected Facts deben evitar:

```text
value judgments
recommendations
assumptions
adoption decisions
```

Un Fact describe.

No evalúa.

---

## 26. Evidence

Evidence es la información utilizada para justificar una evaluación.

Puede proceder de:

```text
README
source code
configuration
dependency manifests
tests
CI configuration
documentation
runtime artifacts
database migrations
API definitions
repository structure
```

Una Responsibility puede requerir varias piezas de Evidence.

Por tanto:

```text
Responsibility
    ↓
one or more Evidence items
```

La Evidence debe ser suficientemente concreta para permitir revisión posterior.

Siempre que sea razonable debe identificar:

```text
file
directory
section
configuration element
implementation location
```

---

## 27. Responsibility State

El estado provisional continúa siendo:

```text
Satisfied
Partial
Missing
```

### Satisfied

La Evidence disponible demuestra que la Responsibility está razonablemente cubierta.

Esto no exige necesariamente una implementación canónica.

---

### Partial

La Responsibility está cubierta solo parcialmente.

Puede existir:

```text
incomplete documentation
distributed information
missing important detail
partial implementation
insufficient discoverability
```

---

### Missing

No se encuentra Evidence suficiente de que la Responsibility esté cubierta.

`Missing` describe el estado observado.

No implica automáticamente:

```text
ADD
```

---

## 28. Applicability

Applicability debe evaluarse independientemente de State.

Valores:

```text
Applicable
Not Applicable
Uncertain
```

Esto preserva una regla fundamental:

```text
Missing
    ≠
Applicable
```

Una Responsibility puede estar ausente y al mismo tiempo no resultar necesaria para el consumer actual.

---

## 29. Implementation Characteristics

Las características de implementación permiten describir cómo aparece una Responsibility cuando existe.

Valores provisionales:

```text
Canonical
Own
Equivalent
Specialized
Distributed
```

Pueden coexistir.

Ejemplo:

```text
Own
+
Distributed
```

si una Responsibility está cubierta mediante convenciones propias repartidas entre varios artifacts.

No deben interpretarse como estados de calidad.

Por ejemplo:

```text
Own
    ≠
bad

Canonical
    ≠
automatically preferable
```

---

## 30. Uncertainty

Debe registrarse explícitamente cuando la Evidence no permita una conclusión suficientemente segura.

La incertidumbre puede derivar de:

```text
ambiguous documentation
distributed evidence
external dependencies
unclear ownership
missing runtime context
incomplete repository history
```

Uncertainty no debe resolverse mediante suposición.

Cuando exista:

```text
Uncertainty
    ↓
make it visible
```

---

## 31. Evaluation Rationale

Evaluation Rationale explica:

```text
why the evidence
supports the evaluated state
```

Debe responder principalmente:

> ¿Por qué esta Responsibility ha sido evaluada de esta forma?

No debe responder todavía:

> ¿Qué deberíamos cambiar?

Ejemplo conceptual:

```text
State
    Partial

Evaluation Rationale
    The repository documents the technology stack,
    but does not explain the main architectural components
    or their relationships.
```

---

## 32. Adoption Decision

La decisión se registra después de la evaluación.

El vocabulario provisional continúa siendo:

```text
PRESERVE
ADAPT
ADD
ACCEPT
EVALUATE
JUSTIFY
OMIT
```

No existe un mapping automático:

```text
State
    ↓
Decision
```

La decisión depende de:

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
```

---

## 33. Decision Semantics

### PRESERVE

La Responsibility está adecuadamente cubierta y no necesita una modificación relevante.

---

### ADAPT

Existe una base válida, pero conviene modificarla para mejorar alineación, claridad o cobertura.

---

### ADD

La Responsibility es aplicable y debe incorporarse porque no existe cobertura suficiente.

---

### ACCEPT

La implementación existente es diferente de la forma canónica pero resulta suficientemente adecuada.

---

### EVALUATE

La información disponible todavía no permite cerrar una decisión estable.

Su función sigue considerándose potencialmente transicional.

---

### JUSTIFY

La situación requiere una explicación explícita para mantener una desviación o elección.

Su relación exacta con Decision Rationale continúa provisional.

---

### OMIT

La Responsibility no debe incorporarse al consumer actual.

Normalmente requiere una razón explícita basada en Applicability o contexto.

---

## 34. Decision Rationale

Decision Rationale explica:

```text
why this adoption decision
is appropriate
```

Debe permanecer separada de Evaluation Rationale.

Conceptualmente:

```text
Evaluation Rationale
    why this is the current state

Decision Rationale
    why this is the chosen action
```

Ejemplo:

```text
State
    Missing

Applicability
    Not Applicable

Decision
    OMIT

Decision Rationale
    The consumer does not expose deployment responsibilities
    that justify maintaining dedicated deployment documentation.
```

---

## 35. Requirement Level

El Requirement Level definido por el Repository Template debe conservarse durante el assessment.

Valores existentes:

```text
Required
Recommended
Optional
```

Requirement Level influye en la decisión, pero tampoco determina automáticamente el resultado.

Por ejemplo:

```text
Required + Missing
```

genera una señal fuerte, pero la evaluación debe seguir registrando Evidence, Applicability y Rationale.

---

## 36. Summary and Detail

La representación utilizará dos niveles complementarios.

### Summary Table

Debe permitir comprender rápidamente:

```text
Responsibility
Requirement Level
State
Applicability
Adoption Decision
```

Su función es:

```text
scan
compare
review globally
```

---

### Responsibility Detail

Debe conservar la información necesaria para justificar cada evaluación.

Como mínimo:

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
Adoption Decision
Decision Rationale
```

La Summary Table no sustituye Responsibility Detail.

Responsibility Detail no elimina la necesidad de Summary.

---

## 37. Evidence Discipline

Durante el experimento debe aplicarse la siguiente regla:

```text
repository evidence first
```

No deben utilizarse como sustituto de Evidence:

```text
prior knowledge
memory of the project
expected framework behavior
assumed best practices
future intentions
```

Si existe conocimiento previo no verificable en el repositorio:

```text
do not convert it into fact
```

Debe quedar fuera del assessment o registrarse como incertidumbre si resulta relevante.

---

## 38. Assessment Independence

El consumer debe evaluarse respecto a `TPL-BACKEND v0.1.0`.

No respecto a:

```text
another consumer
personal preference
ideal architecture
latest implementation patterns
```

Otros repositories pueden ayudar a comprender contexto histórico, pero no deben utilizarse como Evidence del consumer evaluado.

En este experimento:

```text
dental-back
    ≠
Evidence for dental-back-spring
```

---

## 39. No Automatic Remediation

Este assessment no modifica el consumer.

Por tanto:

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

continúa siendo el límite operativo.

Quedan fuera:

```text
APPLY
VERIFY
```

No debe ejecutarse una modificación para demostrar que una decisión podría aplicarse.

---

## 40. No Tooling Requirement

La guía debe poder utilizarse manualmente.

No requiere:

```text
CLI
parser
validator
generator
GitHub Action
structured schema
database
```

Si durante el experimento aparece una necesidad de tooling, debe registrarse como observación.

No debe introducirse automáticamente.

---

## 41. Review Rule

Antes de considerar una Responsibility cerrada debe poder responderse:

```text
What did we observe?
What evidence supports it?
What state did we assign?
Is it applicable?
How is it implemented?
What uncertainty remains?
Why did we evaluate it this way?
What adoption decision did we make?
Why?
```

Si alguna respuesta esencial no puede registrarse mediante la representación actual, deberá anotarse como:

```text
representation friction
```

---

## 42. Minimality Rule

La guía debe permanecer mínima.

Durante el experimento no se añadirán reglas simplemente porque:

```text
they could be useful
```

Solo se considerará ampliar la representación cuando exista:

```text
observed assessment need
```

Por tanto:

```text
possible future usefulness
    ≠
current requirement
```

---

## 43. Guide Version Freeze

La guía definida en las secciones 22–42 constituye:

```text
Minimal Adoption Guide
Version 0
```

Durante el assessment de `dental-back-spring`:

```text
Version 0
    is frozen
```

Los problemas encontrados se registrarán primero como Evidence del experimento.

No se corregirá silenciosamente la guía durante la ejecución.

Cualquier modificación posterior deberá clasificarse como:

```text
wording refinement
local refinement
structural refinement
substantial redesign
```

---

## 44. Next Representation Artifact

Con la guía Version 0 congelada, el siguiente paso es definir:

```text
Structured Markdown Assessment Template
Version 0
```

La plantilla deberá materializar exactamente las dimensiones establecidas en esta guía, sin añadir nuevas dimensiones conceptuales antes del experimento.

---

## 45. Structured Markdown Assessment Template — Version 0

La plantilla debe materializar la guía Version 0 sin introducir nuevas dimensiones conceptuales.

Su función es proporcionar una estructura repetible para:

```text
record
review
compare
trace
```

cada Responsibility evaluada.

La plantilla no pretende ser:

```text
machine-readable schema
serialization contract
parser syntax
database model
```

Es una convención Markdown para revisión humana.

---

## 46. Assessment Header

Cada assessment debe comenzar con una cabecera mínima.

```markdown
# Adoption Assessment

## Assessment Context

- **Consumer:** `<repository>`
- **Repository Template:** `<template and version>`
- **Assessment Type:** Existing Repository Adoption
- **Assessment Representation:** Structured Markdown Assessment — Version 0
- **Assessment Date:** `<date>`
- **Repository Reference:** `<branch, tag or commit if relevant>`
- **Assessment Status:** `<In Progress | Completed>`
```

La cabecera debe permitir identificar:

```text
what was assessed
against what
using which representation
at which point in time
```

No se requiere metadata formal adicional en Version 0.

---

## 47. Assessment Scope

La cabecera debe ir seguida de una breve declaración de alcance.

```markdown
## Scope

This assessment evaluates the consumer repository against the Responsibilities
defined by `<Repository Template>`.

The assessment records repository evidence, evaluates each Responsibility and
documents adoption decisions.

It does not modify the consumer repository.
```

Su objetivo es preservar explícitamente el límite:

```text
Assessment
    ≠
Application
```

---

## 48. Assessment Summary

El assessment debe incluir una Summary Table antes del detalle de Responsibilities.

Version 0 utilizará:

```markdown
## Summary

| Responsibility | Requirement Level | State | Applicability | Adoption Decision |
|---|---|---|---|---|
| `<ID>` | `<Required / Recommended / Optional>` | `<Satisfied / Partial / Missing>` | `<Applicable / Not Applicable / Uncertain>` | `<Decision>` |
```

La tabla debe contener una fila por Responsibility.

No incluirá en Version 0:

```text
Evidence
Implementation Characteristics
Uncertainty detail
Rationale
```

porque estos elementos reducirían la legibilidad del resumen.

---

## 49. Summary Purpose

La Summary Table debe permitir responder rápidamente:

```text
What responsibilities were assessed?
How important are they?
What is their current state?
Are they applicable?
What decision was made?
```

No debe intentar responder:

```text
Why?
```

La explicación pertenece a Responsibility Detail.

Por tanto:

```text
Summary
    = orientation

Detail
    = justification
```

---

## 50. Optional Aggregate Summary

Version 0 permite, pero no exige, un resumen agregado.

Puede utilizarse cuando ayude a comprender el assessment.

Ejemplo:

```markdown
### Aggregate Results

#### State

| State | Count |
|---|---:|
| Satisfied | `<n>` |
| Partial | `<n>` |
| Missing | `<n>` |

#### Applicability

| Applicability | Count |
|---|---:|
| Applicable | `<n>` |
| Not Applicable | `<n>` |
| Uncertain | `<n>` |

#### Adoption Decision

| Decision | Count |
|---|---:|
| PRESERVE | `<n>` |
| ADAPT | `<n>` |
| ADD | `<n>` |
| ACCEPT | `<n>` |
| EVALUATE | `<n>` |
| JUSTIFY | `<n>` |
| OMIT | `<n>` |
```

Este resumen es derivado.

No constituye una nueva dimensión del assessment.

---

## 51. Responsibility Detail Structure

Cada Responsibility debe utilizar la misma estructura básica.

```markdown
## `<Responsibility ID>` — `<Responsibility Name>`

- **Requirement Level:** `<Required / Recommended / Optional>`
- **State:** `<Satisfied / Partial / Missing>`
- **Applicability:** `<Applicable / Not Applicable / Uncertain>`
- **Implementation Characteristics:** `<one or more values, or None observed>`
- **Uncertainty:** `<None | description>`

### Detected Facts

- `<fact>`
- `<fact>`

### Evidence

- `<repository location or evidence item>`
- `<repository location or evidence item>`

### Evaluation Rationale

`<why the evidence supports the assigned State and Applicability>`

### Adoption Decision

`<PRESERVE | ADAPT | ADD | ACCEPT | EVALUATE | JUSTIFY | OMIT>`

### Decision Rationale

`<why this decision is appropriate>`
```

Esta estructura constituye el núcleo de:

```text
Structured Markdown Assessment
Version 0
```

---

## 52. Responsibility Identity

Cada bloque debe conservar:

```text
Responsibility ID
Responsibility Name
Requirement Level
```

tal como se definen en el Repository Template.

No deben renombrarse las Responsibilities para adaptarlas al consumer.

Puede añadirse contexto dentro del rationale, pero no alterar la identidad evaluada.

Esto preserva:

```text
Template Responsibility
        ↓
Consumer Assessment
```

sin crear una taxonomía paralela.

---

## 53. Detected Facts Field

`Detected Facts` debe contener únicamente observaciones verificables.

Formato preferido:

```markdown
### Detected Facts

- `README.md` contains a technology stack section.
- `pom.xml` declares Spring Security.
- No `docs/` directory is present.
```

No debe utilizarse:

```markdown
- The documentation is poor.
- Security is well implemented.
- The repository should add an architecture document.
```

porque esas frases mezclan:

```text
Fact
Evaluation
Decision
```

---

## 54. Evidence Field

`Evidence` debe identificar los artifacts concretos utilizados para sustentar la evaluación.

Ejemplo:

```markdown
### Evidence

- `README.md` — "Technologies" section.
- `pom.xml` — Spring Security dependency.
- `src/main/java/.../SecurityConfig.java`.
```

Si la Evidence está distribuida:

```markdown
### Evidence

- `README.md`.
- `pom.xml`.
- `src/main/java/...`.
- `src/main/resources/application.properties`.
```

Esto permite representar directamente:

```text
Distributed Evidence
```

sin crear otra estructura.

---

## 55. Evidence Granularity

La Evidence debe ser:

```text
specific enough to review
but
not so detailed that the assessment becomes code documentation
```

No es necesario registrar cada línea relevante de código.

El objetivo es permitir que otro reviewer pueda localizar la base de la evaluación.

Cuando un artifact completo sea suficiente:

```text
file reference
```

puede bastar.

Cuando solo una parte sea relevante:

```text
file + section
file + class
file + configuration key
```

es preferible.

---

## 56. State Field

`State` debe contener exactamente uno de:

```text
Satisfied
Partial
Missing
```

No se introducirán subestados durante Version 0.

Casos como:

```text
Mostly Satisfied
Nearly Missing
Partially Satisfied
```

deben expresarse mediante:

```text
State
+
Evaluation Rationale
```

y no ampliando prematuramente el vocabulario.

---

## 57. Applicability Field

`Applicability` debe contener exactamente uno de:

```text
Applicable
Not Applicable
Uncertain
```

No debe omitirse porque el State parezca suficiente.

Especialmente:

```text
Missing
```

siempre debe seguir evaluándose respecto a Applicability.

---

## 58. Implementation Characteristics Field

El campo admite múltiples valores:

```text
Canonical
Own
Equivalent
Specialized
Distributed
```

Formato:

```markdown
- **Implementation Characteristics:** `Own`, `Distributed`
```

Si no se observa una implementación relevante:

```markdown
- **Implementation Characteristics:** None observed
```

`None observed` no constituye un nuevo valor formal del modelo.

Solo indica ausencia de características aplicables que registrar.

---

## 59. Uncertainty Field

Cuando no exista incertidumbre material:

```markdown
- **Uncertainty:** None
```

Cuando exista:

```markdown
- **Uncertainty:** The repository shows deployment configuration but does not provide enough evidence to determine whether it represents the current production model.
```

No se define un nivel numérico o categórico de uncertainty en Version 0.

Por tanto no se utilizarán:

```text
Low
Medium
High
```

salvo que el experimento demuestre una necesidad real.

---

## 60. Evaluation Rationale Field

Evaluation Rationale debe explicar conjuntamente, cuando sea necesario:

```text
State
Applicability
Implementation Characteristics
Uncertainty
```

pero sin decidir todavía la acción futura.

Ejemplo:

```markdown
### Evaluation Rationale

The repository describes its primary technologies and persistence stack, so the
technical stack responsibility is substantially covered. However, several
runtime dependencies required for local execution are not explained, therefore
the responsibility is evaluated as Partial rather than Satisfied.
```

---

## 61. Adoption Decision Field

Debe contener exactamente una decisión del vocabulario provisional:

```text
PRESERVE
ADAPT
ADD
ACCEPT
EVALUATE
JUSTIFY
OMIT
```

Formato:

```markdown
### Adoption Decision

`ADAPT`
```

La decisión no debe combinarse:

```text
ADAPT / ADD
PRESERVE + JUSTIFY
```

Si aparece necesidad real de decisiones múltiples, debe registrarse como:

```text
representation friction
```

antes de modificar la plantilla.

---

## 62. Decision Rationale Field

Debe justificar la decisión sin repetir simplemente el State.

Ejemplo incorrecto:

```markdown
### Decision Rationale

The responsibility is Partial, therefore ADAPT.
```

Ejemplo preferido:

```markdown
### Decision Rationale

The existing documentation provides a useful base and should be retained, but
it needs additional local setup information to satisfy the responsibility
without replacing the current repository structure.
```

Esto mantiene:

```text
State
    ≠
Decision
```

---

## 63. Handling Not Applicable Responsibilities

Una Responsibility `Not Applicable` debe seguir apareciendo en:

```text
Summary Table
Responsibility Detail
```

No debe eliminarse del assessment.

Ejemplo:

```markdown
- **State:** Missing
- **Applicability:** Not Applicable
```

puede ser perfectamente válido.

El Detail debe explicar:

```text
why the responsibility is not applicable
```

y la decisión puede ser, según contexto:

```text
OMIT
JUSTIFY
```

sin mapping automático.

---

## 64. Handling Uncertain Responsibilities

Cuando Applicability o evaluación no pueda cerrarse de forma fiable:

```text
Uncertainty
```

debe hacerse visible.

Version 0 permite que una Responsibility termine provisionalmente con:

```text
EVALUATE
```

cuando la decisión no pueda cerrarse con la Evidence disponible.

Esto permitirá observar durante el experimento si:

```text
EVALUATE
```

funciona realmente como Adoption Decision final o como workflow state transicional.

Ese comportamiento debe registrarse como hallazgo y no resolverse anticipadamente.

---

## 65. Handling Missing Evidence

Cuando no se encuentre Evidence:

```markdown
### Evidence

- No repository evidence identified.
```

No debe dejarse el campo vacío.

Esto distingue:

```text
Evidence not found
```

de:

```text
assessment not completed
```

---

## 66. Handling Distributed Evidence

Cuando la Responsibility se satisfaga mediante información repartida:

```markdown
- **Implementation Characteristics:** `Distributed`
```

y Evidence debe listar las principales localizaciones.

No es necesario consolidar artificialmente la información antes del assessment.

El assessment debe representar el consumer:

```text
as it exists
```

no como debería quedar después de la adopción.

---

## 67. Handling Equivalent Implementations

Una estructura diferente de la forma canónica puede seguir evaluándose como:

```text
Satisfied
+
Equivalent
```

si la Responsibility se cubre de forma suficiente.

La plantilla no debe generar:

```text
ADAPT
```

únicamente porque exista:

```text
Equivalent
```

Esto permite observar una de las propiedades centrales del modelo:

```text
semantic satisfaction
    ≠
canonical materialization
```

---

## 68. Requirement Ordering

Version 0 conservará el orden del Repository Template.

Para `TPL-BACKEND v0.1.0`:

```text
Required
    ↓
Recommended
    ↓
Optional
```

y dentro de cada grupo se preservará el orden establecido por el template.

Esto favorece:

```text
comparability
review consistency
traceability
```

sin introducir una clasificación adicional.

---

## 69. Assessment Progress

Mientras el assessment esté incompleto, la cabecera debe indicar:

```markdown
- **Assessment Status:** In Progress
```

Cuando todas las Responsibilities hayan sido evaluadas:

```markdown
- **Assessment Status:** Completed
```

`Completed` significa:

```text
assessment representation completed
```

No:

```text
adoption completed
repository changes applied
```

---

## 70. Experimental Observation Log

El Repeatability Experiment necesita registrar problemas de representación sin modificar silenciosamente Version 0.

Por ello, el assessment incluirá al final:

```markdown
## Representation Observations

### Friction

- `<observation or None>`

### Missing Information Slots

- `<observation or None>`

### Redundant Fields

- `<observation or None>`

### Workarounds

- `<observation or None>`

### Template Deviations

- `<observation or None>`

### Unexpected Information Needs

- `<observation or None>`
```

Esta sección pertenece al experimento de repeatability.

No forma parte necesariamente de una futura representación estable de adoption assessment.

---

## 71. Observation Discipline

Los problemas deben registrarse cuando aparezcan.

No deben reinterpretarse retrospectivamente únicamente al final.

Ejemplo:

```markdown
### Friction

- `README-ARCHITECTURE`: the current Evidence field can reference multiple files,
  but it is difficult to distinguish evidence supporting State from evidence
  supporting Implementation Characteristics.
```

Registrar una observación no implica automáticamente:

```text
template change required
```

Primero debe evaluarse si representa:

```text
local inconvenience
repeated friction
structural weakness
```

---

## 72. Assessment Closing Section

Al finalizar el assessment se añadirá:

```markdown
## Assessment Outcome

### Representation Result

`<MODEL HOLDS | REFINEMENT NEEDED | MODEL CONTRADICTION>`

### Result Rationale

`<evidence-based explanation>`

### Observed Refinements

- `<refinement or None>`

### Structural Changes Required

- `<change or None>`

### Repeatability Conclusion

`<whether Version 0 could support the complete assessment without material redesign>`
```

Este resultado evalúa:

```text
the representation
```

no:

```text
the quality of the consumer repository
```

---

## 73. Full Version 0 Skeleton

La plantilla completa queda conceptualmente:

```markdown
# Adoption Assessment

## Assessment Context

- Consumer
- Repository Template
- Assessment Type
- Assessment Representation
- Assessment Date
- Repository Reference
- Assessment Status

## Scope

...

## Summary

| Responsibility | Requirement Level | State | Applicability | Adoption Decision |
|---|---|---|---|---|

### Aggregate Results

...

## `<Responsibility ID>` — `<Responsibility Name>`

- Requirement Level
- State
- Applicability
- Implementation Characteristics
- Uncertainty

### Detected Facts

...

### Evidence

...

### Evaluation Rationale

...

### Adoption Decision

...

### Decision Rationale

...

[repeat for every Responsibility]

## Representation Observations

### Friction
...

### Missing Information Slots
...

### Redundant Fields
...

### Workarounds
...

### Template Deviations
...

### Unexpected Information Needs
...

## Assessment Outcome

### Representation Result
...

### Result Rationale
...

### Observed Refinements
...

### Structural Changes Required
...

### Repeatability Conclusion
...
```

---

## 74. Template Minimality Check

Version 0 incorpora únicamente las dimensiones ya justificadas por Discovery:

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
Adoption Decision
Decision Rationale
```

La estructura adicional:

```text
Assessment Context
Summary
Representation Observations
Assessment Outcome
```

sirve respectivamente para:

```text
traceability
review
experimental observation
experiment conclusion
```

No introduce un nuevo modelo conceptual del consumer.

---

## 75. Representation Freeze — Version 0

Con las secciones 22–74 quedan definidos y congelados:

```text
Minimal Adoption Guide — Version 0
        +
Structured Markdown Assessment Template — Version 0
```

A partir de este punto:

```text
do not redesign first
```

El assessment de `dental-back-spring` deberá utilizar esta representación.

Cualquier problema encontrado deberá registrarse primero en:

```text
Representation Observations
```

antes de considerar cambios.

---

## 76. Experimental Baseline

El baseline del Repeatability Experiment queda:

```text
Consumer
    fran-eliot/dental-back-spring

Repository Template
    TPL-BACKEND v0.1.0

Guide
    Minimal Adoption Guide — Version 0

Assessment Representation
    Structured Markdown Assessment Template — Version 0

Representation Status
    Frozen for experiment

Primary Question
    Can Version 0 support a complete assessment
    without material redesign?
```

---

## 77. Next Step

La siguiente fase ya puede comenzar:

```text
ANALYZE
    dental-back-spring
        ↓
ASSESS
    all 28 TPL-BACKEND Responsibilities
        ↓
RECORD
    Representation Observations
```

El análisis debe comenzar desde Evidence del repositorio y no desde expectativas sobre cómo debería estar organizado.

No se modificarán todavía:

```text
Guide Version 0
Template Version 0
provisional adoption model
decision vocabulary
```

salvo que el experimento produzca evidencia que posteriormente justifique una revisión.

---

## 78. Assessment Execution — Baseline

El assessment comienza sobre:

```text
Consumer
    fran-eliot/dental-back-spring

Repository Template
    TPL-BACKEND v0.1.0

Repository Reference
    main
    e17b009602f25da0d6f32920180254eb9392fee2

Assessment Representation
    Structured Markdown Assessment — Version 0

Assessment Status
    In Progress
```

La evidencia inicial procede exclusivamente del repository consumer.

---

## 79. Repository Facts — Initial Scan

La inspección inicial identifica en la raíz:

```text
README.md
pom.xml
src/
.mvn/
.gitignore
.gitattributes
```

No se observan en la raíz:

```text
CHANGELOG.md
docs/
Dockerfile
docker-compose.yml
GitHub Actions workflows
```

El árbol contiene además:

```text
src/doc/
src/main/java/
src/main/resources/
src/test/java/
```

`src/doc/` contiene principalmente diagramas y capturas de pantalla.

---

## 80. Technical Facts — Initial Scan

`pom.xml` declara, entre otras, dependencias para:

```text
Spring Boot Web
Spring Security
Spring Data JPA
Spring Data MongoDB
Validation
MySQL
JWT
Springdoc OpenAPI
Testing
```

La aplicación utiliza Java 17.

`application.properties` configura:

```text
server.port=8080
MySQL
MongoDB
JPA
JWT
OpenAPI / Swagger
```

Existe una arquitectura de código organizada, entre otros, mediante:

```text
controller
service
repository
entity
dto
config
security
mongo
```

Existe un único test observado inicialmente:

```text
DentalBackSpringApplicationTests
    contextLoads()
```

---

## 81. Important Documentation Inconsistency

La inspección detecta una inconsistencia relevante entre README y repository implementation.

El README indica:

```text
cd backend
mvn clean install
mvn spring-boot:run
```

y documenta el backend en:

```text
http://localhost:3000
```

Sin embargo:

```text
backend/
```

no existe en este repository y `application.properties` configura:

```text
server.port=8080
```

Esto constituye Evidence importante para:

```text
README-QUICK-START
```

y demuestra que:

```text
documentation presence
    ≠
responsibility satisfaction
```

---

# Required Responsibilities Assessment

## 82. README-HERO — Project Identity

- **Requirement Level:** Required
- **State:** Partial
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`
- **Uncertainty:** None

### Detected Facts

- `README.md` comienza con un H1: `SMYLE: CLÍNICA DENTAL — README`.
- Inmediatamente después aparecen autor y referencia al curso.
- No se observa un tagline breve diferenciado.
- No se observan badges principales.
- La descripción del producto comienza posteriormente en `1. Introducción General`.

### Evidence

- `README.md` — cabecera inicial.
- `README.md` — sección `1. Introducción General`.

### Evaluation Rationale

El repositorio identifica claramente el proyecto mediante un H1 y ofrece contexto suficiente para reconocerlo.

Sin embargo, la cabecera funciona parcialmente como identidad del proyecto y parcialmente como identificación del documento y del contexto formativo.

No existe una presentación concisa equivalente a:

```text
Project Name
+
Tagline
+
brief identity
```

antes de comenzar la documentación extensa.

La Responsibility está por tanto cubierta, pero no de forma suficientemente completa para considerarla `Satisfied`.

### Adoption Decision

`ADAPT`

### Decision Rationale

La cabecera actual constituye una base válida y debe conservar la identidad `SMYLE: Clínica Dental`, pero puede adaptarse para presentar de forma más directa el producto y separar el contexto académico de la identidad principal del repository.

---

## 83. README-OVERVIEW — Project Purpose

- **Requirement Level:** Required
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`
- **Uncertainty:** None

### Detected Facts

La sección `1. Introducción General` explica:

- que Dental Clinic es una solución para gestión integral de una clínica dental;
- el objetivo general del sistema;
- los principales módulos funcionales;
- que el proyecto incluye backend, frontend, seguridad y persistencia.

### Evidence

- `README.md` — `1. Introducción General`.

### Evaluation Rationale

La documentación responde claramente a:

```text
what the project is
what it is for
what problem/domain it addresses
```

sin depender de inspeccionar el código.

Aunque incluye alguna información técnica, el propósito funcional del proyecto resulta comprensible.

### Adoption Decision

`PRESERVE`

### Decision Rationale

La Overview existente cumple la responsabilidad y no necesita una sustitución estructural.

---

## 84. README-FEATURES — Main Capabilities

- **Requirement Level:** Required
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`, `Distributed`
- **Uncertainty:** None

### Detected Facts

El README presenta capacidades como:

- gestión de pacientes;
- gestión de profesionales;
- agenda diaria y semanal;
- citas;
- disponibilidades;
- autenticación JWT;
- administración;
- tratamientos.

Además dedica secciones específicas a:

```text
Disponibilidades
Citas
MongoDB
API endpoints
```

### Evidence

- `README.md` — `1. Introducción General`.
- `README.md` — `7. Backend — Módulo de Disponibilidades`.
- `README.md` — `8. Backend — Módulo de Citas`.
- `README.md` — `9. Backend — Módulo MongoDB`.
- `README.md` — `10. API REST — Endpoints más importantes`.

### Evaluation Rationale

Las capacidades principales están explícitamente documentadas.

La información no está materializada como un único componente `Features`, sino distribuida entre la introducción y varias secciones funcionales.

Esto no impide la satisfacción semántica de la Responsibility.

### Adoption Decision

`ACCEPT`

### Decision Rationale

La implementación es distinta de una sección canónica de Features, pero comunica adecuadamente las capacidades del sistema.

No existe evidencia suficiente para exigir una reorganización únicamente por formato.

---

## 85. README-TECH-STACK — Technology Stack

- **Requirement Level:** Required
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`, `Distributed`
- **Uncertainty:** None

### Detected Facts

El README documenta:

```text
Angular 17
Spring Boot 3
MySQL
MongoDB
Java 17
Node.js 18+
Angular CLI
Maven
JWT
Swagger
```

La información aparece distribuida principalmente entre:

```text
Arquitectura General
Requisitos
Configuración del Sistema
```

### Evidence

- `README.md` — `2. Arquitectura General del Proyecto`.
- `README.md` — `3.1. Requisitos`.
- `README.md` — `4. Configuración del Sistema`.
- `pom.xml`.

### Evaluation Rationale

El stack principal puede identificarse claramente a partir del README y es consistente en gran medida con las dependencias observadas en `pom.xml`.

No existe una sección explícita denominada Tech Stack, pero la Responsibility se satisface semánticamente mediante información distribuida.

### Adoption Decision

`ACCEPT`

### Decision Rationale

La estructura existente comunica suficientemente el stack tecnológico.

Una sección canónica podría mejorar scanability, pero no existe evidencia suficiente para exigirla como acción necesaria.

---

## 86. README-QUICK-START — First Execution

- **Requirement Level:** Required
- **State:** Partial
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`
- **Uncertainty:** None

### Detected Facts

El README documenta:

```text
Java 17
Node.js 18+
Angular CLI
MySQL
MongoDB
Maven
```

y proporciona comandos para instalación y ejecución.

Sin embargo, para backend indica:

```text
cd backend
```

aunque no existe un directorio `backend/` en este repository.

También indica:

```text
http://localhost:3000
```

mientras `application.properties` contiene:

```text
server.port=8080
```

### Evidence

- `README.md` — `3. Instalación del Proyecto`.
- `README.md` — `3.2. Instalación del Backend`.
- repository root.
- `src/main/resources/application.properties`.

### Evaluation Rationale

La sección intenta responder correctamente a:

```text
What do I need?
How do I install it?
How do I run it?
```

pero contiene instrucciones incompatibles con el estado actual del repository.

Por tanto, la Responsibility existe materialmente pero no puede considerarse completamente satisfecha.

### Adoption Decision

`ADAPT`

### Decision Rationale

La documentación actual proporciona una base útil y debe conservarse, pero necesita alinearse con la estructura real del repository y con el puerto configurado actualmente.

---

## 87. README-DOCUMENTATION — Documentation Access

- **Requirement Level:** Required
- **State:** Partial
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`, `Distributed`
- **Uncertainty:** None

### Detected Facts

El README actúa explícitamente como:

```text
README
memoria técnica
guía de presentación
```

y contiene documentación extensa sobre:

```text
architecture
database
security
business modules
API
Swagger
frontend
system flow
future improvements
```

También referencia artifacts de `src/doc/`.

No existe una sección específica que agrupe o indexe la documentación disponible.

Tampoco se observa un directorio dedicado con documentos Markdown de arquitectura, API, testing, security u otras áreas.

### Evidence

- `README.md`.
- `src/doc/`.
- repository tree.

### Evaluation Rationale

El repository dispone de una cantidad significativa de documentación, pero ésta está concentrada dentro del propio README y en artifacts gráficos.

La Responsibility de proporcionar acceso organizado a documentación profunda está cubierta parcialmente, porque existe contenido técnico relevante pero no un mecanismo claro de navegación documental.

### Adoption Decision

`ADAPT`

### Decision Rationale

No parece necesario crear documentación por formalismo, pero sí conviene mejorar la capacidad del README para identificar y enlazar las fuentes documentales reales del proyecto.

---

## 88. README-FOOTER — Closing Information

- **Requirement Level:** Required
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`
- **Uncertainty:** None

### Detected Facts

La última sección del README es:

```text
15. Contacto
```

Incluye:

```text
Fran Ramírez
GitHub
LinkedIn
```

### Evidence

- `README.md` — `15. Contacto`.

### Evaluation Rationale

La sección final cumple la función de cierre del README y proporciona información de autor/contacto.

No es necesario que incluya todos los elementos posibles de un footer para satisfacer su responsabilidad.

### Adoption Decision

`PRESERVE`

### Decision Rationale

La implementación existente cumple adecuadamente la función de cierre.

---

## 89. DOC-CHANGELOG — Published Change History

- **Requirement Level:** Required
- **State:** Missing
- **Applicability:** Applicable
- **Implementation Characteristics:** None observed
- **Uncertainty:** None

### Detected Facts

No se observa:

```text
CHANGELOG.md
```

ni otro documento equivalente dedicado al historial estructurado de cambios publicados.

El repository contiene una versión Maven:

```text
0.0.1-SNAPSHOT
```

pero no existe evidencia de un Changelog estructurado.

### Evidence

- repository root.
- repository tree.
- `pom.xml`.

### Evaluation Rationale

No existe Evidence de una implementación equivalente a `DOC-CHANGELOG`.

El repository es un proyecto público y representativo del portfolio, por lo que disponer de un historial de cambios puede resultar aplicable si continúa evolucionando.

La ausencia del artifact no se interpreta únicamente como ausencia de archivo, sino como ausencia de Evidence de la Responsibility correspondiente.

### Adoption Decision

`ADD`

### Decision Rationale

No existe una base documental equivalente que preservar o adaptar.

La Responsibility debe añadirse si el repository continúa manteniendo evolución identificable y cambios relevantes para consumidores o reviewers.

---

## 90. Required Responsibilities — Summary

| Responsibility | Requirement Level | State | Applicability | Adoption Decision |
|---|---|---|---|---|
| README-HERO | Required | Partial | Applicable | ADAPT |
| README-OVERVIEW | Required | Satisfied | Applicable | PRESERVE |
| README-FEATURES | Required | Satisfied | Applicable | ACCEPT |
| README-TECH-STACK | Required | Satisfied | Applicable | ACCEPT |
| README-QUICK-START | Required | Partial | Applicable | ADAPT |
| README-DOCUMENTATION | Required | Partial | Applicable | ADAPT |
| README-FOOTER | Required | Satisfied | Applicable | PRESERVE |
| DOC-CHANGELOG | Required | Missing | Applicable | ADD |

### Aggregate State — Required

| State | Count |
|---|---:|
| Satisfied | 4 |
| Partial | 3 |
| Missing | 1 |

### Aggregate Decision — Required

| Decision | Count |
|---|---:|
| PRESERVE | 2 |
| ACCEPT | 2 |
| ADAPT | 3 |
| ADD | 1 |

---

## 91. Representation Observations — Required Set

### Friction

No structural friction has been identified so far.

The Version 0 representation can express:

```text
Satisfied
Partial
Missing
Own
Distributed
no implementation observed
evaluation rationale
decision rationale
```

without requiring an additional field.

### Missing Information Slots

None observed so far.

### Redundant Fields

None demonstrated so far.

### Workarounds

None required.

### Template Deviations

None required.

### Unexpected Information Needs

A useful distinction emerged between:

```text
documentation exists
```

and:

```text
documentation is operationally correct
```

This was expressible through:

```text
Detected Facts
+
Evidence
+
State
+
Evaluation Rationale
```

and therefore does not currently require a new assessment dimension.

---

## 92. Interim Experimental Finding

The first eight Responsibilities provide initial evidence that Version 0 can represent cases with materially different semantics:

```text
existing and adequate
existing but non-canonical
existing but distributed
existing but inaccurate
partially organized documentation
fully absent responsibility
```

without changing the assessment structure.

This is provisional evidence in favor of:

```text
representation stability
```

but no Repeatability Experiment result should be assigned until all 28 Responsibilities have been assessed.

---

## 93. README-STATUS — Project Status and Maturity

- **Requirement Level:** Recommended
- **State:** Missing
- **Applicability:** Applicable
- **Implementation Characteristics:** None observed
- **Uncertainty:** None

### Detected Facts

El README identifica:

- el proyecto;
- su origen académico/profesional;
- funcionalidades actuales;
- mejoras futuras.

No se observa una sección que comunique explícitamente:

```text
current project status
maturity
maintenance state
release status
```

Tampoco se observan badges o indicadores equivalentes de estado operativo.

### Evidence

- `README.md` — cabecera inicial.
- `README.md` — `14. Mejoras Futuras`.
- repository root.

### Evaluation Rationale

La existencia de futuras mejoras no equivale a describir el estado actual del proyecto.

Un lector puede comprender qué hace el sistema, pero no puede determinar claramente si el repository debe interpretarse como:

```text
active
stable
experimental
academic reference
portfolio project
maintenance mode
```

La Responsibility no dispone de Evidence suficiente para considerarse cubierta.

### Adoption Decision

`ADD`

### Decision Rationale

El proyecto forma parte del portfolio público y presenta una implementación suficientemente desarrollada para que una indicación breve de estado y madurez mejore su interpretación sin introducir documentación pesada.

---

## 94. README-ARCHITECTURE — Architecture Summary

- **Requirement Level:** Recommended
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`, `Distributed`, `Equivalent`
- **Uncertainty:** None

### Detected Facts

El README contiene:

- una sección `2. Arquitectura General del Proyecto`;
- separación entre frontend, backend y bases de datos;
- una sección `6. Backend — Arquitectura Interna`;
- patrón `Controller → Service → Repository`;
- descripción de controladores;
- descripción de servicios;
- descripción de seguridad;
- flujo funcional general del sistema.

### Evidence

- `README.md` — `2. Arquitectura General del Proyecto`.
- `README.md` — `6. Backend — Arquitectura Interna`.
- `README.md` — `13. Flujo completo del sistema`.
- repository package structure.

### Evaluation Rationale

La arquitectura general puede comprenderse sin inspeccionar previamente todo el código.

Aunque la información está distribuida y parte del README describe también el frontend, el backend dispone de una explicación arquitectónica suficiente a nivel de resumen.

La implementación no sigue una sección canónica única denominada `Architecture`, pero cubre semánticamente la Responsibility.

### Adoption Decision

`ACCEPT`

### Decision Rationale

La representación existente cumple el objetivo de proporcionar una visión arquitectónica breve.

Una reorganización podría mejorar claridad, pero no existe evidencia de que sea necesaria para satisfacer esta Responsibility.

---

## 95. README-REPOSITORY-STRUCTURE — Repository Structure

- **Requirement Level:** Recommended
- **State:** Partial
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`, `Distributed`
- **Uncertainty:** None

### Detected Facts

El README contiene una representación explícita de:

```text
src/app
```

para el frontend Angular.

Para el backend explica conceptualmente:

```text
Controller
Service
Repository
DTO
Security
```

pero no proporciona una representación de la estructura física real del repository backend.

El árbol real contiene, entre otros:

```text
src/main/java/com/clinica/dental_back_spring/
    config/
    controller/
    converter/
    dto/
    entity/
    enums/
    mongo/
    repository/
    security/
    service/

src/main/resources/
src/test/java/
src/doc/
```

### Evidence

- `README.md` — `6. Backend — Arquitectura Interna`.
- `README.md` — `12.1. Estructura del proyecto`.
- repository tree.

### Evaluation Rationale

La documentación permite inferir parcialmente cómo está organizado el backend mediante sus capas y componentes.

Sin embargo, la única estructura física presentada explícitamente corresponde al frontend y no al repository evaluado.

Por tanto, la Responsibility está parcialmente cubierta, pero no permite a un nuevo contributor orientarse con precisión dentro del backend.

### Adoption Decision

`ADAPT`

### Decision Rationale

Ya existe suficiente explicación conceptual para servir de base.

La mejora adecuada sería incorporar una representación breve de la estructura real del backend, no sustituir la documentación existente.

---

## 96. README-TESTING — Testing Summary

- **Requirement Level:** Recommended
- **State:** Missing
- **Applicability:** Applicable
- **Implementation Characteristics:** None observed
- **Uncertainty:** None

### Detected Facts

El README no contiene una sección dedicada a testing.

No se documentan:

```text
unit tests
integration tests
E2E tests
coverage
static analysis
test execution
```

`pom.xml` declara:

```text
spring-boot-starter-test
spring-security-test
```

El repository contiene:

```text
DentalBackSpringApplicationTests
```

con un único test:

```text
contextLoads()
```

### Evidence

- `README.md`.
- `pom.xml`.
- `src/test/java/com/clinica/dental_back_spring/DentalBackSpringApplicationTests.java`.

### Evaluation Rationale

La existencia de dependencias de testing y un test de carga de contexto demuestra capacidad técnica para ejecutar pruebas, pero no satisface la Responsibility documental de resumir la estrategia de testing.

No existe Evidence de una explicación sobre qué se prueba, cómo ejecutar tests o cuál es su alcance actual.

### Adoption Decision

`ADD`

### Decision Rationale

La documentación debería reflejar de forma proporcional el estado real del testing.

No es necesario presentar una estrategia madura inexistente; una sección breve que explique el test actual y cómo ejecutarlo sería suficiente como punto de partida.

---

## 97. DOC-ARCHITECTURE — Detailed Architecture Documentation

- **Requirement Level:** Recommended
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Equivalent`, `Own`, `Distributed`
- **Uncertainty:** None

### Detected Facts

No existe un documento separado equivalente a:

```text
ARCHITECTURE.md
docs/architecture.md
```

Sin embargo, el `README` documenta:

- contexto general del sistema;
- división frontend/backend/databases;
- arquitectura interna del backend;
- componentes principales;
- servicios;
- seguridad;
- reglas funcionales;
- flujos del sistema.

El propio README declara actuar como:

```text
README
memoria técnica
guía de presentación
```

### Evidence

- `README.md` — `2. Arquitectura General del Proyecto`.
- `README.md` — `6. Backend — Arquitectura Interna`.
- `README.md` — secciones funcionales 7–10.
- `README.md` — `13. Flujo completo del sistema`.

### Evaluation Rationale

La Responsibility de documentar la arquitectura resulta aplicable y está cubierta semánticamente mediante el README.

El contrato de `DOC-ARCHITECTURE` establece que un documento separado puede no ser necesario cuando la arquitectura puede explicarse suficientemente dentro del README.

Por tanto:

```text
Architecture Responsibility
    Applicable
    +
    Satisfied

Canonical Dedicated Document
    Not required
```

La ausencia de un artifact `DOC-ARCHITECTURE` canónico no convierte la Responsibility en `Not Applicable`.

### Adoption Decision

```text
ACCEPT
```

### Decision Rationale

La implementación equivalente dentro del README debe aceptarse mientras siga siendo suficiente para comprender la arquitectura vigente.

No se justifica crear un documento separado únicamente para adoptar una materialización canónica.

---

## 98. DOC-PROJECT-STATUS — Current Project Status

- **Requirement Level:** Recommended
- **State:** Missing
- **Applicability:** Not Applicable
- **Implementation Characteristics:** None observed
- **Uncertainty:** None

### Detected Facts

No se observa un documento dedicado al estado del proyecto.

El README contiene:

```text
14. Mejoras Futuras
```

pero no mantiene:

```text
current work
current milestone
active iteration
current risks
immediate objectives
version focus
```

### Evidence

- `README.md`.
- repository tree.

### Evaluation Rationale

No existe Evidence de una implementación de `DOC-PROJECT-STATUS`.

Sin embargo, tampoco se observa en el repository un modelo de evolución continua que requiera actualmente una fotografía operativa separada y mantenida periódicamente.

El proyecto puede comunicar su estado de forma más ligera mediante `README-STATUS`.

Por tanto:

```text
State
    Missing

Applicability
    Not Applicable
```

son compatibles.

### Adoption Decision

`OMIT`

### Decision Rationale

Crear un Project Status dedicado introduciría mantenimiento documental sin evidencia actual de una necesidad proporcional.

Si el proyecto entra posteriormente en una fase de evolución activa con milestones, releases o trabajo continuado, Applicability deberá reevaluarse.

---

## 99. DOC-TESTING — Detailed Testing Documentation

- **Requirement Level:** Recommended
- **State:** Missing
- **Applicability:** Not Applicable
- **Implementation Characteristics:** None observed
- **Uncertainty:** None

### Detected Facts

No existe un documento dedicado a testing.

La implementación de pruebas observada se limita actualmente a:

```text
DentalBackSpringApplicationTests
    contextLoads()
```

No se observa una suite suficientemente amplia con:

```text
test categories
coverage policy
test architecture
fixtures
integration strategy
E2E strategy
quality gates
```

### Evidence

- repository tree.
- `src/test/java/com/clinica/dental_back_spring/DentalBackSpringApplicationTests.java`.
- `pom.xml`.

### Evaluation Rationale

La Responsibility documental detallada está ausente.

Sin embargo, el alcance actual del testing no presenta suficiente complejidad para justificar un documento especializado.

La necesidad inmediata puede cubrirse proporcionalmente mediante `README-TESTING`.

Por tanto:

```text
README-TESTING
    Applicable

DOC-TESTING
    Not Applicable at current complexity
```

### Adoption Decision

`OMIT`

### Decision Rationale

Añadir documentación especializada de testing en el estado actual produciría probablemente más estructura que información útil.

La Applicability debería revisarse si la estrategia de pruebas crece materialmente.

---

## 100. Recommended Responsibilities — Summary

| Responsibility | Requirement Level | State | Applicability | Adoption Decision |
|---|---|---|---|---|
| README-STATUS | Recommended | Missing | Applicable | ADD |
| README-ARCHITECTURE | Recommended | Satisfied | Applicable | ACCEPT |
| README-REPOSITORY-STRUCTURE | Recommended | Partial | Applicable | ADAPT |
| README-TESTING | Recommended | Missing | Applicable | ADD |
| DOC-ARCHITECTURE | Recommended | Satisfied | Applicable | ACCEPT |
| DOC-PROJECT-STATUS | Recommended | Missing | Not Applicable | OMIT |
| DOC-TESTING | Recommended | Missing | Not Applicable | OMIT |

### Aggregate State — Recommended

| State | Count |
|---|---:|
| Satisfied | 2 |
| Partial | 1 |
| Missing | 4 |

### Aggregate Applicability — Recommended

| Applicability | Count |
|---|---:|
| Applicable | 5 |
| Not Applicable | 2 |
| Uncertain | 0 |

### Aggregate Decision — Recommended

| Decision | Count |
|---|---:|
| ACCEPT | 2 |
| ADAPT | 1 |
| ADD | 2 |
| OMIT | 2 |

---

## 101. Representation Observations — Recommended Set

### Friction

No structural friction has required changes to Version 0.

The Recommended set instead exposed an important clarification:

```text
Responsibility Applicability
    ≠
Canonical Artifact Necessity
```

A Responsibility may be:

```text
Applicable
+
Satisfied
+
Equivalent
+
ACCEPT
```

even when the canonical dedicated artifact does not exist and does not need to be created.

`DOC-ARCHITECTURE` demonstrates this case.

### Missing Information Slots

None observed.

### Redundant Fields

No field has yet proven redundant.

In particular:

```text
State
    ≠
Applicability
    ≠
Implementation Characteristics
    ≠
Adoption Decision
```

remains necessary.

### Workarounds

None required.

### Template Deviations

None required.

### Unexpected Information Needs

The assessment required distinguishing between:

```text
responsibility is relevant
```

and:

```text
canonical materialization is necessary
```

The existing combination of:

```text
State
Applicability
Implementation Characteristics
Evaluation Rationale
Adoption Decision
Decision Rationale
```

was sufficient.

No new dimension is required.

---

## 102. Interim Experimental Finding — Recommended Set

The Recommended Responsibilities introduce cases such as:

```text
Satisfied + Applicable
Partial + Applicable
Missing + Applicable
Missing + Not Applicable
```

Version 0 can represent all of them without structural changes.

Particularly important is:

```text
Missing
    ≠
ADD
```

demonstrated by:

```text
DOC-PROJECT-STATUS
DOC-TESTING
```

and:

```text
canonical artifact absent
    ≠
responsibility unsatisfied
```

demonstrated by:

```text
DOC-ARCHITECTURE
```

This provides additional provisional evidence in favor of:

```text
State independence
Applicability independence
semantic responsibility assessment
representation stability
```

No modification to the frozen representation is justified at this point.

---

## 103. README-ROADMAP — Future Direction

- **Requirement Level:** Optional
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Equivalent`, `Own`
- **Uncertainty:** None

### Detected Facts

El README contiene:

```text
14. Mejoras Futuras
```

con elementos como:

- notificaciones por email;
- recordatorios automáticos;
- pasarela de pago;
- integración con apps móviles;
- panel BI con métricas.

### Evidence

- `README.md` — `14. Mejoras Futuras`.

### Evaluation Rationale

Aunque no existe una sección denominada formalmente `Roadmap`, el README comunica explícitamente líneas futuras de evolución.

La Responsibility está cubierta a un nivel proporcional al proyecto.

### Adoption Decision

`ACCEPT`

### Decision Rationale

La representación actual es suficiente para comunicar la dirección futura sin introducir un roadmap más formal que no parece necesario en el estado actual.

---

## 104. README-CONTRIBUTING — Contribution Guidance

- **Requirement Level:** Optional
- **State:** Missing
- **Applicability:** Not Applicable
- **Implementation Characteristics:** None observed
- **Uncertainty:** None

### Detected Facts

No se observa:

```text
CONTRIBUTING.md
```

ni una sección del README dedicada a:

```text
contribution workflow
branching
pull requests
coding standards
local contribution setup
```

### Evidence

- repository root.
- `README.md`.

### Evaluation Rationale

La Responsibility está ausente.

Sin embargo, el repository no presenta actualmente Evidence de funcionar como proyecto abierto a contribución externa o con un workflow colaborativo público que requiera una guía específica.

### Adoption Decision

`OMIT`

### Decision Rationale

Añadir contribution guidance sin una necesidad colaborativa real introduciría documentación especulativa.

La Applicability deberá reevaluarse si el repository empieza a aceptar contribuciones externas o desarrolla un workflow público estable.

---

## 105. README-DEMO — Demonstration

- **Requirement Level:** Optional
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Equivalent`, `Distributed`
- **Uncertainty:** None

### Detected Facts

El README incluye numerosas capturas de la aplicación, entre ellas:

```text
Swagger
Login
Gestión de disponibilidades
Listado de citas
Agenda semanal
```

El repository contiene además múltiples imágenes bajo:

```text
src/doc/
```

### Evidence

- `README.md` — `11. Swagger — Documentación Automática`.
- `README.md` — `12.3. Capturas reales incluidas`.
- `src/doc/`.

### Evaluation Rationale

No existe una sección única denominada Demo, pero la documentación muestra visualmente funcionalidades reales del sistema.

La Responsibility de proporcionar una demostración comprensible está cubierta mediante capturas distribuidas.

### Adoption Decision

`ACCEPT`

### Decision Rationale

La demostración existente es suficientemente útil y no necesita reorganizarse únicamente para adoptar una sección canónica.

---

## 106. README-AUTHOR — Author Information

- **Requirement Level:** Optional
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`
- **Uncertainty:** None

### Detected Facts

El README identifica al autor al comienzo y termina con:

```text
15. Contacto
```

incluyendo:

- nombre;
- GitHub;
- LinkedIn.

### Evidence

- `README.md` — cabecera.
- `README.md` — `15. Contacto`.

### Evaluation Rationale

La información requerida para identificar al autor y acceder a sus perfiles está claramente disponible.

### Adoption Decision

`PRESERVE`

### Decision Rationale

La implementación existente cubre adecuadamente esta Responsibility.

---

## 107. README-HIGHLIGHTS — Project Highlights

- **Requirement Level:** Optional
- **State:** Partial
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`, `Distributed`
- **Uncertainty:** None

### Detected Facts

El README destaca indirectamente varios aspectos relevantes:

- módulo de disponibilidades descrito como uno de los más avanzados;
- seguridad JWT;
- arquitectura backend;
- Swagger;
- reglas de negocio de citas;
- MySQL + MongoDB.

Sin embargo, no existe una síntesis breve que identifique los principales puntos diferenciales del proyecto.

### Evidence

- `README.md` — `6. Backend — Arquitectura Interna`.
- `README.md` — `7. Backend — Módulo de Disponibilidades`.
- `README.md` — `8. Backend — Módulo de Citas`.
- `README.md` — `11. Swagger`.

### Evaluation Rationale

Los highlights existen semánticamente, pero están repartidos por el documento.

Un reviewer puede identificarlos, aunque requiere leer una parte considerable del README.

### Adoption Decision

`ADAPT`

### Decision Rationale

La información existente debe conservarse, pero una síntesis más visible podría mejorar la presentación del proyecto como pieza de portfolio sin duplicar contenido técnico.

---

## 108. README-LICENSE — License Information

- **Requirement Level:** Optional
- **State:** Partial
- **Applicability:** Applicable
- **Implementation Characteristics:** `Distributed`
- **Uncertainty:** The OpenAPI configuration declares an MIT License, but no repository-level license artifact was observed.

### Detected Facts

No se observa en la raíz:

```text
LICENSE
LICENSE.md
```

El README no contiene una sección de licencia.

`SwaggerConfig.java` declara:

```text
MIT License
```

dentro de la metadata OpenAPI.

### Evidence

- repository root.
- `README.md`.
- `src/main/java/com/clinica/dental_back_spring/config/SwaggerConfig.java`.

### Evaluation Rationale

Existe una declaración de licencia dentro de la documentación generada de la API, pero no está presentada como información de licencia del repository.

Por tanto, la Responsibility está parcialmente cubierta y existe incertidumbre sobre si esa declaración representa formalmente la licencia del proyecto completo.

### Adoption Decision

`EVALUATE`

### Decision Rationale

Antes de recomendar `PRESERVE`, `ADAPT` o `ADD`, debe aclararse si MIT es realmente la licencia elegida para el repository.

Este caso ofrece una oportunidad real para observar si `EVALUATE` funciona como decisión transicional dentro del modelo.

---

## 109. DOC-ADR — Architecture Decision Records

- **Requirement Level:** Optional
- **State:** Missing
- **Applicability:** Not Applicable
- **Implementation Characteristics:** None observed
- **Uncertainty:** None

### Detected Facts

No se observan ADR ni documentos equivalentes dedicados a conservar:

```text
decision context
alternatives
decision
consequences
```

### Evidence

- repository tree.
- `README.md`.

### Evaluation Rationale

El sistema contiene decisiones arquitectónicas identificables, pero no existe Evidence de que su complejidad histórica requiera actualmente un registro separado de decisiones.

### Adoption Decision

`OMIT`

### Decision Rationale

Introducir ADR retrospectivamente sin una necesidad concreta produciría documentación artificial.

La Responsibility deberá reevaluarse cuando aparezcan decisiones arquitectónicas cuya trazabilidad histórica resulte importante.

---

## 110. DOC-API — API Documentation

- **Requirement Level:** Optional
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Equivalent`, `Distributed`, `Specialized`
- **Uncertainty:** None

### Detected Facts

El README documenta endpoints principales para:

```text
Auth
Users
Professionals
Availabilities
Appointments
```

El proyecto incluye:

```text
springdoc-openapi-starter-webmvc-ui
SwaggerConfig
```

y configura:

```text
/api-docs
/swagger-ui/index.html
```

El README enlaza funcionalmente con Swagger mediante su URL local y captura.

### Evidence

- `README.md` — `10. API REST — Endpoints más importantes`.
- `README.md` — `11. Swagger — Documentación Automática`.
- `pom.xml`.
- `src/main/java/com/clinica/dental_back_spring/config/SwaggerConfig.java`.
- `src/main/resources/application.properties`.

### Evaluation Rationale

La API dispone de documentación humana resumida y documentación especializada generada mediante OpenAPI/Swagger.

No existe un documento `API.md`, pero la Responsibility está cubierta mediante una implementación equivalente y especializada.

### Adoption Decision

`ACCEPT`

### Decision Rationale

La solución actual es más adecuada que duplicar manualmente todos los endpoints en un documento estático.

El README puede seguir proporcionando orientación mientras OpenAPI mantiene el detalle técnico.

---

## 111. DOC-DATABASE — Database Documentation

- **Requirement Level:** Optional
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Equivalent`, `Distributed`
- **Uncertainty:** None

### Detected Facts

El README documenta:

- MySQL como base principal;
- MongoDB como almacenamiento auxiliar;
- principales entidades persistidas;
- configuración de ambas bases;
- propósito de MongoDB;
- un diagrama ER.

El repository contiene:

```text
src/doc/DER-clinica_dental.png
```

### Evidence

- `README.md` — `2. Arquitectura General del Proyecto`.
- `README.md` — `4. Configuración del Sistema`.
- `README.md` — `5. Modelo de Datos (MySQL)`.
- `README.md` — `9. Backend — Módulo MongoDB`.
- `src/doc/DER-clinica_dental.png`.
- entity and repository packages.

### Evaluation Rationale

El modelo de persistencia y las tecnologías utilizadas pueden comprenderse sin inspeccionar exclusivamente el código.

Aunque no existe un documento dedicado, la Responsibility está cubierta de forma equivalente mediante README + diagrama + estructura del proyecto.

### Adoption Decision

`ACCEPT`

### Decision Rationale

No existe evidencia suficiente para justificar duplicar esta información en un documento separado mientras la complejidad siga siendo manejable dentro del README.

---

## 112. DOC-DEPLOYMENT — Deployment Documentation

- **Requirement Level:** Optional
- **State:** Missing
- **Applicability:** Not Applicable
- **Implementation Characteristics:** None observed
- **Uncertainty:** None

### Detected Facts

No se observan:

```text
Dockerfile
docker-compose.yml
deployment manifests
cloud configuration
deployment guide
```

El README documenta únicamente ejecución local.

### Evidence

- repository root.
- repository tree.
- `README.md` — instalación y ejecución local.

### Evaluation Rationale

No existe Evidence de un modelo de deployment diferenciado que necesite documentación especializada.

Ejecutar localmente la aplicación no equivale a disponer de un proceso de deployment.

### Adoption Decision

`OMIT`

### Decision Rationale

No debe añadirse documentación de deployment hasta que exista un mecanismo real que documentar.

---

## 113. DOC-SECURITY — Security Documentation

- **Requirement Level:** Optional
- **State:** Partial
- **Applicability:** Applicable
- **Implementation Characteristics:** `Equivalent`, `Distributed`, `Specialized`
- **Uncertainty:** None

### Detected Facts

El README documenta:

- autenticación JWT;
- roles `ADMIN`, `DENTISTA`, `PACIENTE`;
- rutas públicas y privadas.

El código contiene:

```text
SecurityConfig
JwtFilter
JwtUtil
MyUserDetailsService
```

`SecurityConfig` define reglas de autorización por rutas y roles.

### Evidence

- `README.md` — `2. Arquitectura General del Proyecto`.
- `README.md` — `4.3. Configuración JWT`.
- `README.md` — `6.3. Seguridad`.
- `src/main/java/com/clinica/dental_back_spring/config/SecurityConfig.java`.
- `src/main/java/com/clinica/dental_back_spring/security/`.

### Evaluation Rationale

La seguridad está documentada a nivel funcional y respaldada por una implementación identificable.

Sin embargo, no existe una documentación especializada que explique de forma más completa:

```text
authentication flow
authorization model
security assumptions
credential handling
security limitations
```

Dado el uso de JWT y control de acceso por roles, la Responsibility resulta aplicable.

### Adoption Decision

`ADAPT`

### Decision Rationale

Existe una base significativa que debe conservarse, pero puede mejorarse la documentación de seguridad sin necesidad de crear inicialmente un documento excesivamente extenso.

---

## 114. DOC-DIAGRAMS — Technical Diagrams

- **Requirement Level:** Optional
- **State:** Satisfied
- **Applicability:** Applicable
- **Implementation Characteristics:** `Own`, `Equivalent`
- **Uncertainty:** None

### Detected Facts

El repository contiene:

```text
src/doc/DER-clinica_dental.png
```

y el README incorpora el diagrama dentro de la documentación del modelo de datos.

También existen múltiples capturas, aunque estas no se consideran diagramas técnicos.

### Evidence

- `README.md` — `5. Modelo de Datos (MySQL)`.
- `src/doc/DER-clinica_dental.png`.

### Evaluation Rationale

Existe al menos un diagrama técnico con finalidad concreta: representar el modelo relacional.

La Responsibility está cubierta en el nivel requerido por la complejidad actualmente documentada.

### Adoption Decision

`PRESERVE`

### Decision Rationale

El diagrama existente aporta valor real y debe mantenerse mientras represente el modelo vigente.

---

## 115. DOC-REFERENCES — External References

- **Requirement Level:** Optional
- **State:** Missing
- **Applicability:** Not Applicable
- **Implementation Characteristics:** None observed
- **Uncertainty:** None

### Detected Facts

No existe un documento dedicado a referencias externas.

El proyecto utiliza tecnologías y especificaciones externas, pero el README no mantiene una colección significativa de:

```text
standards
RFCs
official specifications
technical references
research sources
```

### Evidence

- repository tree.
- `README.md`.

### Evaluation Rationale

Aunque el proyecto depende de tecnologías externas, no existe evidencia de una necesidad real de centralizar referencias.

Las pocas referencias que pudieran ser útiles pueden permanecer dentro de su contexto natural.

### Adoption Decision

`OMIT`

### Decision Rationale

Crear un documento de referencias únicamente para listar documentación de Spring, JWT, MySQL o Swagger no aportaría suficiente valor actualmente.

---

## 116. Optional Responsibilities — Summary

| Responsibility | Requirement Level | State | Applicability | Adoption Decision |
|---|---|---|---|---|
| README-ROADMAP | Optional | Satisfied | Applicable | ACCEPT |
| README-CONTRIBUTING | Optional | Missing | Not Applicable | OMIT |
| README-DEMO | Optional | Satisfied | Applicable | ACCEPT |
| README-AUTHOR | Optional | Satisfied | Applicable | PRESERVE |
| README-HIGHLIGHTS | Optional | Partial | Applicable | ADAPT |
| README-LICENSE | Optional | Partial | Applicable | EVALUATE |
| DOC-ADR | Optional | Missing | Not Applicable | OMIT |
| DOC-API | Optional | Satisfied | Applicable | ACCEPT |
| DOC-DATABASE | Optional | Satisfied | Applicable | ACCEPT |
| DOC-DEPLOYMENT | Optional | Missing | Not Applicable | OMIT |
| DOC-SECURITY | Optional | Partial | Applicable | ADAPT |
| DOC-DIAGRAMS | Optional | Satisfied | Applicable | PRESERVE |
| DOC-REFERENCES | Optional | Missing | Not Applicable | OMIT |

### Aggregate State — Optional

| State | Count |
|---|---:|
| Satisfied | 6 |
| Partial | 3 |
| Missing | 4 |

### Aggregate Applicability — Optional

| Applicability | Count |
|---|---:|
| Applicable | 9 |
| Not Applicable | 4 |
| Uncertain | 0 |

### Aggregate Decision — Optional

| Decision | Count |
|---|---:|
| PRESERVE | 2 |
| ACCEPT | 4 |
| ADAPT | 2 |
| EVALUATE | 1 |
| OMIT | 4 |

---

## 117. Full Assessment Summary

### State

| State | Required | Recommended | Optional | Total |
|---|---:|---:|---:|---:|
| Satisfied | 4 | 2 | 6 | **12** |
| Partial | 3 | 1 | 3 | **7** |
| Missing | 1 | 4 | 4 | **9** |
| **Total** | **8** | **7** | **13** | **28** |

### Applicability

| Applicability | Required | Recommended | Optional | Total |
|---|---:|---:|---:|---:|
| Applicable | 8 | 5 | 9 | **22** |
| Not Applicable | 0 | 2 | 4 | **6** |
| Uncertain | 0 | 0 | 0 | **0** |
| **Total** | **8** | **7** | **13** | **28** |

### Adoption Decision

| Decision | Required | Recommended | Optional | Total |
|---|---:|---:|---:|---:|
| PRESERVE | 2 | 0 | 2 | **4** |
| ACCEPT | 2 | 2 | 4 | **8** |
| ADAPT | 3 | 1 | 2 | **6** |
| ADD | 1 | 2 | 0 | **3** |
| EVALUATE | 0 | 0 | 1 | **1** |
| JUSTIFY | 0 | 0 | 0 | **0** |
| OMIT | 0 | 2 | 4 | **6** |
| **Total** | **8** | **7** | **13** | **28** |

---

## 118. Representation Observations — Optional Set

### Friction

No structural friction required changes to Version 0.

However, the Optional set produced the first concrete use of:

```text
EVALUATE
```

through `README-LICENSE`.

The representation can express the case, but it reinforces the earlier hypothesis that `EVALUATE` may behave more naturally as:

```text
transitional assessment outcome
```

than as a stable final adoption disposition.

This remains an observation and does not modify the decision vocabulary during the experiment.

### Missing Information Slots

None observed.

### Redundant Fields

No field has proven structurally redundant.

The Optional set especially confirms the usefulness of keeping:

```text
State
Applicability
Implementation Characteristics
Uncertainty
```

separate.

### Workarounds

None required.

### Template Deviations

None required.

### Unexpected Information Needs

The `README-LICENSE` case required distinguishing:

```text
license declaration exists somewhere
```

from:

```text
repository licensing is formally established
```

The existing fields were sufficient because this distinction could be represented through:

```text
Detected Facts
Evidence
Partial
Uncertainty
EVALUATE
Decision Rationale
```

No additional field was necessary.

---

## 119. Assessment Completion

All:

```text
28 TPL-BACKEND v0.1.0 Responsibilities
```

have now been assessed using the frozen:

```text
Minimal Adoption Guide — Version 0
+
Structured Markdown Assessment Template — Version 0
```

without modifying:

```text
assessment dimensions
section structure
summary structure
decision representation
evidence representation
rationale representation
```

No workaround or alternative representation was required.

---

## 120. Repeatability Evidence

The complete assessment provides evidence that Version 0 can represent:

```text
Satisfied
Partial
Missing

Applicable
Not Applicable

Own
Equivalent
Specialized
Distributed

PRESERVE
ACCEPT
ADAPT
ADD
EVALUATE
OMIT
```

as well as cases such as:

```text
Satisfied + Applicable + PRESERVE
Satisfied + Applicable + ACCEPT
Partial + Applicable + ADAPT
Partial + Applicable + EVALUATE
Missing + Applicable + ADD
Missing + Not Applicable + OMIT
```

The experiment also exercised:

```text
documentation present but inaccurate
canonical artifact absent but responsibility satisfied
responsibility absent and not applicable
evidence distributed across README and code
specialized generated documentation
uncertainty requiring deferred decision
```

All of these cases were expressible within Version 0.

No case required:

```text
Satisfied + Not Applicable
```

once Responsibility Applicability was correctly separated from canonical artifact necessity.

---

## 121. Representation Result

For this experiment, the evidence supports:

```text
MODEL HOLDS
```

No evidence has been identified requiring:

```text
new essential assessment dimension
new State
new Applicability value
new summary structure
structured data representation
mandatory tooling
replacement of Summary + Responsibility Detail
```

Therefore:

```text
Substantial Redesign Required
    No
```

This result applies to the representation tested against this consumer.

It does not establish universal validity across every repository type or assessment context.

---

## 122. Refinement Candidates

The experiment identifies several refinements that do not contradict the representation.

### RC-R01 — Clarify EVALUATE semantics

Observed case:

```text
README-LICENSE
```

reinforces the hypothesis that `EVALUATE` may function more naturally as:

```text
transitional workflow state
```

than as a stable final adoption disposition.

This requires semantic clarification, not structural redesign.

---

### RC-R02 — Clarify Responsibility Applicability vs Artifact Necessity

The experiment demonstrated:

```text
Responsibility Applicability
    ≠
Canonical Artifact Necessity
```

A Responsibility can remain applicable and satisfied through an equivalent implementation even when the canonical artifact does not exist and does not need to be added.

`DOC-ARCHITECTURE` provides the clearest example.

This distinction should be made explicit in future guidance.

---

### RC-R03 — Clarify Documentation Correctness

`README-QUICK-START` demonstrated:

```text
documentation exists
    but
documentation conflicts with repository reality
```

and therefore:

```text
Presence
    ≠
Satisfaction
```

The representation already supports this distinction, but future guidance should highlight it explicitly.

---

### RC-R04 — Reassess JUSTIFY

Across all 28 Responsibilities:

```text
JUSTIFY
    used 0 times
```

This repeats the observation from the previous Manual Adoption Assessment.

Current evidence does not justify removing it during this experiment, but its independent role remains weakly demonstrated.

---

## 123. Repeatability Conclusion

The experiment question was:

> ¿Puede una guía mínima y una plantilla Markdown estructurada utilizarse para ejecutar un nuevo adoption assessment completo sin modificar sustancialmente su estructura?

The evidence from `dental-back-spring` supports:

```text
Yes
```

Version 0 supported a complete assessment of all 28 `TPL-BACKEND v0.1.0` Responsibilities without material redesign.

The representation remained stable across:

```text
Required
Recommended
Optional
```

and across multiple combinations of:

```text
State
Applicability
Implementation Characteristics
Adoption Decision
```

The result is:

```text
Representation Result
    MODEL HOLDS

Repeatability
    Supported by an additional consumer reuse experiment

Substantial Redesign
    Not required

Minor Refinement
    Justified
```

This does not prove universal repeatability.

It provides evidence that the representation can be reused beyond the original manually constructed assessment.

---

## 124. Experiment Outcome

```text
Problem
    Existing Repository Adoption

Consumer
    fran-eliot/dental-back-spring

Template
    TPL-BACKEND v0.1.0

Responsibilities Assessed
    28 / 28

Guide
    Minimal Adoption Guide — Version 0

Representation
    Structured Markdown Assessment — Version 0

Structural Changes During Experiment
    0

Workarounds Required
    0

Representation Result
    MODEL HOLDS

Repeatability
    Supported by additional consumer reuse

Implementation Selected
    No

Delivery Scope Selected
    No

Tooling Selected
    No
```

---

## 125. Discovery Interpretation

The experiment resolves the immediate research question sufficiently to stop treating representation repeatability as the primary unknown.

However:

```text
Repeatability Evidence
    ≠
Delivery Commitment
```

and:

```text
MODEL HOLDS
    ≠
Discovery Automatically Closed
```

The evidence now justifies evaluating whether part of the solution is mature enough to become Delivery Scope.

This evaluation should reconcile:

```text
Solution Hypotheses
Requirement Candidates
EVALUATE semantics
JUSTIFY semantics
representation refinements
governance state
```

before selecting implementation or release scope.

---

## 126. Next Research Question

The next question becomes:

> ¿Existe evidencia suficiente para promover una parte mínima de la solución de Existing Repository Adoption desde Discovery hacia Delivery Scope sin introducir más complejidad de la necesaria?

The next phase should therefore be:

```text
Repeatability Experiment
        ↓
Discovery Synthesis
        ↓
Delivery Scope Evaluation
```

not:

```text
Repeatability Experiment
        ↓
Implementation
```

No implementation architecture, Sprint, milestone or target release is selected by this document.
