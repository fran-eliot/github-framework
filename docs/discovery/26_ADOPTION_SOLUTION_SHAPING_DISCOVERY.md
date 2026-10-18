# 26 — Adoption Solution Shaping Discovery

## 1. Propósito

Este documento continúa la investigación de **Existing Repository Adoption** iniciada en los documentos:

```text
23_BACKEND_ADOPTION_DISCOVERY.md
        ↓
24_ADOPTION_MODEL_DISCOVERY.md
        ↓
25_MANUAL_ADOPTION_ASSESSMENT_DISCOVERY.md
```

Los experimentos anteriores permitieron comprender progresivamente:

- la naturaleza del problema de adopción;
- el modelo conceptual mínimo necesario para representar un assessment;
- la separación entre evidencia, evaluación, estado y decisión;
- los límites actuales de automatización;
- la viabilidad operacional de realizar manualmente un adoption assessment sobre un consumer real.

El siguiente problema ya no consiste únicamente en comprender cómo funciona Existing Repository Adoption.

La pregunta pasa a ser:

> ¿Cuál es la representación mínima que permite ejecutar y conservar un adoption assessment sin introducir acoplamiento técnico prematuro?

El objetivo de este documento es realizar **Solution Shaping Discovery** sobre esa pregunta.

No se pretende todavía seleccionar una arquitectura de implementación ni convertir una Solution Hypothesis en Delivery Scope.

---

## 2. Relación con Discovery anterior

### 2.1 Resultado de Problem Discovery

`24_ADOPTION_MODEL_DISCOVERY.md` consolidó un modelo provisional en el que una evaluación puede necesitar distinguir:

```text
Responsibility
Requirement Level

Detected Facts
Evidence

Evaluation
    State
    Applicability
    Implementation Characteristics
    Uncertainty

Evaluation Rationale

Adoption Decision
Decision Rationale
```

El modelo mantiene explícitamente:

```text
Detected Fact
    ≠
Evidence
    ≠
Evaluated State
    ≠
Adoption Decision
    ≠
Applied Change
```

También mantiene separados:

```text
Responsibility Assessment
        ≠
Adoption Decision
```

y:

```text
Analysis
    ≠
Application
```

---

### 2.2 Resultado del Manual Adoption Assessment

`25_MANUAL_ADOPTION_ASSESSMENT_DISCOVERY.md` utilizó el modelo provisional sobre un cuarto consumer:

```text
fran-eliot/apitimebank
```

mediante el flujo:

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

El experimento mostró que el proceso puede realizarse manualmente de forma operacionalmente viable y trazable.

No se identificó una contradicción fundamental del modelo.

El resultado fue:

```text
REFINEMENT NEEDED
```

principalmente porque el papel de:

```text
EVALUATE
JUSTIFY
```

todavía necesita mayor precisión conceptual.

La repetibilidad del assessment tampoco ha sido validada de forma independiente.

---

### 2.3 Cambio de etapa

La investigación anterior estaba centrada principalmente en:

```text
What is Existing Repository Adoption?
```

y:

```text
What information is needed
to represent an adoption assessment?
```

La etapa actual investiga:

```text
How should that assessment
be represented and used?
```

Por tanto:

```text
Problem Discovery
        ↓
Manual Assessment Experiment
        ↓
Solution Shaping Discovery
```

Solution Shaping permanece dentro de Discovery.

No implica todavía:

```text
Delivery Scope
Implementation
Sprint
Milestone
Target Release
```

---

## 3. Pregunta de Discovery

La pregunta principal es:

> ¿Cuál es la representación mínima que permite ejecutar y conservar un adoption assessment sin introducir acoplamiento técnico prematuro?

Esta pregunta contiene varias dimensiones.

La representación debería permitir:

```text
execute assessment
        +
preserve assessment
        +
review assessment
        +
understand decisions
```

sin exigir prematuramente:

```text
CLI
Manifest
Validator Extension
Generator
GitHub Action
Application Engine
```

La investigación busca por tanto el menor mecanismo capaz de conservar el valor descubierto durante los experimentos anteriores.

---

## 4. Objetivo de Solution Shaping

El objetivo no es elegir la solución técnicamente más sofisticada.

El objetivo es identificar la forma mínima que permita preservar las propiedades que el Discovery ha demostrado necesarias.

La dirección de trabajo es:

```text
Problem Evidence
        ↓
Required Capabilities
        ↓
Candidate Representations
        ↓
Compare Trade-offs
        ↓
Minimal Viable Representation
```

y no:

```text
Preferred Technology
        ↓
Design Solution
        ↓
Find justification
```

La solución deberá derivarse de las necesidades observadas.

---

## 5. Alcance

### 5.1 Incluido

Esta investigación incluye:

- representación manual del adoption assessment;
- representación de las responsabilidades del Repository Template;
- registro de Evidence;
- representación de State;
- representación de Applicability;
- representación de Implementation Characteristics cuando sean relevantes;
- representación de Uncertainty;
- Evaluation Rationale;
- Adoption Decision;
- Decision Rationale;
- revisión humana;
- trazabilidad;
- conservación del assessment;
- comparación de posibles representaciones;
- coste de adopción;
- mantenibilidad;
- posibilidad de evolución futura hacia asistencia automática.

---

### 5.2 Fuera de alcance

Esta investigación no pretende todavía:

- crear una CLI;
- implementar un analyzer;
- diseñar un adoption manifest definitivo;
- extender el Framework Validator;
- generar automáticamente documentación;
- modificar consumers;
- aplicar decisiones de adopción;
- diseñar rollback;
- resolver merge de contenido;
- implementar continuous conformance;
- integrar GitHub Actions;
- definir Repository Initialization;
- crear un nuevo Standard;
- crear historias de implementación;
- abrir un Sprint;
- crear una milestone;
- asignar una versión objetivo.

Estas posibilidades pueden permanecer como hipótesis futuras.

No constituyen el punto de partida de este documento.

---

## 6. Propiedades que debe conservar una representación

Los experimentos anteriores muestran que una representación útil del assessment debe conservar varias propiedades.

### 6.1 Comprensibilidad

Una persona debe poder entender:

```text
what was evaluated
what evidence was found
what conclusion was reached
what decision was taken
why that decision was taken
```

sin necesitar reconstruir el razonamiento desde el repositorio original.

---

### 6.2 Trazabilidad

Debe ser posible recorrer:

```text
Responsibility
        ↓
Evidence
        ↓
Evaluation
        ↓
State / Qualifiers
        ↓
Decision
        ↓
Rationale
```

La representación no debería reducir el resultado a:

```text
Responsibility → Action
```

porque los experimentos han demostrado que esa simplificación pierde información relevante.

---

### 6.3 Separación conceptual

La representación debe evitar mezclar:

```text
State
Applicability
Implementation Characteristics
Decision
```

en un único campo o clasificación.

También debe conservar:

```text
Assessment
    ≠
Decision
```

aunque ambos puedan aparecer dentro del mismo artefacto.

---

### 6.4 Capacidad para representar incertidumbre

La falta de evidencia suficiente no debe transformarse artificialmente en certeza.

La representación debe permitir expresar cuando:

```text
Applicability = Uncertain
```

o cuando una evaluación necesita:

```text
Additional Review
Insufficient Evidence
Contextual Decision
```

sin inventar una conclusión definitiva.

---

### 6.5 Revisión humana

Los experimentos han mostrado que múltiples decisiones requieren interpretación semántica y contextual.

Por tanto, la representación debe facilitar:

```text
read
review
challenge
refine
approve or reconsider
```

por una persona.

Una forma que dificulte la revisión humana sería incompatible con la evidencia actual.

---

### 6.6 Bajo coste de adopción

La representación no debería exigir que un consumer adopte una infraestructura significativa antes de poder evaluar si desea adoptar GitHub Framework.

Debe evitar un patrón como:

```text
Install substantial adoption infrastructure
        ↓
Understand whether Framework adoption is useful
```

La dirección preferible es:

```text
Understand adoption first
        ↓
Introduce additional tooling only if justified
```

---

### 6.7 Mantenibilidad

El assessment debe poder:

