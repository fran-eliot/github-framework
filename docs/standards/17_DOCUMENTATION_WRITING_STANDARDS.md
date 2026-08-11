# 17 - DOCUMENTATION WRITING STANDARDS

| Field        | Value                           |
| ------------ | ------------------------------- |
| **Project**  | GitHub Framework                |
| **Document** | Documentation Writing Standards |
| **Version**  | 1.0.0                           |
| **Status**   | Stable                          |
| **Owner**    | Fran Ramirez                    |

---

# 1. Purpose

Este documento define los estándares oficiales de redacción para la documentación de GitHub Framework.

Su objetivo es garantizar que la documentación sea:

- clara;
- consistente;
- mantenible;
- reutilizable;
- navegable;
- suficientemente precisa sin introducir complejidad innecesaria.

Estos estándares se aplican tanto a la documentación del propio Framework como a los componentes documentales reutilizables que este proporciona.

---

# 2. Documentation Principles

Toda documentación deberá seguir los siguientes principios.

## 2.1 Clarity Before Completeness

La documentación deberá explicar primero lo necesario para comprender y utilizar correctamente el sistema.

No deberá intentar registrar todos los detalles posibles.

---

## 2.2 One Document, One Responsibility

Cada documento deberá tener una responsabilidad principal claramente identificable.

Cuando un contenido pertenezca conceptualmente a otro documento, deberá enlazarse en lugar de duplicarse.

---

## 2.3 Reuse Before Duplication

Antes de crear una nueva estructura documental deberá comprobarse si existe:

- un Documentation Component;
- un patrón existente;
- una plantilla reutilizable;
- un documento que ya actúe como Single Source of Truth.

---

## 2.4 Implementation Before Abstraction

Los patrones documentales reutilizables deberán basarse, siempre que sea posible, en necesidades e implementaciones reales.

No deberán crearse convenciones complejas para escenarios hipotéticos.

---

## 2.5 Documentation Evolves with the Project

La documentación deberá actualizarse cuando cambie materialmente aquello que describe.

No deberá mantenerse información obsoleta únicamente por conservar historial.

El historial pertenece a los mecanismos específicamente destinados a conservarlo.

---

# 3. Language Policy

GitHub Framework utiliza una política lingüística basada en la audiencia y responsabilidad del contenido.

## 3.1 English

Se utilizará inglés para:

- código fuente;
- nombres de archivos;
- nombres de directorios;
- identificadores técnicos;
- IDs de componentes;
- claves de metadata;
- valores canónicos de metadata;
- commits;
- nombres de ramas;
- GitHub repository metadata;
- README público principal;
- contenido público cuya audiencia principal sea internacional.

Ejemplos:

```text
DOC-ARCHITECTURE
project-status/
metadata.yml
Experimental
Recommended
Maintainer
```

---

## 3.2 Spanish

Se utilizará español para:

- documentación de arquitectura;
- documentación de gobierno;
- documentación de diseño;
- documentación de desarrollo;
- especificaciones internas;
- contenido explicativo de los Documentation Components;
- instrucciones incluidas en templates cuando no formen parte del artefacto técnico final.

Los términos técnicos establecidos podrán mantenerse en inglés cuando su traducción reduzca claridad.

---

## 3.3 Bilingual Content

Cuando un documento disponga de versiones inglesa y española:

- ambas deberán mantener la misma estructura;
- ambas deberán comunicar el mismo significado;
- los enlaces deberán mantenerse sincronizados;
- ninguna versión deberá convertirse en una versión simplificada de la otra.

La traducción podrá ser natural y no necesita ser literal.

---

## 3.4 Component Language

En los componentes reutilizables:

```text
Technical identity
→ English

Explanatory documentation
→ Spanish
```

Ejemplo:

```yaml
id: DOC-PROJECT-STATUS
status: Experimental
priority: Required
description: >
  Componente reutilizable para comunicar el estado actual de un proyecto.
```

---

# 4. Writing Style

La redacción deberá ser:

- directa;
- precisa;
- técnica cuando sea necesario;
- comprensible sin conocimiento interno del proyecto;
- libre de lenguaje promocional innecesario.

