# TPL-DOCUMENTATION — Documentation Repository

## 1. Propósito

`TPL-DOCUMENTATION` define una composición reutilizable para repositorios cuyo producto principal es documentación técnica, conocimiento estructurado, estándares, especificaciones o guías.

Su objetivo es proporcionar una base coherente para proyectos donde la documentación no constituye únicamente soporte para otro producto, sino que representa una parte principal del valor entregado por el repositorio.

---

## 2. Cuándo Utilizarlo

Se recomienda utilizar este Template para repositorios como:

- knowledge bases;
- technical handbooks;
- estándares y especificaciones;
- frameworks documentales;
- guías técnicas;
- documentación de arquitectura;
- documentación mantenida como producto.

El Template es independiente de la herramienta utilizada para publicar o visualizar la documentación.

---

## 3. Cuándo No Utilizarlo

No debe utilizarse cuando:

- la documentación sea únicamente soporte de una aplicación backend;
- la documentación sea únicamente soporte de una aplicación Full Stack;
- el producto principal sea software ejecutable;
- unas pocas páginas Markdown sean suficientes y no exista una estructura documental mantenida;
- el repositorio exista únicamente para publicar documentación generada automáticamente desde otro proyecto.

En esos casos deberán utilizarse los Components documentales necesarios dentro del Template correspondiente.

---

## 4. Responsabilidad

`TPL-DOCUMENTATION` responde principalmente a la pregunta:

> ¿Qué composición de GitHub Framework Components permite mantener de forma coherente un repositorio cuyo producto principal es documentación?

No define:

- generador de documentación;
- plataforma de publicación;
- hosting;
- formato editorial concreto;
- taxonomía universal de contenidos;
- sistema de navegación específico.

Estas decisiones pertenecen al proyecto concreto o a Components especializados.

---

## 5. Documentation as Product

La característica fundamental de este Template es:

```text
Documentation
      ↓
Primary Product
```

Esto lo diferencia de otros Repository Templates, donde la documentación acompaña a un producto software.

En `TPL-DOCUMENTATION`, aspectos como:

- arquitectura documental;
- estado;
- evolución;
- referencias;

forman parte central de la composición.

---

## 6. Maturity

Nivel mínimo recomendado:

```text
L2
```

El Template está orientado a repositorios documentales mantenidos y con una estructura suficientemente estable.

Repositorios experimentales o colecciones pequeñas de notas podrán utilizar una composición más reducida.

---

## 7. Required Components

Los siguientes Components forman parte del contrato mínimo:

```text
README-HERO
README-OVERVIEW
README-DOCUMENTATION
README-FOOTER

DOC-ARCHITECTURE
DOC-PROJECT-STATUS
DOC-CHANGELOG
DOC-REFERENCES
```

Estos Components permiten:

- identificar el proyecto;
- explicar su propósito;
- proporcionar acceso al contenido documental;
- describir su organización;
- comunicar su estado;
- registrar su evolución;
- mantener las referencias relevantes.

`DOC-REFERENCES` es `required` en este Template porque las fuentes, estándares, especificaciones y documentación relacionada pueden formar parte estructural del conocimiento mantenido.

---

## 8. Recommended Components

La composición habitual recomienda:

```text
README-ROADMAP
README-REPOSITORY-STRUCTURE

DOC-ADR
DOC-ROADMAP
DOC-GLOSSARY
DOC-DIAGRAMS
```

Estos Components resultan especialmente útiles cuando el repositorio:

- evoluciona mediante decisiones explícitas;
- contiene terminología propia;
- mantiene una planificación;
- utiliza representaciones visuales;
- dispone de una estructura documental amplia.

Podrán omitirse cuando no aporten valor suficiente.

---

## 9. Optional Components

Los siguientes Components pueden incorporarse según las necesidades del proyecto:

```text
README-CONTRIBUTING
README-AUTHOR
README-HIGHLIGHTS
README-LICENSE

DOC-TESTING
DOC-SECURITY
```