- leerse posteriormente;
- corregirse;
- evolucionar;
- compararse con nuevas evaluaciones;
- conservar rationale;
- mantenerse sin tooling especializado obligatorio.

---

### 6.8 Potencial de evolución

Una representación mínima no debería impedir una futura evolución hacia:

```text
Assisted Analysis
Structured Reporting
Validation
Automation
```

Sin embargo:

```text
Future Automation Potential
        ≠
Current Automation Requirement
```

No debe introducirse complejidad presente únicamente para acomodar una implementación futura todavía no seleccionada.

---

## 7. Criterios de evaluación

Las representaciones candidatas se compararán mediante los siguientes criterios.

| Criterion | Question |
|---|---|
| Simplicity | ¿Puede utilizarse sin tooling especializado? |
| Comprehensibility | ¿Puede una persona comprender fácilmente el assessment? |
| Traceability | ¿Permite relacionar evidencia, evaluación y decisión? |
| Reviewability | ¿Facilita revisión y discusión humana? |
| Maintainability | ¿Puede evolucionar sin fricción significativa? |
| Repeatability Support | ¿Ayuda a ejecutar assessments de forma consistente? |
| Adoption Cost | ¿Qué coste introduce para comenzar a utilizarlo? |
| Expressiveness | ¿Representa las dimensiones descubiertas sin pérdida relevante? |
| Flexibility | ¿Puede adaptarse a consumers diferentes? |
| Technical Coupling | ¿Cuánto obliga a adoptar una implementación o tecnología concreta? |
| Future Automation Potential | ¿Puede alimentar posteriormente mecanismos asistidos o automáticos? |
| Framework Fit | ¿Respeta la arquitectura y principios actuales de GitHub Framework? |

Los criterios no se consideran todavía ponderados.

La investigación deberá determinar si todos tienen la misma importancia o si algunos funcionan como restricciones fundamentales.

---

## 8. Restricciones fundamentales

Antes de comparar alternativas pueden establecerse algunas restricciones derivadas directamente del Discovery anterior.

Una representación candidata no debería:

### R-01 — Reducir el assessment a existencia de archivos

```text
File Exists
    ≠
Responsibility Satisfied
```

---

### R-02 — Fusionar State y Adoption Decision

```text
State
    ≠
Decision
```

---

### R-03 — Eliminar rationale

Dos responsabilidades pueden presentar:

```text
same State
+
same Decision
```

por razones diferentes.

---

### R-04 — Forzar estructura canónica

Una implementación válida puede ser:

```text
Own
Equivalent
Specialized
Distributed
```

sin reproducir físicamente el Component canónico.

---

### R-05 — Convertir Optional Missing en ADD

```text
Optional
+
Missing
    ≠
Automatic ADD
```

---

### R-06 — Resolver artificialmente uncertainty

```text
Insufficient Evidence
    ≠
Forced Conclusion
```

---

### R-07 — Mezclar assessment y application

La representación puede expresar decisiones.

No debe asumir que esas decisiones serán aplicadas automáticamente.

```text
REPORT
    ≠
APPLY
```

---

## 9. Representaciones candidatas iniciales

La investigación partirá de cinco representaciones candidatas.

```text
A. Markdown Guide

B. Markdown Assessment

C. Tabular Assessment

D. Generated Report

E. Structured Data Representation
```

Estas alternativas no constituyen todavía soluciones seleccionadas.

Tampoco se presupone que sean mutuamente excluyentes.

Por ejemplo, una solución futura podría combinar:

```text
Structured Data
        ↓
Generated Report
```

o:

```text
Guide
    +
Assessment Template
```

Sin embargo, durante Solution Shaping conviene evaluarlas inicialmente por separado para comprender qué problema resuelve cada una y qué complejidad introduce.

---

## 10. Pregunta del siguiente paso

La siguiente fase de este documento deberá responder, para cada alternativa:

```text
What does it represent well?

What does it represent poorly?

What does it require?

What information does it lose?

What coupling does it introduce?

What future evolution does it enable?

What evidence from Discovery supports it?
```

La comparación debe comenzar por la alternativa de menor complejidad y aumentar progresivamente el grado de estructura.

El objetivo no es encontrar inmediatamente:

```text
the most powerful solution
```

sino:

```text
the least complex representation
that preserves the required properties
of the adoption assessment
```

---

## 11. Alternative A — Markdown Guide

### 11.1 Descripción

La alternativa más simple consiste en documentar el proceso de adoption assessment mediante una guía Markdown.

Conceptualmente:

```text
Repository Template
        +
Markdown Guide
        +
Human Reviewer
        ↓
Adoption Assessment
```

La guía describiría:

- cómo recorrer las Responsibilities;
- qué Evidence buscar;
- cómo determinar State;
- cómo evaluar Applicability;
- cuándo registrar Implementation Characteristics;
- cómo representar Uncertainty;
- cómo separar Evaluation Rationale de Decision Rationale;
- cómo asignar una Adoption Decision;
- cómo revisar casos ambiguos.

La guía no definiría necesariamente una estructura persistente obligatoria para registrar cada assessment.

Su función principal sería:

```text
explain how to assess
```

más que:

```text
store the assessment
```

---

## 12. Capacidades de Markdown Guide

### 12.1 Simplicidad

La principal fortaleza de esta alternativa es su simplicidad.

Requiere únicamente:

```text
Markdown
+
human interpretation
```

No necesita:

- schema;
- parser;
- CLI;
- validator;
- manifest;
- generator;
- runtime específico.

Esto la hace compatible con el principio de bajo acoplamiento técnico.

---

### 12.2 Comprensibilidad

Una guía puede explicar detalladamente:

```text
Responsibility
State
Applicability
Evidence
Uncertainty
Decision
Rationale
```

incluyendo ejemplos y casos límite.

También puede conservar reglas conceptuales importantes como:

```text
File Exists
    ≠
Responsibility Satisfied
```

o:

```text
State
    ≠
Decision
```

Por tanto, funciona bien como mecanismo para transmitir el modelo conceptual.

---

### 12.3 Revisión humana

Markdown es fácilmente revisable mediante:

- Git diff;
- Pull Request;
- Code Review;
- comentarios;
- historial de versiones.

Esto encaja bien con la necesidad observada de mantener revisión humana sobre decisiones semánticas y contextuales.

---

### 12.4 Bajo coste de adopción

El coste inicial es mínimo.

Un consumer podría utilizar la guía sin modificar significativamente su repositorio ni instalar tooling adicional.

Conceptualmente:

```text
Read Guide
    ↓
Inspect Consumer
    ↓
Perform Assessment
```

Esto evita introducir infraestructura antes de comprender si la adopción aporta valor.

---

## 13. Limitaciones de Markdown Guide

La principal limitación aparece al distinguir entre:

```text
process description
```

y:

```text
assessment representation
```

Una guía puede explicar cómo realizar el assessment, pero no garantiza que dos personas registren el resultado de la misma forma.

---

### 13.1 Persistencia débil

La guía no define por sí sola dónde ni cómo conservar:

```text
Responsibility
Evidence
State
Applicability
Decision
Rationale
```

El resultado podría terminar registrado mediante:

- notas libres;
- comentarios;
- Issues;
- documentos diferentes;
- memoria del reviewer;
- ningún artefacto persistente.

Por tanto:

```text
Guide
    ≠
Persistent Assessment
```

---

### 13.2 Repetibilidad limitada

Aunque la guía pueda describir el proceso con precisión, la ejecución sigue dependiendo fuertemente del reviewer.

Dos assessments podrían contener la misma información conceptual pero representarla de manera muy diferente.

Ejemplo:

```text
Reviewer A
    detailed rationale

Reviewer B
    short notes

Reviewer C
    only final decisions
```

La guía reduce variabilidad conceptual, pero no necesariamente variabilidad estructural.

---

### 13.3 Trazabilidad no garantizada

Una guía puede exigir trazabilidad, pero no puede garantizar que el assessment resultante mantenga de forma consistente:

```text
Responsibility
    ↓
Evidence
    ↓
Evaluation
    ↓
Decision
```

Si el resultado se registra como texto libre, algunas relaciones pueden quedar implícitas.

