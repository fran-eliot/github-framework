# 08 - REPOSITORY DESIGN SYSTEM

| Field        | Value                          |
| ------------ | ------------------------------ |
| **Project**  | GitHub Framework               |
| **Document** | Repository Design System (RDS) |
| **Version**  | 1.2.0                          |
| **Status**   | Stable                         |
| **Owner**    | Fran Ramirez                   |

---

# Part 1/7

# Repository Design System Foundations

---

# 1. Purpose

El **Repository Design System (RDS)** define el modelo arquitectónico de GitHub Framework para construir, evolucionar y mantener repositorios mediante elementos reutilizables.

Su objetivo consiste en transformar la creación y mantenimiento de repositorios desde una actividad artesanal hacia un proceso basado en:

- estándares;
- Framework Components;
- Repository Templates;
- Maturity Profiles;
- reglas de composición;
- validación;
- gobernanza.

El RDS complementa los estándares GRS.

Mientras los GRS definen criterios de calidad y evaluación, el RDS define cómo estructurar, reutilizar y combinar las capacidades necesarias para construir repositorios coherentes.

El sistema podrá aplicarse a distintos tipos de proyecto sin imponer una composición, estructura física o nivel de automatización idénticos a todos ellos.

---

# 2. Vision

Todo repositorio que adopte GitHub Framework deberá poder reutilizar responsabilidades ya definidas por el sistema cuando resulten aplicables.

La creación de un nuevo proyecto no deberá comenzar necesariamente desde cero.

Cuando exista un Repository Template adecuado, este proporcionará una composición inicial de Framework Components.

El proyecto consumidor podrá adaptar esa composición según sus necesidades sin:

- duplicar responsabilidades canónicas;
- introducir Components innecesarios;
- alterar arbitrariamente sus contratos;
- asumir que todos los repositorios deben materializar las mismas capacidades de la misma forma.

El objetivo final consiste en permitir que las decisiones reutilizables permanezcan en el Framework mientras las decisiones específicas permanezcan en el repositorio consumidor.

---

# 3. Relationship with Other Standards

El RDS se apoya en los siguientes documentos.

| Document                       | Responsibility                     |
| ------------------------------ | ---------------------------------- |
| 01_BRAND                       | Identidad profesional              |
| 02_VISUAL_IDENTITY             | Lenguaje visual                    |
| 03_PORTFOLIO_ARCHITECTURE      | Arquitectura del portfolio         |
| 04_REPOSITORY_AUDIT            | Estado actual                      |
| 05_PROFILE_README_ARCHITECTURE | Arquitectura del README del perfil |
| 06_VISUAL_DESIGN_SYSTEM        | Sistema visual                     |
| 07_GITHUB_METADATA             | Estándares GRS                     |

El RDS reutiliza estos documentos cuando corresponde.

No los sustituye.

Del mismo modo, el RDS no sustituye:

- el Component Catalog;
- los estándares especializados;
- las especificaciones canónicas de los Components;
- las especificaciones canónicas de los Repository Templates;
- las Reference Implementations;
- la documentación de gobierno.

Cada artefacto mantiene una responsabilidad diferenciada dentro de GitHub Framework.

---

# 4. Repository as a System

Un repositorio deja de considerarse únicamente un conjunto de archivos.

Pasa a entenderse como un sistema formado por responsabilidades relacionadas.

Modelo conceptual:

```text
Repository
    │
    ├── Metadata
    ├── README
    ├── Documentation
    ├── Workflows
    ├── Assets
    └── Governance
```

Estas responsabilidades podrán materializarse mediante uno o varios Framework Components.

Los Framework Components encapsulan responsabilidades reutilizables.

Los Repository Templates determinan qué combinación resulta adecuada para cada tipo de proyecto.

Los repositorios consumidores materializan finalmente esas responsabilidades de acuerdo con su contexto.

Por tanto:

```text
Reusable responsibility
        ↓
Framework Component
        ↓
Repository Template
        ↓
Consumer implementation
```

---

# 5. Component Philosophy

Todo Framework Component deberá perseguir cuatro propiedades fundamentales:

- reutilizable;
- suficientemente desacoplado;
- documentado;
- mantenible.

Un Component deberá representar una responsabilidad generalizable.

Podrá admitir:

- parámetros;
- variantes;
- configuración;
- guidance contextual;
- diferentes mecanismos de materialización cuando su naturaleza lo requiera.

Sin embargo, su definición canónica no deberá depender innecesariamente de un único proyecto consumidor.

Cuando una necesidad sea exclusivamente específica de un proyecto y no exista evidencia de reutilización potencial, deberá permanecer en ese proyecto.

La existencia de una práctica útil en un repositorio no implica automáticamente que deba convertirse en Framework Component.

---

# 6. Design Principles

El Repository Design System seguirá los siguientes principios:

- composición frente a duplicación;
- consistencia frente a personalización excesiva;
- simplicidad frente a complejidad;
- evolución incremental;
- implementación antes que formalización prematura;
- documentación como parte del diseño;
- fuentes canónicas identificables;
- automatización basada en contratos existentes;
- especialización únicamente cuando aporte valor;
- validación mediante uso real cuando corresponda.

Estos principios deberán aplicarse conjuntamente.

Ninguno deberá utilizarse de forma aislada para justificar complejidad innecesaria.

---

# 7. Single Source of Truth

Cada elemento reutilizable del RDS deberá disponer de una fuente canónica identificable.

Para los Framework Components implementados, la definición canónica estará formada por:

```text
Specification
        +
Metadata
        +
Required materialization artifacts
        when applicable
```

La Specification define la responsabilidad y el contrato humano del Component.

La Metadata proporciona su representación estructurada y machine-readable.

Los artefactos de materialización proporcionan la capacidad reutilizable cuando la responsabilidad del Component no puede satisfacerse únicamente mediante Specification y Metadata.

El Component Catalog proporciona descubrimiento, clasificación y estado global.

No sustituye las definiciones canónicas.

Los Repository Templates mantienen su composición canónica en sus propias especificaciones y metadata.

Las plantillas, ejemplos, documentación, consumidores y Reference Implementations deberán derivarse de estas fuentes.

No deberán mantenerse definiciones paralelas incompatibles del mismo elemento.

---

# 8. Component Taxonomy

Los Framework Components podrán organizarse en familias según la responsabilidad que representan.

Las familias actualmente reconocidas por el RDS incluyen:

| Family | Prefix | Responsibility |
| --- | --- | --- |
| README Components | `README-*` | Presentación y navegación principal |
| Documentation Components | `DOC-*` | Documentación técnica, operativa, de gobierno y referencia |
| Workflow Components | `WCL-*` | Procesos de desarrollo, validación, publicación y mantenimiento |
| Visual Components | `VCL-*` | Identidad y comunicación visual |
| Governance Components | Según definición futura | Responsabilidades de gobierno reutilizables cuando exista implementación |

La existencia conceptual de una familia no implica que todos sus Components estén implementados físicamente.

Las familias proporcionan clasificación y contexto arquitectónico.

No determinan requirement levels.

El Component Catalog mantiene la visión global de los Components reconocidos por GitHub Framework.

---

# 9. Component Identity

Todo Framework Component reconocido formalmente deberá disponer de una identidad estable.

La identidad deberá permitir:

- referenciar el Component sin ambigüedad;
- mantener relaciones y dependencias;
- utilizarlo desde Repository Templates;
- localizar su definición canónica;
- validar su estado;
- soportar automatización futura.

Cuando una familia disponga de un prefijo definido, sus identificadores deberán utilizarlo.

Ejemplos:

```text
README-HERO
DOC-ARCHITECTURE
WCL-CI
VCL-BANNER
```

El identificador representa la responsabilidad canónica.

No deberá utilizarse para representar una implementación específica de un repositorio consumidor.

---

# 10. Component Canonical Definition

Un Framework Component implementado deberá disponer de una definición canónica suficiente para comprender y reutilizar su responsabilidad.

Como mínimo, la definición canónica estará formada por:

```text
Component
    │
    ├── Specification
    └── Metadata
```

Cuando la responsabilidad requiera materialización adicional:

```text
Component
    │
    ├── Specification
    ├── Metadata
    └── Materialization Artifacts
```

La Specification deberá describir, según corresponda:

- propósito;
- responsabilidad;
- alcance;
- límites;
- consumidores;
- utilización;
- relaciones;
- dependencias;
- comportamiento esperado;
- criterios relevantes de adopción.

La Metadata deberá proporcionar la información estructurada necesaria para identificación, clasificación, versionado, lifecycle y futuras capacidades de validación o automatización.

Los Materialization Artifacts dependerán de la naturaleza de la responsabilidad.

No todos los Framework Components necesitarán el mismo tipo de artefacto.

---

# 11. Specification

La Specification constituye la representación humana principal del contrato de un Framework Component.

Deberá permitir responder al menos:

```text
What responsibility does this Component represent?

Why does it exist?

What does it cover?

What does it not cover?

How can it be consumed?
```

La Specification no deberá convertirse en una copia de:

- estándares globales;
- metadata;
- implementación específica de un consumidor;
- documentación mantenida canónicamente en otro artefacto.

Cuando existan reglas generales aplicables a toda una familia, la Specification deberá referenciarlas en lugar de duplicarlas innecesariamente.

---

# 12. Metadata

La Metadata constituye la representación estructurada del Component.

Deberá utilizarse cuando sea necesaria para:

- identidad;
- descubrimiento;
- clasificación;
- versionado;
- lifecycle;
- relaciones;
- dependencias;
- validación;
- composición;
- automatización futura.

La Metadata no deberá convertirse en una segunda Specification.

Los campos deberán representar información suficientemente estable y machine-readable.

Las decisiones específicas de cada familia podrán ampliar este contrato cuando exista una necesidad demostrada.

---

# 13. Materialization

La materialización representa la forma mediante la cual una responsabilidad definida por un Framework Component se convierte en una capacidad reutilizable o en una implementación observable.

La forma de materialización dependerá de la naturaleza del Component.

Ejemplos conceptuales:

```text
Documentation responsibility
        ↓
Reusable document structure

README responsibility
        ↓
Reusable README section

Workflow responsibility
        ↓
Configuration / community file / executable workflow / convention

Visual responsibility
        ↓
Reusable visual artifact or specification
```

No deberá imponerse un mecanismo de materialización idéntico a todas las familias ni a todos los Components de una misma familia.

La arquitectura deberá preservar la responsabilidad antes que la simetría del filesystem.

---

# 14. Component Implementation States

El RDS distinguirá como mínimo entre responsabilidades:

```text
Conceptual
Implemented
```

## Conceptual

Una responsabilidad `Conceptual` está reconocida por el RDS pero todavía no dispone de una representación canónica reutilizable suficiente para considerarse implementada dentro del Framework.

Su existencia conceptual permite:

- identificar una responsabilidad;
- evitar duplicaciones futuras;
- discutir su alcance;
- evaluar su necesidad;
- incorporarla posteriormente mediante el lifecycle correspondiente.

No deberá presentarse como capacidad disponible para consumo directo.

## Implemented

Un Component `Implemented` dispone de una definición canónica reutilizable y gobernada que satisface el contrato arquitectónico aplicable a su responsabilidad.

Como mínimo deberá existir:

- Specification;
- Metadata;
- materialización adicional cuando la responsabilidad la requiera.

La existencia de una práctica equivalente en GitHub Framework o en otro repositorio no convierte por sí sola una responsabilidad conceptual en un Component implementado.

---

# 15. Conceptual to Implemented Transition

La transición:

```text
Conceptual
        ↓
Implemented
```

deberá producirse únicamente cuando exista evidencia suficiente de que la responsabilidad ha sido materializada como capacidad reutilizable del Framework.

Antes de cambiar el estado deberá verificarse:

- que la responsabilidad continúa siendo necesaria;
- que no duplica otro Component;
- que su identidad es estable;
- que dispone de Specification;
- que dispone de Metadata;
- que sus dependencias reales están declaradas cuando corresponda;
- que dispone de los artefactos necesarios para satisfacer su responsabilidad;
- que puede ser consumida fuera de una única implementación accidental;
- que cumple los Quality Gates aplicables.

La transición no implica necesariamente que el Component haya alcanzado su máxima madurez.

La validación mediante Reference Implementation o dogfooding podrá producir ajustes posteriores.

---

# 16. Component Lifecycle

Los Framework Components seguirán el lifecycle definido por la gobernanza del RDS.

Conceptualmente:

```text
Idea
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
Deprecation
    ↓
Retirement
```

Los estados de implementación y las etapas del lifecycle representan conceptos relacionados pero diferentes.

Por ejemplo:

```text
Implemented
≠
Fully validated
```

Un Component podrá disponer de implementación antes de completar su validación mediante consumidores reales.

No deberá considerarse suficientemente maduro para adopción general únicamente por existir físicamente.

La definición detallada de estados y transiciones pertenece a la gobernanza del RDS y a los estándares especializados cuando corresponda.

---

# 17. Component Granularity

Los Framework Components deberán ser lo suficientemente pequeños para reutilizarse y suficientemente completos para representar una responsabilidad coherente.

Ejemplos adecuados:

- Hero Section;
- Quick Start;
- Architecture Documentation;
- Continuous Integration;
- Release Management.

Ejemplos excesivamente amplios:

- README completo;
- toda la documentación;
- todo el repositorio;
- todo el lifecycle de desarrollo.

Ejemplos excesivamente pequeños:

- una frase aislada;
- un único comando sin responsabilidad propia;
- una propiedad de configuración sin significado independiente.

La granularidad deberá favorecer composición y mantenimiento.

---

# 18. Composition Model

Los Framework Components se combinan mediante composición.

Ejemplo conceptual:

```text
Component A
+
Component B
+
Component C
        ↓
Repository Template
        ↓
Consumer
```

La composición no será completamente arbitraria.

Deberá respetar:

- la responsabilidad de cada Component;
- sus dependencias cuando existan;
- el Repository Template aplicable;
- las necesidades reales del proyecto consumidor;
- las restricciones derivadas de la propia plataforma cuando correspondan.

No todos los proyectos utilizarán exactamente la misma combinación.

Los Repository Templates proporcionarán composiciones reutilizables sin impedir extensiones justificadas.

---

# 19. Component Requirement Levels

La necesidad de un Framework Component se evaluará dentro del contexto de cada Repository Template.

Los Repository Templates utilizarán tres requirement levels:

## Required

El Component forma parte del contrato mínimo del Template.

## Recommended

El Component aporta valor habitual para ese tipo de repositorio, pero su necesidad final depende del proyecto consumidor.

## Optional

El Component se incorpora únicamente cuando existe una necesidad concreta.

Por tanto:

```text
Component
+
Repository Template Context
        ↓
Requirement Level
```

Un mismo Component podrá tener requirement levels diferentes en Templates distintos.

Ejemplo conceptual:

```text
WCL-CI
    ├── Required      → Template A
    ├── Recommended   → Template B
    └── Optional      → Template C
```

El requirement level no modifica:

- la identidad;
- la definición canónica;
- el estado de implementación;
- la prioridad;
- la madurez intrínseca del Component.

---

# 20. Component Independence

Cada Framework Component deberá poder evolucionar con el menor acoplamiento posible respecto al resto del sistema.

Modificar un Component no deberá obligar a modificar Components no relacionados.

Ejemplo:

```text
README-QUICK-START
```

podrá evolucionar sin requerir el rediseño completo del README.

Sin embargo, independencia no significa ausencia absoluta de relaciones.

Cuando una responsabilidad requiera realmente otra capacidad, la dependencia deberá declararse explícitamente.

---

# 21. Component Dependencies

Una dependencia existe cuando un Component necesita otro elemento para satisfacer correctamente su responsabilidad.

Las dependencias deberán ser:

- reales;
- explícitas;
- mínimas;
- justificables;
- mantenibles.

No deberán inferirse únicamente por:

- proximidad física;
- orden de presentación;
- uso habitual conjunto;
- pertenencia a la misma familia;
- coincidencia de madurez.

Ejemplo:

```text
Component A
        ↓ requires
Component B
```

es diferente de:

```text
Component A
        ↔ commonly used with
Component B
```

Las dependencias reales deberán mantenerse en la definición canónica cuando exista implementación.

---

# 22. Relationships

Los Framework Components podrán mantener relaciones que no constituyan dependencias.

Entre ellas podrán existir:

- complementariedad;
- navegación;
- secuencia operativa;
- especialización;
- consumo conjunto habitual;
- relación con documentación;
- relación con Repository Templates.

Estas relaciones deberán diferenciarse de dependencias estructurales.

La arquitectura no deberá convertir relaciones conceptuales en acoplamiento obligatorio.

---

# 23. Naming Convention

Los elementos reutilizables del RDS deberán utilizar nombres e identificadores estables y suficientemente descriptivos.

Cuando exista un identificador formal deberá seguir la convención definida para su familia.

Ejemplos:

```text
README-HERO
DOC-ARCHITECTURE
WCL-RELEASE
VCL-BANNER
TPL-BACKEND
```

Los nombres deberán representar responsabilidades y evitar ambigüedad.

Los identificadores existentes no deberán modificarse sin evaluar:

- compatibilidad;
- consumidores;
- metadata asociada;
- Repository Templates;
- documentación;
- automatización futura.

---

# 24. Machine-Readable Identifiers

Los elementos reutilizables del RDS utilizarán identificadores estables cuando necesiten ser referenciados por:

- documentación;
- metadata;
- Repository Templates;
- validadores;
- catálogos;
- futuras automatizaciones.

Estos identificadores deberán corresponder con la definición canónica del elemento.

No deberán constituir una taxonomía paralela.

Las futuras capacidades de automatización deberán consumir estos identificadores y la metadata existente en lugar de introducir tokens equivalentes.

---

# 25. Versioning

Los Framework Components podrán mantener versionado independiente del repositorio y de la versión global de GitHub Framework.

Cuando un elemento sea versionable utilizará Semantic Versioning:

```text
Major.Minor.Patch
```

Los Repository Templates podrán mantener igualmente versionado independiente.

Una nueva versión de GitHub Framework no obliga automáticamente a modificar la versión de todos sus Components o Templates.

Los cambios incompatibles deberán reflejarse mediante el versionado correspondiente y seguir la política de compatibilidad definida por la gobernanza.

---

# 26. Backward Compatibility

Los cambios en un Framework Component deberán mantener compatibilidad razonable con consumidores anteriores cuando sea posible.

Los cambios incompatibles deberán:

- estar justificados;
- identificarse claramente;
- reflejarse en el versionado;
- considerar consumidores existentes;
- proporcionar guidance de migración cuando corresponda.

No deberá mantenerse compatibilidad indefinida cuando esta impida corregir un contrato incorrecto o introduzca complejidad desproporcionada.

---

# 27. Component Consumers

Los Framework Components podrán utilizarse, según corresponda, en:

- repositorios backend;
- proyectos full stack;
- repositorios documentales;
- GitHub Profile;
- proyectos de aprendizaje cuando sus necesidades lo justifiquen;
- futuros tipos de repositorio soportados por GitHub Framework.

No todos los Components serán aplicables a todos los consumidores.

La selección deberá realizarse mediante:

```text
Repository Template
```

o mediante una necesidad explícitamente justificada cuando no exista Template aplicable.

La madurez del consumidor podrá modificar las expectativas de calidad y mantenimiento.

No constituye por sí misma un tipo de consumidor ni determina automáticamente la composición.

---

# 28. Consumer Conformance

La disponibilidad de un Framework Component y la conformidad de un consumidor son conceptos diferentes.

```text
Component availability
        ≠
Consumer conformance
```

Un Component podrá estar `Implemented` aunque un repositorio consumidor no lo utilice.

Un repositorio podrá materializar una responsabilidad equivalente sin ser necesariamente conforme con el Component canónico.

La conformidad deberá evaluarse contra:

- el Repository Template aplicable;
- los Components seleccionados;
- sus contratos canónicos;
- las adaptaciones permitidas;
- los Quality Gates correspondientes.

No deberá inferirse conformidad únicamente por la existencia de archivos con nombres similares.

---

# 29. Repository Design Layers

El diseño completo de un repositorio podrá analizarse mediante diferentes capas.

```text
Brand Layer

↓

Metadata Layer

↓

Documentation Layer

↓

Engineering Layer

↓

Governance Layer
```

Las capas proporcionan una vista conceptual.

No obligan a mantener una correspondencia uno a uno con:

- directorios;
- Components;
- Repository Templates;
- mecanismos de materialización.

Un Component podrá contribuir a más de una preocupación arquitectónica cuando su responsabilidad lo justifique.

---

# 30. Reuse Strategy

Antes de crear un Component nuevo deberá comprobarse:

- ¿Existe ya una responsabilidad equivalente?
- ¿Puede reutilizarse un Component existente?
- ¿Puede ampliarse sin romper su responsabilidad?
- ¿Puede parametrizarse?
- ¿La necesidad es suficientemente recurrente?
- ¿Debe permanecer específica del consumidor?

El flujo preferente será:

```text
Reuse
    ↓
Configure
    ↓
Extend
    ↓
Create
```

La creación de un nuevo Component será la última opción cuando las anteriores no representen correctamente la responsabilidad.

---

# 31. Documentation Requirements

Todo Framework Component deberá disponer de documentación suficiente para comprender:

- su propósito;
- su responsabilidad;
- su alcance;
- sus límites;
- su forma de utilización;
- sus relaciones y dependencias cuando existan;
- su mecanismo de materialización cuando sea relevante.

Cuando corresponda, deberá incluir:

- ejemplos;
- templates;
- configuration guidance;
- migration guidance;
- validation guidance.

La documentación forma parte de la definición del Component.

No deberá sustituir a la implementación cuando la responsabilidad requiera capacidad material o ejecutable.

---

# 32. Component Quality Attributes

Todo Framework Component deberá evaluarse según:

- claridad;
- reutilización;
- independencia;
- mantenibilidad;
- facilidad de comprensión;
- consistencia con el resto del sistema;
- verificabilidad;
- proporcionalidad;
- capacidad de evolución.

Los Components ejecutables deberán considerar además atributos específicos como seguridad, observabilidad y reproducibilidad cuando resulten aplicables.

---

# 33. Validation Model

La existencia de una definición canónica no constituye por sí sola evidencia suficiente de que un Component funciona correctamente en consumidores reales.

La validación podrá realizarse mediante:

- implementación directa;
- Reference Implementation;
- dogfooding;
- adopción por consumidores;
- Quality Gates;
- automatización cuando exista.

Modelo conceptual:

```text
Canonical Definition
        ↓
Implementation
        ↓
Reference Implementation
        ↓
Findings
        ↓
Refinement
        ↓
Validated Pattern
```

Los findings obtenidos mediante uso real podrán justificar ajustes arquitectónicos.

No deberán utilizarse para introducir cambios no relacionados con la evidencia observada.

---

# 34. Framework Dogfooding

GitHub Framework podrá utilizarse como consumidor de sus propios Components cuando exista una correspondencia real entre la responsabilidad del Component y las necesidades del repositorio.

El dogfooding permite:

- validar contratos;
- detectar dependencias;
- identificar complejidad innecesaria;
- comprobar materializaciones;
- evaluar mantenibilidad;
- detectar diferencias entre disponibilidad y conformidad.

Sin embargo:

```text
Existing repository practice
        ≠
Framework Component implementation
```

La utilización previa de una práctica dentro de GitHub Framework no demuestra por sí sola que exista un Component reutilizable.

El Component deberá satisfacer su contrato canónico independientemente del consumidor utilizado para validarlo.

---

# 35. Automation Boundary

La automatización futura deberá consumir las fuentes canónicas definidas por el RDS.

No deberá convertirse en una fuente arquitectónica paralela.

Modelo:

```text
Specification
        +
Metadata
        +
Materialization
        ↓
Automation
```

