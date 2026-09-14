# Workflow Component Standards

| Campo | Valor |
|---|---|
| **Proyecto** | GitHub Framework |
| **Documento** | Workflow Component Standards |
| **Versión** | 1.0.0 |
| **Estado** | Active |
| **Ámbito** | Workflow Component Library |
| **Última actualización** | 2026-09-13 |

---

# 1. Propósito

Este documento define los estándares oficiales para diseñar, implementar, adoptar, validar, mantener y evolucionar Workflow Components dentro de GitHub Framework.

Los estándares formalizan patrones validados mediante:

- Workflow Component Architecture;
- Core Workflow Components;
- Workflow Reference Implementation;
- dogfooding sobre el propio repositorio GitHub Framework.

El objetivo es proporcionar convenciones consistentes para la Workflow Component Library sin duplicar decisiones arquitectónicas ni introducir requisitos basados únicamente en escenarios hipotéticos.

```text
Architecture
      ↓
Implementation
      ↓
Dogfooding
      ↓
Validated Patterns
      ↓
Standards
```

Los Workflow Component Standards complementan la arquitectura.

La arquitectura define:

- qué representa un Workflow Component;
- sus responsabilidades;
- sus relaciones;
- sus límites;
- los mecanismos posibles de materialización.

Los estándares definen las reglas prácticas que deberán seguir las implementaciones concretas y su adopción por repositorios consumidores.

---

# 2. Alcance

Estos estándares aplican a los Workflow Components registrados dentro de GitHub Framework.

La primera implementación Core validada está formada por:

```text
WCL-ISSUE
WCL-BRANCH
WCL-COMMIT
WCL-PULL-REQUEST
WCL-CODE-REVIEW
```

El documento regula:

- identidad;
- naming;
- estructura;
- metadata;
- responsabilidad;
- materialización;
- artefactos;
- comportamiento ejecutable y no ejecutable;
- adopción;
- especialización;
- dependencias;
- clasificación de implementación;
- lifecycle;
- versionado;
- maturity;
- Reference Implementations;
- dogfooding;
- validación;
- mantenimiento;
- conformidad;
- Quality Gates;
- evolución.

La Workflow Component Library reconoce adicionalmente responsabilidades que permanecen `Conceptual`.

La existencia de dichas responsabilidades en el modelo NO implica que exista todavía una implementación canónica reutilizable ni evidencia suficiente para establecer reglas específicas sobre su materialización.

Quedan fuera del alcance normativo específico de esta versión:

- diseño detallado de pipelines CI;
- diseño detallado de pipelines CD;
- reusable GitHub Actions workflows;
- `workflow_call`;
- matrices de ejecución;
- estrategias específicas de deployment;
- gestión detallada de secrets;
- políticas específicas de environments;
- automatización de releases;
- resolución automática de dependencias;
- generación automática de Workflow Components;
- CLI;
- schema validation automatizada;
- mecanismos específicos de automatización todavía no validados.

Estos elementos podrán formalizarse cuando exista implementación y evidencia suficiente.

---

# 3. Lenguaje Normativo

Los términos normativos utilizados en este documento deberán interpretarse de la siguiente forma:

| Término | Significado |
|---|---|
| DEBE / DEBEN | Requisito obligatorio |
| NO DEBE / NO DEBEN | Prohibición |
| DEBERÍA / DEBERÍAN | Recomendación fuerte |
| NO DEBERÍA / NO DEBERÍAN | Práctica desaconsejada |
| PUEDE / PUEDEN | Comportamiento permitido |

Las reglas normativas DEBEN basarse en:

- arquitectura vigente;
- implementaciones reales;
- Reference Implementations;
- dogfooding;
- patrones observados y suficientemente validados.

Una posibilidad futura NO constituye por sí sola justificación suficiente para introducir una regla normativa.

Los Workflow Components que permanezcan `Conceptual` PUEDEN aportar contexto arquitectónico, pero NO DEBEN utilizarse como única evidencia para imponer detalles de implementación todavía no demostrados.

---

# 4. Principios

Todo Workflow Component DEBE respetar los siguientes principios.

## 4.1 Responsabilidad antes que artefacto

Un Workflow Component DEBE representar una responsabilidad reutilizable dentro del workflow de ingeniería.

```text
Workflow Component
        ↓
Reusable responsibility
        ↓
Possible materialization
```

Un Workflow Component NO DEBE definirse únicamente por la existencia de:

- un archivo;
- un directorio;
- una GitHub Action;
- una configuración;
- un script;
- una convención aislada.

La materialización deriva de la responsabilidad.

La responsabilidad NO deriva necesariamente de un artefacto físico concreto.

---

## 4.2 Workflow Component no implica automatización

Un Workflow Component NO DEBE interpretarse automáticamente como un workflow ejecutable.

```text
Workflow Component
        ≠
GitHub Action
        ≠
Executable workflow
```

Un Workflow Component PUEDE materializarse mediante:

- Convention;
- Community File;
- Configuration;
- Template;
- Documentation;
- executable workflow;
- combinación de varios mecanismos.

La ausencia de comportamiento ejecutable NO invalida un Workflow Component.

---

## 4.3 Implementación antes que estandarización

Las nuevas reglas DEBERÍAN surgir de patrones observados mediante implementación y validación.

```text
Observed behavior
        ↓
Implementation
        ↓
Validation
        ↓
Reusable rule
```

NO DEBERÍAN introducirse convenciones detalladas para mecanismos que todavía no hayan sido implementados o validados.

La existencia de una responsabilidad `Conceptual` NO obliga a definir anticipadamente su implementación.

---

## 4.4 Simplicidad

Un Workflow Component DEBE contener únicamente los elementos necesarios para expresar y materializar correctamente su responsabilidad.

NO DEBEN crearse:

- archivos vacíos;
- directorios vacíos;
- templates sin utilidad real;
- configuraciones artificiales;
- automatizaciones innecesarias;

únicamente para conseguir simetría estructural entre Components.

```text
Responsibility
      ↓
Minimum useful implementation
```

La consistencia conceptual tiene prioridad sobre la uniformidad física.

---

## 4.5 Reutilización antes que duplicación

Cuando una responsabilidad Workflow ya disponga de una definición canónica reutilizable, nuevas implementaciones DEBERÍAN adoptarla o especializarla antes de crear una definición paralela.

Un consumer NO DEBE necesitar copiar la especificación completa del Component para utilizarlo.

```text
Canonical Component
        ↓
Adoption
        ↓
Consumer specialization
```

Las diferencias propias del repositorio consumidor DEBERÍAN permanecer separadas de la responsabilidad canónica.

---

## 4.6 Materialización proporcional

La materialización física DEBE ser proporcional a la responsabilidad del Component.

Un Component PUEDE considerarse implementado sin disponer de un template o artefacto ejecutable cuando su responsabilidad se materialice suficientemente mediante otros mecanismos.

Ejemplos validados:

```text
WCL-BRANCH
→ Convention

WCL-COMMIT
→ Convention
```

Por tanto:

```text
Implemented
    ≠
Executable
```

y:

```text
Implemented
    ≠
Template required
```

---

## 4.7 Dogfooding

Los Workflow Components destinados a evolucionar hacia estados de lifecycle más estables DEBEN disponer de evidencia de utilización real o representativa.

Cuando GitHub Framework constituya un consumer adecuado, DEBERÍA utilizar sus propios Workflow Components mediante dogfooding.

El dogfooding DEBE utilizarse para comprobar el contrato y descubrir gaps reales, no únicamente para confirmar decisiones existentes.

---

# 5. Identidad

Todo Workflow Component registrado DEBE disponer de una identidad canónica única.

La identidad utiliza el prefijo:

```text
WCL-
```

Ejemplos:

```text
WCL-ISSUE
WCL-BRANCH
WCL-COMMIT
WCL-PULL-REQUEST
WCL-CODE-REVIEW
```

Un identificador DEBE:

- ser único dentro del Framework;
- utilizar mayúsculas;
- utilizar guiones para separar términos cuando sea necesario;
- representar una responsabilidad Workflow reconocible;
- permanecer estable durante la vida de la misma identidad conceptual;
- evitar referencias innecesarias a una tecnología concreta cuando la responsabilidad pueda expresarse de forma independiente.

El identificador NO DEBE representar:

- una versión;
- un nivel de maturity;
- un estado de lifecycle;
- una implementación específica del consumer.

Ejemplos no válidos:

```text
WCL-BRANCH-L2
WCL-COMMIT-STABLE
WCL-ISSUE-V2
```

Version, maturity y lifecycle se modelan como propiedades del Component.

---

# 6. Naming

Los directorios de Workflow Components DEBEN utilizar kebab-case.

Ejemplos:

```text
issue/
branch/
commit/
pull-request/
code-review/
```

La ubicación canónica es:

```text
framework/
└── components/
    └── workflow/
        └── <component-name>/
```

Los nombres DEBEN describir la responsabilidad y evitar detalles propios de un consumer concreto.

Ejemplo recomendado:

```text
code-review/
```

Ejemplo no recomendado:

```text
fran-code-review/
```

Los artefactos canónicos principales utilizan:

```text
README.md
metadata.yml
```

Los artefactos adicionales DEBEN utilizar nombres coherentes con:

- su mecanismo de materialización;
- las convenciones de la plataforma correspondiente;
- los estándares generales de GitHub Framework.

Cuando una plataforma exija un nombre convencional, dicho nombre PUEDE prevalecer sobre las reglas generales de naming.

Ejemplos:

```text
CODEOWNERS
PULL_REQUEST_TEMPLATE.md
config.yml
```

---

# 7. Estructura

La estructura mínima de un Workflow Component implementado es:

```text
<component-name>/
├── README.md
└── metadata.yml
```

`README.md` define la especificación canónica del Component.

`metadata.yml` proporciona su representación estructurada y machine-readable.

Un Workflow Component PUEDE incluir adicionalmente:

```text
templates/
```

cuando exista materialización física reutilizable que justifique su presencia.

Ejemplo:

```text
issue/
├── README.md
├── metadata.yml
└── templates/
    ├── bug_report.yml
    ├── config.yml
    └── feature_request.yml
```

La ausencia de `templates/` NO invalida un Workflow Component.

Ejemplo:

```text
branch/
├── README.md
└── metadata.yml
```

Un Component basado en una Convention PUEDE disponer de una implementación canónica válida sin artefactos físicos adicionales.

NO DEBEN crearse directorios `templates/` vacíos únicamente para mantener simetría entre Workflow Components.

La estructura física DEBE derivarse de la materialización real de la responsabilidad.

---

# 8. Metadata

Todo Workflow Component implementado DEBE disponer de:

```text
metadata.yml
```

La metadata DEBE representar estructuradamente el contrato básico del Component.

La estructura validada por los Core Workflow Components incluye:

```yaml
id:
name:
family:
version:
status:
priority:
audience:
maturity:
description:
dependencies:

materialization:
  primary:
  executable:

artifacts:
  specification:

adoption:
  specialization:

validation:
  dogfooding:
  reference_implementation:
```

Campos adicionales PUEDEN existir cuando la materialización concreta los requiera.