---

### 13.4 Comparabilidad débil

Sin una estructura común, comparar:

```text
Assessment A
vs
Assessment B
```

puede requerir interpretación manual.

Esto limita:

- reassessment;
- comparación entre consumers;
- análisis longitudinal;
- detección de patrones;
- futura automatización.

---

### 13.5 Automatización futura limitada

Una guía Markdown es excelente para consumo humano.

Es menos adecuada como entrada directa para:

```text
parser
validator
report generator
continuous assessment
```

aunque podría coexistir posteriormente con una representación estructurada.

Por tanto:

```text
Human Readability
        high

Machine Readability
        low
```

---

## 14. Evaluación frente a criterios

| Criterion | Assessment |
|---|---|
| Simplicity | Very High |
| Comprehensibility | High |
| Traceability | Medium |
| Reviewability | High |
| Maintainability | High |
| Repeatability Support | Medium |
| Adoption Cost | Very Low |
| Expressiveness | High conceptually |
| Flexibility | Very High |
| Technical Coupling | Very Low |
| Future Automation Potential | Low |
| Framework Fit | High |

---

## 15. Evidence Fit

Markdown Guide está fuertemente respaldada por varias observaciones anteriores.

### Supported by SH-01

`SH-01 — Manual Adoption Guide` permanece como una Solution Hypothesis plausible.

Los experimentos han demostrado que una persona necesita instrucciones para distinguir correctamente:

```text
Detection
Evaluation
Decision
```

---

### Supported by Manual Assessment

El Experimento #4 pudo realizarse manualmente sin tooling especializado.

Esto demuestra que:

```text
specialized implementation
```

no es requisito previo para ejecutar el proceso.

---

### Limited by Traceability Requirement

Sin embargo, el mismo experimento mostró que el resultado necesita conservar múltiples dimensiones y rationale.

Por tanto una guía por sí sola no resuelve completamente:

```text
preserve assessment
```

---

## 16. Resultado provisional — Markdown Guide

La alternativa:

```text
Markdown Guide
```

resuelve adecuadamente:

```text
How do I perform an assessment?
```

pero resuelve débilmente:

```text
How do I preserve an assessment
in a consistent and reviewable form?
```

Su principal valor parece encontrarse en:

```text
Guidance
Process Explanation
Conceptual Consistency
Human Review Support
```

y no necesariamente en:

```text
Assessment Persistence
Structural Consistency
Machine Readability
```

---

## 17. Interpretación provisional

La evidencia actual sugiere:

```text
Markdown Guide
    necessary or useful
        ≠
sufficient representation
```

No aparece como una mala solución.

Aparece como una solución posiblemente incompleta para la pregunta principal de este Discovery.

La pregunta exige simultáneamente:

```text
execute assessment
+
preserve assessment
```

Markdown Guide cubre principalmente el primer término.

Esto produce la primera señal de Solution Shaping:

```text
Guidance
    may be a separate concern
from
Assessment Representation
```

Esta separación deberá contrastarse con las siguientes alternativas.

---

## 18. Finding provisional

### F-22 — Guidance and Assessment Representation may be different concerns

El análisis de Markdown Guide sugiere provisionalmente:

```text
How to perform an assessment
        ≠
How to represent an assessment
```

Una guía puede mejorar consistencia conceptual sin proporcionar por sí sola una representación persistente y comparable del resultado.

Este finding deberá ser confirmado o rechazado al analizar las alternativas restantes.

---

## 19. Alternative B — Markdown Assessment

### 19.1 Descripción

La segunda alternativa consiste en utilizar un documento Markdown específico para registrar cada adoption assessment.

Conceptualmente:

```text
Repository Template
        +
Consumer Repository
        +
Assessment Procedure
        ↓
Markdown Assessment
```

A diferencia de Markdown Guide, esta alternativa no se limita a explicar cómo realizar el proceso.

Su objetivo principal es:

```text
store the assessment
```

de forma:

```text
human-readable
reviewable
versionable
traceable
```

sin introducir todavía un schema formal ni tooling especializado.

---

## 20. Estructura conceptual posible

Un Markdown Assessment podría organizarse por Responsibility.

Ejemplo conceptual:

```text
Responsibility
    README-QUICK-START

Requirement Level
    Required

Detected Facts
    ...

Evidence
    ...

State
    Partial

Applicability
    Applicable

Implementation Characteristics
    Own
    Distributed

Uncertainty
    None

Evaluation Rationale
    ...

Adoption Decision
    ADAPT

Decision Rationale
    ...
```

La estructura podría repetirse para cada Responsibility evaluada.

El documento también podría incluir:

```text
Assessment Metadata
Consumer
Template
Template Version
Assessment Date
Reviewer
Summary
Review Notes
Open Questions
```

sin que estos campos impliquen todavía un contrato formal o machine-readable schema.

---

## 21. Capacidades de Markdown Assessment

### 21.1 Persistencia explícita

Esta alternativa resuelve directamente una de las principales limitaciones de Markdown Guide.

El resultado ya no depende de:

```text
notes
memory
informal discussion
```

sino de un artefacto identificable.

Por tanto:

```text
Assessment
    → persisted artifact
```

Esto permite conservar tanto el resultado como el contexto que condujo a él.

---

### 21.2 Trazabilidad

Markdown permite representar explícitamente la cadena:

```text
Responsibility
        ↓
Detected Facts
        ↓
Evidence
        ↓
Evaluation
        ↓
State / Applicability / Characteristics
        ↓
Adoption Decision
        ↓
Rationale
```

Esto responde directamente a uno de los requisitos más fuertes identificados durante Problem Discovery.

La trazabilidad deja de depender exclusivamente de instrucciones contenidas en una guía.

Pasa a formar parte del propio artefacto.

---

### 21.3 Revisión humana

El documento puede revisarse mediante mecanismos ya disponibles en Git:

```text
diff
history
Pull Request
comments
review
```

Esto resulta especialmente apropiado porque el assessment contiene decisiones semánticas y contextuales.

El formato mantiene visible tanto:

```text
what was concluded
```

como:

```text
why it was concluded
```

---

### 21.4 Bajo acoplamiento técnico

Markdown Assessment no exige:

```text
parser
schema
CLI
database
service
validator
```

La representación puede existir como un archivo independiente.

Por tanto:

```text
Persistent Structure
        +
Low Technical Coupling
```

pueden coexistir.

---

### 21.5 Expresividad

El formato puede representar fácilmente:

```text
long-form rationale
multiple evidence items
uncertainty
exceptions
context
review notes
```

sin forzar la información a un modelo rígido prematuramente.

Esto resulta relevante porque el adoption model todavía contiene dimensiones en refinamiento.

---

## 22. Limitaciones de Markdown Assessment

### 22.1 Estructura convencional, no garantizada

Aunque el documento pueda disponer de una plantilla recomendada, Markdown por sí solo no garantiza que cada assessment conserve exactamente la misma estructura.

Podrían aparecer diferencias como:

```text
Assessment A
    Applicability before State

Assessment B
    State before Applicability

Assessment C
    no explicit Uncertainty field
```

La consistencia depende de:

```text
author discipline
+
template usage
+
review
```

---

### 22.2 Machine readability limitada

Markdown puede analizarse parcialmente de forma automática.

Sin embargo, si su semántica depende de:

```text
headings
free text
lists
tables
```

la automatización futura puede volverse frágil.

Por tanto:

```text
Human Structure
        ≠
Formal Data Structure
```

---

### 22.3 Comparación entre assessments

La comparación humana sería considerablemente mejor que con una guía aislada.

Sin embargo, operaciones como:

```text
compare 20 consumers
count Missing responsibilities
find all EVALUATE decisions
track applicability changes
```

requerirían:

- inspección manual;
- convenciones estrictas;
- parsing específico;
- o transformación posterior.

Markdown Assessment mejora comparabilidad, pero no la resuelve completamente.

---

### 22.4 Riesgo de verbosity

Un assessment completo puede crecer rápidamente.

Con 28 responsabilidades de `TPL-BACKEND`, una representación detallada de:

```text
Facts
Evidence
Evaluation
Rationale
Decision
Decision Rationale
```

