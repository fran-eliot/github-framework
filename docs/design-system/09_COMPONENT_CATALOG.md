# 09 - COMPONENT CATALOG

| Field        | Value                     |
| ------------ | ------------------------- |
| **Project**  | GitHub Framework          |
| **Document** | Component Catalog         |
| **Version**  | 1.1.0 |
| **Status**   | Stable                    |
| **Owner**    | Fran Ramirez              |

---

# Part 1/4

# Registry Foundations

---

# 1. Purpose

El **Component Catalog (CC)** constituye el registro central de descubrimiento y clasificación de los elementos reutilizables reconocidos por GitHub Framework.

Su función consiste en facilitar la identificación, localización y comprensión de:

- Framework Components;
- Repository Templates;
- otros elementos gobernados por el RDS cuando corresponda.

El catálogo no sustituye las definiciones canónicas de estos elementos.

Cuando exista implementación, la definición canónica de un Framework Component estará formada por su especificación y metadata correspondientes.

El **Repository Design System (RDS)** define el modelo arquitectónico, las responsabilidades y las reglas generales del sistema.

Por tanto:

```text
RDS
        ↓
Architecture and rules

Specification + Metadata
        ↓
Canonical element definition

Component Catalog
        ↓
Discovery and classification
```



---

# 2. Vision

El catálogo deberá facilitar el descubrimiento de capacidades reutilizables antes de diseñar nuevas soluciones.

Antes de introducir un nuevo Framework Component deberá comprobarse si:

- existe una responsabilidad equivalente;
- puede reutilizarse un Component existente;
- existe un Repository Template adecuado;
- la necesidad es suficientemente recurrente para justificar generalización.

El catálogo deberá permitir realizar esta evaluación sin convertirse en una copia de las especificaciones canónicas.

---

# 3. Relationship with Other Sources

| Source | Responsibility |
|---|---|
| Repository Design System | Define la arquitectura y las reglas del sistema |
| Component Specification | Define la responsabilidad y comportamiento del Component |
| Component Metadata | Proporciona información estructurada y machine-readable |
| Component Catalog | Facilita descubrimiento y clasificación |
| Repository Templates | Componen Components según el tipo de proyecto |
| Repository Standards | Definen reglas aplicables |
| Reference Implementations | Validan el Framework mediante uso real |

El Component Catalog no duplicará especificaciones completas.

Cuando exista una fuente canónica deberá enlazar o referenciarla.

---

# 4. Registry Philosophy

Cada responsabilidad reutilizable deberá disponer de una definición canónica identificable.

No deberán coexistir Framework Components diferentes que representen esencialmente la misma responsabilidad.

Cuando aparezca una necesidad nueva deberá evaluarse primero si:

- existe un Component equivalente;
- puede ampliarse uno existente;
- puede resolverse mediante configuración;
- pertenece realmente a un Repository Template;
- debe permanecer específica del consumidor;
- justifica la creación de una nueva responsabilidad reutilizable.

El catálogo deberá reflejar el sistema existente y no crear arquitectura paralela.

---

# 5. Registry Architecture

El catálogo organiza los elementos reutilizables según su naturaleza.

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

Las familias de Framework Components representan responsabilidades reutilizables.

Los Repository Templates representan composiciones reutilizables de esas responsabilidades para tipos concretos de proyecto.

Los Maturity Profiles constituyen una dimensión independiente y no forman una familia de Components.

---

# 6. Element Identifier

Todo elemento registrado dispondrá de un identificador estable cuando su naturaleza lo requiera.

Formato general:

```text
PREFIX-NAME
```

Ejemplos.

```
README-HERO

DOC-ADR

WCL-CI

VCL-BANNER

TPL-BACKEND
```

Los prefijos permiten identificar la naturaleza o familia del elemento.

Los identificadores deberán permanecer estables durante la evolución del Framework.

---

# 7. Naming Rules

Los identificadores deberán cumplir:

* inglés;
* mayúsculas;
* guiones;
* sin abreviaturas ambiguas;
* estables entre versiones.

Nunca deberán reutilizarse para otro componente.

---

# 8. Component Metadata

Los Framework Components implementados dispondrán de metadata estructurada conforme a su definición canónica.

Entre los campos actualmente utilizados se encuentran:

| Field | Description |
|---|---|
| ID | Identificador |
| Name | Nombre |
| Family | Familia |
| Version | Versión |
| Status | Estado |
| Priority | Prioridad orientativa del Component |
| Audience | Audiencia principal |
| Maturity | Madurez mínima recomendada |
| Description | Descripción resumida |
| Dependencies | Dependencias declaradas |

La metadata podrá evolucionar conforme maduren las capacidades del Framework.

El catálogo no deberá definir un esquema alternativo incompatible con la metadata canónica.

---

# 9. Component States

Todo componente tendrá un estado.

| State        | Meaning         |
| ------------ | --------------- |
| Draft        | Diseño inicial  |
| Experimental | Validación      |
| Stable       | Uso recomendado |
| Deprecated   | Sustituido      |
| Retired      | Eliminado       |

Los estados deberán comunicarse claramente.

El estado describe el lifecycle del Component.

No determina si debe utilizarse en un Repository Template concreto.

---

# 10. Component Versioning

Cada componente seguirá Semantic Versioning.

Ejemplos.

```text
README-HERO

1.0.0
```

```text
VCL-BANNER

2.1.0
```

La evolución de un Framework Component no implica la actualización inmediata del resto del sistema, salvo cuando existan dependencias o contratos afectados.

---

# 11. Registry Families

El catálogo reconoce actualmente cuatro familias principales de Framework Components:

| Prefix | Family |
|---|---|
| README | README Components |
| DOC | Documentation Components |
| WCL | Workflow Components |
| VCL | Visual Components |

Además, registra Repository Templates mediante el prefijo:

| Prefix | Element |
|---|---|
| TPL | Repository Templates |

Los Repository Templates no constituyen una familia de Framework Components.

Los Maturity Profiles tampoco constituyen Components y se gestionan como una dimensión independiente del modelo.

La incorporación de nuevas familias deberá ser coherente con el Repository Design System.

---

# 12. Component Relationships

Los Framework Components podrán mantener relaciones o dependencias cuando exista una necesidad real.

Ejemplo conceptual:

```text
README-ARCHITECTURE
        ↔
DOC-ARCHITECTURE
```

Una relación no implica necesariamente dependencia funcional.

Las dependencias reales deberán declararse explícitamente en la definición canónica del Component.

No deberán introducirse jerarquías artificiales únicamente para mantener una estructura uniforme.

---

# 13. Component Dependencies

Las dependencias entre Framework Components deberán representar relaciones funcionales reales.

Cuando exista una dependencia deberá quedar registrada en la metadata o especificación canónica correspondiente.

Las dependencias no deberán confundirse con los requirement levels utilizados por Repository Templates.

Por tanto:

```text
Component dependency
≠
Template requirement level
```

Los tipos de dependencia podrán formalizarse en el futuro si aparece una necesidad real de distinguir diferentes contratos entre Components.

---

# 14. Component Consumers

Un Framework Component podrá utilizarse, según su responsabilidad, por diferentes consumidores:

- README;
- documentación;
- repositorios;
- GitHub Profile;
- GitHub Pages;
- automatizaciones;
- Repository Templates;
- futuras herramientas del Framework.

No todos los Components serán aplicables a todos los consumidores.

---

# 15. Component Reuse

Un mismo Framework Component podrá utilizarse en múltiples Repository Templates y Repository Implementations.

Ejemplo:

```text
README-QUICK-START
        ↓
Multiple Repository Templates
        ↓
Multiple Repository Implementations
```

El Component mantiene una única responsabilidad canónica aunque disponga de múltiples consumidores.

---

# 16. Component Ownership

Los Framework Components deberán mantenerse bajo una responsabilidad de mantenimiento identificable a nivel de proyecto o gobernanza.

La asignación de ownership individual por Component podrá incorporarse cuando el modelo colaborativo del Framework lo requiera.

El catálogo no deberá duplicar información de ownership si existe una fuente canónica específica para ella.

---

# 17. Component Lifecycle

Los Framework Components podrán evolucionar mediante un lifecycle como:

```text
Need
        ↓
Specification
        ↓
Implementation
        ↓
Validation
        ↓
Adoption
        ↓
Maintenance
        ↓
Deprecation / Retirement
```

El Component Catalog podrá registrar tanto elementos implementados como responsabilidades conceptuales reconocidas por el RDS, siempre que su estado quede claramente identificado.

La presencia en el catálogo no deberá interpretarse automáticamente como existencia de una implementación canónica.

---

# 18. Implementation Classification

El catálogo podrá distinguir el grado de materialización de un elemento.

Entre las clasificaciones actualmente relevantes se encuentran:

| Classification | Meaning |
|---|---|
| Implemented | Existe una implementación canónica dentro del Framework |
| Conceptual | Responsabilidad reconocida pero todavía no implementada canónicamente |

Esta clasificación es independiente de:

- status;
- priority;
- maturity;
- requirement level.

Por tanto:

```text
Implementation classification
≠
Lifecycle status
≠
Template requirement level
```

---

# 19. Registry Attributes

Además de la metadata canónica, el catálogo podrá exponer información derivada o de descubrimiento como:

- implementación disponible;
- consumidores conocidos;
- Repository Templates relacionados;
- ubicación canónica;
- fecha de última revisión;
- relaciones relevantes.

Los atributos derivados no deberán convertirse en una segunda definición del Component.

---

# 20. Audience Classification

Cada componente indicará su audiencia principal.

| Audience    | Purpose            |
| ----------- | ------------------ |
| Recruiter   | Perfil profesional |
| Developer   | Ingeniería         |
| Contributor | Colaboración       |
| Maintainer  | Mantenimiento      |
| All         | Uso general        |

Esta clasificación facilitará la composición automática de README y plantillas.

La audiencia constituye metadata descriptiva.

No determina por sí misma la inclusión del Component en un Repository Template.

---

# 21. Component Priority

La metadata de un Framework Component podrá expresar una prioridad orientativa dentro de su familia.

Los valores actualmente utilizados incluyen:

| Priority | Meaning |
|---|---|
| Required | Responsabilidad de alta relevancia dentro de su ámbito |
| Recommended | Responsabilidad habitualmente útil |
| Optional | Responsabilidad especializada o contextual |

Esta prioridad describe el Component de forma general.

No determina si debe utilizarse en un repositorio concreto.

La obligatoriedad contextual pertenece exclusivamente al Repository Template mediante sus requirement levels:

```text
Component priority
≠
Template requirement level
```

Un Component con `priority: Required` podrá no ser necesario para determinados tipos de proyecto.

---

# 22. Maturity Mapping

La metadata de un Framework Component podrá indicar el nivel mínimo de madurez recomendado para utilizarlo o mantenerlo adecuadamente.

| Level | Description |
|---|---|
| L1 | Experimental |
| L2 | Public Basic |
| L3 | Supporting |
| L4 | Strategic |

Este valor no determina el tipo de proyecto ni el requirement level del Component.

Representa una expectativa orientativa de madurez.

---

# 23. Registry Navigation

El catálogo deberá permitir localizar elementos mediante:

- identificador;
- familia;
- status;
- audience;
- priority;
- maturity;
- implementation classification;
- Repository Template relacionado;
- ubicación canónica.

---

# 24. Registry Principles

El catálogo seguirá estos principios:

- descubrimiento centralizado;
- nomenclatura estable;
- ausencia de duplicados conceptuales;
- referencias hacia fuentes canónicas;
- clasificación explícita;
- evolución controlada;
- sincronización con la implementación.

---

# 25. Anti-Patterns

No deberán aparecer:

- identificadores repetidos;
- familias ambiguas;
- Components con responsabilidades duplicadas;
- dependencias ocultas;
- elementos presentados como implementados sin implementación canónica;
- requirement levels globales definidos por el catálogo;
- clasificaciones paralelas a las fuentes canónicas;
- metadata duplicada con valores contradictorios;
- Repository Profiles tratados como Components;
- Maturity Profiles tratados como Repository Templates.

---

# 26. Quality Gates

Antes de registrar o actualizar un elemento deberán verificarse:

- [ ] El identificador es único cuando corresponda.
- [ ] La naturaleza o familia está correctamente identificada.
- [ ] Existe una responsabilidad diferenciada.
- [ ] La fuente canónica está identificada cuando existe.
- [ ] El status está correctamente representado.
- [ ] La clasificación de implementación es correcta.
- [ ] Las dependencias reales están documentadas.
- [ ] La metadata mostrada coincide con la fuente canónica.
- [ ] No se introduce un requirement level global.
- [ ] No se duplica una responsabilidad existente.

---

# 27. Long-Term Vision

El Component Catalog deberá convertirse en una interfaz de descubrimiento del ecosistema GitHub Framework.

Permitirá localizar responsabilidades reutilizables, comprender su estado y acceder a sus fuentes canónicas.

Con el tiempo podrá alimentar:

- buscadores de Components;
- Repository Wizards;
- validadores;
- generadores;
- análisis de dependencias;
- herramientas de gobernanza.

La automatización deberá consumir las fuentes canónicas y utilizar el catálogo como índice, no como definición paralela.

---

# 28. Part 1 Conclusions

El **Component Catalog** proporciona una vista centralizada de los elementos reutilizables reconocidos por GitHub Framework.

Su responsabilidad principal es facilitar descubrimiento, clasificación y trazabilidad.

Las especificaciones y metadata mantienen las definiciones canónicas cuando existen.

Los Repository Templates determinan contextualmente la composición de Components, mientras que los Maturity Profiles constituyen una dimensión independiente.

Por tanto:

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

El catálogo deberá mantenerse sincronizado con la evolución real del Framework sin convertirse en una segunda fuente de verdad.

---

# 29. Part 1 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Component Catalog.

---

# 09 - COMPONENT CATALOG

# Part 2/4

# README & Documentation Components Registry

---

# 30. Purpose

Esta sección proporciona la vista de catálogo de las familias:

- README Components (`README-*`);
- Documentation Components (`DOC-*`).

Su objetivo es facilitar el descubrimiento, clasificación y trazabilidad de los Components relacionados con README y documentación.

Las especificaciones y metadata correspondientes constituyen sus fuentes canónicas cuando existe implementación.

