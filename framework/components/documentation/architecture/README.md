# DOC-ARCHITECTURE — Architecture

## 1. Propósito

`DOC-ARCHITECTURE` define una estructura reutilizable para documentar la arquitectura vigente de un proyecto.

Su objetivo es permitir que maintainers, desarrolladores y colaboradores comprendan:

- el contexto arquitectónico del sistema;
- su estructura general;
- sus principales componentes;
- las responsabilidades de cada componente;
- las relaciones entre ellos;
- los flujos relevantes;
- las restricciones que condicionan la arquitectura;
- las decisiones necesarias para comprender el diseño actual.

El componente describe la arquitectura a un nivel superior al detalle de implementación.

---

## 2. Cuándo utilizarlo

Se recomienda utilizar este componente cuando:

- el proyecto contiene varios módulos, componentes, capas o servicios;
- la estructura del repositorio no permite comprender por sí sola la arquitectura;
- existen límites arquitectónicos relevantes;
- diferentes componentes tienen responsabilidades diferenciadas;
- es necesario explicar cómo interactúan las principales partes del sistema;
- existen restricciones que condicionan el diseño.

Resulta especialmente apropiado para proyectos estratégicos o de madurez `L3` o superior.

---

## 3. Cuándo no utilizarlo

No es necesario cuando:

- el proyecto es suficientemente pequeño para explicar su arquitectura dentro del README;
- el documento duplicaría información existente sin aportar una visión arquitectónica superior;
- únicamente se necesita registrar una decisión concreta que debería documentarse mediante `DOC-ADR`;
- el contenido estaría formado principalmente por detalles de clases, funciones o archivos.

No debe incorporarse documentación arquitectónica únicamente por formalismo.

---

## 4. Responsabilidad

`DOC-ARCHITECTURE` responde principalmente a las preguntas:

```text
¿Qué arquitectura existe?

¿Cómo está organizado el sistema?

¿Qué responsabilidades tienen sus principales partes?

¿Cómo se relacionan?

¿Qué restricciones condicionan su diseño?
```

Describe el **estado arquitectónico actual**.

No pretende conservar todo el proceso histórico que condujo hasta él.

---

## 5. Architecture Document vs ADR

`DOC-ARCHITECTURE` y `DOC-ADR` cumplen responsabilidades diferentes.

### Architecture Document

Describe:

- arquitectura vigente;
- estructura;
- componentes;
- responsabilidades;
- relaciones;
- restricciones.

### ADR

Registra:

- contexto de una decisión;
- alternativas consideradas;
- decisión adoptada;
- consecuencias.

La relación esperada es:

```text
DOC-ARCHITECTURE
        │
        ├── describe la arquitectura actual
        │
        └── enlaza
                ↓
             DOC-ADR
                │
                └── explica decisiones concretas
```

El Architecture Document puede resumir una decisión relevante, pero no debe duplicar el ADR completo.

---

## 6. Estructura

La estructura conceptual recomendada es:

```text
Architecture
│
├── Propósito
├── Contexto
├── Visión General
├── Principios Arquitectónicos
├── Estructura del Sistema
├── Componentes
├── Relaciones y Flujos
├── Decisiones Relevantes
├── Restricciones
├── Documentación Relacionada
└── Quality Gates
```

No todas las secciones son obligatorias.

La complejidad del documento debe adaptarse a la complejidad real del proyecto.

---

## 7. Secciones requeridas

### Propósito

Explica qué arquitectura documenta el archivo y cuál es su alcance.

### Contexto

Define el sistema dentro de su entorno.

Puede describir:

- propósito del sistema;
- límites;
- actores;
- sistemas externos;
- integraciones principales.

### Visión General

Proporciona la explicación arquitectónica más breve capaz de permitir una comprensión global del sistema.

Un lector debería poder entender el modelo general antes de profundizar en las siguientes secciones.

### Estructura del Sistema

Presenta la descomposición principal del sistema.

Puede utilizar:

- módulos;
- componentes;
- capas;
- servicios;
- dominios;
- pipelines;
- directorios arquitectónicamente relevantes.

### Componentes

Describe las principales unidades arquitectónicas y sus responsabilidades.

El foco debe estar en:

- responsabilidad;
- límites;
- dependencias;
- propiedad de capacidades o datos.

No en clases o archivos individuales.

---

## 8. Secciones opcionales

### Principios Arquitectónicos

Documenta principios estables que influyen realmente sobre la arquitectura.

Ejemplos:

- separación de responsabilidades;
- modularidad;
- dirección de dependencias;
- desacoplamiento;
- simplicidad;
- evolución incremental.

No deben inventarse principios únicamente para completar la sección.

### Relaciones y Flujos

Explica cómo interactúan los componentes.

Dependiendo del proyecto puede representar:

- request flow;
- data flow;
- event flow;
- dependencias;
- comunicaciones entre servicios;
- interacción frontend/backend.

### Decisiones Relevantes

Resume decisiones necesarias para comprender la arquitectura actual.

