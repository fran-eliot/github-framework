# 25 — Manual Adoption Assessment Discovery

## 1. Propósito

Este documento registra un experimento adicional de Discovery orientado a validar si el modelo provisional de Existing Repository Adoption consolidado en `24_ADOPTION_MODEL_DISCOVERY.md` puede utilizarse manualmente de forma:

- comprensible;
- repetible;
- trazable;
- independiente de una tecnología concreta;
- separando análisis, evaluación y decisión;
- sin seleccionar todavía una arquitectura de implementación.

La pregunta principal del experimento es:

> ¿Puede una persona realizar de forma consistente, comprensible y trazable un adoption assessment real utilizando únicamente el modelo provisional actual?

El objetivo no es implementar una solución de adopción.

No se introduce:

- manifest;
- CLI;
- analyzer;
- validator extension;
- generator;
- GitHub Action;
- automatic apply;
- repository modification.

---

## 2. Relación con Discovery anterior

`24_ADOPTION_MODEL_DISCOVERY.md` consolidó un modelo provisional a partir de tres consumers:

```text
Only Film
    Java / Spring Boot

dental-back
    TypeScript / NestJS

aula-robotica-platform
    Python / FastAPI
```

Los tres experimentos permitieron conservar:

```text
State
    Satisfied
    Partial
    Missing
```

y:

```text
Adoption Decision
    PRESERVE
    ADAPT
    ADD
    ACCEPT
    EVALUATE
    JUSTIFY
    OMIT
```

junto a dimensiones adicionales:

```text
Evidence
Applicability
Implementation Characteristics
Uncertainty
Evaluation Rationale
Decision Rationale
```

El siguiente paso de Discovery quedó definido como la validación de una forma mínima y repetible de realizar manualmente un adoption assessment.

---

## 3. Consumer seleccionado

El consumer utilizado es:

```text
fran-eliot/apitimebank
```

Características principales:

```text
Backend API
PHP
Symfony 5.4
API Platform
Doctrine ORM
MySQL
```

El repositorio es un fork de:

```text
Equipo-20/apitimebank
```

y representa un proyecto backend pequeño, con documentación principalmente concentrada en `README.md`.

Su selección proporciona diversidad tecnológica frente a los tres consumers anteriores.

---

## 4. Repository Template

El experimento utiliza:

```text
TPL-BACKEND
Version: 0.1.0
Status: Experimental
```

El Template define:

```text
Required       8
Recommended    7
Optional      13
----------------
Total         28
```

responsabilidades.

La unidad de análisis continúa siendo:

```text
Responsibility
```

y no:

```text
File
Section
Artifact Name
```

---

## 5. Protocolo utilizado

Se utilizó el flujo provisional:

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

No se ejecutaron:

```text
APPLY
VERIFY
```

porque esas fases permanecen fuera del ámbito validado por Discovery.

---

## 6. ANALYZE

Durante `ANALYZE` se inspeccionaron artefactos reales del consumer.

Entre otros:

```text
README.md
composer.json
composer.lock
symfony.lock
.env
docker-compose.yml
config/
src/
migrations/
```

También se revisaron elementos específicos relevantes para algunas responsabilidades:

```text
config/packages/api_platform.yaml
config/routes/api_platform.yaml
config/packages/security.yaml
src/Entity/Publicacion.php
```

Los hechos detectados se utilizaron exclusivamente como entrada para Evidence.

No se transformaron directamente en estados ni decisiones.

---

## 7. ASSESS

Cada responsabilidad fue evaluada mediante las dimensiones disponibles en el modelo provisional:

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
```

No todos los campos resultaron necesarios en todos los casos.

---

## 8. Required Responsibilities

Resultado:

```text
Required: 8

Satisfied    4
Partial      2
Missing      2
```

### Satisfied

```text
README-HERO
README-OVERVIEW
README-TECH-STACK
README-FOOTER
```

### Partial

```text
README-FEATURES
README-QUICK-START
```

### Missing

```text
README-DOCUMENTATION
DOC-CHANGELOG
```

Un resultado significativo fue:

```text
canonical section absent
        ≠
responsibility Missing
```

Por ejemplo, `README-TECH-STACK` está implementado mediante información distribuida dentro del README aunque no exista una sección canónica equivalente.

---

## 9. Recommended Responsibilities

Resultado inicial:

```text
Recommended: 7

