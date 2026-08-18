# Repository Template Standards

| Campo | Valor |
|---|---|
| **Proyecto** | GitHub Framework |
| **Documento** | Repository Template Standards |
| **Versión** | 1.0.0 |
| **Estado** | Active |
| **Ámbito** | Repository Template Library |
| **Última actualización** | 2026-08-18 |

---

# 1. Propósito

Este documento define los estándares oficiales para diseñar, implementar, mantener y evolucionar Repository Templates dentro de GitHub Framework.

Los estándares formalizan patrones validados mediante:

- Repository Template Architecture;
- Core Repository Templates;
- Repository Template Reference Implementation;
- dogfooding sobre repositorios reales.

El objetivo es proporcionar convenciones consistentes para futuras familias de Templates sin duplicar decisiones arquitectónicas ni introducir requisitos basados únicamente en escenarios hipotéticos.

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

Los Repository Template Standards complementan la arquitectura.

La arquitectura define responsabilidades, relaciones y límites del modelo.

Los estándares definen las reglas prácticas que deberán seguir las implementaciones concretas.

---

# 2. Alcance

Estos estándares aplican a los Repository Templates registrados dentro de GitHub Framework.

Actualmente:

```text
TPL-BACKEND
TPL-FULLSTACK
TPL-DOCUMENTATION
```

El documento regula:

- identidad;
- naming;
- estructura;
- metadata;
- composición mediante Framework Components;
- requirement levels;
- dependencias;
- placeholders;
- especialización;
- extensibilidad;
- materialización física;
- maturity;
- versionado;
- lifecycle;
- mantenimiento;
- conformidad;
- validación;
- Quality Gates.

Quedan fuera del alcance actual:

- Template inheritance;
- generación automática;
- CLI;
- schema validation automatizada;
- migraciones automáticas;
- resolución automática de dependencias;
- Workflow Templates;
- Visual Templates;
- registros remotos de Templates.

Estos elementos podrán formalizarse en futuras versiones cuando exista implementación y evidencia suficiente.

---

# 3. Lenguaje Normativo

Los términos normativos utilizados en este documento deberán interpretarse de la siguiente forma:

| Término |	Significado |
|---|---|
| DEBE / DEBEN | Requisito obligatorio |
| NO DEBE / NO DEBEN |	Prohibición |
| DEBERÍA / DEBERÍAN | Recomendación fuerte |
| NO DEBERÍA / NO DEBERÍAN | Práctica desaconsejada |
| PUEDE / PUEDEN |	Comportamiento permitido |

Las reglas normativas deberán basarse en patrones validados mediante implementación o dogfooding.

Una posibilidad futura no constituye por sí sola justificación suficiente para introducir una regla normativa.

---

# 4. Principios

Todo Repository Template DEBE respetar los siguientes principios.

## 4.1 Composición antes que duplicación

Un Repository Template DEBE componerse mediante Framework Components cuando exista una responsabilidad reutilizable reconocida.

```text
Repository Template
        ↓
Component composition
        ↓
Repository structure
```

El Template NO DEBE duplicar internamente la especificación completa de un Component.

## 4.2 Responsabilidades antes que archivos

Los Templates DEBEN modelar responsabilidades del repositorio y no limitarse a enumerar archivos físicos.

La existencia de una responsabilidad no implica necesariamente la creación de un archivo independiente.

## 4.3 Implementación antes que estandarización

Las nuevas reglas DEBERÍAN surgir de patrones observados mediante implementación y validación.

NO DEBERÍAN introducirse convenciones únicamente para cubrir escenarios hipotéticos.

## 4.4 Simplicidad

Un Template DEBE contener únicamente la estructura y metadata necesarias para expresar su contrato.

NO DEBEN crearse archivos o directorios vacíos únicamente para satisfacer una convención estructural.

## 4.5 Dogfooding

Los Templates destinados a evolucionar hacia estados estables DEBEN validarse mediante repositorios reales o Reference Implementations representativas.

---

# 5. Identidad

Todo Repository Template registrado DEBE disponer de una identidad única.

La identidad canónica utiliza el prefijo:

```text
TPL-
```

Ejemplos:

```text
TPL-BACKEND
TPL-FULLSTACK
TPL-DOCUMENTATION
```

Un identificador DEBE:

- ser único dentro del Framework;
- permanecer estable durante la vida de la misma identidad conceptual;
- utilizar mayúsculas;
- utilizar guiones para separar términos cuando sea necesario;
- describir el tipo de repositorio y no una implementación tecnológica concreta salvo que exista una necesidad validada.

No deberán crearse IDs diferentes para representar únicamente niveles de maturity.

Ejemplo no válido:

```text
TPL-DOCUMENTATION-L2
```

La maturity se modela como propiedad del Template.

---

# 6. Naming

Los directorios de Repository Templates DEBEN utilizar kebab-case.

Ejemplos:

```text
backend/
fullstack/
documentation/
```

La estructura canónica es:

```text
framework/
└── templates/
    └── repositories/
        └── <template-name>/
```

Los nombres DEBERÍAN describir categorías reutilizables de repositorio y evitar nombres ligados a proyectos concretos.

Ejemplo recomendado:

```text
backend/
```

Ejemplo no recomendado:

```text
my-spring-project/
```

Los nombres de archivo canónicos son:

```text
README.md
metadata.yml
```

Cuando exista materialización física adicional, sus nombres DEBERÁN seguir los estándares generales de naming definidos por GitHub Framework.

---

# 7. Estructura

La estructura mínima de un Repository Template implementado es:

```text
<template-name>/
├── README.md
└── metadata.yml
```

`README.md` documenta el contrato, propósito, composición y reglas de utilización del Template.

`metadata.yml` proporciona su representación estructurada y machine-readable.

Un Template PUEDE incluir adicionalmente:

```text
template/
```

cuando exista contenido físico reutilizable que justifique su materialización.

La ausencia de `template/` NO invalida un Repository Template.

NO DEBEN crearse directorios `template/` vacíos únicamente para mantener simetría entre Templates.

---

# 8. Metadata

Todo Repository Template implementado DEBE disponer de:

```text
metadata.yml
```

La metadata DEBE identificar como mínimo:

```text
id:
name:
family:
version:
status:
project_type:
maturity:
description:
components:
```

La familia para los Repository Templates definidos actualmente es:

```text
family: Repository
```

La sección components DEBE distinguir:

```text
components:
  required:
  recommended:
  optional:
```

Un Component NO DEBE aparecer simultáneamente en más de un requirement level dentro del mismo Template.

Los IDs utilizados en la composición DEBEN corresponder a responsabilidades reconocidas por el Component Catalog.