No:

```text
Automation
        ↓
Implicit architecture
```

Las herramientas futuras podrán:

- descubrir Components;
- resolver Repository Templates;
- validar metadata;
- evaluar conformidad;
- materializar artefactos;
- detectar drift.

Estas capacidades deberán derivarse de contratos previamente definidos y validados.

---

# 36. Anti-Patterns

No deberán aparecer:

- Components duplicados;
- Repository Templates incompatibles para necesidades equivalentes;
- nombres inconsistentes;
- documentación repetida;
- definiciones canónicas paralelas;
- Components específicos de un único proyecto sin evidencia de reutilización;
- Components incorporados únicamente para aumentar cobertura;
- composiciones rígidas derivadas exclusivamente de la madurez;
- requirement levels definidos globalmente fuera de Repository Templates;
- dependencias inferidas sin necesidad real;
- artefactos vacíos creados únicamente para aparentar implementación;
- estados `Implemented` sin capacidad reutilizable suficiente;
- automatización que sustituya contratos arquitectónicos;
- estructuras físicas uniformes impuestas a responsabilidades heterogéneas.

---

# 37. Component Quality Gates

Antes de incorporar o promover un Framework Component dentro del RDS deberá verificarse, según corresponda:

- [ ] Tiene un propósito definido.
- [ ] Su responsabilidad está claramente delimitada.
- [ ] Su alcance y límites están documentados.
- [ ] Existe evidencia de reutilización potencial.
- [ ] Está suficientemente desacoplado.
- [ ] Mantiene coherencia con el sistema.
- [ ] No duplica una responsabilidad existente.
- [ ] Su identidad es estable.
- [ ] Su fuente canónica está identificada.
- [ ] Dispone de Specification cuando corresponde a un Component implementado.
- [ ] Dispone de Metadata cuando corresponde a un Component implementado.
- [ ] Incluye materialización suficiente cuando su responsabilidad la requiere.
- [ ] Sus dependencias reales están identificadas.
- [ ] No introduce estructura o automatización innecesaria.
- [ ] Puede validarse mediante implementación, Reference Implementation o dogfooding.
- [ ] Su estado refleja correctamente su disponibilidad real.

Los Quality Gates especializados de cada familia podrán ampliar estos criterios.

---

# 38. Long-Term Vision

El Repository Design System constituye el modelo arquitectónico sobre el que GitHub Framework desarrolla una biblioteca reutilizable para construir y evolucionar repositorios.

Su evolución deberá permitir:

- reducir el esfuerzo de creación;
- reutilizar responsabilidades ya resueltas;
- mantener consistencia;
- acelerar la documentación;
- reutilizar procesos operativos;
- facilitar la evolución de los repositorios;
- validar conformidad;
- detectar drift;
- soportar progresivamente automatización y generación asistida.

La evolución se realizará a partir de necesidades reales y de evidencia obtenida mediante:

- implementaciones;
- consumidores;
- Reference Implementations;
- dogfooding.

La automatización deberá ampliar el sistema sin sustituir sus fuentes canónicas.

---

# 39. Part 1 Conclusions

El **Repository Design System** proporciona los fundamentos arquitectónicos de GitHub Framework.

Los repositorios se entienden como sistemas formados por responsabilidades reutilizables.

Los Framework Components encapsulan esas responsabilidades mediante contratos canónicos.

Los Repository Templates las combinan según tipos de proyecto.

Los Maturity Profiles expresan expectativas de evolución y mantenimiento.

Los consumidores materializan finalmente las responsabilidades seleccionadas.

```text
Standards
        ↓
Framework Components
        ↓
Repository Templates
        ↓
Repository Implementations
        ↓
Validation and Evolution
```

La arquitectura distingue explícitamente entre:

```text
Responsibility
Implementation
Materialization
Availability
Consumer Conformance
```

Estas dimensiones están relacionadas, pero no son equivalentes.

El resultado es un sistema orientado a reutilización, consistencia y evolución incremental sin imponer la misma estructura, composición o materialización a todos los proyectos.

---

# 40. Part 1 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.

---

# 08 - REPOSITORY DESIGN SYSTEM

# Part 2/7

# README Component Library

---

# 41. Purpose

La **README Component Library** define responsabilidades reutilizables para construir la capa principal de presentación, comprensión inicial y navegación de los repositorios que adopten GitHub Framework.

Cada README Component representa una responsabilidad concreta dentro del README.

Los Repository Templates podrán reutilizar estos Components para definir composiciones adecuadas a distintos tipos de proyecto.

El objetivo no consiste en eliminar toda personalización ni en imponer un README universal.

Consiste en evitar que responsabilidades recurrentes deban diseñarse nuevamente desde cero.

---

# 42. README Philosophy

Todo README deberá perseguir tres objetivos principales:

```text
Capture Attention
        ↓
Build Confidence
        ↓
Enable Action
```

El lector deberá poder:

- comprender rápidamente qué es el proyecto;
- identificar su propósito y capacidades principales;
- evaluar su estado y contexto;
- localizar la información necesaria;
- saber cómo comenzar a utilizarlo cuando corresponda.

El README constituye una capa de entrada.

No deberá convertirse en una copia de toda la documentación del proyecto.

---

# 43. README Architecture

La composición conceptual de un README podrá incluir responsabilidades como:

```text
Hero
        ↓
Status
        ↓
Overview
        ↓
Highlights / Features
        ↓
Architecture
        ↓
Technology Stack
        ↓
Repository Structure
        ↓
Quick Start
        ↓
Documentation
        ↓
Demo / Testing
        ↓
Roadmap
        ↓
Contributing
        ↓
License
        ↓
Author / Footer
```

Este flujo representa una referencia de lectura.

No constituye una estructura obligatoria ni un orden universal.

No todos los repositorios necesitarán todos los Components.

La composición efectiva deberá derivarse del Repository Template y de las necesidades reales del consumidor.

---

# 44. README Component Classification

Los README Components se clasifican principalmente por la responsabilidad que representan.

Su necesidad dentro de un repositorio no se define mediante una clasificación global `Core`, `Extended` u `Optional`.

El requirement level pertenece al Repository Template que consume el Component.

Por tanto:

```text
README Component
        ↓
Canonical Responsibility

Repository Template
        ↓
Required / Recommended / Optional
```

Un mismo README Component podrá ser:

- `required` en un Repository Template;
- `recommended` en otro;
- `optional` en otro;
- o no formar parte de una determinada composición.

La prioridad, madurez y disponibilidad canónicas del Component se mantienen separadas de su requirement level contextual.

---

# 45. README-HERO

## Identifier

```text
README-HERO
```

## Purpose

Presentar el proyecto de forma inmediata.

Deberá permitir identificar el proyecto y su propuesta principal en pocos segundos.

## Typical Contents

Podrá incluir:

- banner;
- nombre;
- tagline;
- badges principales.

## Example

```text
Banner

NovaCoquinaria

Knowledge Engineering Platform

Badges
```

La presencia de cada elemento dependerá del proyecto y de su identidad visual.

---

# 46. README-STATUS

## Identifier

```text
README-STATUS
```

## Purpose

Comunicar el estado actual del proyecto.

## Possible Values

Ejemplos:

```text
Active Development
Stable
Maintenance
Archived
Research
```

Los valores concretos deberán mantener coherencia con la gobernanza y metadata del repositorio.

El Component no deberá introducir un estado contradictorio con otras fuentes canónicas.

---

# 47. README-OVERVIEW

## Identifier

```text
README-OVERVIEW
```

## Purpose

Explicar qué es el proyecto, por qué existe y a quién está dirigido.

Deberá responder principalmente:

```text
Why?
What?
Who?
```

La explicación detallada de instalación o ejecución pertenece normalmente a `README-QUICK-START`.

## Recommended Length

Como referencia general:

```text
200–500 palabras
```

La extensión deberá adaptarse a la complejidad real del proyecto.

---

# 48. README-HIGHLIGHTS

## Identifier

```text
README-HIGHLIGHTS
```

## Purpose

Mostrar rápidamente las capacidades o características que mejor representan el valor del proyecto.

## Typical Use

Puede utilizarse para destacar:

- capacidades diferenciales;
- propiedades arquitectónicas;
- casos de uso importantes;
- características especialmente relevantes para el lector.

No deberá convertirse en una repetición completa de `README-FEATURES`.

---

# 49. README-FEATURES

## Identifier

```text
README-FEATURES
```

## Purpose

Presentar las funcionalidades principales del proyecto.

## Principle

Las funcionalidades describen qué puede hacer el sistema.

No deberán confundirse con las tecnologías utilizadas para implementarlo.

Ejemplo:

```text
Feature
    ≠
Technology
```

Cuando el proyecto disponga de una especificación funcional extensa, el README deberá resumirla y enlazar la documentación canónica correspondiente.

---

# 50. README-ARCHITECTURE

## Identifier

```text
README-ARCHITECTURE
```

## Purpose

Proporcionar una visión arquitectónica suficiente para comprender la estructura general del sistema.

## Possible Contents

Podrá incluir:

- módulos principales;
- capas;
- relaciones de alto nivel;
- flujo principal;
- diagrama resumido;
- enlace a documentación arquitectónica completa.

No deberá duplicar innecesariamente `DOC-ARCHITECTURE`.

Cuando exista documentación arquitectónica especializada:

```text
README-ARCHITECTURE
        ↓
Architecture summary
        ↓
DOC-ARCHITECTURE
        ↓
Canonical detailed documentation
```

---

# 51. README-TECH-STACK

## Identifier

```text
README-TECH-STACK
```

## Purpose

Presentar las tecnologías principales utilizadas por el proyecto.

## Principle

Deberá priorizar tecnologías relevantes para comprender, utilizar o mantener el proyecto.

No deberá convertirse en una lista exhaustiva de todas las dependencias.

## Example

```text
Java
Spring Boot
PostgreSQL
Docker
GitHub Actions
```

Las funcionalidades y las tecnologías deberán mantenerse conceptualmente separadas.

---

# 52. README-REPOSITORY-STRUCTURE

## Identifier

```text
README-REPOSITORY-STRUCTURE
```

## Purpose

Explicar la organización principal del repositorio cuando esta información facilite su comprensión o mantenimiento.

## Example

```text
.github/
docs/
framework/
src/
tests/
```

No será necesario documentar cada archivo.

La explicación deberá centrarse en elementos estructurales relevantes.

---

# 53. README-QUICK-START

## Identifier

```text
README-QUICK-START
```

## Purpose

Permitir que un usuario pueda comenzar a utilizar el proyecto con el menor esfuerzo razonable.

## Typical Structure

```text
Requirements
        ↓
Installation
        ↓
Configuration
        ↓
Run
```

Podrán añadirse pasos cuando sean realmente necesarios.

## Principle

El Quick Start deberá optimizar el camino hacia una primera ejecución o utilización satisfactoria.

Como referencia, debería poder completarse o comprenderse en pocos minutos cuando la naturaleza del proyecto lo permita.

No deberá convertirse en documentación operativa exhaustiva.

---

# 54. README-DOCUMENTATION

## Identifier

```text
README-DOCUMENTATION
```

## Purpose

Proporcionar navegación hacia documentación adicional del proyecto.

## Typical Links

Podrá enlazar, según corresponda, a:

- Architecture;
- ADR;
- API;
- Database;
- Deployment;
- Security;
- Testing;
- Roadmap;
- Project Status;
- Glossary;
- References.

Los enlaces deberán corresponder a documentación realmente existente.

No deberán crearse secciones o documentos vacíos únicamente para completar la navegación.

---

# 55. README-DEMO

## Identifier

```text
README-DEMO
```

## Purpose

Mostrar el proyecto funcionando cuando una demostración aporte valor real al lector.

## Possible Formats

Podrá utilizar:

- capturas;
- GIF;
- vídeo;
- GitHub Pages;
- demo desplegada;
- ejemplos ejecutables.

La demostración deberá aportar información funcional.

No deberá utilizarse únicamente como elemento decorativo.

---

# 56. README-TESTING

## Identifier

```text
README-TESTING
```

## Purpose

Explicar cómo validar el proyecto o resumir su estrategia de testing cuando resulte relevante para el usuario o contributor.

## Possible Contents

Podrá incluir:

```text
Test command
Test types
Coverage
CI validation
```

Ejemplo:

```text
JUnit
PyTest
Coverage
CI
```

Cuando exista `DOC-TESTING`, el README deberá proporcionar únicamente la información necesaria para comenzar y enlazar la documentación detallada.

---

# 57. README-ROADMAP

## Identifier

```text
README-ROADMAP
```

## Purpose

Resumir la evolución prevista del proyecto.

No sustituye al `ROADMAP.md` o al artefacto canónico equivalente.

Cuando exista un Roadmap independiente:

```text
README-ROADMAP
        ↓
Summary
        ↓
DOC-ROADMAP / ROADMAP.md
        ↓
Canonical roadmap
```

El README deberá evitar mantener una segunda planificación detallada que pueda divergir.

---

# 58. README-CONTRIBUTING

## Identifier

```text
README-CONTRIBUTING
```

## Purpose

Indicar cómo colaborar con el proyecto.

Deberá utilizarse cuando el repositorio acepte contribuciones o cuando resulte necesario orientar a contributors.

Cuando exista un `CONTRIBUTING.md`, este Component deberá actuar principalmente como punto de entrada.

No deberá duplicar todas las reglas de contribución.

---

# 59. README-LICENSE

## Identifier

```text
README-LICENSE
```

## Purpose

Comunicar la licencia aplicable y proporcionar acceso al artefacto canónico correspondiente.

No deberá reproducir innecesariamente el texto completo de la licencia.

Ejemplo:

```text
This project is released under the MIT License.
```

seguido del enlace correspondiente cuando sea necesario.

---

# 60. README-AUTHOR

## Identifier

```text
README-AUTHOR
```

## Purpose

Identificar al autor, maintainer u organización responsable cuando esta información resulte apropiada para el proyecto.

Deberá mantenerse breve.

Podrá enlazar a:

- GitHub Profile;
- organización;
- portfolio;
- otros canales profesionales relevantes.

No deberá convertirse en una biografía extensa dentro del README.

---

# 61. README-FOOTER

## Identifier

```text
README-FOOTER
```

## Purpose

Cerrar el documento y proporcionar elementos finales de navegación o contexto cuando sean necesarios.

Podrá incluir:

- agradecimientos;
- enlaces;
- navegación;
- referencias breves;
- información complementaria.

No deberá duplicar contenido ya presentado en otras secciones.

---

# 62. README Component Catalog

La README Component Library reconoce actualmente los siguientes Components:

| Component | Identifier | Responsibility |
| --- | --- | --- |
| Hero | `README-HERO` | Presentación inicial |
| Status | `README-STATUS` | Estado del proyecto |
| Overview | `README-OVERVIEW` | Propósito y contexto |
| Highlights | `README-HIGHLIGHTS` | Capacidades destacadas |
| Features | `README-FEATURES` | Funcionalidades principales |
| Architecture | `README-ARCHITECTURE` | Visión arquitectónica |
| Tech Stack | `README-TECH-STACK` | Tecnologías principales |
| Repository Structure | `README-REPOSITORY-STRUCTURE` | Organización del repositorio |
| Quick Start | `README-QUICK-START` | Primer uso |
| Documentation | `README-DOCUMENTATION` | Navegación documental |
| Demo | `README-DEMO` | Demostración |
| Testing | `README-TESTING` | Validación y testing |
| Roadmap | `README-ROADMAP` | Evolución prevista |
| Contributing | `README-CONTRIBUTING` | Contribución |
| License | `README-LICENSE` | Licencia |
| Author | `README-AUTHOR` | Autoría o mantenimiento |
| Footer | `README-FOOTER` | Cierre y navegación final |

El estado, versión, madurez, prioridad y localización canónicos de cada Component deberán consultarse en el Component Catalog y en su definición canónica cuando exista implementación.

Esta tabla representa la taxonomía arquitectónica de la familia.

No sustituye al Component Catalog.

---

# 63. README Composition

Los README Components deberán utilizarse mediante composición.

Ejemplo conceptual:

```text
README-HERO
+
README-STATUS
+
README-OVERVIEW
+
README-FEATURES
+
README-QUICK-START
+
README-DOCUMENTATION
+
README-LICENSE
        ↓
README
```

La composición dependerá del Repository Template y de las necesidades del consumidor.

No deberá seleccionarse un Component únicamente porque esté disponible en el Framework.

---

# 64. README Component Dependencies

La mayoría de README Components deberán mantenerse suficientemente independientes.

Sin embargo, podrán existir relaciones o dependencias reales.

Ejemplo conceptual:

```text
README-DOCUMENTATION
        ↓ may reference
DOC-ARCHITECTURE
DOC-API
DOC-ROADMAP
```

Esta relación no implica necesariamente que todos esos Documentation Components sean obligatorios.

Las dependencias reales deberán mantenerse en la definición canónica del Component cuando exista implementación.

Las relaciones de navegación o uso habitual no deberán convertirse automáticamente en dependencias.

---

# 65. Relationship with Documentation Components

README Components y Documentation Components cumplen responsabilidades diferentes.

```text
README Component
        ↓
Entry point / summary / navigation

Documentation Component
        ↓
Detailed canonical documentation
```

Cuando una responsabilidad necesite explicación extensa, el README deberá resumir y enlazar.

Ejemplo:

```text
README-ARCHITECTURE
        ↓
DOC-ARCHITECTURE
```

No deberá mantenerse la misma documentación detallada en ambos lugares.

---

# 66. Relationship with Repository Templates

Los Repository Templates determinan qué README Components forman parte de la composición inicial para un tipo de proyecto.

Modelo:

```text
Project Type
        ↓
Repository Template
        ↓
README Component Composition
        ↓
Consumer
```

Cada Repository Template podrá clasificar los README Components como:

```text
Required
Recommended
Optional
```

El requirement level pertenece al Template.

No deberá añadirse como propiedad universal del README Component.

---

# 67. Relationship with Maturity

La madurez del repositorio puede modificar las expectativas sobre profundidad, calidad y mantenimiento de un README.

No determina automáticamente qué README Components deben existir.

El modelo correcto es:

```text
Project Type
        ↓
Repository Template
        ↓
README Component Composition
        +
Maturity Expectations
```

Dos repositorios con la misma madurez podrán utilizar README Components diferentes.

Dos repositorios del mismo tipo podrán presentar diferente profundidad documental según su estado de evolución, siempre que respeten el contrato aplicable.

---

# 68. README Materialization

Un README Component implementado deberá seguir el contrato general definido por el RDS:

```text
Specification
        +
Metadata
        +
Reusable materialization when required
```

La forma concreta de materialización dependerá de la responsabilidad.

Podrá consistir, por ejemplo, en:

- estructura reutilizable;
- template;
- guidance de composición;
- contenido parametrizable;
- combinación de estos mecanismos.

La existencia de una sección equivalente en un README consumidor no implica por sí sola que exista una implementación canónica del Component dentro del Framework.

---

# 69. README Consumer Adaptation

Los consumidores podrán adaptar los README Components cuando sea necesario para representar correctamente su proyecto.

La adaptación podrá afectar, según corresponda, a:

- contenido;
- ejemplos;
- enlaces;
- parámetros;
- nivel de detalle;
- orden de presentación.

La adaptación no deberá:

- cambiar la responsabilidad canónica;
- introducir contradicciones con otras fuentes;
- duplicar innecesariamente documentación;
- convertir un Component en una responsabilidad diferente.

Cuando una adaptación recurrente revele una necesidad generalizable, deberá evaluarse si corresponde evolucionar el Component o introducir una nueva responsabilidad.

---

# 70. README Anti-Patterns

No utilizar:

- README innecesariamente extensos;
- secciones vacías;
- tecnologías repetidas;
- duplicación de información mantenida canónicamente en `docs/`;
- GIF puramente decorativos;
- badges sin significado;
- Components incorporados sin necesidad;
- requirement levels definidos globalmente fuera de Repository Templates;
- orden rígido cuando no responda a la experiencia de lectura;
- Components utilizados para responsabilidades distintas de su contrato;
- contenido placeholder presentado como documentación final;
- copias de documentación canónica que puedan divergir.

---

# 71. README Quality Gates

Antes de aprobar un README deberá verificarse:

- [ ] El propósito del proyecto puede comprenderse rápidamente.
- [ ] Los Required README Components del Repository Template están correctamente materializados.
- [ ] Los Components adicionales responden a necesidades reales.
- [ ] No existen secciones vacías o redundantes.
- [ ] Funcionalidades y tecnologías están diferenciadas cuando corresponda.
- [ ] La navegación hacia documentación es coherente cuando exista documentación adicional.
- [ ] Las instrucciones de uso son suficientes para el tipo de proyecto.
- [ ] Los enlaces son válidos.
- [ ] La composición mantiene coherencia con el resto del repositorio.
- [ ] No se duplica innecesariamente información canónica mantenida en otros documentos.
- [ ] Las adaptaciones preservan la responsabilidad de los Components utilizados.
- [ ] El README refleja el estado real del proyecto.

---

# 72. Long-Term Vision

La README Component Library permitirá construir README reutilizando responsabilidades estandarizadas y validadas.

Los Repository Templates proporcionarán composiciones iniciales adecuadas a diferentes tipos de proyecto.

Cada Component podrá evolucionar independientemente dentro de su contrato y política de compatibilidad.

Con el tiempo, las Specifications y Metadata podrán permitir generación asistida de README a partir de Repository Templates y parámetros del proyecto.

La automatización deberá consumir las fuentes canónicas existentes y no sustituirlas.

---

# 73. Part 2 Conclusions

La **README Component Library** convierte el README en un sistema modular de responsabilidades reutilizables.

Cada README Component dispone, cuando está implementado, de una definición canónica conforme al contrato general del RDS.

Los Repository Templates determinan contextualmente qué Components son:

```text
Required
Recommended
Optional
```

La materialización final permanece adaptada al proyecto consumidor.

Por tanto, la biblioteca no define un README universal.

Proporciona responsabilidades reutilizables que permiten construir README coherentes, mantenibles y adecuados al tipo real de proyecto.

---

# 74. Part 2 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.

---

# 08 - REPOSITORY DESIGN SYSTEM

# Part 3/7

# Documentation Component Library

---

# 75. Purpose

La **Documentation Component Library (DCL)** define responsabilidades documentales reutilizables reconocidas por GitHub Framework.

Mientras la README Component Library está orientada principalmente a la presentación, comprensión inicial y navegación del proyecto, la DCL proporciona Components para documentación:

- técnica;
- operativa;
- arquitectónica;
- de gobierno;
- de referencia.

Los Repository Templates podrán reutilizar estos Components cuando resulten adecuados para el tipo de proyecto.

La existencia de un Documentation Component en el RDS no implica necesariamente que disponga de una implementación canónica disponible dentro del Framework.

El objetivo de la DCL consiste en evitar que responsabilidades documentales recurrentes deban diseñarse nuevamente desde cero sin imponer un sistema documental idéntico a todos los repositorios.

---

# 76. Documentation Philosophy

La documentación forma parte del producto cuando resulta necesaria para comprender, utilizar, mantener o evolucionar un proyecto.

Cada documento deberá responder a una necesidad concreta.

No deberá existir documentación únicamente para aumentar cobertura o aparentar madurez.

Cuando una responsabilidad documental sea reutilizable y esté reconocida por GitHub Framework, deberá evaluarse la reutilización del Documentation Component correspondiente.

Las necesidades específicas de un proyecto que no justifiquen generalización podrán permanecer como documentación propia del consumidor.

La documentación deberá:

- mantener una fuente canónica identificable;
- evitar duplicaciones innecesarias;
- reflejar razonablemente el estado actual del proyecto;
- evolucionar junto con las responsabilidades que documenta.

---

