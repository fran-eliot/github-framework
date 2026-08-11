# Architecture

| Campo                    | Valor                |
| ------------------------ | -------------------- |
| **Proyecto**             | `<PROJECT_NAME>`     |
| **Estado**               | `<DOCUMENT_STATUS>`  |
| **Última actualización** | `<YYYY-MM-DD>`       |

---

## Propósito

Este documento describe la arquitectura de `<PROJECT_NAME>`.

Su objetivo es explicar:

- <responsabilidad arquitectónica>;
- <responsabilidad arquitectónica>;
- <responsabilidad arquitectónica>.

El documento describe la estructura estable del sistema y evita detalles de implementación que no resulten arquitectónicamente relevantes.

---

## Contexto

### Propósito del Sistema

<Explicar brevemente qué problema resuelve el sistema y cuál es su responsabilidad principal.>

### Límite del Sistema

El sistema es responsable de:

- <responsabilidad>;
- <responsabilidad>;
- <responsabilidad>.

El sistema no es responsable de:

- <responsabilidad fuera de alcance>;
- <responsabilidad fuera de alcance>.

### Contexto Externo

<Describir usuarios, sistemas externos, APIs, servicios o infraestructura relevantes para comprender la arquitectura.>

Representación opcional:

```text
<ACTOR_OR_EXTERNAL_SYSTEM>
           │
           ▼
┌────────────────────────┐
│                        │
│     <PROJECT_NAME>     │
│                        │
└────────────────────────┘
           │
           ▼
<EXTERNAL_DEPENDENCY>
```

---

## Visión General de la Arquitectura

<Explicar en pocos párrafos el modelo arquitectónico general.

Esta sección debe permitir comprender la arquitectura sin necesidad de revisar todavía sus componentes individuales.>

### Estilo Arquitectónico

`<ARCHITECTURAL_STYLE>`

<Explicar únicamente cuando identificar el estilo ayude a comprender el sistema.>

Ejemplos:

```text
Layered Architecture
Modular Monolith
Hexagonal Architecture
Client-Server
Event-Driven Architecture
Pipeline Architecture
```

No asignar una etiqueta arquitectónica si no describe correctamente el sistema.

---

## Principios Arquitectónicos

> Eliminar esta sección cuando no existan principios arquitectónicos relevantes que documentar.

### <PRINCIPLE_NAME>

<Explicar cómo afecta este principio a la arquitectura.>

### <PRINCIPLE_NAME>

<Explicar cómo afecta este principio a la arquitectura.>

---

## Estructura del Sistema

El sistema se organiza en las siguientes áreas principales:

```text
<PROJECT>/
├── <COMPONENT_OR_MODULE>/
├── <COMPONENT_OR_MODULE>/
├── <COMPONENT_OR_MODULE>/
└── <COMPONENT_OR_MODULE>/
```

Esta representación debe mostrar estructura arquitectónica.

No es necesario reproducir todos los archivos o directorios del repositorio.

---

## Componentes

### <COMPONENT_NAME>

**Responsabilidad**

<Describir la responsabilidad principal del componente.>

**Gestiona**

- <capacidad, información o responsabilidad>;
- <capacidad, información o responsabilidad>.

**Depende de**

- <dependencia>;
- <dependencia>.

**No gestiona**

- <responsabilidad expresamente fuera del componente>.

---

### <COMPONENT_NAME>

**Responsabilidad**

<Describir la responsabilidad principal del componente.>

**Gestiona**

- <capacidad, información o responsabilidad>.

**Depende de**

- <dependencia>.

**No gestiona**

- <responsabilidad expresamente fuera del componente>.

---

## Relaciones y Flujos

<Explicar cómo interactúan los principales componentes arquitectónicos.>

Ejemplo:

```text
<ACTOR>
   │
   ▼
<COMPONENT_A>
   │
   ▼
<COMPONENT_B>
   │
   ├────────► <EXTERNAL_SYSTEM>
   │
   ▼
<COMPONENT_C>
```

### <FLOW_NAME>

1. <Primera interacción arquitectónica>.
2. <Segunda interacción arquitectónica>.
3. <Tercera interacción arquitectónica>.
4. <Resultado>.

El flujo debe documentarse a nivel arquitectónico.

Evitar detalles de métodos, clases o instrucciones concretas salvo que tengan relevancia arquitectónica.

---

## Decisiones Relevantes

| Decisión | Justificación breve | ADR |
| -------- | ------------------- | --- |
| `<DECISION>` | `<RATIONALE>` | `<ADR_LINK_OR_NA>` |
| `<DECISION>` | `<RATIONALE>` | `<ADR_LINK_OR_NA>` |

Esta sección resume únicamente las decisiones necesarias para comprender la arquitectura vigente.

Utilizar ADR para documentar contexto, alternativas y consecuencias completas.

---

## Restricciones

### <CONSTRAINT_NAME>

<Explicar la restricción y su impacto arquitectónico.>

### <CONSTRAINT_NAME>

<Explicar la restricción y su impacto arquitectónico.>

Pueden incluirse, por ejemplo:

- restricciones de plataforma;
- requisitos de compatibilidad;
- límites de seguridad;
- limitaciones de APIs externas;
- restricciones de despliegue;
- reglas de dependencias.

---

## Documentación Relacionada

| Documento | Propósito |
| --------- | --------- |
| `<DOCUMENT_LINK>` | `<DOCUMENT_PURPOSE>` |
| `<DOCUMENT_LINK>` | `<DOCUMENT_PURPOSE>` |

Eliminar las entradas que no existan en el proyecto.

---

## Quality Gates

- [ ] El límite del sistema está claramente definido.
- [ ] La arquitectura puede comprenderse sin revisar todo el código.
- [ ] Los principales componentes están identificados.
- [ ] Las responsabilidades están claramente diferenciadas.
- [ ] Las relaciones relevantes están documentadas.
- [ ] Las restricciones arquitectónicas son visibles.
- [ ] Los detalles de implementación no dominan el documento.
- [ ] Las decisiones que requieren contexto histórico enlazan a ADR cuando corresponde.
- [ ] Los diagramas representan la arquitectura vigente.
- [ ] La documentación relacionada está correctamente enlazada.

---

## Mantenimiento

Revisar este documento cuando:

- se añada o elimine un componente arquitectónico importante;
- cambien los límites del sistema;
- cambien dependencias arquitectónicas relevantes;
- cambien integraciones principales;
- cambien significativamente los flujos;
- cambien restricciones arquitectónicas.

Los cambios menores de implementación no requieren normalmente modificar este documento.