Un Component clasificado como `Conceptual` PUEDE aparecer en la composición cuando su responsabilidad forme parte legítima del contrato del Template.

Su presencia NO DEBE interpretarse como disponibilidad material de una implementación reutilizable.

La metadata y el README del Template DEBEN permanecer semánticamente sincronizados.

Las diferencias entre ambos artefactos deberán considerarse un defecto de consistencia.

---

# 9. Component Composition

Los Repository Templates DEBEN expresar su contrato mediante composición de Framework Components.

La composición permite que un Template seleccione responsabilidades reutilizables sin duplicar sus especificaciones.

~~~text
Repository Template
        │
        ├── required
        ├── recommended
        └── optional
                ↓
        Framework Components
~~~

La composición DEBE utilizar los identificadores canónicos registrados por GitHub Framework.

Ejemplos:

~~~text
README-HERO
README-OVERVIEW
DOC-ARCHITECTURE
DOC-CHANGELOG
~~~

Un Repository Template NO DEBE copiar la definición interna completa de un Component para incorporarlo a su contrato.

La responsabilidad del Template consiste en determinar:

- qué Components forman parte de su composición;
- qué requirement level corresponde a cada Component;
- qué especializaciones contextuales resultan necesarias;
- qué dependencias deben respetarse.

La especificación interna del Component permanece gobernada por su propia definición canónica.

Un mismo Component PUEDE formar parte de diferentes Repository Templates con requirement levels distintos.

Ejemplo conceptual:

~~~text
                    TPL-BACKEND     TPL-DOCUMENTATION

DOC-ARCHITECTURE      Recommended         Required
~~~

Esta diferencia es válida porque el requirement level pertenece al contexto del Template y no constituye una propiedad global del Component.

---

# 10. Requirement Levels

Todo Component incluido en un Repository Template DEBE clasificarse en exactamente uno de los siguientes niveles:

~~~text
required
recommended
optional
~~~

Estos niveles expresan la importancia contextual de una responsabilidad dentro del contrato de un Template.

## 10.1 Required

Un Component `required` representa una responsabilidad que forma parte del contrato mínimo del Repository Template.

Un repositorio consumidor DEBE satisfacer las responsabilidades `required` aplicables para considerarse estructuralmente conforme con el Template.

`required` NO significa necesariamente que:

- deba copiarse literalmente una implementación canónica;
- deba existir un archivo independiente;
- el Framework Component correspondiente esté clasificado como `Implemented`.

La conformidad se determina por la satisfacción efectiva de la responsabilidad.

## 10.2 Recommended

Un Component `recommended` representa una responsabilidad que mejora significativamente la calidad, mantenibilidad, comprensión o gobernanza del repositorio.

Un repositorio consumidor DEBERÍA satisfacerla cuando resulte aplicable.

Su omisión PUEDE estar justificada por:

- alcance;
- maturity;
- tamaño del proyecto;
- arquitectura;
- ausencia de necesidad real;
- existencia de una responsabilidad equivalente ya cubierta.

La omisión de un Component `recommended` NO invalida automáticamente la conformidad estructural con el Template.

## 10.3 Optional

Un Component `optional` representa una responsabilidad válida que PUEDE incorporarse cuando aporte valor al repositorio.

Su ausencia no requiere justificación salvo que una especialización concreta del Template establezca lo contrario.

## 10.4 Requirement Level vs Component Priority

El requirement level de un Component dentro de un Repository Template y su prioridad global dentro del Component Catalog son dimensiones diferentes.

~~~text
Component priority
        ≠
Template requirement level
~~~

La prioridad expresa la relevancia general del Component dentro del Framework.

El requirement level expresa su relevancia dentro de un Template concreto.

Un Repository Template NO DEBE derivar automáticamente sus requirement levels de la prioridad registrada en el Component Catalog.

---

# 11. Component Availability

La composición de un Repository Template PUEDE incluir Components clasificados como:

~~~text
Implemented
Conceptual
~~~

La clasificación de implementación describe la disponibilidad de una implementación canónica reutilizable dentro del Framework.

~~~text
Implemented
    ↓
Canonical reusable implementation available

Conceptual
    ↓
Recognized responsibility without canonical implementation
~~~

La clasificación de implementación NO modifica automáticamente el requirement level asignado por un Repository Template.

~~~text
Implementation classification
        ≠
Template requirement level
~~~

Por tanto, un Component `Conceptual` PUEDE ser:

- `required`;
- `recommended`;
- `optional`.

Un Template DEBE reflejar con claridad cuando su composición contiene responsabilidades conceptuales todavía no materializadas.

NO DEBE presentar un Component `Conceptual` como si existiera una implementación reutilizable disponible.

La materialización futura de un Component `Conceptual` NO DEBE alterar automáticamente su requirement level dentro de los Templates existentes.

Cualquier cambio de requirement level deberá justificarse mediante la evolución del contrato del Template.

---

# 12. Dependencies

Los Repository Templates DEBEN respetar las dependencias definidas por los Framework Components que componen.

Un Template NO DEBE redefinir una dependencia canónica de un Component únicamente para adaptarla a una composición concreta.

Cuando un Component dependa de otra responsabilidad, el Template DEBERÁ comprobar si dicha dependencia:

- ya está satisfecha por otro Component de la composición;
- debe incorporarse explícitamente;
- puede satisfacerse mediante una implementación equivalente;
- no resulta aplicable al contexto concreto.

Las dependencias NO DEBERÍAN provocar la incorporación automática de estructuras innecesarias.

~~~text
Component dependency
        ↓
Evaluate responsibility
        ↓
Applicable?
   ┌────┴────┐
  yes        no
   ↓          ↓
satisfy     justify
~~~

Una dependencia satisfecha conceptualmente NO requiere necesariamente duplicación física.

Los Repository Templates NO DEBEN introducir sistemas de resolución automática de dependencias mientras no exista una necesidad validada y una arquitectura específica para ello.

---

# 13. Placeholders

Los Repository Templates PUEDEN utilizar placeholders cuando exista contenido que necesariamente deba adaptarse al repositorio consumidor.

Ejemplos de información potencialmente parametrizable:

~~~text
<PROJECT_NAME>
<PROJECT_DESCRIPTION>
<OWNER>
~~~

Los placeholders DEBEN:

- escribirse en mayúsculas;
- utilizar nombres descriptivos;
- mantener un único significado;
- ser claramente identificables;
- describir qué información debe proporcionar el consumer;
- evitar valores que puedan confundirse con contenido real;
- mantenerse al mínimo necesario;
- aparecer únicamente cuando la reutilización requiera personalización.

Los placeholders NO DEBEN utilizarse para simular contenido técnico que todavía no ha sido definido.

Ejemplo no recomendado:

~~~text
TODO: describe architecture here
~~~

cuando el Template no dispone de una estructura o responsabilidad arquitectónica suficientemente definida.

Los Templates NO DEBEN convertirse en colecciones extensas de texto provisional.

Cuando una responsabilidad pueda expresarse mediante un Framework Component, DEBERÍA preferirse la composición frente a la duplicación de placeholders equivalentes.

Los placeholders incluidos dentro de artefactos materializados DEBERÁN eliminarse o sustituirse durante la adopción del Template cuando formen parte del contenido final del repositorio consumidor.

---

# 14. Specialization

Un Repository Template PUEDE especializar el uso de Framework Components para adaptarlos al contexto del tipo de repositorio que representa.

La especialización PUEDE afectar a:

- requirement level;
- orden recomendado;
- contexto de utilización;
- instrucciones de adopción;
- ejemplos;
- relaciones con otros Components.

La especialización NO DEBE modificar la identidad ni la responsabilidad fundamental del Component.

~~~text
Framework Component
        ↓
Canonical responsibility
        ↓
Template specialization
        ↓
Contextual usage
~~~

Si una especialización modifica sustancialmente la responsabilidad original hasta convertirla en otro concepto, DEBERÍA evaluarse la creación de un nuevo Component en lugar de extender artificialmente el existente.

Un Template NO DEBE mantener copias divergentes de la especificación canónica de un Component.

Las especializaciones relevantes DEBERÍAN quedar documentadas en el README del Template cuando afecten a su correcta adopción.

---

# 15. Extensibility

Los Repository Templates DEBEN permitir que un repositorio consumidor incorpore responsabilidades adicionales cuando su contexto lo requiera.

La composición declarada por un Template define una base reutilizable, no una lista cerrada de capacidades permitidas.

~~~text
Template contract
        +
Consumer-specific responsibilities
        ↓
Concrete repository
~~~

Un consumer PUEDE añadir:

- Framework Components adicionales;
- documentación específica del dominio;
- automatizaciones;
- configuraciones;
- estructuras propias;
- artefactos técnicos necesarios para su implementación.

Estas extensiones NO DEBEN invalidar las responsabilidades `required` del Template.

Un Repository Template NO DEBERÍA intentar anticipar todas las posibles extensiones futuras.

Las extensiones repetidas observadas en múltiples consumers PUEDEN constituir evidencia para:

- incorporar nuevos Components;
- modificar requirement levels;
- crear nuevos Repository Templates;
- evolucionar estándares existentes.

Dichos cambios DEBERÁN evaluarse mediante evidencia real y no únicamente por posibilidad teórica.

---

# 16. Physical Materialization

Un Repository Template define un contrato de responsabilidades y PUEDE proporcionar materialización física reutilizable.

~~~text
Repository Template
        │
        ├── Contract
        │
        └── Physical materialization (optional)
~~~

La materialización física PUEDE incluir:

- archivos;
- directorios;
- fragmentos reutilizables;
- configuraciones;
- estructuras iniciales.

Cuando exista contenido físico propio del Template, DEBERÍA ubicarse en:

~~~text
template/
~~~

salvo que una convención específica del Framework establezca otra ubicación.

La existencia de `template/` NO es obligatoria.

Un Repository Template basado únicamente en composición, metadata e instrucciones de adopción PUEDE ser válido sin materialización física adicional.

NO DEBEN crearse:

- archivos vacíos;
- directorios vacíos;
- documentos placeholder sin utilidad;
- estructuras especulativas;

únicamente para hacer que diferentes Repository Templates presenten una estructura física uniforme.

La materialización DEBE responder a una necesidad reutilizable demostrada.

## 16.1 Materialization vs Conformance

La disponibilidad de materialización reutilizable y la conformidad de un repositorio consumidor son dimensiones independientes.

~~~text
Framework Component availability
              ≠
Consumer requirement satisfaction
~~~

Un repositorio consumidor PUEDE satisfacer una responsabilidad mediante:

- una implementación canónica del Framework;
- una implementación propia;
- una implementación especializada;
- una responsabilidad equivalente distribuida entre varios artefactos.

Por tanto:

~~~text
Reusable implementation unavailable
              ↓
does not automatically imply
              ↓
Consumer non-conformance
~~~

La conformidad DEBE evaluarse por la responsabilidad satisfecha y no exclusivamente por la presencia física de una implementación canónica.

## 16.2 Equivalent Implementations

Una implementación equivalente PUEDE considerarse válida cuando:

- satisface la responsabilidad definida por el Template;
- resulta identificable durante la validación;
- no contradice las restricciones del Component o del Template;
- proporciona evidencia suficiente para evaluar su conformidad.

La equivalencia NO DEBE utilizarse para justificar la ausencia de una responsabilidad realmente necesaria.

Cuando la equivalencia no resulte evidente, DEBERÍA documentarse durante la Reference Implementation, evaluación o proceso de adopción.

## 16.3 Conceptual Components

La presencia de un Component `Conceptual` dentro de la composición de un Template indica que la responsabilidad está reconocida aunque todavía no exista implementación canónica reutilizable.

Un consumer PUEDE satisfacer dicha responsabilidad mediante una implementación propia.

Ejemplo validado mediante dogfooding:

~~~text
README-LICENSE

Framework availability → Conceptual
Consumer responsibility → Satisfied
~~~

Este comportamiento NO convierte automáticamente el Component en `Implemented`.

La transición:

~~~text
Conceptual
    ↓
Implemented
~~~

requiere la materialización y gobernanza de una implementación canónica dentro del Framework.

---

# 17. Maturity

Todo Repository Template DEBE declarar su nivel de maturity.

La maturity expresa el nivel de sofisticación estructural y documental esperado del repositorio consumidor.

La maturity NO representa:

- una versión del Template;
- un estado de lifecycle;
- una variante independiente del Template;
- una medida automática de calidad.

~~~text
Template identity
      ≠
Template maturity
      ≠
Template lifecycle status
~~~

Un mismo Repository Template mantiene su identidad aunque evolucione su maturity.

Ejemplo:

~~~text
TPL-DOCUMENTATION
        ↓
maturity: L2
~~~

NO DEBEN crearse Templates independientes cuya única diferencia sea el nivel de maturity.

Ejemplo no recomendado:

~~~text
TPL-DOCUMENTATION-L1
TPL-DOCUMENTATION-L2
TPL-DOCUMENTATION-L3
~~~

## 17.1 Maturity como propiedad

La maturity DEBE declararse como propiedad estructurada dentro de `metadata.yml`.

Ejemplo:

~~~yaml
maturity: L2
~~~

El README del Template DEBERÍA explicar las implicaciones del nivel declarado cuando resulten relevantes para su adopción.