# 77. Documentation Architecture

La documentación de un repositorio podrá organizarse mediante diferentes responsabilidades según su tipo y necesidades.

Modelo conceptual:

```text
README
        ↓
Project Documentation
        ├── Architecture
        ├── Engineering
        ├── Governance
        └── Reference
```

El README actúa como punto de entrada cuando corresponde.

La estructura concreta deberá derivarse del Repository Template y de las necesidades reales del proyecto.

No todos los repositorios necesitarán todas las áreas documentales.

Tampoco deberán organizarlas físicamente de la misma forma.

La arquitectura documental prioriza responsabilidades sobre estructuras rígidas.

---

# 78. Documentation Layers

La documentación puede analizarse mediante diferentes capas funcionales.

| Layer | Purpose |
| --- | --- |
| Entry | Primera toma de contacto y navegación |
| Functional | Explicación del funcionamiento |
| Technical | Arquitectura e implementación |
| Governance | Gestión y evolución |
| Reference | Información de consulta |

Estas capas proporcionan un modelo conceptual para separar responsabilidades.

Un Documentation Component podrá relacionarse con una o varias capas cuando su responsabilidad lo justifique.

Las capas no determinan:

- requirement levels;
- estructura física;
- estado de implementación;
- obligatoriedad universal.

---

# 79. Documentation Component Classification

Los Documentation Components se clasifican principalmente por la responsabilidad documental que representan.

Podrán relacionarse conceptualmente con áreas como:

- architecture;
- engineering;
- governance;
- reference.

Estas categorías facilitan descubrimiento y organización.

No determinan si un Component es obligatorio.

La necesidad de cada Documentation Component se establece contextualmente mediante el Repository Template correspondiente.

```text
Documentation Component
        ↓
Canonical Responsibility

Repository Template
        ↓
Required / Recommended / Optional
```

La clasificación funcional, la prioridad, la madurez, la disponibilidad y el requirement level son dimensiones diferentes.

No deberán confundirse.

---

# 80. Documentation Component Canonical Definition

Un Documentation Component `Implemented` deberá seguir el contrato general del RDS:

```text
Specification
        +
Metadata
        +
Materialization when required
```

En esta familia, la materialización podrá consistir principalmente en:

- estructura documental reusable;
- `template.md`;
- guidance;
- ejemplos;
- metadata;
- reglas de adopción;
- combinaciones de estos elementos.

La definición canónica deberá mantenerse dentro de:

```text
framework/components/documentation/
```

cuando exista implementación material.

La mera existencia de un documento equivalente en un repositorio consumidor no implica que el Framework Component esté implementado.

---

# 81. DOC-ARCHITECTURE

## Identifier

```text
DOC-ARCHITECTURE
```

## Purpose

Describir la arquitectura general del proyecto.

## Typical Responsibilities

Podrá incluir:

- visión general;
- módulos;
- capas;
- relaciones;
- diagramas;
- dependencias relevantes;
- decisiones arquitectónicas principales.

Cuando existan ADR, deberán complementar la arquitectura y no sustituirla.

---

# 82. DOC-ADR

## Identifier

```text
DOC-ADR
```

## Purpose

Registrar decisiones arquitectónicas relevantes.

## Typical Structure

```text
Context
        ↓
Decision
        ↓
Consequences
```

Los ADR deberán utilizarse para decisiones que merezcan trazabilidad.

No deberán emplearse para registrar decisiones triviales o temporales sin impacto arquitectónico relevante.

---

# 83. DOC-ROADMAP

## Identifier

```text
DOC-ROADMAP
```

## Purpose

Mostrar la evolución prevista del proyecto.

## Possible Horizons

```text
Current
Next Release
Future
Long Term
```

El Roadmap deberá representar dirección y prioridades.

No deberá convertirse en una copia del Product Backlog.

---

# 84. DOC-PROJECT-STATUS

## Identifier

```text
DOC-PROJECT-STATUS
```

## Purpose

Reflejar el estado operativo actual del proyecto.

## Possible Information

Podrá incluir:

- versión actual;
- fase;
- Sprint;
- capacidades implementadas;
- riesgos;
- próximos objetivos;
- estado de release;
- decisiones recientes relevantes.

El documento deberá representar el presente.

No deberá utilizarse como historial detallado del proyecto.

---

# 85. DOC-KNOWN-ISSUES

## Identifier

```text
DOC-KNOWN-ISSUES
```

## Purpose

Registrar limitaciones, problemas o restricciones conocidas que resulte útil mantener visibles.

## Implementation Status

Responsabilidad documental reconocida por el RDS.

No dispone actualmente de una implementación canónica dentro de:

```text
framework/components/documentation/
```

Por tanto, permanece:

```text
Conceptual
```

Su incorporación futura como Framework Component requerirá:

- Specification;
- Metadata;
- materialización cuando corresponda;
- validación conforme al lifecycle del RDS.

## Principle

Las limitaciones relevantes no deberán ocultarse.

La transparencia forma parte de la calidad técnica.

---

# 86. DOC-CHANGELOG

## Identifier

```text
DOC-CHANGELOG
```

## Purpose

Mantener el historial funcional de cambios relevantes del proyecto.

## Preferred Model

Podrá seguir convenciones compatibles con:

```text
Keep a Changelog
+
Semantic Versioning
```

cuando el proyecto utilice releases versionadas.

El Changelog no deberá sustituir el historial Git ni convertirse en una lista de commits.

---

# 87. DOC-RELEASE-NOTES

## Identifier

```text
DOC-RELEASE-NOTES
```

## Purpose

Comunicar los cambios relevantes de una release concreta.

No sustituye al Changelog.

Mientras el Changelog mantiene una visión acumulativa:

```text
CHANGELOG
        ↓
Version history
```

las Release Notes describen una versión determinada:

```text
Release
        ↓
Highlights / Changes / Migration / Known Issues
```

## Implementation Status

Responsabilidad documental reconocida por el RDS.

No dispone actualmente de una implementación canónica dentro de:

```text
framework/components/documentation/
```

Por tanto, permanece `Conceptual`.

---

# 88. DOC-API

## Identifier

```text
DOC-API
```

## Purpose

Documentar interfaces públicas consumibles por otros sistemas o desarrolladores.

## Possible Formats

Podrá materializarse mediante:

- OpenAPI;
- Markdown;
- Javadoc;
- generated documentation;
- otros formatos adecuados al proyecto.

La forma concreta dependerá del tipo de interfaz.

---

# 89. DOC-DATABASE

## Identifier

```text
DOC-DATABASE
```

## Purpose

Documentar el modelo de datos cuando resulte relevante para comprender o mantener el proyecto.

## Possible Contents

Podrá incluir:

- entidades;
- relaciones;
- restricciones;
- diagramas ER;
- convenciones;
- migraciones;
- decisiones importantes del modelo.

No deberá duplicar automáticamente esquemas generados o documentación que pueda obtenerse directamente de otra fuente canónica.

---

# 90. DOC-DEPLOYMENT

## Identifier

```text
DOC-DEPLOYMENT
```

## Purpose

Explicar cómo desplegar o publicar el sistema cuando exista una responsabilidad de deployment.

## Possible Sections

Podrá incluir:

- requisitos;
- infraestructura;
- variables;
- secretos;
- Docker;
- Kubernetes;
- entornos;
- comandos;
- rollback;
- validación posterior.

El nivel de detalle deberá ser proporcional al modelo de despliegue real.

---

# 91. DOC-TESTING

## Identifier

```text
DOC-TESTING
```

## Purpose

Explicar la estrategia de testing y validación técnica del proyecto.

## Possible Contents

Podrá incluir:

- unit tests;
- integration tests;
- end-to-end tests;
- fixtures;
- coverage;
- quality gates;
- CI;
- comandos de ejecución.

El documento deberá explicar la estrategia.

No deberá convertirse únicamente en una lista de herramientas.

---

# 92. DOC-SECURITY

## Identifier

```text
DOC-SECURITY
```

## Purpose

Documentar aspectos de seguridad relevantes para comprender, utilizar o mantener el proyecto.

## Possible Contents

Podrá incluir:

- autenticación;
- autorización;
- secretos;
- configuración;
- threat considerations;
- vulnerabilidades conocidas;
- reporting;
- dependencias;
- prácticas seguras.

Cuando exista una política pública de reporte de vulnerabilidades, podrá relacionarse con un artefacto especializado como `SECURITY.md`.

---

# 93. DOC-DIAGRAMS

## Identifier

```text
DOC-DIAGRAMS
```

## Purpose

Centralizar o gobernar representaciones visuales técnicas cuando exista suficiente volumen o necesidad de reutilización.

## Preferred Formats

Se priorizarán formatos:

- versionables;
- reproducibles;
- abiertos;
- mantenibles.

Ejemplos:

```text
Mermaid
PlantUML
SVG
```

Se evitarán diagramas editables únicamente mediante herramientas cerradas cuando no exista una representación versionable equivalente.

---

# 94. DOC-GLOSSARY

## Identifier

```text
DOC-GLOSSARY
```

## Purpose

Definir terminología relevante para comprender el dominio, arquitectura o funcionamiento del proyecto.

Resulta especialmente útil cuando:

- existe terminología específica;
- aparecen siglas no evidentes;
- diferentes actores podrían interpretar conceptos de forma distinta;
- el proyecto representa un dominio complejo.

No deberá convertirse en un diccionario genérico de términos técnicos.

---

# 95. DOC-REFERENCES

## Identifier

```text
DOC-REFERENCES
```

## Purpose

Centralizar fuentes y referencias externas relevantes para comprender o mantener el proyecto.

## Possible Targets

Podrá incluir:

- documentación externa;
- estándares;
- RFC;
- papers;
- especificaciones;
- APIs externas;
- fuentes normativas;
- documentación de terceros.

Cada referencia deberá aportar contexto suficiente para comprender su relevancia.

---

# 96. Documentation Component Catalog

La Documentation Component Library reconoce actualmente las siguientes responsabilidades:

| Component | Identifier | Responsibility |
| --- | --- | --- |
| Architecture | `DOC-ARCHITECTURE` | Arquitectura general |
| ADR | `DOC-ADR` | Decisiones arquitectónicas |
| Roadmap | `DOC-ROADMAP` | Evolución prevista |
| Project Status | `DOC-PROJECT-STATUS` | Estado operativo |
| Known Issues | `DOC-KNOWN-ISSUES` | Limitaciones conocidas |
| Changelog | `DOC-CHANGELOG` | Historial funcional |
| Release Notes | `DOC-RELEASE-NOTES` | Comunicación de releases |
| API | `DOC-API` | Interfaces públicas |
| Database | `DOC-DATABASE` | Modelo de datos |
| Deployment | `DOC-DEPLOYMENT` | Despliegue |
| Testing | `DOC-TESTING` | Estrategia de calidad |
| Security | `DOC-SECURITY` | Seguridad |
| Diagrams | `DOC-DIAGRAMS` | Representaciones técnicas |
| Glossary | `DOC-GLOSSARY` | Terminología |
| References | `DOC-REFERENCES` | Fuentes y referencias |

Esta tabla representa la taxonomía arquitectónica de la familia.

El estado real de implementación deberá consultarse en:

```text
Component Catalog
        +
Canonical Component Definition
```

cuando exista.

La DCL no deberá convertirse en una segunda fuente de estado o metadata.

---

# 97. Documentation Implementation Model

Los Documentation Components podrán encontrarse en diferentes estados de implementación.

Modelo conceptual:

```text
Recognized Responsibility
        ↓
Conceptual
        ↓
Specification
        ↓
Metadata
        ↓
Reusable Materialization
        ↓
Implemented
        ↓
Validation
```

La creación de un documento en un repositorio consumidor no cambia automáticamente la clasificación del Framework Component.

Para evolucionar a `Implemented`, deberá existir una representación canónica reutilizable dentro del Framework.

---

# 98. Navigation Principles

La documentación deberá permitir al lector:

- comprender su contexto;
- localizar información relacionada;
- identificar fuentes canónicas;
- profundizar cuando sea necesario.

Según el tipo de documento podrán utilizarse:

- enlaces hacia documentación de nivel superior;
- enlaces hacia información especializada;
- documentos relacionados;
- índices;
- navegación desde el README;
- referencias cruzadas.

La navegación bidireccional se utilizará cuando aporte valor.

No será necesario introducir enlaces artificiales únicamente para satisfacer una estructura uniforme.

---

# 99. Documentation Hierarchy

Los documentos deberán mantener responsabilidades diferenciadas y evitar duplicar información canónica.

Cuando exista una relación de profundización podrá utilizarse un modelo como:

```text
README
        ↓
Architecture Summary
        ↓
DOC-ARCHITECTURE
        ↓
DOC-ADR
```

El nivel superior resume y orienta.

El nivel especializado desarrolla el detalle correspondiente.

Las referencias podrán ser bidireccionales cuando mejoren la navegación.

El contenido canónico deberá permanecer en el artefacto responsable de esa información.

---

# 100. Cross References

Las referencias internas entre archivos del repositorio utilizarán preferentemente enlaces relativos.

Esto facilita:

- forks;
- branches;
- reorganizaciones;
- reutilización de Templates;
- consumo local;
- mantenimiento.

Las referencias hacia recursos externos utilizarán la URL correspondiente.

Los enlaces deberán apuntar a la fuente canónica siempre que sea posible.

---

# 101. Document Metadata

Los Documentation Components podrán definir metadata cuando sea necesaria para su mantenimiento y gobernanza.

Entre los campos habituales podrán encontrarse:

- título;
- versión;
- estado;
- owner;
- fecha;
- historial;
- scope;
- relaciones.

La metadata requerida dependerá de la responsabilidad del Component.

No todos los documentos necesitarán necesariamente el mismo bloque de metadata.

Cuando exista una Specification canónica del Component, esta determinará los campos aplicables.

La metadata del documento consumidor no deberá confundirse con la Metadata canónica del Framework Component.

---

# 102. Documentation Materialization

Un Documentation Component podrá materializarse de diferentes formas según su responsabilidad.

Ejemplos:

```text
DOC-CHANGELOG
        ↓
CHANGELOG.md

DOC-ADR
        ↓
ADR structure / template

DOC-API
        ↓
OpenAPI / Markdown / generated reference

DOC-DIAGRAMS
        ↓
Diagram governance + reusable conventions
```

La arquitectura no exige una correspondencia universal:

```text
1 Component
=
1 fixed filename
```

salvo cuando la Specification del Component establezca explícitamente esa restricción.

La responsabilidad deberá prevalecer sobre una estructura física artificial.

---

# 103. Documentation Consumer Adaptation

Los repositorios consumidores podrán adaptar un Documentation Component dentro de los límites de su responsabilidad.

La adaptación podrá afectar a:

- profundidad;
- organización;
- ejemplos;
- nomenclatura contextual;
- formato;
- navegación;
- información específica del proyecto.

La adaptación no deberá:

- cambiar la responsabilidad fundamental;
- eliminar información necesaria para satisfacer el contrato;
- crear contradicciones con otras fuentes canónicas;
- convertir el documento en una copia de otro Component.

Cuando aparezca una necesidad recurrente que exceda el contrato actual, deberá evaluarse una evolución del Component.

---

# 104. Relationship with README Components

README y Documentation Components deberán cooperar sin duplicar responsabilidades.

Modelo habitual:

```text
README Component
        ↓
Summary / Navigation
        ↓
Documentation Component
        ↓
Detailed Content
```

Ejemplos:

```text
README-ARCHITECTURE
        ↓
DOC-ARCHITECTURE
```

```text
README-ROADMAP
        ↓
DOC-ROADMAP
```

```text
README-TESTING
        ↓
DOC-TESTING
```

Estas relaciones deberán utilizarse cuando mejoren navegación y claridad.

No constituyen dependencias universales.

---

# 105. Relationship with Repository Templates

La composición de Documentation Components pertenece a los Repository Templates.

Un Template podrá seleccionar diferentes responsabilidades documentales según el tipo de proyecto.

Modelo:

```text
Project Type
        ↓
Repository Template
        ↓
Documentation Component Composition
        ↓
Required / Recommended / Optional
```

La DCL no deberá mantener una matriz universal de documentos.

La composición canónica deberá consultarse siempre en el Repository Template correspondiente.

---

# 106. Relationship with Maturity

Los Maturity Profiles podrán incrementar las expectativas de:

- profundidad;
- mantenimiento;
- trazabilidad;
- gobernanza;
- calidad documental.

No constituyen una matriz universal de Documentation Components.

Por tanto:

```text
Same maturity
≠
Same documentation
```

Dos repositorios con la misma madurez podrán necesitar sistemas documentales diferentes.

La madurez modifica expectativas.

El Repository Template define composición.

---

# 107. Documentation Dependencies

Los Documentation Components podrán mantener dependencias cuando una responsabilidad necesite realmente otra capacidad.

Ejemplo conceptual:

```text
DOC-API
        ↓ may require context from
DOC-SECURITY
```

solo cuando la relación sea necesaria para satisfacer correctamente el contrato.

Las relaciones habituales o de navegación no deberán convertirse automáticamente en dependencias.

Las dependencias reales deberán mantenerse en la definición canónica cuando exista implementación.

---

# 108. Callout Standards

Cuando la documentación utilice callouts en Markdown de GitHub se priorizarán los mecanismos nativos soportados por la plataforma.

Ejemplos:

```markdown
> [!NOTE]

> [!TIP]

> [!IMPORTANT]

> [!WARNING]

> [!CAUTION]
```

No deberán crearse estilos personalizados sin una necesidad demostrada.

Las reglas detalladas de escritura pertenecen a los Documentation Writing Standards.

---

# 109. Diagram Principles

Los diagramas deberán:

- mantenerse junto al proyecto o en una fuente controlada;
- ser reproducibles cuando sea posible;
- utilizar formatos abiertos o versionables;
- actualizarse junto con la documentación;
- responder a una necesidad de comprensión;
- evitar complejidad visual innecesaria.

Las reglas detalladas de representación podrán pertenecer al Visual Design System o a Components especializados.

---

# 110. Documentation Anti-Patterns

No utilizar:

- documentación duplicada;
- diagramas sin mantener;
- ADR para decisiones triviales;
- enlaces rotos;
- documentos huérfanos sin justificación;
- mezclas innecesarias de idiomas dentro de un mismo artefacto;
- referencias externas sin contexto;
- Documentation Components incorporados sin necesidad;
- requirement levels definidos globalmente fuera de Repository Templates;
- documentación creada únicamente para aumentar cobertura;
- definiciones paralelas de una misma responsabilidad documental;
- documentos placeholder presentados como implementación completa;
- estructuras físicas rígidas sin necesidad;
- contenido desactualizado mantenido únicamente por compatibilidad visual.

---

# 111. Documentation Quality Gates

Antes de aprobar el sistema documental de un repositorio deberá verificarse, según corresponda:

- [ ] Los Required Documentation Components del Repository Template están correctamente materializados.
- [ ] Cada documento responde a una responsabilidad identificable.
- [ ] Los Components adicionales responden a necesidades reales.
- [ ] No existe duplicación innecesaria de información canónica.
- [ ] La navegación permite localizar la información relevante.
- [ ] Los enlaces internos y externos son válidos.
- [ ] La metadata requerida por los Components aplicables está presente.
- [ ] Los diagramas existentes están actualizados y son mantenibles.
- [ ] No existen documentos obsoletos o huérfanos sin justificación.
- [ ] La documentación refleja razonablemente el estado actual del proyecto.
- [ ] Las adaptaciones del consumidor preservan la responsabilidad de los Components.
- [ ] Las fuentes canónicas pueden identificarse.

---

# 112. Long-Term Vision

La Documentation Component Library permitirá construir sistemas documentales reutilizando responsabilidades estandarizadas y validadas.

Los Repository Templates proporcionarán composiciones adecuadas a diferentes tipos de proyecto.

Los repositorios podrán compartir:

- responsabilidades;
- convenciones;
- patrones de navegación;
- estructuras reutilizables;
- metadata;

sin necesitar una estructura documental idéntica.

Con el tiempo, las Specifications y Metadata podrán permitir:

- resolución automática de Documentation Components;
- generación asistida;
- validación de conformidad;
- detección de documentación obsoleta;
- análisis de navegación;
- comprobación de referencias.

La automatización deberá consumir las fuentes canónicas existentes y no sustituirlas.

---

# 113. Part 3 Conclusions

La **Documentation Component Library** convierte responsabilidades documentales recurrentes en elementos reutilizables del Framework.

Cada Documentation Component representa una responsabilidad definida.

Cuando existe implementación, su definición canónica sigue el contrato general:

```text
Specification
        +
Metadata
        +
Materialization when required
```

El RDS podrá reconocer responsabilidades conceptuales pendientes de implementación siempre que su clasificación quede claramente diferenciada.

Los Repository Templates determinan contextualmente qué Documentation Components son:

```text
Required
Recommended
Optional
```

La madurez modifica expectativas de profundidad y mantenimiento.

No determina una composición universal.

Por tanto, la DCL proporciona responsabilidades reutilizables para construir documentación:

- coherente;
- mantenible;
- navegable;
- verificable;
- adaptada a las necesidades reales del proyecto.

---

# 114. Part 3 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.

---

# 08 - REPOSITORY DESIGN SYSTEM

# Part 4/7

# Workflow Component Library

---

# 115. Purpose

La **Workflow Component Library (WCL)** define responsabilidades operativas reutilizables relacionadas con:

- planificación;
- desarrollo;
- validación;
- integración;
- publicación;
- mantenimiento;
- evolución de repositorios.

Los Workflow Components permiten reutilizar prácticas, procesos, configuraciones y automatizaciones cuando resultan adecuados para el tipo de proyecto y su contexto operativo.

Los Repository Templates podrán incorporar estos Components mediante requirement levels contextuales.

El objetivo consiste en proporcionar capacidades operativas reutilizables sin imponer un workflow universal a todos los repositorios.

Diferentes proyectos podrán utilizar composiciones operativas diferentes incluso cuando compartan tipo de proyecto o nivel de madurez.

---

# 116. Workflow Philosophy

Un workflow deberá responder a una necesidad operativa identificable.

Deberá favorecer, según corresponda:

- claridad;
- reproducibilidad;
- reducción de errores;
- trazabilidad;
- mantenibilidad;
- colaboración;
- automatización útil;
- observabilidad;
- seguridad.

Los procesos deberán ayudar al desarrollo y mantenimiento del proyecto.

No deberán incorporarse únicamente para reproducir prácticas habituales de otros repositorios.

La complejidad del workflow deberá ser proporcional a las necesidades reales del consumidor.

La automatización constituye un mecanismo posible de materialización.

No constituye la definición completa de un Workflow Component.

---

# 117. Workflow Responsibility Model

Cada Workflow Component representa una responsabilidad operativa reutilizable.

Ejemplos:

```text
WCL-ISSUE
        ↓
Work intake and issue structure

WCL-PULL-REQUEST
        ↓
Change integration and review context

WCL-CI
        ↓
Automated integration validation

WCL-RELEASE
        ↓
Version publication process
```

La responsabilidad deberá permanecer independiente de una implementación concreta siempre que sea razonable.

Por ejemplo:

```text
WCL-CI
        ≠
specific ci.yml file
```

El archivo concreto constituye una posible materialización.

El Component representa la responsabilidad reusable que dicha materialización implementa.

---

# 118. Workflow Layers

Los Workflow Components podrán analizarse mediante diferentes capas funcionales.

```text
Planning
        ↓
Development
        ↓
Validation
        ↓
Release
        ↓
Maintenance
```

Estas capas proporcionan un modelo conceptual para organizar responsabilidades operativas.

Un Workflow Component podrá relacionarse con una o varias capas cuando su responsabilidad lo justifique.

Las capas no determinan:

- requirement levels;
- dependencias;
- estado de implementación;
- mecanismo de materialización;
- secuencia universal.

---

# 119. Workflow Classification

Los Workflow Components podrán relacionarse con diferentes áreas operativas:

| Area | Purpose |
| --- | --- |
| Planning | Organización y entrada de trabajo |
| Development | Desarrollo e integración de cambios |
| Validation | Revisión y comprobación de calidad |
| Release | Versionado y publicación |
| Maintenance | Evolución posterior y mantenimiento |

Estas áreas facilitan clasificación y descubrimiento.

No determinan si un Workflow Component es obligatorio.

La necesidad del Component se establece contextualmente mediante:

```text
Repository Template
+
Project Needs
```

La clasificación funcional, la prioridad, la madurez, la disponibilidad y el requirement level son dimensiones diferentes.

---

# 120. Workflow Component Canonical Definition

Un Workflow Component `Implemented` deberá disponer de una definición canónica formada por:

```text
Workflow Component
    │
    ├── Specification
    ├── Metadata
    └── Materialization
            when required
```

La Specification define la responsabilidad y el contrato humano.

La Metadata proporciona la representación estructurada.

La Materialization proporciona la capacidad operativa reutilizable cuando la responsabilidad no puede satisfacerse únicamente mediante Specification y Metadata.

La definición canónica deberá permitir distinguir claramente:

```text
Responsibility
        ≠
Specification
        ≠
Materialization
        ≠
Consumer configuration
```

---

# 121. Workflow Specification

La Specification de un Workflow Component deberá describir, según corresponda:

- propósito;
- responsabilidad;
- alcance;
- límites;
- consumidores;
- triggers;
- inputs;
- outputs;
- precondiciones;
- comportamiento esperado;
- dependencias;
- approval points;
- configuración;
- observabilidad;
- security considerations;
- adopción;
- validación.

No todos estos elementos serán necesarios para todos los Workflow Components.

La Specification deberá mantenerse proporcional a la responsabilidad.

No deberá convertirse en una descripción detallada de una implementación específica de GitHub Framework.

---

# 122. Workflow Metadata

La Metadata de un Workflow Component deberá proporcionar información estructurada suficiente para:

- identidad;
- familia;
- versionado;
- lifecycle;
- prioridad;
- audiencia;
- madurez;
- dependencias;
- clasificación;
- descubrimiento;
- automatización futura.

Podrá incorporar información adicional cuando una necesidad real lo justifique.

La Metadata no deberá duplicar:

- instrucciones extensas;
- lógica ejecutable;
- documentación normativa;
- configuración específica de consumidores.

---

# 123. Workflow Materialization Model

La materialización de un Workflow Component depende de la naturaleza de su responsabilidad.

No todos los Workflow Components se implementarán mediante GitHub Actions.

Modelo conceptual:

```text
Workflow Component
        │
        ├── Specification
        ├── Metadata
        │
        └── Materialization
                ├── Community File
                ├── Configuration
                ├── Executable Workflow
                ├── Convention
                ├── Composite Materialization
                └── Other validated mechanism
```

La arquitectura deberá favorecer la materialización mínima suficiente para satisfacer la responsabilidad.

No deberá imponerse simetría física entre Components heterogéneos.

---

# 124. Materialization Types

Los Workflow Components podrán materializarse mediante diferentes tipos.

## Community File

Artefactos nativos o convencionales de GitHub utilizados para estructurar interacción o colaboración.

Ejemplos:

```text
.github/ISSUE_TEMPLATE/
.github/PULL_REQUEST_TEMPLATE.md
```

## Configuration

Archivos de configuración que gobiernan comportamiento o capacidades del repositorio.

Ejemplos conceptuales:

```text
dependabot.yml
label configuration
repository settings representation
```

## Executable Workflow

Automatización ejecutable mediante una plataforma como GitHub Actions.

Ejemplo:

```text
.github/workflows/ci.yml
```

## Convention

Regla formalizada que representa un comportamiento reutilizable sin requerir necesariamente ejecución automática.

Ejemplos:

```text
branch naming
commit convention
release procedure
```

## Composite Materialization

Combinación de varios mecanismos cuando una única forma no resulte suficiente.

Ejemplo conceptual:

```text
WCL-RELEASE
        │
        ├── Release Specification
        ├── Versioning Convention
        ├── CHANGELOG interaction
        └── Optional executable automation
```

Un Component no deberá clasificarse artificialmente dentro de un único tipo si su responsabilidad necesita una composición real.

---

# 125. Executable Workflow Components

Un Workflow Component será ejecutable cuando su responsabilidad incluya comportamiento automático materializado mediante código, configuración ejecutable o automatización.

Ejemplos potenciales:

```text
WCL-CI
WCL-CD
WCL-SECURITY
WCL-DEPENDABOT
```

cuando su implementación utilice mecanismos automáticos.

Los Components ejecutables deberán considerar, cuando corresponda:

- triggers;
- permissions;
- secrets;
- inputs;
- outputs;
- failure behavior;
- retries;
- observability;
- security;
- portability;
- maintenance.

La existencia de código ejecutable implica obligaciones adicionales de calidad y seguridad.

---

# 126. Non-Executable Workflow Components

Algunos Workflow Components podrán representar responsabilidades operativas que no requieren ejecución automática.

Ejemplos:

```text
WCL-BRANCH
WCL-COMMIT
WCL-PULL-REQUEST
```

según su implementación concreta.

Estos Components podrán materializarse mediante:

- convenciones;
- community files;
- templates;
- guidance;
- configuración;
- reglas de proceso.

La ausencia de código ejecutable no implica que el Component sea menos válido.

La arquitectura evalúa si la responsabilidad está suficientemente materializada como capacidad reusable.

---

# 127. Composite Workflow Components

Una responsabilidad operativa podrá requerir diferentes artefactos coordinados.

Ejemplo:

```text
WCL-RELEASE
        │
        ├── Specification
        ├── Metadata
        ├── Versioning rules
        ├── Release checklist
        ├── CHANGELOG interaction
        └── Optional GitHub Actions workflow
```

En estos casos, el Component deberá mantener una única identidad.

No deberán crearse Components separados únicamente porque la responsabilidad se materialice mediante varios artefactos.

La separación solo estará justificada cuando existan responsabilidades independientes y reutilizables.

---

# 128. Materialization Sufficiency

Un Workflow Component no deberá considerarse `Implemented` únicamente porque existan Specification y Metadata si su responsabilidad exige una capacidad material adicional.

Ejemplo:

```text
WCL-CI
        ↓
Specification + Metadata only
        ↓
Insufficient
```

cuando el contrato del Component requiera validación automática reutilizable.

Del mismo modo:

```text
WCL-BRANCH
        ↓
Specification + Metadata + reusable convention
        ↓
Potentially sufficient
```

si la responsabilidad queda correctamente satisfecha sin automatización.

La suficiencia deberá evaluarse sobre la responsabilidad.

No sobre el número de archivos.

---

# 129. Conceptual to Implemented Transition for Workflow Components

Un Workflow Component podrá evolucionar:

```text
Conceptual
        ↓
Implemented
```

cuando exista una representación canónica reutilizable y gobernada suficiente para satisfacer su responsabilidad.

Antes de realizar la transición deberá verificarse:

- [ ] La responsabilidad continúa siendo válida.
- [ ] El identificador `WCL-*` es estable.
- [ ] Existe Specification canónica.
- [ ] Existe Metadata canónica.
- [ ] Se ha identificado el tipo de materialización.
- [ ] La materialización es suficiente para la responsabilidad.
- [ ] Las dependencias reales están declaradas.
- [ ] Los mecanismos específicos del consumidor se han separado del contrato reusable.
- [ ] No se duplica otro Workflow Component.
- [ ] Los security considerations han sido evaluados cuando existe ejecución.
- [ ] Puede reutilizarse fuera de una única implementación accidental.
- [ ] Los Quality Gates aplicables están satisfechos.

La transición no significa que el Component sea `Stable`.

Podrá permanecer en lifecycle `Experimental` mientras se valida mediante Reference Implementation y dogfooding.

---

# 130. Workflow Implementation vs Consumer Practice

La existencia de una práctica operativa en un repositorio consumidor no constituye automáticamente una implementación canónica.

Ejemplo:

```text
GitHub Framework uses Pull Requests
        ≠
WCL-PULL-REQUEST is Implemented
```

Para considerarlo implementado deberá existir una capacidad reutilizable gobernada dentro del Framework.

El flujo correcto es:

```text
Existing practice
        ↓
Analyze
        ↓
Extract reusable responsibility
        ↓
Define canonical Component
        ↓
Materialize
        ↓
Validate through consumer
```

Este principio evita convertir accidentalmente cualquier práctica local en arquitectura del Framework.

---

# 131. Workflow Portability

Los Workflow Components deberán evitar acoplamiento innecesario con un único repositorio consumidor.

Cuando una responsabilidad dependa de GitHub como plataforma, podrá utilizar capacidades específicas de GitHub.

Sin embargo, deberán diferenciarse:

```text
Platform dependency
        ≠
Consumer-specific assumption
```

Ejemplo válido:

```text
WCL-PULL-REQUEST
        ↓
GitHub Pull Request capability
```

Ejemplo problemático:

```text
hard-coded repository name
hard-coded branch belonging to one project
hard-coded maintainer
consumer-specific paths without configuration
```

Los parámetros específicos del consumidor deberán externalizarse o documentarse cuando sea razonable.

---

# 132. Workflow Inputs

Un Workflow Component podrá recibir inputs cuando su comportamiento dependa de configuración contextual.

Ejemplos:

```text
branch name
runtime version
documentation paths
test command
release branch
artifact path
```

Los inputs deberán:

- representar variabilidad legítima;
- evitar valores hard-coded del consumidor;
- mantenerse al mínimo necesario;
- disponer de defaults cuando estos sean realmente generales;
- documentarse cuando afecten a adopción o ejecución.

No deberá parametrizarse arbitrariamente todo comportamiento.

---

# 133. Workflow Outputs

Un Workflow Component podrá producir outputs observables.

Ejemplos:

```text
validation result
build artifact
release artifact
GitHub status
generated report
updated documentation
```

Cuando existan outputs relevantes deberán documentarse.

Los outputs machine-readable podrán facilitar futura composición y automatización.

No deberán introducirse contratos de outputs complejos sin necesidad real.

---

# 134. Workflow Triggers

Los Components ejecutables o event-driven podrán reaccionar a triggers.

Ejemplos:

```text
push
pull_request
workflow_dispatch
release
schedule
repository event
```

Los triggers deberán derivarse de la responsabilidad del Component.

No deberán copiarse de otro workflow sin evaluar el contexto.

La Specification deberá permitir comprender por qué existe cada trigger relevante.

---

# 135. Manual Approval Points

Determinadas decisiones podrán requerir aprobación humana según el riesgo y contexto.

Ejemplos:

- publicar una release;
- desplegar a producción;
- modificar una licencia;
- archivar un repositorio;
- ejecutar una migración;
- promover un artefacto crítico.

Los approval points deberán utilizarse cuando aporten control real.

No deberán introducirse como burocracia universal.

Un Workflow Component podrá combinar automatización con decisión humana.

---

# 136. Workflow Security

Los Workflow Components ejecutables deberán diseñarse aplicando privilegio mínimo.

Cuando corresponda deberá evaluarse:

- permisos;
- secretos;
- tokens;
- actions externas;
- pinning de versiones;
- ejecución sobre forks;
- exposición de información;
- generación o publicación de artefactos;
- acceso de escritura;
- supply chain.

La reutilización no deberá aumentar innecesariamente la superficie de ataque.

Los security considerations específicas deberán documentarse en la Specification o en estándares especializados.

---

# 137. Workflow Observability

Los workflows automatizados deberán producir evidencia suficiente para comprender su ejecución.

Según el Component podrá incluir:

- logs;
- status;
- summaries;
- artifacts;
- annotations;
- failure messages;
- outputs.

Los fallos deberán ser suficientemente comprensibles para permitir diagnóstico razonable.

La observabilidad deberá ser proporcional a la responsabilidad.

---

# 138. Workflow Failure Behavior

Los Components ejecutables deberán definir un comportamiento razonable ante fallos.

Cuando corresponda deberá quedar claro:

- qué constituye fallo;
- si el fallo bloquea integración;
- si permite retry;
- si requiere intervención humana;
- si produce evidencia;
- si puede dejar estado parcial.

No deberá ocultarse un fallo relevante para conseguir pipelines aparentemente verdes.

---

# 139. Workflow Dependencies

Un Workflow Component podrá depender de otro Framework Component cuando esa relación sea necesaria para satisfacer su responsabilidad.

Ejemplo conceptual:

```text
WCL-DOCUMENTATION-UPDATE
        ↓ may depend on
Documentation Components
```

o:

```text
WCL-RELEASE
        ↓ may interact with
DOC-CHANGELOG
```

Estas relaciones deberán analizarse cuidadosamente.

Interacción no implica automáticamente dependencia.

Las dependencias reales deberán:

- declararse;
- justificarse;
- evitar ciclos innecesarios;
- mantenerse mínimas;
- permitir comprender impacto de cambios.

---

# 140. Workflow Relationships

Los Workflow Components podrán participar en secuencias operativas sin que ello implique dependencia estructural.

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

No constituye una cadena obligatoria.

Un consumidor podrá utilizar subconjuntos diferentes.

La arquitectura deberá preservar:

```text
Operational sequence
        ≠
Structural dependency
```

---

# 141. Workflow Composition

Los Workflow Components se combinan mediante necesidades operativas y Repository Templates.

Ejemplo conceptual:

```text
WCL-ISSUE
+
WCL-PULL-REQUEST
+
WCL-CI
+
WCL-RELEASE
        ↓
Repository Template
        ↓
Consumer operational model
```

La composición deberá evitar:

- workflows innecesarios;
- dependencias artificiales;
- automatización sin necesidad;
- duplicación de responsabilidades;
- procesos incompatibles entre sí.

La existencia de un Component implementado no implica que deba incorporarse a todos los Repository Templates.

---

# 142. Repository Template Integration

Los Repository Templates podrán incorporar Workflow Components mediante requirement levels contextuales.

Modelo:

```text
Project Type
        ↓
Repository Template
        ↓
Workflow Component Composition
        ↓
Required / Recommended / Optional
```

Un mismo Workflow Component podrá tener diferentes requirement levels.

Ejemplo conceptual:

```text
WCL-CI
        ├── Required
        ├── Recommended
        ├── Optional
        └── Not selected
```

dependiendo del Template.

El requirement level no deberá mantenerse dentro de la definición canónica del Workflow Component.

---

# 143. Maturity Interaction

Los Maturity Profiles podrán incrementar expectativas sobre:

- automatización;
- trazabilidad;
- revisión;
- seguridad;
- observabilidad;
- mantenimiento.

Sin embargo:

```text
Same maturity
        ≠
Same workflow composition
```

La madurez no determina una matriz universal de Workflow Components.

Un repositorio L3 podrá necesitar CI y no releases formales.

Otro repositorio L3 podrá necesitar releases y no deployment automático.

La composición depende de necesidades reales.

---

# 144. WCL-ISSUE

## Identifier

```text
WCL-ISSUE
```

## Purpose

Representar una unidad estructurada de trabajo o cambio dentro de un repositorio.

## Possible Responsibilities

Podrá incluir:

```text
Context
        ↓
Problem / Objective
        ↓
Expected Result
        ↓
Relevant Information
```

La estructura concreta podrá variar según el tipo de Issue.

## Possible Materialization

Podrá materializarse mediante:

- GitHub Issue Forms;
- Issue templates;
- configuration;
- conventions;
- guidance.

El Component no obliga a utilizar un único formulario universal.

---

# 145. WCL-LABEL

## Identifier

```text
WCL-LABEL
```

## Purpose

Clasificar trabajo y facilitar navegación, filtrado o automatización cuando sea necesario.

## Possible Categories

Podrán existir categorías como:

```text
type
priority
status
area
```

La taxonomía concreta dependerá del consumidor.

## Possible Materialization

Podrá utilizar:

- label specification;
- reusable label set;
- configuration;
- setup guidance;
- future automation.

No todos los consumidores necesitarán el mismo conjunto de labels.

---

# 146. WCL-PROJECT

## Identifier

```text
WCL-PROJECT
```

## Purpose

Organizar trabajo mediante una vista de planificación cuando el repositorio necesite gestión estructurada de backlog o roadmap.

## Possible Views

Ejemplos:

- Backlog;
- Sprint;
- Roadmap;
- Done.

La utilización de GitHub Projects no deberá ser obligatoria para repositorios cuya complejidad no lo justifique.

---

# 147. WCL-BRANCH

## Identifier

```text
WCL-BRANCH
```

## Purpose

Definir una estrategia coherente para organizar ramas cuando el proyecto necesite desarrollo paralelo o aislamiento de cambios.

## Possible Strategies

Podrán utilizarse estrategias como:

```text
main
+
feature/*
```

o:

```text
main
+
develop
+
feature/*
+
release/*
+
hotfix/*
```

También podrán utilizarse otros modelos.

No se impondrá Git Flow como estrategia universal.

## Materialization

Podrá materializarse principalmente mediante:

- convention;
- branch naming rules;
- protection configuration;
- repository guidance.

---

# 148. WCL-COMMIT

## Identifier

```text
WCL-COMMIT
```

## Purpose

Definir una convención consistente para commits.

## Possible Convention

Podrá utilizarse un modelo basado en prefijos como:

```text
feat
fix
docs
test
refactor
build
ci
chore
```

El consumidor podrá establecer:

- idioma;
- scope;
- formato adicional;
- reglas específicas.

## Materialization

Podrá utilizar:

- convention;
- examples;
- commit tooling;
- validation automation;
- configuration.

La automatización de la convención será opcional salvo que el contrato específico determine lo contrario.

---

# 149. WCL-PULL-REQUEST

## Identifier

```text
WCL-PULL-REQUEST
```

## Purpose

Estructurar la integración de cambios y proporcionar contexto suficiente para revisión.

## Typical Responsibilities

Podrá cubrir:

```text
Summary
Changes
Validation
Evidence
Related Issues
```

## Possible Materialization

Podrá utilizar:

- Pull Request template;
- guidance;
- branch integration rules;
- checks;
- metadata or configuration.

La existencia de un PR template no garantiza por sí sola la satisfacción completa del Component.

---

# 150. WCL-CODE-REVIEW

## Identifier

```text
WCL-CODE-REVIEW
```

## Purpose

Definir prácticas reutilizables para revisar cambios antes de su integración.

## Possible Review Areas

Podrá incluir:

- arquitectura;
- naming;
- tests;
- documentación;
- seguridad;
- duplicación;
- complejidad;
- impacto;
- compatibilidad.

## Possible Materialization

Podrá utilizar:

- review guidance;
- checklist;
- CODEOWNERS;
- branch protection;
- approval rules;
- automation complementaria.

La revisión humana no deberá automatizarse artificialmente cuando requiera juicio técnico.

---

# 151. WCL-CI

## Identifier

```text
WCL-CI
```

## Purpose

Validar automáticamente cambios integrables para detectar problemas antes de su incorporación al repositorio principal.

## Typical Responsibilities

Podrá incluir:

```text
Checkout
        ↓
Setup
        ↓
Dependencies
        ↓
Build / Validation
        ↓
Tests
        ↓
Static Checks
        ↓
Result
```

No todos los proyectos necesitarán cada paso.

## Materialization

`WCL-CI` requerirá una capacidad ejecutable reutilizable cuando se considere `Implemented`.

Podrá materializarse mediante:

- GitHub Actions;
- reusable workflows;
- composite actions;
- configuration;
- scripts invocados por el workflow;
- combinaciones de estos mecanismos.

La mera documentación de un proceso CI no será suficiente para considerarlo implementado si el contrato exige ejecución automática.

---

# 152. WCL-CD

## Identifier

```text
WCL-CD
```

## Purpose

Automatizar o estructurar la entrega o despliegue de artefactos cuando el proyecto necesite una capacidad de Continuous Delivery o Deployment.

## Possible Targets

Podrá incluir:

- GitHub Pages;
- package registries;
- container registries;
- cloud environments;
- documentation sites;
- release artifacts.

## Materialization

Su implementación dependerá fuertemente del entorno consumidor.

Por ello deberá evitar acoplamiento innecesario a una única plataforma de deployment salvo que la responsabilidad del Component lo justifique.

---

# 153. WCL-DEPENDABOT

## Identifier

```text
WCL-DEPENDABOT
```

## Purpose

Gestionar actualizaciones automáticas de dependencias cuando aporten valor operativo.

## Possible Materialization

Podrá utilizar:

```text
.github/dependabot.yml
```

junto con guidance y configuración reusable.

## Principles

La frecuencia y configuración deberán adaptarse a:

- ecosistema tecnológico;
- actividad;
- riesgo;
- necesidades de mantenimiento.

Las actualizaciones automáticas no deberán generar ruido operativo innecesario.

---

# 154. WCL-SECURITY

## Identifier

```text
WCL-SECURITY
```

## Purpose

Representar procesos reutilizables de validación o mantenimiento de seguridad.

## Possible Capabilities

Podrá incluir:

- dependency scanning;
- code scanning;
- secret scanning;
- security checks;
- policy validation;
- vulnerability reporting integration.

## Materialization

Podrá combinar:

- GitHub Actions;
- GitHub security configuration;
- community files;
- policies;
- reusable configuration.

El alcance deberá mantenerse claramente delimitado respecto a `DOC-SECURITY`.

---

# 155. WCL-RELEASE

## Identifier

```text
WCL-RELEASE
```

## Purpose

Definir un proceso reproducible para publicar versiones cuando el proyecto mantenga releases formales.

## Possible Responsibilities

Un release podrá implicar:

- versionado;
- changelog;
- tag;
- release notes;
- GitHub Release;
- build de artefactos;
- publicación;
- actualización de estado;
- validación posterior.

No todos estos pasos serán obligatorios.

## Possible Materialization

Podrá combinar:

- release specification;
- checklist;
- versioning convention;
- GitHub Actions;
- scripts;
- templates;
- interactions with Documentation Components.

No todos los repositorios necesitarán releases formales.

---

# 156. WCL-HOTFIX

## Identifier

```text
WCL-HOTFIX
```

## Purpose

Gestionar correcciones urgentes que requieran un tratamiento diferente al flujo ordinario.

## Possible Responsibilities

Podrá incluir:

- aislamiento;
- prioridad;
- validación acelerada;
- integración;
- release;
- sincronización;
- documentación.

## Materialization

Dependerá especialmente de:

```text
WCL-BRANCH
+
WCL-RELEASE
```

cuando existan esas responsabilidades.

La relación no deberá convertirse automáticamente en dependencia obligatoria.

---

# 157. WCL-DOCUMENTATION-UPDATE

## Identifier

```text
WCL-DOCUMENTATION-UPDATE
```

## Purpose

Mantener sincronizada la documentación cuando cambios del repositorio puedan invalidarla.

## Possible Triggers

Podrá reaccionar a:

- cambios de comportamiento;
- cambios arquitectónicos;
- nuevas capacidades;
- releases;
- configuración;
- cambios de metadata;
- cambios que afecten a documentación existente.

## Possible Materialization

Podrá combinar:

- checklist;
- PR validation;
- path-based detection;
- automation;
- metadata validation;
- documentation build;
- manual review points.

La responsabilidad no presupone que toda actualización documental pueda automatizarse.

---

# 158. WCL-ASSESSMENT

## Identifier

```text
WCL-ASSESSMENT
```

## Purpose

Ejecutar una evaluación estructurada del repositorio cuando corresponda.

Podrá incluir GRS Assessment cuando forme parte del modelo de evaluación aplicable.

## Possible Outputs

Podrá producir:

```text
Score
Readiness
Findings
Backlog
Recommendations
```

