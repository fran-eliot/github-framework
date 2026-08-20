# 09 - COMPONENT CATALOG

| Field        | Value             |
| ------------ | ----------------- |
| **Project**  | GitHub Framework  |
| **Document** | Component Catalog |
| **Version**  | 1.2.0             |
| **Status**   | Stable            |
| **Owner**    | Fran Ramirez      |

---

# Part 1/4

# Registry Foundations

---

# 1. Purpose

El **Component Catalog (CC)** constituye el registro central de descubrimiento, clasificación y trazabilidad de los elementos reutilizables reconocidos por GitHub Framework.

Su responsabilidad consiste en facilitar la identificación y localización de:

- Framework Components;
- Repository Templates;
- otras capacidades reutilizables gobernadas por el Repository Design System cuando corresponda.

El Component Catalog no constituye una fuente arquitectónica paralela.

Tampoco sustituye:

- Specifications;
- Metadata;
- Materialization Artifacts;
- Repository Template definitions;
- Standards;
- Reference Implementations.

El catálogo representa el Framework existente.

No lo redefine.

---

# 2. Vision

El Component Catalog deberá permitir responder rápidamente preguntas como:

```text
What reusable capabilities exist?

Which family do they belong to?

Are they Conceptual or Implemented?

What is their lifecycle status?

Where is their canonical definition?

Which Repository Templates reference them?
```

Su objetivo consiste en facilitar descubrimiento antes de diseñar nuevas soluciones.

Antes de introducir un nuevo Framework Component deberá comprobarse si:

- existe una responsabilidad equivalente;
- puede reutilizarse un Component existente;
- puede ampliarse una capacidad ya definida;
- existe un Repository Template apropiado;
- la necesidad es suficientemente recurrente;
- debe permanecer específica del consumidor.

El catálogo deberá ayudar a realizar esta evaluación sin duplicar las fuentes canónicas.

---

# 3. Relationship with Canonical Sources

GitHub Framework mantiene responsabilidades diferenciadas entre sus principales fuentes.

| Source | Responsibility |
| --- | --- |
| Repository Design System | Define arquitectura, contratos generales y reglas de composición |
| Component Specification | Define responsabilidad, alcance y comportamiento esperado |
| Component Metadata | Proporciona representación estructurada y machine-readable |
| Materialization Artifacts | Proporcionan capacidad reusable cuando la responsabilidad lo requiere |
| Component Catalog | Facilita descubrimiento, clasificación y trazabilidad |
| Repository Templates | Componen Components según el tipo de proyecto |
| Standards | Formalizan reglas prácticas validadas |
| Reference Implementations | Proporcionan evidencia mediante uso real |
| Governance Documents | Gestionan evolución, backlog y estado del proyecto |

Modelo:

```text
Repository Design System
        ↓
Architecture

Specification
+
Metadata
+
Materialization when required
        ↓
Canonical Component Definition

Component Catalog
        ↓
Discovery and Classification

Repository Templates
        ↓
Contextual Composition

Repository Implementations
        ↓
Consumer Materialization
```

El catálogo deberá referenciar estas fuentes.

No deberá copiarlas íntegramente.

---

# 4. Registry Philosophy

Cada responsabilidad reusable deberá disponer de una identidad canónica reconocible.

No deberán coexistir Framework Components diferentes que representen esencialmente la misma responsabilidad.

Cuando aparezca una nueva necesidad deberá evaluarse:

```text
Reuse existing Component
        ↓
Configure
        ↓
Extend
        ↓
Create new Component
```

La incorporación de una responsabilidad al catálogo no implica automáticamente que exista implementación material.

El catálogo podrá registrar:

```text
Conceptual
Implemented
```

siempre que la clasificación sea explícita.

---

# 5. Registry Architecture

El Component Catalog organiza los elementos reutilizables según su naturaleza.

```text
GitHub Framework
        │
        ├── Framework Components
        │       ├── README
        │       ├── Documentation
        │       ├── Workflow
        │       └── Visual
        │
        └── Repository Templates
```

Los Framework Components representan responsabilidades reutilizables.

Los Repository Templates representan composiciones reutilizables de esas responsabilidades.

Los Maturity Profiles constituyen una dimensión independiente.

No forman una familia de Components ni Repository Templates.

---

# 6. Registry Families

El catálogo reconoce actualmente cuatro familias principales de Framework Components.

| Prefix | Family |
| --- | --- |
| `README-*` | README Components |
| `DOC-*` | Documentation Components |
| `WCL-*` | Workflow Components |
| `VCL-*` | Visual Components |

Además, registra Repository Templates mediante:

| Prefix | Element |
| --- | --- |
| `TPL-*` | Repository Templates |

Los Repository Templates no constituyen una familia de Framework Components.

La incorporación futura de nuevas familias deberá estar respaldada por el Repository Design System.

---

# 7. Element Identity

Todo elemento registrado deberá disponer de un identificador estable cuando su naturaleza lo requiera.

Formato general:

```text
PREFIX-NAME
```

Ejemplos:

```text
README-HERO
DOC-ARCHITECTURE
WCL-CI
VCL-BANNER
TPL-BACKEND
```

El identificador deberá:

- ser único;
- representar una responsabilidad estable;
- permitir referencias machine-readable;
- mantenerse consistente entre versiones compatibles;
- corresponder con la fuente canónica del elemento.

No deberá utilizarse el mismo identificador para responsabilidades diferentes.

---

# 8. Naming Rules

Los identificadores deberán utilizar:

- inglés;
- mayúsculas;
- guiones;
- nombres descriptivos;
- prefijo oficial de la familia.

Se evitarán:

- abreviaturas ambiguas;
- nombres ligados a consumidores concretos;
- nombres tecnológicos cuando la responsabilidad sea más general;
- identificadores duplicados;
- cambios innecesarios de naming.

La estabilidad del identificador forma parte del contrato público del Framework.

---

# 9. Canonical Component Definition

Cuando un Framework Component esté `Implemented`, su definición canónica seguirá el modelo establecido por el RDS:

```text
Specification
        +
Metadata
        +
Materialization when required
```

La Specification define la responsabilidad humana.

La Metadata proporciona representación estructurada.

La Materialization proporciona capacidad reusable cuando la responsabilidad la requiere.

El Component Catalog no sustituye ninguno de estos elementos.

Su función consiste en indicar:

- qué Component existe;
- cómo se clasifica;
- dónde localizarlo;
- cuál es su disponibilidad actual.

---

# 10. Component Metadata

Los Framework Components implementados dispondrán de Metadata estructurada conforme a su definición canónica.

Entre los campos actualmente relevantes podrán encontrarse:

| Field | Description |
| --- | --- |
| ID | Identificador estable |
| Name | Nombre |
| Family | Familia |
| Version | Versión |
| Status | Lifecycle status |
| Priority | Prioridad orientativa |
| Audience | Audiencia principal |
| Maturity | Madurez mínima recomendada |
| Description | Descripción resumida |
| Dependencies | Dependencias declaradas |

La Metadata podrá evolucionar conforme maduren las capacidades del Framework.

El catálogo no deberá definir un esquema alternativo incompatible.

---

# 11. Implementation Classification

El Component Catalog distingue la disponibilidad material de una responsabilidad mediante:

| Classification | Meaning |
| --- | --- |
| `Conceptual` | Responsabilidad reconocida sin implementación canónica reusable suficiente |
| `Implemented` | Existe una definición canónica reusable y gobernada conforme al RDS |

Esta clasificación responde:

```text
Is a canonical reusable capability available?
```

No responde:

```text
Is it Stable?
Is it Required?
Does a consumer conform?
```

Por tanto:

```text
Implementation Classification
        ≠
Lifecycle Status
        ≠
Template Requirement Level
        ≠
Consumer Conformance
```

---

# 12. Conceptual Elements

Un Component `Conceptual` representa una responsabilidad reconocida por la arquitectura que todavía no dispone de implementación canónica reusable suficiente.

Puede existir conceptualmente para:

- preservar una responsabilidad identificada;
- evitar duplicaciones;
- facilitar planificación;
- permitir futura composición;
- preparar implementación posterior.

No deberá presentarse como capacidad material disponible.

La existencia de una práctica equivalente en un repositorio consumidor no modifica automáticamente esta clasificación.

---

# 13. Implemented Elements

Un Component podrá clasificarse como `Implemented` cuando exista una definición canónica reusable conforme al contrato del RDS.

Como mínimo deberá disponer de:

```text
Specification
+
Metadata
```

y además:

```text
Materialization
```

cuando su responsabilidad requiera capacidad material adicional.

La clasificación deberá reflejar la realidad del Framework.

No deberá utilizarse para representar intención futura.

---

# 14. Implementation Classification vs Materialization

El mecanismo de materialización depende de la familia y responsabilidad.

Ejemplos conceptuales:

```text
README Component
        ↓
Reusable section or template
```

```text
Documentation Component
        ↓
Reusable documentation structure
```

```text
Workflow Component
        ↓
Community file / configuration / executable workflow / convention
```

```text
Visual Component
        ↓
Asset / layout / convention / template
```

El Component Catalog no define estos mecanismos en detalle.

Esa responsabilidad pertenece al RDS y a las Specifications canónicas.

---

# 15. Lifecycle Status

Los elementos implementados podrán mantener lifecycle states como:

| State | Meaning |
| --- | --- |
| Draft | Diseño o implementación inicial |
| Experimental | Implementado y en validación |
| Stable | Validado para uso recomendado |
| Deprecated | Disponible por compatibilidad, pero sustituido |
| Retired | Fuera del catálogo activo |

El lifecycle status describe evolución y madurez de adopción.

No indica disponibilidad material por sí solo.

Ejemplo válido:

```text
implementation: Implemented
status: Experimental
```

---

# 16. Implementation Classification vs Lifecycle

La implementación y el lifecycle constituyen dimensiones distintas.

Modelo:

```text
Conceptual
        ↓
Implementation work
        ↓
Implemented
        ↓
Experimental
        ↓
Validation
        ↓
Stable
```

Este flujo es orientativo.

El catálogo deberá representar ambas dimensiones cuando corresponda.

No deberá utilizar `Stable` como sustituto de `Implemented`.

---

# 17. Component Priority

La Metadata de un Framework Component podrá expresar una prioridad orientativa dentro de su familia.

Valores actuales:

| Priority | Meaning |
| --- | --- |
| Required | Responsabilidad de alta relevancia dentro de su ámbito |
| Recommended | Responsabilidad habitualmente útil |
| Optional | Responsabilidad especializada o contextual |

La prioridad describe el Component de forma general.

No determina su obligatoriedad dentro de un Repository Template.

Por tanto:

```text
Component Priority
        ≠
Template Requirement Level
```

---

# 18. Template Requirement Levels

Los Repository Templates utilizan:

```text
required
recommended
optional
```

para expresar la importancia contextual de un Component dentro de una composición concreta.

El Component Catalog no deberá convertir estos requirement levels en propiedades universales.

Un mismo Component puede ser:

```text
required
```

en un Template y:

```text
recommended
```

en otro.