puede producir un documento extenso.

Esto puede afectar:

```text
scanability
review speed
maintenance cost
```

especialmente si muchas responsabilidades presentan resultados simples.

---

### 22.5 Duplicación potencial

Si cada Responsibility contiene siempre todos los campos, podría aparecer repetición innecesaria.

Por ejemplo:

```text
Uncertainty
    None
```

repetido numerosas veces.

La representación necesitaría encontrar un equilibrio entre:

```text
explicitness
        vs
document noise
```

---

## 23. Variantes internas posibles

Markdown Assessment no constituye una única estructura.

Pueden imaginarse varias formas.

### 23.1 Narrative Assessment

Cada Responsibility se representa mediante bloques descriptivos.

Ventaja:

```text
high expressiveness
```

Desventaja:

```text
lower structural consistency
```

---

### 23.2 Structured Markdown Sections

Cada Responsibility utiliza siempre las mismas subsecciones.

Ejemplo:

```text
### README-QUICK-START

- Requirement Level:
- State:
- Applicability:
- Implementation Characteristics:
- Uncertainty:
- Adoption Decision:

#### Evidence

...

#### Evaluation Rationale

...

#### Decision Rationale

...
```

Ventaja:

```text
higher consistency
```

sin introducir todavía un schema formal.

---

### 23.3 Hybrid Markdown

Información compacta en una tabla:

```text
Responsibility
Requirement Level
State
Applicability
Decision
```

más bloques narrativos para:

```text
Evidence
Rationale
Uncertainty
```

Esta variante intenta equilibrar:

```text
scanability
+
expressiveness
```

La existencia de estas variantes indica que la alternativa necesita todavía refinement antes de considerarse una representación concreta.

---

## 24. Evaluación frente a criterios

| Criterion | Assessment |
|---|---|
| Simplicity | High |
| Comprehensibility | High |
| Traceability | High |
| Reviewability | Very High |
| Maintainability | High |
| Repeatability Support | High if templated |
| Adoption Cost | Low |
| Expressiveness | Very High |
| Flexibility | Very High |
| Technical Coupling | Very Low |
| Future Automation Potential | Medium |
| Framework Fit | Very High |

---

## 25. Evidence Fit

Markdown Assessment está respaldado directamente por el Experimento #4.

El propio assessment manual necesitó conservar:

```text
facts
evidence
state
applicability
rationale
decision
```

y demostró que dichas dimensiones pueden representarse manualmente.

La alternativa también responde directamente a:

```text
SH-02
Adoption Checklist / Assessment
```

y parcialmente a:

```text
SH-04
Adoption Report
```

sin exigir todavía decidir si ambos conceptos deben materializarse como artefactos distintos.

---

## 26. Relación con Markdown Guide

Las dos primeras alternativas parecen resolver problemas diferentes.

```text
Markdown Guide
    ↓
how to perform assessment
```

mientras:

```text
Markdown Assessment
    ↓
how to preserve assessment
```

Esto refuerza provisionalmente `F-22`.

También sugiere una posible composición:

```text
Guide
    +
Assessment Template
```

pero esta combinación todavía no debe seleccionarse.

Primero debe comprobarse si alternativas más estructuradas ofrecen suficiente valor adicional para justificar mayor complejidad.

---

## 27. Resultado provisional — Markdown Assessment

Markdown Assessment resuelve de forma considerablemente más completa la pregunta principal de Discovery:

```text
execute assessment
+
preserve assessment
```

Puede conservar:

```text
Responsibility
Evidence
Evaluation
Decision
Rationale
```

sin exigir infraestructura adicional.

Sus principales debilidades se concentran en:

```text
formal consistency
machine readability
large-scale comparison
```

más que en la capacidad de representar el assessment individual.

---

## 28. Interpretación provisional

La evidencia actual sugiere:

```text
Markdown Assessment
    may satisfy
the minimum viable representation
```

pero todavía no puede concluirse.

Debe compararse con representaciones más estructuradas antes de determinar si:

```text
additional structure
```

aporta valor suficiente para justificar:

```text
additional complexity
```

La carga de la prueba cambia a partir de este punto.

Las siguientes alternativas no deberían considerarse mejores únicamente por ser más estructuradas.

Deberán demostrar qué necesidad observada resuelven que Markdown Assessment no resuelve suficientemente.

---

## 29. Finding provisional

### F-23 — Persistent structure does not require formal data modeling

Markdown Assessment muestra que es posible introducir:

```text
persistent assessment
+
repeatable structure
+
traceability
```

sin introducir todavía:

```text
schema
manifest
parser
validator
```

Esto abre una posible frontera mínima entre:

```text
free-form guidance
```

y:

```text
formal structured data
```

La siguiente alternativa deberá comprobar si una representación tabular mejora de forma material esta frontera.

---

## 30. Alternative C — Tabular Assessment

### 30.1 Descripción

La tercera alternativa consiste en representar el adoption assessment principalmente mediante una estructura tabular.

Conceptualmente:

```text
Responsibility
    ×
Assessment Dimensions
```

La forma más simple sería una tabla con columnas como:

```text
Responsibility
Requirement Level
State
Applicability
Implementation Characteristics
Uncertainty
Adoption Decision
```

y campos adicionales para:

```text
Evidence
Evaluation Rationale
Decision Rationale
```

dependiendo del grado de detalle necesario.

El objetivo principal de esta alternativa sería mejorar:

```text
scanability
consistency
comparability
```

frente a una representación narrativa.

---

## 31. Capacidades de Tabular Assessment

### 31.1 Escaneabilidad

Una tabla permite obtener rápidamente una visión global del assessment.

Por ejemplo:

```text
Responsibility                State       Applicability     Decision
README-HERO                   Satisfied   Applicable        ACCEPT
README-QUICK-START            Partial     Applicable        ADAPT
DOC-CHANGELOG                 Missing     Applicable        ADD
DOC-ADR                       Missing     Not Applicable    OMIT
```

Esto facilita detectar:

```text
patterns
outliers
missing areas
decision distribution
```

sin recorrer bloques extensos de texto.

---

### 31.2 Consistencia estructural

La estructura tabular fuerza una representación más uniforme.

Cada Responsibility ocupa una fila y cada dimensión dispone de una posición definida.

Por tanto:

```text
same concept
    → same column
```

Esto reduce variaciones entre reviewers.

---

### 31.3 Comparabilidad

Una tabla facilita comparar:

```text
Responsibility A
vs
Responsibility B
```

y también:

```text
Consumer A
vs
Consumer B
```

si ambos utilizan la misma estructura.

Esto resulta especialmente útil para:

- identificar patrones;
- comparar coverage;
- revisar decisiones;
- detectar inconsistencias;
- resumir resultados.

---

### 31.4 Repeatability Support

La estructura reduce libertad accidental.

Un reviewer recibe implícitamente una checklist de campos:

```text
State?
Applicability?
Decision?
Uncertainty?
```

Esto puede mejorar la repetibilidad del proceso respecto a una representación completamente narrativa.

---

### 31.5 Potencial de automatización

Una tabla tiene más estructura que Markdown libre.

Puede facilitar posteriormente:

```text
parsing
aggregation
reporting
filtering
statistics
```

especialmente si los valores de determinadas columnas utilizan vocabularios controlados.

Por tanto:

```text
Machine Readability
```

es potencialmente mayor que en Markdown narrativo.

---

## 32. Limitaciones de Tabular Assessment

### 32.1 Evidence puede no ser tabular

La principal dificultad aparece con Evidence.

Evidence puede consistir en:

```text
multiple files
multiple observations
distributed implementation
textual findings
runtime behavior
configuration evidence
```

Forzar toda esta información a una única celda puede producir:

```text
long cells
poor readability
loss of structure
```

---

### 32.2 Rationale tampoco es naturalmente tabular

Evaluation Rationale y Decision Rationale pueden requerir explicaciones contextuales.

Ejemplo:

```text
State = Missing
Applicability = Applicable
Decision = EVALUATE
```

puede depender de una cuestión de provenance, authority o contexto que no se expresa correctamente mediante una etiqueta corta.

Por tanto:

```text
Decision value
    ≠
Decision explanation
```

Una tabla puede registrar bien la primera y peor la segunda.

---

### 32.3 Riesgo de compresión semántica

La estructura tabular puede incentivar una simplificación excesiva:

```text
Responsibility
State
Decision
```

omitiendo progresivamente:

```text
Evidence
Uncertainty
Rationale
```

porque estos campos dificultan la compactación.

Esto podría reintroducir precisamente el problema que Discovery había separado:

```text
Responsibility
    →
Action
```

---

### 32.4 Distributed Evidence

Algunas Responsibilities pueden estar satisfechas mediante información distribuida.

En ese caso:

```text
Evidence
    =
artifact A
+
artifact B
+
artifact C
```

La representación tabular puede mostrar referencias, pero resulta menos adecuada para explicar la relación semántica entre ellas.

---

### 32.5 Reviewability de casos complejos

Las tablas funcionan muy bien para casos simples.

Pero pueden degradarse cuando aparecen:

```text
Uncertainty
Equivalent implementation
Distributed evidence
Conflicting signals
Contextual applicability
```

Los casos más importantes para revisión humana suelen ser precisamente los menos compactables.

---

## 33. Variantes internas posibles

Tabular Assessment admite varias variantes.

### 33.1 Single Table

Todo el assessment se registra en una única tabla.

Ventajas:

```text
maximum scanability
maximum structural consistency
```

Desventajas:

```text
poor narrative capacity
very wide rows
large cells
```

---

### 33.2 Summary Table + Detail Sections

Una tabla resume:

```text
Responsibility
State
Applicability
Decision
```

y los casos que necesitan explicación disponen de secciones detalladas.

Conceptualmente:

```text
Summary Table
        ↓
Detailed Assessment Notes
```

Esto mejora:

```text
scanability
+
expressiveness
```

pero empieza a acercarse a una variante híbrida de Markdown Assessment.

---

### 33.3 One Table per Requirement Level

Podrían existir tablas separadas para:

```text
Required
Recommended
Optional
```

Esto mejora navegación y refleja la estructura del Repository Template.

Sin embargo, no resuelve por sí mismo el problema de Evidence y Rationale.

---

## 34. Evaluación frente a criterios

| Criterion | Assessment |
|---|---|
| Simplicity | High |
| Comprehensibility | High |
| Traceability | Medium to High |
| Reviewability | High for simple cases |
| Maintainability | High |
| Repeatability Support | Very High |
| Adoption Cost | Low |
| Expressiveness | Medium |
| Flexibility | Medium to High |
| Technical Coupling | Very Low |
| Future Automation Potential | Medium to High |
| Framework Fit | High |

---

## 35. Evidence Fit

Tabular Assessment responde bien a varias necesidades observadas:

```text
consistent traversal
repeatable fields
summary visibility
cross-responsibility comparison
```

Sin embargo, los experimentos anteriores muestran que la evaluación no consiste únicamente en asignar valores controlados.

Necesita conservar también:

```text
Evidence
Rationale
Uncertainty
Context
```

Esto limita la suficiencia de una tabla pura.

---

## 36. Comparación con Markdown Assessment

Markdown Assessment prioriza:

```text
expressiveness
context
rationale
```

mientras Tabular Assessment prioriza:

```text
consistency
scanability
comparability
```

La tensión puede expresarse como:

```text
Narrative Freedom
        ↑
Markdown Assessment

        ↕

Structural Consistency
        ↑
Tabular Assessment
```

Ninguna propiedad parece prescindible por completo.

---

## 37. Resultado provisional — Tabular Assessment

Una tabla representa muy bien la parte más clasificable del modelo:

```text
Responsibility
Requirement Level
State
Applicability
Implementation Characteristics
Uncertainty
Decision
```

pero representa peor:

```text
Detected Facts
Evidence
Evaluation Rationale
Decision Rationale
```

cuando estas dimensiones requieren contexto significativo.

Por tanto:

```text
Tabular Assessment
    is strong as summary structure
```

pero aparece menos convincente como representación completa del assessment.

---

## 38. Interpretación provisional

La evidencia actual sugiere que una tabla pura probablemente introduce demasiada compresión semántica.

Sin embargo, la capacidad de resumen que aporta parece valiosa.

Esto produce una nueva hipótesis:

```text
Detailed Assessment
        +
Tabular Summary
```

podría ofrecer mejor equilibrio que cualquiera de las dos formas por separado.

Todavía no debe seleccionarse esta combinación.

Primero deben analizarse alternativas con mayor grado de estructura técnica.

---

## 39. Finding provisional

### F-24 — Assessment summary and assessment detail may require different representations

El análisis sugiere provisionalmente:

```text
assessment detail
    ≠
assessment summary
```

La información necesaria para comprender completamente una decisión puede ser demasiado rica para una tabla.

Sin embargo, una vista tabular puede resultar especialmente adecuada para:

```text
overview
comparison
review navigation
aggregate analysis
```

Esto introduce una segunda separación potencial dentro del problema:

```text
Guidance
        ≠
Assessment Detail
        ≠
Assessment Summary
```

La siguiente alternativa deberá comprobar si un Generated Report aporta valor adicional o simplemente automatiza una representación que todavía puede producirse manualmente.

---

## 40. Alternative D — Generated Report

### 40.1 Descripción

La cuarta alternativa consiste en generar automáticamente un informe de adoption assessment a partir de una fuente de datos o de un proceso previo de evaluación.

Conceptualmente:

```text
Assessment Inputs
        ↓
Generation Mechanism
        ↓
Generated Report
```

El informe podría adoptar forma de:

```text
Markdown
HTML
PDF
other human-readable output
```

pero el elemento distintivo no es el formato de salida.

La característica fundamental es:

```text
report is generated
```

y no redactado manualmente como representación primaria.

Esto introduce una diferencia importante respecto a las alternativas anteriores.

---

## 41. Qué presupone un Generated Report

Para generar un informe de forma consistente debe existir previamente alguna representación de entrada.

Conceptualmente:

```text
Generated Report
    requires
Structured or semi-structured source
```

La fuente podría ser:

```text
Structured Data
Assessment Form
Parser Output
CLI Result
Analyzer Result
Intermediate Representation
```

Por tanto:

```text
Generated Report
    ≠
Primary Assessment Model
```

al menos no necesariamente.

Puede ser simplemente una proyección de otra representación subyacente.

---

## 42. Capacidades de Generated Report

### 42.1 Consistencia de presentación

Una vez definido el mecanismo de generación, todos los informes pueden utilizar una estructura uniforme.

Esto mejora:

```text
consistency
presentation quality
navigation
summary structure
```

y reduce variabilidad accidental entre reviewers.

---

### 42.2 Separación entre datos y presentación

Un Generated Report permite conceptualmente separar:

```text
Assessment Data
        ≠
Presentation
```

Esto puede facilitar múltiples vistas sobre la misma evaluación.

Por ejemplo:

```text
Structured Assessment
        ↓
Markdown Report

Structured Assessment
        ↓
Summary Table

Structured Assessment
        ↓
HTML View
```

Esta separación puede resultar útil si existe una representación primaria suficientemente estable.

---

### 42.3 Automatización de resúmenes

El informe podría calcular automáticamente:

```text
Satisfied count
Partial count
Missing count

Applicable count
Not Applicable count
Uncertain count

Decision distribution
```

así como generar tablas de navegación y secciones de detalle.

Esto reduce trabajo repetitivo y errores de agregación manual.

---

### 42.4 Reproducibilidad de salida

Dada la misma entrada y el mismo generador:

```text
same input
+
same generation rules
    →
same report
```

Esto mejora la reproducibilidad de la presentación.

Sin embargo, no debe confundirse con reproducibilidad de la evaluación semántica.

---

### 42.5 Reviewability

Si el resultado generado es Markdown o HTML legible, puede facilitar una revisión humana eficaz.

Especialmente puede combinar:

```text
summary
+
detail
```

sin obligar al reviewer a mantener ambas vistas manualmente.

---

## 43. Limitaciones de Generated Report

### 43.1 No resuelve por sí mismo la representación primaria