Por ejemplo:

```yaml
artifacts:
  specification: README.md
  templates:
    - templates/example.yml
```

o:

```yaml
adoption:
  target: .github/CODEOWNERS
  specialization: Required
```

## 8.1 Identity Metadata

Los campos:

```text
id
name
family
version
```

DEBEN identificar inequívocamente el Component.

Para esta biblioteca:

```yaml
family: Workflow
```

El `id` DEBE corresponder con la identidad canónica registrada en el Component Catalog.

---

## 8.2 Status

El campo:

```yaml
status:
```

representa el lifecycle del Component.

NO DEBE utilizarse para representar su clasificación de implementación.

Por tanto:

```text
status: Experimental
```

NO significa:

```text
Implementation: Conceptual
```

Un Workflow Component PUEDE estar simultáneamente:

```text
Implementation: Implemented
Lifecycle: Experimental
```

---

## 8.3 Materialization

La sección:

```yaml
materialization:
  primary:
  executable:
```

DEBE describir cómo se expresa principalmente la responsabilidad.

`primary` PUEDE contener uno o varios mecanismos.

Ejemplos validados:

```yaml
materialization:
  primary:
    - Convention
  executable: false
```

```yaml
materialization:
  primary:
    - Convention
    - Configuration
  executable: false
```

El campo:

```yaml
executable:
```

DEBE indicar si la implementación canónica contiene comportamiento ejecutable como parte de su materialización.

La ausencia de ejecución NO afecta por sí sola a la clasificación `Implemented`.

---

## 8.4 Artifacts

La sección:

```yaml
artifacts:
```

DEBE identificar los artefactos canónicos mantenidos por el Component.

Todo Workflow Component implementado DEBE identificar su especificación:

```yaml
artifacts:
  specification: README.md
```

Cuando existan templates u otros artefactos reutilizables, DEBERÍAN declararse explícitamente.

La metadata NO DEBE declarar artefactos inexistentes para mantener uniformidad con otros Components.

---

## 8.5 Adoption

La sección:

```yaml
adoption:
```

DEBE expresar las condiciones relevantes para utilizar el Component en un consumer.

Cuando exista una ubicación física convencional en el repositorio consumidor, PUEDE declararse mediante:

```yaml
target:
```

Ejemplo:

```yaml
adoption:
  target: .github/PULL_REQUEST_TEMPLATE.md
  specialization: Allowed
```

Cuando no exista un target físico único, `target` NO es obligatorio.

---

## 8.6 Specialization

La metadata DEBE indicar la política de especialización mediante:

```yaml
specialization:
```

Los valores utilizados por los Core Workflow Components validados son:

```text
Allowed
Required
```

`Allowed` indica que el consumer PUEDE adaptar la materialización manteniendo la responsabilidad canónica.

`Required` indica que la adopción necesita información o adaptación propia del consumer para producir una materialización válida.

La especialización NO DEBE interpretarse como permiso para redefinir la responsabilidad fundamental del Component.

---

## 8.7 Validation

La sección:

```yaml
validation:
  dogfooding:
  reference_implementation:
```

DEBE representar evidencia de validación del Component.

Ejemplo validado:

```yaml
validation:
  dogfooding: true
  reference_implementation: Validated
```

La validación es independiente del lifecycle.

Por tanto:

```text
Experimental
     +
Reference Implementation Validated
```

es un estado válido.

La finalización de una Reference Implementation NO DEBE provocar automáticamente una promoción a `Stable`.

---

## 8.8 Synchronization

`README.md` y `metadata.yml` DEBEN permanecer semánticamente sincronizados.

Las diferencias relevantes sobre:

- identidad;
- versión;
- lifecycle;
- priority;
- maturity;
- materialización;
- artefactos;
- dependencias;
- adopción;
- especialización;
- validación;

DEBEN considerarse defectos de consistencia.

La metadata NO DEBE utilizarse como una segunda especificación completa del Component.

```text
README
   ↓
Canonical specification

metadata.yml
   ↓
Structured representation
```

Cada artefacto mantiene una responsabilidad distinta y complementaria.

---

# 9. Responsibility Model

Un Workflow Component DEBE representar una responsabilidad reutilizable y suficientemente delimitada dentro del workflow de ingeniería de un repositorio.

```text
Engineering workflow
        ↓
Reusable responsibility
        ↓
Workflow Component
        ↓
Materialization
```

La responsabilidad constituye la identidad conceptual del Component.

Los artefactos utilizados para materializarla PUEDEN cambiar sin que necesariamente cambie dicha identidad.

## 9.1 Responsibility Boundary

Todo Workflow Component DEBE disponer de límites suficientemente claros para determinar:

- qué responsabilidad cubre;
- qué responsabilidades quedan fuera;
- cuándo debe utilizarse;
- cuándo no debe utilizarse;
- qué relaciones mantiene con otros Components.

Un Component NO DEBERÍA acumular responsabilidades independientes únicamente porque formen parte de una misma fase del workflow.

Ejemplo:

```text
Issue management
        ≠
Branch management
        ≠
Commit conventions
        ≠
Pull Request management
        ≠
Code Review
```

Estas responsabilidades pueden relacionarse dentro de un mismo flujo, pero mantienen identidades independientes.

---

## 9.2 Responsibility vs Materialization

La responsabilidad y su materialización DEBEN tratarse como dimensiones relacionadas pero diferentes.

```text
Responsibility
      ↓
defines what

Materialization
      ↓
defines how
```

Un cambio en la materialización NO implica necesariamente un cambio de responsabilidad.

Ejemplo conceptual:

```text
Code Review responsibility
        ↓
Convention
        +
CODEOWNERS
```

Una implementación futura podría utilizar mecanismos adicionales sin que ello requiera redefinir automáticamente `WCL-CODE-REVIEW`.

---

## 9.3 Responsibility vs Platform

Una responsabilidad Workflow DEBERÍA definirse con el menor acoplamiento razonable a una plataforma concreta.

La utilización actual de GitHub como plataforma principal NO DEBE provocar que una responsabilidad reutilizable se defina exclusivamente mediante una característica específica de GitHub cuando exista una abstracción más estable.

Sin embargo, el Framework NO DEBERÍA introducir abstracciones multiplataforma especulativas cuando no exista una necesidad real.

```text
Avoid unnecessary coupling
          +
Avoid speculative abstraction
          ↓
Minimum useful responsibility
```

Cuando la plataforma forme parte esencial de la materialización validada, dicha relación PUEDE documentarse explícitamente.

---

## 9.4 Responsibility Satisfaction

Un consumer satisface una responsabilidad cuando su implementación cumple efectivamente el contrato definido por el Workflow Component.

La satisfacción NO DEBE depender únicamente de:

- igualdad textual;
- igualdad de archivos;
- igualdad de estructura física;
- copia literal de un template;
- utilización exacta de la materialización canónica.

```text
Canonical Component
        ↓
Responsibility contract
        ↓
Consumer implementation
        ↓
Responsibility satisfied
```

Una implementación especializada o equivalente PUEDE satisfacer correctamente la responsabilidad cuando conserva su propósito y restricciones esenciales.

---

# 10. Materialization

La materialización describe cómo una responsabilidad Workflow se expresa mediante mecanismos concretos.

Un Workflow Component PUEDE utilizar uno o varios mecanismos de materialización.

Los mecanismos validados por los Core Workflow Components incluyen:

```text
Convention
Community File
Configuration
Template
```

Otros mecanismos, incluido comportamiento ejecutable, PUEDEN incorporarse cuando exista implementación y evidencia suficiente.

## 10.1 Primary Materialization

Todo Workflow Component implementado DEBE identificar su materialización primaria.

Ejemplos validados:

```text
WCL-ISSUE
→ Community File
→ Configuration

WCL-PULL-REQUEST
→ Community File

WCL-CODE-REVIEW
→ Convention
→ Configuration

WCL-BRANCH
→ Convention

WCL-COMMIT
→ Convention
```

La materialización primaria DEBE describir los mecanismos fundamentales utilizados para expresar la responsabilidad.

NO DEBE enumerar mecanismos únicamente porque sean técnicamente posibles.

---

## 10.2 Multiple Materializations

Un Workflow Component PUEDE necesitar más de un mecanismo de materialización.

```text
Responsibility
      ↓
 ┌────┴─────────┐
 │              │
Convention   Configuration
 │              │
 └──────┬───────┘
        ↓
Complete materialization
```

Cuando existan varios mecanismos, su combinación DEBE responder a una necesidad real del contrato.

La existencia de una configuración física NO elimina necesariamente la necesidad de una Convention asociada.

Del mismo modo, una Convention NO impide que existan artefactos físicos complementarios.

---

## 10.3 Physical Materialization

La materialización física PUEDE incluir:

- Community Files;
- archivos de configuración;
- templates;
- scripts;
- workflows ejecutables;
- otros artefactos reutilizables.

Cuando exista materialización física reutilizable propia del Component, DEBERÍA almacenarse dentro de su estructura canónica.

Ejemplo:

```text
pull-request/
├── README.md
├── metadata.yml
└── templates/
    └── PULL_REQUEST_TEMPLATE.md
```

Los artefactos físicos DEBEN existir porque materializan una responsabilidad real.

NO DEBEN crearse únicamente para demostrar que un Component está implementado.

---

## 10.4 Convention Materialization

Una Convention PUEDE constituir por sí misma la materialización principal de un Workflow Component.

Ejemplos validados:

```text
WCL-BRANCH
WCL-COMMIT
```

En estos casos, la implementación canónica DEBE definir con suficiente precisión:

- propósito;
- reglas;
- comportamiento esperado;
- ejemplos cuando aporten valor;
- límites;
- relaciones;
- criterios de validación.

```text
Convention
     +
Canonical specification
     +
Structured metadata
     ↓
Implemented Component
```

La ausencia de un artefacto adicional NO convierte automáticamente el Component en `Conceptual`.

---

## 10.5 Materialization Equivalence

Un consumer NO DEBE estar obligado a reproducir literalmente la materialización canónica cuando una implementación equivalente satisfaga la misma responsabilidad y la especialización esté permitida.

```text
Canonical materialization
           ≠
Mandatory literal copy
```

La equivalencia DEBERÍA evaluarse atendiendo a:

- responsabilidad satisfecha;
- comportamiento esperado;
- restricciones relevantes;
- evidencia disponible;
- política de especialización.

Cuando la equivalencia no resulte evidente, DEBERÍA documentarse durante la adopción o validación.

---

# 11. Executable vs Non-Executable Components

El comportamiento ejecutable constituye una propiedad de la materialización y NO una condición necesaria para ser Workflow Component.

```text
Workflow Component
        │
        ├── Non-Executable
        │
        └── Executable
```

Ambos modelos son válidos cuando representan responsabilidades Workflow reutilizables.

## 11.1 Non-Executable Components

Un Workflow Component no ejecutable PUEDE materializarse mediante:

- Convention;
- Community File;
- Configuration;
- Template;
- Documentation;
- combinación de estos mecanismos.

