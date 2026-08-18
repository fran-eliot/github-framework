# TPL-BACKEND — Backend Repository

## 1. Propósito

`TPL-BACKEND` define una composición reutilizable para repositorios cuyo producto principal es una aplicación, servicio, API, worker o proceso ejecutado principalmente en backend.

Su objetivo es proporcionar una base documental y estructural común sin imponer un lenguaje, framework, arquitectura o tecnología concreta.

---

## 2. Cuándo Utilizarlo

Se recomienda utilizar este Template para proyectos como:

- servicios backend;
- APIs;
- aplicaciones server-side;
- workers;
- procesos batch;
- servicios de integración.

Puede aplicarse, entre otros, a proyectos desarrollados con:

```text
Java / Spring
Python / FastAPI
Python / Django
Node.js / NestJS
```

La tecnología utilizada no forma parte del contrato del Template.

---

## 3. Cuándo No Utilizarlo

No debe utilizarse cuando:

- el producto principal sea documentación;
- frontend y backend formen una única unidad arquitectónica que requiera coordinación explícita;
- el repositorio sea únicamente una librería;
- la estructura específica del proyecto no pueda representarse razonablemente como un repositorio backend.

---

## 4. Responsabilidad

`TPL-BACKEND` responde principalmente a la pregunta:

> ¿Qué composición mínima de GitHub Framework Components permite mantener de forma coherente un repositorio backend?

No define:

- lenguaje;
- framework;
- base de datos;
- arquitectura software;
- protocolo;
- infraestructura;
- sistema de despliegue.

Estas decisiones pertenecen al proyecto concreto o a Components especializados.

---

## 5. Maturity

Nivel mínimo recomendado:

```text
L2
```

El Template está orientado inicialmente a repositorios públicos mantenidos.

Repositorios experimentales `L1` podrán utilizar una composición más reducida.

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
DOC-CHANGELOG
```

Estos elementos permiten:

- identificar el proyecto;
- explicar su propósito;
- presentar sus capacidades;
- comunicar su stack;
- permitir una primera ejecución;
- proporcionar acceso a documentación profunda;
- mantener historial de cambios.

---

## 7. Recommended Components

La composición habitual recomienda:

```text
README-STATUS
README-ARCHITECTURE
README-REPOSITORY-STRUCTURE
README-TESTING
DOC-ARCHITECTURE
DOC-PROJECT-STATUS
DOC-TESTING
```

Podrán omitirse cuando la complejidad del proyecto no justifique su incorporación.

---

## 8. Optional Components

Los Components opcionales permiten adaptar el Template a diferentes tipos de backend:

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
DOC-DEPLOYMENT
DOC-SECURITY
DOC-DIAGRAMS
DOC-REFERENCES
```

Por ejemplo:

- `DOC-API` solo resulta necesario cuando existe una interfaz pública relevante;
- `DOC-DATABASE` solo cuando existe un modelo de datos que necesita documentación propia;
- `DOC-DEPLOYMENT` cuando el despliegue tiene suficiente complejidad;
- `DOC-SECURITY` cuando existen decisiones de seguridad que necesitan documentación especializada.

---

### Disponibilidad de Components

Todos los Components `required` declarados por `TPL-BACKEND` disponen actualmente de implementación canónica en el Framework.

Por tanto, el contrato mínimo del Template puede materializarse con los Components disponibles en la versión actual.

Los niveles `recommended` y `optional` incluyen tanto Components implementados como responsabilidades conceptuales todavía no materializadas.

La disponibilidad actual puede resumirse como:

```text
Required       8/8  Implemented
Recommended    5/7  Implemented
Optional       3/13 Implemented
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

## 10. Estructura Específica

`TPL-BACKEND` no define inicialmente una estructura física propia.

No se impone:

```text
src/
tests/
config/
```

porque estas estructuras dependen del ecosistema tecnológico.

Ejemplos:

```text
Java
src/main/
src/test/
```

```text
Python
app/
tests/
```

```text
Node.js
src/
test/
```

La ausencia inicial de `template/` es deliberada.

El valor principal de `TPL-BACKEND` en esta versión reside en su composición de Components y sus reglas de uso.

---

## 11. Placeholders

Los placeholders mínimos previstos son:

```text
<PROJECT_NAME>
<PROJECT_DESCRIPTION>
<OWNER>
```

No se incorporarán placeholders dependientes de tecnología hasta que un caso de uso real los justifique.

---

## 12. Personalización

Una implementación podrá:

- añadir Components opcionales;
- omitir Components recomendados;
- incorporar estructura tecnológica propia;
- añadir documentación específica;
- configurar herramientas particulares.

Deberá conservar los Components `required` para considerarse una implementación completa de `TPL-BACKEND`.

---

## 13. Neutralidad Tecnológica

`TPL-BACKEND` no prescribe:

```text
Spring
Django
FastAPI
NestJS
PostgreSQL
MySQL
MongoDB
Docker
Kubernetes
```

El Template describe un tipo de repositorio.

No selecciona su stack tecnológico.

---

## 14. Quality Gates

Antes de considerar válida una implementación:

- [ ] El proyecto representa realmente un sistema backend.
- [ ] Los Components `required` están presentes.
- [ ] Los Components recomendados omitidos no son necesarios para comprender el proyecto.
- [ ] Los Components opcionales responden a necesidades reales.
- [ ] No se duplican especificaciones canónicas de Components.
- [ ] La documentación permite comprender y comenzar a utilizar el proyecto.
- [ ] La estructura tecnológica pertenece al proyecto y no al Template genérico.
- [ ] La composición sigue siendo independiente del lenguaje o framework.
- [ ] Todos los Components `required` están implementados y disponibles.
- [ ] Cada Component pertenece a un único requirement level.

---

## 15. Estado

`TPL-BACKEND` se encuentra actualmente en estado `Experimental`.

Su composición deberá validarse mediante un mecanismo representativo antes de considerarse `Stable`.

La validación podrá realizarse mediante una implementación real, Reference Implementation, instanciación representativa, dogfooding u otro caso de uso suficientemente realista.