La principal limitación es estructural.

Para generar un informe debe existir algo que generar.

Por tanto la pregunta:

```text
How should assessment be represented?
```

no queda respondida únicamente por:

```text
Generate a report
```

Sigue siendo necesario responder:

```text
Generate it from what?
```

---

### 43.2 Introduce tooling

A diferencia de Markdown Guide, Markdown Assessment y Tabular Assessment, esta alternativa necesita algún mecanismo ejecutable.

Como mínimo:

```text
generator
+
input contract
```

Esto introduce:

```text
implementation
maintenance
versioning
failure modes
```

antes de haber demostrado que dicha complejidad sea necesaria.

---

### 43.3 Riesgo de inversión prematura

El Discovery actual busca:

```text
minimum representation
```

Un Generated Report puede llevar rápidamente a decisiones sobre:

```text
language
template engine
schema
CLI
file locations
commands
output formats
```

Estas decisiones pueden producir acoplamiento técnico antes de consolidar el modelo de representación.

---

### 43.4 Generación no mejora evaluación semántica

Un generador puede reproducir fielmente datos ya registrados.

No puede convertir automáticamente:

```text
insufficient evidence
```

en:

```text
correct semantic evaluation
```

ni determinar necesariamente:

```text
Applicability
Equivalence
Decision
```

Por tanto:

```text
automated presentation
    ≠
automated assessment
```

---

### 43.5 Dependencia de estabilidad del modelo

Si todavía se están refinando conceptos como:

```text
EVALUATE
JUSTIFY
Uncertainty
```

un generador puede cristalizar demasiado pronto una estructura aún provisional.

Cada cambio conceptual podría requerir:

```text
input migration
generator modification
template modification
compatibility handling
```

---

## 44. Generated Report como output secundario

La alternativa parece más sólida si se interpreta como:

```text
Assessment Representation
        ↓
Generated Report
```

y no como:

```text
Generated Report
        =
Assessment Representation
```

Esto permitiría utilizar el report para:

```text
communication
review
summary
publication
```

mientras otra representación conserva la información primaria.

---

## 45. Relación con SH-04

`SH-04 — Adoption Report` recibe apoyo claro de los experimentos anteriores.

Sin embargo:

```text
Adoption Report
    ≠
Generated Adoption Report
```

Un report puede redactarse manualmente.

La evidencia de Discovery demuestra la necesidad de un resultado trazable.

No demuestra todavía la necesidad de generar ese resultado automáticamente.

Por tanto, SH-04 no debe interpretarse prematuramente como justificación de tooling.

---

## 46. Relación con automatización futura

Generated Report encaja bien con el principio:

> Automate Evidence before Automating Decisions.

pero solo parcialmente.

Puede automatizar:

```text
aggregation
formatting
navigation
presentation
```

una vez que Evidence y Evaluation estén disponibles.

Esto podría convertirse en un paso futuro razonable:

```text
Assessment
    ↓
Report Generation
```

sin automatizar la decisión semántica.

---

## 47. Evaluación frente a criterios

| Criterion | Assessment |
|---|---|
| Simplicity | Low to Medium |
| Comprehensibility | Very High as output |
| Traceability | High if source preserves it |
| Reviewability | Very High |
| Maintainability | Medium |
| Repeatability Support | High for presentation |
| Adoption Cost | Medium |
| Expressiveness | High if source supports it |
| Flexibility | Medium to High |
| Technical Coupling | Medium |
| Future Automation Potential | Very High |
| Framework Fit | Medium at current stage |

---

## 48. Evidence Fit

Los experimentos respaldan claramente la necesidad de:

```text
reportable assessment
```

pero no todavía de:

```text
generated assessment report
```

La diferencia es importante.

Actualmente existe evidencia suficiente para afirmar:

```text
Assessment result should be preservable
and reviewable
```

pero no:

```text
Assessment result must be generated
by tooling
```

---

## 49. Comparación con alternativas anteriores

Markdown Guide responde principalmente a:

```text
How do I assess?
```

Markdown Assessment responde principalmente a:

```text
How do I preserve the assessment?
```

Tabular Assessment mejora:

```text
How do I summarize and compare it?
```

Generated Report responde principalmente a:

```text
How can I consistently present
an already represented assessment?
```

Por tanto empieza a aparecer una posible cadena conceptual:

```text
Guidance
        ↓
Assessment Representation
        ↓
Summary
        ↓
Generated Presentation
```

Estas responsabilidades no deberían confundirse.

---

## 50. Resultado provisional — Generated Report

Generated Report aporta valor real en:

```text
presentation consistency
summary generation
repeatable output
human review
future automation
```

pero introduce una dependencia fundamental:

```text
it needs a source representation
```

Por tanto no parece resolver por sí mismo la pregunta principal de este Discovery.

Además, exige tooling antes de que exista evidencia suficiente de que dicho tooling sea necesario.

---

## 51. Interpretación provisional

La evidencia actual sugiere:

```text
Generated Report
    potentially valuable later
        ≠
minimum primary representation
```

Parece más razonable interpretarlo como una capacidad derivada futura.

En términos de Solution Shaping:

```text
Primary Representation
        first

Generated Views
        later if justified
```

Esto preserva el principio de mínimo acoplamiento técnico.

---

## 52. Finding provisional

### F-25 — Report generation is downstream from assessment representation

El análisis sugiere:

```text
Assessment Representation
        precedes
Report Generation
```

Un Generated Report puede mejorar la presentación, consistencia y reviewability.

Sin embargo, no elimina la necesidad de una representación primaria del assessment.

Por tanto:

```text
Generated Report
    may be a future capability
rather than
the minimum representation
```

La siguiente alternativa debe analizar la opción con mayor estructura explícita:

```text
Structured Data Representation
```

y comprobar si sus beneficios en consistencia, validación y automatización justifican el incremento de complejidad y acoplamiento.

---

## 53. Alternative E — Structured Data Representation

### 53.1 Descripción

La quinta alternativa consiste en representar el adoption assessment mediante una estructura de datos explícita.

Conceptualmente:

```text
Assessment
    =
Structured Data
```

La representación podría adoptar formas como:

```text
YAML
JSON
TOML
other structured format
```

pero el formato concreto no es todavía relevante.

La característica distintiva es:

```text
explicit fields
+
controlled structure
+
machine-readable representation
```

Frente a Markdown Assessment, la semántica deja de depender principalmente de convenciones humanas y pasa a estar codificada de forma más explícita.

---

## 54. Estructura conceptual posible

Una representación estructurada podría aproximarse conceptualmente a:

```text
assessment
    consumer
    template
    template_version
    assessment_date
    reviewer

    responsibilities
        responsibility_id
        requirement_level

        detected_facts
        evidence

        state
        applicability
        implementation_characteristics
        uncertainty

        evaluation_rationale

        adoption_decision
        decision_rationale
```

Esta estructura no implica todavía:

```text
schema selected
file selected
field names finalized
serialization format selected
```

Su función aquí es únicamente mostrar qué significaría transformar el modelo provisional en datos explícitos.

---

## 55. Capacidades de Structured Data Representation

### 55.1 Consistencia estructural

Una representación estructurada puede garantizar que conceptos equivalentes aparezcan siempre en posiciones equivalentes.

Por ejemplo:

```text
State
    always in State field

Applicability
    always in Applicability field

Decision
    always in Decision field
```

Esto reduce ambigüedad y variabilidad accidental.

---

### 55.2 Machine readability

Esta es su principal fortaleza.

Los datos podrían ser consumidos posteriormente por:

```text
validator
report generator
CLI
dashboard
comparison tooling
continuous assessment
```

sin depender de parsing frágil de texto libre.

Por tanto:

```text
Machine Readability
    Very High
```

---

### 55.3 Validación

Si posteriormente se definiese un contrato formal, podría comprobarse:

```text
required fields
allowed values
invalid combinations
duplicate responsibilities
unknown responsibility IDs
```

Esto podría mejorar consistencia y detectar errores de representación.

Sin embargo, esa capacidad depende de una fase posterior de formalización.

---

### 55.4 Comparabilidad

Una representación estructurada facilita operaciones como:

```text
compare consumers
filter decisions
aggregate states
detect patterns
track changes
```

de forma más fiable que una representación narrativa.

---

### 55.5 Evolución hacia automatización

Structured Data ofrece la mejor base entre las alternativas analizadas para:

```text
automated evidence collection
assisted assessment
generated reporting
validation
reassessment
```

Esto la convierte en una opción atractiva para una evolución futura del Framework.

---

## 56. Limitaciones de Structured Data Representation

### 56.1 Mayor complejidad inicial

La principal desventaja aparece inmediatamente.

Para representar correctamente el assessment deben decidirse cuestiones como:

```text
field names
nesting
cardinality
optional fields
controlled vocabularies
nullability
versioning
```

Esto introduce decisiones de diseño antes de que el modelo conceptual esté completamente estabilizado.

---

### 56.2 Riesgo de formalización prematura

El modelo provisional todavía contiene áreas abiertas.

Especialmente:

```text
EVALUATE
JUSTIFY
Uncertainty
Implementation Characteristics
```

Formalizar estos conceptos demasiado pronto puede convertir una hipótesis provisional en un contrato difícil de modificar.

Conceptualmente:

```text
Provisional Model
        ↓
Premature Schema
        ↓
Accidental Standard
```

Este riesgo es especialmente relevante en GitHub Framework, donde las estructuras formales tienden posteriormente a convertirse en contratos reutilizables.

---

### 56.3 Human readability inferior

Aunque YAML o formatos similares pueden ser legibles, no ofrecen la misma capacidad narrativa que Markdown para:

```text
complex rationale
context
exceptions
interpretation
review discussion
```

Las explicaciones largas pueden terminar como grandes bloques de texto embebidos dentro de una estructura de datos.

Esto puede producir una representación que sea:

```text
machine-friendly
but
human-unfriendly
```

---

### 56.4 Coste de mantenimiento del contrato

Una vez que existe una estructura formal, cualquier evolución conceptual puede requerir:

```text
schema changes
migration rules
version compatibility
tool updates
documentation updates
```

Esto incrementa el coste de cambio precisamente durante una fase donde todavía estamos aprendiendo.

---

### 56.5 Acoplamiento técnico

Aunque el formato pueda parecer simple, Structured Data introduce inevitablemente cierto grado de contrato técnico.

Incluso sin tooling:

```text
field names
allowed values
structure
```

constituyen ya decisiones técnicas.

Por tanto:

```text
Structured Data
    introduces
Technical Coupling
```

en mayor medida que Markdown Assessment.

---

## 57. Structured Data no implica automatización de decisiones

Es importante mantener la frontera descubierta anteriormente.

Una representación estructurada puede almacenar:

```text
State = Partial
Applicability = Applicable
Decision = ADAPT
```

pero no determina necesariamente cómo se obtuvieron esos valores.

Por tanto:

```text
Machine-readable assessment
        ≠
Machine-made assessment
```

La estructura puede automatizar:

```text
storage
validation
aggregation
report generation
```

sin automatizar:

```text
semantic evaluation
applicability reasoning
equivalence judgment
adoption decision
```

---

## 58. Posibles niveles de estructuración

Structured Data tampoco constituye necesariamente una única opción.

### 58.1 Loose Structured Data

Campos definidos, pero sin schema formal.

Ejemplo conceptual:

```text
responsibility: README-QUICK-START
state: Partial
applicability: Applicable
decision: ADAPT
```

Ventaja:

```text
low formalization cost
```

Desventaja:

```text
limited validation
```

---

### 58.2 Schema-backed Structured Data

La representación utiliza un contrato formal.

Por ejemplo:

```text
required fields
enums
types
constraints
```

Ventaja:

```text
strong consistency
```

Desventaja:

```text
higher coupling
higher migration cost
```

---

### 58.3 Structured Core + Narrative Fields

Una posible variante conservaría campos estructurados para:

```text
Responsibility
Requirement Level
State
Applicability
Decision
```

y texto libre para:

```text
Evidence
Evaluation Rationale
Decision Rationale
```

Conceptualmente:

```text
Structured Classification
        +
Narrative Explanation
```

Esta variante reduce parte de la tensión entre machine readability y expresividad humana.

---

## 59. Evaluación frente a criterios

| Criterion | Assessment |
|---|---|
| Simplicity | Medium to Low |
| Comprehensibility | Medium to High |
| Traceability | Very High |
| Reviewability | Medium to High |
| Maintainability | Medium |
| Repeatability Support | Very High |
| Adoption Cost | Medium |
| Expressiveness | High if narrative fields allowed |
| Flexibility | Medium |
| Technical Coupling | Medium to High |
| Future Automation Potential | Very High |
| Framework Fit | Potentially High, but premature |

---

## 60. Evidence Fit

Structured Data responde especialmente bien a necesidades futuras identificadas durante Discovery:

```text
consistent persistence
comparison
aggregation
validation
automation
```

Sin embargo, los experimentos realizados no han demostrado todavía que estas capacidades sean necesarias para ejecutar correctamente el assessment actual.

La evidencia sí demuestra la necesidad de:

```text
persistent
traceable
reviewable
assessment
```

pero no todavía de:

```text
formal machine-readable contract
```

Por tanto existe una diferencia entre:

```text
future usefulness
```

y:

```text
current necessity
```

---

## 61. Comparación con Markdown Assessment

La comparación más importante es:

```text
Markdown Assessment
        vs
Structured Data Representation
```

Markdown Assessment maximiza:

```text
human readability
flexibility
low adoption cost
low coupling
```

Structured Data maximiza:

```text
consistency
machine readability
validation potential
automation potential
```

La diferencia puede expresarse como:

```text
Lower Formalization
        ←
Markdown Assessment

        continuum

Structured Data
        →
Higher Formalization
```

La pregunta de Solution Shaping es dónde se encuentra el punto mínimo suficiente.

---

## 62. Resultado provisional — Structured Data Representation

Structured Data es la alternativa con mayor potencial técnico.

Puede soportar:

```text
validation
aggregation
generated reports
assisted analysis
automation
```

mejor que las alternativas anteriores.

Sin embargo, ese potencial tiene un coste:

```text
greater formalization
greater coupling
greater maintenance burden
greater risk of premature schema design
```

La evidencia actual no demuestra que ese coste sea necesario en esta etapa.

---

## 63. Interpretación provisional

La alternativa parece especialmente adecuada como evolución futura cuando exista necesidad demostrada de:

```text
machine processing
cross-consumer analysis
validation
generated output
```

pero resulta difícil justificarla como representación mínima inicial.

Por tanto:

```text
Structured Data
    strong future candidate
        ≠
obvious current minimum
```

---

## 64. Finding provisional

### F-26 — Machine readability is valuable but not yet a minimum requirement

La investigación muestra que:

```text
Machine Readability
```

puede habilitar capacidades futuras importantes.

Sin embargo, los experimentos realizados hasta ahora han requerido principalmente:

```text
Human Readability
Traceability
Reviewability
Persistence
```

Por tanto:

```text
future automation value
        ≠
current minimum requirement
```

La representación mínima no debería formalizar datos únicamente para preservar posibilidades futuras que todavía no han demostrado necesidad operacional.

---

## 65. Comparative Analysis

Tras analizar las cinco alternativas:

```text
A. Markdown Guide
B. Markdown Assessment
C. Tabular Assessment
D. Generated Report
E. Structured Data Representation
```

es posible compararlas de forma conjunta.

---

### 65.1 Comparative Matrix

| Criterion | Markdown Guide | Markdown Assessment | Tabular Assessment | Generated Report | Structured Data |
|---|---:|---:|---:|---:|---:|
| Simplicity | Very High | High | High | Low–Medium | Medium–Low |
| Comprehensibility | High | High | High | Very High | Medium–High |
| Traceability | Medium | High | Medium–High | High* | Very High |
| Reviewability | High | Very High | High | Very High | Medium–High |
| Maintainability | High | High | High | Medium | Medium |
| Repeatability Support | Medium | High | Very High | High* | Very High |
| Adoption Cost | Very Low | Low | Low | Medium | Medium |
| Expressiveness | High | Very High | Medium | High* | High |
| Flexibility | Very High | Very High | Medium–High | Medium–High | Medium |
| Technical Coupling | Very Low | Very Low | Very Low | Medium | Medium–High |
| Future Automation Potential | Low | Medium | Medium–High | Very High | Very High |
| Framework Fit — Current Stage | High | Very High | High | Medium | Medium |

