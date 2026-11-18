# 17 — Global Strategic Review

Date: 2026-11-18  
Status: Proposed — strategic review in progress  
Baseline: [59c2167265d0d72579b8a65ecc30a4bd1247d33b](https://github.com/fran-eliot/github-framework/commit/59c2167265d0d72579b8a65ecc30a4bd1247d33b)

## Propósito

Orientar la evolución de GitHub Framework por resultados útiles para consumidores, no por acumulación de opciones, componentes o documentos. Esta revisión no cambia la arquitectura, el Roadmap comprometido ni el alcance de ninguna release.

## Baseline y evidencia

- [v0.12.0](https://github.com/fran-eliot/github-framework/releases/tag/v0.12.0), tag 8fc0a036489a60f72c2ee66185bbd5e53b3a89c1.
- [PR #393](https://github.com/fran-eliot/github-framework/pull/393) integrada, rama eliminada; sin PR abiertas al verificar el baseline.
- [CI 44409979771](https://github.com/fran-eliot/github-framework/actions/runs/44409979771): Ubuntu, Windows y paridad correctos.
- Composition Preview Complete — Unreleased. La aceptación AC-01–AC-17 y sus límites se conservan; 282 + 24 tests por plataforma corresponden a la evidencia del cierre, no a una nueva ejecución independiente.
- 21 Components implementados, 41 conceptuales y tres Repository Templates según el inventario del Discovery. Las 77 referencias del preview (43 Resolved, 34 Conceptual) son ocurrencias, no IDs únicos.
- Only Film: Assessment exclusivamente documental Complete, sin autorización de Application/Integration ni modificación. UX-02 Prepared — Not Executed.

Fuentes de gobierno: [Continuity Kit](16_CONTINUITY_KIT.md), [Project Status](12_PROJECT_STATUS.md), [Backlog](14_BACKLOG.md), [Roadmap](../../ROADMAP.md), [CHANGELOG](../../CHANGELOG.md), [README](../../README.md).

## Diagnóstico preliminar

| Área | Madurez cualitativa | Brecha principal |
| --- | --- | --- |
| Arquitectura, estándares y gobierno | Consolidada | Evitar duplicidad y sobrearquitectura |
| Component Library y Templates | Operativa, parcial | Cobertura útil de recorridos completos |
| Validator y CI | Operativa, verificada internamente | Distribución y uso por terceros; no certificación de consumidores |
| Composition Preview | Complete — Unreleased | Resolución no equivale a generación |
| Adoption Cores | Documentados y verificados mediante escenarios acotados | Reducir esfuerzo manual y demostrar uso integral |
| Experiencia y distribución | Incipiente | Onboarding reproducible y evidencia independiente |
| Generación de repositorios | No implementada | Materialización segura y personalización explícita |

Las valoraciones son juicios de revisión preliminar, no mediciones certificadas. No se ha realizado nueva auditoría de código, benchmark externo ni prueba independiente de usabilidad.

## Visión candidata

Repository engineering a lo largo del ciclo de vida: CREATE y ADOPT como entradas; VALIDATE, MAINTAIN e IMPROVE como capacidades de continuidad. Mantener los contratos humanos de Adoption y separar la validación de bibliotecas de la validación de consumidores. La visión no afirma que estas capacidades estén actualmente implementadas.

## Hipótesis de valor y prioridades candidatas

| Línea | Resultado para el usuario | Prioridad provisional | Evidencia requerida |
| --- | --- | --- | --- |
| Recorrido de primer uso | Obtener un resultado útil sin conocer la arquitectura interna | Muy alta | Ejecución reproducible, tiempos y obstáculos registrados |
| Composición a materialización | Crear un repositorio nuevo a partir de una selección explícita | Muy alta | Experimento aislado, sin sobrescrituras, archivos verificables, tratamiento de componentes conceptuales |
| Assisted Analysis ejecutable | Reducir recopilación repetitiva de evidencia de repositorios existentes | Alta | Comparación con evidencia manual, límites y errores explícitos |
| Distribución y contratos | Ejecutar herramientas sin depender del conocimiento del árbol fuente | Alta | Instalación reproducible y contrato de compatibilidad acotado |
| Componentes adicionales | Cerrar carencias concretas de recorridos | Condicionada | Caso de uso y reutilización demostrados |
| Mantenimiento continuo | Detectar cambios relevantes sin decidir automáticamente | Posterior | Necesidad observada tras adopción |
| Marketplace, interfaz gráfica, plugins y automatización autónoma | Ampliar ecosistema | Diferida | Demanda demostrada y coste sostenible |

## Método de selección

Comparar necesidad, utilidad directa, alcance de usuarios, evidencia disponible, esfuerzo, riesgo y coste de mantenimiento. Las prioridades anteriores son hipótesis, no compromisos. No asignar puntuaciones de demanda sin datos. Comparar al menos creación de repositorios nuevos, adopción existente y consolidación de onboarding/distribución; incluir alternativa de no construir nuevas capacidades.

## Horizontes orientativos

- Corto: inventario de capacidades y recorridos, identificación de fricciones, selección de un experimento observable.
- Medio: una primera experiencia integral de alto valor, distribución reproducible y validación con consumidores autorizados.
- Largo: mantenimiento evolutivo, expansión selectiva, estabilidad de contratos y criterios verificables para v1.0.0.

Sin fechas, versiones ni Sprint comprometidos.

## Siguiente decisión

Completar el análisis de recorridos y evidencia de uso; contrastar alternativas de mayor valor antes de aprobar un Delivery Scope. Una hipótesis prioritaria es un recorrido de creación nuevo, usando Composition Preview como entrada y experimentando de forma aislada; no presupone que todos los Components sean materializables.

No crear releases, tags, Sprints o milestones ni modificar consumidores. Las pruebas independientes no se declaran realizadas. Las decisiones de producto requieren aceptación expresa; fusionar este baseline documental no equivale a aprobar implementación ni publicación.