## 17.2 Evolución de maturity

Un cambio de maturity PUEDE modificar las expectativas estructurales o documentales del Template.

Dicho cambio DEBE evaluarse explícitamente y NO DEBE utilizarse como mecanismo implícito para introducir requisitos incompatibles.

Cuando una evolución de maturity modifique el contrato del Template, el cambio DEBERÁ reflejarse también mediante el versionado correspondiente.

La maturity DEBERÍA evolucionar únicamente cuando exista evidencia suficiente obtenida mediante implementación, adopción o dogfooding.

---

# 18. Versioning

Todo Repository Template implementado DEBE declarar una versión propia.

La versión del Template describe la evolución de su contrato y es independiente de la versión global de GitHub Framework.

~~~text
GitHub Framework version
          ≠
Repository Template version
~~~

Ejemplo:

~~~yaml
id: TPL-DOCUMENTATION
version: 0.1.0
~~~

Los Repository Templates DEBEN utilizar Semantic Versioning como referencia para expresar cambios en su contrato.

~~~text
MAJOR.MINOR.PATCH
~~~

## 18.1 PATCH

Un incremento `PATCH` DEBERÍA utilizarse para cambios que no modifiquen materialmente el contrato del Template.

Ejemplos:

- correcciones de redacción;
- aclaraciones;
- correcciones de ejemplos;
- mejoras documentales;
- correcciones de metadata que no alteren la composición;
- ajustes equivalentes sin impacto contractual.

## 18.2 MINOR

Un incremento `MINOR` DEBERÍA utilizarse cuando el Template evolucione de forma compatible.

Ejemplos:

- incorporación de Components `recommended`;
- incorporación de Components `optional`;
- nuevas instrucciones de adopción;
- nuevas especializaciones compatibles;
- ampliación de metadata sin romper consumidores existentes;
- nuevas capacidades de materialización opcional.

Los cambios `MINOR` NO DEBERÍAN invalidar repositorios consumidores previamente conformes.

## 18.3 MAJOR

Un incremento `MAJOR` DEBE considerarse cuando se produzcan cambios incompatibles en el contrato.

Ejemplos:

- incorporación de nuevas responsabilidades `required` que afecten a consumers existentes;
- eliminación de responsabilidades `required`;
- cambio incompatible de significado de un requirement level;
- cambio incompatible de estructura o metadata obligatoria;
- redefinición sustancial del propósito del Template.

Antes de introducir un cambio `MAJOR`, DEBERÍA existir evidencia suficiente que justifique la ruptura de compatibilidad.

## 18.4 Sincronización de versión

La versión declarada en `metadata.yml` y cualquier referencia equivalente en la documentación del Template DEBEN permanecer sincronizadas.

Las diferencias de versión entre artefactos del mismo Template deberán considerarse un defecto de consistencia.

---

# 19. Lifecycle

Todo Repository Template DEBE declarar un estado de lifecycle.

El lifecycle describe el grado de definición, validación, soporte y retirada de la implementación del Template.

Los estados actualmente reconocidos son:

~~~text
Draft
Experimental
Stable
Deprecated
Retired
~~~

El flujo habitual es:

~~~text
Draft
  ↓
Experimental
  ↓
Stable
  ↓
Deprecated
  ↓
Retired
~~~

La transición entre estados NO DEBE producirse únicamente por antigüedad o por número de versiones publicadas.

DEBE basarse en evidencia relacionada con definición, implementación, validación y mantenimiento.

## 19.1 Draft

Un Template `Draft` se encuentra en especificación o implementación inicial.

Puede utilizarse para explorar el contrato, pero NO DEBE presentarse como una implementación reutilizable validada.

Un Template `Draft` PUEDE cambiar de forma significativa mientras se define su identidad, composición o metadata.

## 19.2 Experimental

Un Template `Experimental` representa una implementación utilizable cuyo contrato todavía puede evolucionar a partir de evidencia real.

Un Template Experimental:

- PUEDE utilizarse en Reference Implementations;
- PUEDE utilizarse para dogfooding;
- PUEDE contener Components `Conceptual`;
- PUEDE descubrir gaps durante su adopción;
- DEBE documentar limitaciones relevantes conocidas.

El estado `Experimental` NO significa que el Template sea meramente conceptual.

Debe existir una implementación material del Repository Template para utilizar este estado.

## 19.3 Stable

Un Repository Template PUEDE evolucionar a `Stable` cuando exista evidencia suficiente de que su contrato es consistente, reutilizable y mantenible.

Antes de promover un Template a `Stable`, DEBE comprobarse como mínimo que:

- su identidad y propósito están claramente definidos;
- `README.md` y `metadata.yml` están sincronizados;
- su composición ha sido validada;
- sus responsabilidades `required` son coherentes y satisfacibles;
- sus Quality Gates pueden evaluarse;
- existe evidencia suficiente de adopción, Reference Implementation, dogfooding u otro mecanismo representativo;
- los gaps críticos detectados durante la validación han sido resueltos o explícitamente aceptados;
- no existen contradicciones conocidas entre el Template y la arquitectura vigente.

La presencia de Components `Conceptual` NO impide automáticamente la promoción a `Stable`.

La decisión DEBE basarse en la estabilidad del contrato y en la capacidad demostrada de satisfacer sus responsabilidades, no exclusivamente en la disponibilidad material de todos los Framework Components referenciados.

## 19.4 Deprecated

Un Template DEBE marcarse como `Deprecated` cuando siga registrado por razones de compatibilidad o trazabilidad pero ya no deba utilizarse para nuevas adopciones.

La deprecación DEBERÍA indicar:

- motivo;
- alternativa recomendada, cuando exista;
- impacto sobre consumidores existentes;
- estrategia de transición cuando resulte necesaria.

Un Template Deprecated NO DEBE eliminarse inmediatamente si existen consumers que todavía dependan de su contrato.

## 19.5 Retired

Un Template `Retired` NO DEBE utilizarse para nuevas adopciones.

Su registro PUEDE conservarse cuando resulte necesario para:

- trazabilidad histórica;
- documentación de migraciones;
- referencia de consumidores existentes;
- comprensión de la evolución del Framework.

Un Template NO DEBERÍA evolucionar directamente a `Retired` sin pasar previamente por `Deprecated`, salvo que exista una razón excepcional documentada.

## 19.6 Transiciones de lifecycle

Las transiciones DEBEN quedar documentadas.

~~~text
Draft → Experimental
      ↓
implementation available

Experimental → Stable
      ↓
representative validation required

Stable → Deprecated
      ↓
deprecation rationale required

Deprecated → Retired
      ↓
retirement decision required
~~~

