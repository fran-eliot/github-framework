# TPL-FULLSTACK — Full Stack Repository

## 1. Propósito

`TPL-FULLSTACK` define una composición reutilizable para repositorios que integran una aplicación frontend y una aplicación backend dentro de una misma unidad de proyecto.

Su objetivo es proporcionar una base común para proyectos donde ambas partes evolucionan de forma coordinada y mantienen una relación arquitectónica explícita.

El Template no prescribe tecnologías concretas ni una estructura física única.

---

## 2. Cuándo Utilizarlo

Se recomienda utilizar este Template cuando:

- frontend y backend forman parte del mismo producto;
- ambas aplicaciones se mantienen dentro del mismo repositorio;
- existe integración directa entre ellas;
- comparten ciclo de desarrollo o release;
- resulta necesario documentar sus límites y relaciones.

Ejemplos posibles:

```text
Angular + Spring Boot
React + FastAPI
Vue + NestJS
```

Las tecnologías utilizadas no forman parte del contrato del Template.

---

## 3. Cuándo No Utilizarlo

No debe utilizarse cuando:

- frontend y backend viven en repositorios completamente independientes;
- el proyecto contiene únicamente backend;
- el producto principal es documentación;
- una de las dos capas representa únicamente un ejemplo o demo auxiliar;
- no existe una relación arquitectónica relevante entre frontend y backend.

---

## 4. Responsabilidad

`TPL-FULLSTACK` responde principalmente a la pregunta:

> ¿Qué composición de GitHub Framework Components permite mantener de forma coherente un repositorio que integra frontend y backend?

No define:

- framework frontend;
- framework backend;
- lenguaje;
- base de datos;
- mecanismo de autenticación;
- infraestructura;
- estrategia concreta de despliegue.

Estas decisiones pertenecen al proyecto concreto o a Components especializados.

---

## 5. Maturity

Nivel mínimo recomendado:

```text
L2
```

El Template está orientado inicialmente a repositorios públicos mantenidos.

Repositorios experimentales podrán utilizar una composición más reducida.

---

## 6. Required Components

Los siguientes Components forman parte del contrato mínimo:

```text
README-HERO
README-OVERVIEW
README-FEATURES
README-TECH-STACK
README-QUICK-START
README-DOCUMENTATION
README-FOOTER
DOC-ARCHITECTURE
DOC-CHANGELOG
```

`DOC-ARCHITECTURE` es `required` porque la relación entre frontend y backend forma parte de la responsabilidad central del Template.

La arquitectura deberá permitir comprender:

```text
Frontend
    │
    ▼
Integration Boundary
    │
    ▼
Backend
```

sin imponer un patrón tecnológico concreto.

---

## 7. Recommended Components

La composición habitual recomienda:

```text
README-STATUS
README-ARCHITECTURE
README-REPOSITORY-STRUCTURE
README-TESTING

DOC-PROJECT-STATUS
DOC-TESTING
DOC-DEPLOYMENT
DOC-DIAGRAMS
```

Estos Components aportan visibilidad sobre:

- estado del proyecto;
- estructura global;
- estrategia de testing;
- despliegue;
- relaciones arquitectónicas.

Podrán omitirse cuando la complejidad del proyecto no justifique su incorporación.

---

## 8. Optional Components

Los siguientes Components pueden incorporarse cuando exista una necesidad concreta:

```text
README-ROADMAP
README-CONTRIBUTING
README-DEMO
README-AUTHOR
README-HIGHLIGHTS
README-LICENSE

DOC-ADR
DOC-API
DOC-DATABASE
DOC-SECURITY
DOC-REFERENCES
```

Por ejemplo:

- `DOC-API` cuando el contrato entre frontend y backend necesite documentación específica;
- `DOC-DATABASE` cuando exista un modelo de datos relevante;
- `DOC-SECURITY` cuando autenticación, autorización u otros aspectos requieran documentación propia;
- `README-DEMO` cuando la interfaz permita mostrar claramente el producto funcionando.

---

### Disponibilidad de Components

Todos los Components `required` declarados por `TPL-FULLSTACK` disponen actualmente de implementación canónica en el Framework.

Por tanto, el contrato mínimo del Template puede materializarse con los Components disponibles en la versión actual.

Los niveles `recommended` y `optional` incluyen tanto Components implementados como responsabilidades conceptuales todavía no materializadas.

La disponibilidad actual puede resumirse como:

```text
Required       9/9  Implemented
Recommended    4/8  Implemented
Optional       3/11 Implemented
Total         16/28 Implemented
```