`*` depende de la representación primaria utilizada como fuente.

Las valoraciones son cualitativas y comparativas.

No representan una puntuación cuantitativa ni una ponderación formal de los
criterios. Su función es hacer explícitos los trade-offs observados durante
Solution Shaping.

La selección provisional se basa en suficiencia con mínima complejidad, no
en maximizar el número de valoraciones `High` o `Very High`.

---

## 66. Qué problema resuelve cada alternativa

La comparación revela que las alternativas no son completamente equivalentes.

```text
Markdown Guide
    → Guidance

Markdown Assessment
    → Persistent detailed assessment

Tabular Assessment
    → Summary and comparison

Generated Report
    → Presentation of existing assessment data

Structured Data
    → Formal machine-readable persistence
```

Por tanto, tratarlas como cinco soluciones competidoras puras sería incorrecto.

Varias representan capas diferentes del mismo problema.

---

## 67. Separación de concerns emergente

La investigación produce una posible descomposición:

```text
Guidance
        ↓
Assessment Representation
        ↓
Assessment Summary
        ↓
Generated Presentation
        ↓
Automation
```

No todas estas capas necesitan existir desde el inicio.

El problema mínimo actual parece concentrarse en:

```text
Guidance
+
Assessment Representation
```

mientras:

```text
Generated Presentation
Automation
```

parecen capacidades posteriores.

---

## 68. Minimum Viable Representation

La pregunta principal era:

> ¿Cuál es la representación mínima que permite ejecutar y conservar un adoption assessment sin introducir acoplamiento técnico prematuro?

La evidencia comparativa apunta actualmente hacia:

```text
Markdown Guide
        +
Structured Markdown Assessment
```

como candidato de menor complejidad capaz de cubrir simultáneamente:

```text
execute
preserve
review
trace
maintain
```

sin exigir:

```text
schema
parser
CLI
generator
validator
```

En este contexto, `Structured Markdown Assessment` significa un documento
Markdown con una estructura convencional y repetible de secciones y campos.

No implica:

- machine-readable schema;
- typed data model;
- serialization contract;
- parser-required syntax.

La estructura es una convención para revisión humana, no todavía un contrato
formal de datos.

---

## 69. Papel de Tabular Summary

Tabular Assessment no parece suficiente como representación completa.

Sin embargo, una tabla puede funcionar bien como vista resumida dentro del propio Markdown Assessment.

Conceptualmente:

```text
Markdown Assessment

    Summary Table
        ↓
    Detailed Responsibility Sections
```

Esto permitiría combinar:

```text
scanability
+
expressiveness
```

sin crear una representación primaria adicional.

---

## 70. Representación mínima candidata

La forma mínima candidata puede expresarse como:

```text
Adoption Guide
        +
Assessment Template
            ↓
        Summary
            +
        Responsibility Details
```

donde el Assessment Template sigue siendo Markdown.

Todavía no implica:

```text
formal schema
structured data contract
tooling
```

pero introduce suficiente convención para mejorar repetibilidad.

---

## 71. Qué no se selecciona todavía

Aunque la comparación favorece una representación Markdown estructurada, este Discovery no selecciona todavía:

```text
exact file name
exact repository path
exact heading structure
field syntax
schema
YAML
JSON
CLI
generator
validator
GitHub Action
```

Tampoco convierte automáticamente la conclusión en Delivery Scope.

Primero debe comprobarse que esta representación candidata funciona de forma repetible.

---

## 72. Findings consolidados

### F-22 — Guidance and Assessment Representation may be different concerns

```text
How to assess
    ≠
How to store assessment
```

---

### F-23 — Persistent structure does not require formal data modeling

```text
Persistent Assessment
    can exist without
Schema
```

---

### F-24 — Assessment summary and assessment detail may require different representations

```text
Summary
    ≠
Detail
```

pero pueden coexistir dentro del mismo artefacto.

---

### F-25 — Report generation is downstream from assessment representation

```text
Assessment Representation
    precedes
Generated Report
```

---

### F-26 — Machine readability is valuable but not yet a minimum requirement

```text
Future Automation Potential
    ≠
Current Minimum Requirement
```

---

## 73. Solution Shaping Result

El resultado provisional de esta comparación es:

```text
MINIMAL REPRESENTATION CANDIDATE

Markdown Guide
    +
Structured Markdown Assessment
        including
            Summary Table
            Responsibility Detail
```

Este resultado no constituye todavía una solución implementada.

Representa una hipótesis de solución significativamente más concreta que las alternativas iniciales.

---

## 74. Solution Hypotheses después de la comparación

La comparación modifica el peso relativo de las Solution Hypotheses.

### SH-01 — Manual Adoption Guide

```text
Strongly Supported
```

Parece resolver una necesidad distinta y complementaria.

---

### SH-02 — Adoption Checklist / Assessment

```text
Strongly Supported
```

Es el núcleo de la representación mínima candidata.

---

### SH-04 — Adoption Report

```text
Supported
```

pero no necesita implicar generación automática.

El propio Markdown Assessment puede actuar inicialmente como report.

---

### SH-11 — Staged Adoption Process

```text
Strongly Supported
```

La separación:

```text
ANALYZE
ASSESS
REVIEW
DECIDE
REPORT
```

continúa siendo útil para organizar la guía y el assessment.

---

### Structured Data Representation

```text
Future Candidate
```

Debe permanecer abierta, pero no parece necesaria en el alcance mínimo actual.

---

### Generated Report

```text
Future Capability
```

Puede añadirse posteriormente sobre una representación primaria estable.

---

## 75. Próximo experimento necesario

La comparación conceptual por sí sola no demuestra que la representación candidata sea repetible.

El siguiente paso debería ser construir una forma mínima de:

```text
Markdown Guide
+
Structured Markdown Assessment Template
```

y utilizarla sobre un consumer real.

El objetivo no sería todavía implementar tooling.

Sería comprobar:

```text
Can another assessment be performed
using the same representation
without redesigning the format?
```

---

## 76. Pregunta del siguiente Discovery

La siguiente pregunta puede formularse como:

> ¿Puede una guía mínima y una plantilla Markdown estructurada utilizarse para ejecutar un nuevo adoption assessment completo sin modificar sustancialmente su estructura?

La prueba debería observar especialmente:

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

---

## 77. Estado al cierre de Solution Shaping

```text
Problem Discovery
    Completed provisionally

Adoption Model
    Provisional
    Operationally usable

Manual Assessment
    Operationally feasible
    Traceable
    Repeatability not independently validated

Solution Shaping Comparison
    Completed provisionally

Minimal Representation Candidate
    Markdown Guide
    +
    Structured Markdown Assessment
    Status: Identified
    Repeatability: Not yet validated

Structured Data
    Deferred

Generated Report
    Deferred

Delivery Scope
    Not selected

Implementation Architecture
    Not selected

Sprint
    None

Target Release
    None
```

---

## 78. Conclusión

Solution Shaping muestra que la pregunta de Existing Repository Adoption no necesita resolverse inicialmente mediante tooling especializado.

La evidencia actual favorece una solución basada en:

```text
human-readable guidance
+
persistent structured assessment
```

materializada provisionalmente mediante Markdown.

Esta combinación conserva:

```text
simplicity
traceability
reviewability
expressiveness
low adoption cost
low technical coupling
```

y permite posponer:

```text
schema design
tooling
generation
automation
```

hasta que exista evidencia operacional suficiente.

El siguiente paso no debería ser implementar una CLI ni formalizar un manifest.

Debería ser comprobar si la representación mínima candidata puede utilizarse de nuevo sin rediseñarla.

En otras palabras:

```text
Conceptual Comparison
        ↓
Minimal Representation Candidate
        ↓
Repeatability Experiment
        ↓
only then
possible Delivery Scope
```