Los cinco Core Workflow Components actualmente implementados han demostrado que una biblioteca Workflow útil puede contener Components no ejecutables.

Por tanto:

```text
Non-Executable
      ≠
Conceptual
```

y:

```text
Non-Executable
      ≠
Incomplete
```

La validez del Component depende de la suficiencia de su contrato e implementación.

---

## 11.2 Executable Components

Un Workflow Component PUEDE contener comportamiento ejecutable cuando su responsabilidad lo requiera.

Ejemplos conceptuales de responsabilidades que podrían necesitarlo incluyen:

```text
CI
CD
Release Automation
Security Automation
Maintenance Automation
```

La existencia conceptual de estas responsabilidades NO establece todavía reglas específicas sobre:

- plataforma de ejecución;
- triggers;
- jobs;
- matrices;
- permissions;
- secrets;
- environments;
- reusable workflows;
- estrategia de ejecución.

Dichas reglas DEBERÁN derivarse de futuras implementaciones y validaciones.

---

## 11.3 Executability Metadata

La metadata DEBE declarar explícitamente:

```yaml
materialization:
  executable: true
```

o:

```yaml
materialization:
  executable: false
```

según corresponda a la implementación canónica.

Este valor NO DEBE inferirse únicamente a partir del nombre del Component.

---

## 11.4 Implementation Classification

La clasificación `Implemented` NO DEBE depender de que:

```yaml
executable: true
```

Un Component no ejecutable PUEDE estar completamente implementado.

```text
Implementation classification
          ≠
Executability
```

La clasificación de implementación se determina por la existencia de una implementación canónica suficiente para representar y reutilizar la responsabilidad.

---

# 12. Artifacts

Los artefactos son las materializaciones físicas mantenidas por un Workflow Component.

Todo Workflow Component implementado DEBE disponer de:

```text
README.md
metadata.yml
```

Estos dos archivos tienen responsabilidades diferentes.

```text
README.md
    ↓
Canonical specification

metadata.yml
    ↓
Structured representation
```

## 12.1 Specification

`README.md` DEBE actuar como especificación canónica del Component.

DEBERÍA explicar, cuando resulte aplicable:

- propósito;
- responsabilidad;
- cuándo utilizarlo;
- cuándo no utilizarlo;
- materialización;
- reglas;
- adopción;
- especialización;
- relaciones;
- dependencias;
- mantenimiento;
- validación;
- Quality Gates;
- estado.

No todas las secciones son obligatorias cuando no aporten valor.

---

## 12.2 Reusable Artifacts

Un Workflow Component PUEDE proporcionar artefactos reutilizables adicionales.

Ejemplos validados:

```text
bug_report.yml
feature_request.yml
config.yml
PULL_REQUEST_TEMPLATE.md
CODEOWNERS
```

Estos artefactos DEBEN:

- materializar una parte real de la responsabilidad;
- ser reutilizables;
- evitar información específica de un único consumer salvo mediante placeholders;
- permanecer coherentes con la especificación canónica;
- permitir la especialización definida por el Component.

---

## 12.3 Templates

Los templates DEBEN representar materializaciones reutilizables y no copias de una implementación concreta.

La información necesariamente específica del consumer DEBERÍA expresarse mediante placeholders cuando resulte apropiado.

Ejemplo:

```text
<OWNER>
<TEAM>
<PROJECT_SPECIFIC_VALUE>
```

Los placeholders DEBEN:

- ser identificables;
- utilizar nombres descriptivos;
- evitar ambigüedad;
- mantenerse al mínimo necesario.

Un Component NO DEBE incluir un template si su responsabilidad puede expresarse correctamente sin él.

---

## 12.4 Platform-Conventional Artifacts

Cuando una plataforma utilice nombres o ubicaciones convencionales, el Component PUEDE proporcionar artefactos compatibles con dichas convenciones.

Ejemplos:

```text
.github/ISSUE_TEMPLATE/
.github/PULL_REQUEST_TEMPLATE.md
.github/CODEOWNERS
```

La ubicación canónica dentro del Framework y el destino de adopción son responsabilidades diferentes.

```text
Framework canonical artifact
          ↓
Adoption
          ↓
Consumer platform location
```

El artefacto reutilizable DEBERÍA mantenerse junto al Component.

Su destino en el consumer DEBERÍA declararse mediante las reglas de adopción cuando resulte necesario.

---

# 13. Adoption

La adopción es el proceso mediante el cual un repositorio consumidor satisface la responsabilidad definida por un Workflow Component.

```text
Workflow Component
        ↓
Canonical contract
        ↓
Adoption
        ↓
Consumer implementation
```

La adopción NO implica necesariamente copiar literalmente los artefactos canónicos.

## 13.1 Adoption Mechanisms

Un consumer PUEDE adoptar un Workflow Component mediante:

- utilización directa de un artefacto canónico;
- copia y especialización permitida;
- configuración equivalente;
- aplicación de una Convention;
- implementación propia compatible;
- combinación de varios mecanismos.

El mecanismo elegido DEBE satisfacer la responsabilidad y respetar las restricciones del Component.

---

## 13.2 Adoption Target

Cuando la materialización requiera una ubicación específica en el consumer, el Component PUEDE declarar:

```yaml
adoption:
  target:
```

Ejemplos:

```text
.github/ISSUE_TEMPLATE/
.github/PULL_REQUEST_TEMPLATE.md
.github/CODEOWNERS
```

El `target` representa el destino esperado de adopción.

NO representa necesariamente la ubicación del artefacto dentro de GitHub Framework.

---

## 13.3 Convention Adoption

Los Components materializados principalmente mediante Convention NO necesitan disponer de un `target` físico.

Ejemplo:

```text
WCL-BRANCH
        ↓
Branch naming and lifecycle convention
        ↓
Applied through repository practice
```

La adopción DEBE poder demostrarse mediante evidencia suficiente.

Ejemplos de evidencia:

```text
Git branch history
Git commit history
Repository configuration
Community Files
Pull Requests
Issues
```

La ausencia de un archivo específico NO implica ausencia de adopción.

---

## 13.4 Adoption vs Canonical Implementation

La implementación canónica proporciona una referencia reutilizable.

El consumer conserva responsabilidad sobre su adopción concreta.

```text
Canonical implementation
          ↓
Reusable baseline
          ↓
Consumer adoption
          ↓
Contextual implementation
```

La implementación canónica NO DEBE incorporar información propia de un consumer concreto únicamente para facilitar una adopción determinada.

---

# 14. Specialization

La especialización permite adaptar un Workflow Component al contexto de un repositorio consumidor sin redefinir su responsabilidad fundamental.

```text
Canonical responsibility
        ↓
Specialization
        ↓
Consumer-specific implementation
```

La especialización PUEDE afectar a:

- contenido;
- owners;
- labels;
- instrucciones;
- campos;
- ejemplos;
- convenciones contextuales;
- configuraciones;
- integración con procesos propios del consumer.

La especialización NO DEBE modificar la identidad fundamental del Component.

---

## 14.1 Allowed Specialization

Cuando:

```yaml
specialization: Allowed
```

el consumer PUEDE adaptar la implementación canónica cuando su contexto lo requiera.

La adaptación DEBE conservar:

- responsabilidad;
- propósito;
- restricciones esenciales;
- compatibilidad conceptual con el Component.

Ejemplos validados incluyen la especialización de:

```text
WCL-ISSUE
WCL-PULL-REQUEST
```

mediante contenido específico del repositorio consumidor.

---

## 14.2 Required Specialization

Cuando:

```yaml
specialization: Required
```

la implementación canónica necesita información contextual del consumer para convertirse en una adopción válida.

Ejemplo validado:

```text
WCL-CODE-REVIEW
        ↓
CODEOWNERS
        ↓
Consumer-specific owners required
```

El Framework NO DEBE incorporar valores específicos de un consumer dentro del artefacto canónico únicamente para eliminar esta necesidad de especialización.

---

## 14.3 Specialization vs Divergence

Una especialización válida conserva la responsabilidad canónica.

```text
Specialization
      ≠
Responsibility redefinition
```

Si una adaptación modifica sustancialmente:

- propósito;
- límites;
- comportamiento esperado;
- responsabilidad principal;

DEBERÍA evaluarse si representa:

- otro Workflow Component;
- una responsabilidad adicional;
- una implementación no conforme.

La especialización NO DEBE utilizarse para mantener forks divergentes de la especificación canónica.

---

## 14.4 Canonical vs Consumer Content

La implementación canónica DEBERÍA contener únicamente aquello que sea reutilizable.

El consumer DEBERÍA proporcionar aquello que pertenezca exclusivamente a su contexto.

```text
Canonical
├── reusable responsibility
├── reusable structure
└── reusable defaults

Consumer
├── project-specific values
├── owners
├── contextual instructions
└── justified specialization
```

Esta separación reduce acoplamiento y evita que la implementación canónica se convierta en una copia del repositorio utilizado para dogfooding.

---

# 15. Dependencies

Un Workflow Component PUEDE declarar dependencias cuando su responsabilidad necesite otra responsabilidad reconocida para funcionar o resultar coherente.

Las dependencias DEBEN expresarse mediante IDs canónicos cuando correspondan a Framework Components.

Ejemplo conceptual:

```yaml
dependencies:
  - WCL-ISSUE
```

Una dependencia DEBE representar una necesidad real del contrato.

NO DEBE utilizarse únicamente para describir:

- proximidad conceptual;
- orden habitual del workflow;
- relación temática;
- una posible integración futura.

---

## 15.1 Dependency vs Sequence

La existencia de una secuencia habitual NO implica automáticamente dependencia.

```text
Issue
  ↓
Branch
  ↓
Commit
  ↓
Pull Request
  ↓
Code Review
```

Este flujo representa una relación frecuente entre responsabilidades.

NO significa necesariamente:

```text
WCL-BRANCH depends on WCL-ISSUE
WCL-COMMIT depends on WCL-BRANCH
WCL-PULL-REQUEST depends on WCL-COMMIT
```

Una dependencia DEBE declararse únicamente cuando el contrato del Component la necesite realmente.

---

## 15.2 Dependency Satisfaction

Cuando exista una dependencia, el consumer DEBERÍA satisfacer la responsabilidad correspondiente mediante:

- implementación canónica;
- implementación propia compatible;
- especialización;
- mecanismo equivalente.

La satisfacción conceptual de una dependencia NO exige necesariamente una copia física de otro Component.

```text
Dependency
     ↓
Required responsibility
     ↓
Satisfied by consumer
```

---

## 15.3 Dependency Minimalism

Las dependencias DEBEN mantenerse al mínimo necesario.

Un Workflow Component DEBERÍA poder adoptarse independientemente cuando su responsabilidad no requiera realmente otros Components.

NO DEBERÍAN construirse cadenas de dependencias únicamente para representar el workflow completo del repositorio.

```text
Related
   ≠
Dependent
```

Este principio reduce:

- acoplamiento;
- adopción forzada;
- complejidad;
- propagación innecesaria de cambios.

---

## 15.4 No Automatic Dependency Resolution

La declaración de dependencias NO implica actualmente:

- instalación automática;
- resolución transitiva automática;
- generación de archivos;
- modificación automática del consumer;
- validación automática de dependencias.

```text
Dependency declaration
          ↓
Contract information
```

La resolución automática de dependencias queda fuera del alcance de estos estándares mientras no exista implementación y evidencia suficiente que justifique dicho mecanismo.

---

# 16. Implementation Classification

Todo Workflow Component reconocido por GitHub Framework DEBE distinguir su clasificación de implementación de otras dimensiones como lifecycle, maturity o validation.

Las clasificaciones actualmente reconocidas son:

```text
Conceptual
Implemented
```

## 16.1 Conceptual

Un Workflow Component `Conceptual` representa una responsabilidad reconocida por la arquitectura y el Component Catalog para la que todavía no existe una implementación canónica reutilizable suficiente dentro del Framework.

```text
Recognized responsibility
          +
No canonical reusable implementation
          ↓
Conceptual
```

Un Component `Conceptual` PUEDE:

- formar parte del modelo arquitectónico;
- mantener un ID canónico;
- relacionarse con otros Components;
- orientar futuras implementaciones;
- ser satisfecho por un consumer mediante una implementación propia.

La existencia de una implementación específica en un repositorio consumidor NO convierte automáticamente el Component en `Implemented`.

La transición:

```text
Conceptual
    ↓
Implemented
```

requiere una implementación canónica gobernada por GitHub Framework.

---

## 16.2 Implemented

Un Workflow Component se clasifica como `Implemented` cuando GitHub Framework dispone de una implementación canónica suficiente para:

- definir su responsabilidad;
- permitir su reutilización;
- expresar estructuradamente su contrato;
- identificar su materialización;
- establecer sus reglas de adopción.

La implementación mínima DEBE disponer de:

```text
README.md
metadata.yml
```

y PUEDE incluir artefactos adicionales cuando su materialización lo requiera.

`Implemented` NO significa necesariamente:

```text
Executable
Template available
Stable
Reference Implementation Validated
Automated
```

Por tanto, son combinaciones válidas:

```text
Implemented + Non-Executable
Implemented + Experimental
Implemented + Reference Implementation Pending
Implemented + Reference Implementation Validated
```

---

## 16.3 Implementation vs Materialization

La clasificación de implementación NO DEBE derivarse de un mecanismo concreto de materialización.

Los siguientes modelos PUEDEN representar Components implementados:

```text
Specification
    +
Metadata
    +
Convention
```

```text
Specification
    +
Metadata
    +
Configuration
```

```text
Specification
    +
Metadata
    +
Template
```

o futuras combinaciones suficientemente validadas.

La existencia de un archivo ejecutable NO convierte automáticamente una responsabilidad conceptual en un Workflow Component implementado.

Primero DEBE existir un contrato canónico gobernado por el Framework.

---

## 16.4 Implementation Classification vs Lifecycle

La clasificación de implementación y el lifecycle son dimensiones independientes.

```text
Implementation classification
          ≠
Lifecycle
```

Ejemplo validado:

```text
Implementation: Implemented
Lifecycle: Experimental
```

El lifecycle describe el grado de estabilidad y evolución del contrato.

La clasificación de implementación describe la disponibilidad de una implementación canónica reutilizable.

---

## 16.5 Implementation Classification vs Validation

La clasificación de implementación y la validación también son dimensiones independientes.

```text
Implemented
     ↓
may still require
     ↓
Reference Implementation
```

Un Component PUEDE estar `Implemented` antes de haber sido validado mediante una Reference Implementation.

La validación posterior NO cambia automáticamente su clasificación de implementación.

---

# 17. Lifecycle

Todo Workflow Component implementado DEBE declarar un estado de lifecycle.

Los estados reconocidos por el modelo vigente son:

```text
Draft
Experimental
Stable
Deprecated
Retired
```

El flujo habitual es:

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

Las transiciones NO DEBEN producirse automáticamente por:

- antigüedad;
- número de commits;
- número de versiones;
- finalización de un Sprint;
- finalización de una milestone;
- existencia de materialización física.

El lifecycle DEBE basarse en evidencia sobre la definición, implementación, validación, reutilización y mantenimiento del Component.

---

## 17.1 Draft

Un Workflow Component `Draft` se encuentra en especificación o implementación inicial.

PUEDE utilizarse para explorar:

- responsabilidad;
- límites;
- metadata;
- materialización;
- adopción;
- dependencias.

Un Component `Draft` NO DEBE presentarse como una implementación reutilizable suficientemente definida para adopción general.

Su contrato PUEDE cambiar significativamente.

---

## 17.2 Experimental

Un Workflow Component `Experimental` dispone de una implementación utilizable cuyo contrato todavía puede evolucionar a partir de evidencia real.

Un Component `Experimental`:

- PUEDE utilizarse en consumers reales;
- PUEDE utilizarse mediante dogfooding;
- PUEDE actuar en una Reference Implementation;
- PUEDE haber completado una Reference Implementation;
- PUEDE descubrir nuevos gaps durante futuras adopciones;
- DEBE mantener explícitas las limitaciones relevantes conocidas.

Por tanto:

```text
Experimental
     +
Reference Implementation Validated
```

es una combinación válida.

La finalización de una Reference Implementation NO obliga a promover el Component a `Stable`.

---

## 17.3 Stable

Un Workflow Component PUEDE evolucionar a `Stable` cuando exista evidencia suficiente de que su contrato es:

- claro;
- consistente;
- reutilizable;
- suficientemente validado;
- mantenible.

Antes de promover un Component a `Stable`, DEBERÍA comprobarse como mínimo que:

- su responsabilidad está claramente delimitada;
- su identidad es estable;
- README y metadata están sincronizados;
- su materialización es suficiente;
- sus reglas de adopción son comprensibles;
- las especializaciones necesarias están correctamente modeladas;
- las dependencias relevantes son coherentes;
- sus Quality Gates pueden evaluarse;
- existe evidencia representativa de adopción, dogfooding o Reference Implementation;
- no existen gaps críticos conocidos sin resolver o aceptar explícitamente;
- no existen contradicciones conocidas con la arquitectura vigente.

Una única Reference Implementation validada NO DEBE considerarse automáticamente evidencia suficiente para promoción.

---

## 17.4 Deprecated

Un Workflow Component DEBE marcarse como `Deprecated` cuando permanezca registrado por compatibilidad o trazabilidad pero ya no deba recomendarse para nuevas adopciones.

La deprecación DEBERÍA indicar:

- motivo;
- alternativa recomendada, cuando exista;
- impacto sobre consumers;
- estrategia de transición cuando resulte necesaria.

Un Component Deprecated NO DEBE eliminarse inmediatamente cuando su contrato siga siendo relevante para consumers existentes.

---

## 17.5 Retired

Un Workflow Component `Retired` NO DEBE utilizarse para nuevas adopciones.

Su definición PUEDE conservarse cuando sea necesaria para:

- trazabilidad;
- migraciones;
- consumidores históricos;
- comprensión de la evolución del Framework.

Un Component NO DEBERÍA evolucionar directamente a `Retired` sin pasar por `Deprecated`, salvo que exista una razón excepcional documentada.

---

## 17.6 Lifecycle Transitions

Las transiciones relevantes DEBEN quedar documentadas.

```text
Draft → Experimental
      ↓
canonical implementation available

Experimental → Stable
      ↓
sufficient validation evidence

Stable → Deprecated
      ↓
deprecation rationale

Deprecated → Retired
      ↓
retirement decision
```

Un nuevo estado de lifecycle NO DEBERÍA introducirse sin una necesidad validada.

---

# 18. Versioning

Todo Workflow Component implementado DEBE declarar una versión propia.

```yaml
version: 0.1.0
```

La versión del Component es independiente de la versión global de GitHub Framework.

```text
GitHub Framework version
          ≠
Workflow Component version
```

Los Workflow Components DEBEN utilizar Semantic Versioning como referencia para expresar la evolución de su contrato.

```text
MAJOR.MINOR.PATCH
```

## 18.1 PATCH

Un incremento `PATCH` DEBERÍA utilizarse para cambios compatibles que no modifiquen materialmente el contrato.

Ejemplos:

- correcciones de redacción;
- aclaraciones;
- corrección de ejemplos;
- correcciones de metadata sin impacto contractual;
- mejoras documentales equivalentes.

---

## 18.2 MINOR

Un incremento `MINOR` DEBERÍA utilizarse cuando el Component evolucione de forma compatible.

Ejemplos:

- ampliación compatible de reglas;
- incorporación de artefactos reutilizables opcionales;
- mejora de instrucciones de adopción;
- incorporación de mecanismos compatibles de materialización;
- ampliación compatible de metadata;
- nuevas especializaciones compatibles.

Los cambios `MINOR` NO DEBERÍAN invalidar consumers previamente conformes.

---

## 18.3 MAJOR

Un incremento `MAJOR` DEBE considerarse cuando cambie de forma incompatible el contrato del Component.

Ejemplos:

- redefinición sustancial de la responsabilidad;
- cambio incompatible de reglas obligatorias;
- eliminación de una forma de adopción previamente válida;
- modificación incompatible de metadata obligatoria;
- cambio de una política de especialización que invalide consumers existentes;
- cambio incompatible de materialización cuando forme parte esencial del contrato.

Antes de introducir un cambio `MAJOR`, DEBERÍA existir evidencia suficiente que justifique la ruptura de compatibilidad.

---

## 18.4 Version Synchronization

La versión declarada en `metadata.yml` y cualquier referencia equivalente dentro de la especificación DEBEN permanecer sincronizadas.

Las diferencias de versión entre artefactos del mismo Component DEBEN considerarse un defecto de consistencia.

La versión global del Framework NO DEBE copiarse automáticamente a cada Workflow Component.

---

# 19. Maturity

Todo Workflow Component implementado DEBE declarar su nivel de maturity conforme al modelo general de GitHub Framework.

Ejemplo:

```yaml
maturity: L2
```

La maturity expresa el nivel de sofisticación o profundidad esperado de la responsabilidad.

NO representa:

- la versión;
- el lifecycle;
- la clasificación de implementación;
- el estado de validación.

```text
Maturity
   ≠
Lifecycle
   ≠
Implementation
   ≠
Validation
```

## 19.1 Maturity as a Property

La maturity DEBE mantenerse como propiedad del Component.

NO DEBEN crearse identidades diferentes cuya única diferencia sea su maturity.

Ejemplo no recomendado:

```text
WCL-ISSUE-L1
WCL-ISSUE-L2
WCL-ISSUE-L3
```

La identidad permanece:

```text
WCL-ISSUE
```

y su maturity evoluciona como propiedad cuando exista justificación.

---

## 19.2 Maturity Evolution

La maturity DEBERÍA evolucionar únicamente cuando exista evidencia suficiente de que la responsabilidad requiere un nivel diferente de sofisticación.

Un cambio de maturity NO DEBE utilizarse como mecanismo indirecto para redefinir la responsabilidad.

Cuando una evolución de maturity modifique materialmente el contrato, DEBERÁ evaluarse también su impacto sobre:

- versioning;
- consumers existentes;
- documentación;
- lifecycle.

---

# 20. Consumer Adoption and Conformance

La conformidad de un consumer con un Workflow Component DEBE evaluarse sobre la responsabilidad efectivamente satisfecha.

```text
Workflow Component
        ↓
Responsibility contract
        ↓
Consumer implementation
        ↓
Conformance assessment
```

La conformidad NO DEBE evaluarse únicamente mediante comparación física con la implementación canónica.

## 20.1 Responsibility-Based Conformance

Un consumer es conforme cuando satisface la responsabilidad definida por el Component respetando sus restricciones aplicables.

La evaluación DEBE considerar:

- propósito;
- comportamiento esperado;
- reglas obligatorias;
- materialización relevante;
- especialización;
- dependencias aplicables;
- evidencia observable.

```text
Same responsibility satisfied
          ↓
Possible conformance
```

aunque:

```text
Physical implementation differs
```

---

## 20.2 Canonical Artifact vs Consumer Artifact

Un artefacto consumer NO necesita ser textualmente idéntico al artefacto canónico cuando la especialización esté permitida o requerida.

Ejemplos validados mediante dogfooding:

```text
Canonical Issue Forms
          ≠
GitHub Framework Issue Forms
```

```text
Canonical Pull Request Template
          ≠
GitHub Framework Pull Request Template
```

Las diferencias contextuales son válidas cuando ambas implementaciones mantienen la misma responsabilidad.

Por tanto:

```text
Textual difference
        ≠
Non-conformance
```

---

## 20.3 Convention Conformance

Los Components materializados mediante Convention DEBEN evaluarse mediante evidencia de práctica real.

Ejemplos:

```text
WCL-BRANCH
→ branch names
→ branch lifecycle
→ Git history

WCL-COMMIT
→ commit messages
→ Git history
```

La ausencia de un archivo de configuración específico NO implica no conformidad.

---

## 20.4 Required Specialization Conformance

Cuando:

```yaml
specialization: Required
```

la conformidad requiere que el consumer proporcione la información contextual necesaria.

Ejemplo:

```text
Canonical CODEOWNERS
        ↓
Reusable structure
        +
Consumer owners
        ↓
Valid adoption
```

Una copia literal que conserve placeholders sin resolver NO DEBERÍA considerarse una adopción completa cuando dichos valores sean necesarios para satisfacer la responsabilidad.

---

## 20.5 Equivalent Implementations

Una implementación equivalente PUEDE considerarse conforme cuando:

- satisface la misma responsabilidad;
- respeta las restricciones obligatorias;
- puede identificarse y evaluarse;
- proporciona evidencia suficiente;
- no contradice la política de especialización.

La equivalencia NO DEBE utilizarse para justificar la ausencia de una responsabilidad realmente requerida.

Cuando no resulte evidente, DEBERÍA documentarse.

---

## 20.6 Adoption vs Availability

La disponibilidad de una implementación canónica y la satisfacción de una responsabilidad por un consumer son dimensiones diferentes.

```text
Framework availability
        ≠
Consumer conformance
```

Un consumer PUEDE disponer de una implementación propia de una responsabilidad cuyo Component permanezca `Conceptual`.

Esto NO convierte automáticamente el Component en `Implemented`.

Del mismo modo, la existencia de un Component `Implemented` NO garantiza que el consumer lo haya adoptado correctamente.

---

# 21. Reference Implementations

Una Reference Implementation es una adopción real o representativa utilizada para validar un Workflow Component frente a un contexto concreto.

Su función principal es proporcionar evidencia.

```text
Workflow Component
        ↓
Reference Implementation
        ↓
Evidence
        ↓
Findings
        ↓
Framework refinement
```

Una Reference Implementation NO DEBE tratarse como una copia normativa que todos los consumers deban reproducir.

Su función consiste en comprobar si el contrato funciona cuando se aplica.

## 21.1 Selection

La Reference Implementation DEBERÍA utilizar un contexto realista y suficientemente representativo.

Cuando el propio GitHub Framework constituya un consumer adecuado, PUEDE actuar como Reference Implementation mediante dogfooding.

DEBERÍA evitarse crear un consumer artificial únicamente para conseguir una validación positiva.

---

## 21.2 Evidence

La validación DEBERÍA obtener evidencia adecuada al mecanismo de materialización.

Ejemplos:

```text
Community File
→ consumer file

Configuration
→ repository configuration

Convention
→ observable repository practice

Template
→ adopted and specialized artifact

Executable workflow
→ execution evidence
```

El tipo de evidencia DEBE adaptarse al Component.

NO DEBE exigirse el mismo tipo de evidencia a todos los Workflow Components.

---

## 21.3 Findings

Los findings de una Reference Implementation PUEDEN identificar:

```text
Consumer gap
Component gap
Architecture gap
Documentation drift
Expected specialization
Validation gap
```

Un finding NO DEBE provocar automáticamente una modificación.

Primero DEBE clasificarse y determinarse qué capa es responsable.

```text
Finding
   ↓
Classify
   ↓
Evaluate
   ↓
Change only responsible layer
```

---

## 21.4 Reference Implementation Result

Una Reference Implementation DEBERÍA registrar un resultado suficientemente claro.

La metadata PUEDE representar dicho resultado mediante:

```yaml
validation:
  reference_implementation: Pending
```

o:

```yaml
validation:
  reference_implementation: Validated
```

La transición:

```text
Pending
   ↓
Validated
```

indica que se ha obtenido evidencia suficiente para la validación definida.

NO representa automáticamente una transición de lifecycle.

---

# 22. Dogfooding

GitHub Framework DEBERÍA utilizar sus propios Workflow Components cuando el proyecto proporcione un contexto representativo para hacerlo.

El dogfooding permite evaluar las abstracciones del Framework mediante uso real.

```text
GitHub Framework
      ↓
uses Workflow Components
      ↓
produces evidence
      ↓
detects gaps
      ↓
improves Framework
```

## 22.1 Objectives

El dogfooding DEBERÍA permitir comprobar:

- claridad de la responsabilidad;
- suficiencia de la especificación;
- coherencia de metadata;
- utilidad de la materialización;
- reglas de adopción;
- necesidad de especialización;
- dependencias;
- mantenibilidad;
- coherencia entre arquitectura y uso real.

---

## 22.2 Dogfooding Is Not Literal Copying

Dogfooding NO significa que GitHub Framework deba copiar literalmente todos los artefactos canónicos.

El propio Framework es también un consumer y PUEDE necesitar especialización.

```text
Canonical Component
        ↓
Dogfooding
        ↓
GitHub Framework specialization
```

La validación DEBE comprobar la responsabilidad, no la igualdad textual.

---

## 22.3 Dogfooding Evidence

La evidencia PUEDE proceder de distintos mecanismos.

La primera Reference Implementation de los Core Workflow Components ha validado, entre otros:

```text
Issue Forms
Pull Request Template
CODEOWNERS
Branch conventions
Commit conventions
```

Esto demuestra que el dogfooding PUEDE validar tanto:

```text
Physical materializations
```

como:

```text
Non-physical conventions
```

La ausencia de un artefacto físico NO impide obtener evidencia válida.

---

## 22.4 Treatment of Gaps

Los gaps detectados durante dogfooding DEBEN analizarse antes de modificar el Framework.

```text
Observed gap
      ↓
Classify
      ↓
 ┌────────┬───────────┬──────────────┬────────────┐
 │        │           │              │            │
Consumer Component Architecture Documentation Validation
 │        │           │              │            │
 ↓        ↓           ↓              ↓            ↓
Fix      Evolve     Review         Sync         Improve
consumer component  model          docs          evidence
```

NO DEBE modificarse automáticamente el Component para conseguir que el consumer resulte conforme.

Tampoco DEBE modificarse automáticamente el consumer para conseguir que la implementación canónica parezca correcta.

La capa responsable DEBE determinarse a partir de evidencia.

---

## 22.5 Validated Patterns

Los patrones confirmados mediante implementación y dogfooding PUEDEN convertirse en estándares normativos.

```text
Implementation
      ↓
Dogfooding
      ↓
Evidence
      ↓
Validated pattern
      ↓
Standard
```

Una posibilidad no observada o puramente hipotética NO DEBERÍA convertirse en una regla normativa.

---

# 23. Validation

La validación determina si la implementación canónica de un Workflow Component representa de forma suficiente, reutilizable y mantenible su responsabilidad.

```text
Specification
      +
Metadata
      +
Materialization
      ↓
Adoption
      ↓
Evidence
      ↓
Validation
```

La validación DEBE considerar el Component como un contrato completo y no únicamente sus artefactos físicos.

## 23.1 Validation Dimensions

La validación DEBERÍA evaluar, cuando resulte aplicable:

```text
Identity
Responsibility
Specification
Metadata
Materialization
Artifacts
Adoption
Specialization
Dependencies
Consumer conformance
Maintainability
Architectural consistency
```

No todas las dimensiones necesitan la misma evidencia.

---

## 23.2 Validation by Materialization Type

La evidencia DEBE adaptarse al tipo de materialización.

### Convention

Puede evaluarse mediante:

```text
repository practice
Git history
documented process
observable naming
observable lifecycle
```

### Community File

Puede evaluarse mediante:

```text
consumer artifact
platform-recognized location
content specialization
actual repository usage
```

### Configuration

Puede evaluarse mediante:

```text
consumer configuration
configured values
platform behavior
repository integration
```

### Executable Materialization

Cuando se implementen Components ejecutables, la validación DEBERÁ incluir evidencia adecuada de ejecución.

Los detalles específicos NO se establecen todavía en esta versión de los Standards.

---

## 23.3 Validation Does Not Require Identity

La validación NO DEBE exigir igualdad literal entre:

```text
Canonical implementation
```

y:

```text
Consumer implementation
```

Debe comprobar:

```text
Responsibility
        ↓
Preserved
```

junto con las restricciones aplicables.

La diferencia física o textual PUEDE ser consecuencia legítima de la especialización.

---

## 23.4 Validation Result vs Lifecycle

El resultado de validación y el lifecycle son dimensiones independientes.

```text
Validation
    ≠
Lifecycle
```

Por tanto:

```text
Lifecycle: Experimental
Validation: Reference Implementation Validated
```

es un estado válido y demostrado por los Core Workflow Components.

La validación satisfactoria proporciona evidencia para futuras decisiones de lifecycle, pero NO determina automáticamente dichas decisiones.

---

## 23.5 Validation Result vs Implementation Classification

La validación tampoco redefine automáticamente la clasificación de implementación.

```text
Implemented
      +
Validated
```

indica que una implementación canónica existente ha sido evaluada satisfactoriamente.

No representa una nueva clasificación.

Un Component `Conceptual` NO DEBE marcarse como `Validated` mediante la validación de una implementación consumer aislada si todavía no existe una implementación canónica gobernada por el Framework.

---

## 23.6 Validation Findings

Toda validación que detecte gaps relevantes DEBERÍA determinar si corresponden a:

```text
Consumer
Component
Architecture
Documentation
Validation process
Expected specialization
```