Por ejemplo:

- `README-CONTRIBUTING` cuando exista colaboración externa;
- `DOC-TESTING` cuando la documentación disponga de validaciones automáticas;
- `DOC-SECURITY` cuando el contenido o su proceso de mantenimiento tenga requisitos específicos de seguridad.

---

## 10. Component Priority vs Template Requirement

La prioridad global definida en el Component Catalog no determina automáticamente el requirement level dentro de este Template.

```text
Component Catalog
        ↓
prioridad general

TPL-DOCUMENTATION
        ↓
necesidad dentro de esta composición
```

Por ejemplo, `DOC-REFERENCES` puede ser globalmente `Recommended` y formar parte de los elementos `required` de `TPL-DOCUMENTATION`.

Esto permite adaptar los Components al contexto sin modificar su definición canónica.

---

## 11. Arquitectura Documental

Un repositorio documental mantenido deberá disponer de una organización comprensible.

Conceptualmente:

```text
Repository
    │
    ├── Entry Point
    │
    ├── Documentation Structure
    │
    ├── Governance / Status
    │
    └── References
```

El Template no prescribe una taxonomía concreta.

La arquitectura deberá responder a las necesidades reales del dominio documental.

---

## 12. Estructura Específica

`TPL-DOCUMENTATION` no impone inicialmente una estructura física obligatoria.

Una implementación podrá utilizar:

```text
docs/
```

o:

```text
content/
```

o cualquier estructura coherente con sus necesidades.

El Template tampoco prescribe herramientas como:

```text
MkDocs
Docusaurus
GitBook
GitHub Pages
```

Por esta razón, la versión inicial no requiere un directorio `template/`.

Su valor principal reside en:

```text
composition
+
documentation architecture
+
governance
+
guidance
```

---

## 13. Placeholders

Los placeholders mínimos previstos son:

```text
<PROJECT_NAME>
<PROJECT_DESCRIPTION>
<OWNER>
```

Podrán aparecer posteriormente placeholders relacionados con la estructura documental cuando una implementación real demuestre su necesidad.

No deberán añadirse de forma especulativa.

---

## 14. Personalización

Una implementación podrá:

- añadir Components opcionales;
- omitir Components recomendados;
- incorporar documentación especializada;
- establecer su propia taxonomía;
- utilizar herramientas de publicación;
- incorporar automatización;
- añadir mecanismos propios de validación.

Deberá conservar los Components `required` para considerarse una implementación completa de `TPL-DOCUMENTATION`.

---

## 15. Neutralidad Tecnológica

`TPL-DOCUMENTATION` no prescribe:

```text
Markdown
MkDocs
Docusaurus
GitBook
GitHub Pages
Sphinx
```

Markdown puede utilizarse como formato dentro del propio GitHub Framework, pero no constituye una dependencia conceptual del Repository Template.

El Template describe una composición documental.

No una herramienta de publicación.

---

## 16. Quality Gates

Antes de considerar válida una implementación:

- [ ] La documentación representa un producto principal del repositorio.
- [ ] Los Components `required` están presentes.
- [ ] La arquitectura documental resulta comprensible.
- [ ] El punto de entrada permite localizar la documentación principal.
- [ ] El estado y evolución del proyecto están documentados.
- [ ] Las referencias relevantes pueden localizarse.
- [ ] Los Components recomendados omitidos no son necesarios para comprender el repositorio.
- [ ] Los Components opcionales responden a necesidades reales.
- [ ] No se duplican especificaciones canónicas de Components.
- [ ] La estructura física responde al dominio y no a una imposición del Template.
- [ ] El Template permanece independiente de herramientas concretas de publicación.

---

## 17. Estado

`TPL-DOCUMENTATION` se encuentra actualmente en estado `Experimental`.

Su composición deberá validarse mediante una Reference Implementation antes de considerarse `Stable`.