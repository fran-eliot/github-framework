# DOC-PROJECT-STATUS — Project Status

## 1. Propósito

`DOC-PROJECT-STATUS` define una estructura reutilizable para documentar el estado actual de un proyecto.

Su objetivo es proporcionar a maintainers y colaboradores una visión rápida y actualizada sobre:

- situación general del proyecto;
- progreso de sus principales áreas;
- trabajo actualmente en curso;
- próximos hitos;
- riesgos conocidos;
- objetivos inmediatos.

El componente representa una fotografía operativa del proyecto en un momento determinado.

---

## 2. Cuándo utilizarlo

Se recomienda utilizar este componente cuando un proyecto:

- evoluciona mediante múltiples versiones o iteraciones;
- dispone de varias áreas de trabajo;
- necesita comunicar regularmente su estado;
- mantiene un roadmap o planificación;
- requiere continuidad entre diferentes sesiones o colaboradores.

Resulta especialmente útil en repositorios de madurez `L2` o superior.

---

## 3. Cuándo no utilizarlo

No es necesario cuando:

- el repositorio es experimental y de vida muy corta;
- el estado puede comunicarse suficientemente mediante el README;
- no existe evolución o mantenimiento continuado;
- el documento acabaría duplicando información sin aportar contexto operativo.

El componente no debe incorporarse únicamente para aumentar la cantidad de documentación.

---

## 4. Responsabilidad

`DOC-PROJECT-STATUS` responde principalmente a la pregunta:

> ¿Cuál es el estado actual del proyecto y qué ocurrirá a continuación?

No sustituye a:

- `DOC-ROADMAP`, que describe la evolución prevista;
- `DOC-CHANGELOG`, que registra cambios publicados;
- `DOC-KNOWN-ISSUES`, que mantiene problemas conocidos;
- herramientas de gestión de Issues o Projects.

Debe resumir y enlazar cuando sea necesario, no duplicar esas fuentes.

---

## 5. Estructura

El componente se organiza en bloques progresivos:

```text
Metadata
   ↓
Estado General
   ↓
Estado por Áreas
   ↓
Trabajo Actual
   ↓
Próximo Hito
   ↓
Riesgos
   ↓
Principios Activos
   ↓
Próximos Objetivos
   ↓
Historial
```

No todas las secciones tienen que utilizarse en todos los proyectos.

---

## 6. Secciones requeridas

### Estado General

Resume brevemente la situación actual del proyecto.

Debe permitir comprender su estado sin necesidad de consultar el resto del documento.

### Estado por Áreas

Presenta el progreso de las principales capacidades, módulos o áreas del proyecto.

La granularidad debe mantenerse suficientemente alta para evitar convertir el documento en un gestor de tareas.

### Próximo Hito

Identifica el siguiente resultado significativo esperado.

### Próximos Objetivos

Enumera las prioridades inmediatas del proyecto.

---

## 7. Secciones opcionales

### Trabajo Actual

Puede representar:

- Sprint actual;
- iteración;
- fase;
- iniciativa;
- conjunto de trabajo activo.

La terminología dependerá de la metodología utilizada por el proyecto.

### Release Focus

Puede utilizarse cuando el desarrollo está organizado alrededor de una versión objetivo.

### Riesgos

Resume riesgos relevantes para la evolución inmediata del proyecto.

No sustituye a un registro especializado de riesgos cuando este sea necesario.

### Principios Activos

Permite destacar restricciones o principios especialmente relevantes durante la etapa actual.

### Historial de Versiones

Proporciona una referencia compacta de los principales estados alcanzados.

No sustituye al Changelog.

---

## 8. Reglas de Contenido

El Project Status debe:

- representar el estado presente;
- mantenerse conciso;
- priorizar información útil para la toma de decisiones;
- evitar detalles propios de tareas individuales;
- enlazar a fuentes más detalladas cuando existan;
- actualizarse cuando cambie materialmente el estado del proyecto.

No debe convertirse en una copia del backlog, roadmap o changelog.

---

## 9. Personalización

Los nombres de las áreas, estados y secciones podrán adaptarse al dominio del proyecto.

Por ejemplo:

```text
Estado por Áreas
```

podría representar:

- módulos de software;
- dominios funcionales;
- datasets;
- servicios;
- documentación;
- infraestructura.

La responsabilidad conceptual del componente debe mantenerse aunque cambie el dominio.

---

## 10. Relación con Otros Componentes

```text
DOC-ROADMAP
      │
      ▼
DOC-PROJECT-STATUS
      │
      ├── DOC-KNOWN-ISSUES
      │
      └── DOC-CHANGELOG
```

Las relaciones son informativas.

`DOC-PROJECT-STATUS` debe poder utilizarse independientemente cuando los demás componentes no estén presentes.

---

## 11. Mantenimiento

El documento deberá revisarse:

- al finalizar una iteración significativa;
- al publicar una versión;
- cuando cambie el estado de una capacidad importante;
- cuando cambien los próximos objetivos;
- cuando aparezca un riesgo relevante.

Las actualizaciones puramente cosméticas no justifican por sí mismas una nueva revisión.

---

## 12. Quality Gates

El documento deberá revisarse:

- [ ] al finalizar una iteración significativa;
- [ ] al publicar una versión;
- [ ] cuando cambie el estado de una capacidad importante;
- [ ] cuando cambien los próximos objetivos;
- [ ] cuando aparezca un riesgo relevante.

Las actualizaciones puramente cosméticas no justifican por sí mismas una nueva revisión.

---

## 13. Estado del Componente

`DOC-PROJECT-STATUS` se encuentra actualmente en estado `Experimental`.

Su contrato será validado mediante dogfooding sobre GitHub Framework antes de considerarse `Stable`.