## Materialization

Podrá combinar:

- checklist;
- assessment specification;
- scripts;
- reports;
- future validators.

La evaluación automática no deberá sustituir criterios cualitativos que requieran juicio.

---

# 159. WCL-MAINTENANCE

## Identifier

```text
WCL-MAINTENANCE
```

## Purpose

Definir un ciclo de mantenimiento reutilizable para repositorios que necesiten revisión periódica.

## Typical Responsibilities

Podrá incluir:

- actualizar dependencias;
- revisar Issues;
- revisar Pull Requests pendientes;
- comprobar enlaces;
- actualizar Roadmap;
- revisar documentación;
- revisar seguridad;
- detectar deuda.

## Materialization

Podrá utilizar:

- schedule;
- checklist;
- Issues recurrentes;
- automation;
- reports;
- manual review process.

No deberá introducir ciclos periódicos sin una necesidad de mantenimiento real.

---

# 160. Workflow Component Catalog

La Workflow Component Library reconoce actualmente:

| Identifier | Responsibility |
| --- | --- |
| `WCL-ISSUE` | Issue management |
| `WCL-LABEL` | Classification |
| `WCL-PROJECT` | Project planning |
| `WCL-BRANCH` | Branch strategy |
| `WCL-COMMIT` | Commit convention |
| `WCL-PULL-REQUEST` | Pull Request integration |
| `WCL-CODE-REVIEW` | Review process |
| `WCL-CI` | Continuous Integration |
| `WCL-CD` | Continuous Delivery / Deployment |
| `WCL-DEPENDABOT` | Dependency updates |
| `WCL-SECURITY` | Security workflow |
| `WCL-RELEASE` | Release management |
| `WCL-HOTFIX` | Urgent correction process |
| `WCL-DOCUMENTATION-UPDATE` | Documentation synchronization |
| `WCL-ASSESSMENT` | Repository assessment |
| `WCL-MAINTENANCE` | Maintenance cycle |

Esta tabla representa la taxonomía arquitectónica.

El Component Catalog mantiene:

- clasificación de implementación;
- prioridad;
- audiencia;
- madurez;
- estado;
- descubrimiento.

La WCL no deberá duplicar esos datos salvo cuando resulten necesarios para explicar arquitectura.

---

# 161. Current Implementation Boundary

La arquitectura Workflow definida por esta Part dispone actualmente de una primera biblioteca Core materializada en:

```text
framework/components/workflow/
```

Los siguientes Workflow Components cuentan con implementación canónica:

```text
WCL-ISSUE
WCL-BRANCH
WCL-COMMIT
WCL-PULL-REQUEST
WCL-CODE-REVIEW
```

Su estado actual es:

```text
Implementation: Implemented
Lifecycle: Experimental
Validation: Reference Implementation Validated
```

Los once Workflow Components restantes permanecen:

```text
Conceptual
```

La clasificación de implementación deberá continuar reflejando la disponibilidad material real del Framework.

La existencia de prácticas equivalentes en GitHub Framework u otros consumidores no convierte automáticamente una responsabilidad conceptual en un Component implementado.

La implementación de nuevos Components pertenece al lifecycle de cada Component y deberá satisfacer el contrato definido por esta Part.

La arquitectura no deberá presentar prematuramente como disponible aquello que todavía no exista materialmente.

---

# 162. Workflow Reference Implementation

Los Workflow Components implementados deberán validarse mediante consumidores representativos cuando resulte necesario.

GitHub Framework ha actuado como primera Reference Implementation de los Core Workflow Components mediante dogfooding.

El proceso deberá distinguir:

```text
Framework Component
        ↓
Canonical reusable capability

Consumer
        ↓
Repository-specific adoption
```

La Reference Implementation deberá permitir detectar:

- gaps de Specification;
- gaps de Metadata;
- materializaciones insuficientes;
- dependencias incorrectas;
- acoplamiento al consumidor;
- problemas de seguridad;
- problemas de mantenibilidad;
- simplificaciones posibles.

Los findings deberán clasificarse antes de modificar arquitectura o Component.

---

# 163. Workflow Conformance

La conformidad de un consumidor se evaluará contra los Workflow Components que realmente le correspondan.

No deberá exigir todos los Components reconocidos por la WCL.

Modelo:

```text
Repository Template
        ↓
Selected Workflow Components
        ↓
Consumer Materialization
        ↓
Conformance Evaluation
```

La evaluación deberá considerar:

- responsabilidad satisfecha;
- configuración;
- ejecución cuando corresponda;
- dependencias;
- evidencia;
- adaptación permitida.

La simple existencia de:

```text
.github/workflows/
```

no implica conformidad con `WCL-CI`.

La evaluación debe comprobar el contrato.

---

# 164. Workflow Quality Attributes

Todo Workflow Component deberá ser, según corresponda:

- claro;
- reproducible;
- reutilizable;
- documentado;
- observable;
- mantenible;
- proporcional a la necesidad;
- suficientemente desacoplado;
- configurable cuando exista variabilidad legítima.

Los Components ejecutables deberán considerar además:

- seguridad;
- confiabilidad;
- behavior ante fallo;
- permisos;
- portabilidad razonable;
- trazabilidad.

---

# 165. Workflow Anti-Patterns

No utilizar:

- procesos duplicados;
- branching models complejos sin necesidad;
- ramas permanentes innecesarias;
- workflows sin mantenimiento;
- Pull Requests innecesariamente grandes;
- releases formales cuando el proyecto no las necesita;
- automatizaciones opacas;
- Components incorporados únicamente por madurez;
- requirement levels definidos globalmente fuera de Repository Templates;
- dependencias artificiales;
- procesos copiados de otro proyecto sin evaluar contexto;
- hard-coded values específicos de un consumidor dentro del contrato reusable;
- Specification sin materialización cuando la responsabilidad exige ejecución;
- GitHub Actions creadas únicamente para aparentar automatización;
- permisos más amplios de lo necesario;
- Components separados únicamente por diferencias menores de configuración;
- secuencias operativas presentadas como dependencias universales;
- prácticas locales presentadas como Components implementados sin definición canónica.

---

# 166. Workflow Component Quality Gates

Antes de promover un Workflow Component a `Implemented` deberá verificarse:

- [ ] El identificador `WCL-*` es único y estable.
- [ ] El propósito está definido.
- [ ] La responsabilidad está claramente delimitada.
- [ ] El alcance y límites están documentados.
- [ ] Existe Specification canónica.
- [ ] Existe Metadata canónica.
- [ ] El mecanismo de materialización está identificado.
- [ ] La materialización es suficiente para satisfacer la responsabilidad.
- [ ] Las dependencias reales están declaradas.
- [ ] No se han introducido dependencias artificiales.
- [ ] La variabilidad legítima puede configurarse cuando corresponde.
- [ ] La implementación no está acoplada innecesariamente a un consumidor.
- [ ] Los triggers están justificados cuando existen.
- [ ] Inputs y outputs relevantes están documentados.
- [ ] El comportamiento ante fallos es comprensible cuando existe ejecución.
- [ ] La observabilidad es suficiente cuando corresponde.
- [ ] Los permisos y security considerations han sido revisados cuando existe ejecución.
- [ ] No duplica otra responsabilidad Workflow.
- [ ] Puede reutilizarse razonablemente.
- [ ] Su clasificación de implementación refleja la realidad.

---

# 167. Workflow Composition Quality Gates

Antes de aprobar una composición de Workflow Components para un consumidor deberá verificarse:

- [ ] Cada Component responde a una necesidad operativa real.
- [ ] Los Required Workflow Components del Repository Template están correctamente materializados.
- [ ] Los Components adicionales aportan valor.
- [ ] No existen procesos duplicados.
- [ ] Las dependencias reales están satisfechas.
- [ ] La automatización está justificada.
- [ ] Los approval points son proporcionales al riesgo.
- [ ] La composición puede mantenerse.
- [ ] Los procesos son observables cuando corresponde.
- [ ] La seguridad ha sido considerada.
- [ ] No se ha utilizado la madurez como matriz automática de composición.
- [ ] La composición refleja las necesidades actuales del proyecto.

---

# 168. Workflow Automation Policy

Toda tarea repetitiva deberá evaluarse para automatización cuando exista:

- repetición suficiente;
- proceso estable;
- beneficio operativo;
- posibilidad razonable de mantenimiento.

Ejemplos:

- testing;
- validación Markdown;
- validación de metadata;
- comprobación de enlaces;
- releases;
- documentación;
- assessment;
- mantenimiento.

La automatización deberá:

- aportar valor;
- ser comprensible;
- mantenerse observable;
- consumir fuentes canónicas;
- evitar duplicar reglas;
- utilizar permisos mínimos.

No se automatizarán decisiones que requieran necesariamente juicio humano.

---

# 169. Long-Term Vision

La Workflow Component Library permitirá construir modelos operativos reutilizando responsabilidades estandarizadas y validadas.

Los Repository Templates podrán proporcionar composiciones adecuadas a distintos tipos de proyecto.

Los repositorios podrán compartir:

- prácticas;
- convenciones;
- community files;
- configuraciones;
- automatizaciones;
- procesos de validación;

sin necesitar exactamente la misma forma de trabajar.

Con el tiempo, Specifications y Metadata podrán permitir:

- resolución automática de Workflow Components;
- configuración asistida;
- validación de dependencias;
- análisis de conformidad;
- generación de workflows;
- detección de drift;
- mantenimiento asistido;
- integración con Framework Automation.

La automatización deberá consumir las fuentes canónicas existentes.

No deberá sustituir el contrato arquitectónico de los Components.

---

# 170. Part 4 Conclusions

La **Workflow Component Library** convierte responsabilidades operativas recurrentes en elementos reutilizables del Framework.

Cada Workflow Component representa una responsabilidad independiente de su materialización concreta.

El contrato general es:

```text
Workflow Component
        │
        ├── Specification
        ├── Metadata
        └── Materialization when required
```

La materialización podrá utilizar:

```text
Community Files
Configuration
Executable Workflows
Conventions
Composite mechanisms
```

según la responsabilidad.

La transición:

```text
Conceptual
        ↓
Implemented
```

requiere una capacidad reutilizable suficiente.

No basta con que una práctica equivalente exista en un repositorio consumidor.

Los Repository Templates determinan contextualmente qué Workflow Components son:

```text
Required
Recommended
Optional
```

Los Maturity Profiles podrán incrementar expectativas operativas.

No definen una composición universal.

Por tanto:

```text
Reusable Workflow Responsibilities
        +
Repository Template
        +
Project Needs
        +
Appropriate Materialization
        ↓
Consumer Operational Model
```

La WCL no pretende que todos los repositorios trabajen de la misma forma.

Pretende evitar que responsabilidades operativas recurrentes deban diseñarse nuevamente desde cero.

---

# 171. Part 4 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.

---

# 08 - REPOSITORY DESIGN SYSTEM

# Part 5/7

# Visual Component Library

---

# 172. Purpose

La **Visual Component Library (VCL)** define responsabilidades visuales reutilizables reconocidas por GitHub Framework.

Su objetivo consiste en facilitar una presentación visual coherente, profesional y mantenible mediante Components reutilizables cuando exista una necesidad visual identificable.

La VCL complementa el **Visual Design System**, pero no lo sustituye.

El Visual Design System define principios, reglas y constraints como:

- color;
- tipografía;
- espaciado;
- accesibilidad;
- compatibilidad visual;
- comportamiento responsive;
- consistencia gráfica.

La Visual Component Library define responsabilidades reutilizables que podrán materializar esas reglas.

Por tanto:

```text
Visual Design System
        ↓
Visual rules and constraints

Visual Component Library
        ↓
Reusable visual responsibilities
```

No todos los proyectos necesitarán Visual Components específicos.

Tampoco deberán compartir exactamente la misma identidad gráfica o composición visual.

---

# 173. Visual Philosophy

Todo Visual Component deberá responder a una necesidad identificable.

Podrá contribuir a:

- facilitar comprensión;
- reforzar identidad;
- mejorar navegación;
- comunicar información;
- representar estructura;
- explicar procesos;
- proporcionar contexto visual.

Los elementos visuales no deberán incorporarse únicamente con fines decorativos.

La complejidad visual deberá ser proporcional al valor que aporta al consumidor.

La coherencia deberá derivarse del Visual Design System y de la responsabilidad del Component.

No deberá conseguirse mediante la repetición obligatoria de los mismos elementos gráficos en todos los repositorios.

---

# 174. Visual Responsibility Model

Cada Visual Component representa una responsabilidad visual reutilizable.

Ejemplos:

```text
VCL-BANNER
        ↓
Repository visual presentation

VCL-BADGES
        ↓
Compact project information

VCL-ARCHITECTURE-DIAGRAM
        ↓
Architecture visualization

VCL-NAVIGATION-CARD
        ↓
Visual navigation
```

La responsabilidad visual deberá permanecer diferenciada de su implementación concreta.

Por ejemplo:

```text
VCL-BANNER
        ≠
specific PNG file
```

El asset concreto constituye una materialización.

El Component representa la responsabilidad reutilizable.

---

# 175. Visual Architecture

La experiencia visual de un repositorio podrá construirse mediante diferentes responsabilidades.

Modelo conceptual:

```text
Visual Experience
        │
        ├── Identity
        ├── Presentation
        ├── Information
        ├── Navigation
        └── Technical Visualization
```

Los Visual Components podrán relacionarse con una o varias de estas áreas.

No existe una secuencia visual universal que todos los repositorios deban implementar.

La composición deberá derivarse de:

```text
Repository Template
+
Consumer Context
+
Visual Design System
+
Project Needs
```

---

# 176. Visual Classification

Los Visual Components podrán relacionarse con diferentes áreas funcionales:

| Area | Purpose |
| --- | --- |
| Identity | Identidad visual del proyecto |
| Presentation | Presentación inicial y comunicación |
| Information | Comunicación visual de información |
| Navigation | Acceso visual a contenidos relacionados |
| Technical Visualization | Representación de arquitectura, estructura o procesos |

Estas áreas facilitan clasificación y descubrimiento.

No determinan:

- requirement levels;
- estado de implementación;
- prioridad;
- madurez;
- estructura física.

Un Visual Component podrá utilizarse en diferentes tipos de consumidor cuando su responsabilidad resulte aplicable.

---

# 177. Visual Component Canonical Definition

Un Visual Component `Implemented` deberá seguir el contrato general definido por el RDS:

```text
Visual Component
        │
        ├── Specification
        ├── Metadata
        └── Materialization
                when required
```

La Specification define la responsabilidad visual y sus constraints.

La Metadata proporciona identificación, clasificación y trazabilidad.

La Materialization representa la capacidad visual reutilizable cuando la responsabilidad requiera un artefacto concreto.

La definición canónica deberá distinguir:

```text
Visual Responsibility
        ≠
Visual Design Rule
        ≠
Reusable Asset
        ≠
Consumer-specific Asset
```

---

# 178. Relationship with Visual Design System

El Visual Design System mantiene las reglas visuales globales.

La VCL deberá consumirlas.

No deberá duplicarlas innecesariamente.

Modelo:

```text
Visual Design System
        ↓
Color / Typography / Spacing / Accessibility / Responsive Rules
        ↓
Visual Component
        ↓
Consumer Materialization
```

Por tanto:

```text
VCL-BANNER
```

podrá definir la responsabilidad de presentar visualmente un proyecto.

Pero las reglas generales de:

- contraste;
- colores;
- tipografía;
- accesibilidad;

permanecerán en el Visual Design System cuando exista una fuente canónica para ellas.

---

# 179. Visual Materialization Model

Los Visual Components podrán materializarse mediante diferentes mecanismos según su responsabilidad.

Ejemplos:

```text
Visual Component
        │
        ├── Asset
        ├── Layout
        ├── Snippet
        ├── Convention
        ├── Template
        ├── Configuration
        └── Composite Materialization
```

No deberá imponerse una forma física idéntica.

Ejemplo:

```text
VCL-BANNER
        ↓
SVG / PNG / reusable template
```

mientras:

```text
VCL-CALL-OUT
        ↓
Markdown convention
```

y:

```text
VCL-ARCHITECTURE-DIAGRAM
        ↓
Mermaid / PlantUML / SVG guidance
```

podrán necesitar mecanismos diferentes.

---

# 180. Visual Materialization Sufficiency

Un Visual Component no deberá considerarse `Implemented` únicamente por existir una descripción conceptual cuando su responsabilidad requiera una capacidad visual reusable.

La suficiencia deberá evaluarse según la responsabilidad.

Ejemplo:

```text
VCL-BANNER
        ↓
Specification + Metadata only
        ↓
Potentially insufficient
```

si el contrato exige una materialización reusable.

Mientras:

```text
VCL-CALL-OUT
        ↓
Specification + Metadata + reusable convention
        ↓
Potentially sufficient
```

cuando la responsabilidad quede completamente satisfecha mediante una convención.

La arquitectura prioriza:

```text
Responsibility satisfaction
        >
Number of files
```

---

# 181. Visual Consumer Adaptation

Los consumidores podrán adaptar Visual Components para representar correctamente su identidad y contexto.

La adaptación podrá afectar a:

- contenido;
- texto;
- iconografía;
- dimensiones;
- composición;
- assets;
- enlaces;
- variantes;
- parámetros.

La adaptación no deberá:

- alterar la responsabilidad canónica;
- contradecir el Visual Design System;
- eliminar requisitos esenciales de accesibilidad;
- introducir dependencia innecesaria de un único proveedor;
- convertir una variante local en un nuevo Component sin evidencia de reutilización.

---

# 182. Visual Portability

Los Visual Components deberán evitar acoplamiento innecesario a un único consumidor o proveedor.

Cuando se utilice un servicio externo, deberá distinguirse:

```text
Visual Responsibility
        ≠
Provider
```

Ejemplo:

```text
VCL-SKILL-ICONS
        ↓
Technology representation
```

no deberá redefinirse utilizando el nombre de un proveedor específico si la responsabilidad puede satisfacerse mediante otros mecanismos equivalentes.

La dependencia de proveedor deberá justificarse cuando exista.

---

# 183. VCL-BANNER

## Identifier

```text
VCL-BANNER
```

## Purpose

Presentar visualmente el proyecto.

## Possible Contents

Podrá incluir:

- nombre;
- tagline;
- iconografía;
- identidad;
- fondo;
- elementos gráficos relacionados.

## Materialization

Podrá utilizar:

- SVG;
- PNG;
- template reusable;
- asset generation guidance;
- otros formatos mantenibles.

## Guidance

Cuando se necesite un formato horizontal reusable podrá utilizarse como referencia una relación aproximada:

```text
2:1
```

Las dimensiones concretas deberán adaptarse al contexto.

---

# 184. VCL-SOCIAL-PREVIEW

## Identifier

```text
VCL-SOCIAL-PREVIEW
```

## Purpose

Representar visualmente el repositorio cuando se comparte mediante plataformas que utilizan una preview image.

## Principles

Deberá ser:

- legible en tamaños reducidos;
- reconocible;
- coherente con la identidad;
- suficientemente simple;
- mantenible.

No deberá contener texto excesivo.

## Materialization

Podrá utilizar:

- PNG;
- SVG transformado;
- reusable template;
- generated asset.

---

# 185. VCL-HERO

## Identifier

```text
VCL-HERO
```

## Purpose

Representar visualmente la cabecera o presentación principal del README.

## Relationship

Puede complementar:

```text
README-HERO
```

pero no sustituye su responsabilidad documental.

Modelo:

```text
README-HERO
        ↓
Content responsibility

VCL-HERO
        ↓
Visual presentation responsibility
```

## Typical Structure

```text
Banner
        ↓
Project Name
        ↓
Tagline
        ↓
Primary Badges
```

La composición concreta deberá adaptarse al proyecto.

---

# 186. VCL-BADGES

## Identifier

```text
VCL-BADGES
```

## Purpose

Mostrar información breve y relevante mediante indicadores visuales compactos.

## Possible Categories

Podrá incluir:

- build;
- version;
- license;
- documentation;
- status;
- coverage;
- release.

## Badge Policy

Los badges deberán aportar información real.

No deberán utilizarse para:

- decorar;
- aumentar artificialmente percepción de actividad;
- repetir información irrelevante;
- mostrar métricas sin utilidad.

La cantidad deberá mantenerse limitada.

---

# 187. VCL-SKILL-ICONS

## Identifier

```text
VCL-SKILL-ICONS
```

## Purpose

Representar tecnologías, herramientas o stacks mediante iconografía reusable.

## Possible Providers

Podrán utilizarse proveedores o assets compatibles con el Visual Design System.

Entre las opciones actuales podrá utilizarse, cuando resulte apropiado:

```text
skillicons.dev
```

La responsabilidad del Component no depende de este proveedor.

## Principles

Se priorizarán:

- pocas tecnologías relevantes;
- agrupación coherente;
- ausencia de duplicados;
- consistencia visual;
- legibilidad.

---

# 188. VCL-PROJECT-CARD

## Identifier

```text
VCL-PROJECT-CARD
```

## Purpose

Representar visualmente un proyecto relacionado.

## Possible Contents

Podrá incluir:

- nombre;
- descripción;
- stack;
- estado;
- enlace;
- preview.

## Possible Consumers

- GitHub Profile;
- portfolio;
- landing pages;
- documentación;
- páginas de proyectos.

El Component deberá mantener una responsabilidad de representación.

No deberá convertirse en un bloque rígido de contenido.

---

# 189. VCL-STATS

## Identifier

```text
VCL-STATS
```

## Purpose

Representar visualmente métricas o estadísticas cuando aporten información relevante.

## Typical Consumer

GitHub Profile.

## Guidance

Las estadísticas deberán utilizarse únicamente cuando ayuden a comprender:

- actividad;
- contribuciones;
- uso;
- estado;
- evolución.

La selección de métricas o proveedores no forma parte del contrato general del Component.

No deberá asumirse que todos los repositorios necesitan estadísticas visuales.

---

# 190. VCL-CONTRIBUTION-GRAPH

## Identifier

```text
VCL-CONTRIBUTION-GRAPH
```

## Purpose

Representar visualmente actividad o contribuciones cuando resulte relevante para el consumidor.

## Typical Consumer

GitHub Profile.

## Guidance

Su uso deberá estar justificado por el contexto.

No forma parte de la composición visual universal de los repositorios.

La visualización deberá evitar interpretaciones engañosas de actividad o productividad.

---

# 191. VCL-TYPING-BANNER

## Identifier

```text
VCL-TYPING-BANNER
```

## Purpose

Mostrar contenido textual dinámico cuando aporte valor real a la presentación.

## Typical Consumer

GitHub Profile.

## Guidance

Su utilización deberá ser excepcional.

No deberá incorporarse como elemento estándar de todos los consumidores.

Los efectos dinámicos deberán evitar:

- ruido visual;
- problemas de accesibilidad;
- carga innecesaria;
- dependencia excesiva de proveedores.

---

# 192. VCL-ARCHITECTURE-DIAGRAM

## Identifier

```text
VCL-ARCHITECTURE-DIAGRAM
```

## Purpose

Representar visualmente la arquitectura de un sistema.

## Possible Formats

Se priorizarán:

```text
Mermaid
PlantUML
SVG
```

cuando resulten adecuados.

## Principles

El diagrama deberá:

- ayudar a comprender;
- representar información relevante;
- ser mantenible;
- evolucionar con la arquitectura;
- evitar detalle innecesario.

## Relationship

Podrá complementar:

```text
README-ARCHITECTURE
DOC-ARCHITECTURE
DOC-DIAGRAMS
```

sin sustituir sus responsabilidades.

---

# 193. VCL-WORKFLOW-DIAGRAM

## Identifier

```text
VCL-WORKFLOW-DIAGRAM
```

## Purpose