Esta sección no determina qué Components son obligatorios para cada tipo de proyecto.

Esa responsabilidad corresponde a los Repository Templates.

---

# 31. README Component Family

## Prefix

```text id="cc010"
README
```

---

## Purpose

Construir README modulares, reutilizables y consistentes.

---

## Consumer

* GitHub Repository
* GitHub Profile
* GitHub Pages
* Documentation Landing Pages

---

## Relationships

Los README Components podrán relacionarse con Components de otras familias cuando exista una responsabilidad compartida o complementaria.

Entre las relaciones habituales podrán encontrarse:

- Documentation Components (`DOC-*`);
- Visual Components (`VCL-*`).

Las dependencias reales deberán declararse individualmente en la definición canónica de cada Component.

La pertenencia a la familia README no implica automáticamente una dependencia con otra familia.

---

# 32. README Component Registry

| ID                          | Name                 | Priority    | Audience    | Maturity | Implementation |
| --------------------------- | -------------------- | ----------- | ----------- | -------- | -------------- |
| README-HERO                 | Hero Section         | Required    | All         | L1       | Implemented    |
| README-STATUS               | Project Status       | Required    | All         | L2       | Implemented    |
| README-OVERVIEW             | Project Overview     | Required    | All         | L1       | Implemented    |
| README-HIGHLIGHTS           | Highlights           | Recommended | Recruiter   | L2       | Conceptual     |
| README-FEATURES             | Features             | Required    | All         | L2       | Implemented    |
| README-ARCHITECTURE         | Architecture         | Recommended | Developer   | L3       | Implemented    |
| README-TECH-STACK           | Tech Stack           | Required    | All         | L2       | Implemented    |
| README-REPOSITORY-STRUCTURE | Repository Structure | Recommended | Developer   | L3       | Conceptual     |
| README-QUICK-START          | Quick Start          | Required    | Developer   | L2       | Implemented    |
| README-DOCUMENTATION        | Documentation        | Required    | Developer   | L2       | Implemented    |
| README-DEMO                 | Demo                 | Optional    | Recruiter   | L2       | Conceptual     |
| README-TESTING              | Testing              | Recommended | Developer   | L3       | Implemented    |
| README-ROADMAP              | Roadmap              | Recommended | Maintainer  | L3       | Implemented    |
| README-CONTRIBUTING         | Contributing         | Optional    | Contributor | L3       | Conceptual     |
| README-LICENSE              | License              | Required    | All         | L2       | Conceptual     |
| README-AUTHOR               | Author               | Recommended | Recruiter   | L2       | Implemented    |
| README-FOOTER               | Footer               | Required    | All         | L1       | Implemented    |

Los valores de `Priority` representan metadata orientativa del Component conforme a §21.

No constituyen requirement levels globales.

La selección efectiva para cada tipo de proyecto corresponde a los Repository Templates.

---

# 33. README Implementation Status

La familia README contiene actualmente Components implementados y responsabilidades conceptuales reconocidas por el Framework.

```text
README Components
        │
        ├── 12 Implemented
        └── 5 Conceptual
                ├── README-HIGHLIGHTS
                ├── README-REPOSITORY-STRUCTURE
                ├── README-DEMO
                ├── README-CONTRIBUTING
                └── README-LICENSE
```

La clasificación `Implemented` indica que existe una implementación canónica dentro de `framework/components/readme/`.

Los Components clasificados como `Conceptual` representan responsabilidades reconocidas que todavía no disponen de implementación canónica materializada.

La presencia de un Component en el catálogo no implica por sí misma disponibilidad material ni obligatoriedad dentro de un Repository Template.

---

# 34. README Selection Model

Los README Components no se agrupan globalmente como Core, Extended u Optional.

Su necesidad depende del tipo de proyecto y del Repository Template correspondiente.

```text
README Component
        ↓
Repository Template
        ↓
required / recommended / optional
        ↓
Repository Implementation
```

Por tanto, un mismo README Component podrá tener diferentes requirement levels según el Template consumidor.

---

# 35. README Catalog Responsibility

El catálogo describe qué README Components reconoce el Framework y facilita su descubrimiento.

No determina una composición universal de README.

La composición efectiva deberá derivarse de:

- Repository Template;
- necesidades reales del proyecto;
- madurez esperada;
- personalización justificada del consumidor.

Las decisiones contextuales no deberán convertirse en nuevas clasificaciones globales dentro del catálogo.

---

# 36. README Relationships

Los README Components pueden mantener relaciones de composición o complementariedad sin constituir una jerarquía obligatoria.

Ejemplo:

```text
README-HERO
        │
        └── may use → VCL-HERO

README-ARCHITECTURE
        │
        └── may reference → DOC-ARCHITECTURE

README-DOCUMENTATION
        │
        └── may expose → Documentation Components
```

Estas relaciones son contextuales.

Las dependencias funcionales reales deberán declararse en la definición canónica de cada Component.

---

# 37. Documentation Component Family

## Prefix

```text
DOC
```

---

## Purpose

Construir sistemas documentales completos.

---

## Consumer

* Documentation
* MkDocs
* GitHub Wiki
* GitHub Pages

---

## Relationships

Los Documentation Components podrán relacionarse entre sí y con otras familias cuando exista una necesidad documental real.

Estas relaciones no constituyen una jerarquía global.

Las dependencias deberán declararse individualmente en las fuentes canónicas correspondientes.

---

# 38. Documentation Component Registry

| ID                 | Name                         | Priority    | Audience   | Maturity | Implementation |
| ------------------ | ---------------------------- | ----------- | ---------- | -------- | -------------- |
| DOC-ARCHITECTURE   | Architecture                 | Required    | Developer  | L3       | Implemented    |
| DOC-ADR            | Architecture Decision Record | Recommended | Developer  | L3       | Conceptual     |
| DOC-ROADMAP        | Roadmap                      | Recommended | Maintainer | L3       | Conceptual     |
| DOC-PROJECT-STATUS | Project Status               | Required    | Maintainer | L2       | Implemented    |
| DOC-KNOWN-ISSUES   | Known Issues                 | Recommended | Maintainer | L3       | Conceptual     |
| DOC-CHANGELOG      | Changelog                    | Required    | All        | L2       | Implemented    |
| DOC-RELEASE-NOTES  | Release Notes                | Recommended | All        | L3       | Conceptual     |
| DOC-API            | API Documentation            | Optional    | Developer  | L3       | Conceptual     |
| DOC-DATABASE       | Database Documentation       | Optional    | Developer  | L3       | Conceptual     |
| DOC-DEPLOYMENT     | Deployment Guide             | Optional    | Developer  | L3       | Conceptual     |
| DOC-TESTING        | Testing Strategy             | Recommended | Developer  | L3       | Conceptual     |
| DOC-SECURITY       | Security                     | Recommended | Developer  | L3       | Conceptual     |
| DOC-DIAGRAMS       | Diagrams                     | Recommended | Developer  | L3       | Conceptual     |
| DOC-GLOSSARY       | Glossary                     | Optional    | All        | L4       | Conceptual     |
| DOC-REFERENCES     | References                   | Recommended | All        | L2       | Implemented    |

Los Components clasificados como `Conceptual` representan responsabilidades reconocidas por el RDS que todavía no disponen de implementación canónica.