La fuente normativa de esta decisión será el Repository Template.

---

# 19. Component Availability vs Consumer Conformance

El catálogo deberá mantener explícitamente la distinción:

```text
Component Availability
        ≠
Consumer Conformance
```

Un Component puede permanecer `Conceptual` mientras un consumidor satisface correctamente su responsabilidad mediante una implementación propia.

Del mismo modo, un Component `Implemented` puede existir sin ser utilizado por un consumidor concreto.

El catálogo informa disponibilidad.

La conformance deberá evaluarse contra:

- Repository Template;
- responsabilidades seleccionadas;
- Component contracts;
- consumer materialization.

---

# 20. Component Relationships

Los Framework Components podrán mantener relaciones con otros elementos.

Podrán existir:

- complementariedad;
- navegación;
- secuencia operativa;
- consumo conjunto;
- dependencia;
- especialización;
- relación con Repository Templates.

El catálogo podrá exponer estas relaciones con fines de descubrimiento.

No deberá transformar relaciones conceptuales en dependencias técnicas.

---

# 21. Component Dependencies

Una dependencia representa una relación funcional real.

Deberá declararse en la Specification o Metadata canónica cuando exista.

Principio:

```text
Dependency
        ≠
Common usage
```

y:

```text
Dependency
        ≠
Template requirement level
```

El Component Catalog podrá mostrar dependencias.

No deberá inventarlas.

---

# 22. Component Consumers

Un Framework Component podrá ser consumido, según su responsabilidad, por:

- repository README;
- documentation;
- GitHub configuration;
- GitHub Actions;
- Repository Templates;
- GitHub Profile;
- GitHub Pages;
- Framework Automation;
- futuros consumidores.

La aplicabilidad depende de la responsabilidad.

No todos los Components serán válidos para todos los contextos.

---

# 23. Cross-Family Reuse

Los Components podrán relacionarse entre familias.

Ejemplos:

```text
README-ARCHITECTURE
        ↔
DOC-ARCHITECTURE
```

```text
README-HERO
        ↔
VCL-HERO
```

```text
WCL-RELEASE
        ↔
DOC-CHANGELOG
```

Estas relaciones deberán preservar responsabilidades independientes.

No constituyen una jerarquía universal entre familias.

---

# 24. Component Ownership

Todo elemento reusable deberá disponer de ownership identificable mediante la gobernanza del proyecto.

El catálogo podrá exponer ownership cuando resulte útil para descubrimiento.

No deberá mantener una segunda fuente contradictoria si existe una fuente canónica específica.

Actualmente, el ownership general pertenece al mantenimiento de GitHub Framework.

Podrán incorporarse owners especializados en el futuro.

---

# 25. Component Versioning

Los Framework Components podrán mantener versionado independiente de GitHub Framework.

Se utilizará Semantic Versioning cuando corresponda:

```text
Major.Minor.Patch
```

La actualización del Framework no obliga automáticamente a actualizar todos los Components.

El catálogo deberá reflejar la versión canónica.

No generar una versión paralela.

---

# 26. Maturity Mapping

La Metadata podrá indicar una madurez mínima recomendada.

| Level | Description |
| --- | --- |
| L1 | Experimental |
| L2 | Public Basic |
| L3 | Supporting |
| L4 | Strategic |

Este valor representa una expectativa orientativa.

No determina:

- project type;
- lifecycle status;
- requirement level;
- implementation classification.

---

# 27. Registry Attributes

El Component Catalog podrá exponer dos tipos de información.

## Canonical Metadata

Información procedente directamente de la fuente canónica.

Ejemplos:

- ID;
- Name;
- Version;
- Family;
- Status;
- Priority;
- Audience;
- Maturity;
- Dependencies.

## Derived Catalog Information

Información calculada o mantenida para descubrimiento.

Ejemplos:

- implementation classification;
- canonical location;
- Repository Templates relacionados;
- consumidores conocidos;
- última revisión;
- familia.

La información derivada no deberá convertirse en una segunda Specification.

---

# 28. Canonical Location

Cuando exista implementación, el catálogo deberá permitir localizar la fuente canónica.

Ubicaciones principales actuales:

```text
framework/components/readme/
framework/components/documentation/
framework/templates/repositories/
```

Conforme se materialicen nuevas familias podrán añadirse ubicaciones como:

```text
framework/components/workflow/
framework/components/visual/
```

La presencia de una ubicación potencial no implica que la familia ya disponga de Components implementados.

---

# 29. Registry Navigation

El catálogo deberá permitir localizar elementos mediante criterios como:

- ID;
- family;
- implementation classification;
- lifecycle status;
- priority;
- audience;
- maturity;
- Repository Template;
- canonical location;
- dependency;
- responsibility.

La navegación podrá evolucionar hacia herramientas machine-readable.

La documentación actual constituye la interfaz humana principal.

---

# 30. Registry Synchronization

El Component Catalog deberá mantenerse sincronizado con la implementación real.

Cambios como:

```text
Conceptual
        ↓
Implemented
```

deberán reflejarse cuando exista una fuente canónica real.

La sincronización podrá afectar a:

- registry tables;
- implementation counts;
- canonical locations;
- summaries;
- relationships;
- status;
- version.

El catálogo no deberá adelantarse a la implementación.

---

# 31. Registry Evolution

La incorporación o evolución de un elemento deberá seguir conceptualmente:

```text
Need
        ↓
RDS evaluation
        ↓
Specification
        ↓
Implementation
        ↓
Catalog synchronization
        ↓
Validation
        ↓
Adoption
```

Un elemento conceptual podrá existir antes de la implementación cuando resulte útil para representar una responsabilidad reconocida.

En ese caso deberá permanecer claramente clasificado.

---

# 32. Registry Principles

El Component Catalog seguirá estos principios:

- descubrimiento centralizado;
- nomenclatura estable;
- clasificación explícita;
- trazabilidad;
- ausencia de duplicados conceptuales;
- referencias a fuentes canónicas;
- sincronización con implementación;
- separación entre disponibilidad y conformance;
- separación entre implementation classification y lifecycle;
- ausencia de requirement levels globales.

---

# 33. Registry Anti-Patterns

No deberán aparecer:

- identificadores duplicados;
- familias ambiguas;
- Components con responsabilidades equivalentes;
- dependencias ocultas;
- Components conceptuales presentados como implementados;
- lifecycle status utilizado como implementación;
- requirement levels globales definidos por el catálogo;
- Metadata duplicada con valores contradictorios;
- Repository Profiles tratados como Components;
- Maturity Profiles tratados como Repository Templates;
- canonical locations inexistentes presentadas como disponibles;
- prácticas de un consumer presentadas como implementación canónica;
- información derivada convertida en Specification paralela.

---

# 34. Registry Quality Gates

Antes de registrar o actualizar un elemento deberá verificarse:

- [ ] El identificador es único.
- [ ] La naturaleza o familia está correctamente identificada.
- [ ] Existe una responsabilidad diferenciada.
- [ ] La clasificación `Conceptual / Implemented` es correcta.
- [ ] El lifecycle status es coherente cuando corresponde.
- [ ] La fuente canónica está identificada cuando existe.
- [ ] La ubicación canónica es correcta cuando existe implementación.
- [ ] Las dependencias reales están documentadas.
- [ ] La Metadata reproducida coincide con la fuente canónica.
- [ ] No existe un requirement level global inventado.
- [ ] La disponibilidad no se confunde con consumer conformance.
- [ ] No se duplica una responsabilidad existente.
- [ ] El catálogo continúa alineado con el RDS.

---

# 35. Long-Term Vision

El Component Catalog deberá evolucionar hacia una interfaz central de descubrimiento de GitHub Framework.

Permitirá localizar:

- responsabilidades reutilizables;
- implementaciones disponibles;
- Repository Templates;
- relaciones;
- dependencias;
- estado;
- versiones;
- fuentes canónicas.

Con el tiempo podrá alimentar:

- Repository Wizards;
- CLI;
- validadores;
- generadores;
- herramientas de gobernanza;
- dependency analysis;
- Repository Health;
- Framework Automation.

Estas herramientas deberán consumir las fuentes canónicas.

El Catalog actuará como índice y capa de descubrimiento.

No como arquitectura paralela.

---

# 36. Part 1 Conclusions

El **Component Catalog** proporciona una vista centralizada y gobernada de los elementos reutilizables reconocidos por GitHub Framework.

El RDS define arquitectura.

Las Specifications definen responsabilidades.

La Metadata estructura información.

Las Materializations proporcionan capacidad reusable cuando resulta necesaria.

El Component Catalog permite descubrir y clasificar estos elementos.

Modelo:

```text
Canonical Sources
        ↓
Component Catalog
        ↓
Discovery and Classification
        ↓
Repository Templates
        ↓
Repository Implementations
```

El catálogo distingue explícitamente:

```text
Conceptual
        ≠
Implemented
```

```text
Implementation Classification
        ≠
Lifecycle Status
```

```text
Component Priority
        ≠
Template Requirement Level
```

```text
Component Availability
        ≠
Consumer Conformance
```

Estas separaciones permiten representar con precisión el estado real del Framework sin convertir el catálogo en una segunda fuente de verdad.

---

# 37. Part 1 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Component Catalog.

---

# 09 - COMPONENT CATALOG

# Part 2/4

# README & Documentation Components Registry

---

# 38. Purpose

Esta Part registra los Framework Components pertenecientes a las familias:

```text
README-*
DOC-*
```

Ambas familias proporcionan responsabilidades documentales reutilizables, pero operan en niveles diferentes.

Los README Components estructuran la superficie principal de entrada de un repositorio.

Los Documentation Components representan responsabilidades documentales especializadas que pueden requerir artefactos, estructuras o documentos adicionales.

Modelo:

```text
README Components
        ↓
Repository Entry Surface

Documentation Components
        ↓
Specialized Documentation
```

La clasificación de esta Part refleja la disponibilidad canónica real dentro del Framework.

Las responsabilidades reconocidas arquitectónicamente que todavía no disponen de implementación reusable suficiente permanecen `Conceptual`.

---

# 39. README Component Family

La familia:

```text
README-*
```

representa responsabilidades reutilizables destinadas principalmente a la composición de archivos `README.md`.

Su objetivo consiste en evitar que cada repositorio diseñe desde cero responsabilidades recurrentes de presentación, comprensión, navegación y adopción.

Los README Components no representan necesariamente archivos independientes.

Su materialización habitual consiste en estructuras o secciones reutilizables dentro de un README consumidor.

---

# 40. README Component Registry

El catálogo reconoce actualmente los siguientes README Components:

| ID | Responsibility | Implementation |
| --- | --- | :---: |
| `README-HERO` | Presentación principal e identidad inicial | Implemented |
| `README-OVERVIEW` | Explicación resumida del proyecto | Implemented |
| `README-HIGHLIGHTS` | Capacidades o elementos destacados | Conceptual |
| `README-FEATURES` | Funcionalidades principales | Implemented |
| `README-TECH-STACK` | Tecnologías principales | Implemented |
| `README-QUICK-START` | Inicio rápido y primeros pasos | Implemented |
| `README-DEMO` | Demostración o acceso al resultado | Conceptual |
| `README-ARCHITECTURE` | Resumen arquitectónico | Implemented |
| `README-DOCUMENTATION` | Acceso a documentación ampliada | Implemented |
| `README-REPOSITORY-STRUCTURE` | Explicación de estructura del repositorio | Conceptual |
| `README-TESTING` | Información resumida sobre testing | Implemented |
| `README-STATUS` | Estado actual del proyecto | Implemented |
| `README-ROADMAP` | Evolución prevista | Implemented |
| `README-CONTRIBUTING` | Acceso o resumen de contribución | Conceptual |
| `README-LICENSE` | Información de licencia | Conceptual |
| `README-AUTHOR` | Información de autoría o mantenimiento | Implemented |
| `README-FOOTER` | Cierre y navegación complementaria | Implemented |

---

# 41. README Registry Summary

Estado actual:

```text
README Components
        17 total

Implemented
        12

Conceptual
         5
```

Components implementados:

```text
README-ARCHITECTURE
README-AUTHOR
README-DOCUMENTATION
README-FEATURES
README-FOOTER
README-HERO
README-OVERVIEW
README-QUICK-START
README-ROADMAP
README-STATUS
README-TECH-STACK
README-TESTING
```

Components conceptuales:

```text
README-HIGHLIGHTS
README-REPOSITORY-STRUCTURE
README-DEMO
README-CONTRIBUTING
README-LICENSE
```

La clasificación representa disponibilidad reusable dentro de GitHub Framework.

No representa consumer conformance.

---

# 42. README Implemented Components

Los README Components clasificados como `Implemented` disponen de una definición canónica reusable dentro de:

```text
framework/components/readme/
```

Su implementación deberá mantenerse conforme al contrato general del RDS:

```text
Specification
+
Metadata
+
Materialization when required
```

El Component Catalog no reproduce las Specifications completas.

Las tablas del catálogo proporcionan:

- descubrimiento;
- clasificación;
- trazabilidad;
- navegación.

---

# 43. README Conceptual Components

Los README Components clasificados como `Conceptual` representan responsabilidades reconocidas por el Framework que todavía no disponen de implementación canónica reusable suficiente.

Actualmente:

```text
README-HIGHLIGHTS
README-REPOSITORY-STRUCTURE
README-DEMO
README-CONTRIBUTING
README-LICENSE
```

La existencia de contenido equivalente en:

- GitHub Framework;
- Repository Templates;
- Reference Implementations;
- otros consumidores;

no modifica automáticamente esta clasificación.

---

# 44. README-HIGHLIGHTS

`README-HIGHLIGHTS` representa la responsabilidad de presentar capacidades, características o elementos especialmente relevantes de un proyecto.

Registry classification:

```text
Family: README
Implementation: Conceptual
```

Un consumidor puede incluir highlights sin que exista todavía una implementación reusable de este Component.

---

# 45. README-REPOSITORY-STRUCTURE

`README-REPOSITORY-STRUCTURE` representa la responsabilidad de explicar desde el README la organización principal del repositorio cuando resulte útil.

Registry classification:

```text
Family: README
Implementation: Conceptual
```

La existencia de árboles de directorios o explicaciones estructurales en consumidores no constituye por sí sola implementación canónica.

---

# 46. README-DEMO

`README-DEMO` representa la responsabilidad de facilitar acceso a una demostración, preview o resultado observable del proyecto cuando exista.

Registry classification:

```text
Family: README
Implementation: Conceptual
```

Su aplicabilidad depende del tipo de proyecto.

No todos los repositorios necesitan esta responsabilidad.

---

# 47. README-CONTRIBUTING

`README-CONTRIBUTING` representa la responsabilidad de facilitar desde el README el acceso al proceso de contribución.

Registry classification:

```text
Family: README
Implementation: Conceptual
```

La existencia de:

```text
CONTRIBUTING.md
```

o de un proceso de contribución en un consumidor no constituye automáticamente una implementación reusable de `README-CONTRIBUTING`.

---

# 48. README-LICENSE

`README-LICENSE` representa la responsabilidad de comunicar desde el README la licencia aplicable al proyecto.

Registry classification:

```text
Family: README
Implementation: Conceptual
```

La existencia de:

```text
LICENSE
```

en un repositorio consumidor satisface una responsabilidad relacionada.

No constituye por sí sola una implementación canónica reusable de `README-LICENSE`.

---

# 49. README Composition

Los README Components están diseñados para composición.

Ejemplo:

```text
README-HERO
+
README-OVERVIEW
+
README-FEATURES
+
README-TECH-STACK
+
README-QUICK-START
+
README-STATUS
        ↓
Repository README
```

No todos los repositorios deberán utilizar todos los Components.

La selección depende de:

- Repository Template;
- project type;
- audience;
- maturity;
- contexto;
- necesidades del consumidor.

El Component Catalog no establece una composición universal.

---

# 50. README Component Relationships

Los README Components podrán mantener relaciones naturales con Documentation Components.

Ejemplos:

| README Component | Related Documentation Responsibility |
| --- | --- |
| `README-ARCHITECTURE` | `DOC-ARCHITECTURE` |
| `README-DOCUMENTATION` | Documentation system |
| `README-TESTING` | `DOC-TESTING` |
| `README-ROADMAP` | `DOC-ROADMAP` |
| `README-STATUS` | `DOC-PROJECT-STATUS` |
| `README-LICENSE` | Repository licensing responsibility |

Estas relaciones expresan complementariedad.

No implican dependencia universal.

---

# 51. README Summary vs Documentation Detail

Los README Components deberán favorecer información resumida.

Los Documentation Components podrán proporcionar profundidad adicional.

Modelo:

```text
README
        ↓
Understand

Documentation
        ↓
Explore
```

Ejemplo:

```text
README-ARCHITECTURE
        ↓
Architecture summary

DOC-ARCHITECTURE
        ↓
Detailed architecture
```

Ambas responsabilidades pueden coexistir sin duplicación cuando mantienen diferentes niveles de profundidad.

---

# 52. README Reuse Principle

Antes de crear una nueva responsabilidad reusable para README deberá evaluarse:

```text
Existing README Component?
        ↓
Can it be configured?
        ↓
Can it be extended?
        ↓
Is a new responsibility really needed?
```

Una variante de contenido no constituye automáticamente un nuevo Component.

La familia deberá mantenerse limitada a responsabilidades suficientemente recurrentes.

---

# 53. README Consumer Adaptation

Los consumidores podrán adaptar un README Component a su contexto.

La adaptación podrá afectar a:

- contenido;
- profundidad;
- enlaces;
- ejemplos;
- orden;
- visibilidad;
- integración con otros Components.

La responsabilidad deberá mantenerse reconocible.

Un Component no representa texto literal obligatorio.

---

# 54. README Availability vs Consumer Conformance

El catálogo mantiene explícitamente:

```text
README Component Availability
        ≠
README Consumer Conformance
```

Un Component puede permanecer `Conceptual` mientras un consumidor satisface correctamente la responsabilidad mediante contenido propio.

Del mismo modo, un Component `Implemented` puede existir sin ser utilizado por un consumidor concreto.

---

# 55. README Registry Maintenance

Cuando un README Component cambie de:

```text
Conceptual
        ↓
Implemented
```

deberán revisarse:

- registry table;
- implementation counts;
- canonical location;
- lifecycle status;
- relationships;
- Repository Templates que lo referencien;
- documentación de Framework.

La transición deberá producirse únicamente después de existir una implementación canónica suficiente.

---

# 56. Documentation Component Family

La familia:

```text
DOC-*
```

representa responsabilidades documentales especializadas reutilizables entre repositorios.

Estas responsabilidades suelen necesitar mayor profundidad que una sección README.

Podrán materializarse mediante:

- documentos Markdown;
- estructuras documentales;
- templates;
- conventions;
- metadata;
- otros artefactos apropiados.

La materialización concreta depende del Component.

---

# 57. Documentation Component Registry

El catálogo reconoce actualmente los siguientes Documentation Components:

| ID | Responsibility | Implementation |
| --- | --- | :---: |
| `DOC-ADR` | Architecture Decision Records | Conceptual |
| `DOC-API` | Documentación de APIs | Conceptual |
| `DOC-ARCHITECTURE` | Arquitectura del sistema | Implemented |
| `DOC-CHANGELOG` | Historial de cambios | Implemented |
| `DOC-DATABASE` | Modelo y responsabilidades de datos | Conceptual |
| `DOC-DEPLOYMENT` | Despliegue y operación | Conceptual |
| `DOC-DIAGRAMS` | Diagramas técnicos | Conceptual |
| `DOC-GLOSSARY` | Terminología y conceptos | Conceptual |
| `DOC-KNOWN-ISSUES` | Problemas conocidos y limitaciones | Conceptual |
| `DOC-PROJECT-STATUS` | Estado actual del proyecto | Implemented |
| `DOC-REFERENCES` | Referencias y fuentes relacionadas | Implemented |
| `DOC-RELEASE-NOTES` | Información específica de releases | Conceptual |
| `DOC-ROADMAP` | Evolución prevista | Conceptual |
| `DOC-SECURITY` | Documentación de seguridad | Conceptual |
| `DOC-TESTING` | Estrategia y prácticas de testing | Conceptual |

---

# 58. Documentation Registry Summary

Estado actual:

```text
Documentation Components
        15 total

Implemented
         4

Conceptual
        11
```

Components implementados:

```text
DOC-ARCHITECTURE
DOC-CHANGELOG
DOC-PROJECT-STATUS
DOC-REFERENCES
```

Components conceptuales:

```text
DOC-ADR
DOC-API
DOC-DATABASE
DOC-DEPLOYMENT
DOC-DIAGRAMS
DOC-GLOSSARY
DOC-KNOWN-ISSUES
DOC-RELEASE-NOTES
DOC-ROADMAP
DOC-SECURITY
DOC-TESTING
```

---

# 59. Implemented Documentation Components

Los Documentation Components implementados disponen de definición canónica reusable dentro de:

```text
framework/components/documentation/
```

Actualmente:

```text
DOC-ARCHITECTURE
DOC-CHANGELOG
DOC-PROJECT-STATUS
DOC-REFERENCES
```

El catálogo no deberá reproducir:

- Specifications completas;
- Metadata completa;
- templates completos;
- examples completos.

Su responsabilidad consiste en registrar existencia, clasificación y trazabilidad.

---

# 60. DOC-ARCHITECTURE

`DOC-ARCHITECTURE` representa la responsabilidad de documentar la arquitectura de un sistema o proyecto.

Registry classification:

```text
Family: Documentation
Implementation: Implemented
```

Puede complementar:

```text
README-ARCHITECTURE
```

cuando sea necesaria mayor profundidad.

---

# 61. DOC-CHANGELOG

`DOC-CHANGELOG` representa la responsabilidad de mantener un historial comprensible de cambios relevantes.

Registry classification:

```text
Family: Documentation
Implementation: Implemented
```