Se preferirán frases cortas o medias.

Los párrafos deberán desarrollar una sola idea principal.

---

# 5. Terminology

Los términos oficiales del Framework deberán utilizarse de forma consistente.

Ejemplos:

```text
GitHub Framework
Repository Design System
Component Catalog
Documentation Components
Reference Implementation
Quality Gates
dogfooding
```

No deberán alternarse nombres diferentes para el mismo concepto sin una razón explícita.

Los identificadores técnicos nunca deberán traducirse.

---

# 6. Heading Structure

Los encabezados deberán mantener una jerarquía coherente.

Un documento utilizará un único título principal:

```markdown
# Document Title
```

Las secciones principales utilizarán:

```markdown
## Section
```

y las subsecciones:

```markdown
### Subsection
```

Los documentos históricos existentes que utilicen una convención distinta podrán conservarla mientras permanezca consistente internamente.

No deberán saltarse niveles de encabezado sin necesidad.

---

# 7. Lists

Las listas deberán utilizarse cuando faciliten el escaneo o representen elementos equivalentes.

Se utilizarán listas numeradas cuando el orden sea significativo:

```markdown
1. Primer paso.
2. Segundo paso.
3. Tercer paso.
```

Se utilizarán listas no ordenadas cuando el orden no tenga importancia:

```markdown
- Elemento.
- Elemento.
- Elemento.
```

Las listas no deberán utilizarse para fragmentar artificialmente texto que resulte más comprensible como párrafo.

---

# 8. Checklists

Las checklists se reservarán para:

- Definition of Done;
- Quality Gates;
- validaciones;
- procedimientos de revisión.

Formato:

```markdown
- [ ] Criterio pendiente.
- [x] Criterio completado.
```

No deberán utilizarse como sustituto de listas informativas normales.

---

# 9. Tables

Las tablas deberán utilizarse para información estructurada o comparativa.

Son apropiadas para:

- metadata;
- estados;
- matrices;
- componentes;
- relaciones;
- versiones.

No deberán utilizarse como mecanismo general de layout.

Una tabla deberá seguir siendo comprensible en una pantalla razonablemente estrecha.

---

# 10. Code Blocks

Los bloques de código deberán indicar el lenguaje cuando resulte útil.

Ejemplos:

```text
framework/
├── components/
└── templates/
```

```yaml
status: Experimental
```

```bash
git status
```

Para diagramas textuales se utilizará normalmente:

```text
Component A
     ↓
Component B
```

---

# 11. Diagrams

Los diagramas deberán utilizarse únicamente cuando mejoren la comprensión.

Formatos recomendados:

```text
Mermaid
PlantUML
SVG
Text Tree
```

Todo diagrama deberá:

- representar el estado actual;
- ser mantenible;
- tener una responsabilidad clara;
- estar acompañado de contexto textual suficiente.

---

# 12. Links

Los enlaces internos utilizarán rutas relativas siempre que sea posible.

Ejemplo:

```markdown
[Component Catalog](../design-system/09_COMPONENT_CATALOG.md)
```

Los enlaces deberán utilizar texto descriptivo.

Evitar:

```text
click here
link
more
```

Preferir:

```text
Component Catalog
Architecture Documentation
Contribution Guide
```

---

# 13. Single Source of Truth

Cada concepto deberá disponer de una única fuente principal.

Otros documentos deberán:

- resumir;
- contextualizar;
- enlazar.

No deberán reproducir grandes bloques de información mantenidos en otra ubicación.

Ejemplo:

```text
Component Catalog
        ↓
registers component metadata

Component README
        ↓
specifies component behavior

Project Implementation
        ↓
instantiates component
```

Cada nivel tiene una responsabilidad distinta.

---

# 14. Component Documentation

Todo Documentation Component deberá seguir el contrato establecido por la Documentation Component Library:

```text
component/
├── metadata.yml
├── README.md
├── template.md
└── example.md
```

`example.md` será opcional cuando no aporte información adicional relevante.

---

# 15. Component README

El `README.md` de un componente deberá explicar, cuando resulte aplicable:

- propósito;
- cuándo utilizarlo;
- cuándo no utilizarlo;
- responsabilidad;
- estructura;
- reglas de contenido;
- relaciones;
- mantenimiento;
- Quality Gates;
- estado del componente.

No es obligatorio utilizar todas las secciones cuando no aporten valor.

---

# 16. Templates

Los templates deberán representar estructuras reutilizables, no implementaciones concretas.

La información específica del proyecto deberá expresarse mediante placeholders.

Ejemplos:

```text
<PROJECT_NAME>
<CURRENT_VERSION>
<COMPONENT_NAME>
<YYYY-MM-DD>
```

Los placeholders deberán:

- ser identificables;
- tener nombres descriptivos;
- utilizar mayúsculas;
- evitar ambigüedad.

---

# 17. Examples

Un `example.md` solo deberá existir cuando:

- facilite significativamente la comprensión;
- muestre una utilización que el template no explica por sí mismo;
- permita validar una estructura compleja.

No deberá añadirse para cumplir mecánicamente una estructura.

---

# 18. Duplication

Antes de añadir contenido deberá comprobarse:

1. si ya existe en otro documento;
2. cuál es su Single Source of Truth;
3. si basta con resumirlo;
4. si puede enlazarse;
5. si realmente necesita repetirse.

La duplicación deliberada solo será aceptable cuando mejore significativamente la experiencia del lector y su coste de mantenimiento sea bajo.

---

# 19. Document Size

No existe un límite universal de longitud.

La documentación deberá ser tan extensa como requiera su responsabilidad y no más.

Cuando un documento acumule responsabilidades diferentes deberá evaluarse su división.

La longitud por sí sola no justifica dividir un documento.

---

# 20. Maintenance

Todo documento deberá poder responder:

```text
¿Cuándo debe actualizarse?
```

Los triggers de mantenimiento dependerán de su responsabilidad.

Ejemplos:

```text
Architecture
→ cambios arquitectónicos

Project Status
→ cambios significativos de estado

Changelog
→ cambios relevantes publicados o pendientes de publicación

References
→ cambios en las fuentes relevantes
```

---

# 21. Historical Information

La documentación operativa deberá representar principalmente el estado vigente.

El historial deberá mantenerse en los artefactos adecuados:

```text
Git history
CHANGELOG
Release Notes
ADR
Revision History
```

No deberá conservarse contenido obsoleto dentro de una sección activa únicamente por valor histórico.

---

# 22. Quality Gates

Antes de considerar preparada una modificación documental deberá verificarse:

- [ ] La responsabilidad del documento sigue siendo clara.
- [ ] El contenido está actualizado.
- [ ] No existe duplicación innecesaria.
- [ ] La terminología es consistente.
- [ ] La política lingüística se respeta.
- [ ] Los identificadores técnicos no se han traducido.
- [ ] La jerarquía Markdown es coherente.
- [ ] Los enlaces son válidos.
- [ ] Las tablas y listas aportan claridad.
- [ ] Los diagramas representan el estado actual.
- [ ] Los placeholders son comprensibles.
- [ ] La documentación refleja la implementación real.

---

# 23. Anti-Patterns

Deberán evitarse:

- documentación creada sin una necesidad real;
- secciones vacías;
- duplicación entre README y documentación profunda;
- plantillas excesivamente específicas;
- términos diferentes para el mismo concepto;
- mezcla arbitraria de idiomas;
- enlaces sin contexto;
- diagramas obsoletos;
- ejemplos que no representan el template;
- documentación que describe una intención futura como si estuviera implementada;
- estructuras complejas para problemas simples.

---

# 24. Evolution

Estos estándares evolucionarán únicamente cuando la implementación real demuestre una necesidad no cubierta.

Los cambios deberán:

- resolver un problema repetido;
- mantener simplicidad;
- evitar excepciones específicas de un único proyecto;
- conservar compatibilidad razonable con la documentación existente.

---

# 25. Revision History

| Version | Date       | Description |
| ------- | ---------- | ----------- |
| 1.0.0   | 2026-08-11 | Primera versión de los Documentation Writing Standards. |