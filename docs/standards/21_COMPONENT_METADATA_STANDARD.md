# 21 - COMPONENT METADATA STANDARD

## 1. Propósito

El **Component Metadata Standard** define el contrato común de metadata para los Framework Components implementados por GitHub Framework.

Su propósito es proporcionar una representación machine-readable coherente, predecible y reutilizable de las propiedades fundamentales de un Component, independientemente de la familia a la que pertenezca.

El estándar establece:

- un núcleo común de metadata;
- los campos obligatorios y opcionales del contrato;
- la representación canónica de propiedades compartidas;
- los mecanismos permitidos de extensión por familia;
- las reglas generales de evolución del schema;
- las condiciones mínimas que permiten validar metadata mediante tooling determinista.

Este contrato constituye la base estructural para las capacidades de automatización introducidas a partir de `v0.6.0 — Framework Automation`.

El estándar no sustituye las especificaciones particulares de cada familia de Components. Su función es definir el contrato compartido sobre el que dichas familias pueden añadir información específica cuando exista una necesidad demostrada.

---

## 2. Alcance

Este estándar se aplica a los **Framework Components implementados** que dispongan de un archivo `metadata.yml` dentro de la estructura canónica:

```text
framework/components/
```

En el momento de definir esta primera versión del contrato, el Framework dispone de tres familias físicas de Components:

- `README`;
- `Documentation`;
- `Workflow`.

El estándar cubre:

- estructura común de `metadata.yml`;
- identificación del Component;
- versión del contrato de metadata;
- versión del Component;
- familia;
- lifecycle;
- prioridad;
- descripción;
- audiencia;
- maturity;
- dependencias;
- extensiones específicas por familia;
- representación canónica de valores controlados;
- requisitos estructurales necesarios para validación determinista.

El estándar está diseñado a partir de los contratos y patrones ya demostrados por los Components implementados.

No introduce requisitos especulativos para familias conceptuales o futuras.

Cuando una nueva familia de Components sea implementada, deberá adoptar el núcleo común definido por este estándar y podrá introducir extensiones únicamente cuando sus responsabilidades lo requieran.

---

## 3. Principios

El Component Metadata Standard se rige por los siguientes principios.

### 3.1 Common Core First

Todos los Framework Components comparten un conjunto mínimo de propiedades fundamentales.

Estas propiedades deben representarse mediante una estructura común antes de introducir diferencias específicas por familia.

Las diferencias históricas de formato no constituyen por sí mismas una razón para mantener contratos distintos.

---

### 3.2 Normalize Before Automate

La automatización no debe incorporar complejidad destinada únicamente a interpretar inconsistencias estructurales que el propio Framework puede eliminar.

Por tanto:

> El Framework normaliza primero los contratos establecidos y automatiza después operaciones deterministas sobre ellos.

El tooling no debe convertirse en una capa permanente de compatibilidad para formatos históricos cuando estos puedan migrarse sin pérdida semántica.

---

### 3.3 Preserve Semantics

La normalización estructural no debe alterar el significado de los Components existentes.

En particular, una migración de metadata no debe modificar automáticamente:

- lifecycle;
- Component version;
- prioridad;
- maturity;
- audiencia;
- dependencias;
- estado de validación;
- mecanismos de materialización;
- reglas de adopción;
- responsabilidades específicas de familia.

Normalizar representación y modificar semántica son operaciones diferentes.

---

### 3.4 Family Extensions Are Explicit

Las familias pueden necesitar metadata que no pertenece al núcleo común.

Estas extensiones son válidas cuando representan responsabilidades reales y demostradas de una familia.

Una extensión específica de familia:

- no debe duplicar un campo ya definido por el Common Core;
- no debe cambiar el significado de un campo común;
- debe conservar una estructura machine-readable;
- debe poder validarse independientemente cuando sea necesario.

---

### 3.5 No Invented Metadata

La adopción del contrato común no obliga a inventar valores opcionales inexistentes.

Si un Component no dispone actualmente de una propiedad opcional y no existe evidencia que permita establecerla, la migración puede omitirla.

La normalización debe ser **lossless**, pero no debe fabricar información.

---

### 3.6 Human Design, Deterministic Validation

La metadata representa decisiones tomadas por maintainers y autores de Components.

El tooling puede comprobar que esas decisiones están representadas correctamente, pero no debe sustituirlas.

Por ejemplo, un Validator puede comprobar que:

```yaml
status: Experimental
```

utiliza un lifecycle permitido.

No debe decidir automáticamente si ese Component debería promocionarse a `Stable`.

---

### 3.7 Single Machine-Readable Contract

El archivo `metadata.yml` de cada Component constituye su contrato machine-readable primario.

La documentación arquitectónica, el Component Catalog y el Repository Design System pueden describir, registrar o contextualizar Components, pero no deben convertirse en formatos alternativos que el tooling necesite interpretar para comprender la estructura básica de un Component implementado.

---

### 3.8 Progressive Automation

El contrato debe permitir automatización incremental.

La existencia del estándar no implica que todas sus propiedades deban automatizarse inmediatamente.

Las primeras herramientas deben concentrarse en reglas:

- explícitas;
- deterministas;
- reproducibles;
- demostradas por el Framework.

Las decisiones que requieran interpretación arquitectónica permanecen bajo responsabilidad humana.

---

## 4. Modelo de Metadata

Cada Framework Component implementado dispone de un archivo:

```text
metadata.yml
```

Este archivo describe el Component mediante dos niveles conceptuales:

```text
Component Metadata
│
├── Common Core
│   ├── schema_version
│   ├── id
│   ├── name
│   ├── family
│   ├── version
│   ├── status
│   ├── priority
│   ├── description
│   ├── owner
│   ├── audience
│   ├── maturity
│   └── dependencies
│
└── Family Extensions
    ├── README
    ├── Documentation
    └── Workflow
```

El **Common Core** contiene conceptos compartidos entre familias.

Las **Family Extensions** contienen únicamente información cuya semántica pertenece específicamente a una familia.

El modelo evita wrappers estructurales que no aportan semántica adicional.

Por ejemplo, propiedades comunes no deben necesitar estructuras diferentes como:

```yaml
component:
  id: README-HERO
  name: Hero
```

o:

```yaml
classification:
  priority: required
```

cuando pueden representarse mediante el contrato común:

```yaml
id: README-HERO
name: Hero
priority: Required
```

Esta simplificación reduce diferencias accidentales entre familias y permite que el tooling consuma directamente el mismo núcleo de metadata.

---

## 5. Common Component Metadata Schema

La versión inicial del contrato se denomina:

> **Common Component Metadata Schema v1**