Los cambios resultantes DEBEN aplicarse únicamente cuando exista evidencia suficiente.

Una Reference Implementation que no requiera cambios arquitectónicos constituye también un resultado válido.

```text
Validation
    ↓
No architecture gap detected
    ↓
Architecture preserved
```

La ausencia de cambios NO significa que la validación carezca de valor.

Demuestra que las assumptions evaluadas han sobrevivido al uso real.

---

# 24. Quality Gates

Todo Workflow Component DEBERÍA evaluarse mediante Quality Gates antes de considerarse suficientemente validado para adopción estable o evolución de lifecycle.

Los Quality Gates proporcionan controles verificables sobre:

- identidad;
- responsabilidad;
- estructura;
- metadata;
- materialización;
- adopción;
- especialización;
- dependencias;
- validación;
- mantenimiento.

```text
Workflow Component
        ↓
Quality Gates
        ↓
Validation Evidence
        ↓
Lifecycle Decision
```

Los Quality Gates NO sustituyen la evaluación arquitectónica.

Su función es detectar inconsistencias y proporcionar evidencia para tomar decisiones.

---

## 24.1 Identity Gate

El Component DEBE:

- disponer de un ID canónico único;
- utilizar el prefijo `WCL-`;
- mantener un nombre coherente con su responsabilidad;
- declarar `family: Workflow`;
- declarar versión;
- declarar lifecycle;
- declarar priority;
- declarar audience;
- declarar maturity.

Resultado esperado:

```text
Identity → Valid
```

---

## 24.2 Responsibility Gate

La responsabilidad DEBE:

- ser claramente identificable;
- ser suficientemente reutilizable;
- disponer de límites comprensibles;
- evitar duplicar otra responsabilidad reconocida;
- poder evaluarse independientemente de una materialización concreta.

El Component NO DEBE existir únicamente porque exista:

- un archivo;
- una configuración;
- una GitHub Action;
- un proceso particular de un único consumer.

Resultado esperado:

```text
Responsibility → Valid
```

---

## 24.3 Structure Gate

Todo Workflow Component implementado DEBE contener:

```text
README.md
metadata.yml
```

Los artefactos adicionales DEBEN existir únicamente cuando su materialización lo requiera.

La estructura NO DEBE contener:

- directorios vacíos por convención;
- templates vacíos;
- archivos placeholder sin utilidad;
- artefactos creados únicamente para mantener simetría.

Resultado esperado:

```text
Structure → Valid
```

---

## 24.4 Metadata Gate

`metadata.yml` DEBE:

- ser sintácticamente válido;
- contener los campos necesarios;
- utilizar el ID canónico correcto;
- declarar `family: Workflow`;
- declarar materialización;
- declarar `executable`;
- declarar artefactos reales;
- expresar la política de adopción;
- expresar la política de especialización;
- representar el estado de validación;
- permanecer semánticamente sincronizado con el README.

Resultado esperado:

```text
Metadata → Valid
```

---

## 24.5 Materialization Gate

La materialización DEBE:

- derivarse de la responsabilidad;
- utilizar únicamente mecanismos necesarios;
- ser suficientemente clara para permitir adopción;
- evitar artefactos especulativos;
- evitar automatización innecesaria;
- distinguir correctamente entre comportamiento ejecutable y no ejecutable.

Un Component basado únicamente en Convention PUEDE superar este Gate.

```text
Convention
     +
Specification
     +
Metadata
     ↓
Valid materialization
```

Resultado esperado:

```text
Materialization → Valid
```

---

## 24.6 Artifact Gate

Cuando existan artefactos reutilizables, estos DEBEN:

- corresponder a la responsabilidad;
- permanecer alineados con la especificación;
- evitar información propia de un único consumer;
- permitir la especialización declarada;
- utilizar nombres y formatos compatibles con la plataforma correspondiente.

Los artefactos declarados en metadata DEBEN existir realmente.

Resultado esperado:

```text
Artifacts → Valid
```

---

## 24.7 Adoption Gate

Las reglas de adopción DEBEN permitir comprender cómo puede un consumer satisfacer la responsabilidad.

DEBE poder determinarse si la adopción ocurre mediante:

- artefacto físico;
- configuración;
- Convention;
- especialización;
- implementación equivalente;
- combinación de mecanismos.

Cuando exista un destino físico específico, este DEBERÍA declararse mediante:

```yaml
adoption:
  target:
```

La ausencia de `target` es válida cuando la adopción no requiere una ubicación física única.

Resultado esperado:

```text
Adoption → Valid
```

---

## 24.8 Specialization Gate

La política de especialización DEBE ser coherente con la naturaleza del Component.

Cuando:

```yaml
specialization: Allowed
```

el consumer PUEDE adaptar la materialización conservando la responsabilidad.

Cuando:

```yaml
specialization: Required
```

la implementación canónica DEBE dejar explícito qué información o adaptación necesita aportar el consumer.

La especialización NO DEBE utilizarse para justificar una redefinición de la responsabilidad.

Resultado esperado:

```text
Specialization → Valid
```

---

## 24.9 Dependency Gate

Las dependencias DEBEN:

- representar necesidades contractuales reales;
- utilizar IDs canónicos cuando correspondan a Framework Components;
- mantenerse al mínimo necesario;
- evitar modelar simples relaciones temáticas como dependencias;
- evitar convertir la secuencia habitual del workflow en una cadena artificial.

```text
Related
   ≠
Dependent
```

La ausencia de resolución automática de dependencias NO invalida el Component.

Resultado esperado:

```text
Dependencies → Valid
```

---

## 24.10 Executability Gate

La metadata DEBE indicar correctamente:

```yaml
materialization:
  executable:
```

Cuando el Component sea no ejecutable:

```yaml
executable: false
```

NO DEBE interpretarse como falta de implementación.

Cuando se implementen Components ejecutables, su comportamiento DEBERÁ poder validarse mediante evidencia adecuada.

Resultado esperado:

```text
Executability → Valid
```

---

## 24.11 Consumer Conformance Gate

El Component DEBERÍA disponer de evidencia de que un consumer representativo puede satisfacer su responsabilidad.

La evaluación NO DEBE depender únicamente de:

- igualdad textual;
- igualdad estructural;
- copia literal de artefactos.

Debe comprobar:

```text
Responsibility satisfied
```

mediante evidencia observable.

Para Components basados en Convention, dicha evidencia PUEDE proceder de prácticas reales del repositorio.

Resultado esperado:

```text
Consumer Conformance → Valid
```

---

## 24.12 Reference Implementation Gate

Cuando un Workflow Component declare:

```yaml
validation:
  reference_implementation: Validated
```

DEBE existir una Reference Implementation real o representativa que haya producido evidencia suficiente para evaluar el contrato del Component.

La Reference Implementation PUEDE realizarse mediante dogfooding cuando GitHub Framework constituya un consumer adecuado.

La validación DEBERÍA permitir comprobar:

- responsabilidad;
- materialización;
- adopción;
- especialización;
- dependencias aplicables;
- conformidad del consumer;
- mantenibilidad;
- consistencia arquitectónica.

Los findings detectados DEBERÍAN clasificarse antes de producir cambios.

La ausencia de gaps arquitectónicos NO invalida la utilidad de la Reference Implementation.

Resultado esperado:

```text
Reference Implementation → Validated
```

---

## 24.13 Consistency Gate

DEBE comprobarse coherencia entre:

```text
README.md
metadata.yml
Component Catalog
Repository Design System
Workflow Component Standards
consumer evidence
```

Las inconsistencias relevantes DEBEN resolverse o documentarse antes de promover lifecycle.

Resultado esperado:

```text
Consistency → Valid
```

---

## 24.14 Maintenance Gate

El Component DEBE disponer de una base mantenible.

DEBERÍA comprobarse:

- ausencia de duplicaciones innecesarias;
- ausencia de artefactos especulativos;
- claridad de las fuentes canónicas;
- versionado coherente;
- lifecycle explícito;
- metadata actualizada;
- validación trazable;
- posibilidad razonable de evolución.

Resultado esperado:

```text
Maintenance → Valid
```

---

## 24.15 Stable Promotion Gate

La promoción:

```text
Experimental
     ↓
Stable
```

DEBE producirse únicamente cuando exista evidencia suficiente de reutilización y estabilidad contractual.

Antes de promover un Component a `Stable`, DEBERÍA comprobarse que:

- los Quality Gates aplicables han sido evaluados;
- existe validación representativa;
- no existen gaps críticos sin resolver o aceptar explícitamente;
- la responsabilidad permanece estable;
- la materialización es mantenible;
- las reglas de adopción son suficientemente claras;
- no existen contradicciones conocidas con la arquitectura.

La promoción NO DEBE utilizarse únicamente para cerrar:

- un Sprint;
- una milestone;
- una release.

---

# 25. Validation Checklist

La siguiente checklist proporciona una referencia operativa para revisar un Workflow Component.

No sustituye los Quality Gates ni la evaluación arquitectónica.

## 25.1 Identity

- [ ] ID canónico definido.
- [ ] Prefijo `WCL-` utilizado.
- [ ] Nombre coherente con la responsabilidad.
- [ ] `family: Workflow` declarada.
- [ ] `version` declarada.
- [ ] `status` declarado.
- [ ] `priority` declarada.
- [ ] `audience` declarada.
- [ ] `maturity` declarada.

---

## 25.2 Responsibility

- [ ] La responsabilidad está claramente definida.
- [ ] Los límites son comprensibles.
- [ ] El propósito es reutilizable.
- [ ] No duplica otro Component existente.
- [ ] Puede explicarse independientemente de un artefacto concreto.
- [ ] Se distingue correctamente de responsabilidades relacionadas.

---

## 25.3 Structure

- [ ] `README.md` presente.
- [ ] `metadata.yml` presente.
- [ ] No existen directorios vacíos por simetría.
- [ ] No existen templates vacíos.
- [ ] Los artefactos adicionales responden a una necesidad real.
- [ ] Los nombres respetan las convenciones del Framework.

---

## 25.4 Metadata

- [ ] Metadata sintácticamente válida.
- [ ] ID correcto.
- [ ] `family: Workflow`.
- [ ] `dependencies` declaradas.
- [ ] `materialization.primary` declarada.
- [ ] `materialization.executable` declarado.
- [ ] `artifacts.specification` declarado.
- [ ] `adoption.specialization` declarada.
- [ ] Validation metadata presente.
- [ ] README y metadata están sincronizados.

---

## 25.5 Materialization

- [ ] La materialización deriva de la responsabilidad.
- [ ] Los mecanismos declarados existen realmente.
- [ ] No existe materialización especulativa.
- [ ] No se fuerza un template cuando no resulta necesario.
- [ ] No se fuerza ejecución cuando no resulta necesaria.
- [ ] Las Conventions están suficientemente especificadas.
- [ ] La materialización física es reutilizable cuando existe.

---

## 25.6 Artifacts

- [ ] Los artefactos declarados existen.
- [ ] Los artefactos están alineados con la especificación.
- [ ] No contienen información específica innecesaria de un consumer.
- [ ] Los placeholders son claros cuando existen.
- [ ] Los nombres y ubicaciones son compatibles con la plataforma.
- [ ] No existen artefactos sin responsabilidad real.