Satisfied    0
Partial      0
Missing      7
```

Sin embargo, el estado `Missing` no determinó por sí solo applicability ni adoption decision.

Durante el assessment aparecieron dos grupos:

```text
Missing + Applicable

README-STATUS
README-ARCHITECTURE
README-REPOSITORY-STRUCTURE
README-TESTING
```

y:

```text
Missing + Applicability initially Uncertain

DOC-ARCHITECTURE
DOC-PROJECT-STATUS
DOC-TESTING
```

Esto reforzó:

```text
State
    ≠
Applicability
```

---

## 10. Optional Responsibilities

Resultado:

```text
Optional: 13

Satisfied    1
Partial      3
Missing      9
```

### Satisfied

```text
README-AUTHOR
```

### Partial

```text
DOC-API
DOC-DATABASE
DOC-REFERENCES
```

### Missing

```text
README-ROADMAP
README-CONTRIBUTING
README-DEMO
README-HIGHLIGHTS
README-LICENSE
DOC-ADR
DOC-DEPLOYMENT
DOC-SECURITY
DOC-DIAGRAMS
```

Las responsabilidades Optional proporcionaron la mayor evidencia sobre applicability.

---

## 11. Resultado agregado del ASSESS

```text
Responsibilities assessed: 28

Satisfied     5
Partial       5
Missing      18
```

El conteo agregado resultó útil como resumen, pero insuficiente como representación del assessment.

Por ejemplo:

```text
README-LICENSE

State
    Missing

Applicability
    Applicable
```

y:

```text
DOC-ADR

State
    Missing

Applicability
    Not Applicable
```

comparten State, pero representan situaciones diferentes.

---

## 12. REVIEW

Los casos inicialmente marcados como:

```text
Applicability = Uncertain
```

fueron revisados utilizando el contexto completo del consumer.

El resultado final fue:

```text
Applicable        17
Not Applicable    11
Uncertain          0
```

Entre las responsabilidades consideradas `Not Applicable` en el contexto actual se encuentran:

```text
DOC-ARCHITECTURE
DOC-PROJECT-STATUS
DOC-TESTING

README-ROADMAP
README-CONTRIBUTING
README-DEMO
README-HIGHLIGHTS

DOC-ADR
DOC-DEPLOYMENT
DOC-SECURITY
DOC-DIAGRAMS
```

La revisión confirmó:

```text
Missing
    ≠
Applicable
```

y:

```text
Repository complexity
        ↓
may influence Applicability
        ↓
but does not change State
```

---

## 13. DECIDE

Después de cerrar el assessment se asignaron Adoption Decisions.

Resultado:

```text
PRESERVE     3
ACCEPT       2
ADAPT        5
ADD          7
OMIT        11
EVALUATE     0
JUSTIFY      0
----------------
TOTAL       28
```

### PRESERVE

```text
README-OVERVIEW
README-FOOTER
README-AUTHOR
```

### ACCEPT

```text
README-HERO
README-TECH-STACK
```

### ADAPT

```text
README-FEATURES
README-QUICK-START
DOC-API
DOC-DATABASE
DOC-REFERENCES
```

### ADD

```text
README-DOCUMENTATION
DOC-CHANGELOG
README-STATUS
README-ARCHITECTURE
README-REPOSITORY-STRUCTURE
README-TESTING
README-LICENSE
```

### OMIT

```text
DOC-ARCHITECTURE
DOC-PROJECT-STATUS
DOC-TESTING
README-ROADMAP
README-CONTRIBUTING
README-DEMO
README-HIGHLIGHTS
DOC-ADR
DOC-DEPLOYMENT
DOC-SECURITY
DOC-DIAGRAMS
```

---

## 14. PRESERVE y ACCEPT

El experimento mantiene útil la distinción entre ambas decisiones.

Ejemplo de implementación directa:

```text
README-OVERVIEW

State
    Satisfied

Decision
    PRESERVE
```

Ejemplo de implementación válida no canónica o distribuida:

```text
README-TECH-STACK

State
    Satisfied

Implementation Characteristics
    Own
    Distributed

Decision
    ACCEPT
```

Por tanto:

```text
PRESERVE
    ≠