NO DEBERÍA introducirse un nuevo estado de lifecycle sin una necesidad validada.

---

# 20. Maintenance

Todo Repository Template implementado DEBE mantenerse sincronizado con las fuentes arquitectónicas y de catálogo que gobiernan su contrato.

Como mínimo, el mantenimiento DEBE considerar:

- Repository Template Architecture;
- Component Catalog;
- Framework Components utilizados;
- Repository Template Standards;
- Reference Implementations relevantes;
- metadata del propio Template.

~~~text
Architecture
      ↓
Component Catalog
      ↓
Repository Template
      ↓
Reference Implementation
      ↓
Validated findings
      ↺
~~~

## 20.1 Sincronización

Los maintainers DEBEN revisar un Template cuando cambie de forma relevante:

- la identidad de un Component utilizado;
- la responsabilidad de un Component;
- la clasificación `Implemented / Conceptual`;
- una dependencia;
- un estándar aplicable;
- una regla arquitectónica que afecte a su contrato.

La modificación de una fuente relacionada NO implica necesariamente modificar el Template.

Primero DEBE evaluarse si el cambio afecta realmente a su composición o contrato.

## 20.2 Evitar drift

El README y `metadata.yml` del Template DEBEN permanecer semánticamente alineados.

NO DEBERÁ mantenerse información contradictoria sobre:

- identidad;
- versión;
- status;
- maturity;
- composición;
- requirement levels;
- disponibilidad declarada;
- propósito.

Los datos derivados de otras fuentes DEBERÍAN mantenerse al mínimo necesario para reducir el riesgo de drift.

## 20.3 Cambios de composición

La incorporación, eliminación o reclasificación de Components DEBE justificarse mediante una necesidad del contrato.

NO DEBE modificarse una composición únicamente para:

- hacer coincidir números;
- eliminar gaps artificialmente;
- conseguir que todos los Components estén `Implemented`;
- aumentar simetría con otros Templates;
- satisfacer una expectativa no validada.

Un gap detectado durante la validación DEBERÍA tratarse como información de diseño antes de modificar el Template.

~~~text
Gap detected
      ↓
Evaluate responsibility
      ↓
 ┌────┴───────────────┐
 │                    │
Contract is valid     Contract is wrong
 │                    │
Preserve + evolve     Modify requirement
implementation        with evidence
~~~

---

# 21. Consumer Conformance

La conformidad con un Repository Template DEBE evaluarse sobre el repositorio consumidor.

El objetivo de la evaluación es determinar si el consumer satisface las responsabilidades definidas por el contrato del Template.

~~~text
Repository Template
        ↓
Responsibilities
        ↓
Consumer implementation
        ↓
Conformance assessment
~~~

La conformidad NO DEBE evaluarse únicamente mediante:

- igualdad de estructura física;
- copia literal de archivos;
- presencia de todos los Framework Components como implementaciones canónicas;
- coincidencia textual con ejemplos del Template.

## 21.1 Required Responsibilities

Para alcanzar conformidad estructural, un consumer DEBE satisfacer todas las responsabilidades `required` aplicables.

~~~text
Required responsibilities
          ↓
     all satisfied
          ↓
Structural Conformance
~~~

Una responsabilidad PUEDE satisfacerse mediante:

- implementación canónica de un Framework Component;
- implementación propia;
- especialización compatible;
- implementación equivalente;
- responsabilidad distribuida entre varios artefactos.

La evaluación DEBE considerar el resultado efectivo y no únicamente el mecanismo utilizado.

## 21.2 Recommended Responsibilities

Las responsabilidades `recommended` DEBERÍAN evaluarse para determinar si:

- están satisfechas;
- han sido omitidas justificadamente;
- no resultan aplicables;
- revelan oportunidades de mejora.

Su ausencia NO DEBE producir automáticamente no conformidad estructural.

## 21.3 Optional Responsibilities

Las responsabilidades `optional` PUEDEN evaluarse como información complementaria.

Su ausencia NO afecta por sí sola a la conformidad.

## 21.4 Availability vs Conformance

La clasificación de implementación de un Framework Component y la conformidad del consumer son dimensiones independientes.

~~~text
Component availability
        ≠
Consumer conformance
~~~

Ejemplo validado mediante dogfooding:

~~~text
README-LICENSE

Framework Component
    → Conceptual

Consumer responsibility
    → Satisfied

Consumer conformance
    → Conforme
~~~

Por tanto, un Component `Conceptual` NO implica automáticamente un consumer gap.

Del mismo modo, la existencia de un Component `Implemented` NO garantiza que el consumer satisfaga correctamente su responsabilidad.

## 21.5 Evidencia

Una evaluación de conformidad DEBERÍA identificar evidencia suficiente para cada responsabilidad relevante.

Ejemplos:

~~~text
README.md
LICENSE
CHANGELOG.md
ROADMAP.md
docs/governance/...
docs/architecture/...
~~~

Cuando la satisfacción de una responsabilidad no resulte evidente, la evaluación DEBERÍA documentar la equivalencia o especialización utilizada.

---

# 22. Reference Implementations

Una Reference Implementation es una implementación real utilizada para validar un Repository Template frente a un caso de uso representativo.

Su función principal es proporcionar evidencia.

~~~text
Repository Template
        ↓
Reference Implementation
        ↓
Evidence
        ↓
Findings
        ↓
Framework refinement
~~~

Una Reference Implementation NO DEBE tratarse como una copia perfecta o normativa del Template.

Su propósito es demostrar:

- qué responsabilidades funcionan;
- qué responsabilidades necesitan especialización;
- qué elementos pueden omitirse;
- qué gaps existen;
- qué reglas necesitan refinamiento;
- qué assumptions arquitectónicas sobreviven al uso real.

## 22.1 Selección

La Reference Implementation DEBERÍA representar un caso de uso realista para la familia del Template.

DEBERÍA evitarse una implementación artificial creada únicamente para conseguir que todos los Quality Gates aparezcan como superados.

Cuando sea posible, DEBERÍA utilizarse un repositorio real.

## 22.2 Evidencia

La Reference Implementation DEBERÍA registrar:

- Template evaluado;
- consumer utilizado;
- responsabilidades `required`;
- responsabilidades `recommended`;
- responsabilidades `optional` cuando aporten información;
- evidencia encontrada;
- gaps;
- decisiones;
- findings;
- resultado de conformidad.

## 22.3 Findings

Los findings obtenidos mediante una Reference Implementation PUEDEN producir cambios en:

- Repository Template Architecture;
- Component Catalog;
- Framework Components;
- composición del Template;
- requirement levels;
- Repository Template Standards;
- documentación de gobierno.

Un finding NO DEBE provocar automáticamente una modificación.