Su presencia en el catálogo no deberá interpretarse como disponibilidad material dentro de `framework/components/documentation/`.

---

# 39. Documentation Implementation Status

La familia Documentation contiene actualmente Components implementados y responsabilidades conceptuales reconocidas por el Framework.

```text
Documentation Components
        │
        ├── 4 Implemented
        │       ├── DOC-ARCHITECTURE
        │       ├── DOC-PROJECT-STATUS
        │       ├── DOC-CHANGELOG
        │       └── DOC-REFERENCES
        │
        └── 11 Conceptual
                ├── DOC-ADR
                ├── DOC-ROADMAP
                ├── DOC-KNOWN-ISSUES
                ├── DOC-RELEASE-NOTES
                ├── DOC-API
                ├── DOC-DATABASE
                ├── DOC-DEPLOYMENT
                ├── DOC-TESTING
                ├── DOC-SECURITY
                ├── DOC-DIAGRAMS
                └── DOC-GLOSSARY
```

Los Components conceptuales representan responsabilidades reconocidas que todavía no disponen de implementación canónica dentro de `framework/components/documentation/`.

Podrán evolucionar hacia `Implemented` cuando exista una necesidad validada y dispongan de una definición materializada y gobernada conforme al modelo del Framework.

---

# 40. Documentation Selection Model

Los Documentation Components no se clasifican globalmente como Core, Extended o Specialized.

Su aplicabilidad depende del Repository Template y de las características reales del proyecto.

Ejemplos:

```text
Backend
        → may require DOC-API

Documentation
        → may recommend DOC-GLOSSARY

Project without database
        → DOC-DATABASE not applicable
```

La selección contextual deberá expresarse mediante los requirement levels del Repository Template.

---

# 41. Conceptual Documentation Components

El catálogo puede registrar responsabilidades documentales conceptuales antes de que exista implementación canónica.

Actualmente:

```text
DOC-ADR
DOC-ROADMAP
DOC-KNOWN-ISSUES
DOC-RELEASE-NOTES
DOC-API
DOC-DATABASE
DOC-DEPLOYMENT
DOC-TESTING
DOC-SECURITY
DOC-DIAGRAMS
DOC-GLOSSARY
```

Estos elementos permiten preservar responsabilidades reconocidas por la arquitectura sin crear archivos vacíos o implementaciones prematuras.

Para evolucionar a `Implemented` deberán disponer de:

- especificación canónica;
- metadata;
- estructura material dentro del Framework;
- validación suficiente para su reutilización.

---

# 42. Documentation Relationships

Los Documentation Components podrán relacionarse según las necesidades del sistema documental.

Ejemplos:

```text
DOC-ARCHITECTURE
        └── may be complemented by → DOC-ADR

DOC-ARCHITECTURE
        └── may use → DOC-DIAGRAMS

DOC-API
        └── may reference → DOC-SECURITY

DOC-REFERENCES
        └── may support → multiple Documentation Components
```

Estas relaciones no representan una secuencia obligatoria.

Las dependencias reales deberán mantenerse en las fuentes canónicas correspondientes.

---

# 43. Repository Template Mapping

La aplicabilidad de README y Documentation Components a cada tipo de proyecto se define mediante Repository Templates.

Ejemplos de tipos actualmente contemplados:

```text
Backend
Full Stack
AI
Documentation
Library
Website
```

El Component Catalog podrá mostrar estas relaciones con fines de descubrimiento, pero no deberá mantener una segunda matriz normativa de selección.

La fuente aplicable para `required`, `recommended` y `optional` será el Repository Template correspondiente.

---

# 44. Cross-Consumer Reuse

Los README y Documentation Components podrán reutilizarse por diferentes consumidores cuando sus responsabilidades sean aplicables.

Ejemplos:

| Component | Primary Consumer | Possible Additional Consumers |
|---|---|---|
| README-HERO | Repository README | GitHub Profile |
| README-TECH-STACK | Repository README | GitHub Profile |
| README-ROADMAP | Repository README | Documentation landing page |
| DOC-ARCHITECTURE | Documentation | Repository Template |
| DOC-ADR | Documentation | Repository Template |
| DOC-CHANGELOG | Documentation | Release workflows |
| DOC-DIAGRAMS | Documentation | README |

Esta tabla representa posibilidades de reutilización y no requirement levels.

---

# 45. Family Lifecycle

Los README y Documentation Components siguen el lifecycle general definido en §17.

Su estado concreto deberá obtenerse de la fuente canónica correspondiente.

La clasificación `Implemented` o `Conceptual` es independiente del lifecycle status.

---

# 46. Registry Evolution Rules

Un nuevo README o Documentation Component solo deberá incorporarse cuando:

- no exista una responsabilidad equivalente;
- aporte una responsabilidad reutilizable diferenciada;
- exista un caso de uso suficientemente claro;
- pueda definirse sin acoplarse a un único proyecto;
- sea coherente con el RDS;
- su estado de implementación pueda representarse explícitamente.

La creación de un Component conceptual no obliga a implementar inmediatamente su representación material.

---

# 47. Anti-Patterns

No deberán existir:

- dos Components para la misma responsabilidad;
- README que replique documentación extensa sin necesidad;
- documentos técnicos duplicados;
- dependencias circulares entre Components;
- jerarquías artificiales presentadas como dependencias;
- clasificaciones globales Core / Extended / Optional;
- Components conceptuales presentados como implementados;
- selección por tipo de proyecto duplicada respecto a Repository Templates.

---

# 48. Quality Gates

Antes de registrar o actualizar un README o Documentation Component deberán verificarse:

- [ ] Identificador único.
- [ ] Nombre consistente.
- [ ] Responsabilidad diferenciada.
- [ ] Priority coherente con la metadata cuando exista.
- [ ] Audience definida.
- [ ] Maturity mínima recomendada.
- [ ] Implementation classification correcta.
- [ ] Dependencias reales documentadas.
- [ ] Fuente canónica identificada cuando exista.
- [ ] Ausencia de requirement levels globales.
- [ ] Coherencia con los Repository Templates.

---

# 49. Long-Term Vision

Las familias README y Documentation constituirán la base documental reutilizable del GitHub Framework.

Los proyectos del ecosistema podrán seleccionar los Components adecuados a su tipo, contexto y madurez mediante Repository Templates.

La existencia de un vocabulario común permitirá mantener consistencia sin imponer una composición documental idéntica.

Con el tiempo, las fuentes canónicas y los Repository Templates podrán alimentar mecanismos automáticos de generación, validación y actualización documental.

---

# 50. Part 2 Conclusions

Las familias **README** y **Documentation** proporcionan responsabilidades documentales reutilizables y gobernadas.

El Component Catalog permite descubrir estas capacidades y distinguir claramente entre Components implementados y conceptuales.

La selección concreta no corresponde al catálogo:

```text
Component Catalog
        ↓
Discover available responsibilities

Repository Template
        ↓
Assign contextual requirement levels

Repository Implementation
        ↓
Materialize selected Components
```

Este modelo permite mantener consistencia documental sin convertir el catálogo en una composición universal para todos los repositorios.

---

# 51. Part 2 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Component Catalog.

---

