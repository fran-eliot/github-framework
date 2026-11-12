# Only Film — Assessment Batch 6: Demo, Highlights y Diagrams

## 1. Contexto

Inspección documental **read-only** de tres Responsibilities `Optional` de `TPL-BACKEND` 0.1.0 para el repositorio consumidor `fran-eliot/only_film`.

| Campo | Valor |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND metadata 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Collection Scope | `README-DEMO`, `README-HIGHLIGHTS`, `DOC-DIAGRAMS` |
| Assessment Status | `In Progress` |
| Mutation | `NONE` |

Se han inspeccionado el README y las rutas del árbol Git fijado. No se ha ejecutado la aplicación ni inspeccionado visualmente el contenido de cada imagen. El nivel `Optional` no equivale a `Not Applicable`.

## 2. Resumen provisional

| Responsibility | Requirement Level | Cobertura | State / Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-DEMO` | `Optional` | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `README-HIGHLIGHTS` | `Optional` | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |
| `DOC-DIAGRAMS` | `Optional` | Explored — provisional | Pendientes de revisión | `Needs Further Evaluation` | `—` |

`Explored — provisional` describe cobertura de inspección; no es un `State` del Assessment Template.

## 3. README-DEMO

**Detected Facts**

- El README contiene una sección `Capturas de la aplicación`, con una tabla que referencia imágenes de cartelera, detalle de película, selección de butacas y compra con ticket QR.
- En el árbol Git existen las rutas `docs/screenshots/cartelera.png`, `pelicula.png`, `sesion.png`, `compra-qr.png`, `checkout.png`, `perfil-usuario.png`, `usuarios-admin.png` y otras capturas.
- El README ofrece un procedimiento de arranque local mediante Docker Compose y la ruta `http://localhost:8080/movies`.
- La ruta de aplicación indicada es local; no constituye por sí sola un enlace a una demo pública en funcionamiento.

**Evidence**

- [README.md — Capturas e inicio rápido](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Directorio de capturas en el commit fijado](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c/docs/screenshots)

**Evaluation Rationale (pendiente)**

Las capturas y las instrucciones de ejecución son posibles materiales de demostración, pero la existencia de archivos de imagen no demuestra que los flujos funcionen en el commit inspeccionado ni que haya una demo desplegada o reproducible por un usuario nuevo.

**Uncertainty**

- ¿Bastan capturas para los objetivos documentales de Demo en este consumer, o hace falta una demostración ejecutable o vídeo?
- ¿Las imágenes reflejan exactamente la interfaz del commit evaluado?
- ¿Existen restricciones de credenciales o datos de demostración que deban explicarse?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 4. README-HIGHLIGHTS

**Detected Facts**

- El README describe funcionalidades diferenciadas para visitantes, usuarios y administradores.
- En la descripción de `Funcionalidades` se destaca la prevención de doble venta de butacas mediante transacciones y bloqueo de base de datos.
- En `Seguridad y límites actuales` se detallan medidas declaradas como BCrypt, CSRF, control de propiedad de entradas y reseñas, validación de imágenes y limitaciones del checkout de demostración.
- El README no presenta un apartado denominado literalmente `Highlights`; las capacidades destacadas se distribuyen entre secciones existentes.

**Evidence**

- [README.md — Funcionalidades, seguridad y límites](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [pom.xml — dependencias declaradas](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) (fuente de contexto, no prueba de funcionamiento)

**Evaluation Rationale (pendiente)**

Las capacidades destacadas son afirmaciones documentales que podrían servir como Highlights. Una sección con otro título no representa incumplimiento automático; falta evaluar si están suficientemente diferenciadas de la descripción general y sustentadas por evidencia funcional actual.

**Uncertainty**

- ¿Qué funcionalidades destacan realmente como valor diferencial ante un usuario o colaborador nuevo?
- ¿Conviene separar destacados de la enumeración completa de Features?
- ¿Qué afirmaciones necesitan evidencias de pruebas o demostración antes de presentarse como verificadas?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

## 5. DOC-DIAGRAMS

**Detected Facts**

- El README incluye un flujo textual de capas `Controlador MVC → servicio / reglas de negocio → repositorio JPA → base de datos`.
- El árbol Git del commit contiene imágenes de interfaz bajo `docs/screenshots/` y un recurso SVG de interfaz en `src/main/resources/static/images/avatar.svg`.
- En la inspección de rutas del árbol no se identificaron archivos nombrados como diagramas de arquitectura ni archivos de formatos habituales `.drawio`, `.puml` o Mermaid.
- No se ha inspeccionado exhaustivamente el contenido de todos los documentos para detectar diagramas embebidos en Markdown u otros formatos.
- Las capturas de pantalla y el SVG de interfaz no se pueden clasificar automáticamente como diagramas técnicos del sistema.

**Evidence**

- [README.md — Tecnologías y arquitectura](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Árbol Git fijado](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)
- [Auditoría de arquitectura histórica](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) (existencia documentada; no se afirma que contenga diagramas)

**Evaluation Rationale (pendiente)**

Existe una descripción textual de arquitectura, pero no se ha verificado un artefacto de diagrama técnico. La ausencia de un fichero con nombre o extensión específica no demuestra automáticamente que la Responsibility esté `Missing`; además, el Template la clasifica como `Optional`.

**Uncertainty**

- ¿Necesita este proyecto diagramas para comunicar relaciones de entidades, flujos o despliegue?
- ¿Existen diagramas embebidos en documentos que esta inspección de rutas no localizó?
- ¿Sería suficiente el flujo textual o aportaría valor un diagrama mantenible?

**State / Applicability:** pendientes de revisión semántica.

**Decision Status:** `Needs Further Evaluation`. **Adoption Decision:** `—`.

**Propuesta semántica posterior:** la [revisión E3 de Demo, Highlights y Diagrams](only-film-optional-showcase-semantic-review.md) distingue recursos de presentación de una demo operativa, evidencias parciales de funcionalidades y diagramas técnicos no verificados. Los estados y aplicabilidades siguen sujetos a reviewer, sin resolver Adoption Decisions.

## 6. Resultado y continuación

| Verificación | Resultado |
| --- | --- |
| Tres responsabilidades Optional identificadas en TPL-BACKEND | Documentado |
| Hechos observables vinculados al SHA del consumer | Documentados |
| Límites de capturas, destacados y diagramas distinguidos | Documentados |
| Revisión humana de State, Applicability y decisiones | Pendiente |
| Ejecución del consumer, tests y despliegue | No realizada |
| Mutation | `NONE` |

La [matriz de cobertura](only-film-assessment-coverage.md) pasa de **19/28 a 22/28 Responsibilities exploradas documentalmente**: 8 Required, 7 Recommended y 7 Optional. Permanecen **6 Optional sin explorar**.

No se ha determinado la conformidad de estas responsabilidades. El Assessment permanece `In Progress` y no se autoriza Application ni Integration.