Primero deberá determinarse si representa:

~~~text
Consumer gap
Template gap
Component gap
Architecture gap
Documentation drift
Expected specialization
~~~

La clasificación ayuda a evitar correcciones en la capa equivocada.

---

# 23. Dogfooding

GitHub Framework DEBERÍA validar sus propias abstracciones mediante dogfooding siempre que exista un caso de uso representativo dentro del propio proyecto.

El dogfooding consiste en utilizar el Framework como consumer de sus propias reglas, Components o Templates.

~~~text
GitHub Framework
      ↓
uses GitHub Framework
      ↓
detects real gaps
      ↓
improves GitHub Framework
~~~

El dogfooding NO DEBE utilizarse únicamente para demostrar que el diseño existente es correcto.

DEBE permitir descubrir contradicciones, gaps y necesidades de refinamiento.

## 23.1 Objetivos

El dogfooding DEBERÍA permitir comprobar:

- materialización real del contrato;
- claridad de las responsabilidades;
- utilidad de los requirement levels;
- suficiencia de la metadata;
- coherencia entre arquitectura e implementación;
- existencia de duplicaciones;
- aparición de estructuras innecesarias;
- gaps de documentación;
- mantenibilidad.

## 23.2 Tratamiento de gaps

Los gaps detectados DEBEN analizarse antes de corregirse.

~~~text
Observed gap
      ↓
Classify
      ↓
 ┌────────┬────────┬─────────┬──────────────┐
 │        │        │         │              │
Consumer Template Component Architecture  Drift
 │        │        │         │              │
 ↓        ↓        ↓         ↓              ↓
Fix      Refine   Evolve    Reconsider    Synchronize
consumer contract component model        documentation
~~~

NO DEBE modificarse automáticamente el Template para hacer desaparecer un consumer gap.

Tampoco DEBE implementarse automáticamente un Component conceptual únicamente porque aparezca referenciado por un Template.

## 23.3 Validación iterativa

El dogfooding PUEDE producir ciclos iterativos.

~~~text
Architecture
      ↓
Template
      ↓
Implementation
      ↓
Dogfooding
      ↓
Findings
      ↓
Refinement
      └──────────→ Architecture
~~~

Estos ciclos son una forma válida de evolución del Framework siempre que los cambios resultantes permanezcan documentados y gobernados.

## 23.4 Evidencia validada

Los patrones observados repetidamente y confirmados mediante dogfooding PUEDEN convertirse en estándares normativos.

~~~text
Observed pattern
      ↓
Validated pattern
      ↓
Reusable rule
      ↓
Standard
~~~

Una posibilidad no observada o puramente hipotética NO DEBERÍA convertirse en una regla normativa sin evidencia adicional.

---

# 24. Quality Gates

Todo Repository Template DEBERÍA evaluarse mediante Quality Gates antes de considerarse suficientemente validado para su uso estable.

Los Quality Gates proporcionan controles verificables sobre el contrato, implementación, mantenimiento y validación del Template.

~~~text
Repository Template
        ↓
Quality Gates
        ↓
Validation Evidence
        ↓
Lifecycle Decision
~~~

Los Quality Gates NO sustituyen la evaluación arquitectónica.

Su función es detectar inconsistencias y proporcionar evidencia para decidir si el Template puede avanzar dentro de su lifecycle.

## 24.1 Identity Gate

El Template DEBE:

- disponer de un ID canónico único;
- utilizar el prefijo `TPL-`;
- disponer de un nombre coherente con su propósito;
- representar una categoría reutilizable de repositorio;
- declarar su familia;
- declarar su versión;
- declarar su status;
- declarar su maturity.

Resultado esperado:

~~~text
Identity → Valid
~~~

## 24.2 Structure Gate

La implementación mínima DEBE contener:

~~~text
README.md
metadata.yml
~~~

La presencia de:

~~~text
template/
~~~

es opcional y solo DEBERÍA existir cuando haya materialización física reutilizable que lo justifique.

El Template NO DEBE contener estructuras vacías creadas únicamente por simetría.

Resultado esperado:

~~~text
Structure → Valid
~~~

## 24.3 Metadata Gate

`metadata.yml` DEBE:

- ser sintácticamente válido;
- contener los campos mínimos establecidos por estos estándares;
- utilizar IDs reconocidos;
- declarar los Components por requirement level;
- evitar Components duplicados entre niveles;
- permanecer semánticamente sincronizado con el README.

Resultado esperado:

~~~text
Metadata → Valid
~~~

## 24.4 Composition Gate

La composición DEBE:

- utilizar Framework Components reconocidos;
- asignar cada Component a un único requirement level;
- responder al propósito del Template;
- evitar duplicación innecesaria de responsabilidades;
- respetar dependencias relevantes;
- distinguir entre composición y disponibilidad material.

Un Component `Conceptual` PUEDE formar parte de una composición válida.

Resultado esperado:

~~~text
Composition → Valid
~~~

## 24.5 Required Responsibilities Gate

Todas las responsabilidades `required` DEBEN estar claramente identificadas.

Antes de considerar el Template suficientemente validado, DEBE demostrarse que dichas responsabilidades pueden satisfacerse en un consumer representativo.

~~~text
Required responsibilities
          ↓
Satisfiable
          ↓
Gate passed
~~~

La satisfacción NO exige necesariamente que todos los Framework Components correspondientes estén clasificados como `Implemented`.

El Gate evalúa el contrato del Template, no únicamente la disponibilidad de implementaciones reutilizables.

## 24.6 Availability Transparency Gate

El Template NO DEBE presentar Components `Conceptual` como materialmente disponibles.

Cuando existan Components conceptuales en la composición, su situación DEBERÍA ser comprensible para maintainers y adopters.

~~~text
Conceptual
    ≠
Implemented
~~~

La transparencia sobre disponibilidad NO DEBE alterar artificialmente los requirement levels.

## 24.7 Consistency Gate

Los artefactos del Template DEBEN permanecer semánticamente consistentes.

Como mínimo, DEBE comprobarse coherencia entre:

~~~text
README.md
metadata.yml
Component Catalog
Repository Template Architecture
Repository Template Standards
~~~

Las inconsistencias relevantes DEBEN resolverse o documentarse antes de una promoción de lifecycle.

## 24.8 Conformance Gate

El Template DEBERÍA disponer de evidencia de que un consumer representativo puede satisfacer su contrato.

La evaluación DEBE distinguir:

~~~text
Component availability
        ≠
Consumer conformance
~~~

Para superar este Gate, todas las responsabilidades `required` aplicables DEBEN estar satisfechas por el consumer evaluado.

## 24.9 Dogfooding / Reference Implementation Gate