Su materialización podrá integrarse con prácticas de release y versionado.

---

# 62. DOC-PROJECT-STATUS

`DOC-PROJECT-STATUS` representa la responsabilidad de comunicar el estado actual de un proyecto mediante documentación especializada.

Registry classification:

```text
Family: Documentation
Implementation: Implemented
```

Podrá complementar:

```text
README-STATUS
```

cuando sea necesaria información más detallada.

---

# 63. DOC-REFERENCES

`DOC-REFERENCES` representa la responsabilidad de mantener referencias, fuentes y recursos relacionados.

Registry classification:

```text
Family: Documentation
Implementation: Implemented
```

La implementación pertenece específicamente a la familia Documentation.

No implica que exista una responsabilidad equivalente formalizada dentro de la familia README.

---

# 64. Conceptual Documentation Components

Los siguientes Components permanecen `Conceptual`:

```text
DOC-ADR
DOC-API
DOC-DATABASE
DOC-DEPLOYMENT
DOC-DIAGRAMS
DOC-GLOSSARY
DOC-KNOWN-ISSUES
DOC-RELEASE-NOTES
DOC-ROADMAP
DOC-SECURITY
DOC-TESTING
```

Sus responsabilidades están reconocidas.

Sin embargo, no disponen actualmente de una implementación canónica reusable suficiente dentro del Framework.

---

# 65. DOC-ADR

`DOC-ADR` representa la responsabilidad de documentar decisiones arquitectónicas significativas.

Registry classification:

```text
Family: Documentation
Implementation: Conceptual
```

La existencia de decisiones arquitectónicas documentadas dentro de GitHub Framework no constituye automáticamente una implementación reusable del Component.

---

# 66. DOC-API

`DOC-API` representa la responsabilidad de documentar interfaces o APIs relevantes.

Registry classification:

```text
Family: Documentation
Implementation: Conceptual
```

Su aplicabilidad dependerá del tipo de proyecto.

---

# 67. DOC-DATABASE

`DOC-DATABASE` representa la responsabilidad de documentar estructuras, decisiones y responsabilidades relacionadas con persistencia o datos.

Registry classification:

```text
Family: Documentation
Implementation: Conceptual
```

La responsabilidad deberá permanecer conceptual hasta disponer de una implementación reusable suficientemente validada.

---

# 68. DOC-DEPLOYMENT

`DOC-DEPLOYMENT` representa la responsabilidad de documentar cómo desplegar, publicar u operar una solución.

Registry classification:

```text
Family: Documentation
Implementation: Conceptual
```

Podrá relacionarse con futuros Workflow Components de deployment sin constituir la misma responsabilidad.

---

# 69. DOC-DIAGRAMS

`DOC-DIAGRAMS` representa la responsabilidad de incorporar y mantener diagramas técnicos cuando mejoren la comprensión del sistema.

Registry classification:

```text
Family: Documentation
Implementation: Conceptual
```

La existencia de diagramas concretos en consumidores no constituye una implementación reusable.

---

# 70. DOC-GLOSSARY

`DOC-GLOSSARY` representa la responsabilidad de mantener terminología compartida cuando un proyecto disponga de vocabulario suficientemente específico.

Registry classification:

```text
Family: Documentation
Implementation: Conceptual
```

---

# 71. DOC-KNOWN-ISSUES

`DOC-KNOWN-ISSUES` representa la responsabilidad de documentar problemas conocidos, limitaciones o comportamientos relevantes todavía no resueltos.

Registry classification:

```text
Family: Documentation
Implementation: Conceptual
```

La responsabilidad deberá utilizarse únicamente cuando aporte valor real al consumidor.

---

# 72. DOC-RELEASE-NOTES

`DOC-RELEASE-NOTES` representa la responsabilidad de comunicar información específica asociada a releases.

Registry classification:

```text
Family: Documentation
Implementation: Conceptual
```

Se diferencia de:

```text
DOC-CHANGELOG
```

porque las Release Notes pueden proporcionar contexto específico de una publicación, mientras el Changelog mantiene un historial continuo de cambios.

---

# 73. DOC-ROADMAP

`DOC-ROADMAP` representa la responsabilidad de documentar la evolución prevista de un proyecto.

Registry classification:

```text
Family: Documentation
Implementation: Conceptual
```

La existencia del `ROADMAP.md` del propio GitHub Framework no constituye automáticamente una implementación reusable de `DOC-ROADMAP`.

---

# 74. DOC-SECURITY

`DOC-SECURITY` representa la responsabilidad de documentar aspectos de seguridad relevantes para un proyecto.

Registry classification:

```text
Family: Documentation
Implementation: Conceptual
```

Su aplicabilidad y profundidad dependerán del contexto del consumidor.

---

# 75. DOC-TESTING

`DOC-TESTING` representa la responsabilidad de documentar estrategia, alcance y prácticas de testing.

Registry classification:

```text
Family: Documentation
Implementation: Conceptual
```

Puede relacionarse con:

```text
README-TESTING
WCL-CI
```

sin constituir la misma responsabilidad.

---

# 76. Documentation Composition

Los Documentation Components pueden combinarse según las necesidades del consumidor.

Ejemplo conceptual:

```text
DOC-ARCHITECTURE
+
DOC-API
+
DOC-DATABASE
+
DOC-TESTING
+
DOC-DEPLOYMENT
        ↓
Backend Documentation System
```

La composición pertenece principalmente a:

- Repository Templates;
- consumidores.

No al Component Catalog.

---

# 77. Documentation Component Relationships

Los Documentation Components podrán relacionarse entre sí.

Ejemplos:

```text
DOC-ARCHITECTURE
        ↔
DOC-DIAGRAMS
```

```text
DOC-API
        ↔
DOC-TESTING
```

```text
DOC-DEPLOYMENT
        ↔
DOC-SECURITY
```

```text
DOC-PROJECT-STATUS
        ↔
DOC-ROADMAP
```

Estas relaciones sirven para descubrimiento.

No constituyen automáticamente dependencies.

---

# 78. Documentation and README Relationships

README y Documentation Components podrán representar responsabilidades complementarias.

Ejemplos:

```text
README-ARCHITECTURE
        ↔
DOC-ARCHITECTURE
```

```text
README-TESTING
        ↔
DOC-TESTING
```

```text
README-STATUS
        ↔
DOC-PROJECT-STATUS
```

```text
README-ROADMAP
        ↔
DOC-ROADMAP
```

El README proporciona normalmente una superficie resumida.

La Documentation puede proporcionar mayor profundidad.

---

# 79. Documentation and Workflow Relationships

Documentation y Workflow Components podrán mantener relaciones complementarias.

Ejemplos:

```text
DOC-TESTING
        ↔
WCL-CI
```

```text
DOC-CHANGELOG
        ↔
WCL-RELEASE
```

```text
DOC-DEPLOYMENT
        ↔
WCL-CD
```

```text
DOC-SECURITY
        ↔
WCL-SECURITY
```

La Documentation explica, registra o contextualiza.

El Workflow coordina, ejecuta o gobierna procesos.

---

# 80. Documentation Consumer Adaptation

Los consumidores podrán adaptar Documentation Components a:

- dominio;
- stack;
- arquitectura;
- profundidad;
- audiencia;
- madurez;
- operación.

La adaptación no deberá modificar la responsabilidad canónica.

Una especialización contextual no constituye automáticamente un nuevo Component.

---

# 81. Documentation Materialization

Los Documentation Components no requieren necesariamente una estructura física idéntica.

Un Component podrá materializarse mediante:

```text
single Markdown file
directory
template
structured documentation set
convention
```

según su responsabilidad.

La clasificación `Implemented` deberá basarse en capacidad reusable real.

No en simetría del filesystem.

---

# 82. Documentation Availability vs Consumer Conformance

Un Documentation Component `Conceptual` puede representar una responsabilidad satisfecha correctamente por un consumidor.

Ejemplo:

```text
DOC-ROADMAP
        ↓
Conceptual in Framework

GitHub Framework
        ↓
ROADMAP.md
```

Estas dos afirmaciones pueden coexistir.

Por tanto:

```text
Consumer artifact
        ≠
Canonical Framework Component
```

---

# 83. Documentation Registry Maintenance

Cuando un Documentation Component cambie de:

```text
Conceptual
        ↓
Implemented
```

deberán revisarse:

- registry table;
- implementation counts;
- canonical location;
- lifecycle status;
- Repository Templates relacionados;
- relationships;
- Framework documentation.

El cambio deberá producirse después de disponer de implementación canónica real.

---

# 84. README Registry Quality Gates

Antes de modificar la clasificación de un README Component deberá verificarse:

- [ ] El Component representa una responsabilidad reusable.
- [ ] El ID es único.
- [ ] La responsabilidad no duplica otro README Component.
- [ ] Existe Specification cuando se clasifica como `Implemented`.
- [ ] Existe Metadata cuando se clasifica como `Implemented`.
- [ ] La materialización requerida existe.
- [ ] La implementación puede adaptarse a diferentes consumidores.
- [ ] La canonical location es real.
- [ ] Los conteos del catálogo permanecen sincronizados.

---

# 85. Documentation Registry Quality Gates

Antes de modificar la clasificación de un Documentation Component deberá verificarse:

- [ ] La responsabilidad continúa siendo diferenciada.
- [ ] El ID permanece estable.
- [ ] Existe Specification cuando se clasifica como `Implemented`.
- [ ] Existe Metadata cuando se clasifica como `Implemented`.
- [ ] Existe materialización reusable suficiente cuando corresponde.
- [ ] La canonical location es real.
- [ ] No se confunde documentación del propio Framework con implementación reusable.
- [ ] Las relaciones no se presentan como dependencies sin justificación.
- [ ] Los Repository Templates afectados permanecen coherentes.
- [ ] Los conteos del catálogo están sincronizados.

---

# 86. Family Statistics

Estado actual de las dos familias registradas en esta Part:

| Family | Implemented | Conceptual | Total |
| --- | ---: | ---: | ---: |
| README Components | 12 | 5 | 17 |
| Documentation Components | 4 | 11 | 15 |
| **Total** | **16** | **16** | **32** |

Estas cifras representan disponibilidad dentro de GitHub Framework.

No representan:

- adopción;
- conformidad;
- requirement levels;
- utilización por Repository Templates.

---

# 87. Implementation Distribution

Distribución actual:

```text
README
        12 Implemented
         5 Conceptual

Documentation
         4 Implemented
        11 Conceptual

Total
        16 Implemented
        16 Conceptual
```

La proporción de Components implementados constituye una métrica descriptiva.

No representa por sí sola madurez global del Framework.

---

# 88. Part 2 Conclusions

Las familias README y Documentation combinan actualmente responsabilidades implementadas y conceptuales.

Estado:

```text
README
        17 Components
        12 Implemented
         5 Conceptual

Documentation
        15 Components
         4 Implemented
        11 Conceptual
```

La clasificación se deriva de la disponibilidad canónica real.

Por tanto:

```text
Responsibility recognized
        ≠
Component implemented
```

y:

```text
Consumer artifact exists
        ≠
Framework implementation exists
```

Esta distinción permite que el Component Catalog represente fielmente el estado del Framework sin promover artificialmente responsabilidades todavía no materializadas.

---

# 89. Part 2 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Component Catalog.

---

# 09 - COMPONENT CATALOG

# Part 3/4

# Workflow & Visual Components Registry

---

# 90. Purpose

Esta Part registra las familias:

```text
WCL-*
VCL-*
```

correspondientes a:

- Workflow Components;
- Visual Components.

Ambas familias representan responsabilidades reutilizables reconocidas por GitHub Framework.

Su presencia en el Component Catalog no implica automáticamente que exista una implementación canónica reusable.

La clasificación:

```text
Conceptual
Implemented
```

deberá reflejar exclusivamente la disponibilidad real dentro del Framework.

---

# 91. Workflow Component Family

La familia:

```text
WCL-*
```

representa responsabilidades operativas reutilizables relacionadas con:

- planificación;
- desarrollo;
- integración;
- validación;
- release;
- seguridad;
- mantenimiento;
- evolución de repositorios.

Los Workflow Components no constituyen únicamente automatizaciones.

Podrán representar:

```text
Community Files
Configuration
Executable Workflows
Conventions
Composite Materializations
```

según la responsabilidad definida por el RDS.

---

# 92. Workflow Architecture Reference

La arquitectura canónica de la familia Workflow pertenece al Repository Design System.

El modelo general es:

```text
Workflow Component
        │
        ├── Specification
        ├── Metadata
        └── Materialization when required
```

El Component Catalog no vuelve a definir este contrato.

Su responsabilidad consiste en registrar:

- identidad;
- responsabilidad;
- clasificación de implementación;
- estado;
- localización;
- relaciones relevantes.

---

# 93. Workflow Component Registry

El catálogo reconoce actualmente los siguientes Workflow Components:

| ID | Responsibility | Implementation |
| --- | --- | :---: |
| `WCL-ISSUE` | Gestión estructurada de Issues | Conceptual |
| `WCL-LABEL` | Clasificación mediante labels | Conceptual |
| `WCL-PROJECT` | Organización y planificación del trabajo | Conceptual |
| `WCL-BRANCH` | Estrategia de ramas | Conceptual |
| `WCL-COMMIT` | Convención de commits | Conceptual |
| `WCL-PULL-REQUEST` | Integración mediante Pull Requests | Conceptual |
| `WCL-CODE-REVIEW` | Revisión de cambios | Conceptual |
| `WCL-CI` | Continuous Integration | Conceptual |
| `WCL-CD` | Continuous Delivery / Deployment | Conceptual |
| `WCL-DEPENDABOT` | Actualización de dependencias | Conceptual |
| `WCL-SECURITY` | Procesos de seguridad | Conceptual |
| `WCL-RELEASE` | Gestión de releases | Conceptual |
| `WCL-HOTFIX` | Gestión de correcciones urgentes | Conceptual |
| `WCL-DOCUMENTATION-UPDATE` | Sincronización documental | Conceptual |
| `WCL-ASSESSMENT` | Evaluación estructurada del repositorio | Conceptual |
| `WCL-MAINTENANCE` | Ciclo de mantenimiento | Conceptual |

---

# 94. Workflow Registry Summary

Estado actual:

```text
Workflow Components
        16 total

Implemented
         0

Conceptual
        16
```

Por tanto:

```text
Workflow Component Architecture
        ↓
Defined

Workflow Component Implementations
        ↓
Not yet available
```

La definición arquitectónica completada por el RDS no modifica automáticamente la clasificación de implementación.

---

# 95. Workflow Current Implementation Boundary

Los 16 Workflow Components permanecen:

```text
Conceptual
```

porque todavía no existe una biblioteca canónica materializada dentro de:

```text
framework/components/workflow/
```

que satisfaga el contrato definido por el RDS.

La utilización actual de:

- Issues;
- labels;
- Pull Requests;
- branches;
- commits;
- releases;
- documentación de mantenimiento;

dentro del propio GitHub Framework constituye práctica de consumidor.

No constituye por sí misma una implementación canónica reusable.

---

# 96. Workflow Conceptual Status

La clasificación `Conceptual` significa que la responsabilidad está reconocida.

No significa que:

- la responsabilidad sea hipotética;
- el proceso no exista en consumidores;
- no pueda formar parte de Repository Templates;
- no pueda evaluarse durante una Reference Implementation.

Significa únicamente:

```text
No canonical reusable implementation
currently exists in GitHub Framework
```

Esta distinción permite evolucionar la arquitectura sin simular disponibilidad material.

---

# 97. Workflow Materialization Classification

Cuando los Workflow Components se implementen, podrán utilizar diferentes mecanismos de materialización.

El catálogo podrá registrar esta información con fines de descubrimiento.

Tipos reconocidos arquitectónicamente:

```text
Community File
Configuration
Executable Workflow
Convention
Composite Materialization
```

Ejemplos conceptuales:

```text
WCL-ISSUE
        ↓
Community File / Configuration
```

```text
WCL-CI
        ↓
Executable Workflow
```

```text
WCL-BRANCH
        ↓
Convention / Configuration
```

```text
WCL-RELEASE
        ↓
Composite Materialization
```

La clasificación concreta deberá derivarse de la implementación canónica.

---

# 98. Executable Workflow Components

Algunos Workflow Components podrán requerir comportamiento ejecutable para satisfacer su responsabilidad.

Entre los candidatos se encuentran:

```text
WCL-CI
WCL-CD
WCL-DEPENDABOT
WCL-SECURITY
```

dependiendo de su implementación final.

El catálogo no deberá clasificarlos como `Implemented` únicamente porque exista una descripción del workflow.

Cuando la responsabilidad requiera ejecución automática deberá existir una materialización ejecutable reusable suficiente.

---

# 99. Non-Executable Workflow Components

Otros Workflow Components podrán satisfacer su responsabilidad sin código ejecutable.

Ejemplos potenciales:

```text
WCL-BRANCH
WCL-COMMIT
WCL-PULL-REQUEST
WCL-CODE-REVIEW
```

Podrán materializarse mediante:

- conventions;
- templates;
- community files;
- configuration;
- guidance;
- combinaciones apropiadas.

La ausencia de GitHub Actions no impide que un Workflow Component pueda considerarse `Implemented`.

---

# 100. Composite Workflow Components

Determinadas responsabilidades podrán requerir varios mecanismos coordinados.

Ejemplo conceptual:

```text
WCL-RELEASE
        │
        ├── Specification
        ├── Metadata
        ├── Versioning Convention
        ├── Release Process
        ├── CHANGELOG Interaction
        └── Optional Automation
```

El catálogo deberá mantener una única identidad:

```text
WCL-RELEASE
```

mientras la responsabilidad continúe siendo única.

No deberán crearse Components separados únicamente por cada archivo que forme parte de la materialización.

---

# 101. Workflow Implementation Transition

Cuando un Workflow Component pase de:

```text
Conceptual
        ↓
Implemented
```

el catálogo deberá actualizar:

- registry table;
- implementation counts;
- canonical location;
- lifecycle status cuando corresponda;
- version;
- materialization information cuando sea útil;
- relationships;
- registry summary.

La transición deberá producirse únicamente después de existir una implementación canónica suficiente.

---

# 102. Workflow Lifecycle

La futura clasificación habitual de un Workflow Component recién implementado podrá ser:

```text
Implementation: Implemented
Status: Experimental
```

mientras se valida mediante:

- Reference Implementation;
- dogfooding;
- consumer adoption;
- execution testing;
- Quality Gates.

La promoción posterior a:

```text
Stable
```

pertenece al lifecycle.

No a la implementation classification.

---

# 103. Workflow Relationships

Los Workflow Components podrán participar en secuencias operativas.

Ejemplo:

```text
WCL-ISSUE
        ↓
WCL-BRANCH
        ↓
WCL-COMMIT
        ↓
WCL-PULL-REQUEST
        ↓
WCL-CODE-REVIEW
        ↓
WCL-CI
        ↓
WCL-RELEASE
```

Esta representación facilita comprensión.

No constituye una cadena universal de dependencias.

El catálogo deberá distinguir:

```text
Operational Relationship
        ≠
Functional Dependency
```

---

# 104. Workflow Cross-Family Relationships

Los Workflow Components podrán relacionarse con otras familias.

Ejemplos:

```text
WCL-DOCUMENTATION-UPDATE
        ↔
Documentation Components
```

```text
WCL-RELEASE
        ↔
DOC-CHANGELOG
```

```text
WCL-CI
        ↔
DOC-TESTING
```

```text
WCL-SECURITY
        ↔
DOC-SECURITY
```

Estas relaciones representan responsabilidades complementarias.

No deberán convertirse automáticamente en dependencies.

---

# 105. Workflow Capability Mapping

El catálogo podrá utilizar capability mapping para facilitar descubrimiento.

| Component | Primary Capability |
| --- | --- |
| `WCL-ISSUE` | Work Management |
| `WCL-LABEL` | Work Classification |
| `WCL-PROJECT` | Project Planning |
| `WCL-BRANCH` | Version Control Strategy |
| `WCL-COMMIT` | Change Traceability |
| `WCL-PULL-REQUEST` | Collaborative Development |
| `WCL-CODE-REVIEW` | Review and Quality |
| `WCL-CI` | Continuous Integration |
| `WCL-CD` | Delivery / Deployment |
| `WCL-DEPENDABOT` | Dependency Maintenance |
| `WCL-SECURITY` | Secure Development |
| `WCL-RELEASE` | Release Management |
| `WCL-HOTFIX` | Urgent Change Management |
| `WCL-DOCUMENTATION-UPDATE` | Documentation Synchronization |
| `WCL-ASSESSMENT` | Engineering Governance |
| `WCL-MAINTENANCE` | Repository Maintenance |

El capability mapping es descriptivo.

No determina:

- requirement level;
- lifecycle;
- implementation classification;
- dependency.

---

# 106. Workflow Repository Template Integration

Los Repository Templates podrán seleccionar Workflow Components mediante:

```text
required
recommended
optional
```

La presencia de un Workflow Component `Conceptual` dentro de un Template no implica disponibilidad canónica.

Significa que la responsabilidad pertenece a la composición contextual.

Modelo:

```text
Repository Template
        ↓
Workflow Responsibility
        ↓
Consumer Materialization
```

hasta que exista una implementación reusable del Framework.

---

# 107. Workflow Availability vs Conformance

El catálogo mantiene:

```text
Workflow Component Availability
        ≠
Consumer Workflow Conformance
```

Ejemplo:

```text
WCL-PULL-REQUEST
Implementation: Conceptual
```

mientras:

```text
GitHub Framework
        ↓
Pull Request template + PR process
        ↓
Consumer responsibility potentially satisfied
```

Ambas afirmaciones pueden ser correctas simultáneamente.

---

# 108. Workflow Reference Implementation Boundary

La futura Workflow Reference Implementation deberá consumir Components previamente implementados.

