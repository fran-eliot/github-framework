# Only Film — Demo, author and highlights: human review batch

## Review scope and constraints

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Pinned consumer reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Framework Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-DEMO`, `README-AUTHOR`, `README-HIGHLIGHTS` |
| Review status | **Three reviewer-facing proposals, no maintainer State/Applicability approval in this packet** |
| Previous formal approvals | `20/28` |
| Assessment status | `In Progress` |
| Resolved Adoption Decisions | `0` |
| Consumer mutation | `NONE` |

This review is limited to content directly fetched from Only Film's README at the pinned SHA, the existing Framework semantic reviews and the `README-AUTHOR` Component. The existing Framework review records are explicitly distinguished from fresh independent checks. This packet does not inspect the screenshot image pixels, execute Compose or deploy a hosted demo, establish intellectual-property rights, or authorize any implementation.

## Proposed evaluations

| Responsibility | Currently proposed State / Applicability | Recommended reviewer candidate | Documentary interpretation |
| --- | --- | --- | --- |
| `README-DEMO` | `Partial / Applicable` | **Retain `Partial / Applicable`** | Four inline screenshot references and a local startup route make the application visible; freshness, visual fidelity and a verified runnable demonstration remain open |
| `README-AUTHOR` | `Partial / Applicable` | **Consider `Satisfied / Applicable`** | The existing origin and credits section distinguishes the academic team from subsequent maintenance, meeting the Framework Component's identification purpose |
| `README-HIGHLIGHTS` | `Partial / Applicable` | **Consider `Satisfied / Applicable`** | Differentiating technical features are already communicated through Features and Security without a dedicated Highlights heading |

These are **documentation** judgments. `Satisfied` would not verify screenshot accuracy, ownership, complete security properties, or operational success.

## 1. README-DEMO — retain `Partial / Applicable` as a proposal

### Direct pinned evidence

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) contains a `Capturas de la aplicación` section with four Markdown image references: `docs/screenshots/cartelera.png`, `docs/screenshots/pelicula.png`, `docs/screenshots/sesion.png`, and `docs/screenshots/compra-qr.png`. They illustrate the movie listing, movie details, seat selection and QR ticket at the level of their **captions and reference paths**.
- The README includes a local Docker Compose onboarding command and `http://localhost:8080/movies`; this is a **localhost** address and cannot be called a public hosted demo.
- The existing [Optional showcase semantic review](only-film-optional-showcase-semantic-review.md) reports earlier confirmation that screenshot files were present and records an unverified Compose smoke-execution gap at the pinned SHA. This new review did **not** independently open or inspect the screenshot image pixels or rerun the image/path inventory.
- The earlier [Compose evidence gap](only-film-compose-evidence-gap.md) distinguishes a successful JAR-on-PostgreSQL CI path from direct execution of the complete Compose stack. Missing verified Compose evidence is **not** evidence of failure.

### Evaluation and choice

`Partial / Applicable` is a defensible conservative **review recommendation** where demo communication is interpreted as showing both appearance **and** a verified usable demonstration path. The four references already give readers visual entry points; neither a public demo nor a video is automatically necessary for this Optional Responsibility. The maintainer may select `Satisfied / Applicable` if clearly labeled screenshots suffice for this portfolio audience, while **retaining that visual fidelity, screenshot age and working Compose startup have not been independently verified**.

**Open gate:** whether the image content is sufficiently current/representative, whether demo-data prerequisites are clear, and what audience-specific demonstration threshold applies. No code, screenshot replacement, Docker execution, demo deployment or secret change is authorized.

## 2. README-AUTHOR — `Satisfied / Applicable` candidate

### Direct pinned evidence

- The [pinned README's `Origen, créditos y evolución`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) identifies the project as derived from [`certidevs/g1_testing`](https://github.com/certidevs/g1_testing), links **four named academic collaborators**, and describes technical evolution in `fran-eliot/only_film`. Its wording explicitly distinguishes **original shared authorship** from later maintenance.
- The [Framework README-AUTHOR Component](../../components/readme/author/README.md) calls for information about an author or responsible team; name, GitHub, LinkedIn or website are possible fields. It does not prescribe a separate heading or demand every possible social link.
- The existing [Optional governance semantic review](only-film-optional-governance-semantic-review.md) already recognized meaningful author/team coverage but kept its earlier `Partial` as an editorial hypothesis pending reviewer acceptance. This batch revisits the **documentary threshold**, not all project history.

### Evaluation and choice

The existing, explicitly balanced attribution fulfills a plausible README-level team/author identification requirement. `Satisfied / Applicable` is a reasonable **candidate** for maintainer review, without adding a redundant Author section or implying one individual created every academic contribution. `Partial / Applicable` could be retained if the maintainer identifies a **specific** missing ownership/contact distinction that is material to readers.

**Open gate:** whether the four listed academic collaborators and subsequent maintenance description are sufficiently accurate and complete for the audience. **Not established:** copyright ownership, license grants, all individuals' contribution-by-contribution histories, or exclusive attribution rights. No changes to credits or license language are authorized.

## 3. README-HIGHLIGHTS — `Satisfied / Applicable` candidate

### Direct pinned evidence

- The README's [`Funcionalidades` and `Seguridad y límites actuales`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) describe ticket availability protection through transactional and locked operations, role-based access, review/ticket authorization, image-content validation, and PostgreSQL/Flyway support.
- The README explicitly qualifies checkout as a **demonstration flow without a real payment gateway** and disclaims a complete security audit or production-hardened deployment. These qualifications must travel with any highlights.
- The existing [Optional showcase semantic review](only-film-optional-showcase-semantic-review.md) proposed `Partial` pending an editorial judgment about whether a separate Highlights block would materially clarify the portfolio; it did not identify the absence of a literal `Highlights` heading as a functional defect.
- Previous [Surefire/Sonar log evidence](only-film-verified-surefire-sonar-logs.md) reports a successful **selected H2 regression** at the pinned SHA; this is supporting bounded test evidence, **not a fresh verification** of all showcase claims or a certification of feature/security completeness.

### Evaluation and choice

The distinctive capabilities are already discoverable in coherent existing sections. `Satisfied / Applicable` is a reasonable **candidate** if the maintainer considers an explicit independent `Highlights` header unnecessary duplication. `Partial / Applicable` remains defensible if a genuinely useful short technical differentiation section is missing for the target reader; that is an editorial question, not a proven deficiency.

**Open gate:** audience clarity, factual claim qualifications and whether a standalone highlights block adds value beyond Features. No new marketing promises, technology claims, security guarantees or README edits are authorized.

## Formal approval gate

The maintainer may separately approve or revise each **State** and **Applicability**:

| Responsibility | Default candidate | Reasonable alternative |
| --- | --- | --- |
| `README-DEMO` | `Partial / Applicable` | `Satisfied / Applicable` if screenshot-based demo suffices without claiming an executed/hosted demo |
| `README-AUTHOR` | `Satisfied / Applicable` | `Partial / Applicable` if a material documentary attribution gap is identified |
| `README-HIGHLIGHTS` | `Satisfied / Applicable` | `Partial / Applicable` if audience-specific clarity genuinely requires a separate summary |

**Merging this review packet does not approve any of these values**. The Assessment must remain `In Progress` until all formal review criteria are met, and every Adoption Decision stays `—` with `Decision Status: Needs Further Evaluation` until separately selected. The pinned source is `28d75a50e0a178954dd46acc23300d9dd327843c`; the review date and any eventual sign-off date must be separately recorded. Only Film remains read-only.