---

## 25.7 Adoption

- [ ] La estrategia de adopción es comprensible.
- [ ] `target` está declarado cuando corresponde.
- [ ] La adopción mediante Convention puede demostrarse.
- [ ] Se permite implementación equivalente cuando corresponde.
- [ ] La implementación canónica no contiene información propia del consumer.
- [ ] La responsabilidad puede evaluarse en un consumer.

---

## 25.8 Specialization

- [ ] La política `Allowed` o `Required` es correcta.
- [ ] La especialización conserva la responsabilidad.
- [ ] Las adaptaciones esperadas están documentadas.
- [ ] Los valores específicos del consumer permanecen fuera de la definición canónica.
- [ ] No existe divergencia contractual disfrazada de especialización.

---

## 25.9 Dependencies

- [ ] Las dependencias declaradas son realmente necesarias.
- [ ] Utilizan IDs reconocidos.
- [ ] No representan únicamente secuencia de workflow.
- [ ] No existen dependencias artificiales.
- [ ] Las dependencias pueden satisfacerse conceptualmente.
- [ ] No se asume resolución automática inexistente.

---

## 25.10 Validation

- [ ] Existe evidencia representativa.
- [ ] La evidencia corresponde al tipo de materialización.
- [ ] Se ha evaluado la responsabilidad y no únicamente el artefacto.
- [ ] Las diferencias consumer/canonical han sido evaluadas correctamente.
- [ ] Los gaps observados han sido clasificados.
- [ ] Los findings críticos han sido resueltos o aceptados explícitamente.
- [ ] El resultado de validación está sincronizado con metadata.

---

## 25.11 Lifecycle

- [ ] El lifecycle declarado refleja el estado real.
- [ ] Validation y lifecycle no se confunden.
- [ ] Implementation classification y lifecycle no se confunden.
- [ ] No existe promoción automática por cierre de Sprint o release.
- [ ] Las transiciones relevantes disponen de evidencia.

---

## 25.12 Maintenance

- [ ] Versionado coherente.
- [ ] README y metadata sincronizados.
- [ ] Component Catalog revisado.
- [ ] Repository Design System revisado cuando corresponde.
- [ ] No existe drift conocido relevante.
- [ ] Las fuentes canónicas son identificables.
- [ ] No existe duplicación innecesaria.

---

# 26. Anti-patterns

Los siguientes patrones DEBEN evitarse al diseñar, implementar o mantener Workflow Components.

## 26.1 Workflow Component = GitHub Action

NO DEBE asumirse:

```text
Workflow Component
        =
GitHub Action
```

Una responsabilidad Workflow puede ser:

- convencional;
- documental;
- configurable;
- materializada mediante Community Files;
- ejecutable.

Reducir la biblioteca únicamente a automatización contradice el modelo validado.

---

## 26.2 File-Driven Component Design

NO DEBE crearse un Workflow Component únicamente porque exista un archivo reconocible.

Ejemplo incorrecto:

```text
File exists
    ↓
Create Component
```

El proceso correcto es:

```text
Reusable responsibility
        ↓
Component
        ↓
Appropriate materialization
```

---

## 26.3 Executable by Default

NO DEBE asumirse que un Workflow Component necesita:

- script;
- job;
- workflow;
- Action;
- trigger.

```text
Workflow responsibility
        ≠
Automatic execution
```

La automatización DEBE incorporarse únicamente cuando la responsabilidad la requiera.

---

## 26.4 Template by Symmetry

NO DEBE crearse:

```text
templates/
```

en todos los Components únicamente para mantener una estructura uniforme.

Ejemplo no deseado:

```text
branch/
├── README.md
├── metadata.yml
└── templates/
```

si no existe ningún artefacto reutilizable que justifique dicho directorio.

---

## 26.5 Implementation by Empty Artifact

La existencia de un archivo vacío o placeholder NO constituye una implementación válida.

Ejemplo:

```text
CODEOWNERS
    ↓
TODO
```

no demuestra que `WCL-CODE-REVIEW` esté correctamente materializado.

---

## 26.6 Copying Consumer Content into Canonical Artifacts

La implementación canónica NO DEBE contener información específica del consumer utilizada durante dogfooding.

Ejemplos no recomendados:

```text
@fran-eliot
project-specific labels
repository-specific issue IDs
consumer-only instructions
```

cuando dichos valores no sean reutilizables.

El consumer debe aportar su especialización.

---

## 26.7 Literal Conformance

NO DEBE declararse no conformidad únicamente porque:

```text
Consumer artifact
        ≠
Canonical artifact
```

Debe evaluarse la responsabilidad.

```text
Physical difference
        ≠
Responsibility difference
```

---

## 26.8 Validation by File Presence

La existencia de un archivo esperado NO demuestra por sí sola satisfacción de la responsabilidad.

```text
Expected filename exists
        ≠
Component responsibility satisfied
```

Debe evaluarse:

- contenido;
- configuración;
- comportamiento;
- uso real;
- evidencia contextual.

---

## 26.9 Sequence as Dependency

NO DEBE convertirse automáticamente:

```text
Issue
  ↓
Branch
  ↓
Commit
  ↓
Pull Request
  ↓
Code Review
```

en una cadena de dependencias.

```text
Workflow sequence
       ≠
Dependency graph
```

Solo deben declararse dependencias contractuales reales.

---

## 26.10 Stable by Validation Alone

Un Component NO DEBE promocionarse automáticamente a `Stable` únicamente porque:

```text
reference_implementation: Validated
```

La validación constituye evidencia.

La estabilidad requiere una evaluación más amplia del contrato y su reutilización.

---

## 26.11 Implemented by Consumer Existence

La existencia de una implementación específica en un consumer NO convierte automáticamente un Component `Conceptual` en `Implemented`.

```text
Consumer implementation exists
          ≠
Canonical Framework implementation exists
```

La clasificación `Implemented` requiere una implementación canónica gobernada por GitHub Framework.

---

## 26.12 Premature Automation

NO DEBERÍAN formalizarse sistemas de:

- generación automática;
- dependency resolution;
- schema validation compleja;
- reusable workflow orchestration;
- deployment orchestration;
- component installation;

antes de disponer de necesidades e implementaciones reales que justifiquen dichas capacidades.

---

## 26.13 Platform Overfitting

Un Component NO DEBERÍA definirse de manera innecesariamente dependiente de GitHub cuando la responsabilidad pueda expresarse de forma más estable.

Sin embargo, tampoco DEBERÍA crearse una abstracción multiplataforma hipotética sin consumidores reales.

```text
Avoid overfitting
      +
Avoid speculative abstraction
```

---

## 26.14 Closing Gaps by Relaxing the Contract

Un gap observado durante dogfooding NO DEBE resolverse automáticamente relajando la responsabilidad.

Ejemplo:

```text
Consumer does not satisfy rule
        ↓
Change rule until consumer passes
```

constituye un anti-pattern cuando no existe evidencia que justifique el cambio.

Primero debe determinarse si el problema pertenece al:

```text
Consumer
Component
Architecture
Documentation
Validation
```

---

## 26.15 Metadata Drift

La metadata NO DEBE afirmar:

```text
dogfooding: false
```

cuando la Reference Implementation ya se ha completado.

Tampoco DEBE declarar artefactos, lifecycle, materialización o dependencias que contradigan la especificación canónica.

El drift entre README y metadata constituye un defecto de mantenimiento.

---

# 27. Maintenance

Todo Workflow Component implementado DEBE mantenerse sincronizado con las fuentes que gobiernan su contrato.

Como mínimo, el mantenimiento DEBE considerar:

```text
Repository Design System
Component Catalog
Workflow Component Standards
Component README
Component metadata
Canonical artifacts
Reference Implementations
```

```text
Architecture
      ↓
Catalog
      ↓
Component
      ↓
Consumer adoption
      ↓
Validation evidence
      ↺
```

---

## 27.1 Synchronization

Los maintainers DEBEN revisar un Component cuando cambie materialmente:

- su responsabilidad;
- una dependencia;
- su materialización;
- un artefacto canónico;
- la política de adopción;
- la política de especialización;
- una regla arquitectónica;
- un Standard aplicable;
- su lifecycle;
- su clasificación de implementación.

La modificación de una fuente relacionada NO implica automáticamente modificar el Component.

Primero DEBE evaluarse el impacto real.

---

## 27.2 Avoiding Drift

El README y `metadata.yml` DEBEN permanecer semánticamente alineados.

NO DEBERÁ mantenerse información contradictoria sobre:

- identidad;
- versión;
- status;
- maturity;
- materialización;
- executability;
- dependencies;
- artifacts;
- adoption;
- specialization;
- validation.

Los datos derivados de otras fuentes DEBERÍAN mantenerse al mínimo necesario.

---

## 27.3 Canonical Artifacts

Los artefactos reutilizables DEBEN revisarse cuando:

- cambie su especificación;
- cambie la plataforma;
- deje de ser válida una convención;
- una Reference Implementation revele un problema;
- aparezca una especialización recurrente que justifique evolución.

NO DEBEN modificarse únicamente para que coincidan textualmente con un consumer concreto.

---

## 27.4 Validation State

La metadata de validación DEBE representar el estado real.

Ejemplo:

```yaml
validation:
  dogfooding: true
  reference_implementation: Validated
```

Si una evolución material del Component invalida significativamente la evidencia anterior, DEBERÍA evaluarse si requiere nueva validación.

Una corrección menor NO necesita reiniciar automáticamente todo el proceso de Reference Implementation.

---

## 27.5 Dependency Maintenance

Las dependencias DEBERÍAN revisarse cuando:

- cambie la responsabilidad de un Component relacionado;
- aparezca una nueva dependencia real;
- una dependencia deje de ser necesaria;
- la validación demuestre que una relación anteriormente considerada dependencia era únicamente contextual.

Las dependencias obsoletas DEBEN eliminarse.

---

## 27.6 Lifecycle Review

El lifecycle DEBERÍA revisarse cuando exista nueva evidencia relevante sobre:

- reutilización;
- estabilidad;
- problemas recurrentes;
- deprecación;
- sustitución;
- mantenibilidad.

La antigüedad por sí sola NO justifica una promoción o deprecación.

---

# 28. Evolution Rules

Los Workflow Components DEBEN evolucionar mediante cambios controlados y respaldados por evidencia.

```text
Evidence
   ↓
Finding
   ↓
Evaluation
   ↓
Decision
   ↓
Evolution
```

---

## 28.1 Sources of Evolution

La evolución PUEDE originarse en:

- Reference Implementations;
- dogfooding;
- adopción real;
- nuevos consumers;
- gaps recurrentes;
- cambios de plataforma;
- cambios arquitectónicos;
- mantenimiento;
- nuevas responsabilidades demostradas.

Una posibilidad hipotética NO DEBERÍA ser suficiente por sí sola para modificar el contrato.

---

## 28.2 Classification Before Modification

Antes de modificar un Component debido a un problema observado, DEBERÍA clasificarse el finding.