# 09 - COMPONENT CATALOG

# Part 3/4

# Workflow & Visual Components Registry

---

# 52. Purpose

Esta sección proporciona la vista de catálogo de las familias:

- Workflow Components (`WCL-*`);
- Visual Components (`VCL-*`).

Su objetivo es facilitar el descubrimiento, clasificación y evolución de responsabilidades operativas y visuales reconocidas por GitHub Framework.

La presencia de una responsabilidad en esta sección no implica necesariamente que disponga de implementación canónica.

Su grado de materialización deberá expresarse mediante la clasificación `Implemented` o `Conceptual`.

---

# 53. Workflow Component Family

## Prefix

```text
WCL
```

---

## Purpose

Definir procesos reutilizables para el desarrollo, revisión, publicación y mantenimiento de repositorios.

---

## Consumer

* GitHub
* GitHub Actions
* Project Boards
* Pull Requests
* Releases

---

## Relationships

Los Workflow Components podrán relacionarse con otras familias cuando sus procesos consuman o afecten responsabilidades documentales, visuales o de repositorio.

Estas relaciones podrán incluir, según el Component:

- README Components (`README-*`);
- Documentation Components (`DOC-*`);
- Visual Components (`VCL-*`).

La pertenencia a la familia Workflow no implica automáticamente estas dependencias.

Las dependencias reales deberán declararse individualmente en las fuentes canónicas correspondientes.

---

# 54. Workflow Component Registry

| ID                       | Name                   | Priority    | Audience   | Maturity | Implementation |
| ------------------------ | ---------------------- | ----------- | ---------- | -------- | -------------- |
| WCL-ISSUE                | Issue Template         | Required    | Maintainer | L2       | Conceptual     |
| WCL-LABEL                | Labels                 | Required    | Maintainer | L2       | Conceptual     |
| WCL-PROJECT              | Project Board          | Recommended | Maintainer | L3       | Conceptual     |
| WCL-BRANCH               | Branch Strategy        | Required    | Developer  | L2       | Conceptual     |
| WCL-COMMIT               | Commit Convention      | Required    | Developer  | L2       | Conceptual     |
| WCL-PULL-REQUEST         | Pull Request           | Required    | Developer  | L2       | Conceptual     |
| WCL-CODE-REVIEW          | Code Review            | Recommended | Developer  | L3       | Conceptual     |
| WCL-CI                   | Continuous Integration | Recommended | Developer  | L3       | Conceptual     |
| WCL-CD                   | Continuous Delivery    | Optional    | Maintainer | L4       | Conceptual     |
| WCL-DEPENDABOT           | Dependency Updates     | Recommended | Maintainer | L3       | Conceptual     |
| WCL-SECURITY             | Security Workflow      | Recommended | Developer  | L3       | Conceptual     |
| WCL-RELEASE              | Release Workflow       | Recommended | Maintainer | L3       | Conceptual     |
| WCL-HOTFIX               | Hotfix Workflow        | Optional    | Developer  | L3       | Conceptual     |
| WCL-DOCUMENTATION-UPDATE | Documentation Sync     | Recommended | Maintainer | L3       | Conceptual     |
| WCL-ASSESSMENT           | GRS Assessment         | Required    | Maintainer | L4       | Conceptual     |
| WCL-MAINTENANCE          | Maintenance Cycle      | Recommended | Maintainer | L3       | Conceptual     |

Los Workflow Components se encuentran actualmente reconocidos como responsabilidades conceptuales del Framework.

La utilización real de Issues, Pull Requests, Releases u otras capacidades en el propio repositorio no constituye por sí misma una implementación canónica del Component correspondiente.

Para evolucionar a `Implemented` deberá existir una definición materializada y gobernada conforme al modelo del Framework.

---

# 55. Workflow Implementation Status

La familia Workflow se encuentra actualmente en fase conceptual.

```text
Workflow Components
        │
        ├── 0 Implemented
        └── 16 Conceptual
```

Estos Components representan responsabilidades operativas reconocidas que podrán materializarse progresivamente conforme avance el Framework.

---

# 56. Workflow Selection Model

Los Workflow Components no se clasifican globalmente como Core, Extended o Specialized.

Su necesidad dependerá del Repository Template, del contexto del proyecto y de las capacidades operativas requeridas.

```text
Workflow Component
        ↓
Repository Template
        ↓
required / recommended / optional
        ↓
Repository Implementation
```

La prioridad del Component no sustituye este requirement level contextual.

---

# 57. Workflow Materialization

Un Workflow Component podrá evolucionar de `Conceptual` a `Implemented` cuando exista una representación canónica reutilizable y gobernada.

Según su naturaleza, dicha materialización podrá incluir:

- especificaciones;
- configuraciones;
- GitHub community files;
- GitHub Actions workflows;
- convenciones formalizadas;
- automatizaciones;
- metadata.

La forma material concreta dependerá de la responsabilidad del Component y no deberá forzarse a una estructura uniforme.

---

# 58. Workflow Relationships

Los Workflow Components podrán participar en secuencias operativas sin que ello implique dependencia estructural entre ellos.

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

Este flujo representa una posible interacción operativa.

No constituye una cadena obligatoria de dependencias.

Las dependencias funcionales reales deberán declararse individualmente.

---

# 59. Workflow Capability Mapping

| Component        | Primary Capability        |
| ---------------- | ------------------------- |
| WCL-BRANCH       | Git Strategy              |
| WCL-COMMIT       | Version Control           |
| WCL-PULL-REQUEST | Collaborative Development |
| WCL-CODE-REVIEW  | Code Quality              |
| WCL-CI           | Continuous Integration    |
| WCL-CD           | DevOps                    |
| WCL-SECURITY     | Secure Development        |
| WCL-RELEASE      | Release Management        |
| WCL-ASSESSMENT   | Engineering Governance    |

El capability mapping describe la responsabilidad principal de cada Component y no determina su requirement level ni su estado de implementación.

---

# 60. Visual Component Family

## Prefix

```text
VCL
```

---

## Purpose

Definir responsabilidades visuales reutilizables para presentación, navegación, comunicación y visualización técnica cuando resulten aplicables.

La familia Visual proporciona un vocabulario común sin imponer una identidad gráfica idéntica a todos los consumidores.

---

## Consumer

* README
* GitHub Profile
* GitHub Pages
* Portfolio

---

## Relationships

Los Visual Components podrán complementar Components de otras familias, especialmente README y Documentation.

Estas relaciones representan capacidades de presentación y comunicación visual.

No implican automáticamente dependencias funcionales.

Las dependencias reales deberán declararse individualmente cuando existan.

---

# 61. Visual Component Registry