No deberá utilizarse para declarar automáticamente como implementadas prácticas existentes.

Flujo correcto:

```text
Architecture
        ↓
Canonical Implementation
        ↓
Reference Implementation
        ↓
Validation
        ↓
Refinement
```

El catálogo deberá actualizarse al producirse la implementación.

No esperar necesariamente al resultado final de validación para representar que existe una capacidad material.

---

# 109. Workflow Registry Quality Gates

Antes de cambiar un `WCL-*` a `Implemented` deberá verificarse:

- [ ] El ID permanece único y estable.
- [ ] Existe Specification canónica.
- [ ] Existe Metadata canónica.
- [ ] La materialización requerida existe.
- [ ] La materialización satisface la responsabilidad.
- [ ] La ubicación canónica es real.
- [ ] El tipo de materialización puede identificarse.
- [ ] Las dependencies reales están declaradas.
- [ ] La implementación no está acoplada innecesariamente a un único consumidor.
- [ ] Los aspectos de seguridad han sido evaluados cuando existe ejecución.
- [ ] La clasificación del Catalog coincide con la implementación.
- [ ] Los conteos del Registry están sincronizados.

---

# 110. Visual Component Family

La familia:

```text
VCL-*
```

representa responsabilidades visuales reutilizables relacionadas con:

- identidad;
- presentación;
- comunicación;
- navegación;
- visualización técnica.

La Visual Component Library complementa al Visual Design System.

No lo sustituye.

Modelo:

```text
Visual Design System
        ↓
Rules and Constraints

Visual Components
        ↓
Reusable Visual Responsibilities
```

---

# 111. Visual Architecture Reference

La arquitectura canónica de Visual Components pertenece al RDS.

Modelo:

```text
Visual Component
        │
        ├── Specification
        ├── Metadata
        └── Materialization when required
```

La materialización podrá adoptar formas como:

```text
Asset
Layout
Snippet
Convention
Template
Configuration
Composite mechanism
```

El Component Catalog registra disponibilidad.

No redefine estas reglas.

---

# 112. Visual Component Registry

El catálogo reconoce actualmente los siguientes Visual Components:

| ID | Responsibility | Implementation |
| --- | --- | :---: |
| `VCL-BANNER` | Presentación visual del repositorio | Conceptual |
| `VCL-SOCIAL-PREVIEW` | Imagen de preview al compartir el repositorio | Conceptual |
| `VCL-HERO` | Composición visual principal | Conceptual |
| `VCL-BADGES` | Información visual compacta | Conceptual |
| `VCL-SKILL-ICONS` | Representación visual de tecnologías | Conceptual |
| `VCL-PROJECT-CARD` | Representación visual de proyectos | Conceptual |
| `VCL-STATS` | Visualización de métricas | Conceptual |
| `VCL-CONTRIBUTION-GRAPH` | Visualización de contribuciones | Conceptual |
| `VCL-TYPING-BANNER` | Presentación textual dinámica | Conceptual |
| `VCL-ARCHITECTURE-DIAGRAM` | Visualización de arquitectura | Conceptual |
| `VCL-WORKFLOW-DIAGRAM` | Visualización de procesos | Conceptual |
| `VCL-FOLDER-DIAGRAM` | Visualización de estructura | Conceptual |
| `VCL-NAVIGATION-CARD` | Navegación visual | Conceptual |
| `VCL-CALL-OUT` | Destacado visual de información | Conceptual |

---

# 113. Visual Registry Summary

Estado actual:

```text
Visual Components
        14 total

Implemented
         0

Conceptual
        14
```

La utilización real de:

- badges;
- diagrams;
- banners;
- callouts;
- icons;

en repositorios consumidores no modifica automáticamente esta clasificación.

---

# 114. Visual Current Implementation Boundary

Actualmente no existe una biblioteca canónica completa materializada dentro de:

```text
framework/components/visual/
```

Por tanto, los 14 Visual Components permanecen:

```text
Conceptual
```

El Visual Design System y los assets utilizados por consumidores constituyen fuentes relacionadas.

No equivalen automáticamente a implementaciones `VCL-*`.

---

# 115. Visual Conceptual Status

La clasificación conceptual permite reconocer responsabilidades visuales sin crear prematuramente:

- assets;
- templates;
- directories;
- metadata;
- implementations;

que todavía no hayan demostrado suficiente necesidad reusable.

Esto mantiene el principio:

```text
Recognized Responsibility
        ≠
Available Reusable Component
```

---

# 116. Visual Materialization

La futura materialización de Visual Components podrá incluir:

```text
assets
layouts
templates
snippets
configuration
conventions
metadata
```

La forma concreta dependerá de la responsabilidad.

Ejemplos:

```text
VCL-BANNER
        ↓
Reusable visual asset/template
```

```text
VCL-CALL-OUT
        ↓
Reusable convention
```

```text
VCL-ARCHITECTURE-DIAGRAM
        ↓
Diagram specification/template
```

El catálogo no deberá imponer una estructura uniforme.

---

# 117. Visual Relationships

Los Visual Components podrán mantener relaciones de complementariedad.

Ejemplo:

```text
VCL-BANNER
        ↔
VCL-HERO
        ↔
VCL-BADGES
```

Esto no implica una dependencia obligatoria.

Cada Component deberá conservar una responsabilidad independiente.

---

# 118. Visual Cross-Family Relationships

Entre las relaciones posibles se encuentran:

```text
README-HERO
        ↔
VCL-HERO
```

```text
README-ARCHITECTURE
        ↔
VCL-ARCHITECTURE-DIAGRAM
```

```text
DOC-ARCHITECTURE
        ↔
VCL-ARCHITECTURE-DIAGRAM
```

```text
WCL-RELEASE
        ↔
VCL-WORKFLOW-DIAGRAM
```

El Component visual proporciona representación.

No sustituye la responsabilidad documental u operativa.

---

# 119. Visual Capability Mapping

El catálogo podrá utilizar el siguiente mapping descriptivo:

| Component | Primary Capability |
| --- | --- |
| `VCL-BANNER` | Brand Presentation |
| `VCL-SOCIAL-PREVIEW` | Social Communication |
| `VCL-HERO` | Visual Information Architecture |
| `VCL-BADGES` | Compact Status Communication |
| `VCL-SKILL-ICONS` | Technology Communication |
| `VCL-PROJECT-CARD` | Project Presentation |
| `VCL-STATS` | Metrics Visualization |
| `VCL-CONTRIBUTION-GRAPH` | Activity Visualization |
| `VCL-TYPING-BANNER` | Dynamic Presentation |
| `VCL-ARCHITECTURE-DIAGRAM` | Architecture Visualization |
| `VCL-WORKFLOW-DIAGRAM` | Process Visualization |
| `VCL-FOLDER-DIAGRAM` | Structure Visualization |
| `VCL-NAVIGATION-CARD` | Visual Navigation |
| `VCL-CALL-OUT` | Information Highlighting |

El mapping facilita descubrimiento.

No constituye Specification.

---

# 120. Visual Repository Template Integration

Los Repository Templates podrán seleccionar Visual Components únicamente cuando exista una necesidad real de presentación o comunicación.

La madurez no deberá utilizarse como matriz automática.

Modelo:

```text
Project Type
+
Communication Needs
+
Visual Design System
        ↓
Visual Component Selection
```

La selección final seguirá siendo contextual.

---

# 121. Visual Availability vs Consumer Conformance

Puede existir:

```text
VCL-BANNER
Implementation: Conceptual
```

mientras un repositorio consumidor dispone de:

```text
custom banner
```

La existencia del asset puede satisfacer una responsabilidad local.

No convierte automáticamente ese asset en una implementación reusable de `VCL-BANNER`.

Por tanto:

```text
Consumer Visual Asset
        ≠
Canonical Visual Component
```

---

# 122. Visual Registry Quality Gates

Antes de cambiar un `VCL-*` a `Implemented` deberá verificarse:

- [ ] El ID permanece único y estable.
- [ ] Existe Specification canónica.
- [ ] Existe Metadata canónica.
- [ ] La materialización requerida está disponible.
- [ ] La materialización es reusable.
- [ ] No duplica reglas pertenecientes al Visual Design System.
- [ ] No duplica otro Visual Component.
- [ ] La ubicación canónica es real.
- [ ] Las dependencies reales están correctamente representadas.
- [ ] Los aspectos de accesibilidad han sido considerados.
- [ ] Las dependencias de proveedores externos están justificadas.
- [ ] La clasificación del Catalog coincide con la implementación.

---

# 123. Workflow and Visual Cross-Consumer Reuse

Workflow y Visual Components podrán tener consumidores distintos.

| Family | Primary Context | Possible Consumers |
| --- | --- | --- |
| Workflow | Repository operations | GitHub repositories, Repository Templates, automation |
| Visual | Visual communication | README, Documentation, GitHub Profile, GitHub Pages |

La posibilidad de reutilización no implica obligatoriedad.

Cada adopción deberá responder a una necesidad real.

---

# 124. Workflow and Visual Evolution

Las dos familias evolucionarán mediante el lifecycle general:

```text
Recognized Responsibility
        ↓
Conceptual
        ↓
Specification
        ↓
Metadata
        ↓
Materialization
        ↓
Implemented
        ↓
Validation
        ↓
Stable when justified
```

No deberán implementarse todos los Components simultáneamente.

La evolución será incremental y guiada por casos reales.

---

# 125. Family Statistics

Estado actual de las familias registradas en esta Part:

| Family | Implemented | Conceptual | Total |
| --- | ---: | ---: | ---: |
| Workflow Components | 0 | 16 | 16 |
| Visual Components | 0 | 14 | 14 |
| **Total** | **0** | **30** | **30** |

Estas cifras representan disponibilidad dentro del Framework.

No representan adopción ni utilidad potencial.

---

# 126. Current Development Focus

La siguiente familia prevista para materialización es:

```text
Workflow Components
```

El flujo actual de evolución es:

```text
Workflow Component Architecture
        ↓
Core Workflow Components
        ↓
Workflow Reference Implementation
        ↓
Workflow Standards
```

El Component Catalog deberá evolucionar junto con cada transición real de implementación.

La familia Visual permanecerá conceptual hasta que exista una necesidad de implementación explícitamente planificada.

---

# 127. Part 3 Conclusions

Las familias **Workflow** y **Visual** representan actualmente responsabilidades reconocidas arquitectónicamente pero todavía no materializadas como bibliotecas canónicas del Framework.

Estado:

```text
Workflow
        16 Components
         0 Implemented
        16 Conceptual

Visual
        14 Components
         0 Implemented
        14 Conceptual
```

La arquitectura Workflow ya dispone de un contrato de materialización definido por el RDS.

Esto no cambia su clasificación de implementación.

El siguiente cambio relevante deberá producirse cuando existan realmente:

```text
framework/components/workflow/
        ↓
Canonical WCL implementations
```

La familia Visual mantiene igualmente la separación:

```text
Visual responsibility recognized
        ≠
Visual Component implemented
```

El catálogo preserva así una representación fiel del Framework actual.

---