Antes de evolucionar a `Stable`, un Template DEBE disponer de evidencia obtenida mediante al menos uno de los mecanismos:

- Reference Implementation;
- dogfooding;
- implementación real;
- instanciación representativa;
- adopción real equivalente.

La validación DEBERÍA haber permitido detectar y clasificar gaps reales.

Un Template NO DEBERÍA promocionarse a `Stable` únicamente porque su documentación parezca completa.

## 24.10 Maintenance Gate

El Template DEBE disponer de una base suficientemente mantenible.

DEBERÍA comprobarse:

- ausencia de duplicaciones innecesarias;
- ausencia de estructuras especulativas;
- claridad de las fuentes canónicas;
- capacidad de sincronización con el Component Catalog;
- versionado coherente;
- lifecycle explícito;
- trazabilidad de decisiones relevantes.

## 24.11 Stable Promotion Gate

La promoción:

~~~text
Experimental
     ↓
Stable
~~~

DEBE producirse únicamente cuando los Quality Gates aplicables hayan sido evaluados y no existan gaps críticos sin resolver o explícitamente aceptados.

La promoción NO DEBE utilizarse como mecanismo para declarar finalizado un Sprint o alcanzar artificialmente una milestone.

`Stable` representa estabilidad del contrato y evidencia suficiente de reutilización.

---

# 25. Validation Checklist

La siguiente checklist proporciona una referencia operativa para revisar un Repository Template.

No sustituye los Quality Gates ni la evaluación arquitectónica.

## 25.1 Identity

- [ ] ID canónico definido.
- [ ] Prefijo `TPL-` utilizado.
- [ ] Nombre coherente con el propósito.
- [ ] Categoría reutilizable de repositorio.
- [ ] `family` declarada.
- [ ] `version` declarada.
- [ ] `status` declarado.
- [ ] `maturity` declarada.

## 25.2 Structure

- [ ] `README.md` presente.
- [ ] `metadata.yml` presente.
- [ ] No existen directorios vacíos por convención.
- [ ] `template/` existe únicamente si hay materialización física que lo justifique.
- [ ] Los nombres respetan las convenciones del Framework.

## 25.3 Metadata

- [ ] Metadata sintácticamente válida.
- [ ] Campos mínimos presentes.
- [ ] `components.required` definido.
- [ ] `components.recommended` definido.
- [ ] `components.optional` definido.
- [ ] No existen Components duplicados entre requirement levels.
- [ ] Los IDs referenciados son responsabilidades reconocidas.
- [ ] Metadata y README están sincronizados.

## 25.4 Composition

- [ ] La composición responde al propósito del Template.
- [ ] Los requirement levels son contextuales al Template.
- [ ] Component priority y Template requirement level no se confunden.
- [ ] Los Components `Conceptual` están correctamente identificados.
- [ ] Las dependencias relevantes han sido evaluadas.
- [ ] No existe duplicación innecesaria de especificaciones de Components.

## 25.5 Materialization

- [ ] No existen archivos placeholder sin utilidad.
- [ ] No existen estructuras especulativas.
- [ ] Los placeholders necesarios son claros.
- [ ] La materialización física responde a necesidades reutilizables.
- [ ] Las implementaciones equivalentes pueden identificarse cuando corresponda.

## 25.6 Conformance

- [ ] Todas las responsabilidades `required` pueden evaluarse.
- [ ] Todas las responsabilidades `required` aplicables están satisfechas en el consumer de referencia.
- [ ] Las responsabilidades `recommended` han sido evaluadas.
- [ ] Las omisiones relevantes están justificadas.
- [ ] Availability y conformance se evalúan como dimensiones independientes.
- [ ] Existe evidencia suficiente para las decisiones de conformidad.

## 25.7 Validation

- [ ] Existe Reference Implementation, dogfooding o evidencia equivalente cuando resulte necesaria.
- [ ] Los consumer gaps han sido identificados.
- [ ] Los Template gaps han sido identificados.
- [ ] Los Component gaps han sido identificados cuando corresponda.
- [ ] Los architecture gaps han sido identificados cuando corresponda.
- [ ] Los findings relevantes han sido documentados.
- [ ] Los gaps críticos han sido resueltos o aceptados explícitamente.

## 25.8 Maintenance

- [ ] Versionado coherente.
- [ ] Lifecycle explícito.
- [ ] Documentación sincronizada.
- [ ] Component Catalog revisado cuando corresponda.
- [ ] Fuentes canónicas identificables.
- [ ] No existe drift conocido relevante.

---

# 26. Anti-patterns

Los siguientes patrones DEBEN evitarse al diseñar o mantener Repository Templates.

## 26.1 Template por tecnología sin necesidad validada

~~~text
TPL-SPRING-BOOT
TPL-DJANGO
TPL-FASTAPI
~~~

NO DEBERÍAN crearse únicamente porque dichas tecnologías existan.

Una especialización tecnológica solo debería formalizarse como Template independiente cuando represente un contrato reutilizable suficientemente distinto y validado.

## 26.2 Template por maturity

~~~text
TPL-BACKEND-L1
TPL-BACKEND-L2
TPL-BACKEND-L3
~~~

La maturity es una propiedad y NO DEBE utilizarse para multiplicar identidades de Templates sin una diferencia contractual real.

## 26.3 Simetría artificial

No debe forzarse:

~~~text
backend/template/
fullstack/template/
documentation/template/
~~~

si alguno de esos directorios no contiene materialización reutilizable real.

La consistencia conceptual tiene prioridad sobre la simetría visual del filesystem.

## 26.4 Empty Placeholder Architecture

NO DEBEN crearse archivos únicamente para aparentar que una responsabilidad está implementada.

Ejemplo:

~~~text
SECURITY.md
    ↓
"TODO"
~~~

Esto no constituye satisfacción válida de una responsabilidad.

## 26.5 Required by Availability

Un Component NO DEBE clasificarse como `required` únicamente porque ya esté `Implemented`.

~~~text
Implemented
    ≠
Required
~~~

El requirement level debe derivarse del contrato del Template.

## 26.6 Optional by Unavailability

Un Component NO DEBE degradarse automáticamente a `optional` únicamente porque permanezca `Conceptual`.

~~~text
Conceptual
    ≠
Optional
~~~

La ausencia de implementación canónica no redefine la importancia de la responsabilidad.

## 26.7 Conformance by File Matching

NO DEBE declararse conformidad únicamente porque el consumer contenga archivos con nombres esperados.

~~~text
Expected filename exists
        ≠
Responsibility satisfied
~~~

Debe evaluarse el contenido y la responsabilidad efectiva.

## 26.8 Non-conformance by Structural Difference