Todo `metadata.yml` normalizado debe declarar explícitamente la versión del schema mediante:

```yaml
schema_version: "1.0"
```

`schema_version` identifica la versión del **contrato de metadata**.

No debe confundirse con:

```yaml
version: "1.0.0"
```

que identifica la versión del **Component**.

Ambos mecanismos evolucionan de forma independiente.

---

### 5.1 Core obligatorio

Todo Framework Component implementado debe proporcionar como mínimo:

```yaml
schema_version: "1.0"

id: <component-id>
name: <component-name>
family: <component-family>
version: <component-version>
status: <lifecycle-status>
priority: <component-priority>

description: >
  <component-description>
```

Los campos del Core obligatorio son:

| Campo | Responsabilidad |
|---|---|
| `schema_version` | Identifica la versión del contrato de metadata. |
| `id` | Identificador canónico y único del Component. |
| `name` | Nombre humano del Component. |
| `family` | Familia arquitectónica a la que pertenece. |
| `version` | Versión propia del Component. |
| `status` | Estado de lifecycle del Component. |
| `priority` | Nivel de prioridad dentro del modelo del Framework. |
| `description` | Descripción concisa de la responsabilidad del Component. |

Estos campos forman el contrato mínimo que cualquier tooling general del Framework puede asumir.

---

### 5.2 Core opcional

El contrato común reconoce además las siguientes propiedades compartidas:

```yaml
owner: <owner>

audience:
  - <audience>

maturity: <maturity>

dependencies: []
```

Estas propiedades pertenecen al Common Core porque su significado no depende de una familia concreta.

Sin embargo, no son obligatorias en esta versión del schema.

Un Component puede omitirlas cuando:

- la propiedad no sea aplicable;
- el Framework no haya establecido todavía el valor;
- la información no exista en el contrato actual;
- introducirla requiriese inventar metadata durante una migración.

Cuando estén presentes, deberán respetar las reglas definidas por este estándar.

---

### 5.3 Extensiones específicas por familia

Después del Common Core, cada familia puede declarar propiedades adicionales.

Conceptualmente:

```yaml
schema_version: "1.0"

# Common Core
id: ...
name: ...
family: ...
version: ...
status: ...
priority: ...
description: ...

# Common optional metadata
audience: ...
maturity: ...
dependencies: ...

# Family-specific metadata
...
```

La primera versión del estándar reconoce extensiones demostradas para:

```text
README
└── metadata editorial, composición y representación del README

Documentation
└── sin extensión específica obligatoria demostrada actualmente

Workflow
└── materialization
    artifacts
    adoption
    validation
```

La ausencia de una extensión específica no reduce la validez de una familia.

Una familia debe introducir metadata adicional únicamente cuando exista semántica propia que no pueda representarse correctamente mediante el Common Core.

---

### 5.4 Separación entre Core y extensiones

La clasificación de una propiedad debe basarse en su significado, no en el lugar donde aparecía históricamente.

Por ejemplo:

```text
owner
audience
maturity
dependencies
```

pueden aparecer actualmente en estructuras distintas o solo en determinadas familias, pero conceptualmente pueden describir cualquier Framework Component.

Por tanto, pertenecen al Common Core.

En cambio:

```text
materialization
adoption
```

describen actualmente conceptos específicos del modelo Workflow demostrado y permanecen como extensiones de esa familia.

---

### 5.5 Regla de no duplicación

Una Family Extension no debe redefinir información que ya exista en el Common Core.

No sería válido, por ejemplo:

```yaml
id: README-HERO

component:
  id: README-HERO
```

ni:

```yaml
priority: Required

classification:
  priority: Required
```

El contrato debe disponer de una única representación canónica para cada concepto común.

---

### 5.6 Orden recomendado

YAML no requiere semánticamente un orden específico de claves.

Sin embargo, para mejorar legibilidad y consistencia, se recomienda organizar `metadata.yml` de la siguiente forma:

```text
1. Schema
2. Identity
3. Classification
4. Description
5. Common optional metadata
6. Family-specific extensions
```

Ejemplo:

```yaml
schema_version: "1.0"

id: WCL-ISSUE
name: Issue
family: Workflow
version: "0.1.0"
status: Experimental
priority: Required

description: >
  Defines the reusable responsibility for issue-based
  work intake and structured issue creation.

audience:
  - Maintainer
  - Contributor

maturity: L2

dependencies: []

materialization:
  primary:
    - Community File
    - Configuration
  executable: false

artifacts:
  specification: README.md

adoption:
  target: .github/ISSUE_TEMPLATE/
  specialization: Allowed

validation:
  dogfooding: true
  reference_implementation: Validated
```

El orden recomendado es una convención de mantenimiento y no debe utilizarse como requisito semántico de validación.

---

## 6. Schema Version

`schema_version` identifica la versión del contrato de metadata utilizado por un Framework Component.

Es un campo obligatorio del Common Core.

La versión inicial del contrato es:

```yaml
schema_version: "1.0"
```

### 6.1 Reglas

* Debe existir en todos los `metadata.yml` normalizados.
* Debe representarse como string YAML.
* Debe identificar una versión reconocida del Component Metadata Standard.
* No representa la versión funcional del Component.
* No debe modificarse como consecuencia de cambios ordinarios en el contenido del Component.

Un Component puede evolucionar su versión propia sin cambiar `schema_version`.

### 6.2 Compatibilidad

La introducción de una nueva versión del schema requiere definir sus cambios y condiciones de compatibilidad.

Un Validator debe interpretar `schema_version` antes de aplicar reglas dependientes de una versión concreta del contrato.

La compatibilidad con versiones futuras no debe suponerse automáticamente.

Durante la normalización inicial de los Components implementados se adoptará `schema_version: "1.0"`.

---

## 7. Component Identity

El campo `id` identifica de forma canónica a un Framework Component.

```yaml
id: README-HERO
```

### 7.1 Reglas generales

El identificador debe:

* existir;
* ser un string no vacío;
* ser único entre los Framework Components implementados;
* respetar la convención de identificación de su familia;
* permanecer estable mientras se preserve la identidad del Component.

El nombre humano del Component no sustituye su identificador.

### 7.2 Prefijos de familia

Las familias implementadas utilizan actualmente los siguientes prefijos:

| Familia       | Prefijo   | Ejemplo            |
| ------------- | --------- | ------------------ |
| README        | `README-` | `README-HERO`      |
| Documentation | `DOC-`    | `DOC-ARCHITECTURE` |
| Workflow      | `WCL-`    | `WCL-ISSUE`        |

El prefijo del identificador debe ser coherente con el valor declarado en `family`.