# 128. Part 3 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Component Catalog.

---

# 09 - COMPONENT CATALOG

# Part 4/4

# Repository Templates & Framework Governance

---

# 129. Purpose

Esta Part completa el Component Catalog incorporando:

- Repository Templates;
- Maturity Profiles;
- relaciones globales del Framework;
- trazabilidad;
- gobernanza del catálogo;
- resumen global del Registry.

Los Repository Templates no constituyen una familia de Framework Components.

Representan composiciones reutilizables de Components adaptadas a tipos concretos de proyecto.

Los Maturity Profiles constituyen una dimensión independiente.

El Component Catalog deberá mantener estas distinciones explícitas.

---

# 130. Repository Template Registry

Los Repository Templates utilizan el prefijo:

```text
TPL-*
```

Su responsabilidad consiste en definir composiciones reutilizables de Framework Components para tipos concretos de proyecto.

Un Repository Template:

- identifica un project type;
- declara una madurez mínima recomendada;
- selecciona Components existentes;
- asigna requirement levels contextuales;
- proporciona guidance de composición;
- permite evaluar consumer conformance.

No introduce nuevas responsabilidades canónicas dentro de los Components.

---

# 131. Repository Template Canonical Definition

Un Repository Template implementado dispone de una definición canónica formada por:

```text
Specification
        +
Metadata
```

La Specification define:

- propósito;
- alcance;
- project type;
- composición;
- requirement levels;
- guidance;
- extensibilidad;
- especialización.

La Metadata proporciona representación estructurada para:

- identidad;
- versionado;
- lifecycle;
- project type;
- maturity;
- Components;
- requirement levels;
- automatización futura.

La implementación canónica actual se mantiene en:

```text
framework/templates/repositories/
```

---

# 132. Repository Template Registry

El catálogo registra actualmente:

| ID | Project Type | Maturity | Lifecycle | Implementation |
| --- | --- | :---: | --- | --- |
| `TPL-BACKEND` | Backend | L2 | Experimental | Implemented |
| `TPL-FULLSTACK` | Full Stack | L2 | Experimental | Implemented |
| `TPL-DOCUMENTATION` | Documentation | L2 | Experimental | Implemented |

Los tres Templates disponen de implementación canónica.

No existen actualmente otros `TPL-*` oficiales.

---

# 133. Repository Template Summary

Estado actual:

```text
Repository Templates
        3 total

Implemented
        3

Conceptual
        0
```

Los tipos de proyecto potenciales no deberán contabilizarse como Templates oficiales hasta disponer de:

- Specification;
- Metadata;
- composición;
- implementación;
- validación suficiente.

---

# 134. TPL-BACKEND

`TPL-BACKEND` representa repositorios cuyo producto principal es una aplicación, servicio o capacidad backend.

Registry classification:

```text
ID: TPL-BACKEND
Project Type: Backend
Maturity: L2
Lifecycle: Experimental
Implementation: Implemented
```

Canonical location:

```text
framework/templates/repositories/backend/
```

La composición exacta deberá consultarse en su Metadata y Specification.

El Component Catalog no la duplica.

---

# 135. TPL-FULLSTACK

`TPL-FULLSTACK` representa repositorios que integran responsabilidades frontend y backend dentro de una misma unidad de proyecto.

Registry classification:

```text
ID: TPL-FULLSTACK
Project Type: Full Stack
Maturity: L2
Lifecycle: Experimental
Implementation: Implemented
```

Canonical location:

```text
framework/templates/repositories/fullstack/
```

La selección concreta de Components pertenece a su definición canónica.

---

# 136. TPL-DOCUMENTATION

`TPL-DOCUMENTATION` representa repositorios cuyo producto principal es documentación, conocimiento estructurado o documentación de Framework.

Registry classification:

```text
ID: TPL-DOCUMENTATION
Project Type: Documentation
Maturity: L2
Lifecycle: Experimental
Implementation: Implemented
```

Canonical location:

```text
framework/templates/repositories/documentation/
```

GitHub Framework ha sido utilizado como Reference Implementation de este Template mediante dogfooding.

Esta validación no modifica su naturaleza de Repository Template.

---

# 137. Repository Template Requirement Levels

Los Templates utilizan:

```text
required
recommended
optional
```

para expresar la importancia contextual de un Component.

El Component Catalog deberá mantener la distinción:

```text
Component Priority
        ≠
Template Requirement Level
```

y:

```text
Implementation Classification
        ≠
Template Requirement Level
```

Un Component `Conceptual` puede formar parte legítimamente de un Template cuando su responsabilidad corresponda al contrato.

---

# 138. Template Composition Source

La composición canónica pertenece exclusivamente a cada Repository Template.

Por tanto, el Catalog no deberá mantener una segunda matriz normativa de:

```text
required
recommended
optional
```

para todos los Templates.

El catálogo podrá exponer relaciones derivadas con fines de descubrimiento.

La fuente normativa continuará siendo:

```text
framework/templates/repositories/<template>/
```

---

# 139. Component Availability in Templates

Un Repository Template podrá referenciar Components:

```text
Implemented
Conceptual
```

La disponibilidad de implementación no determina su requirement level.

Ejemplo conceptual:

```text
Component
Implementation: Conceptual

Template
Requirement Level: Required
```

puede ser válido cuando:

- la responsabilidad pertenece al contrato del Template;
- el Framework todavía no dispone de implementación reusable;
- el consumidor puede satisfacer la responsabilidad mediante una materialización compatible.

---

# 140. Template Conformance

El catálogo deberá distinguir:

```text
Template composition
        ≠
Consumer conformance
```

La composición define responsabilidades esperadas.

La conformance evalúa si el consumidor las satisface.

Modelo:

```text
Repository Template
        ↓
Selected Responsibilities
        ↓
Consumer Materialization
        ↓
Conformance Evaluation
```

El Component Catalog no realiza por sí mismo esta evaluación.

---

# 141. Template Lifecycle

Los Repository Templates podrán utilizar lifecycle states:

```text
Draft
Experimental
Stable
Deprecated
Retired
```

Los Templates actuales permanecen:

```text
Experimental
```

Esto significa que:

- están implementados;
- pueden utilizarse;
- están siendo validados;
- su contrato todavía puede evolucionar.

No significa que sean conceptuales.

---

# 142. Repository Template Promotion

La promoción:

```text
Experimental
        ↓
Stable
```

deberá basarse en evidencia.

Entre los factores relevantes podrán encontrarse:

- Reference Implementations;
- consumer adoption;
- conformance results;
- estabilidad de composición;
- ausencia de gaps críticos;
- calidad de Metadata;
- mantenimiento;
- compatibilidad.

La antigüedad no constituye evidencia suficiente.

---

# 143. Potential Repository Templates

Tipos de proyecto reconocidos como posibles candidatos futuros incluyen:

```text
AI
Library
Website
```

Estos nombres no constituyen IDs oficiales.

No deberán registrarse prematuramente como:

```text
TPL-AI
TPL-LIBRARY
TPL-WEBSITE
```

hasta que exista una necesidad reusable suficientemente validada.

---

# 144. Maturity Profiles

GitHub Framework mantiene cuatro niveles de madurez:

| Level | Description |
| --- | --- |
| L1 | Experimental |
| L2 | Public Basic |
| L3 | Supporting |
| L4 | Strategic |

Los Maturity Profiles representan expectativas sobre:

- calidad;
- documentación;
- mantenimiento;
- automatización;
- governance;
- continuidad.

No constituyen Repository Templates.

---

# 145. Maturity Independence

La madurez constituye una dimensión independiente.

Por tanto:

```text
Project Type
        ↓
Repository Template
```

y:

```text
Maturity
        ↓
Quality and Maintenance Expectations
```

son decisiones distintas.

No existen Templates como:

```text
TPL-L1
TPL-L2
TPL-L3
TPL-L4
```

---

# 146. Maturity and Requirement Levels

La madurez no deberá utilizarse para asignar automáticamente requirement levels.

Ejemplo incorrecto:

```text
L3
        ↓
WCL-CI must be Required
```

La necesidad de `WCL-CI` depende de:

- project type;
- Repository Template;
- contexto del consumidor;
- necesidades operativas.

La madurez puede aumentar expectativas.

No determina por sí sola la composición.

---

# 147. Repository Context

Factores como:

- desarrollo individual;
- trabajo en equipo;
- open source;
- investigación;
- entorno empresarial;

pueden modificar necesidades de un consumidor.

Estos factores forman parte del contexto.

No constituyen actualmente una familia formal de Repository Profiles.

El modelo anterior de Profiles permanece fuera de la arquitectura activa.

---

# 148. Repository Profile Boundary

Identificadores históricos o conceptuales como:

```text
PROFILE-SOLO
PROFILE-TEAM
PROFILE-OPEN-SOURCE
PROFILE-RESEARCH
PROFILE-ENTERPRISE
```

no forman parte del Registry actual.

La experiencia obtenida durante la evolución del Framework mostró que estos conceptos mezclaban:

- contexto;
- composición;
- madurez;
- governance.

El modelo actual separa estas dimensiones.

---

# 149. Framework Composition

La arquitectura global del Framework puede representarse como:

```text
Standards
        ↓
Repository Design System
        ↓
Framework Components
        ├── README
        ├── Documentation
        ├── Workflow
        └── Visual
        ↓
Repository Templates
        ↓
Repository Implementations
        ↓
Reference Implementations
        ↓
Validation and Evolution
```

Los Maturity Profiles operan como una dimensión independiente.

No constituyen una capa física adicional.

---

# 150. Framework Registry Summary

Estado global actual:

| Element | Implemented | Conceptual | Total |
| --- | ---: | ---: | ---: |
| README Components | 12 | 5 | 17 |
| Documentation Components | 4 | 11 | 15 |
| Workflow Components | 0 | 16 | 16 |
| Visual Components | 0 | 14 | 14 |
| Repository Templates | 3 | 0 | 3 |
| **Total** | **19** | **46** | **65** |

Estas cifras representan elementos reconocidos por el Registry.

No representan:

- adoption;
- consumer conformance;
- project maturity;
- requirement levels;
- release readiness.

---

# 151. Framework Component Summary

Considerando únicamente Framework Components:

```text
README
        17

Documentation
        15

Workflow
        16

Visual
        14
        ──
        62 total
```

Distribución:

```text
Implemented
        16

Conceptual
        46
```

Los Repository Templates se contabilizan por separado porque no constituyen Framework Components.

---

# 152. Implementation Distribution

Distribución global:

```text
Framework Components
        16 Implemented
        46 Conceptual

Repository Templates
         3 Implemented
         0 Conceptual

Total Registered Elements
        65
```

Por clasificación de implementación:

```text
Implemented
        19

Conceptual
        46
```

La proporción de elementos materializados constituye una métrica descriptiva.

No representa el progreso global exacto del proyecto.

---

# 153. Registry Relationships

Principales relaciones:

| Element | Main Responsibility |
| --- | --- |
| README Components | Repository entry and presentation |
| Documentation Components | Detailed knowledge |
| Workflow Components | Operational processes |
| Visual Components | Visual communication |
| Repository Templates | Contextual composition |
| Maturity Profiles | Quality expectations |

