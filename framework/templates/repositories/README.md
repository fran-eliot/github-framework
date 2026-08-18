# Repository Templates

La **Repository Template Library** define composiciones reutilizables de GitHub Framework Components para construir repositorios coherentes según su tipo y nivel de madurez.

Mientras los Components representan capacidades reutilizables independientes, los Repository Templates representan **composiciones reutilizables** de esas capacidades.

---

## 1. Propósito

Los Repository Templates permiten crear estructuras de repositorio consistentes sin duplicar componentes ni mantener esqueletos independientes incompatibles.

Su objetivo es:

- seleccionar Components reutilizables;
- definir cuáles son obligatorios, recomendados u opcionales;
- aportar únicamente estructura específica del tipo de repositorio;
- establecer reglas de personalización;
- proporcionar una base coherente para futuras herramientas de generación.

Un Repository Template no representa un repositorio terminado.

Representa una composición reutilizable que podrá instanciarse posteriormente como un repositorio concreto.

---

## 2. Modelo Conceptual

La relación principal del sistema es:

```text
GitHub Framework
      │
      ├── Components
      │      └── reusable capabilities
      │
      └── Repository Templates
             └── reusable compositions
```

Un Template selecciona y configura Components.

La dependencia es unidireccional:

```text
Repository Template
        │
        ▼
    Components
```

Un Component no deberá depender de un Repository Template.

---

## 3. Component vs Repository Template

| Responsabilidad | Component | Repository Template |
| --------------- | :-------: | :-----------------: |
| Resolver una responsabilidad reutilizable | ✅ | ❌ |
| Representar una composición | ❌ | ✅ |
| Ser reutilizable entre proyectos | ✅ | ✅ |
| Seleccionar Components | ❌ | ✅ |
| Definir estructura específica de un tipo de repositorio | ❌ | ✅ |
| Disponer de una definición canónica propia | ✅ | ✅ |
| Preparar una futura instanciación | ❌ | ✅ |

La separación entre ambas abstracciones deberá mantenerse explícita.

La definición canónica de cada elemento corresponde a sus artefactos contractuales y metadata, no al catálogo que permite descubrirlo.

---

## 4. Familia

Los Repository Templates utilizan el prefijo:

```text
TPL-
```

Ejemplos:

```text
TPL-BACKEND
TPL-FULLSTACK
TPL-DOCUMENTATION
```

Los identificadores deberán ser:

- únicos;
- estables;
- escritos en inglés;
- independientes del nombre físico del directorio.

---

## 5. Ubicación

La Repository Template Library se encuentra en:

```text
framework/templates/repositories/
```

La estructura base es:

```text
repositories/
├── README.md
└── <repository-template>/
    ├── metadata.yml
    ├── README.md
    └── template/        # opcional
```

El directorio `template/` es opcional.

Solo deberá existir cuando el Repository Template necesite artefactos físicos propios cuya responsabilidad no esté cubierta por Framework Components.

No se crearán directorios vacíos para representar estructura todavía no necesaria.

---

## 6. Naming

### Identificador

Formato:

```text
TPL-<NAME>
```

Ejemplos:

```text
TPL-BACKEND
TPL-FULLSTACK
TPL-DOCUMENTATION
```

### Directorio

Los directorios utilizarán minúsculas y `kebab-case`.

Ejemplos:

```text
TPL-BACKEND        → backend/
TPL-FULLSTACK      → fullstack/
TPL-DOCUMENTATION  → documentation/
```

### Archivos contractuales

Todo Repository Template seguirá inicialmente este contrato mínimo:

```text
<template>/
├── metadata.yml
└── README.md
```

Cuando exista estructura física específica del Template podrá añadirse:

```text
<template>/
├── metadata.yml
├── README.md
└── template/
```

El directorio `template/` no forma parte del contrato mínimo obligatorio.

No se añadirán archivos o directorios adicionales sin una necesidad demostrada.

---

## 7. Metadata

La metadata mínima de un Repository Template será:

```yaml
id:
name:
family:
version:
status:
project_type:
maturity:
description:
components:
  required: []
  recommended: []
  optional: []
```