No se introducen prefijos nuevos para familias todavía no implementadas.

### 7.3 Unicidad

Dos Components implementados no deben declarar el mismo `id`.

La unicidad se comprueba sobre el conjunto de Components descubiertos en `framework/components/`.

Un identificador registrado únicamente como conceptual en la documentación no constituye, por sí mismo, una implementación física.

### 7.4 Nombre humano

`name` es obligatorio y debe contener un string no vacío.

```yaml
name: Issue
```

No necesita coincidir literalmente con el sufijo del identificador.

El `id` representa identidad canónica; `name` representa una denominación legible.

---

## 8. Component Version

El campo `version` identifica la versión propia del Component.

```yaml
version: "0.1.0"
```

### 8.1 Reglas

* Es obligatorio.
* Debe representarse como string YAML.
* Debe utilizar el formato de versión establecido para los Components del Framework.
* Evoluciona independientemente de `schema_version`.
* No debe incrementarse automáticamente durante una normalización puramente estructural.

La representación canónica inicial utiliza tres segmentos numéricos:

```text
MAJOR.MINOR.PATCH
```

Ejemplos:

```yaml
version: "0.1.0"
```

```yaml
version: "1.0.0"
```

### 8.2 Normalización

Los Components existentes conservan su versión durante la migración al schema común.

Por ejemplo:

```yaml
version: 0.1.0
```

puede normalizarse a:

```yaml
version: "0.1.0"
```

sin que ello constituya una nueva versión funcional del Component.

La normalización no implica promover lifecycle ni modificar maturity.

---

## 9. Family

El campo `family` identifica la familia arquitectónica a la que pertenece el Component.

Es obligatorio.

### 9.1 Valores reconocidos

La versión inicial del contrato reconoce las familias físicamente implementadas:

```yaml
family: README
```

```yaml
family: Documentation
```

```yaml
family: Workflow
```

Los valores son sensibles a mayúsculas y minúsculas.

### 9.2 Coherencia

La familia declarada debe ser coherente con:

* el prefijo del identificador;
* la ubicación física del Component;
* las extensiones específicas utilizadas.

Un Component no debe declararse como perteneciente a una familia diferente para reutilizar artificialmente sus reglas de metadata.

### 9.3 Nuevas familias

La incorporación de una nueva familia implementada requiere establecer su identidad y las reglas específicas necesarias.

El Common Core debe reutilizarse sin duplicación.

La existencia de una familia conceptual en el Component Catalog no implica que deba incorporarse inmediatamente al conjunto de familias físicas admitidas por el Validator.

---

## 10. Lifecycle Status

`status` representa el estado de lifecycle del Component.

Es obligatorio.

### 10.1 Valores canónicos

Los valores de lifecycle reconocidos por el Framework son:

| Estado         | Significado                                     |
| -------------- | ----------------------------------------------- |
| `Draft`        | En diseño o implementación inicial.             |
| `Experimental` | Implementado y en validación.                   |
| `Stable`       | Validado para uso recomendado.                  |
| `Deprecated`   | Disponible por compatibilidad, pero sustituido. |
| `Retired`      | Fuera del catálogo activo.                      |

Estos valores deben utilizarse con su representación canónica y son sensibles a mayúsculas y minúsculas.

`Archived` no pertenece al vocabulario de lifecycle establecido por el Repository Design System.

El Validator puede comprobar la pertenencia al conjunto de valores permitidos, pero no determinar si el estado declarado es arquitectónicamente adecuado.

### 10.2 Separación de conceptos

Lifecycle no debe confundirse con:

* clasificación de implementación;
* maturity;
* versión del Component;
* estado de Reference Implementation;
* estado de adopción.

Un Component puede estar implementado y validado mediante dogfooding mientras permanece en lifecycle `Experimental`.

### 10.3 Normalización

La migración debe conservar el significado del lifecycle existente.

Por ejemplo:

```yaml
status: stable
```

se normaliza a:

```yaml
status: Stable
```

En cambio, un Component declarado como `Experimental` no debe convertirse en `Stable` por el mero hecho de adoptar el schema común.

---

## 11. Priority

`priority` representa la prioridad del Component dentro del modelo del Framework.

Es obligatorio.

### 11.1 Valores canónicos

```yaml
priority: Required
```

```yaml
priority: Recommended
```

```yaml
priority: Optional
```

Los valores son sensibles a mayúsculas y minúsculas.

### 11.2 Semántica

La prioridad expresa el nivel de necesidad o recomendación establecido para el Component.

No representa:

* prioridad de una Issue;
* orden de implementación;
* estado de lifecycle;
* maturity;
* calidad del Component.

### 11.3 Normalización

Las representaciones históricas en minúsculas deben adoptar la forma canónica.

```yaml
priority: required
```

se convierte en:

```yaml
priority: Required
```

La migración no debe modificar el nivel de prioridad.

---

## 12. Audience

`audience` identifica los perfiles a los que se dirige el Component.

Es un campo opcional del Common Core.

### 12.1 Representación

Cuando esté presente, debe utilizar una lista YAML de strings no vacíos.

```yaml
audience:
  - Maintainer
  - Contributor
```

La representación mediante un único string escalar no forma parte del contrato canónico.

### 12.2 Reglas

* Cada entrada debe identificar una audiencia reconocible.
* No deben existir entradas vacías.
* No deben duplicarse valores dentro de la lista.
* La audiencia no debe inferirse automáticamente a partir de `family` o `priority`.

### 12.3 Normalización

Los valores existentes deben conservarse.

No es obligatorio añadir `audience` a Components que actualmente no dispongan de esta propiedad.

El establecimiento de un vocabulario cerrado de audiencias requiere evidencia suficiente y no forma parte del núcleo inicial de reglas deterministas.

---

## 13. Maturity

`maturity` representa la madurez establecida para el Component dentro del modelo del Framework.

Es un campo opcional del Common Core.

La versión inicial del contrato reconoce dos representaciones existentes: un nivel simple y una estructura de niveles.

### 13.1 Nivel simple

Un Component puede declarar un único nivel de maturity:

```yaml
maturity: L2
```

Esta representación se utiliza actualmente en Documentation y Workflow Components.

Cuando se utilice, el valor debe ser un string no vacío correspondiente a un nivel reconocido por el Framework.

### 13.2 Estructura de niveles

Cuando el contrato del Component necesite expresar distintos niveles de aplicación, puede utilizarse una estructura:

```yaml
maturity:
  minimum: L1
  recommended: L2
  supported:
    - L1
    - L2
    - L3
    - L4
```

Esta representación está demostrada por `README-HERO`.

Los campos tienen responsabilidades diferentes:

| Campo         | Responsabilidad                           |
| ------------- | ----------------------------------------- |
| `minimum`     | Nivel mínimo declarado para el Component. |
| `recommended` | Nivel recomendado de aplicación.          |
| `supported`   | Conjunto de niveles admitidos.            |

La estructura debe conservarse durante la normalización.

No debe reducirse a un único nivel, ya que ello eliminaría información.

### 13.3 Reglas comunes

Cuando `maturity` esté presente:

* debe utilizar una de las dos representaciones reconocidas;
* los niveles declarados deben pertenecer al vocabulario de maturity establecido por el Framework;
* no deben existir niveles vacíos;
* los niveles de `supported` no deben duplicarse;
* `minimum` y `recommended` deben pertenecer a `supported` cuando se declare esta lista;
* no debe inferirse automáticamente a partir de `version`, `status` o Reference Implementation.

La validación de relaciones entre niveles debe limitarse a reglas explícitas y deterministas.

### 13.4 Separación de lifecycle

Maturity y lifecycle representan dimensiones diferentes.

Por ejemplo:

```yaml
status: Experimental
maturity: L2
```

puede ser una combinación válida.

La normalización no debe modificar maturity como consecuencia de un cambio estructural o de la existencia de evidencia de implementación.

### 13.5 Normalización

Si un Component declara maturity, su información debe conservarse íntegramente.

Si no la declara, no debe inventarse un nivel durante la migración.

La normalización de un Component que utiliza una estructura de niveles no debe convertirla en un valor escalar.

---

## 14. Dependencies

`dependencies` declara relaciones de dependencia del Component.

Es un campo opcional del Common Core.

La versión inicial reconoce dos estructuras de declaración:

* lista simple;
* dependencias clasificadas.

Las entradas de dependencia pueden representarse mediante un identificador o mediante un objeto estructurado, según la información que deba conservarse.

### 14.1 Sin dependencias

Un Component puede declarar explícitamente que no tiene dependencias:

```yaml
dependencies: []
```

La ausencia del campo también es válida cuando el contrato actual no dispone de información de dependencias.

No debe interpretarse automáticamente la ausencia del campo como una declaración explícita de inexistencia de dependencias.

### 14.2 Lista simple

Cuando no sea necesario distinguir categorías, puede utilizarse una lista:

```yaml
dependencies:
  - README-HERO
  - README-OVERVIEW
```

Cada entrada debe identificar un Component.

Esta representación no introduce información adicional sobre la versión mínima ni sobre la categoría de dependencia.

### 14.3 Dependencias clasificadas

Cuando el contrato requiera distinguir niveles de dependencia, puede utilizarse una estructura:

```yaml
dependencies:
  required:
    - id: VCL-HERO
      minimum_version: "1.0.0"

  recommended:
    - id: VCL-BANNER
      minimum_version: "1.0.0"

  optional: []
```

Las categorías reconocidas son:

* `required`;
* `recommended`;
* `optional`.

Estas categorías representan relaciones de dependencia y no sustituyen el campo común `priority`.

### 14.4 Entradas estructuradas

Una dependencia puede declararse mediante un objeto:

```yaml
id: VCL-HERO
minimum_version: "1.0.0"
```

`id` identifica el Component referenciado.

`minimum_version` expresa la versión mínima declarada para esa relación.

Cuando esté presente, `minimum_version` debe representarse como string YAML y respetar el formato de versión establecido para los Components.

La normalización no debe eliminar esta información ni convertir una entrada estructurada en un identificador simple si ello implica pérdida semántica.

### 14.5 Preservación semántica

La normalización no debe:

* convertir una estructura clasificada en una lista simple cuando se pierda información;
* inventar categorías para dependencias que no las distinguen;
* eliminar versiones mínimas;
* cambiar una dependencia recomendada por una obligatoria;
* transformar relaciones de composición en dependencias;
* declarar una dependencia como satisfecha únicamente porque su ID figure en el Component Catalog.

La estructura existente debe conservarse cuando sea compatible con el contrato.

### 14.6 Reglas deterministas

Cuando `dependencies` esté presente:

* debe utilizar una estructura reconocida;
* las categorías clasificadas deben pertenecer al conjunto permitido;
* cada entrada debe contener un identificador de Component no vacío;
* los objetos estructurados deben declarar `id`;
* `minimum_version`, cuando exista, debe utilizar el formato de versión establecido;
* no deben existir dependencias duplicadas dentro de una misma declaración.

La comprobación de duplicados debe basarse en el identificador referenciado, independientemente de que se represente mediante un string o un objeto.

Un mismo identificador no debe aparecer más de una vez en la declaración de dependencias de un Component, tampoco cuando las entradas pertenezcan a categorías diferentes.

Por ejemplo, un Component no debe declarar simultáneamente `VCL-HERO` como dependencia `required` y `recommended`.

La normalización no debe resolver automáticamente esta contradicción: deberá registrarse para su revisión por los maintainers.

### 14.7 Referencias conceptuales

La comprobación de existencia debe distinguir entre:

* Components implementados;
* Components conceptuales reconocidos;
* identificadores inválidos o desconocidos.

Una dependencia arquitectónica válida no debe rechazarse automáticamente por el mero hecho de que el Component referenciado todavía no disponga de implementación física.

La existencia de una referencia conceptual tampoco implica que su implementación esté disponible.

### 14.8 Límites

El Validator puede comprobar representación, identidad, versiones y coherencia determinista.

No debe decidir si una dependencia es arquitectónicamente necesaria.

La evaluación de su necesidad funcional permanece bajo responsabilidad humana.

---

## 15. Family Extensions

Las Family Extensions permiten representar propiedades cuya semántica pertenece a una familia concreta de Framework Components.

El Common Component Metadata Schema establece un núcleo compartido, pero no exige que todas las familias utilicen las mismas propiedades adicionales.

Una extensión es válida cuando:

* responde a una responsabilidad demostrada de la familia;
* no duplica propiedades del Common Core;
* conserva la semántica de los Components existentes;
* utiliza una estructura machine-readable;
* permite aplicar reglas de validación deterministas cuando corresponda.

La existencia de una propiedad en una sola familia no implica automáticamente que deba incorporarse al Common Core.

Del mismo modo, una propiedad conceptualmente compartida no debe permanecer dentro de una extensión únicamente por razones históricas.

### 15.1 README Components

Los README Components disponen de metadata específica para describir contenido, composición, compatibilidad y representación de secciones reutilizables de README.

La normalización debe eliminar los wrappers históricos `component` y `classification` sin eliminar las propiedades que contienen.

#### 15.1.1 Propiedades específicas

La primera versión del contrato reconoce las siguientes propiedades README:

| Propiedad              | Responsabilidad                                              |
| ---------------------- | ------------------------------------------------------------ |
| `category`             | Categoría funcional o editorial del Component.               |
| `repository_types`     | Tipos de repositorio a los que se dirige.                    |
| `responsibilities`     | Responsabilidades específicas del Component.                 |
| `non_responsibilities` | Responsabilidades explícitamente excluidas.                  |
| `inputs`               | Información requerida o admitida para componer el contenido. |
| `outputs`              | Representación o contenido producido.                        |
| `compatibility`        | Condiciones de compatibilidad.                               |
| `composition`          | Reglas o relaciones de composición.                          |
| `constraints`          | Restricciones específicas.                                   |
| `quality_gates`        | Condiciones de calidad declaradas.                           |
| `files`                | Archivos asociados al Component.                             |
| `catalog`              | Información de catalogación específica.                      |
| `implementation`       | Información sobre su implementación.                         |
| `maintenance`          | Información de mantenimiento.                                |

Estas propiedades son extensiones reconocidas, no campos universalmente obligatorios.

Su presencia depende del contrato y las responsabilidades de cada README Component.

#### 15.1.2 Normalización de propiedades comunes

Las propiedades compartidas deben trasladarse a su ubicación canónica.

Por ejemplo, la representación histórica:

```yaml
schema_version: "1.0"

component:
  id: README-HERO
  name: Hero
  family: README
  category: presentation
  version: "1.0.0"
  status: stable
  owner: Maintainer

classification:
  priority: required
  maturity: L2
  audience:
    - Developer
  repository_types:
    - backend
```

se normaliza estructuralmente como:

```yaml
schema_version: "1.0"

id: README-HERO
name: Hero
family: README
version: "1.0.0"
status: Stable
priority: Required

description: >
  ...

owner: Maintainer

audience:
  - Developer

maturity: L2

category: presentation

repository_types:
  - backend
```

Los valores del ejemplo son ilustrativos. La migración real debe conservar los valores existentes de cada Component.

#### 15.1.3 Preservación de metadata rica

Los README Components no presentan todos el mismo nivel de detalle.

Algunos disponen de un contrato relativamente reducido; otros, como `README-HERO`, incluyen información adicional de composición, restricciones, calidad, implementación y mantenimiento.

La normalización no debe reducir todos los Components a un subconjunto mínimo.

El Common Core establece propiedades compartidas, no un límite máximo de expresividad.

#### 15.1.4 Estructuras internas

Las estructuras internas de las extensiones README deben conservarse durante la migración inicial, salvo cuando contradigan directamente el contrato común.

No deben renombrarse, simplificarse o reinterpretarse propiedades específicas únicamente para facilitar la implementación del Validator.

La definición de reglas detalladas para una extensión debe basarse en su contrato existente y en evidencia de uso.

#### 15.1.5 Validación

La validación de README Components puede comprobar:

* presencia y tipos de propiedades obligatorias del Common Core;
* coherencia de `family` e `id`;
* representación de propiedades opcionales conocidas;
* estructura determinista de extensiones cuando exista un contrato establecido.

No debe evaluar automáticamente la calidad editorial, la utilidad del contenido o la adecuación arquitectónica de una sección README.

---

### 15.2 Documentation Components

Los Documentation Components implementados utilizan actualmente un modelo de metadata que puede representarse mediante el Common Core.

En esta primera versión no se ha identificado una extensión específica obligatoria para la familia `Documentation`.

#### 15.2.1 Contrato inicial

Un Documentation Component normalizado puede representarse mediante:

```yaml
schema_version: "1.0"

id: DOC-ARCHITECTURE
name: Architecture
family: Documentation
version: "0.1.0"
status: Experimental
priority: Required

description: >
  ...

audience:
  - Developer

maturity: L3

dependencies: []
```

Los valores deben corresponder al Component real.

#### 15.2.2 Ausencia de extensiones obligatorias

No debe introducirse una estructura artificial para Documentation únicamente por simetría con README o Workflow.

El siguiente modelo es suficiente:

```text
Documentation Component
└── Common Core
```

Si una futura implementación demuestra la necesidad de metadata específica, podrá definirse una extensión de Documentation.

Dicha extensión deberá respetar el Common Core y las reglas de evolución del schema.

#### 15.2.3 Validación

La validación inicial de Documentation Components se concentra en el contrato común y en la coherencia de identidad y ubicación física.

La ausencia de extensiones específicas no constituye una deficiencia del modelo.

---

### 15.3 Workflow Components

Los Workflow Components describen responsabilidades reutilizables relacionadas con prácticas, convenciones, configuraciones y mecanismos de trabajo de un repositorio.

Su metadata incluye propiedades específicas que permiten representar cómo se materializa, adopta y valida una responsabilidad Workflow.

La primera versión del contrato reconoce cuatro extensiones:

```text
Workflow Component
│
├── Common Core
│
├── materialization
├── artifacts
├── adoption
└── validation
```

Estas propiedades conservan su semántica específica de Workflow.

#### 15.3.1 Materialization

`materialization` describe cómo se materializa la responsabilidad del Workflow Component.

Ejemplo:

```yaml
materialization:
  primary:
    - Community File
    - Configuration
  executable: false
```

La representación debe permitir distinguir entre una responsabilidad materializada mediante archivos, configuración, convenciones u otros mecanismos reconocidos por el modelo Workflow.

`executable` debe representarse como booleano YAML.

Un Component puede estar implementado sin disponer de un artefacto ejecutable.

La existencia de una materialización convencional no implica que deba generarse un archivo artificial para satisfacer el contrato.

#### 15.3.2 Artifacts

`artifacts` declara archivos asociados a la implementación del Workflow Component.

Ejemplo:

```yaml
artifacts:
  specification: README.md
  templates:
    - templates/bug_report.yml
    - templates/feature_request.yml
    - templates/config.yml
```

La especificación puede existir sin que el Component disponga de templates.

Ejemplo:

```yaml
artifacts:
  specification: README.md
```

La ausencia de `templates` es válida cuando la responsabilidad se materializa mediante una convención u otro mecanismo que no requiera archivos adicionales.

Las rutas declaradas deben interpretarse respecto a la ubicación del Component, salvo que el contrato específico establezca expresamente otra base.

#### 15.3.3 Adoption

`adoption` describe las condiciones de adopción del Workflow Component por un repositorio consumidor.

Ejemplo:

```yaml
adoption:
  target: .github/ISSUE_TEMPLATE/
  specialization: Allowed
```

Cuando no exista un destino físico concreto, puede declararse únicamente la política de especialización:

```yaml
adoption:
  specialization: Allowed
```

Los valores demostrados para `specialization` son:

* `Allowed`;
* `Required`.

La especialización del consumidor debe preservar la responsabilidad del Component.

No implica que el artefacto adoptado tenga que ser textualmente idéntico al artefacto canónico.

La validación del destino de adopción debe distinguir entre la definición reutilizable del Component y su materialización en un repositorio consumidor.

#### 15.3.4 Validation

`validation` registra evidencia de validación del Workflow Component.

Ejemplo:

```yaml
validation:
  dogfooding: true
  reference_implementation: Validated
```

`dogfooding` debe ser un booleano YAML.

`reference_implementation` debe utilizar un estado reconocido por el contrato Workflow.

La validación de Reference Implementation es independiente del lifecycle.

Por tanto:

```yaml
status: Experimental

validation:
  dogfooding: true
  reference_implementation: Validated
```

puede representar un estado coherente.

El Validator no debe promocionar automáticamente el lifecycle a partir de la evidencia declarada.

#### 15.3.5 Preservación de las materializaciones existentes

Los cinco Core Workflow Components implementados demuestran mecanismos distintos:

| Component          | Materialización principal      |
| ------------------ | ------------------------------ |
| `WCL-ISSUE`        | Community File + Configuration |
| `WCL-PULL-REQUEST` | Community File                 |
| `WCL-CODE-REVIEW`  | Convention + Configuration     |
| `WCL-BRANCH`       | Convention                     |
| `WCL-COMMIT`       | Convention                     |

La normalización debe conservar estas diferencias.

No debe exigir templates o ejecutables a Components cuya responsabilidad ya está materializada mediante convenciones.

#### 15.3.6 Validación

Las reglas deterministas de Workflow pueden comprobar:

* estructura de `materialization`;
* tipos de los campos declarados;
* existencia de artefactos locales;
* representación de `adoption`;
* valores permitidos de especialización;
* representación de evidencia de validación.

La validación no debe sustituir la revisión humana sobre la adecuación de una convención, la calidad de una revisión de código o la suficiencia de la evidencia de dogfooding.

---

## 16. Canonical Values

El Common Component Metadata Schema utiliza representaciones canónicas para los campos compartidos cuyo vocabulario está establecido.

La normalización debe eliminar diferencias accidentales de escritura sin modificar la semántica.

### 16.1 Valores comunes

| Campo            | Valores o representación                                    |
| ---------------- | ----------------------------------------------------------- |
| `schema_version` | String; versión inicial `"1.0"`.                            |
| `id`             | String; identificador canónico de Component.                |
| `name`           | String no vacío.                                            |
| `family`         | `README`, `Documentation`, `Workflow`.                      |
| `version`        | String con representación `MAJOR.MINOR.PATCH`.              |
| `status`         | Lifecycle canónico reconocido por el Framework.             |
| `priority`       | `Required`, `Recommended`, `Optional`.                      |
| `description`    | String no vacío.                                            |
| `owner`          | String no vacío cuando esté presente.                       |
| `audience`       | Lista de strings no vacíos cuando esté presente.            |
| `maturity` | Nivel `L1`–`L4` o estructura `minimum` / `recommended` / `supported`. |
| `dependencies`   | Lista simple o estructura clasificada cuando esté presente. |

El conjunto definitivo de valores de lifecycle y maturity debe mantenerse alineado con los estándares arquitectónicos vigentes.

No deben introducirse nuevos estados o niveles únicamente para satisfacer una implementación de tooling.

### 16.2 Normalización de escritura

Las diferencias históricas de capitalización deben normalizarse cuando exista una correspondencia semántica inequívoca.

Ejemplos:

```text
stable       → Stable
required     → Required
recommended  → Recommended
optional     → Optional
```

La normalización de escritura no debe utilizarse para cambiar una clasificación.

### 16.3 Valores específicos de familia

Las extensiones pueden definir sus propios valores controlados cuando exista un contrato demostrado.

En Workflow, por ejemplo:

```yaml
adoption:
  specialization: Required
```

La coincidencia textual entre un valor de extensión y un valor del Common Core no implica que ambos campos representen el mismo concepto.

`priority: Required` y `adoption.specialization: Required` pertenecen a dimensiones diferentes.

### 16.4 Valores no cerrados

No todos los campos deben convertirse en enumeraciones.

Por ejemplo, `name`, `description` y `owner` representan información abierta.

`audience` tampoco dispone todavía de un vocabulario cerrado universal demostrado.

El Validator no debe rechazar valores legítimos de campos abiertos por no pertenecer a una lista arbitraria.

---

## 17. Validation Requirements

El Component Metadata Standard define las condiciones que pueden ser comprobadas mediante validación determinista.

La implementación ejecutable del Framework Validator pertenece a #25.

Este apartado establece el contrato que dicha implementación deberá respetar, sin imponer todavía una arquitectura interna, librería o interfaz de ejecución.

### 17.1 Descubrimiento

Los Components implementados se descubren desde:

```text
framework/components/
```

Cada Component descubierto debe disponer de un archivo `metadata.yml` en su ubicación canónica.

La existencia de un identificador en el Component Catalog no implica por sí sola que exista una implementación física.

### 17.2 Validación del Common Core

El Validator debe poder comprobar:

* existencia de los campos obligatorios;
* tipos de datos;
* valores no vacíos;
* versión de schema reconocida;
* formato de versión del Component;
* valores controlados;
* representación de propiedades opcionales presentes.

La ausencia de un campo opcional no constituye un error.

### 17.3 Identidad y coherencia

El Validator debe poder comprobar:

* unicidad de `id`;
* coherencia entre `id` y `family`;
* coherencia determinista entre familia y ubicación física;
* ausencia de duplicación de propiedades comunes mediante wrappers históricos.

La validación no debe inventar identificadores ni modificar automáticamente la identidad de un Component.

### 17.4 Reglas específicas por familia

Las reglas específicas deben aplicarse únicamente a la familia correspondiente.

No debe exigirse a un Documentation Component que declare `materialization`, ni a un Workflow Component que declare `repository_types`.

La existencia de extensiones no implica que todas sus propiedades sean obligatorias para todos los Components de esa familia.

### 17.5 Validación de artefactos

Cuando un Component declare artefactos físicos mediante un contrato conocido, el Validator debe poder comprobar su existencia.

La comprobación debe utilizar la base de rutas establecida por el contrato.

Una convención no debe tratarse automáticamente como un archivo ausente.

### 17.6 Referencias y dependencias

Las referencias machine-readable deben validarse según su semántica.

La validación debe distinguir entre:

* referencias a Components implementados;
* referencias a Components conceptuales reconocidos;
* referencias inválidas;
* rutas locales;
* destinos de adopción del consumidor.

No todas las referencias tienen que resolver a un archivo físico del propio Component.

### 17.7 Resultados

El Validator deberá proporcionar resultados comprensibles que permitan identificar, como mínimo:

* Component afectado;
* regla incumplida;
* ubicación o propiedad relevante;
* descripción del problema.

La ejecución deberá distinguir de forma determinista entre validación satisfactoria y validación fallida.

El formato concreto del reporte y los códigos de salida se definirán durante la implementación del Framework Validator.

### 17.8 Límites de la validación

La validación determinista no debe decidir:

* si un Component debería existir;
* si su diseño es adecuado;
* si su descripción es editorialmente suficiente;
* si una dependencia es funcionalmente necesaria;
* si una materialización es la mejor alternativa;
* si corresponde promocionar su lifecycle;
* si una Reference Implementation aporta evidencia arquitectónica suficiente.

Estas decisiones permanecen bajo responsabilidad de los maintainers.

### 17.9 Contrato y ejecución

El estándar define las reglas normativas.

El Validator implementa comprobaciones ejecutables sobre dichas reglas.

La Reference Implementation demuestra su aplicación sobre un repositorio real.

La relación prevista es:

```text
Component Metadata Standard
            │
            ▼
Normalized Component Metadata
            │
            ▼
Framework Validator
            │
            ▼
Automation Reference Implementation
            │
            ▼
Dogfooding Evidence
```

La implementación puede revelar necesidades de refinamiento del contrato.

Cualquier modificación normativa resultante deberá documentarse explícitamente y no introducirse como una excepción oculta dentro del Validator.

---

## 18. Metadata Normalization Principles

La normalización de metadata tiene como objetivo establecer una representación estructural común para los Framework Components implementados.

La normalización DEBE eliminar diferencias accidentales entre familias sin alterar la responsabilidad, identidad o semántica de los Components.

El proceso seguirá estos principios:

* **Preservación semántica:** los valores existentes mantienen su significado.
* **Núcleo común:** los campos compartidos utilizan una ubicación y representación canónicas.
* **Extensibilidad por familia:** las estructuras específicas se conservan cuando expresan necesidades reales.
* **Migración sin pérdida:** ningún dato significativo se elimina para simplificar el esquema.
* **Ausencia de valores inventados:** los campos opcionales no se completan artificialmente.
* **Automatización posterior:** el Validator consume el contrato normalizado, no formatos históricos.

La normalización no constituye una revisión arquitectónica de los Components.

```text
Existing Component Metadata
            ↓
Structural Normalization
            ↓
Common Component Metadata Schema
            ↓
Deterministic Validation
```

### 18.1 Normalization Boundary

La normalización PUEDE modificar:

* ubicación de campos;
* estructuras de agrupación innecesarias;
* representación de valores controlados;
* incorporación de `schema_version`;
* formato YAML cuando no afecte a su significado.

La normalización NO DEBE modificar automáticamente:

* identificadores;
* nombres;
* versiones de Component;
* responsabilidades;
* dependencias reales;
* lifecycle;
* prioridades;
* maturity;
* políticas de adopción;
* estados de validación;
* artefactos declarados.

Cuando se detecte una inconsistencia semántica, deberá registrarse y evaluarse separadamente.

No deberá corregirse silenciosamente como parte de una transformación estructural.

---

## 19. Family Migration Rules

La migración al contrato común deberá adaptarse a las estructuras actualmente implementadas.

### 19.1 README Components

Los README Components utilizan actualmente una estructura anidada basada en:

```yaml
component:
  id:
  name:
  family:
  category:
  description:
  version:
  status:

classification:
  priority:
```

La normalización trasladará los campos compartidos al nivel raíz:

```yaml
schema_version: "1.0"

id: README-ARCHITECTURE
name: Repository Architecture
family: README
version: "1.0.0"
status: Stable
priority: Recommended

description: >
  Resume la arquitectura técnica del proyecto y enlaza
  a la documentación detallada.

category: engineering
```

Las propiedades específicas de README permanecerán como extensiones.

Entre ellas podrán encontrarse:

```text
category
repository_types
responsibilities
non_responsibilities
inputs
outputs
compatibility
composition
constraints
quality_gates
files
catalog
implementation
maintenance
```

La migración NO DEBE eliminar extensiones únicamente porque otros Component families no las utilicen.

### 19.2 Documentation Components

Los Documentation Components implementados ya utilizan una estructura plana compatible con el núcleo común.

Su normalización deberá incorporar:

```yaml
schema_version: "1.0"
```

y preservar los campos existentes.

Ejemplo:

```yaml
schema_version: "1.0"

id: DOC-ARCHITECTURE
name: Architecture
family: Documentation
version: "0.1.0"
status: Experimental
priority: Required

audience:
  - Developer

maturity: L3

description: >
  Componente reutilizable para describir la arquitectura
  de un proyecto.

dependencies: []
```

No deberán añadirse extensiones específicas de Documentation sin una necesidad demostrada.

### 19.3 Workflow Components

Los Workflow Components implementados utilizan una estructura plana que incorpora extensiones propias de su familia.

La normalización deberá incorporar `schema_version` y preservar:

```text
materialization
artifacts
adoption
validation
```

Ejemplo:

```yaml
schema_version: "1.0"

id: WCL-ISSUE
name: Issue
family: Workflow
version: "0.1.0"
status: Experimental
priority: Required

audience:
  - Maintainer
  - Contributor

maturity: L2

description: >
  Componente reutilizable para estructurar
  la creación de Issues.

dependencies: []

materialization:
  primary:
    - Community File
    - Configuration
  executable: false

artifacts:
  specification: README.md
  templates:
    - templates/bug_report.yml
    - templates/feature_request.yml
    - templates/config.yml

adoption:
  target: .github/ISSUE_TEMPLATE/
  specialization: Allowed

validation:
  dogfooding: true
  reference_implementation: Validated
```

La normalización NO DEBE modificar las políticas de materialización, adopción o validación.

---

## 20. Preservation of Structured Metadata

El contrato común no exige que todos los campos compartidos tengan una estructura escalar.

Cuando un Component necesite una representación más expresiva, esta deberá conservarse.

### 20.1 Maturity

La maturity PUEDE representarse mediante un nivel simple:

```yaml
maturity: L2
```

o mediante una estructura de niveles:

```yaml
maturity:
  minimum: L1
  recommended: L2
  supported:
    - L1
    - L2
    - L3
    - L4
```

La segunda representación NO DEBE reducirse automáticamente a un único nivel.

