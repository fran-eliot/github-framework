# DOC-REFERENCES — References

## 1. Propósito

`DOC-REFERENCES` define una estructura reutilizable para centralizar las fuentes externas relevantes utilizadas por un proyecto.

Su objetivo es facilitar el acceso a documentación, estándares, especificaciones y recursos de consulta sin dispersar enlaces importantes por múltiples documentos.

El componente proporciona contexto sobre las fuentes utilizadas, pero no sustituye a la documentación propia del proyecto.

---

## 2. Cuándo utilizarlo

Se recomienda utilizar este componente cuando un proyecto:

- depende de varios estándares o especificaciones;
- utiliza documentación externa relevante;
- necesita conservar referencias técnicas estables;
- cita RFC, papers o documentación oficial;
- requiere proporcionar contexto adicional a maintainers o colaboradores.

Resulta especialmente útil cuando las referencias aparecen repetidamente en distintos documentos.

---

## 3. Cuándo no utilizarlo

No es necesario cuando:

- existen muy pocas referencias;
- los enlaces pueden mantenerse de forma clara en el documento donde se utilizan;
- el componente se convertiría únicamente en una colección indiscriminada de URLs;
- las referencias no aportan contexto técnico relevante.

No debe crearse un registro de enlaces por formalismo.

---

## 4. Responsabilidad

`DOC-REFERENCES` responde principalmente a la pregunta:

> ¿Qué fuentes externas ayudan a comprender, implementar o mantener este proyecto?

Puede incluir:

- documentación oficial;
- estándares;
- RFC;
- especificaciones;
- papers;
- documentación de herramientas;
- recursos técnicos relevantes.

No debe convertirse en:

- una lista de bookmarks;
- una colección de tutoriales sin criterio;
- documentación interna del proyecto;
- un sustituto de otros componentes especializados.

---

## 5. Estructura

El componente puede organizar las referencias por categorías.

Ejemplo:

```text
References
│
├── Standards
├── Specifications
├── Official Documentation
├── Research
└── Additional Resources
```

Las categorías deben adaptarse al proyecto.

No es necesario mantener secciones vacías.

---

## 6. Tipos de Referencias

### Standards

Normas o estándares relevantes para el proyecto.

Ejemplos:

```text
Semantic Versioning
Keep a Changelog
Conventional Commits
```

### Specifications

Especificaciones técnicas utilizadas o implementadas.

Ejemplos:

```text
OpenAPI Specification
OAuth 2.0
JSON Schema
```

### Official Documentation

Documentación oficial de tecnologías, plataformas o herramientas.

Siempre deberá preferirse documentación primaria cuando exista.

### Research

Papers, publicaciones académicas o documentación de investigación relevante.

Especialmente útil en proyectos de IA, datos o investigación aplicada.

### Additional Resources

Recursos adicionales que aporten contexto significativo y no encajen en las categorías anteriores.

Esta sección deberá utilizarse con moderación.

---

## 7. Reglas de Contenido

Cada referencia deberá:

- tener una finalidad clara;
- utilizar un nombre descriptivo;
- enlazar preferentemente a la fuente original;
- aportar contexto suficiente para comprender por qué resulta relevante;
- mantenerse relacionada con el proyecto.

Debe evitarse registrar enlaces simplemente porque fueron consultados durante el desarrollo.

---

## 8. Formato de Referencia

Formato recomendado:

```markdown
- [Nombre de la referencia](URL) — Breve explicación de su relevancia.
```

Ejemplo:

```markdown
- [Semantic Versioning](URL) — Convención utilizada para el versionado de releases.
```

Cuando el contexto sea evidente, la explicación puede omitirse.

---

## 9. Fuentes Primarias

Siempre que sea posible deberá priorizarse:

```text
Official Documentation
        ↓
Official Specification
        ↓
Original Paper
        ↓
Secondary Resource
```

Una fuente secundaria puede resultar útil, pero no debería sustituir a la referencia original cuando esta esté disponible.

---

## 10. Organización

Las referencias deberán agruparse por significado, no por orden cronológico de incorporación.

Ejemplo:

```text
Standards
Specifications
Official Documentation
Research
```

No:

```text
Links added in June
Links added in July
Links added in August
```

---

## 11. Relación con Otros Componentes

`DOC-REFERENCES` puede ser consumido por distintos componentes:

```text
DOC-ARCHITECTURE
        │
        ├── DOC-ADR
        ├── DOC-SECURITY
        ├── DOC-API
        └── DOC-REFERENCES
```

Los demás documentos pueden enlazar a este componente cuando necesiten proporcionar una colección más amplia de fuentes.

Una referencia específica puede permanecer en su documento natural cuando centralizarla reduzca claridad.

---

## 12. Enlaces

Cuando las referencias formen parte del propio repositorio deberán utilizarse rutas relativas.

Para recursos externos deberán utilizarse enlaces estables y preferentemente oficiales.

Los enlaces obsoletos deberán eliminarse o sustituirse.

---

## 13. Mantenimiento

El documento deberá revisarse cuando:

- se incorpore un nuevo estándar relevante;
- cambie una especificación utilizada;
- una referencia deje de estar disponible;
- una fuente deje de representar la implementación actual;
- aparezca una fuente primaria mejor que una referencia secundaria existente.

No requiere actualización por cada consulta realizada durante el desarrollo.

---

## 14. Quality Gates

Antes de considerar válida una implementación:

- [ ] Cada referencia tiene una finalidad clara.
- [ ] Se priorizan fuentes primarias cuando existen.
- [ ] Los enlaces son válidos.
- [ ] No existen referencias duplicadas.
- [ ] Las categorías aportan claridad.
- [ ] No se incluyen enlaces irrelevantes.
- [ ] La documentación propia del proyecto no se sustituye por referencias externas.
- [ ] Las referencias continúan representando el estado actual del proyecto.

---

## 15. Estado del Componente

`DOC-REFERENCES` se encuentra actualmente en estado `Experimental`.

Su contrato será validado mediante implementaciones reales antes de considerarse `Stable`.