La metadata deberá permanecer procesable por máquinas y evitar campos especulativos.

---

### Definición canónica

La definición canónica de un Repository Template implementado está formada por:

```text
<repository-template>/
├── README.md
└── metadata.yml
```

Cuando exista:

```text
template/
```

sus artefactos forman parte de la implementación del Template, pero no sustituyen su especificación ni su metadata.

Por tanto:

```text
README.md
        +
metadata.yml
        +
template/ (when applicable)
        ↓
Canonical Repository Template Definition
```

El Component Catalog podrá registrar y facilitar el descubrimiento del Template, pero no constituye su definición canónica.

---

## 8. Identidad

### `id`

Identificador permanente del Template.

Ejemplo:

```yaml
id: TPL-BACKEND
```

### `name`

Nombre legible del Template.

Ejemplo:

```yaml
name: Backend Repository
```

### `family`

La familia inicial será:

```yaml
family: Repository
```

### `project_type`

Representa el tipo de repositorio.

Valores iniciales podrán incluir:

```text
Backend
FullStack
Documentation
```

La incorporación de nuevos tipos deberá estar respaldada por una diferencia estructural o compositiva real.

---

## 9. Versionado

Cada Repository Template mantiene una versión independiente de la versión global del Framework.

Formato:

```text
MAJOR.MINOR.PATCH
```

Ejemplo:

```text
GitHub Framework v0.4.0

TPL-BACKEND v0.1.0
```

### MAJOR

Cambios incompatibles en el contrato, estructura o composición del Template.

### MINOR

Nuevas capacidades compatibles o ampliaciones que no rompen el contrato existente.

### PATCH

Correcciones que no modifican el contrato del Template.

Los primeros Templates deberán comenzar normalmente como:

```yaml
version: 0.1.0
status: Experimental
```

---

## 10. Estados

Los Repository Templates utilizarán los estados oficiales del Framework:

```text
Draft
Experimental
Stable
Deprecated
Retired
```

### Draft

El Template se encuentra en especificación o implementación inicial.

### Experimental

Existe una implementación funcional y se encuentra en validación.

### Stable

El Template ha sido validado mediante un mecanismo representativo y se recomienda para reutilización.

### Deprecated

Existe una alternativa recomendada y el Template permanece disponible temporalmente.

### Retired

El Template ya no deberá utilizarse para nuevas instancias.

---

## 11. Maturity

Cada Template declarará el nivel mínimo de madurez para el que resulta apropiado.

Valores:

```text
L1
L2
L3
L4
```

La madurez representa el nivel mínimo recomendado del repositorio consumidor.

No representa la madurez interna del propio Template.

---

## 12. Modelo de Composición

Un Repository Template declara explícitamente los Components que forman parte de su composición.

Ejemplo conceptual:

```yaml
components:
  required:
    - <COMPONENT_ID>

  recommended:
    - <COMPONENT_ID>

  optional:
    - <COMPONENT_ID>
```

Cada Component deberá pertenecer a un único requirement level dentro del Template.

### Requirement Level vs Component Priority

Los requirement levels declarados por un Repository Template son contextuales.

```text
required
recommended
optional
```

expresan la necesidad de un Component dentro de ese Template concreto.

No deberán confundirse con el campo priority de la metadata canónica del Component.

Por tanto:

```text
Component priority
≠
Template requirement level
```

Un Component con `priority: Required` podrá ser `recommended`, `optional` o no formar parte de determinados Repository Templates.

---

## 13. Required Components

Los Components `required` forman parte del contrato mínimo del Template.

Eliminar uno implica que la implementación deja de cumplir completamente ese Repository Template.

Ejemplo conceptual:

```text
required
    ↓
minimum template contract
```

Los elementos obligatorios deberán ser realmente necesarios.

---

## 14. Recommended Components

Los Components `recommended` representan la composición habitual del Template.

Podrán omitirse justificadamente sin invalidar el Template.

```text
recommended
    ↓
expected but removable
```

No deberán utilizarse para ocultar elementos que realmente sean obligatorios.

---

## 15. Optional Components

Los Components `optional` representan capacidades compatibles y relevantes para el tipo de repositorio.

