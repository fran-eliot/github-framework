# Automation Reference Implementation

| Field                 | Value                                  |
| --------------------- | -------------------------------------- |
| **Project**           | GitHub Framework                       |
| **Document**          | Automation Reference Implementation    |
| **Framework Version** | v0.6.0 (en desarrollo)                 |
| **Validator**         | Framework Validator (#25)              |
| **Metadata Contract** | Component Metadata Standard (#23)      |
| **Metadata Baseline** | Component Metadata Normalization (#24) |
| **Status**            | Validated                              |
| **Validation Method** | Dogfooding                             |

---

## 1. Propósito

Este documento registra la primera **Automation Reference Implementation** de GitHub Framework.

La implementación de referencia utiliza el propio repositorio GitHub Framework para demostrar que el Framework Validator puede descubrir, cargar y validar los metadatos normalizados de los Components implementados.

La validación contrasta conjuntamente:

* el contrato definido por `21_COMPONENT_METADATA_STANDARD.md`;
* los metadatos normalizados de `framework/components/`;
* las reglas implementadas por el Framework Validator;
* el comportamiento observable de su interfaz de línea de comandos.

El objetivo no es declarar que toda la automatización futura del Framework está implementada.

El objetivo es obtener evidencia reproducible de que el contrato actual puede verificarse de forma determinista sobre un repositorio real.

---

## 2. Alcance

La Reference Implementation comprende:

* ejecución del validador sobre los Components implementados;
* comprobación del Common Core y de las extensiones aplicables;
* verificación de identidad, unicidad de IDs y dependencias declaradas;
* validación de artefactos Workflow y de su ubicación física;
* comprobación de resultados legibles;
* verificación de códigos de salida de éxito y error;
* demostración de fallos representativos mediante entornos de prueba aislados;
* registro de supuestos, limitaciones y posibles refinamientos.

Quedan fuera de alcance:

* generación automática de repositorios o Components;
* modificación automática de metadatos;
* migraciones y adaptadores para formatos históricos;
* integración con GitHub Actions u otros sistemas CI;
* orquestación compleja de pipelines;
* decisiones arquitectónicas o de ciclo de vida tomadas por el validador;
* mantenimiento autónomo del repositorio.

La implementación de referencia no introduce un registro paralelo de Components. Los archivos `metadata.yml` continúan siendo la fuente de verdad de los Components implementados.

---

## 3. Repositorio y componentes validados

Repositorio consumidor y objeto de validación:

```text
GitHub Framework
```

Raíz de descubrimiento:

```text
framework/components/
```

Distribución observada durante la ejecución de referencia:

| Familia       | Components descubiertos |
| ------------- | ----------------------: |
| Documentation |                       4 |
| README        |                      12 |
| Workflow      |                       5 |
| **Total**     |                  **21** |

El validador descubre los directorios de Components implementados y procesa sus respectivos archivos `metadata.yml`.

Los Components conceptuales que no disponen de implementación física quedan fuera de este descubrimiento.

La validación de dependencias no exige que todos los IDs referenciados correspondan a Components implementados físicamente: pueden existir dependencias declaradas hacia Components conceptuales.

---

## 4. Método de validación

La validación combina dos tipos de evidencia:

**A. Dogfooding sobre el repositorio real.** Se ejecuta el CLI sobre los 21 Components existentes, sin alterar sus metadatos, y se comprueba que el proceso termina correctamente.

**B. Pruebas aisladas de comportamiento.** Se ejecutan pruebas sobre directorios temporales que contienen Components válidos o deliberadamente incorrectos. Estas pruebas permiten demostrar el tratamiento de errores sin introducir datos inválidos en el repositorio real.

Flujo de referencia:

```text
Component Metadata Standard
              │
              ▼
Normalized metadata.yml
              │
              ▼
Framework Validator
              │
       ┌──────┴──────┐
       ▼             ▼
  Valid metadata  Invalid metadata
       │             │
       ▼             ▼
  Readable report  Readable errors
  Exit code: 0     Exit code: 1
```

Los tests verifican el comportamiento del validador, mientras que la ejecución sobre el repositorio confirma su aplicación a los Components reales.

Una ejecución satisfactoria sobre el repositorio no sustituye las pruebas negativas. Ambas evidencias son complementarias.

---

## 5. Punto de entrada y ejecución local

El Framework Validator dispone de un punto de entrada mínimo mediante un módulo Python.

Desde la raíz del repositorio, con el entorno Python del proyecto preparado:

```powershell
python -m scripts.framework_validator
```

Para consultar el código de salida inmediatamente después de la ejecución, en PowerShell:

```powershell
$LASTEXITCODE
```

Para ejecutar la batería de pruebas:

```powershell
python -m unittest discover -s tests/framework_validator -p "test_*.py"
```

Para ejecutar únicamente las pruebas de integración del CLI:

```powershell
python -m unittest discover -s tests/framework_validator -p "test_cli.py" -v
```

El CLI valida el árbol de Components configurado por el proyecto. No se ha introducido una interfaz pública para seleccionar arbitrariamente otros repositorios ni un sistema de configuración adicional.

La ejecución local no depende de GitHub Actions.

---

## 6. Evidencia positiva: validación del repositorio real

Se ejecutó el Framework Validator desde la raíz del repositorio GitHub Framework:

```powershell
python -m scripts.framework_validator
```

La ejecución descubrió los siguientes Components:

```text
GitHub Framework Validator

Components discovered: 21
  DOC-ARCHITECTURE: architecture
  DOC-CHANGELOG: changelog
  DOC-PROJECT-STATUS: project-status
  DOC-REFERENCES: references
  README-ARCHITECTURE: architecture
  README-AUTHOR: author
  README-DOCUMENTATION: documentation
  README-FEATURES: features
  README-FOOTER: footer
  README-HERO: hero
  README-OVERVIEW: overview
  README-QUICK-START: quick-start
  README-ROADMAP: roadmap
  README-STATUS: status
  README-TECH-STACK: tech-stack
  README-TESTING: testing
  WCL-BRANCH: branch
  WCL-CODE-REVIEW: code-review
  WCL-COMMIT: commit
  WCL-ISSUE: issue
  WCL-PULL-REQUEST: pull-request

Validation passed: discovery, metadata loading, Common Core, identity, uniqueness, maturity, dependencies and Workflow extensions.
```

La consulta inmediata de `$LASTEXITCODE` devolvió:

```text
0
```

### Resultado observado

| Comprobación                 | Resultado              |
| ---------------------------- | ---------------------- |
| Descubrimiento de Components | 21 descubiertos        |
| Carga de metadatos           | Sin errores reportados |
| Common Core                  | Sin errores reportados |
| Identidad canónica           | Sin errores reportados |
| Unicidad de IDs              | Sin errores reportados |
| Madurez y dependencias       | Sin errores reportados |
| Extensiones Workflow         | Sin errores reportados |
| Informe de ejecución         | Legible                |
| Código de salida             | `0`                    |

**Resultado:** el conjunto actual de Components implementados supera las reglas del Framework Validator.

Este resultado acredita la conformidad con las comprobaciones implementadas en la versión actual del validador. No constituye una verificación exhaustiva de todos los aspectos arquitectónicos o documentales del Framework.

---

## 7. Evidencia negativa: errores representativos

Los errores se demostraron mediante pruebas de integración del CLI sobre directorios temporales.

Cada prueba construye un árbol de Components aislado, sustituye temporalmente la raíz de descubrimiento y ejecuta `main()`.

Este procedimiento evita modificar los metadatos reales del Framework.

### 7.1. Metadatos inválidos

Prueba:

```text
test_invalid_common_core
```

Se modifica deliberadamente el estado de un Component de prueba:

```yaml
status: Unknown
```

El CLI debe:

* detectar el valor no reconocido;
* identificar la propiedad `status`;
* incluir el archivo `metadata.yml` en el informe;
* comunicar el fallo de validación;
* devolver el código de salida `1`.

**Resultado:** prueba superada.

### 7.2. Artefacto Workflow inexistente

Prueba:

```text
test_missing_workflow_artifact
```

Se construye un Component `WCL-ISSUE` temporal que declara:

```yaml
artifacts:
  specification: README.md
  templates:
    - templates/bug_report.yml
```

Se crea físicamente `README.md`, pero se omite deliberadamente `templates/bug_report.yml`.

El CLI debe identificar:

```text
artifacts.templates[0]
```

y comunicar que el archivo declarado no existe.

**Resultado:** prueba superada; código de salida esperado y comprobado: `1`.

Este caso demuestra que el validador no se limita a comprobar la estructura YAML: también contrasta los artefactos locales declarados con el sistema de archivos.

### 7.3. ID duplicado entre Components

Prueba:

```text
test_duplicate_component_id
```

Se crean dos Components temporales:

```text
documentation/
├── architecture/
│   └── metadata.yml
└── references/
    └── metadata.yml
```

Ambos declaran deliberadamente:

```yaml
id: DOC-ARCHITECTURE
```

El CLI debe:

* descubrir los dos Components;
* detectar la duplicidad de `DOC-ARCHITECTURE`;
* identificar la primera declaración;
* informar del fallo;
* devolver el código de salida `1`.

El segundo Component también incumple la correspondencia entre su ID y su directorio físico. Ambos errores pueden aparecer en el mismo informe.

**Resultado:** prueba superada.

### 7.4. Otros errores cubiertos

La batería de integración también comprueba:

| Prueba                       | Condición                                           |
| ---------------------------- | --------------------------------------------------- |
| `test_empty_components_root` | No se descubre ningún Component                     |
| `test_missing_metadata`      | Un directorio de Component carece de `metadata.yml` |
| `test_invalid_yaml`          | El archivo YAML no puede cargarse                   |

Estas pruebas verifican que el CLI informa de fallos de descubrimiento o carga sin presentar un resultado de validación satisfactorio.

---

## 8. Resultados de las pruebas automatizadas

### 8.1. Pruebas de integración del CLI

Comando:

```powershell
python -m unittest discover -s tests/framework_validator -p "test_cli.py" -v
```

Resultado observado:

```text
test_duplicate_component_id ... ok
test_empty_components_root ... ok
test_invalid_common_core ... ok
test_invalid_yaml ... ok
test_missing_metadata ... ok
test_missing_workflow_artifact ... ok
test_valid_component ... ok

Ran 7 tests

OK
```

Las siete pruebas verifican conjuntamente los caminos de éxito y error del CLI.

### 8.2. Batería completa

Antes de incorporar las dos nuevas pruebas de integración, se ejecutó la batería completa:

```text
Ran 107 tests

OK
```

Las dos pruebas añadidas en #26 elevan la batería completa a 109 tests.

La ejecución completa con las nuevas pruebas:

```
Ran 109 tests

OK
```

---

## 9. Contrato de salida

El comportamiento demostrado del Framework Validator distingue dos resultados:

| Código | Significado                                                        |
| ------ | ------------------------------------------------------------------ |
| `0`    | La ejecución termina sin errores de validación                     |
| `1`    | Se detecta al menos un error de descubrimiento, carga o validación |

El informe proporciona contexto sobre los Components procesados y, cuando corresponde, identifica propiedades, archivos o inconsistencias.

Los códigos de salida pertenecen al proceso del validador.

Cuando el validador se ejecuta dentro de una prueba automatizada, el ejecutor de tests tiene su propio código de salida. Por ejemplo, un test que comprueba correctamente que el validador devuelve `1` puede terminar con código `0` porque la prueba ha pasado.

El CLI no modifica automáticamente los metadatos ni intenta resolver los errores detectados.

---

## 10. Reglas ejercitadas

La evidencia combina la validación del repositorio real con las pruebas aisladas.

| Área                | Comprobaciones ejercitadas                                         |
| ------------------- | ------------------------------------------------------------------ |
| Descubrimiento      | Familias y directorios de Components implementados                 |
| Carga               | Presencia de `metadata.yml`, YAML válido y estructura de metadatos |
| Common Core         | Campos obligatorios, tipos y vocabularios controlados              |
| Identidad           | Correspondencia entre familia, directorio e ID                     |
| Unicidad            | IDs duplicados entre Components                                    |
| Madurez             | Niveles y declaraciones compatibles con el contrato                |
| Dependencias        | Estructura, IDs, versiones mínimas y duplicidades                  |
| Workflow            | Materialización, artefactos, adopción y evidencias                 |
| Sistema de archivos | Existencia y ubicación de artefactos locales                       |
| CLI                 | Informe legible y códigos de salida `0` y `1`                      |

Las pruebas unitarias complementan las pruebas de integración mediante casos específicos de valores inválidos, rutas absolutas, escape del directorio del Component, duplicidades y campos ausentes.

La implementación de referencia no pretende demostrar que todas las combinaciones posibles de metadatos hayan sido probadas. Su propósito es verificar el contrato implementado mediante casos reales y fallos representativos.

---

## 11. Dogfooding Findings

La aplicación del Framework Validator al propio repositorio GitHub Framework permite registrar los siguientes hallazgos.

### Finding 1 — El contrato normalizado es verificable

Los 21 Components implementados superan las reglas del validador sobre sus respectivos archivos `metadata.yml`.

La validación confirma que el contrato normalizado de #23, aplicado en #24, puede procesarse mediante las reglas deterministas desarrolladas en #25.

Resultado:

```text
Normalized Component Metadata
            ↓
Framework Validator
            ↓
21 Components validated
```

No se han identificado errores de metadatos durante la ejecución de referencia.

Este resultado no implica que cualquier propiedad futura del Framework quede automáticamente cubierta por el validador.

### Finding 2 — Los artefactos Workflow pueden contrastarse con el sistema de archivos

Los Components Workflow declaran artefactos locales mediante `artifacts.specification` y, cuando corresponde, `artifacts.templates`.

El validador comprueba su existencia y que sus rutas permanezcan dentro del directorio del Component.

La prueba de integración `test_missing_workflow_artifact` demuestra que una declaración estructuralmente válida puede producir un error si el archivo físico no existe.

Resultado:

```text
Declared local artifact
          ↓
Filesystem validation
          ↓
Existing file / Validation error
```

La propiedad `adoption.target` representa una ubicación prevista en el repositorio consumidor. No se interpreta como un archivo que deba existir dentro del directorio del Component.

### Finding 3 — Las inconsistencias entre Components requieren validación conjunta

La unicidad de los IDs no puede comprobarse examinando cada `metadata.yml` de forma aislada.

La prueba `test_duplicate_component_id` demuestra que el validador identifica una declaración repetida entre dos Components y señala su primera aparición.

Resultado:

```text
Component A ── ID ──┐
                    ├── Duplicate detected
Component B ── ID ──┘
```

La validación de identidad física y la validación de unicidad son complementarias. Una misma declaración puede incumplir ambas reglas y producir más de un error.

### Finding 4 — La ejecución local es suficiente para demostrar el contrato inicial

El punto de entrada:

```powershell
python -m scripts.framework_validator
```

permite ejecutar la validación sin depender de un proveedor de CI.

Los códigos de salida `0` y `1` proporcionan un contrato mínimo para distinguir ejecuciones satisfactorias y fallidas.

La integración con GitHub Actions u otros sistemas podrá evaluarse posteriormente, sin convertirla en requisito de esta Reference Implementation.

### Finding 5 — Los errores deben detectarse sin modificar el repositorio

Las pruebas negativas utilizan directorios temporales y no requieren introducir metadatos inválidos en los Components reales.

Este enfoque permite verificar errores de carga, estructura, identidad, artefactos y duplicidad de forma aislada y reproducible.

El validador informa de los problemas, pero no modifica los archivos ni decide cómo resolverlos.

### Finding 6 — La validación automatizada y la evaluación arquitectónica son distintas

El validador comprueba reglas expresables de forma determinista.

No sustituye la revisión humana de responsabilidades, composición, calidad documental o decisiones arquitectónicas.

Resultado:

```text
Deterministic validation
          ≠
Architectural assessment
```

Una ejecución satisfactoria acredita que no se han detectado incumplimientos de las reglas implementadas. No constituye una certificación general de calidad del repositorio.

---

## 12. Supuestos y limitaciones

### 12.1. Supuestos

La implementación de referencia parte de los siguientes supuestos:

* La ejecución se realiza desde la raíz del repositorio, con el entorno Python y las dependencias del proyecto preparados.
* Los Components implementados se encuentran bajo `framework/components/`, organizados en las familias reconocidas.
* Cada Component implementado dispone de un archivo `metadata.yml`.
* Los metadatos normalizados son la fuente de verdad para las propiedades validadas.
* Las rutas de artefactos Workflow son relativas al directorio de su Component.
* Las pruebas de integración pueden sustituir temporalmente la raíz de descubrimiento para construir escenarios aislados.

### 12.2. Limitaciones

El Framework Validator actual:

* reconoce las familias implementadas `README`, `Documentation` y `Workflow`;
* no descubre Components conceptuales sin directorio físico;
* no exige que las dependencias declaradas correspondan a Components implementados;
* no verifica automáticamente la satisfacción de responsabilidades por parte de un repositorio consumidor;
* no valida la calidad semántica del contenido de los documentos;
* no genera ni corrige archivos;
* no realiza migraciones de metadatos históricos;
* no incorpora integración CI en esta fase;
* no proporciona una interfaz pública para seleccionar arbitrariamente una raíz de Components.

La validación de extensiones específicas se aplica donde existen reglas implementadas. La ausencia de una regla adicional no debe interpretarse como una validación implícita de cualquier propiedad.

---

## 13. Refinamientos del contrato y del validador

La implementación de referencia no ha identificado, durante la ejecución positiva sobre los 21 Components, una incompatibilidad que exija modificar el contrato normalizado.

La revisión realizada durante #25 permitió alinear el validador con los estándares existentes:

| Ajuste                         | Resultado                                            |
| ------------------------------ | ---------------------------------------------------- |
| Estados de referencia Workflow | `Pending` y `Validated` reconocidos                  |
| Materialización Workflow       | `Template` incorporado como mecanismo válido         |
| Wrappers históricos            | `component` y `classification` rechazados en la raíz |

Estos ajustes se incorporaron al validador antes de la Reference Implementation y no representan cambios nuevos en el contrato de #23.

No se propone introducir reglas adicionales, un registro paralelo ni nuevos mecanismos de automatización como resultado de este dogfooding.

Si futuras implementaciones detectan una incompatibilidad real, deberá registrarse y evaluarse antes de modificar el contrato o el validador.

---

## 14. Reproducibilidad

La Reference Implementation puede reproducirse mediante el siguiente procedimiento:

1. Preparar el entorno Python del proyecto.
2. Ejecutar la batería de tests del Framework Validator.
3. Ejecutar el CLI sobre el repositorio real.
4. Consultar el código de salida.
5. Comprobar que el informe identifica los Components descubiertos y el resultado de validación.

Comandos:

```powershell
python -m unittest discover -s tests/framework_validator -p "test_*.py"
python -m scripts.framework_validator
$LASTEXITCODE
```

Las pruebas negativas están incluidas en la batería automatizada y utilizan directorios temporales.

No es necesario modificar manualmente los `metadata.yml` reales para reproducir los escenarios de error.

---

## 15. Criterios de finalización

La Reference Implementation se considerará completada cuando:

* [x] el validador se haya ejecutado sobre los Components reales;
* [x] los 21 Components implementados hayan superado la validación;
* [x] se haya verificado el código de salida `0`;
* [x] se hayan demostrado errores representativos con código de salida `1`;
* [x] se hayan cubierto mediante integración los errores de artefactos y duplicidad;
* [x] se hayan documentado el punto de entrada, los resultados y las limitaciones;
* [x] se haya ejecutado la batería completa tras incorporar las nuevas pruebas;
* [x] se haya realizado la revisión final del documento y los cambios de #26.

La validación final del Sprint 8 y la preparación de la release `v0.6.0` son actividades posteriores e independientes del cierre de esta implementación de referencia.

---

## 16. Estado

```text
Status: Validated
```

La primera Automation Reference Implementation ha demostrado el funcionamiento del Framework Validator sobre los 21 Components implementados de GitHub Framework.

La ejecución real ha finalizado correctamente y las pruebas de integración han demostrado fallos representativos sin alterar el repositorio.

La Reference Implementation queda validada mediante dogfooding. Su incorporación al repositorio se registra en el commit de #26.