Una diferencia física respecto a un ejemplo o materialización canónica NO implica automáticamente no conformidad.

Una implementación equivalente PUEDE satisfacer correctamente el contrato.

## 26.9 Copying Component Specifications

Un Repository Template NO DEBE mantener copias completas y divergentes de especificaciones canónicas de Framework Components.

~~~text
Component specification
      ↓
single canonical source
~~~

El Template debe referenciar, componer y especializar, no bifurcar innecesariamente.

## 26.10 Premature Automation

NO DEBERÍAN formalizarse sistemas de:

- generación;
- inheritance;
- resolución automática;
- schemas complejos;
- migración;

antes de disponer de patrones y necesidades validadas que justifiquen su arquitectura.

## 26.11 Closing Gaps by Changing the Contract

Un gap detectado durante dogfooding NO DEBE resolverse automáticamente relajando el contrato del Template.

~~~text
Gap
 ↓
Analyze
 ↓
Decide
~~~

Modificar `required → optional` únicamente para conseguir conformidad constituye un anti-pattern si no existe evidencia que justifique el cambio contractual.

## 26.12 Catalog Drift

Un Template NO DEBE mantener afirmaciones sobre disponibilidad de Components que contradigan sus fuentes canónicas.

La información derivada DEBERÍA revisarse cuando evolucione el Component Catalog o la implementación física del Framework.

---

# 27. Evolution Rules

Los Repository Templates DEBEN evolucionar mediante cambios controlados y respaldados por evidencia.

~~~text
Evidence
   ↓
Finding
   ↓
Evaluation
   ↓
Decision
   ↓
Evolution
~~~

## 27.1 Sources of Evolution

La evolución PUEDE originarse en:

- Reference Implementations;
- dogfooding;
- adopción por repositorios reales;
- cambios en Framework Components;
- nuevos requisitos recurrentes;
- gaps observados;
- mantenimiento;
- cambios arquitectónicos previamente aprobados.

Una posibilidad hipotética NO DEBERÍA ser suficiente por sí sola para modificar el contrato.

## 27.2 Classification Before Modification

Antes de modificar un Template debido a un problema observado, DEBERÍA clasificarse el finding.

~~~text
Consumer gap
Template gap
Component gap
Architecture gap
Documentation drift
Expected specialization
~~~

La modificación DEBE realizarse en la capa responsable del problema.

Ejemplos:

~~~text
Consumer content outdated
        ↓
Fix consumer

Wrong requirement level
        ↓
Fix Template

Missing reusable responsibility
        ↓
Evaluate Component

Incorrect model assumption
        ↓
Review Architecture
~~~

## 27.3 Requirement Level Changes

Un cambio entre:

~~~text
required
recommended
optional
~~~

DEBE justificarse mediante evidencia suficiente.

Especialmente, los cambios hacia o desde `required` DEBEN analizar su impacto sobre consumidores existentes.

La disponibilidad material de un Component NO constituye por sí sola evidencia suficiente para modificar su requirement level.

## 27.4 New Components

Un Repository Template PUEDE revelar la necesidad de un nuevo Framework Component.

El nuevo Component NO DEBE crearse automáticamente.

Primero DEBERÍA comprobarse que la responsabilidad:

- es reutilizable;
- tiene límites identificables;
- no duplica otro Component;
- aparece en un contexto real;
- merece una implementación canónica independiente.

## 27.5 New Repository Templates

Un nuevo Repository Template DEBERÍA crearse únicamente cuando exista una categoría de repositorio con un contrato reutilizable suficientemente distinto de los Templates existentes.

Antes de crear uno nuevo, DEBERÍA evaluarse si la necesidad puede resolverse mediante:

- especialización;
- extensión;
- Components adicionales;
- configuración contextual de un Template existente.

~~~text
New use case
     ↓
Existing Template sufficient?
   ┌────┴────┐
  yes        no
   ↓          ↓
extend      evaluate
existing    new Template
~~~

## 27.6 Backward Compatibility

Los cambios compatibles DEBERÍAN preservar la conformidad de consumers existentes siempre que resulte razonable.

Los cambios incompatibles DEBEN reflejarse mediante versionado adecuado.

Una evolución del Framework NO DEBE asumir automáticamente que todos los consumers pueden migrar de forma inmediata.

## 27.7 Deprecation

Cuando un Template deje de ser recomendable, DEBERÍA preferirse una transición explícita a `Deprecated` frente a su eliminación inmediata.

La deprecación DEBE preservar suficiente información para comprender:

- qué contrato representaba;
- por qué fue sustituido;
- qué alternativa existe;
- cómo afecta a consumers existentes.

## 27.8 Standards Evolution

Estos Repository Template Standards también DEBEN evolucionar a partir de evidencia.

Una regla nueva DEBERÍA incorporarse cuando:

~~~text
Observed behavior
        ↓
Repeated or significant evidence
        ↓
Validated pattern
        ↓
Normative rule
~~~

Los estándares NO DEBERÍAN convertirse en un catálogo de escenarios hipotéticos.

---

# 28. Summary

Los Repository Template Standards establecen las reglas prácticas para crear y mantener Repository Templates coherentes dentro de GitHub Framework.

El modelo puede resumirse como:

~~~text
Repository Template
        │
        ├── Identity
        ├── Metadata
        ├── Component Composition
        │       ├── required
        │       ├── recommended
        │       └── optional
        │
        ├── Maturity
        ├── Version
        ├── Lifecycle
        └── Quality Gates
                ↓
        Reference Implementation
                ↓
            Dogfooding
                ↓
             Findings
                ↓
             Evolution
~~~

Las distinciones fundamentales son:

~~~text
Component priority
        ≠
Template requirement level

Component availability
        ≠
Consumer conformance

Template maturity
        ≠
Template lifecycle status

Template contract
        ≠
Physical materialization

Structural difference
        ≠
Non-conformance
~~~

Un Repository Template define responsabilidades reutilizables para una categoría de repositorio.

Los Framework Components proporcionan implementaciones reutilizables de responsabilidades reconocidas.

Los repositorios consumidores satisfacen esas responsabilidades mediante implementaciones canónicas, propias, especializadas o equivalentes.

La conformidad se evalúa sobre las responsabilidades satisfechas.

La estabilidad se obtiene mediante evidencia.

~~~text
Architecture
      ↓
Implementation
      ↓
Validation
      ↓
Dogfooding
      ↓
Evidence
      ↓
Standards
      ↓
Evolution
~~~

GitHub Framework DEBE continuar priorizando patrones demostrados sobre abstracciones hipotéticas.

---

# Revision History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-08-18 | Primera versión de Repository Template Standards basada en Repository Template Architecture, Core Repository Templates y findings de la Reference Implementation |