ACCEPT
```

continúa siendo una distinción útil.

---

## 15. ADAPT

`ADAPT` resultó necesario cuando una implementación válida ya existía pero necesitaba correcciones o consolidación.

Un caso particularmente claro fue:

```text
README-QUICK-START
```

El consumer es un fork de:

```text
Equipo-20/apitimebank
```

y el README conserva:

```text
git clone https://github.com/Equipo-20/apitimebank.git
```

La instrucción es coherente con el repositorio original, pero no permite clonar directamente el consumer evaluado.

Por tanto:

```text
State
    Partial

Decision
    ADAPT
```

sin necesidad de sustituir completamente la implementación existente.

---

## 16. ADD

`ADD` resultó adecuado para responsabilidades:

```text
Missing
+
Applicable
```

cuando no se identificó una implementación equivalente existente.

Ejemplo:

```text
DOC-CHANGELOG

State
    Missing

Applicability
    Applicable

Decision
    ADD
```

Sin embargo, el experimento no convierte esta relación en una regla automática universal.

---

## 17. OMIT

`OMIT` permitió representar claramente:

```text
Missing
+
Not Applicable
```

Ejemplo:

```text
DOC-ADR

State
    Missing

Applicability
    Not Applicable

Decision
    OMIT
```

El rationale conserva la explicación contextual de la omisión.

Esto evita interpretar:

```text
Missing
```

como una obligación automática de añadir contenido.

---

## 18. EVALUATE y JUSTIFY

El experimento no necesitó utilizar finalmente:

```text
EVALUATE
JUSTIFY
```

Esto no demuestra que deban eliminarse.

Sin embargo, introduce una señal de refinamiento.

### EVALUATE

Durante `REVIEW` existieron responsabilidades con:

```text
Applicability = Uncertain
```

que necesitaban evaluación adicional.

Una vez resuelta la incertidumbre, recibieron una disposition final diferente.

Esto sugiere provisionalmente que:

```text
EVALUATE
```

puede comportarse más como una transición o estado de workflow que como una final adoption disposition.

### JUSTIFY

Las decisiones `OMIT` ya requieren:

```text
Decision Rationale
```

Por tanto, el experimento no encontró un caso donde `JUSTIFY` fuese necesario además de una decisión final.

Esto sugiere investigar si:

```text
JUSTIFY
```

representa realmente una disposition independiente o una obligación asociada a determinadas decisiones.

No se modifica todavía la taxonomía.

---

## 19. Findings del Experimento #4

### F-16 — Missing does not imply Applicable

```text
Missing
    ≠
Applicable
```

Una responsabilidad puede estar ausente y ser correctamente `Not Applicable`.

---

### F-17 — Applicability can depend on consumer complexity

La complejidad y contexto del consumer pueden afectar a applicability sin modificar State.

```text
Consumer Complexity
        ↓
Applicability Context
```

---

### F-18 — Canonical structure remains unnecessary for semantic satisfaction

El cuarto consumer vuelve a confirmar:

```text
Canonical Artifact Absent
        ≠
Responsibility Missing
```

---

### F-19 — Functional capability does not imply documentation satisfaction

Ejemplos:

```text
API exists
    ≠
DOC-API Satisfied
```

y:

```text
security configuration exists
    ≠
DOC-SECURITY Satisfied
```

---

### F-20 — Manual assessment is operationally feasible

Las 28 responsabilidades pudieron evaluarse mediante el modelo provisional sin introducir:

- nuevos States;
- nuevas categorías de Applicability;
- reglas específicas de PHP o Symfony;
- nuevas fases fundamentales del proceso.

---

### F-21 — Decision taxonomy is broadly sufficient

Las decisiones existentes permitieron representar el consumer completo.

Sin embargo:

```text
EVALUATE
JUSTIFY
```

presentan señales de comportamiento diferente respecto a:

```text
PRESERVE
ACCEPT
ADAPT
ADD
OMIT
```

y requieren investigación adicional antes de normativizar la taxonomía.

---

## 20. Resultado frente al modelo provisional

El resultado global del experimento es:

```text
REFINEMENT NEEDED
```

No fundamental contradiction identified.

The provisional model remains operationally usable, but the role of EVALUATE and JUSTIFY requires refinement.

No aparece:

```text
MODEL CONTRADICTION
```

El modelo provisional ha permitido representar:

```text
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