No deberán utilizarse para listar todos los Components técnicamente compatibles con el Template.

```text
optional
    ↓
relevant contextual extension
```

El Component Catalog proporciona la vista centralizada de descubrimiento y clasificación del inventario reconocido por el Framework.

Las definiciones canónicas permanecen en las especificaciones, metadata e implementaciones correspondientes.

---

## 16. Fuentes Canónicas

Los Repository Templates referencian Framework Components mediante sus identificadores estables.

No mantienen copias independientes de sus especificaciones canónicas.

```text
Component Specification + Metadata
        │
        │ canonical definition
        ▼
Framework Component
        │
        │ referenced by ID
        ▼
Repository Template
        │
        │ composition
        ▼
Repository Implementation
```

Cada Repository Template mantiene a su vez su propia definición canónica mediante sus artefactos contractuales y metadata.

La futura instanciación podrá materializar el contenido requerido dentro del repositorio generado.

El Template no deberá mantener una segunda definición incompatible de ningún Component.

---

## 17. Estructura Específica

Cuando un Repository Template necesite estructura física propia podrá incorporar el directorio:

```text
template/
```

Este directorio contendrá únicamente artefactos específicos del tipo de repositorio cuya responsabilidad no esté cubierta por Framework Components.

Antes de incorporar un archivo o directorio deberá evaluarse:

> ¿Representa una responsabilidad que podría reutilizarse independientemente en otros Templates?

Si la respuesta es afirmativa, deberá considerarse primero como candidato a Component.

La ausencia de `template/` es válida cuando el valor del Repository Template reside exclusivamente en la composición declarativa de Components y en sus reglas de instanciación.

No se crearán directorios vacíos únicamente para satisfacer una convención estructural.

---

## 18. Placeholders

Los Templates podrán utilizar placeholders para información que se resolverá durante la instanciación.

Convención:

```text
<PROJECT_NAME>
<PROJECT_DESCRIPTION>
<OWNER>
<LICENSE>
<PACKAGE_NAME>
```

Los placeholders deberán:

- escribirse en mayúsculas;
- utilizar nombres descriptivos;
- mantener un único significado;
- aparecer únicamente cuando exista una necesidad real de parametrización.

La automatización de resolución de placeholders queda fuera del alcance inicial de Repository Templates.

---

## 19. Instanciación

La relación entre Template y repositorio concreto será:

```text
Repository Template
        ↓
   Instantiation
        ↓
Concrete Repository
```

Durante la instanciación podrán:

- resolverse placeholders;
- seleccionarse Components opcionales;
- omitirse Components recomendados;
- añadirse necesidades específicas del proyecto.

El Repository Template no contiene datos reales de un proyecto concreto.

---

## 20. Personalización

Una implementación podrá personalizar el Template cuando:

- mantenga los Components `required`;
- preserve las responsabilidades arquitectónicas;
- añada Components compatibles;
- incorpore necesidades específicas del proyecto.

La personalización no deberá modificar la especificación canónica del Repository Template.

---

## 21. Template Inheritance

La herencia entre Repository Templates no forma parte de la arquitectura inicial.

No se implementarán en `v0.4.0` mecanismos como:

```text
extends
mixins
overlays
template chaining
```

La arquitectura inicial utiliza:

```text
Template
    ↓
Components
    ↓
Instantiation
```

Si una implementación real demuestra posteriormente la necesidad de composición entre Templates, la arquitectura podrá evolucionar.

---

## 22. Compatibilidad

Los Repository Templates evolucionan independientemente de los repositorios ya instanciados.

Una nueva versión de un Template no obliga automáticamente a migrar sus implementaciones existentes.

```text
TPL-BACKEND v0.1.0
        ↓
Project A

TPL-BACKEND v0.2.0
        ↓
future instances
```

La adopción de una nueva versión deberá ser explícita.

Los cambios incompatibles requerirán una versión mayor.

---

## 23. Lifecycle

El ciclo de vida esperado es:

```text
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

La validación podrá realizarse mediante:

- Reference Implementation;
- implementación real;
- instanciación representativa;
- dogfooding;
- otro caso de uso suficientemente realista.

Un Repository Template no deberá pasar a `Stable` sin una validación representativa.

---

## 24. Reference Implementation

Todo Template candidato a `Stable` deberá haber sido validado mediante al menos uno de los siguientes mecanismos:

- una implementación real;
- una instanciación representativa;
- dogfooding;
- otro caso de uso suficientemente realista.

La validación deberá comprobar especialmente:

- composición;
- límites Component / Template;
- requirement levels;
- estructura específica;
- placeholders;
- ausencia de duplicación innecesaria.

---

## 25. Quality Gates

Antes de considerar válido un Repository Template deberá verificarse:

- [ ] Tiene un identificador `TPL-*` único.
- [ ] Representa un tipo de repositorio claramente definido.
- [ ] No duplica la responsabilidad de otro Template.
- [ ] Sigue el contrato estándar de Repository Template.
- [ ] Su metadata está completa.
- [ ] Los Components utilizados están declarados explícitamente.
- [ ] Cada Component pertenece a un único requirement level.
- [ ] Los elementos `required` forman un contrato mínimo coherente.
- [ ] Los elementos `recommended` pueden omitirse justificadamente.
- [ ] Los elementos `optional` tienen una relación real con el Template.
- [ ] La estructura local contiene únicamente responsabilidades específicas del Template.
- [ ] No mantiene copias independientes de Components canónicos.
- [ ] Los placeholders son explícitos y reutilizables.
- [ ] No depende de herencia entre Templates.
- [ ] Puede instanciarse sin conocimiento implícito del autor.
- [ ] Ha sido validado mediante una implementación, Reference Implementation, instanciación representativa o dogfooding antes de pasar a `Stable`.

---

## 26. Límites de la Primera Versión

Quedan fuera del alcance inicial:

```text
Template inheritance
Automatic generation
CLI tooling
Schema validation
Automatic migrations
Template marketplace
```

Estas capacidades podrán abordarse posteriormente cuando exista evidencia real que justifique su incorporación.

---

## 27. Evolución

Un nuevo Repository Template deberá incorporarse únicamente cuando:

1. represente una composición recurrente;
2. exista una diferencia significativa respecto a los Templates existentes;
3. sus responsabilidades no puedan resolverse mediante configuración de un Template existente;
4. exista un caso de uso real;
5. pueda mantenerse sin duplicar Components.

El objetivo no es maximizar el número de Templates.

El objetivo es mantener **el conjunto mínimo de composiciones reutilizables que aporten valor real**.

---

## 28. Estado Actual

La Repository Template Architecture está definida.

Los primeros Repository Templates están implementados en estado `Experimental` y permiten validar el contrato de composición mediante casos de uso reales.

La siguiente etapa consiste en validar el modelo mediante implementaciones representativas y dogfooding antes de considerar estable cualquier Repository Template.

---

## 29. Component Availability

Los Repository Templates podrán referenciar Framework Components clasificados como `Implemented` o `Conceptual`.

La clasificación de implementación describe la disponibilidad de una implementación canónica reutilizable.

No determina el requirement level contextual del Component dentro del Template.

~~~text
Implementation classification
        ≠
Template requirement level
~~~

Por tanto, un Component `Conceptual` podrá formar parte de:

~~~text
required
recommended
optional
~~~

cuando su responsabilidad pertenezca legítimamente al contrato del Template.

En estos casos:

- su clasificación deberá ser explícita;
- no deberá presentarse como una capacidad reutilizable materialmente disponible;
- un consumer podrá satisfacer la responsabilidad mediante una implementación propia, especializada o equivalente;
- su presencia no obligará automáticamente a implementar el Framework Component.

La conformidad del consumer deberá evaluarse mediante la responsabilidad satisfecha:

~~~text
Component availability
        ≠
Consumer conformance
~~~

Un Repository Template podrá evolucionar a `Stable` cuando su contrato sea suficientemente estable y exista evidencia representativa de que todas sus responsabilidades `required` pueden satisfacerse.

La existencia de un Component `required` clasificado como `Conceptual` no impedirá por sí sola dicha promoción.

La promoción deberá basarse en evidencia de validación y no únicamente en disponibilidad material de Framework Components.