| ID                       | Name                 | Priority    | Audience  | Maturity | Implementation |
| ------------------------ | -------------------- | ----------- | --------- | -------- | -------------- |
| VCL-BANNER               | Repository Banner    | Recommended | Recruiter | L3       | Conceptual     |
| VCL-SOCIAL-PREVIEW       | Social Preview       | Recommended | Recruiter | L3       | Conceptual     |
| VCL-HERO                 | Hero Layout          | Required    | All       | L2       | Conceptual     |
| VCL-BADGES               | Badge Group          | Required    | All       | L2       | Conceptual     |
| VCL-SKILL-ICONS          | Skill Icons          | Required    | Recruiter | L2       | Conceptual     |
| VCL-PROJECT-CARD         | Project Card         | Recommended | Recruiter | L3       | Conceptual     |
| VCL-STATS                | GitHub Stats         | Optional    | Recruiter | L2       | Conceptual     |
| VCL-CONTRIBUTION-GRAPH   | Contribution Graph   | Optional    | Recruiter | L2       | Conceptual     |
| VCL-TYPING-BANNER        | Typing Animation     | Optional    | Recruiter | L2       | Conceptual     |
| VCL-ARCHITECTURE-DIAGRAM | Architecture Diagram | Recommended | Developer | L3       | Conceptual     |
| VCL-WORKFLOW-DIAGRAM     | Workflow Diagram     | Recommended | Developer | L3       | Conceptual     |
| VCL-FOLDER-DIAGRAM       | Repository Tree      | Recommended | Developer | L2       | Conceptual     |
| VCL-NAVIGATION-CARD      | Navigation Card      | Recommended | All       | L3       | Conceptual     |
| VCL-CALL-OUT             | GitHub Callouts      | Required    | All       | L2       | Conceptual     |

Los Visual Components se encuentran actualmente reconocidos como responsabilidades conceptuales.

La existencia de elementos visuales similares en repositorios o perfiles no implica que exista todavía una implementación canónica gobernada por GitHub Framework.

---

# 62. Visual Implementation Status

La familia Visual se encuentra actualmente en fase conceptual.

```text
Visual Components
        │
        ├── 0 Implemented
        └── 14 Conceptual
```

Su futura implementación deberá priorizar responsabilidades visuales reutilizables y evitar convertir decisiones puramente decorativas en Components del Framework.

---

# 63. Visual Selection Model

Los Visual Components no se clasifican globalmente como Core, Extended u Optional.

Su utilización dependerá del consumidor, del Repository Template y de las necesidades reales de comunicación visual.

Un mismo Component podrá ser relevante para un GitHub Profile y no aplicable a un repositorio técnico, o viceversa.

La selección deberá mantenerse contextual.

---

# 64. Visual Materialization

Un Visual Component podrá evolucionar a `Implemented` cuando disponga de una representación canónica reutilizable.

Según su naturaleza, podrá materializarse mediante:

- assets;
- layouts;
- snippets;
- convenciones visuales;
- configuraciones;
- templates;
- metadata.

La implementación deberá priorizar consistencia y reutilización sobre decoración.

---

# 65. Visual Relationships

Los Visual Components podrán combinarse para construir experiencias visuales coherentes.

Ejemplo:

```text
VCL-BANNER
        ↔
VCL-HERO
        ↔
VCL-BADGES
```

Estas relaciones representan complementariedad y no una jerarquía obligatoria.

Cada Component deberá conservar una responsabilidad independiente y reutilizable.

---

# 66. Visual Capability Mapping

| Component                | Primary Capability       |
| ------------------------ | ------------------------ |
| VCL-BANNER               | Brand Identity           |
| VCL-HERO                 | Information Architecture |
| VCL-BADGES               | Project Status           |
| VCL-SKILL-ICONS          | Technology Communication |
| VCL-PROJECT-CARD         | Portfolio Presentation   |
| VCL-ARCHITECTURE-DIAGRAM | Software Architecture    |
| VCL-WORKFLOW-DIAGRAM     | Process Design           |

El capability mapping facilita descubrimiento y clasificación.

No representa dependencias ni requirement levels.

---

# 67. Cross-Family Relationships

Los Framework Components podrán relacionarse entre familias cuando sus responsabilidades sean complementarias.

Ejemplos conceptuales:

```text
README-HERO
        ↔
VCL-HERO

README-ARCHITECTURE
        ↔
DOC-ARCHITECTURE
        ↔
VCL-ARCHITECTURE-DIAGRAM

README-DOCUMENTATION
        ↔
Documentation Components
```

Estas relaciones facilitan composición y descubrimiento.

No deberán interpretarse automáticamente como dependencias funcionales.

---

# 68. Cross-Consumer Reuse

Workflow y Visual Components podrán tener diferentes consumidores según su responsabilidad.

| Family | Primary Context | Possible Consumers |
|---|---|---|
| WCL | Repository operations | GitHub, automation, Repository Templates |
| VCL | Visual communication | README, Documentation, GitHub Profile, GitHub Pages |

Esta clasificación representa posibilidades de reutilización y no obligatoriedad.

---

# 69. Registry Evolution Rules

Los Workflow y Visual Components solo deberán ampliarse cuando:

- exista una necesidad recurrente;
- la responsabilidad sea reutilizable;
- no exista un Component equivalente;
- no se incremente innecesariamente la complejidad;
- exista coherencia con el RDS;
- pueda identificarse claramente su estado de implementación.

La incorporación conceptual no obliga a una implementación inmediata.

---

# 70. Anti-Patterns

No deberán registrarse:

- workflows específicos de un único proyecto;
- elementos visuales puramente decorativos sin responsabilidad reutilizable;
- automatizaciones sin estrategia de mantenimiento;
- variantes mínimas del mismo Component;
- jerarquías artificiales presentadas como dependencias;
- clasificaciones globales Core / Extended / Optional;
- Components conceptuales presentados como implementados;
- uso real de una capacidad confundido con implementación canónica.

---

# 71. Quality Gates

Antes de registrar o actualizar un Workflow o Visual Component deberán verificarse:

- [ ] Identificador único.
- [ ] Responsabilidad diferenciada.
- [ ] Audience identificada.
- [ ] Priority coherente.
- [ ] Maturity mínima recomendada.
- [ ] Implementation classification correcta.
- [ ] Relaciones reales documentadas.
- [ ] Fuente canónica identificada cuando exista.
- [ ] Ausencia de requirement levels globales.
- [ ] Coherencia con el RDS.

---

# 72. Long-Term Vision

Las familias Workflow y Visual proporcionarán capacidades reutilizables para la operación y presentación de repositorios.

Su evolución permitirá compartir patrones de trabajo y comunicación visual sin imponer procesos o diseños idénticos a todos los proyectos.

Conforme estas familias se materialicen, podrán alimentar Repository Templates, automatizaciones y herramientas futuras del Framework.

---

# 73. Part 3 Conclusions

Las familias **Workflow** y **Visual** representan responsabilidades operativas y visuales reconocidas por GitHub Framework.

Actualmente constituyen principalmente un catálogo conceptual que orienta futuras implementaciones.

Su evolución deberá seguir el mismo principio que el resto del sistema:

```text
Recognized responsibility
        ↓
Canonical definition
        ↓
Implementation
        ↓
Validation
        ↓
Reusable adoption
```

El catálogo permite preservar estas responsabilidades sin presentar prematuramente como implementado aquello que todavía pertenece al diseño.

---

# 74. Part 3 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Component Catalog.

---

# 09 - COMPONENT CATALOG

# Part 4/4

# Repository Templates & Framework Governance

---

# 75. Purpose

Esta sección completa el **Component Catalog** incorporando el registro de Repository Templates (`TPL-*`) y las reglas globales de trazabilidad y gobernanza del catálogo.

Los Repository Templates no constituyen una familia de Framework Components.