sobre un cuarto consumer tecnológicamente diferente.

---

## 21. Validación de la pregunta de Discovery

La pregunta era:

> ¿Puede una persona realizar de forma consistente, comprensible y trazable un adoption assessment real utilizando únicamente el modelo provisional actual?

El experimento proporciona evidencia suficiente para responder provisionalmente:

> Sí. El modelo provisional puede utilizarse manualmente sobre un consumer backend real para recorrer las responsabilidades de un Repository Template, reunir evidencia, evaluar State y Applicability, resolver incertidumbre y registrar decisiones de adopción trazables sin requerir todavía una implementación técnica especializada.

Esto proporciona evidencia adicional favorable a:

```text
SH-01  Manual Adoption Guide
SH-02  Adoption Checklist / Assessment
SH-04  Adoption Report
SH-11  Staged Adoption Process
```

como un conjunto coherente de necesidades y resultados.

No selecciona todavía su implementación.

---

## 22. Frontera de automatización

El experimento vuelve a confirmar:

```text
Detected Facts
        ↓
Evidence
        ↓
Semantic Evaluation
        ↓
Adoption Decision
```

con disminución progresiva del determinismo.

Parte de `ANALYZE` podría potencialmente recibir asistencia automática.

Sin embargo:

```text
State
Applicability
Semantic Equivalence
Decision
```

continúan requiriendo contexto y review en múltiples casos.

Por tanto permanece válido el principio:

> Automate Evidence before Automating Decisions.

---

## 23. Qué no valida este experimento

El experimento no valida:

```text
APPLY
VERIFY
```

ni:

- modificación automática de repositories;
- merge de contenido;
- conflict resolution;
- rollback;
- idempotency;
- manifest persistence;
- reassessment;
- continuous conformance;
- Initialization;
- otros Repository Templates.

Tampoco convierte el modelo provisional en un Standard definitivo.

---

## 24. Estado de Discovery

Tras este experimento:

```text
Discovery Topic
    Existing Repository Adoption

Repository Template
    TPL-BACKEND v0.1.0

Consumers Assessed
    4

Technology Contexts
    Java / Spring Boot
    TypeScript / NestJS
    Python / FastAPI
    PHP / Symfony

Manual Assessment
    Operationally feasible
    Traceable in the experiment
    Repeatability not independently validated

Adoption Model
    Provisional
    Operationally usable

Solution Selected
    No

Implementation Architecture Selected
    No

Delivery Scope Selected
    No
```

---

## 25. Conclusión

El principal resultado de esta etapa es que GitHub Framework ya dispone de un modelo conceptual suficientemente maduro para realizar manualmente Existing Repository Adoption.

El problema deja de ser únicamente:

```text
Do we understand adoption?
```

y pasa a ser:

```text
How should this demonstrated process
be represented and supported
with the minimum necessary mechanism?
```

La evidencia obtenida no justifica todavía comenzar por:

```text
CLI
Manifest
Generator
Validator Extension
GitHub Actions
```

Sí justifica avanzar desde Problem Discovery hacia una etapa de **solution shaping** centrada inicialmente en:

```text
Problem Discovery
        ↓
Manual Assessment Experiment
        ↓
Solution Shaping Discovery
        ↓
compare minimal representations

NOT YET:

Delivery Scope
Implementation
Release Planning
```

sin seleccionar todavía su representación técnica definitiva.

---

## 26. Próximo paso recomendado

El siguiente paso debería comparar las alternativas mínimas para materializar el proceso validado.

La pregunta puede formularse como:

> ¿Cuál es la representación mínima que permite ejecutar y conservar un adoption assessment sin introducir acoplamiento técnico prematuro?

Las alternativas iniciales a contrastar podrían incluir:

```text
Markdown Guide
Markdown Assessment
Tabular Assessment
Generated Report
Structured Data Representation
```

sin asumir todavía que ninguna de ellas constituye la solución final.

La selección deberá basarse en:

- simplicidad;
- trazabilidad;
- mantenibilidad;
- repetibilidad;
- coste de adopción;
- facilidad de revisión humana;
- potencial de automatización futura;
- mínimo acoplamiento con una implementación concreta.