Estas relaciones describen responsabilidad.

No constituyen dependencias universales.

---

# 154. Repository Selection Strategy

Conceptualmente, un consumidor deberá seguir:

```text
Identify Project Type
        ↓
Select Repository Template
        ↓
Review Maturity Expectations
        ↓
Apply Required Responsibilities
        ↓
Evaluate Recommended Components
        ↓
Add Optional Components when justified
        ↓
Configure Consumer Context
        ↓
Validate
```

El Component Catalog facilita descubrimiento durante este proceso.

No sustituye la lógica del Repository Template.

---

# 155. Framework Layers

El Framework puede analizarse mediante:

```text
Standards Layer
        ↓
Architecture Layer
        ↓
Component Layer
        ↓
Template Layer
        ↓
Implementation Layer
        ↓
Validation Layer
        ↓
Governance Layer
```

Estas capas representan responsabilidades.

No implican estructuras físicas obligatorias.

---

# 156. Element Traceability

Todo elemento registrado deberá permitir responder, cuando corresponda:

- ¿Cuál es su ID?
- ¿Cuál es su responsabilidad?
- ¿A qué familia pertenece?
- ¿Es `Conceptual` o `Implemented`?
- ¿Cuál es su lifecycle status?
- ¿Cuál es su versión?
- ¿Dónde está su definición canónica?
- ¿Qué dependencies mantiene?
- ¿Qué Repository Templates lo referencian?
- ¿Cuál es su maturity?
- ¿Qué consumidores conocidos existen?

La trazabilidad deberá derivarse de fuentes reales.

No de información duplicada manualmente sin control.

---

# 157. Registry Fields

El catálogo podrá exponer:

## Canonical Fields

- ID;
- Name;
- Family;
- Version;
- Status;
- Priority;
- Audience;
- Maturity;
- Dependencies.

## Derived Fields

- Implementation;
- canonical location;
- related Templates;
- known consumers;
- last reviewed;
- materialization classification;
- capability mapping.

Los campos derivados deberán mantenerse sincronizados.

---

# 158. Catalog Governance

Todo elemento registrado deberá respetar la gobernanza del RDS.

Para incorporar o modificar un elemento deberá evaluarse:

- responsabilidad;
- duplicación;
- identidad;
- implementación;
- Metadata;
- lifecycle;
- dependencies;
- relaciones;
- compatibilidad;
- consumer impact.

La incorporación al catálogo proporciona descubrimiento.

No sustituye implementación ni validación.

---

# 159. Registry Change Process

Los cambios del catálogo deberán producirse como consecuencia de cambios reales en el Framework.

Flujo habitual:

```text
Framework Change
        ↓
Canonical Source Update
        ↓
Catalog Synchronization
        ↓
Validation
```

No:

```text
Catalog Change
        ↓
Assume Framework changed
```

Esta dirección protege la fuente de verdad.

---

# 160. Catalog Review Triggers

El Component Catalog deberá revisarse cuando:

- se implemente un Component;
- se depreque un Component;
- cambie una versión;
- aparezca un nuevo Repository Template;
- evolucione un Template;
- cambien dependencies;
- se detecte un canonical location incorrecto;
- una auditoría revele drift;
- cambie la arquitectura del RDS.

Las revisiones deberán mantenerse trazables.

---

# 161. Catalog Drift

Existe `Catalog Drift` cuando la representación del catálogo no coincide con la realidad.

Ejemplos:

```text
Catalog says Implemented
        ↓
No canonical implementation exists
```

o:

```text
Canonical Component exists
        ↓
Catalog still says Conceptual
```

El drift deberá considerarse deuda del Design System.

Deberá corregirse cuando se detecte.

---

# 162. Catalog Audit

Las auditorías del Component Catalog podrán comprobar:

- IDs;
- duplicados;
- implementation classification;
- canonical locations;
- Metadata;
- counts;
- Repository Template references;
- dependencies;
- lifecycle;
- missing registrations;
- orphan implementations.

Las auditorías automáticas podrán incorporarse en futuras versiones del Framework.

---

# 163. Machine-Readable Evolution

Conforme evolucione GitHub Framework, parte del Component Catalog podrá derivarse automáticamente de Metadata canónica.

Modelo futuro:

```text
Canonical Metadata
        ↓
Registry Index
        ↓
Human-readable Catalog
+
Automation
```

Esto permitirá reducir drift.

El documento Markdown podrá continuar proporcionando interpretación humana.

---

# 164. Framework Automation Relationship

Framework Automation deberá consumir:

```text
Canonical Definitions
        +
Metadata
        +
Repository Templates
```

El Component Catalog podrá proporcionar índices o navegación.

No deberá convertirse en el único origen machine-readable cuando exista Metadata más precisa.

---

# 165. Repository Bootstrap Relationship

Las futuras herramientas de bootstrap podrán utilizar:

```text
Repository Template
        ↓
Resolve Component IDs
        ↓
Locate Implemented Components
        ↓
Detect Conceptual Responsibilities
        ↓
Materialize / Guide Consumer
```

El Catalog podrá facilitar resolución.

La lógica normativa deberá derivarse de Templates y Components.

---

# 166. Validation Tooling Relationship

Los validadores futuros podrán utilizar el Catalog para:

- discovery;
- classification;
- canonical location;
- status overview.

La evaluación de conformance deberá utilizar contratos canónicos.

No únicamente las tablas del Catalog.

---

# 167. Repository Health Relationship

Repository Health podrá utilizar información del Component Catalog como una de sus entradas.

Ejemplos:

- availability;
- Template composition;
- consumer adoption;
- lifecycle.

Sin embargo, el Catalog no define actualmente un algoritmo de Health.

La capacidad permanece futura.

---

# 168. Registry Anti-Patterns

No deberán existir:

- IDs duplicados;
- Responsibilities equivalentes con IDs distintos;
- canonical locations ficticias;
- Components conceptuales presentados como implementados;
- Templates potenciales presentados como oficiales;
- Profiles obsoletos registrados como activos;
- Maturity Profiles registrados como Templates;
- lifecycle confundido con implementation classification;
- priority confundida con requirement level;
- availability confundida con conformance;
- counts desincronizados;
- Metadata contradictoria;
- información del Catalog utilizada como Specification completa;
- automatización basada en datos derivados obsoletos.

---

# 169. Global Catalog Quality Gates

Antes de aprobar una nueva versión del Component Catalog deberá verificarse:

- [ ] Las familias coinciden con el RDS.
- [ ] Los IDs son únicos.
- [ ] Los Registry tables coinciden con las responsabilidades reconocidas.
- [ ] La clasificación `Implemented / Conceptual` refleja la realidad.
- [ ] Los lifecycle states son coherentes.
- [ ] Los canonical locations existen cuando se declaran.
- [ ] Los Repository Templates registrados coinciden con la implementación.
- [ ] Los Maturity Profiles permanecen como dimensión independiente.
- [ ] Los Repository Profiles no aparecen como arquitectura activa.
- [ ] Las dependencies reales están correctamente representadas.
- [ ] No existen requirement levels globales.
- [ ] Los counts están sincronizados.
- [ ] La Metadata reproducida coincide con fuentes canónicas.
- [ ] La disponibilidad no se confunde con consumer conformance.
- [ ] El Catalog continúa alineado con el RDS.

---

# 170. Registry Evolution Strategy

La evolución del Catalog seguirá:

```text
Recognize
        ↓
Classify
        ↓
Implement
        ↓
Synchronize
        ↓
Validate
        ↓
Maintain
```

Los elementos conceptuales podrán permanecer registrados durante varias releases cuando su responsabilidad continúe siendo válida.

No deberán implementarse únicamente para reducir el número de Components conceptuales.

---

# 171. Current Framework Focus

La evolución actual del Framework se centra en:

```text
Workflow Component Architecture
        ↓
Core Workflow Components
        ↓
Workflow Reference Implementation
        ↓
Workflow Standards
        ↓
v0.5.0
```

Por tanto, el próximo cambio esperado en el Registry será la transición de determinados `WCL-*`:

```text
Conceptual
        ↓
Implemented
```

cuando sus implementaciones canónicas existan realmente.

---

# 172. Long-Term Vision

El Component Catalog deberá convertirse en la interfaz central de descubrimiento del ecosistema GitHub Framework.

Permitirá comprender:

- qué responsabilidades reconoce el Framework;
- cuáles están implementadas;
- cuáles siguen conceptuales;
- qué Repository Templates existen;
- qué lifecycle mantiene cada elemento;
- dónde se encuentran las fuentes canónicas;
- cómo se relacionan los diferentes elementos.

Con el tiempo podrá alimentar:

- CLI;
- Repository Wizards;
- validators;
- generators;
- dependency analysis;
- migration tooling;
- governance tools;
- Framework Automation.

Su valor continuará siendo:

```text
Discovery
+
Classification
+
Traceability
```

No duplicación arquitectónica.

---

# 173. Final Conclusions

El **Component Catalog** proporciona una vista gobernada del estado real de GitHub Framework.

Las responsabilidades están separadas:

```text
Repository Design System
        ↓
Architecture

Specifications + Metadata + Materialization
        ↓
Canonical Definitions

Component Catalog
        ↓
Discovery and Classification

Repository Templates
        ↓
Contextual Composition

Repository Implementations
        ↓
Consumer Materialization

Reference Implementations
        ↓
Validation
```

Estado actual:

```text
Framework Components
        62 total

Implemented
        16

Conceptual
        46


Repository Templates
         3 total

Implemented
         3

Conceptual
         0


Total Registered Elements
        65
```

La familia Workflow dispone ahora de un contrato arquitectónico suficientemente definido para iniciar implementación.

Sin embargo, sus 16 Components continúan `Conceptual` hasta que existan implementaciones canónicas reales.

El Catalog mantiene así una fotografía verificable del Framework:

```text
Architecture recognized
        ≠
Implementation available
```

```text
Implementation available
        ≠
Consumer conformance
```

```text
Lifecycle status
        ≠
Implementation classification
```

Estas distinciones permiten que GitHub Framework evolucione sin presentar como materializado aquello que todavía pertenece al diseño.

---

# 174. Revision History

| Version | Date | Description |
| --- | --- | --- |
| 1.0.0 | 2026-08-05 | Primera versión del Component Catalog. |
| 1.0.1 | 2026-08-11 | Metadata alineada con GitHub Framework durante la implementación de referencia del Documentation Framework. |
| 1.1.0 | 2026-08-16 | Arquitectura del catálogo consolidada alrededor de fuentes canónicas, clasificación de implementación, Repository Templates contextuales y Maturity Profiles independientes; retirados Repository Profiles y Maturity Templates como elementos activos. |
| 1.2.0 | 2026-08-19 | Catalog alineado con RDS 1.2.0, incorporando distinción explícita entre Specification, Metadata y Materialization, implementation classification frente a lifecycle, Component availability frente a consumer conformance y contrato actualizado para futura materialización de Workflow Components. |