Ambas representaciones expresan información válida, aunque con diferente profundidad.

El Validator deberá comprobar la estructura correspondiente sin interpretar que ambas formas contienen información equivalente.

### 20.2 Dependencies

Un Component sin dependencias PUEDE declarar:

```yaml
dependencies: []
```

Cuando exista una clasificación explícita, deberá preservarse:

```yaml
dependencies:
  required:
    - id: VCL-HERO
      minimum_version: "1.0.0"

  recommended:
    - id: VCL-BANNER
      minimum_version: "1.0.0"

  optional: []
```

La normalización NO DEBE:

* eliminar `minimum_version`;
* convertir dependencias recomendadas en obligatorias;
* transformar relaciones de composición en dependencias;
* declarar una dependencia como satisfecha por el mero hecho de existir su ID en el Catalog.

La validez de una referencia y la disponibilidad de su implementación son comprobaciones diferentes.

Un Component PUEDE referenciar una responsabilidad `Conceptual` cuando su contrato lo permita.

### 20.3 Lifecycle and Implementation

El campo común:

```yaml
status: Stable
```

representa lifecycle.

No deberá confundirse con una extensión como:

```yaml
implementation:
  status: implemented
```

que representa clasificación de implementación.

Del mismo modo:

```yaml
validation:
  reference_implementation: Validated
```

representa evidencia de validación.

Estas dimensiones permanecen independientes:

```text
Lifecycle
    ≠
Implementation Classification
    ≠
Validation
```

La normalización de valores controlados NO DEBE provocar promociones automáticas de lifecycle ni cambios de clasificación.

---

## 21. Validation Contract

El Component Metadata Standard constituye el contrato normativo que deberá consumir el Framework Validator.

Las reglas de validación se establecen en la sección 17. Esta sección delimita su aplicación durante la normalización y la implementación del tooling.

### 21.1 Contract Before Tooling

El Validator deberá consumir metadata normalizada conforme al Common Component Metadata Schema.

La implementación no deberá definir un contrato alternativo ni incorporar una capa permanente de compatibilidad para interpretar los wrappers históricos `component` y `classification`.

Si la implementación identifica una inconsistencia del estándar, deberá documentarse y resolverse en el contrato antes de introducir una excepción específica en el Validator.

### 21.2 Validation Responsibilities

La validación deberá distinguir tres niveles:

| Nivel             | Responsabilidad                                                                          |
| ----------------- | ---------------------------------------------------------------------------------------- |
| Common Core       | Comprobar los campos, tipos, valores y relaciones compartidos.                           |
| Family Extensions | Comprobar únicamente las reglas específicas demostradas para la familia correspondiente. |
| Cross-Component   | Comprobar identidad, duplicados y referencias cuya resolución sea determinista.          |

La ausencia de un campo opcional no constituye un error.

La ausencia de una extensión específica de otra familia tampoco constituye un error.

Las reglas ejecutables deberán derivarse de este estándar y de los contratos de familia aplicables, no de suposiciones sobre la estructura de otros Components.

### 21.3 Validation and Migration

La migración de metadata y la implementación del Validator son entregables distintos.

El Issue #24 deberá establecer una representación común para los Components existentes y revisar que se preserva su semántica.

El Issue #25 implementará comprobaciones deterministas sobre el contrato resultante.

El Validator no deberá utilizarse como justificación para eliminar metadata legítima o simplificar estructuras que contienen información significativa.

### 21.4 Human Decisions

Superar la validación estructural no implica que un Component haya sido aprobado arquitectónicamente.

El Validator no deberá modificar lifecycle, maturity, prioridad, dependencias ni estados de validación.

Las decisiones arquitectónicas y las promociones de lifecycle permanecen bajo responsabilidad humana.

La Automation Reference Implementation deberá demostrar el uso del Validator sin atribuirle capacidades de evaluación que excedan este contrato.

---

## 22. Migration and Acceptance Criteria

La adopción del Common Component Metadata Schema deberá completarse mediante una migración verificable.

### 22.1 Migration Sequence

La secuencia prevista es:

```text
Component Metadata Standard
            ↓
Metadata Normalization
            ↓
Migration Review
            ↓
Framework Validator
            ↓
Automation Reference Implementation
```

El estándar se define en el Issue #23.

La migración de los Components existentes corresponde al Issue #24.

El Validator corresponde al Issue #25.

La Reference Implementation y el dogfooding corresponden al Issue #26.

### 22.2 Migration Acceptance Criteria

La migración deberá demostrar que:

* los 21 Components actualmente implementados utilizan el contrato común;
* cada Component dispone de `schema_version`;
* los campos compartidos utilizan las ubicaciones canónicas;
* los valores controlados están normalizados;
* las extensiones específicas permanecen disponibles;
* los estados de lifecycle conservan su significado;
* las versiones de Component no cambian por la migración estructural;
* las dependencias mantienen su clasificación e información;
* los artefactos declarados no se pierden;
* la metadata continúa siendo YAML válido;
* no se han introducido campos opcionales artificiales;
* no se necesita una capa permanente de adaptadores para leer los Components migrados.

La validación de estos criterios deberá realizarse antes de construir el Validator sobre el nuevo contrato.

### 22.3 Standard Acceptance Criteria

El Issue #23 podrá considerarse completado cuando:

* el núcleo común esté definido;
* los campos obligatorios y opcionales estén diferenciados;
* los valores controlados estén documentados;
* las extensiones por familia estén delimitadas;
* las representaciones estructuradas existentes estén contempladas;
* las reglas de normalización estén definidas;
* los límites de validación estén establecidos;
* el contrato pueda aplicarse a los 21 Components implementados sin pérdida semántica identificada.

La finalización del estándar NO implica que la migración o el Validator estén implementados.

---

## 23. Conclusions

El Common Component Metadata Schema establece una base estructural compartida para los Framework Components implementados.

El núcleo común proporciona consistencia.

Las extensiones por familia preservan las diferencias legítimas.

La normalización elimina diferencias históricas innecesarias antes de introducir automatización.

```text
Common Contract
       +
Family Extensions
       ↓
Normalized Component Metadata
       ↓
Deterministic Validation
```

El contrato distingue explícitamente:

```text
Schema Version
    ≠
Component Version
```

```text
Lifecycle
    ≠
Implementation Classification
    ≠
Validation
```

```text
Structural Conformity
    ≠
Architectural Correctness
```

La primera versión del estándar se limita a las necesidades demostradas por los 21 Framework Components actualmente implementados.

Las futuras extensiones deberán derivarse de nuevas implementaciones y evidencia real.

**Principio final:**

> Normalize established contracts first. Automate deterministic operations second.