Cuando una decisión requiera contexto histórico deberá enlazar al correspondiente `DOC-ADR`.

### Restricciones

Documenta condiciones que limitan o condicionan la arquitectura.

Por ejemplo:

- compatibilidad;
- plataforma;
- seguridad;
- infraestructura;
- APIs externas;
- restricciones de despliegue;
- reglas de dependencias.

### Documentación Relacionada

Permite profundizar mediante otros documentos especializados.

Ejemplos:

```text
DOC-ADR
DOC-API
DOC-DATABASE
DOC-DEPLOYMENT
DOC-SECURITY
DOC-DIAGRAMS
```

### Quality Gates

Define las condiciones mínimas para considerar útil y actualizada la documentación arquitectónica.

---

## 9. Nivel de Abstracción

`DOC-ARCHITECTURE` debe describir elementos arquitectónicamente estables.

Ejemplo adecuado:

```text
API Layer
    ↓
Application Services
    ↓
Persistence
```

Ejemplo excesivamente específico:

```text
UserController.java
    ↓
UserServiceImpl.java
    ↓
JpaUserRepository.java
```

Los detalles de implementación pertenecen al código o a documentación especializada.

La arquitectura debe seguir siendo útil aunque cambien clases, funciones o archivos internos.

---

## 10. Neutralidad Arquitectónica

El componente no prescribe una arquitectura concreta.

Puede documentar, entre otras:

- Layered Architecture;
- Hexagonal Architecture;
- Clean Architecture;
- Modular Monolith;
- Microservices;
- Event-Driven Architecture;
- Client-Server Architecture;
- Pipeline Architecture.

La plantilla describe la arquitectura seleccionada por el proyecto.

No selecciona una arquitectura por él.

---

## 11. Diagramas

Los diagramas son opcionales.

Deben utilizarse únicamente cuando expliquen una relación con mayor claridad que el texto.

Un diagrama deberá:

- tener una finalidad concreta;
- representar la arquitectura vigente;
- poder mantenerse;
- almacenarse en un formato versionable cuando sea posible;
- disponer de contexto textual suficiente.

Formatos recomendados:

```text
Mermaid
PlantUML
SVG
```

No deberán añadirse diagramas únicamente para hacer que la documentación parezca más técnica.

---

## 12. Reglas de Contenido

El Architecture Document debe:

- describir la arquitectura vigente;
- mantener un nivel de abstracción estable;
- identificar responsabilidades claramente;
- mostrar límites relevantes;
- explicar relaciones significativas;
- declarar restricciones importantes;
- evitar duplicar documentación especializada;
- enlazar ADR cuando sea necesario conservar contexto histórico.

Debe evitar convertirse en una especificación exhaustiva de implementación.

---

## 13. Relación con Otros Componentes

Una relación habitual puede representarse así:

```text
README-ARCHITECTURE
        ↓
README-DOCUMENTATION
        ↓
DOC-ARCHITECTURE
        │
        ├── DOC-ADR
        ├── DOC-DIAGRAMS
        ├── DOC-API
        ├── DOC-DATABASE
        └── DOC-DEPLOYMENT
```

El README proporciona orientación.

`DOC-ARCHITECTURE` proporciona comprensión estructural.

Los componentes especializados proporcionan profundidad adicional.

---

## 14. Personalización

Cada proyecto podrá adaptar:

- nombres de secciones;
- representación estructural;
- número de componentes;
- diagramas;
- profundidad;
- documentación relacionada.

La personalización no debe alterar la responsabilidad fundamental del componente:

> Explicar de forma clara y mantenible la arquitectura vigente del sistema.

---

## 15. Mantenimiento

El documento deberá revisarse cuando:

- se añada o elimine un componente arquitectónico importante;
- cambien límites relevantes;
- cambie la dirección de dependencias;
- se modifiquen integraciones principales;
- cambien significativamente los flujos de datos o interacción;
- aparezca una nueva restricción arquitectónica relevante.

Los cambios menores de implementación no deberían requerir una actualización arquitectónica.

---

## 16. Quality Gates

Antes de considerar válida una implementación:

- [ ] El límite del sistema resulta comprensible.
- [ ] La arquitectura general puede entenderse sin leer todo el código.
- [ ] Los principales componentes están identificados.
- [ ] Las responsabilidades están claramente separadas.
- [ ] Las relaciones relevantes están documentadas.
- [ ] Las restricciones arquitectónicas importantes son visibles.
- [ ] El documento mantiene un nivel adecuado de abstracción.
- [ ] No duplica innecesariamente documentación especializada.
- [ ] Las decisiones históricas se delegan a ADR cuando corresponde.
- [ ] Los diagramas, cuando existen, representan la arquitectura vigente.
- [ ] Los enlaces hacia documentación relacionada son válidos.

---

## 17. Estado del Componente

`DOC-ARCHITECTURE` se encuentra actualmente en estado `Experimental`.

Su contrato será validado mediante implementaciones reales antes de considerarse `Stable`.