```text
Consumer gap
Component gap
Architecture gap
Documentation drift
Validation gap
Expected specialization
```

El cambio DEBE aplicarse en la capa responsable.

Ejemplos:

```text
Consumer config incorrect
        ↓
Fix consumer

Canonical rule unclear
        ↓
Fix Component

Incorrect responsibility boundary
        ↓
Review Architecture

README / metadata contradiction
        ↓
Synchronize documentation
```

---

## 28.3 Responsibility Changes

Una modificación sustancial de la responsabilidad DEBE evaluarse cuidadosamente.

Si el cambio altera:

- propósito;
- límites;
- consumidores esperados;
- comportamiento esencial;

DEBERÍA determinarse si:

```text
Same Component evolved
```

o:

```text
New Component required
```

La identidad NO DEBE conservarse artificialmente cuando el concepto haya cambiado de forma fundamental.

---

## 28.4 Materialization Changes

Un Component PUEDE evolucionar su materialización sin cambiar su identidad cuando la responsabilidad permanezca estable.

Ejemplo conceptual:

```text
Convention
     ↓
Convention + Configuration
```

La nueva materialización DEBE:

- aportar valor real;
- permanecer coherente con la responsabilidad;
- evitar invalidar consumers existentes sin necesidad;
- reflejarse en metadata;
- evaluarse mediante versioning apropiado.

---

## 28.5 New Workflow Components

Un nuevo Workflow Component DEBERÍA crearse únicamente cuando la responsabilidad:

- sea reutilizable;
- tenga límites reconocibles;
- no duplique otro Component;
- aparezca en un contexto real;
- justifique una identidad independiente.

```text
Observed need
     ↓
Reusable responsibility?
   ┌────┴────┐
  no         yes
  ↓           ↓
consumer    evaluate
specific    Component
```

La existencia de una nueva funcionalidad de GitHub NO constituye por sí sola motivo suficiente para crear un Component.

---

## 28.6 Conceptual to Implemented

La transición:

```text
Conceptual
    ↓
Implemented
```

DEBE producirse cuando exista una implementación canónica suficiente y gobernada por GitHub Framework.

La transición DEBERÍA incluir:

- especificación;
- metadata;
- materialización;
- reglas de adopción;
- validación inicial cuando corresponda;
- actualización del Component Catalog;
- actualización arquitectónica cuando resulte necesaria.

Una implementación consumer aislada NO es suficiente.

---

## 28.7 Backward Compatibility

Los cambios compatibles DEBERÍAN preservar adopciones existentes siempre que resulte razonable.

Los cambios incompatibles DEBEN:

- estar justificados;
- utilizar versioning adecuado;
- considerar impacto sobre consumers;
- documentar transición cuando sea necesaria.

GitHub Framework NO DEBE asumir que todos los consumers pueden migrar inmediatamente.

---

## 28.8 Deprecation

Cuando un Workflow Component deje de ser recomendable, DEBERÍA preferirse una transición explícita a:

```text
Deprecated
```

frente a su eliminación inmediata.

La deprecación DEBE indicar:

- motivo;
- alternativa;
- impacto;
- transición recomendada.

---

## 28.9 Standards Evolution

Estos Workflow Component Standards también DEBEN evolucionar a partir de evidencia.

Una nueva regla normativa DEBERÍA incorporarse cuando exista:

```text
Observed behavior
        ↓
Relevant or repeated evidence
        ↓
Validated pattern
        ↓
Reusable rule
```

Los Standards NO DEBERÍAN convertirse en un catálogo de escenarios hipotéticos.

---

## 28.10 Architecture Preservation

La validación o evolución de un Workflow Component NO DEBE producir cambios arquitectónicos por defecto.

La arquitectura DEBERÍA modificarse únicamente cuando la evidencia revele:

- una assumption incorrecta;
- un límite conceptual insuficiente;
- una responsabilidad mal definida;
- una relación estructural ausente;
- una contradicción real del modelo.

Cuando la implementación y validación confirmen el modelo existente:

```text
Evidence
    ↓
Architecture remains valid
```

preservar la arquitectura constituye la decisión correcta.

---

# 29. Summary

Los Workflow Component Standards establecen las reglas prácticas para diseñar, implementar, adoptar, validar, mantener y evolucionar Workflow Components dentro de GitHub Framework.

El modelo puede resumirse como:

```text
Workflow Component
        │
        ├── Identity
        ├── Responsibility
        ├── Metadata
        ├── Materialization
        │       ├── Convention
        │       ├── Community File
        │       ├── Configuration
        │       ├── Template
        │       └── Executable mechanism
        │
        ├── Artifacts
        ├── Adoption
        ├── Specialization
        ├── Dependencies
        ├── Version
        ├── Maturity
        ├── Lifecycle
        └── Validation
                ↓
        Reference Implementation
                ↓
            Dogfooding
                ↓
             Evidence
                ↓
             Findings
                ↓
             Evolution
```

Las distinciones fundamentales son:

```text
Workflow Component
        ≠
GitHub Action

Responsibility
        ≠
Artifact

Responsibility
        ≠
Materialization

Materialization
        ≠
Executability

Implemented
        ≠
Executable

Implemented
        ≠
Stable

Implementation classification
        ≠
Lifecycle

Implementation classification
        ≠
Validation

Lifecycle
        ≠
Validation

Maturity
        ≠
Lifecycle

Canonical implementation
        ≠
Consumer implementation

Physical difference
        ≠
Non-conformance

Workflow sequence
        ≠
Dependency graph

Consumer implementation exists
        ≠
Canonical Framework implementation exists
```

Un Workflow Component define una responsabilidad reutilizable dentro del workflow de ingeniería.

La responsabilidad constituye el núcleo conceptual del Component.

La materialización define cómo dicha responsabilidad se expresa.

```text
Responsibility
      ↓
Materialization
      ↓
Adoption
      ↓
Evidence
```

La materialización PUEDE ser:

```text
Physical
Non-physical
Executable
Non-executable
```

y ninguna de estas dimensiones determina por sí sola la validez del Component.

Los Core Workflow Components han demostrado que una implementación canónica PUEDE basarse en mecanismos diferentes:

```text
WCL-ISSUE
→ Community File + Configuration

WCL-PULL-REQUEST
→ Community File

WCL-CODE-REVIEW
→ Convention + Configuration

WCL-BRANCH
→ Convention

WCL-COMMIT
→ Convention
```

Por tanto, GitHub Framework NO DEBE imponer una única forma física de implementación para toda la Workflow Component Library.

La estructura debe seguir a la responsabilidad.

```text
Responsibility
      ↓
Minimum useful materialization
```

y no:

```text
Uniform filesystem
      ↓
Forced implementation
```

La implementación canónica proporciona una base reutilizable.

El consumer puede adoptar dicha base mediante:

- uso directo;
- especialización;
- configuración;
- Convention;
- implementación equivalente;
- combinación de mecanismos.

```text
Canonical Component
        ↓
Consumer adoption
        ↓
Contextual implementation
```

La conformidad se evalúa sobre la responsabilidad satisfecha.

NO se evalúa únicamente mediante:

- igualdad textual;
- igualdad física;
- coincidencia exacta de archivos;
- copia literal de templates.

```text
Responsibility satisfied
        ↓
Possible conformance
```

aunque:

```text
Canonical artifact
        ≠
Consumer artifact
```

La especialización permite adaptar el Component al contexto del consumer.

```text
Canonical responsibility
        ↓
Specialization
        ↓
Consumer-specific implementation
```

La especialización debe preservar el propósito y los límites de la responsabilidad.

Cuando:

```yaml
specialization: Allowed
```

el consumer PUEDE adaptar la implementación.

Cuando:

```yaml
specialization: Required
```

el consumer DEBE aportar información contextual necesaria para completar correctamente la adopción.

Las dependencias deben representar necesidades contractuales reales.

```text
Related
   ≠
Dependent
```

Por tanto, un flujo habitual como:

```text
Issue
  ↓
Branch
  ↓
Commit
  ↓
Pull Request
  ↓
Code Review
```

NO debe convertirse automáticamente en:

```text
Dependency graph
```

La clasificación de implementación indica si existe una implementación canónica reutilizable.

```text
Conceptual
Implemented
```

El lifecycle expresa el grado de estabilidad del contrato.

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

La validación expresa la evidencia obtenida mediante adopción representativa.

Estas dimensiones son independientes.

La primera implementación Core ha demostrado como estado válido:

```text
Implementation: Implemented
Lifecycle: Experimental
Validation: Reference Implementation Validated
Materialization: Non-Executable
```

La validación NO implica automáticamente promoción a `Stable`.

```text
Validated
    ↓
provides evidence for
    ↓
Lifecycle decision
```

Una Reference Implementation proporciona evidencia sobre el comportamiento del contrato en un contexto real.

```text
Component
    ↓
Reference Implementation
    ↓
Evidence
    ↓
Findings
```

El dogfooding permite que GitHub Framework actúe como consumer de sus propios Components cuando resulte representativo.

```text
GitHub Framework
      ↓
uses GitHub Framework
      ↓
produces evidence
      ↓
improves GitHub Framework
```

El objetivo del dogfooding NO es demostrar que la arquitectura existente es correcta.

Su objetivo es permitir descubrir:

- consumer gaps;
- Component gaps;
- architecture gaps;
- documentation drift;
- validation gaps;
- especializaciones esperadas.

Un finding debe clasificarse antes de producir cambios.

```text
Observed gap
      ↓
Classify
      ↓
Change responsible layer
```

La ausencia de cambios arquitectónicos tras una validación también constituye un resultado válido.

```text
Architecture
      ↓
Implementation
      ↓
Reference Implementation
      ↓
No architecture gap
      ↓
Architecture preserved
```

GitHub Framework debe continuar priorizando:

```text
Implementation
      ↓
Evidence
      ↓
Validated pattern
      ↓
Standard
```

frente a:

```text
Hypothetical scenario
      ↓
Premature abstraction
      ↓
Unnecessary complexity
```

La evolución de la Workflow Component Library DEBE producirse mediante evidencia real.

Los Components `Conceptual` NO deben recibir reglas detalladas de implementación antes de disponer de materialización y validación suficientes.

La automatización NO debe considerarse el objetivo por defecto de la biblioteca.

```text
Workflow Component Library
        ↓
Reusable engineering responsibilities
```

de las cuales algunas podrán ser:

```text
Manual
Conventional
Configured
Templated
Automated
Executable
```

según lo requiera realmente su responsabilidad.

La estabilidad requiere evidencia suficiente.

La complejidad debe justificarse.

La reutilización debe preceder a la duplicación.

La responsabilidad debe preceder al artefacto.

```text
Architecture
      ↓
Implementation
      ↓
Reference Implementation / Dogfooding
      ↓
Evidence
      ↓
Validation
      ↓
Validated Patterns
      ↓
Standards
      ↓
Evolution
```

---

# Revision History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-09-13 | Primera versión de Workflow Component Standards basada en Workflow Component Architecture, Core Workflow Components y findings de la Workflow Reference Implementation |