Representan composiciones reutilizables de Components adaptadas a tipos concretos de proyecto.

Los Maturity Profiles constituyen una dimensión independiente del modelo y no se registran como Templates ni como Components.

Esta sección deberá mantenerse alineada con:

- Repository Design System;
- especificaciones y metadata canónicas;
- Repository Template Library;
- implementación real del Framework.

---

# 76. Repository Template Registry

## Prefix

```text
TPL
```

---

## Purpose

Los Repository Templates representan composiciones reutilizables de Framework Components para tipos concretos de proyecto.

Un Template:

- define un project_type;
- declara una madurez mínima recomendada;
- selecciona Components existentes;
- asigna requirement levels contextuales;
- proporciona guidance específico de composición.

No introduce nuevas responsabilidades canónicas dentro de los Components.

---

## Consumer

- nuevos repositorios;
- Repository Implementations;
- futuras herramientas de bootstrap;
- futuros generadores o validadores.

La existencia futura de automatización no forma parte todavía del contrato obligatorio del Template.

---

# 77. Template Registry

Los Repository Templates implementados actualmente son:

| ID | Name | Project Type | Maturity | Status | Implementation |
|---|---|---|---|---|---|
| `TPL-BACKEND` | Backend Repository | Backend | L2 | Experimental | Implemented |
| `TPL-FULLSTACK` | Full Stack Repository | Full Stack | L2 | Experimental | Implemented |
| `TPL-DOCUMENTATION` | Documentation Repository | Documentation | L2 | Experimental | Implemented |

La implementación canónica se mantiene en:

```text
framework/templates/repositories/
```

Otros tipos de proyecto identificados como candidatos son:

| Project Type | Classification |
|---|---|
| AI | Potential |
| Library | Potential |
| Website | Potential |

Estos tipos no constituyen Repository Templates oficiales mientras no dispongan de:

- caso de uso real;
- especificación;
- composición;
- metadata;
- implementación;
- validación.

Por tanto, no se registran actualmente identificadores como `TPL-AI`, `TPL-LIBRARY` o `TPL-WEBSITE` como Templates implementados.

---

# 78. Maturity Profiles

GitHub Framework mantiene cuatro niveles de madurez:

| Level | Description |
|---|---|
| L1 | Experimental |
| L2 | Public Basic |
| L3 | Supporting |
| L4 | Strategic |

Los Maturity Profiles expresan expectativas de evolución, mantenimiento y exigencia.

No constituyen Repository Templates.

Por tanto, no existen:

```text
TPL-L1
TPL-L2
TPL-L3
TPL-L4
```

La madurez se registra como propiedad del Repository Template o del elemento correspondiente.

Ejemplo:

```text
TPL-DOCUMENTATION
maturity: L2
```

Dos Repository Templates con la misma madurez podrán utilizar composiciones diferentes.

---

# 79. Repository Context

Factores como:

- desarrollo individual;
- trabajo en equipo;
- open source;
- investigación;
- entorno empresarial;

pueden modificar necesidades operativas o de gobernanza de un repositorio.

Estos factores forman parte del contexto del consumidor.

No constituyen actualmente una familia formal de `Repository Profiles` dentro de GitHub Framework.

Cuando afecten a la composición, deberán resolverse mediante:

- configuración del consumidor;
- Components aplicables;
- guidance del Repository Template;
- futuras capacidades respaldadas por casos de uso reales.

---

# 80. Repository Profile Model

El modelo anterior basado en identificadores como:

```text
PROFILE-SOLO
PROFILE-TEAM
PROFILE-OPEN-SOURCE
PROFILE-RESEARCH
PROFILE-ENTERPRISE
```

no forma parte de la arquitectura actual del Framework.

La experiencia obtenida durante la implementación mostró que estos conceptos mezclaban contexto operativo con composición arquitectónica.

El modelo actual separa:

```text
Project Type
        ↓
Repository Template


Maturity
        ↓
Independent expectation


Repository Context
        ↓
Consumer-specific configuration
```

No se incorporará una nueva abstracción de Profile sin evidencia de una necesidad reutilizable que no pueda resolverse adecuadamente mediante el modelo existente.

---

# 81. Template Composition

Un Repository Template se define mediante:

```text
Repository Template
        ├── Project Type
        ├── Maturity
        ├── Required Components
        ├── Recommended Components
        ├── Optional Components
        └── Template-specific guidance
```

Ejemplo conceptual:

```text
TPL-BACKEND
        │
        ├── project_type: Backend
        ├── maturity: L2
        └── components
                ├── required
                ├── recommended
                └── optional
```

No se compone mediante otros Templates de madurez ni Repository Profiles.

El requirement level pertenece al contexto del Template y no modifica la metadata canónica del Component.

---

# 82. Framework Composition

La arquitectura general del Framework puede representarse como:

```text
Standards
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
Validation and Evolution
```

Los Maturity Profiles actúan como una dimensión independiente que modifica expectativas de calidad, mantenimiento y evolución.

No forman una capa adicional de Components ni Templates.

---

# 83. Framework Relationships

Las principales relaciones del sistema son:

```text
RDS
        ↓ defines architecture

Framework Components
        ↓ provide reusable responsibilities

Repository Templates
        ↓ compose Components

Repository Implementations
        ↓ consume Templates and Components

Reference Implementations
        ↓ validate the model
```

Las relaciones entre Components deberán declararse únicamente cuando exista dependencia funcional real.

El catálogo no mantendrá una jerarquía global artificial entre familias.

---

# 84. Framework Registry Summary

| Element | Prefix | Recognized | Implemented | Conceptual / Potential |
|---|---|---:|---:|---:|
| README Components | `README-*` | 17 | 12 | 5 |
| Documentation Components | `DOC-*` | 15 | 4 | 11 |
| Workflow Components | `WCL-*` | 16 | 0 | 16 |
| Visual Components | `VCL-*` | 14 | 0 | 14 |
| Repository Templates | `TPL-*` | 3 | 3 | 0 |

Los tipos potenciales de Repository Template se registran por separado y no se contabilizan como Templates registrados.

Los Maturity Profiles no se contabilizan como Components ni como Templates.

---

# 85. Registry Relationships

| Element | Main Relationship |
|---|---|
| README Components | Presentación y navegación |
| Documentation Components | Conocimiento técnico y operativo |
| Workflow Components | Procesos de desarrollo y mantenimiento |
| Visual Components | Comunicación y presentación visual |
| Repository Templates | Composición contextual de Components |
| Maturity Profiles | Expectativas independientes de evolución |

Estas relaciones describen responsabilidades dentro del Framework.

No representan dependencias técnicas universales entre familias.

---

# 86. Repository Selection Strategy

Al crear un repositorio que adopte GitHub Framework se seguirá conceptualmente:

```text
Identify Project Type
        ↓
Select Repository Template
        ↓
Review Template Maturity
        ↓
Apply Required Components
        ↓
Evaluate Recommended Components
        ↓
Add Optional Components when justified
        ↓
Configure Consumer-specific Needs
        ↓
Validate
        ↓
Publish
```

Cuando no exista un Repository Template adecuado deberá evaluarse si:

- puede utilizarse uno existente;
- la necesidad puede resolverse mediante configuración;
- existe suficiente evidencia para diseñar un nuevo Template.

No se crearán Templates únicamente para cubrir variaciones menores.

---

# 87. Framework Layers

GitHub Framework puede analizarse mediante diferentes capas de responsabilidad:

```text
Standards Layer
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

Estas capas representan responsabilidades arquitectónicas.

No implican una estructura física obligatoria del repositorio.

---

# 88. Element Traceability

Todo elemento registrado deberá permitir responder, cuando corresponda:

- ¿Cuál es su identificador?
- ¿Cuál es su responsabilidad?
- ¿Cuál es su fuente canónica?
- ¿Está implementado o es conceptual?
- ¿Cuál es su status?
- ¿Qué Repository Templates lo utilizan?
- ¿Qué relaciones o dependencias mantiene?
- ¿Cuál es su versión?
- ¿Cuál es su maturity?
- ¿Dónde está materializado?

La trazabilidad deberá derivarse de fuentes canónicas y datos de catálogo sincronizados.

---

# 89. Registry Fields

El catálogo podrá exponer dos tipos de información.

## Canonical Metadata

Cuando exista implementación:

| Field | Description |
|---|---|
| ID | Identificador |
| Name | Nombre |
| Family | Familia |
| Version | Semantic Version |
| Status | Estado |
| Priority | Prioridad orientativa |
| Audience | Audiencia |
| Maturity | Madurez mínima recomendada |
| Description | Descripción |
| Dependencies | Dependencias declaradas |

## Derived Catalog Information

El catálogo podrá añadir información derivada como:

- implementation classification;
- canonical location;
- Repository Templates relacionados;
- consumidores conocidos;
- última revisión.

La información derivada deberá mantenerse sincronizada con las fuentes canónicas y no sustituirlas.

---

# 90. Catalog Governance

Todo elemento reconocido por el Component Catalog deberá respetar la gobernanza definida por el RDS.

Para incorporar un nuevo Framework Component deberá:

- existir una responsabilidad reutilizable diferenciada;
- disponer de identificador estable cuando corresponda;
- estar documentado;
- declarar correctamente su estado de implementación;
- evitar duplicar responsabilidades existentes;
- mantener coherencia con las fuentes canónicas.

La incorporación al catálogo proporciona descubrimiento y trazabilidad.

No sustituye la especificación, metadata, implementación ni validación necesarias para considerar un elemento materializado.

---

# 91. Repository Bootstrap Process

El bootstrap conceptual de un repositorio será:

```text
Framework
        ↓
Identify Project Type
        ↓
Repository Template
        ↓
Required / Recommended / Optional Components
        ↓
Repository Implementation
        ↓
Validation
```

La madurez se evalúa dentro de este proceso como expectativa independiente.

No se selecciona un Repository Profile ni un Maturity Template adicional.

---

# 92. Evolution Strategy

La evolución de los elementos reutilizables seguirá conceptualmente:

```text
Need
        ↓
Evaluate Existing Model
        ↓
Specification
        ↓
Implementation
        ↓
Catalog Synchronization
        ↓
Validation
        ↓
Adoption
        ↓
Maintenance
```

La incorporación al catálogo no precede necesariamente a toda implementación.

Los elementos conceptuales podrán registrarse cuando resulte útil para representar responsabilidades reconocidas, siempre que su clasificación sea explícita.

---

# 93. Anti-Patterns

No deberán existir:

- Repository Profiles presentados como familia activa del Framework;
- Maturity Profiles modelados como Repository Templates;
- Templates potenciales presentados como implementados;
- Components conceptuales presentados como materializados;
- requirement levels globales mantenidos por el catálogo;
- dependencias universales inventadas entre familias;
- múltiples fuentes de verdad;
- metadata del catálogo contradictoria con fuentes canónicas;
- Templates especulativos sin caso de uso;
- elementos incorporados únicamente para aumentar cobertura.

---

# 94. Catalog Quality Gates

Antes de aprobar una nueva versión del Component Catalog deberá verificarse:

- [ ] Las familias reconocidas están alineadas con el RDS.
- [ ] Los Components registrados coinciden con las responsabilidades reconocidas.
- [ ] La clasificación `Implemented` / `Conceptual` es correcta.
- [ ] Los Repository Templates registrados coinciden con la implementación real.
- [ ] Los Templates potenciales no se presentan como oficiales.
- [ ] Los Maturity Profiles no aparecen como Templates.
- [ ] Los Repository Profiles no se presentan como elementos activos del Framework.
- [ ] La metadata reproducida coincide con las fuentes canónicas.
- [ ] Las relaciones y dependencias están correctamente representadas.
- [ ] No existen requirement levels globales.
- [ ] Las fuentes canónicas pueden localizarse.

---

# 95. Framework Evolution

El Component Catalog deberá evolucionar conforme se materialicen nuevas capacidades del Framework.

Entre las líneas previsibles se encuentran:

- implementación progresiva de Workflow Components;
- implementación progresiva de Visual Components;
- nuevos Repository Templates respaldados por casos reales;
- validación automática del catálogo;
- resolución machine-readable de Components;
- generación asistida;
- herramientas de descubrimiento;
- análisis de dependencias y trazabilidad.

La planificación concreta pertenece a:

```text
ROADMAP.md
+
docs/governance/14_BACKLOG.md
+
GitHub Issues
```

El Component Catalog no mantendrá un roadmap paralelo.

---

# 96. Long-Term Vision

El Component Catalog deberá funcionar como interfaz central de descubrimiento del ecosistema GitHub Framework.

Permitirá comprender:

- qué responsabilidades reconoce el Framework;
- cuáles están implementadas;
- cuáles permanecen conceptuales;
- qué Repository Templates existen;
- cómo localizar sus fuentes canónicas;
- cómo se relacionan los diferentes elementos.

Con el tiempo podrá alimentar herramientas de validación, generación y gobierno sin convertirse en una definición paralela del sistema.

---

# 97. Final Conclusions

El **Component Catalog** proporciona una vista gobernada y centralizada de los elementos reutilizables reconocidos por GitHub Framework.

Las fuentes canónicas mantienen las definiciones.

El catálogo facilita su descubrimiento.

Los Repository Templates realizan la composición contextual.

Los Maturity Profiles expresan expectativas independientes de evolución.

```text
RDS
        ↓
Canonical Definitions
        ↓
Component Catalog
        ↓
Repository Templates
        ↓
Repository Implementations
        ↓
Validation
```

El catálogo permite distinguir claramente entre arquitectura reconocida e implementación disponible.

Su valor no reside en convertirse en una segunda fuente de verdad, sino en mantener una representación coherente y navegable del Framework real.

---

# 98. Revision History

| Version | Date       | Description |
| ------- | ---------- | ----------- |
| 1.0.0   | 2026-08-05 | Primera versión del Component Catalog. |
| 1.0.1   | 2026-08-11 | Metadata alineada con GitHub Framework durante la implementación de referencia del Documentation Framework. |
| 1.1.0   | 2026-08-16 | Arquitectura del catálogo consolidada alrededor de fuentes canónicas, clasificación de implementación, Repository Templates contextuales y Maturity Profiles independientes; retirados Repository Profiles y Maturity Templates como elementos activos. |