Representar visualmente procesos o secuencias operativas.

## Possible Uses

Ejemplos:

- CI/CD;
- release flow;
- development flow;
- documentation pipeline;
- knowledge pipeline;
- maintenance process.

## Relationship

Podrá representar visualmente procesos definidos por Workflow Components.

Ejemplo:

```text
WCL-RELEASE
        ↓
Operational responsibility

VCL-WORKFLOW-DIAGRAM
        ↓
Visual representation
```

No deberá confundirse el diagrama con el workflow ejecutable.

---

# 194. VCL-FOLDER-DIAGRAM

## Identifier

```text
VCL-FOLDER-DIAGRAM
```

## Purpose

Representar la estructura principal de un repositorio, módulo o conjunto de archivos cuando facilite comprensión.

## Possible Formats

Podrá utilizar:

- árbol textual;
- Mermaid;
- SVG;
- diagramas equivalentes mantenibles.

Ejemplo:

```text
.github/
docs/
framework/
src/
tests/
```

No deberá representar cada archivo si ello reduce claridad.

---

# 195. VCL-NAVIGATION-CARD

## Identifier

```text
VCL-NAVIGATION-CARD
```

## Purpose

Representar enlaces o destinos relacionados mediante un elemento visual reusable.

## Possible Targets

Podrá enlazar:

- Architecture;
- API;
- Roadmap;
- ADR;
- Documentation;
- demos;
- proyectos relacionados.

## Guidance

La navegación visual deberá complementar la navegación textual.

No deberá introducir dependencias de JavaScript o HTML complejo cuando una solución simple sea suficiente.

---

# 196. VCL-CALL-OUT

## Identifier

```text
VCL-CALL-OUT
```

## Purpose

Resaltar información relevante dentro de contenido documental.

## Relationship

La sintaxis y utilización deberán seguir los estándares documentales aplicables.

Este Component representa la responsabilidad visual de destacar información.

No redefine las reglas generales de documentación.

## Current Recommended Style

Para GitHub podrá utilizarse:

```markdown
> [!NOTE]

> [!TIP]

> [!IMPORTANT]

> [!WARNING]

> [!CAUTION]
```

cuando corresponda.

---

# 197. Visual Component Catalog

La Visual Component Library reconoce actualmente:

| Identifier | Responsibility |
| --- | --- |
| `VCL-BANNER` | Repository visual presentation |
| `VCL-SOCIAL-PREVIEW` | Shared repository preview |
| `VCL-HERO` | Hero visual layout |
| `VCL-BADGES` | Compact project information |
| `VCL-SKILL-ICONS` | Technology representation |
| `VCL-PROJECT-CARD` | Project representation |
| `VCL-STATS` | Metrics visualization |
| `VCL-CONTRIBUTION-GRAPH` | Contribution visualization |
| `VCL-TYPING-BANNER` | Dynamic textual presentation |
| `VCL-ARCHITECTURE-DIAGRAM` | Architecture visualization |
| `VCL-WORKFLOW-DIAGRAM` | Process visualization |
| `VCL-FOLDER-DIAGRAM` | Repository structure visualization |
| `VCL-NAVIGATION-CARD` | Visual navigation |
| `VCL-CALL-OUT` | Highlighted information |

Esta tabla representa la taxonomía arquitectónica de la familia.

El Component Catalog mantiene la clasificación global de:

- implementación;
- prioridad;
- audiencia;
- madurez;
- descubrimiento.

La VCL no deberá convertirse en una segunda fuente de esos datos.

---

# 198. Current Implementation Boundary

El RDS reconoce actualmente las responsabilidades visuales de la VCL.

La existencia de:

- banners;
- badges;
- diagramas;
- callouts;
- iconos;
- social previews;

en GitHub Framework u otros consumidores no implica automáticamente que los Components correspondientes estén `Implemented`.

La transición requiere una definición canónica reusable conforme al contrato general:

```text
Specification
        +
Metadata
        +
Sufficient Materialization
```

La práctica del consumidor constituye evidencia potencial.

No constituye por sí sola implementación canónica.

---

# 199. Color System

El sistema de color pertenece al Visual Design System.

Los Visual Components deberán reutilizar sus roles y convenciones cuando corresponda.

No deberán introducir colores arbitrarios que contradigan la identidad o reglas definidas.

Los tokens concretos, variantes y decisiones cromáticas deberán permanecer en su fuente canónica.

La VCL podrá referenciarlos.

No deberá duplicarlos.

---

# 200. Typography

Los Visual Components deberán respetar las reglas tipográficas definidas por el Visual Design System y las capacidades del medio donde se rendericen.

En GitHub se priorizará:

- tipografía nativa;
- legibilidad;
- compatibilidad;
- accesibilidad.

Se evitarán:

- fuentes embebidas innecesarias;
- imágenes utilizadas únicamente para representar texto;
- efectos tipográficos que reduzcan comprensión;
- dependencias externas sin valor suficiente.

---

# 201. Spacing

Los Visual Components deberán mantener una separación visual coherente con su contexto.

Se evitarán:

- bloques excesivamente densos;
- encabezados consecutivos sin contenido;
- separación irregular;
- hacks de Markdown o HTML;
- espacios creados artificialmente mediante caracteres invisibles.

Las reglas específicas de espaciado pertenecen al Visual Design System cuando estén definidas.

---

# 202. Iconography

Los Visual Components deberán utilizar iconografía coherente cuando resulte necesaria.

Las fuentes podrán incluir:

- Skill Icons;
- Simple Icons;
- GitHub Octicons;
- assets propios;
- proveedores equivalentes.

La selección deberá respetar:

- consistencia;
- legibilidad;
- licencia;
- accesibilidad;
- mantenimiento.

No deberán mezclarse estilos incompatibles sin justificación.

---

# 203. Image Policy

Las imágenes utilizadas por Visual Components deberán formar parte de una estrategia mantenible.

Cuando corresponda deberán:

- estar versionadas;
- almacenarse en una fuente controlada;
- optimizarse;
- mantenerse actualizadas;
- utilizar nombres comprensibles;
- disponer de texto alternativo;
- respetar licencias.

Las dependencias externas deberán utilizarse únicamente cuando aporten una ventaja justificada.

La ubicación física dependerá del Repository Template o del consumidor.

---

# 204. Dark Mode Compatibility

Los Visual Components deberán verificarse en los modos de visualización relevantes.

Para GitHub deberán considerarse, cuando corresponda:

```text
GitHub Dark
GitHub Light
```

Los Components no deberán depender exclusivamente de un único modo cuando ello comprometa:

- legibilidad;
- contraste;
- comprensión;
- reconocimiento.

Las variantes podrán utilizarse cuando aporten una solución mantenible.

---

# 205. Responsive Behavior

Los Visual Components deberán conservar su comprensión en los tamaños de pantalla relevantes para su consumidor.

Cuando corresponda deberán evaluarse en:

- escritorio;
- tablet;
- móvil.

Se prestará especial atención a:

- assets muy anchos;
- texto integrado en imágenes;
- tablas visuales;
- diagramas densos;
- cards;
- banners.

La responsividad deberá perseguir comprensión.

No uniformidad absoluta.

---

# 206. Accessibility

Los Visual Components deberán respetar principios básicos de accesibilidad.

Entre ellos:

- contraste suficiente;
- no depender únicamente del color;
- texto alternativo cuando proceda;
- legibilidad;
- tamaño adecuado;
- movimiento limitado;
- estructura comprensible;
- información equivalente cuando una imagen sea esencial.

La accesibilidad forma parte del contrato de calidad visual.

No constituye una mejora opcional posterior.

---

# 207. Visual Dependencies

Los Visual Components podrán mantener dependencias únicamente cuando sean necesarias.

Ejemplo:

```text
VCL-HERO
        ↓ may rely on
VCL-BANNER
```

solo cuando la Specification concreta lo establezca.

El uso habitual conjunto no deberá interpretarse automáticamente como dependencia.

Ejemplo:

```text
VCL-BANNER
+
VCL-BADGES
```

puede representar complementariedad sin dependencia.

Las dependencias reales deberán mantenerse en la definición canónica correspondiente.

---

# 208. Cross-Family Relationships

Los Visual Components podrán complementar responsabilidades de otras familias.

Ejemplos:

```text
README-HERO
        ↔
VCL-HERO
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

Estas relaciones deberán mantener responsabilidades separadas.

La familia visual representa comunicación visual.

No sustituye documentación, workflows ni contenido.

---

# 209. Repository Template Integration

La composición de Visual Components pertenece a los Repository Templates y a las necesidades del consumidor.

Modelo:

```text
Project Type
        ↓
Repository Template
        ↓
Visual Component Composition
        ↓
Required / Recommended / Optional
```

No existen Visual Profiles independientes como:

```text
Strategic
Supporting
Learning
Experimental
```

La madurez constituye una dimensión independiente.

El Repository Template define la composición contextual.

---

# 210. Maturity Interaction

Los Maturity Profiles podrán incrementar expectativas relacionadas con:

- calidad visual;
- consistencia;
- mantenimiento;
- accesibilidad;
- presentación;
- identidad.

Sin embargo:

```text
Same maturity
        ≠
Same visual composition
```

Un repositorio estratégico no necesita necesariamente todos los Visual Components.

La utilización deberá responder al proyecto real.

---

# 211. Visual Validation

Los Visual Components implementados deberán validarse mediante consumidores representativos cuando resulte necesario.

La validación podrá evaluar:

- claridad;
- reutilización;
- adaptación;
- legibilidad;
- dark/light compatibility;
- responsividad;
- accesibilidad;
- mantenimiento;
- provider dependence;
- consumer coupling.

El dogfooding podrá utilizar GitHub Framework cuando exista una responsabilidad visual aplicable.

No deberá forzarse adopción únicamente para demostrar cobertura.

---

# 212. Visual Anti-Patterns

No utilizar:

- elementos visuales sin propósito;
- GIF puramente decorativos;
- badges excesivos;
- fondos recargados;
- iconografía inconsistente;
- estadísticas sin valor informativo;
- colores arbitrarios;
- tipografías artificiales;
- imágenes de baja calidad;
- Visual Components incorporados únicamente por madurez;
- requirement levels definidos globalmente fuera de Repository Templates;
- reglas del Visual Design System duplicadas dentro de Components;
- dependencias innecesarias de proveedores externos;
- elementos específicos de un consumidor generalizados sin evidencia;
- assets sin mantenimiento;
- texto esencial disponible únicamente dentro de imágenes;
- materializaciones inaccesibles;
- Components distintos creados únicamente para pequeñas variantes estéticas.

---

# 213. Visual Component Quality Gates

Antes de promover un Visual Component a `Implemented` deberá verificarse:

- [ ] El identificador `VCL-*` es único y estable.
- [ ] El propósito está definido.
- [ ] La responsabilidad visual está claramente delimitada.
- [ ] Existe Specification canónica.
- [ ] Existe Metadata canónica.
- [ ] El mecanismo de materialización está identificado.
- [ ] La materialización es suficiente para la responsabilidad.
- [ ] No duplica reglas pertenecientes al Visual Design System.
- [ ] No duplica otro Visual Component.
- [ ] Las dependencias reales están identificadas.
- [ ] Los assets pueden mantenerse cuando existen.
- [ ] Los proveedores externos están justificados cuando se utilizan.
- [ ] La accesibilidad ha sido considerada.
- [ ] La compatibilidad visual ha sido evaluada cuando corresponde.
- [ ] La adaptación del consumidor está suficientemente desacoplada.
- [ ] La clasificación de implementación refleja la realidad.

---

# 214. Visual Composition Quality Gates

Antes de aprobar la composición visual de un consumidor deberá verificarse, según corresponda:

- [ ] Los Required Visual Components del Repository Template están correctamente materializados.
- [ ] Cada elemento visual responde a una necesidad identificable.
- [ ] Los Components adicionales aportan valor.
- [ ] La composición respeta el Visual Design System.
- [ ] La información visual es legible.
- [ ] La navegación visual es comprensible cuando existe.
- [ ] Los assets son mantenibles.
- [ ] La compatibilidad con los modos relevantes ha sido revisada.
- [ ] El comportamiento responsive es adecuado.
- [ ] La accesibilidad ha sido considerada.
- [ ] No existen elementos puramente decorativos que generen ruido.
- [ ] No se duplican reglas mantenidas canónicamente en otras fuentes.
- [ ] La identidad específica del consumidor no ha sido generalizada innecesariamente.

---

# 215. Long-Term Vision

La Visual Component Library permitirá reutilizar responsabilidades visuales validadas cuando un repositorio necesite:

- identidad;
- presentación;
- navegación;
- comunicación;
- visualización técnica.

Los Repository Templates podrán proporcionar composiciones visuales adecuadas a diferentes tipos de proyecto.

Los repositorios podrán compartir lenguaje visual sin necesitar exactamente los mismos elementos gráficos.

Con el tiempo, Specifications, Metadata y materializaciones podrán permitir:

- resolución automática de Visual Components;
- generación asistida de assets;
- validación de consistencia visual;
- comprobaciones de accesibilidad;
- detección de assets obsoletos;
- adaptación de variantes;
- integración con herramientas de bootstrap.

La automatización deberá consumir las fuentes canónicas del Visual Design System y de los Visual Components.

No deberá sustituirlas.

---

# 216. Part 5 Conclusions

La **Visual Component Library** convierte responsabilidades visuales recurrentes en elementos reutilizables del Framework.

Cada Visual Component representa una responsabilidad diferenciada de las reglas globales del Visual Design System.

El contrato general es:

```text
Visual Component
        │
        ├── Specification
        ├── Metadata
        └── Materialization when required
```

Los Visual Components podrán materializarse mediante:

```text
Assets
Layouts
Snippets
Conventions
Templates
Configurations
Composite mechanisms
```

según su naturaleza.

Los Repository Templates determinan contextualmente qué Visual Components son:

```text
Required
Recommended
Optional
```

Los Maturity Profiles podrán incrementar expectativas visuales.

No definen una composición universal.

Por tanto:

```text
Visual Design System
        +
Reusable Visual Responsibilities
        +
Repository Template
        +
Consumer Identity
        ↓
Appropriate Visual Experience
```

La VCL no pretende que todos los repositorios tengan la misma apariencia.

Pretende reutilizar responsabilidades visuales comunes manteniendo:

- coherencia;
- claridad;
- accesibilidad;
- mantenibilidad;
- capacidad de adaptación.

---

# 217. Part 5 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.

---

# 08 - REPOSITORY DESIGN SYSTEM

# Part 6/7

# Repository Templates & Maturity Profiles

---

# 218. Purpose

La **Repository Template Library (RTL)** define composiciones reutilizables para crear, estructurar y evaluar repositorios según su tipo de proyecto.

Cada Repository Template establece:

- un tipo de proyecto;
- una madurez mínima recomendada;
- una composición de Framework Components;
- requirement levels contextuales;
- guidance de adopción;
- reglas de especialización;
- expectativas de conformidad.

El objetivo consiste en reducir decisiones repetitivas durante la creación y evolución de repositorios sin imponer:

- tecnologías concretas;
- estructuras físicas innecesarias;
- Components no aplicables;
- modelos operativos universales;
- una única madurez para todos los consumidores.

---

# 219. Template Philosophy

Los Repository Templates no son repositorios completos ni copias rígidas de una estructura predeterminada.

Representan **contratos de composición reutilizables**.

Principio:

```text
Framework Components
        ↓
Reusable Responsibilities
        ↓
Repository Template
        ↓
Contextual Composition
        ↓
Consumer Repository
```

Un Template selecciona Components existentes.

No redefine sus responsabilidades canónicas.

Un Template podrá añadir guidance contextual cuando sea necesaria para explicar cómo aplicar una responsabilidad dentro del tipo de proyecto que representa.

No deberá duplicar Specifications completas de Components.

---

# 220. Repository Template Responsibility

Cada Repository Template representa una responsabilidad distinta de los Framework Components.

Los Framework Components responden:

```text
What reusable responsibility exists?
```

Los Repository Templates responden:

```text
Which reusable responsibilities are appropriate
for this project type?
```

Por tanto:

```text
Component
        ↓
Defines responsibility

Repository Template
        ↓
Defines composition
```

La separación deberá mantenerse explícita.

Un Template no deberá convertirse en una nueva fuente canónica de responsabilidades ya definidas por Components.

---

# 221. Template Canonical Definition

Un Repository Template implementado deberá disponer de una definición canónica compuesta al menos por:

```text
Repository Template
        │
        ├── Specification
        └── Metadata
```

La Specification deberá explicar:

- propósito;
- tipo de proyecto;
- alcance;
- límites;
- composición;
- requirement levels;
- guidance;
- especialización;
- extensibilidad;
- criterios de adopción.

La Metadata deberá proporcionar una representación estructurada de:

- identidad;
- versión;
- status;
- project type;
- maturity;
- descripción;
- Components;
- requirement levels;
- información adicional necesaria para automatización futura.

La implementación canónica se mantiene actualmente en:

```text
framework/templates/repositories/
```

---

# 222. Template Identity

Todo Repository Template oficial deberá disponer de un identificador estable.

Formato actual:

```text
TPL-NAME
```

Ejemplos:

```text
TPL-BACKEND
TPL-FULLSTACK
TPL-DOCUMENTATION
```

El identificador deberá:

- ser único;
- utilizar el prefijo `TPL-`;
- permanecer estable entre versiones compatibles;
- representar un tipo de composición reutilizable;
- evitar referencias a tecnologías concretas cuando estas no definan realmente el tipo de proyecto.

Los identificadores no deberán reutilizarse para Templates diferentes.

---

# 223. Template Architecture

Un Repository Template se modela conceptualmente mediante:

```text
Repository Template
        │
        ├── Identity
        ├── Project Type
        ├── Version
        ├── Lifecycle Status
        ├── Maturity
        ├── Required Components
        ├── Recommended Components
        ├── Optional Components
        └── Template-specific Guidance
```

El tipo de proyecto determina el contexto principal.

La madurez expresa el nivel mínimo recomendado.

Los requirement levels expresan la importancia contextual de cada Component dentro del Template.

Estas dimensiones deberán mantenerse separadas.

---

# 224. Project Type

El `project_type` identifica la naturaleza principal del repositorio para el que se diseña el Template.

Ejemplos actualmente implementados:

```text
Backend
Full Stack
Documentation
```

El tipo de proyecto deberá representar una diferencia suficientemente significativa como para justificar una composición distinta.

No deberá crearse un Repository Template nuevo únicamente por:

- lenguaje;
- framework;
- proveedor cloud;
- base de datos;
- una diferencia menor de tooling;
- una variante de madurez.

Ejemplo:

```text
Spring Boot backend
FastAPI backend
Django backend
```

podrán consumir:

```text
TPL-BACKEND
```

si sus responsabilidades estructurales continúan siendo equivalentes.

---

# 225. Template Requirement Levels

Cada Repository Template clasifica sus Components mediante tres requirement levels.

## Required

El Component forma parte del contrato mínimo del Template.

Su responsabilidad deberá estar satisfecha para considerar al consumidor conforme, salvo desviación explícitamente justificada.

## Recommended

El Component aporta valor habitual para ese tipo de proyecto.

Su necesidad final depende del contexto del consumidor.

Su ausencia no invalida por sí sola la conformidad.

## Optional

El Component resulta aplicable únicamente cuando existe una necesidad concreta.

No deberá incorporarse únicamente para aumentar cobertura.

Modelo:

```text
Component
        +
Repository Template
        ↓
Requirement Level
```

El requirement level es contextual.

No modifica la definición canónica del Component.

---

# 226. Requirement Level Independence

Los requirement levels deberán mantenerse separados de otras propiedades.

Por tanto:

```text
Component Priority
        ≠
Template Requirement Level
```

```text
Component Maturity
        ≠
Template Requirement Level
```

```text
Component Availability
        ≠
Template Requirement Level
```

```text
Lifecycle Status
        ≠
Template Requirement Level
```

Un Component con prioridad canónica `Recommended` podrá ser `required` dentro de un Repository Template concreto cuando su responsabilidad forme parte del contrato mínimo del tipo de proyecto.

Del mismo modo, un Component implementado podrá no formar parte de una composición determinada.

---

# 227. Template Composition Model

La composición canónica seguirá el modelo:

```text
Repository Template
        │
        ├── required
        ├── recommended
        └── optional
```

Cada Component deberá aparecer como máximo en un único requirement level dentro del mismo Template.

No deberán existir duplicados entre:

```text
required
recommended
optional
```

La ausencia de un Component del Template significa que su responsabilidad no forma parte de la composición canónica.

No significa que el Component sea inválido o incompatible con el consumidor.

---

# 228. Component Availability

Los Repository Templates podrán referenciar Framework Components clasificados como:

```text
Implemented
Conceptual
```

La clasificación de implementación describe la disponibilidad de una capacidad canónica reusable dentro del Framework.

No determina el requirement level contextual.

Por tanto:

```text
Implementation Classification
        ≠
Template Requirement Level
```

Un Component `Conceptual` podrá ser:

```text
required
recommended
optional
```

cuando su responsabilidad pertenezca legítimamente al contrato del Template.

En estos casos deberá quedar claro que:

- la responsabilidad está reconocida;
- no existe todavía implementación canónica reusable;
- el consumidor deberá satisfacerla mediante una materialización apropiada;
- el Framework no deberá presentar un artefacto inexistente como disponible.

---

# 229. Consumer Conformance

La conformidad de un repositorio consumidor se evalúa contra responsabilidades.

No únicamente contra disponibilidad de Framework Components.

Principio:

```text
Component Availability
        ≠
Consumer Conformance
```

Un consumidor podrá satisfacer una responsabilidad mediante:

- implementación canónica del Framework;
- especialización permitida;
- implementación propia compatible;
- mecanismo equivalente que satisfaga el contrato.

Ejemplo conceptual:

```text
README-LICENSE
        ↓
Framework classification: Conceptual
        ↓
Consumer materialization: LICENSE + README reference
        ↓
Responsibility satisfied
```

Por tanto, un Repository Template puede mantener una responsabilidad `required` aunque el Component correspondiente permanezca `Conceptual`.

---

# 230. Responsibility Satisfaction

Una responsabilidad se considerará satisfecha cuando la implementación del consumidor cumpla razonablemente el contrato que representa el Component.

La evaluación deberá considerar:

- propósito;
- contenido o comportamiento;
- evidencia;
- constraints;
- relaciones necesarias;
- materialización;
- adaptación permitida.

No deberá utilizarse únicamente:

```text
filename exists
```

como prueba universal de satisfacción.

Por ejemplo:

```text
CI file exists
        ≠
WCL-CI satisfied
```

si el workflow no realiza la responsabilidad definida.

---

# 231. Consumer Specialization

Un repositorio consumidor podrá especializar Components cuando su contexto lo requiera.

La especialización podrá afectar a:

- contenido;
- parámetros;
- configuración;
- implementación tecnológica;
- estructura física;
- mecanismos operativos;
- profundidad documental.

La especialización deberá preservar la responsabilidad canónica.

Modelo:

```text
Canonical Component
        ↓
Consumer Context
        ↓
Specialized Materialization
```

No deberá utilizarse especialización para justificar una responsabilidad completamente diferente.

---

# 232. Template Specialization

Un Repository Template podrá especializar la utilización de un Framework Component para su tipo de proyecto.

La especialización podrá afectar a:

- requirement level;
- guidance;
- contexto;
- orden recomendado;
- parámetros;
- relaciones relevantes;
- expectativas de materialización.

No deberá redefinir la Specification canónica del Component.

Ejemplo:

```text
DOC-API
        ↓
TPL-BACKEND
        ↓
API-oriented guidance
```

La responsabilidad `DOC-API` permanece independiente del Template.

---

# 233. Template Extensibility

Un repositorio consumidor podrá incorporar Components adicionales no incluidos en la composición canónica cuando exista una necesidad real.

Modelo:

```text
Repository Template
        ↓