Los Components todavía no implementados permanecen válidos como parte de la composición conceptual del Template, pero no deberán interpretarse como disponibles materialmente hasta disponer de implementación canónica.

La clasificación `Conceptual` no modifica su requirement level dentro del Template:

```text
Implementation classification
≠
Template requirement level
```

La evolución de estos Components deberá seguir el lifecycle y las reglas de materialización definidos por GitHub Framework.

---

## 9. Component Priority vs Template Requirement

La prioridad definida en la metadata canónica de un Component y su requirement level dentro de este Template representan conceptos diferentes.

```text
Component Metadata
      ↓
priority orientativa del Component

Repository Template
      ↓
requirement level contextual
```

Por tanto:

```text
Component priority
≠
Template requirement level
```

Un Component con `priority: Required` puede ser `recommended`, `optional` o no formar parte de una composición concreta.

---

## 10. Límites Arquitectónicos

El Template asume la existencia conceptual de dos grandes responsabilidades:

```text
Frontend Application Boundary
            │
            ▼
    Integration Boundary
            │
            ▼
Backend Application Boundary
```

No impone cómo deben representarse físicamente.

Una implementación podrá utilizar:

```text
frontend/
backend/
```

o:

```text
client/
server/
```

o:

```text
apps/web/
apps/api/
```

La nomenclatura pertenece al proyecto concreto.

---

## 11. Estructura Específica

`TPL-FULLSTACK` no define inicialmente una estructura física obligatoria.

La existencia de frontend y backend es arquitectónicamente relevante.

Los nombres concretos de carpetas y la organización interna dependen del ecosistema tecnológico.

Por esta razón, la versión inicial no requiere un directorio `template/`.

El valor principal del Template reside en:

```text
composition
+
architectural boundaries
+
guidance
```

---

## 12. Placeholders

Los placeholders mínimos previstos son:

```text
<PROJECT_NAME>
<PROJECT_DESCRIPTION>
<OWNER>
```

No se incorporarán placeholders específicos de frontend o backend hasta que una implementación real los necesite.

---

## 13. Integración Frontend / Backend

La implementación deberá documentar suficientemente la relación entre ambas partes.

Puede incluir:

- mecanismo de comunicación;
- contrato API;
- autenticación;
- configuración compartida;
- versionado;
- despliegue coordinado;
- dependencias relevantes.

El nivel de detalle dependerá del proyecto.

Los detalles especializados deberán delegarse a Components cuando exista uno apropiado.

---

## 14. Personalización

Una implementación podrá:

- añadir Components opcionales;
- omitir Components recomendados;
- elegir cualquier stack frontend;
- elegir cualquier stack backend;
- organizar físicamente las aplicaciones según sus necesidades;
- incorporar tooling específico;
- añadir documentación especializada.

Deberá conservar los Components `required` y unos límites conceptuales comprensibles entre frontend, integración y backend para considerarse una implementación completa de `TPL-FULLSTACK`.

---

## 15. Neutralidad Tecnológica

`TPL-FULLSTACK` no prescribe:

```text
Angular
React
Vue
Spring Boot
Django
FastAPI
NestJS
PostgreSQL
Docker
Kubernetes
```

El Template representa una composición arquitectónica.

No una combinación de tecnologías.

---

## 16. Quality Gates

Antes de considerar válida una implementación:

- [ ] El proyecto contiene realmente frontend y backend.
- [ ] Ambas partes forman una unidad de proyecto coherente.
- [ ] Los Components `required` están presentes.
- [ ] La relación frontend/backend está documentada.
- [ ] Los límites arquitectónicos resultan comprensibles.
- [ ] Los Components recomendados omitidos no son necesarios para comprender el sistema.
- [ ] Los Components opcionales responden a necesidades reales.
- [ ] No se duplican especificaciones canónicas de Components.
- [ ] La estructura física no se confunde con el contrato conceptual del Template.
- [ ] La composición sigue siendo independiente del stack tecnológico.
- [ ] Todos los Components `required` están implementados y disponibles.
- [ ] Cada Component pertenece a un único requirement level.

---

## 17. Estado

`TPL-FULLSTACK` se encuentra actualmente en estado `Experimental`.

Su composición deberá validarse mediante un mecanismo representativo antes de considerarse `Stable`.

La validación podrá realizarse mediante una implementación real, Reference Implementation, instanciación representativa, dogfooding u otro caso de uso suficientemente realista.