Canonical Composition
        +
Consumer-specific Components
        ↓
Repository Implementation
```

La extensión deberá:

- estar justificada;
- evitar duplicación;
- respetar dependencias;
- mantener coherencia;
- no modificar el Template canónico únicamente por una necesidad específica.

Cuando una extensión aparezca repetidamente en consumidores equivalentes deberá evaluarse si el Repository Template necesita evolucionar.

---

# 234. Maturity Profiles

GitHub Framework mantiene cuatro niveles de madurez:

| Level | Description |
| --- | --- |
| L1 | Experimental |
| L2 | Public Basic |
| L3 | Supporting |
| L4 | Strategic |

Los Maturity Profiles expresan expectativas de:

- calidad;
- mantenimiento;
- documentación;
- automatización;
- gobernanza;
- continuidad.

No constituyen Repository Templates.

Por tanto, no existen Templates como:

```text
TPL-L1
TPL-L2
TPL-L3
TPL-L4
```

La madurez constituye una dimensión independiente.

---

# 235. L1 — Experimental

## Purpose

Explorar y validar ideas con una inversión estructural mínima.

## Typical Characteristics

Podrá incluir:

- estructura reducida;
- documentación esencial;
- pocos Components;
- automatización opcional;
- alto ritmo de cambio;
- contratos todavía inestables.

L1 no define una composición universal.

Tampoco exige un Repository Template específico.

---

# 236. L2 — Public Basic

## Purpose

Mantener un repositorio público comprensible y razonablemente utilizable.

## Typical Characteristics

Podrá incluir:

- identidad clara;
- propósito comprensible;
- licencia cuando corresponda;
- documentación de uso;
- estado visible;
- prácticas básicas de mantenimiento;
- historial cuando exista versionado.

L2 constituye actualmente la madurez mínima recomendada para los Repository Templates implementados.

---

# 237. L3 — Supporting

## Purpose

Mantener proyectos relevantes con mayor profundidad técnica y operativa.

## Typical Characteristics

Podrá incluir:

- documentación técnica ampliada;
- testing mantenido;
- CI;
- Roadmap;
- procesos de revisión;
- contribución;
- mayor trazabilidad;
- automatización de calidad;
- prácticas de mantenimiento.

L3 incrementa expectativas.

No obliga a incorporar todos los Components de estas áreas.

---

# 238. L4 — Strategic

## Purpose

Mantener repositorios estratégicos con alta exigencia de calidad, gobernanza y continuidad.

## Typical Characteristics

Podrá incluir:

- documentación profunda;
- gobernanza explícita;
- seguridad mantenida;
- automatización avanzada;
- releases controladas;
- trazabilidad;
- continuidad operativa;
- procesos de mantenimiento;
- alta calidad de presentación.

L4 representa la madurez más exigente definida actualmente.

No constituye una lista obligatoria de Components.

---

# 239. Maturity and Composition

La madurez no determina directamente la composición.

Principio:

```text
Maturity
        ↓
Quality and Maintenance Expectations
```

mientras:

```text
Project Type
        ↓
Repository Template
        ↓
Component Composition
```

Por tanto:

```text
Same maturity
        ≠
Same components
```

Dos repositorios L3 podrán utilizar composiciones sustancialmente diferentes.

La madurez podrá justificar expectativas adicionales sobre Components seleccionados, pero no deberá convertirse en una matriz automática.

---

# 240. Repository Template Catalog

Los Repository Templates implementados actualmente son:

| Template | Project Type | Maturity | Lifecycle | Implementation |
| --- | --- | :---: | --- | --- |
| `TPL-BACKEND` | Backend | L2 | Experimental | Implemented |
| `TPL-FULLSTACK` | Full Stack | L2 | Experimental | Implemented |
| `TPL-DOCUMENTATION` | Documentation | L2 | Experimental | Implemented |

Las definiciones canónicas se mantienen en:

```text
framework/templates/repositories/
```

El Component Catalog proporciona descubrimiento y clasificación global.

La RTL no deberá duplicar en detalle las composiciones canónicas de estos Templates.

---

# 241. TPL-BACKEND

`TPL-BACKEND` representa repositorios cuyo producto principal es una aplicación, servicio o capacidad backend.

Características actuales:

```text
id: TPL-BACKEND
project_type: Backend
maturity: L2
status: Experimental
```

La composición canónica se mantiene en:

```text
framework/templates/repositories/backend/
```

El Template podrá utilizar responsabilidades relacionadas con:

- presentación;
- arquitectura;
- API;
- persistencia;
- testing;
- documentación;
- despliegue;
- evolución;
- workflows.

La selección exacta pertenece a su Metadata y Specification.

No se duplica en el RDS.

---

# 242. Backend Template Guidance

`TPL-BACKEND` no presupone:

- lenguaje;
- framework;
- base de datos;
- arquitectura concreta;
- proveedor cloud;
- estrategia de despliegue.

Podrá aplicarse, por ejemplo, a:

```text
Spring Boot
FastAPI
Django
NestJS
Other backend stacks
```

si la responsabilidad principal del repositorio continúa siendo backend.

Las tecnologías constituyen decisiones del consumidor.

El Template define responsabilidades.

---

# 243. TPL-FULLSTACK

`TPL-FULLSTACK` representa repositorios que integran responsabilidades frontend y backend dentro de la misma unidad de proyecto.

Características actuales:

```text
id: TPL-FULLSTACK
project_type: Full Stack
maturity: L2
status: Experimental
```

La composición canónica se mantiene en:

```text
framework/templates/repositories/fullstack/
```

Podrá incorporar responsabilidades relacionadas con:

- presentación;
- arquitectura;
- frontend;
- backend;
- interfaces;
- persistencia;
- testing;
- documentación;
- despliegue;
- workflows.

El RDS no mantiene una segunda copia de esa composición.

---

# 244. TPL-DOCUMENTATION

`TPL-DOCUMENTATION` representa repositorios cuyo producto principal es:

- documentación técnica;
- conocimiento estructurado;
- estándares;
- guías;
- documentación de Framework;
- sistemas equivalentes de conocimiento.

Características actuales:

```text
id: TPL-DOCUMENTATION
project_type: Documentation
maturity: L2
status: Experimental
```

La composición canónica se mantiene en:

```text
framework/templates/repositories/documentation/
```

GitHub Framework ha sido utilizado como primera Reference Implementation de `TPL-DOCUMENTATION` mediante dogfooding.

La validación permitió comprobar:

- composición;
- responsibilities `required`;
- disponibilidad de Components;
- consumer conformance;
- especialización;
- gaps del Framework.

El resultado de la Reference Implementation fue conforme tras resolver los findings aplicables.

---

# 245. Repository Template Reference Implementation

Un Repository Template deberá poder validarse mediante un consumidor representativo antes de considerarse suficientemente maduro para adopción general.

Modelo:

```text
Repository Template
        ↓
Reference Implementation
        ↓
Conformance Analysis
        ↓
Findings
        ↓
Refinement
        ↓
Validated Contract
```

La Reference Implementation deberá permitir detectar:

- Template Gaps;
- Component Gaps;
- Consumer Gaps;
- documentación inconsistente;
- requirement levels incorrectos;
- responsabilidades redundantes;
- necesidades de especialización.

La Reference Implementation no deberá modificarse únicamente para conseguir un resultado favorable.

Los findings deberán clasificarse primero.

---

# 246. Gap Classification

Durante una validación podrán aparecer diferentes tipos de gap.

## Consumer Gap

El Repository Template es adecuado, pero el consumidor no satisface correctamente una responsabilidad.

## Template Gap

La composición o guidance del Repository Template no representa correctamente el tipo de proyecto.

## Component Gap

La responsabilidad es correcta, pero el Framework Component:

- no existe;
- permanece conceptual;
- tiene un contrato insuficiente;
- necesita evolución.

## Framework Gap

El problema afecta a una capacidad arquitectónica más amplia del Framework.

La clasificación deberá producirse antes de decidir dónde aplicar el cambio.

---

# 247. Conformance Analysis

La conformidad de un consumidor deberá evaluarse respecto al Repository Template aplicable.

Modelo:

```text
Repository Template
        ↓
Required Responsibilities
        ↓
Consumer Materialization
        ↓
Conformance Analysis
```

Los Components `recommended` y `optional` deberán evaluarse únicamente cuando hayan sido adoptados o cuando su ausencia represente un finding contextual relevante.

La ausencia de un Component `optional` no constituye defecto.

La ausencia de un `recommended` tampoco invalida automáticamente la conformidad.

---

# 248. Conformance Result

Una Reference Implementation deberá poder producir un resultado explícito.

Ejemplos:

```text
CONFORMANT
PARTIAL
NON-CONFORMANT
```

El vocabulario concreto podrá evolucionar mediante Standards o automatización futura.

El resultado deberá estar respaldado por evidencia.

No deberá inferirse únicamente por percepción general de calidad.

Un resultado inicial no conforme puede ser válido y útil cuando permite descubrir gaps reales.

---

# 249. Template Lifecycle

Los Repository Templates seguirán un lifecycle controlado.

Estados reconocidos:

```text
Draft
Experimental
Stable
Deprecated
Retired
```

Flujo habitual:

```text
Draft
        ↓
Experimental
        ↓
Stable
        ↓
Deprecated
        ↓
Retired
```

La transición no deberá producirse únicamente por antigüedad.

Deberá basarse en evidencia.

---

# 250. Draft Templates

Un Repository Template `Draft` se encuentra en definición o implementación inicial.

Podrá cambiar significativamente.

No deberá presentarse como Template validado para adopción general.

Podrá utilizarse para:

- diseño;
- experimentación;
- implementación inicial;
- preparación de Reference Implementations.

---

# 251. Experimental Templates

Un Repository Template `Experimental` dispone de una implementación material suficiente para ser utilizado y validado.

Podrá:

- contener Components `Conceptual`;
- utilizarse mediante dogfooding;
- participar en Reference Implementations;
- descubrir gaps;
- evolucionar su composición.

El estado `Experimental` no significa puramente conceptual.

Debe existir una implementación real del Template.

Los Templates actuales se encuentran en este estado.

---

# 252. Stable Templates

Un Repository Template podrá evolucionar a `Stable` cuando exista evidencia suficiente de que su contrato es:

- coherente;
- reutilizable;
- mantenible;
- validado;
- suficientemente estable.

Antes de promoverlo deberá verificarse, como mínimo:

- identidad definida;
- Specification y Metadata sincronizadas;
- composición validada;
- responsabilidades `required` satisfacibles;
- Quality Gates evaluables;
- evidencia representativa de uso;
- gaps críticos resueltos o explícitamente aceptados;
- ausencia de contradicciones conocidas con el RDS.

La presencia de Components `Conceptual` no impide automáticamente la promoción.

La decisión deberá basarse en la estabilidad del contrato y la capacidad demostrada de satisfacer sus responsabilidades.

---

# 253. Deprecated and Retired Templates

## Deprecated

Un Repository Template `Deprecated` continúa registrado por compatibilidad o trazabilidad, pero no deberá recomendarse para nuevas adopciones.

Deberá indicar, cuando corresponda:

- motivo;
- alternativa;
- impacto;
- estrategia de migración.

## Retired

Un Repository Template `Retired` no deberá utilizarse para nuevas adopciones.

Su definición podrá conservarse para:

- trazabilidad;
- historial;
- migraciones;
- comprensión de consumidores existentes.

Un Template no debería evolucionar directamente de `Stable` a `Retired` sin pasar por `Deprecated`, salvo razón excepcional documentada.

---

# 254. Workflow Composition

Los Repository Templates podrán incorporar Workflow Components cuando el tipo de proyecto y sus necesidades operativas lo justifiquen.

Modelo:

```text
Project Type
+
Repository Needs
+
Maturity Expectations
        ↓
Workflow Component Composition
```

La madurez podrá aumentar expectativas operativas.

No determina automáticamente los Workflow Components.

Un backend y un repositorio documental con madurez L2 pueden necesitar workflows diferentes.

La disponibilidad de un Workflow Component tampoco determina su selección.

---

# 255. Visual Composition

Los Repository Templates podrán incorporar Visual Components cuando exista una responsabilidad visual aplicable.

Modelo:

```text
Project Type
+
Communication Needs
+
Visual Design System
        ↓
Visual Component Composition
```

No todos los repositorios necesitarán:

- banner;
- social preview;
- diagrams;
- cards;
- visual assets.

La composición deberá mantenerse contextual.

---

# 256. Documentation Composition

Los Repository Templates seleccionan Documentation Components según las responsabilidades documentales del tipo de proyecto.

Ejemplo conceptual:

```text
TPL-BACKEND
        ↓
Architecture
API
Testing
Deployment
```

mientras:

```text
TPL-DOCUMENTATION
        ↓
Architecture
Project Status
Changelog
References
```

Las composiciones exactas deberán consultarse en las fuentes canónicas.

El RDS únicamente define el modelo.

---

# 257. README Composition

Los Repository Templates seleccionan README Components para proporcionar una entrada adecuada al tipo de proyecto.

Todos los repositorios no necesitan necesariamente:

- Demo;
- Author;
- Architecture summary;
- Roadmap;
- Testing section;
- Repository Structure.

La composición deberá favorecer:

```text
Understand
        ↓
Trust
        ↓
Use
```

sin convertir el README en documentación completa.

---

# 258. Template Dependencies

Un Repository Template no deberá introducir dependencias entre Components si dichas dependencias no existen realmente.

La inclusión conjunta de:

```text
Component A
+
Component B
```

no implica:

```text
A requires B
```

Las dependencias pertenecen a las definiciones canónicas de los Components.

El Template realiza composición.

No inventa relaciones estructurales.

---

# 259. Template Materialization

Un Repository Template podrá disponer de artefactos físicos adicionales cuando exista una necesidad reusable real.

Ejemplos potenciales:

```text
template files
directory skeleton
configuration defaults
bootstrap artifacts
```

Sin embargo, la existencia de una estructura material idéntica para todos los Templates no es obligatoria.

Principio:

```text
Conceptual consistency
        >
Filesystem symmetry
```

No deberán crearse directorios vacíos únicamente para aparentar que un Template dispone de materialización adicional.

---

# 260. Bootstrap Strategy

Todo nuevo repositorio basado en Repository Templates seguirá conceptualmente:

```text
Identify Project Type
        ↓
Select Repository Template
        ↓
Review Maturity
        ↓
Apply Required Responsibilities
        ↓
Evaluate Recommended Components
        ↓
Add Optional Components when justified
        ↓
Configure Consumer Context
        ↓
Configure Workflows
        ↓
Validate
        ↓
Publish
```

El Repository Template proporciona una base reusable.

No sustituye las decisiones específicas del proyecto.

---

# 261. Repository Migration

Un repositorio existente podrá adoptar un Repository Template de forma incremental.

Modelo:

```text
Existing Repository
        ↓
Identify Project Type
        ↓
Select Repository Template
        ↓
Conformance Analysis
        ↓
Gap Classification
        ↓
Migration Plan
        ↓
Implementation
        ↓
Validation
```

No será necesario recrear el repositorio.

La migración deberá perseguir responsabilidades útiles.

No conformidad mecánica.

---

# 262. Template Versioning

Cada Repository Template mantiene versionado independiente mediante Semantic Versioning.

```text
Major.Minor.Patch
```

## Major

Cambio incompatible del contrato.

## Minor

Nueva capacidad o evolución compatible relevante.

## Patch

Corrección compatible.

Una nueva versión global de GitHub Framework no obliga a modificar la versión de todos los Repository Templates.

---

# 263. Template Compatibility

Los Repository Templates deberán mantener compatibilidad razonable siempre que sea posible.

Un cambio incompatible deberá:

- estar justificado;
- reflejarse en el versionado;
- documentarse;
- identificar consumidores afectados;
- proporcionar guidance de migración cuando corresponda.

La compatibilidad deberá evaluarse sobre:

- responsabilidades;
- composición;
- contratos;
- metadata.

No sobre estructuras accidentales que no formen parte del Template.

---

# 264. Future Repository Templates

La arquitectura admite nuevos tipos de Repository Template.

Entre tipos de proyecto potencialmente identificados se encuentran:

```text
AI
Library
Website
```

Estos tipos no constituyen Templates oficiales mientras no exista:

- un caso de uso real;
- una composición diferenciada;
- Specification;
- Metadata;
- implementación;
- validación.

Flujo:

```text
Potential Project Type
        ↓
Real Use Case
        ↓
Template Specification
        ↓
Implementation
        ↓
Reference Implementation
        ↓
Validation
        ↓
Official Template
```

No se crearán Templates especulativos únicamente para aumentar cobertura.

---

# 265. Template Anti-Patterns

No utilizar:

- Templates gigantes;
- Templates especulativos;
- Templates por tecnología sin necesidad arquitectónica;
- Components innecesarios;
- composiciones basadas únicamente en madurez;
- requirement levels heredados sin análisis;
- duplicación de Specifications de Components;
- estructuras físicas rígidas sin necesidad;
- Components añadidos únicamente para obtener conformidad;
- Template forks por pequeñas variaciones;
- Components conceptuales presentados como materialmente disponibles;
- consumer-specific decisions incorporadas prematuramente al Template;
- múltiples Templates para necesidades equivalentes.

---

# 266. Repository Template Quality Gates

Antes de aprobar o evolucionar un Repository Template deberá verificarse:

- [ ] El identificador `TPL-*` es único y estable.
- [ ] El tipo de proyecto está claramente identificado.
- [ ] Existe una necesidad reusable real.
- [ ] La madurez recomendada está definida.
- [ ] Existe Specification.
- [ ] Existe Metadata.
- [ ] Los Components `required` representan el contrato mínimo.
- [ ] Los Components `recommended` aportan valor habitual.
- [ ] Los Components `optional` responden a escenarios reales.
- [ ] No existen duplicados entre requirement levels.
- [ ] Todos los Component IDs están reconocidos por el Framework.
- [ ] No se duplican Specifications canónicas de Components.
- [ ] Las dependencias no se redefinen artificialmente.
- [ ] La composición puede reutilizarse en proyectos equivalentes.
- [ ] Las decisiones específicas del consumidor permanecen fuera del contrato.
- [ ] La disponibilidad de Components se representa correctamente.
- [ ] La conformidad puede evaluarse por responsabilidad.
- [ ] Existe o puede existir una Reference Implementation representativa.
- [ ] Los gaps críticos están resueltos o registrados.

---

# 267. Stable Promotion Gate

La promoción:

```text
Experimental
        ↓
Stable
```

deberá producirse únicamente cuando:

- los Quality Gates aplicables hayan sido evaluados;
- exista evidencia representativa de adopción o validación;
- el contrato sea suficientemente estable;
- no existan gaps críticos sin resolver o explícitamente aceptados.

La antigüedad de un Template no constituye evidencia suficiente.

---

# 268. Long-Term Vision

La Repository Template Library permitirá iniciar y evolucionar repositorios reutilizando composiciones validadas del Framework.

Cada Template representará un contrato mantenible adaptado a un tipo de proyecto.

La evolución futura podrá incorporar:

- nuevos Repository Templates respaldados por casos reales;
- validación automática;
- resolución de Components;
- generación asistida;
- migraciones;
- análisis de conformidad;
- configuración de Workflow Components;
- integración con Framework Automation.

La automatización deberá construirse sobre el modelo declarativo existente.

No deberá sustituirlo.

---

# 269. Part 6 Conclusions

La **Repository Template Library** transforma la creación y evolución de repositorios en un proceso basado en composición reusable.

Los elementos principales mantienen responsabilidades diferenciadas:

```text
Framework Components
        ↓
Reusable Responsibilities

Repository Templates
        ↓
Contextual Composition

Maturity Profiles
        ↓
Quality and Maintenance Expectations

Repository Implementations
        ↓
Consumer-specific Materialization
```

La conformidad se evalúa sobre responsabilidades.

No exclusivamente sobre disponibilidad física de Components.

Por tanto:

```text
Component Availability
        ≠
Consumer Conformance
```

Los Templates podrán incluir Components `Conceptual` cuando su responsabilidad pertenezca legítimamente al contrato.

Los consumidores podrán satisfacer esas responsabilidades mediante implementaciones equivalentes mientras respeten su propósito.

La validación mediante Reference Implementations y dogfooding proporciona evidencia para refinar:

- Components;
- Templates;
- Standards;
- arquitectura.

La RTL proporciona así una arquitectura:

- extensible;
- reutilizable;
- verificable;
- compatible con diferentes tipos de proyecto;
- preparada para automatización futura.

---

# 270. Part 6 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.

---

# 08 - REPOSITORY DESIGN SYSTEM

# Part 7/7

# RDS Governance, Validation & Evolution

---

# 271. Purpose

Esta Part define la gobernanza, validación y evolución del **Repository Design System (RDS)**.

Su objetivo consiste en garantizar que GitHub Framework:

- permanezca coherente;
- evolucione de forma controlada;
- mantenga fuentes canónicas identificables;
- gestione compatibilidad;
- pueda incorporar nuevas capacidades sin rediseños completos;
- valide sus decisiones mediante implementación real.

El RDS no constituye únicamente documentación arquitectónica.

Representa un producto mantenido que gobierna responsabilidades reutilizables, composición y evolución del Framework.

---

# 272. Governance Philosophy

Todo elemento mantenido por el RDS deberá evolucionar mediante cambios:

- pequeños cuando sea posible;
- revisables;
- trazables;
- documentados;
- versionados;
- compatibles cuando resulte razonable;
- respaldados por necesidades reales.

La arquitectura deberá favorecer:

```text
Reuse
        ↓
Refinement
        ↓
Extension
        ↓
New Capability
```

La creación de nuevas abstracciones deberá ser la última opción.

---

# 273. Framework Element Lifecycle

Todo elemento reutilizable mantenido por el RDS podrá evolucionar mediante un lifecycle controlado.

Modelo conceptual:

```text
Idea
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
Deprecation
        ↓
Retirement
```

Este lifecycle podrá aplicarse, según corresponda, a:

- Framework Components;
- Repository Templates;
- otras capacidades reutilizables gobernadas por el RDS.

La implementación no implica estabilidad automática.

La validación mediante uso real deberá producir evidencia suficiente antes de recomendar adopción general.

---

# 274. Lifecycle States

Los elementos oficiales podrán utilizar estados explícitos de evolución.

| State | Meaning |
| --- | --- |
| Draft | En diseño o implementación inicial |
| Experimental | Implementado y en validación |
| Stable | Validado para uso recomendado |
| Deprecated | Disponible por compatibilidad, pero sustituido |
| Retired | Fuera del catálogo activo |

El lifecycle status deberá mantenerse en la fuente canónica correspondiente.

No deberá inferirse únicamente a partir de:

- antigüedad;
- existencia física;
- número de consumidores;
- versión global de GitHub Framework.

---

# 275. Implementation Classification vs Lifecycle Status

La clasificación:

```text
Conceptual
Implemented
```

representa disponibilidad material.

Los estados:

```text
Draft
Experimental
Stable
Deprecated
Retired
```

representan lifecycle.

Por tanto:

```text
Implementation Classification
        ≠
Lifecycle Status
```

Ejemplo:

```text
WCL-CI
implementation: Implemented
status: Experimental
```

será válido cuando exista una materialización canónica pero todavía se encuentre en validación.

Un Component `Conceptual` no deberá presentarse como `Stable`.

---

# 276. Canonical Source Governance

Cada elemento reutilizable deberá mantener una fuente canónica identificable.

Modelo:

```text
RDS
        ↓
Architecture

Component Specification + Metadata
        ↓
Canonical Component Definition

Repository Template Specification + Metadata
        ↓
Canonical Template Definition

Component Catalog
        ↓
Discovery and Classification

Reference Implementation
        ↓
Validation Evidence
```

Las fuentes deberán mantenerse sincronizadas.

Cuando exista contradicción, deberá resolverse determinando qué artefacto es responsable de la información afectada.

---

# 277. Component Catalog Governance

El **Component Catalog** constituye el registro central de descubrimiento de Framework Components y Repository Templates.

Deberá proporcionar una vista global de:

- identificadores;
- familias;
- responsabilidades;
- priority;
- audience;
- maturity;
- implementation classification;
- lifecycle status;
- localización canónica;
- relaciones relevantes.

No deberá duplicar Specifications completas.

Las diferencias entre el Catalog y las fuentes canónicas deberán considerarse deuda del Design System.

---

# 278. Catalog Synchronization

Cuando un Component evolucione de:

```text
Conceptual
        ↓
Implemented
```

deberá sincronizarse el Component Catalog.

La sincronización deberá reflejar, según corresponda:

- Implementation;
- canonical location;
- status;
- version;
- metadata relevante;
- registry summary.

La actualización del catálogo no constituye por sí sola la implementación.

Deberá producirse como consecuencia de una fuente canónica real.

---

# 279. Repository Template Governance

Los Repository Templates deberán evolucionar independientemente cuando su contrato lo requiera.

La gobernanza deberá controlar:

- composición;
- requirement levels;
- maturity;
- versionado;
- lifecycle;
- compatibilidad;
- Reference Implementations;
- consumidores conocidos;
- gaps.

Un cambio en un Framework Component no obliga automáticamente a modificar todos los Templates que lo referencian.

Deberá evaluarse impacto real.

---

# 280. Workflow Component Governance

Los Workflow Components deberán respetar adicionalmente el contrato definido en la Workflow Component Library.

Todo `WCL-*` deberá mantener, cuando esté `Implemented`:

```text
Specification
        +
Metadata
        +
Sufficient Materialization
```

La gobernanza deberá verificar que el mecanismo de materialización corresponda a la responsabilidad.

No deberá exigir:

```text
GitHub Actions
```

como mecanismo universal.

Podrán coexistir Components:

- ejecutables;
- no ejecutables;
- configuracionales;
- basados en community files;
- basados en convenciones;
- compuestos.

---

# 281. Executable Workflow Governance

Los Workflow Components ejecutables deberán recibir especial atención debido a su impacto operativo.

Cuando corresponda deberán revisarse:

- permisos;
- secrets;
- triggers;
- third-party actions;
- dependency versions;
- outputs;
- failure behavior;
- logs;
- artifacts;
- portability;
- maintenance.

Los cambios que amplíen privilegios o superficie de ataque deberán tratarse como cambios relevantes incluso cuando no modifiquen la identidad del Component.

---

# 282. Workflow Materialization Evolution

Un Workflow Component podrá evolucionar su mecanismo de materialización sin cambiar necesariamente su responsabilidad.

Ejemplo:

```text
WCL-CI
        ↓
initial GitHub Actions workflow
        ↓
reusable workflow
```

podrá constituir una evolución compatible si el contrato permanece equivalente.

Sin embargo:

```text
Change in responsibility
```

podrá requerir:

- nueva versión;
- actualización de Specification;
- revisión de consumidores;
- posible cambio incompatible.

La materialización no deberá convertirse en la identidad del Component.

---

# 283. Framework Review Triggers

Los elementos del RDS deberán revisarse cuando:

- aparezca una necesidad real nueva;
- una Reference Implementation revele un gap;
- el dogfooding contradiga una decisión existente;
- se detecte duplicación;
- evolucione GitHub o una dependencia relevante;
- cambie el comportamiento de una plataforma;
- aparezca deuda de diseño;
- una Specification diverja de su implementación;
- la Metadata quede desincronizada;
- un Repository Template deje de representar correctamente a sus consumidores.

La revisión deberá producir cambios únicamente cuando exista evidencia suficiente.

---

# 284. Change Classification

Los cambios relevantes del RDS deberán clasificarse antes de aplicarse.

Podrán afectar a:

- arquitectura;
- Framework Component;
- Repository Template;
- Metadata;
- Catalog;
- Standard;
- Reference Implementation;
- consumer configuration;
- governance.

La clasificación ayuda a evitar cambios aplicados en el artefacto equivocado.

Ejemplo:

```text
Consumer problem
        ≠
Automatic Framework change
```

Primero deberá determinarse la naturaleza real del finding.

---

# 285. Gap Classification

Los findings podrán clasificarse como:

## Consumer Gap

El consumidor no satisface correctamente un contrato válido.

## Component Gap

La responsabilidad es correcta, pero el Component:

- no existe;
- permanece conceptual;
- tiene Specification insuficiente;
- tiene Metadata insuficiente;
- necesita mejor materialización.

## Template Gap

La composición o guidance del Repository Template es incorrecta o insuficiente.

## Standard Gap

Las reglas prácticas no cubren adecuadamente un patrón validado.

## Framework Gap

Existe una limitación arquitectónica transversal.

## Documentation Gap

La implementación es correcta, pero la documentación está incompleta o desactualizada.

La clasificación deberá preceder a la solución.

---

# 286. Reference Implementation Governance

Las Reference Implementations constituyen evidencia de validación.

No forman parte del contrato canónico de un Component o Template.

Deberán utilizarse para:

- comprobar responsabilidades;
- evaluar conformance;
- detectar gaps;
- validar materialización;
- comprobar dependencias;
- evaluar mantenibilidad;
- descubrir simplificaciones.

No deberán modificarse artificialmente únicamente para obtener un resultado `CONFORMANT`.

Los resultados iniciales no conformes pueden constituir evidencia valiosa.

---

# 287. Dogfooding Governance

GitHub Framework utilizará dogfooding cuando el propio repositorio sea un consumidor legítimo de la capacidad evaluada.

El dogfooding deberá seguir:

```text
Canonical Capability
        ↓
Consumer Adoption
        ↓
Validation
        ↓
Findings
        ↓
Refinement
```

No:

```text
Existing Practice
        ↓
Declare Component Implemented
```

La práctica previa del proyecto constituye evidencia potencial.

No sustituye la extracción y gobernanza de una capacidad reusable.

---

# 288. Validation Philosophy

La validación deberá comprobar contratos reales.

No únicamente estructuras.

Principio:

```text
Responsibility
        >
Filename
```

```text
Behavior
        >
Presence
```

```text
Conformance
        >
Visual Similarity
```

La validación deberá permitir detectar falsas conformidades producidas por archivos existentes que no satisfacen realmente la responsabilidad.

---

# 289. Framework Component Validation

La validación de un Framework Component podrá incluir:

- Specification review;
- Metadata validation;
- materialization review;
- dependency validation;
- consumer adoption;
- Reference Implementation;
- dogfooding;
- Quality Gates;
- execution testing cuando corresponda;
- security review para Components ejecutables.

El tipo de validación deberá adaptarse a la responsabilidad.

---

# 290. Workflow Component Validation

Los Workflow Components deberán validar adicionalmente su comportamiento operativo cuando corresponda.

Para Components ejecutables podrá incluir:

- trigger execution;
- success path;
- failure path;
- permissions;
- outputs;
- logs;
- compatibility;
- configurability.

Para Components no ejecutables podrá incluir:

- claridad;
- adopción;
- consistency;
- usability;
- absence of ambiguity;
- maintenance effort.

No se deberá utilizar una única estrategia de validación para todos los `WCL-*`.

---

# 291. Repository Validation

La validación de un repositorio deberá comprobar su conformidad con las responsabilidades que realmente le correspondan.

Modelo:

```text
Repository Template
        ↓
Required Components
        ↓
Consumer Materialization
        ↓
Conformance Analysis
        ↓
Findings
        ↓
Validation Result
```

La validación podrá incluir:

- README;
- documentación;
- workflows;
- metadata;
- visual responsibilities;
- governance;
- GRS Assessment cuando corresponda.

Los Components `recommended` y `optional` deberán evaluarse contextualmente.

---

# 292. Validation Evidence

Las decisiones de validación deberán estar respaldadas por evidencia suficiente.

La evidencia podrá incluir:

- archivos;
- Metadata;
- workflow runs;
- logs;
- test results;
- screenshots;
- reports;
- GitHub configuration;
- repository state;
- manual review results.

La cantidad de evidencia deberá ser proporcional al riesgo y complejidad.

No deberá generarse evidencia innecesaria únicamente para aumentar formalidad.

---

# 293. Conformance Results

Los procesos de validación podrán utilizar resultados como:

```text
CONFORMANT
PARTIAL
NON-CONFORMANT
```

cuando este vocabulario resulte aplicable.

Un resultado deberá acompañarse de:

- scope;
- responsabilidades evaluadas;
- gaps relevantes;
- decisiones;
- excepciones aceptadas cuando existan.

La conformidad deberá ser reproducible razonablemente por otro maintainer.

---

# 294. Quality Gate Philosophy

Los Quality Gates deberán proteger calidad real.

No deberán convertirse en checklists burocráticos.

Un Quality Gate deberá existir cuando permita detectar:

- inconsistencia;
- deuda;
- riesgo;
- duplicación;
- ausencia de responsabilidad;
- materialización insuficiente;
- dependencia incorrecta;
- problemas de mantenimiento;
- problemas de seguridad.

Los Quality Gates deberán evolucionar a partir de findings reales.

---

# 295. RDS Quality Gates

Antes de aprobar una evolución relevante del Repository Design System deberá verificarse:

- [ ] Las responsabilidades afectadas están correctamente identificadas.
- [ ] Los Framework Components afectados están registrados.
- [ ] Los Repository Templates afectados están sincronizados.
- [ ] La Metadata refleja la implementación real.
- [ ] El Component Catalog está alineado.
- [ ] La compatibilidad ha sido evaluada.
- [ ] Las fuentes canónicas no se contradicen.
- [ ] La documentación aplicable está actualizada.
- [ ] Los examples o Reference Implementations siguen siendo válidos.
- [ ] Los gaps encontrados están resueltos o registrados.
- [ ] La gobernanza refleja los cambios relevantes.
- [ ] No se ha introducido duplicación innecesaria.
- [ ] El cambio responde a una necesidad demostrada.

---

# 296. Definition of Done

Una capacidad reusable del Repository Design System se considerará suficientemente implementada cuando se cumplan los criterios aplicables.

## Specification

- [ ] Su responsabilidad está definida.
- [ ] Su alcance y límites son claros.
- [ ] La fuente canónica está identificada.

## Metadata

- [ ] Existe Metadata cuando corresponda.
- [ ] La Metadata está sincronizada.
- [ ] La identidad es estable.

## Implementation

- [ ] Existe materialización suficiente cuando la responsabilidad la requiere.
- [ ] No duplica responsabilidades existentes.
- [ ] Las dependencias reales están declaradas.
- [ ] La implementación es reusable razonablemente.

## Validation

- [ ] Existe evidencia de uso real, Reference Implementation o dogfooding cuando corresponde.
- [ ] Los gaps encontrados están resueltos o registrados.
- [ ] Los Quality Gates aplicables están satisfechos.

## Governance

- [ ] El cambio es trazable.
- [ ] El Catalog está sincronizado cuando corresponde.
- [ ] La documentación de gobierno está actualizada cuando corresponde.
- [ ] El versionado refleja cambios contractuales relevantes.

La automatización futura no constituye un requisito general para considerar implementada una responsabilidad que no la necesita.

---

# 297. Versioning Strategy

GitHub Framework utilizará Semantic Versioning para los artefactos versionables del RDS.

```text
Major.Minor.Patch
```

## Major

Cambios incompatibles en:

- responsabilidades;
- contratos;
- composición;
- arquitectura pública.

## Minor

Nuevas capacidades compatibles o ampliaciones significativas.

## Patch

Correcciones compatibles que no modifican sustancialmente el contrato.

Los Framework Components y Repository Templates podrán mantener versiones independientes.

---

# 298. Compatibility Policy

La evolución deberá preservar compatibilidad razonable siempre que sea posible.

Los cambios incompatibles deberán:

- estar justificados;
- reflejarse en versionado;
- documentarse;
- identificar consumidores;
- evaluar impacto;
- proporcionar guidance de migración cuando resulte necesario.

No deberá mantenerse compatibilidad con estructuras accidentales que nunca formaron parte de un contrato canónico.

---

# 299. Deprecation Policy

Cuando un Framework Component, Repository Template u otro elemento oficial sea sustituido:

- deberá evolucionar a `Deprecated`;
- permanecerá documentado durante un periodo razonable;
- indicará la alternativa recomendada;
- identificará implicaciones de migración;
- mantendrá compatibilidad temporal cuando sea viable.

La retirada definitiva se representará mediante:

```text
Retired
```

Un elemento no deberá desaparecer silenciosamente del Framework.

---

# 300. Ownership

Todo elemento mantenido por el RDS deberá tener ownership identificable.

Actualmente, el mantenimiento principal corresponde a:

```text
Owner
Fran Ramirez
```

En el futuro podrán existir:

- Maintainers;
- CODEOWNERS;
- responsables por familia;
- responsables por Component;
- responsables por Repository Template.

El ownership deberá permitir identificar quién puede:

- revisar;
- mantener;
- aprobar evolución;
- resolver inconsistencias;
- gestionar deprecations.

---

# 301. Design Debt

El propio Design System puede acumular deuda.

Ejemplos:

- Components redundantes;
- Templates obsoletos;
- documentación divergente;
- Metadata desincronizada;
- diagramas antiguos;
- Specifications que no reflejan implementación;
- definiciones canónicas duplicadas;
- Components conceptuales nunca reevaluados;
- workflows sin mantenimiento;
- Quality Gates desactualizados.

La deuda deberá gestionarse igual que deuda técnica.

Modelo:

```text
Detect
        ↓
Classify
        ↓
Prioritize
        ↓
Resolve
        ↓
Validate
```

---

# 302. Design Backlog

Las mejoras, gaps y deuda del RDS deberán registrarse mediante los mecanismos oficiales del proyecto.

Fuentes principales:

```text
GitHub Issues
+
docs/governance/14_BACKLOG.md
```

Los findings derivados de:

- dogfooding;
- Reference Implementations;
- auditorías;
- Component implementation;
- Template implementation;
- workflow execution;

deberán convertirse en trabajo trazable cuando requieran actuación.

No deberá mantenerse un backlog paralelo del RDS.

---

# 303. Repository Migration

Un repositorio existente podrá adoptar GitHub Framework de forma incremental.

Modelo:

```text
Repository Assessment
        ↓
Identify Project Type
        ↓
Select Repository Template
        ↓
Conformance Analysis
        ↓
Gap Classification
        ↓
Migration Plan
        ↓
Implementation
        ↓
Validation
```

Los gaps deberán distinguirse correctamente.

La migración no deberá perseguir conformidad mecánica.

Solo deberán incorporarse responsabilidades realmente aplicables.

---

# 304. Repository Audit

Los consumidores podrán revisarse periódicamente para detectar:

- divergencias respecto al Repository Template;
- Components desactualizados;
- documentación obsoleta;
- workflows rotos;
- Metadata inconsistente;
- deuda;
- problemas de seguridad;
- oportunidades de simplificación.

La frecuencia dependerá de:

- criticidad;
- actividad;
- madurez;
- ritmo de evolución;
- riesgo;
- necesidades de mantenimiento.

---

# 305. Maintenance Strategy

Los elementos del Framework deberán mantenerse mientras exista:

- responsabilidad válida;
- consumidor potencial;
- utilidad reusable;
- capacidad razonable de mantenimiento.

El mantenimiento podrá incluir:

- dependencia updates;
- documentation updates;
- compatibility review;
- security review;
- Reference Implementation review;
- Metadata synchronization;
- Quality Gate evolution.

Un elemento sin consumidores actuales podrá mantenerse si existe evidencia suficiente de utilidad futura.

No deberá conservarse indefinidamente únicamente por inercia.

---

# 306. Metrics

El RDS podrá utilizar métricas para evaluar su efectividad.

Entre ellas:

- reutilización de Components;
- adopción de Repository Templates;
- tiempo de bootstrap;
- conformance;
- gaps detectados;
- effort de mantenimiento;
- frecuencia de drift;
- workflow reliability;
- migraciones;
- deprecations.

Las métricas deberán ayudar a tomar decisiones.

No deberán convertirse en objetivos artificiales de cobertura.

---

# 307. Repository Health

GitHub Framework podrá incorporar mecanismos para evaluar el estado general de un repositorio.

Una evaluación futura podría considerar:

```text
Template Conformance
+
Maintenance
+
Documentation
+
Workflow Health
+
Quality
+
Security
+
Repository Activity
```

Los algoritmos y niveles concretos deberán validarse antes de constituir una capacidad oficial.

Repository Health continúa siendo una capacidad potencial.

No forma parte todavía del contrato estable del RDS.

---

# 308. Automation Roadmap

La evolución del Framework podrá automatizar progresivamente tareas basadas en contratos canónicos.

Entre ellas:

- Repository Template resolution;
- Component resolution;
- bootstrap;
- repository generation;
- README materialization;
- documentation generation;
- Workflow Component configuration;
- Metadata validation;
- Markdown validation;
- link validation;
- conformance analysis;
- assessment;
- release support;
- maintenance checks.

La automatización deberá consumir:

```text
Specifications
+
Metadata
+
Canonical Materializations
```

No deberá mantener arquitectura duplicada.

---

# 309. Workflow Automation Boundary

El Workflow Framework constituye una capa reusable previa a Framework Automation.

Por tanto:

```text
Workflow Component
        ↓
Reusable Operational Capability
        ↓
Framework Automation
        ↓
Programmatic Resolution / Generation / Validation
```

La futura automatización no deberá definir implícitamente qué es:

```text
WCL-CI
WCL-RELEASE
WCL-DOCUMENTATION-UPDATE
```

Esas responsabilidades deberán existir previamente como contratos canónicos.

Esto permite que automatización y arquitectura evolucionen de forma desacoplada.

---

# 310. Design System Evolution

La evolución del RDS se realizará incrementalmente.

Las capacidades reconocidas actualmente incluyen:

- README Components;
- Documentation Components;
- Workflow Components;
- Visual Components;
- Repository Templates;
- Maturity Profiles;
- Governance.

Su implementación física podrá avanzar a ritmos diferentes.

Las líneas futuras podrán incluir:

- ampliación de Component Libraries;
- Workflow Component implementation;
- Visual Component implementation;
- nuevos Repository Templates;
- validation tooling;
- Framework Automation;
- CLI;
- Repository Health;
- migration tooling;
- AI-assisted generation.

La planificación concreta pertenece al Roadmap y Product Backlog.

---

# 311. Repository Ecosystem

GitHub Framework está diseñado para soportar múltiples repositorios y tipos de proyecto.

Podrá ser consumido por:

- backend;
- full stack;
- documentation;
- GitHub Profile;
- learning projects;
- futuros tipos de proyecto.

Los consumidores podrán diferir en:

- tecnología;
- madurez;
- contexto;
- workflows;
- identidad visual;
- governance.

El Framework deberá reutilizar responsabilidades comunes sin borrar estas diferencias legítimas.

---

# 312. Repository Design Principles

El RDS mantendrá como principios operativos:

- reutilizar antes que duplicar;
- configurar antes que copiar;
- extender antes que crear;
- implementar antes que formalizar prematuramente;
- documentar antes que automatizar;
- automatizar antes que repetir;
- validar mediante uso real;
- evolucionar antes que reemplazar;
- mantener una única fuente canónica;
- separar responsabilidad de materialización;
- separar disponibilidad de conformance;
- evitar complejidad sin necesidad.

Estos principios deberán prevalecer sobre la búsqueda de cobertura total.

---

# 313. Global Anti-Patterns

No deberán aparecer:

- Components duplicados;
- Templates equivalentes incompatibles;
- Templates especulativos;
- Components conceptuales presentados como implementados;
- workflows específicos de un consumidor presentados como capacidad reusable;
- automation-driven architecture;
- Metadata desincronizada;
- múltiples fuentes de verdad;
- dependencias inventadas;
- requirement levels globales;
- Filesystem symmetry utilizada como objetivo arquitectónico;
- Quality Gates puramente burocráticos;
- conformidad conseguida mediante Components innecesarios;
- reglas de madurez utilizadas como composición rígida;
- prácticas sin mantenimiento;
- materialización insuficiente presentada como implementación completa.

---

# 314. Long-Term Vision

GitHub Framework deberá proporcionar una base reusable para construir, evolucionar y mantener repositorios técnicos.

El Repository Design System constituye su modelo arquitectónico para organizar:

- Framework Components;
- Repository Templates;
- Maturity Profiles;
- composition;
- materialization;
- conformance;
- validation;
- governance.

El objetivo no consiste únicamente en producir repositorios visualmente atractivos.

Consiste en crear un ecosistema:

- coherente;
- profesional;
- reusable;
- mantenible;
- verificable;
- extensible;
- preparado para automatización.

La automatización futura deberá ampliar este modelo.

No sustituirlo.

---

# 315. Final Conclusions

El **Repository Design System** proporciona el modelo arquitectónico central de GitHub Framework.

Los Standards definen reglas y criterios.

Los Framework Components encapsulan responsabilidades reutilizables.

Cada Component implementado dispone de:

```text
Specification
        +
Metadata
        +
Materialization when required
```

Los Repository Templates componen estas responsabilidades según tipos de proyecto.

Los Maturity Profiles expresan expectativas independientes de calidad y mantenimiento.

Los repositorios consumidores materializan las responsabilidades seleccionadas.

La validación determina conformance mediante evidencia.

La gobernanza controla evolución, compatibilidad y mantenimiento.

Modelo general:

```text
Standards
        ↓
Repository Design System
        ↓
Framework Components
        ↓
Repository Templates
        ↓
Repository Implementations
        ↓
Reference Implementations
        ↓
Validation and Evolution
```

La arquitectura distingue explícitamente:

```text
Responsibility
        ≠
Materialization
```

```text
Implementation
        ≠
Validation
```

```text
Component Availability
        ≠
Consumer Conformance
```

```text
Operational Sequence
        ≠
Structural Dependency
```

```text
Automation
        ≠
Architecture
```

Estas distinciones permiten que GitHub Framework evolucione sin imponer estructuras artificiales ni convertir prácticas específicas en contratos globales.

---

# 316. Next Evolution

Tras consolidar Repository Templates y definir el contrato arquitectónico de Workflow Components, la siguiente evolución consiste en materializar y validar capacidades operativas reales.

El flujo esperado es:

```text
Workflow Component Architecture
        ↓
Core Workflow Components
        ↓
Workflow Reference Implementation
        ↓
Dogfooding
        ↓
Workflow Standards
        ↓
Workflow Framework v0.5.0
```

La evolución deberá preservar el principio:

```text
Architecture
        ↓
Implementation
        ↓
Validation
        ↓
Standards
```

Los Standards no deberán formalizar patrones que todavía no hayan sido demostrados mediante implementación.

---

# 317. Revision History

| Version | Date | Description |
| --- | --- | --- |
| 1.0.0 | 2026-08-05 | Primera versión completa del Repository Design System. |
| 1.0.1 | 2026-08-11 | Metadata alineada con GitHub Framework durante la implementación de referencia del Documentation Framework. |
| 1.1.0 | 2026-08-14 | Arquitectura del RDS consolidada alrededor de Framework Components, Repository Templates, requirement levels contextuales, Maturity Profiles independientes y fuentes canónicas sincronizadas con la implementación. |
| 1.2.0 | 2026-08-19 | Contrato arquitectónico ampliado para Framework Components y Workflow Components, incluyendo materialization model, criterios `Conceptual → Implemented`, executable and non-executable workflows, conformance, validation y Quality Gates específicos. |
