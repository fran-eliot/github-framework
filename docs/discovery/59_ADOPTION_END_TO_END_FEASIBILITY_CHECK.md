# 59 — Existing Repository Adoption End-to-End Feasibility Check

| Field | Value |
|---|---|
| Project | GitHub Framework |
| Date | 2026-11-11 |
| Phase | Discovery — bounded workflow check |
| Consumer | [fran-eliot/seniormeet](https://github.com/fran-eliot/seniormeet) |
| Consumer reference | `b84b0de246d459caf594a5cdacbe8fccfa68698a` |
| Template | `TPL-BACKEND v0.1.0` |
| Responsibility | `README-QUICK-START` (`Required`) |
| Assessment status | `In Progress`; only one Responsibility examined |
| Application | Not Started — blocked by an unresolved Decision and unverified runtime facts |
| Integration | Not Started — no verified candidate |
| Consumer mutation | **NONE** |

> This study examines the decision gates between Assessment, Application, and Integration. It does not pretend that Application was completed or that an Integration occurred. It is neither a complete Assessment nor a runtime test of the consumer.

---

## 1. Experimental Question

Can a bounded adoption review identify what is missing before objective Evidence can support a reviewable Application, and stop safely before modifying a repository when the necessary decisions are unavailable?

The goal is to examine the Framework's **hand-offs and safe-stops**, not to satisfy every `TPL-BACKEND` Responsibility or fix SeniorMeet.

The following sources are used:

- [TPL-BACKEND](../../framework/templates/repositories/backend/README.md) and its [metadata](../../framework/templates/repositories/backend/metadata.yml).
- [Assessment Guide](../../framework/adoption/README.md) and [Assessment Template](../../framework/adoption/assessment-template.md).
- [Application Guide](../../framework/adoption/application/README.md) and [Application Record](../../framework/adoption/application/application-template.md).
- [Integration Guide](../../framework/adoption/integration/README.md) and [Integration Record](../../framework/adoption/integration/integration-template.md).
- [Assisted Analysis Guide](../../framework/adoption/assisted-analysis/README.md) and [Evidence Snapshot Template](../../framework/adoption/assisted-analysis/evidence-snapshot-template.md).

## 2. Consumer Baseline and Scope

The SeniorMeet state is fixed at commit:

```text
b84b0de246d459caf594a5cdacbe8fccfa68698a
```

The mutable state of `master` is not used to infer the project's current condition.

The selected Template is `TPL-BACKEND v0.1.0`, with status `Experimental` and recommended minimum maturity `L2`. Its composition includes `README-QUICK-START` among eight Required Components.

The Template describes this Responsibility as enabling a documented first run. Only this Responsibility is evaluated here; neither the Template's overall suitability for SeniorMeet nor the consumer's actual maturity is determined.

## 3. Assessment — Detected Facts and Evidence

| ID | Verified Fact | Evidence |
|---|---|---|
| A-01 | `README.md` contains the name `SENIOR MEET` and the description `Red Social para personas mayores`; it has no installation or startup steps. | [Consumer README](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/README.md) |
| A-02 | `pom.xml` defines a Maven/Spring Boot 3.2.2 project with `java.version=21`. | [pom.xml](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/pom.xml) |
| A-03 | The `Dockerfile` uses `maven:3.8.3-openjdk-17` and contains commented examples of `docker build` / `docker run`. | [Dockerfile](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/Dockerfile) |
| A-04 | The same Dockerfile references `target/backend-0.0.1-SNAPSHOT.jar`, while Maven metadata declares `artifactId=seniormeet` and `version=0.0.1`. | [Dockerfile](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/Dockerfile) and [pom.xml](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/pom.xml) |
| A-05 | `docker-compose.yml` declares `mysql` and `spring-app` services, but the README neither references that file nor explains how to use it. | [docker-compose.yml](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/docker-compose.yml) and [README](https://github.com/fran-eliot/seniormeet/blob/b84b0de246d459caf594a5cdacbe8fccfa68698a/README.md) |

These are static observations. Neither a Maven build nor Docker was executed. The Java-version and artifact-name discrepancies are **risks requiring verification**, not proof that all startup paths fail.

## 4. Assessment — Bounded Evaluation

| Field | Value |
|---|---|
| Responsibility | `README-QUICK-START` |
| Requirement Level | `Required` |
| State | `Partial` — provisional |
| Applicability | `Applicable` |
| Implementation Characteristics | `Distributed`, `Own` (descriptive characteristics) |
| Uncertainty | Working commands, prerequisites, JDK and build-artifact compatibility, reproducible execution |
| Decision Status | `Needs Further Evaluation` |
| Adoption Decision | `—` |

**Evaluation Rationale.** The README does not provide a quick-start procedure. Technical artifacts and comments contain some execution hints, providing fragmented documentation coverage rather than a complete, verified Quick Start. The `Partial` classification is **provisional** under the Responsibility over File principle; human review might instead confirm `Missing` if those hints do not provide usable coverage.

The existence of a `Dockerfile` does not ensure its commands work, and missing README instructions do not automatically authorize an `ADD` or `ADAPT` Decision.

**Outstanding Uncertainty:** identify the supported startup method and verify it in an isolated environment before proposing instructions to the consumer.

### Assessment Decision

This bounded exercise remains `In Progress`. Its Decision Status is `Needs Further Evaluation`. No complete Assessment record covering all 28 Responsibilities has been created, and no human approval is implied.

## 5. Assisted Analysis — Actual Scope

This review collected **read-only** data with references to the consumer's files and pinned commit.

Evidence is recorded in a table of facts and sources, but **there is no claim that an automated Assisted Analysis tool was executed or that a formal Evidence Snapshot was completed**.

Identified limitation: moving from observed facts to working startup instructions requires technical verification and semantic evaluation. The Framework can keep both pending without converting them into automatic conclusions.

## 6. Application — Entry Gate

Application Core requires a **resolved Adoption Decision** for the selected Responsibility and recommends refreshing Evidence before planning operations.

In this case:

```text
README-QUICK-START
    State: Partial (provisional)
    Decision Status: Needs Further Evaluation
    Adoption Decision: —
              ↓
        Application gate
              ↓
       STOP / DEFER
```

Selecting `CREATE` or `MODIFY` is not yet justified.

A possible Application Intent could be considered **only as a hypothesis for future review**: document a reproducible startup process compatible with the actual technical state while preserving the existing README. This is not an approved Change Set.

### Evidence Needed Before Resuming Application

1. Determine the startup process recommended by the SeniorMeet maintainer.
2. Verify Java, database, and tool prerequisites.
3. Check whether the build produces the artifact referenced by Docker.
4. Verify the instructions in an isolated execution without real credentials or data.
5. Complete the Evaluation Rationale and resolve the Adoption Decision through human review.
6. Refresh Evidence against the consumer state that would actually be modified.

No branch was created in SeniorMeet; there is no Application Result, verified candidate, or adoption patch.

## 7. Integration — Entry Gate

Integration Core requires a `VERIFIED` candidate, an Application Outcome, a Candidate Reference, and sufficient verification Evidence.

Here:

```text
Application not started
    ↓
No candidate branch / commit
    ↓
No Application verification
    ↓
Integration: NOT STARTED
```

It would be premature to check mergeability or declare `INTEGRATED`, `VERIFIED STABLE STATE`, or `RELEASE READY`.

This **safe-stop** is a valid experimental outcome: the architecture does not allow Integration to be treated as complete without verifiable input.

## 8. Friction and Findings

| ID | Observation | Implication |
|---|---|---|
| E2E-F01 | The model preserves facts, provisional interpretation, and unresolved decisions separately. | Traceability strength |
| E2E-F02 | Working startup instructions cannot safely be inferred from Docker comments, Maven metadata, or Compose without verification. | Prior technical review needed |
| E2E-F03 | A partial evaluation does not authorize Application. | Entry gate respected; no mutation authorized |
| E2E-F04 | Valid Integration requires a verified candidate. | Entry gate respected |
| E2E-F05 | No empirical evidence yet measures the time or difficulty experienced by external developers. | Do not justify new tooling from this study alone |
| E2E-F06 | Progress from an incomplete Assessment can legitimately end in `STOP / DEFER`. | Research outcome, not a capability failure |

## 9. Result and Next Check

**Observed result:** a bounded read-only review was conducted against a real consumer; a provisional evaluation was recorded for one Required Responsibility; and the Application and Integration gates were considered conceptually. Both **stop the workflow because required preconditions are missing**.

An end-to-end Adoption involving real changes, a candidate, and stable-state verification **was not completed** in this exercise. Nor does this demonstrate that any user can follow the workflow independently.

A useful future experiment would require a human-reviewed `Resolved` Decision and an Application sufficiently small and safe to assess **plan → isolated change → verify → integration review**. The consumer mutation boundary and available checks would need explicit agreement first.

No Sprint, milestone, version, or Delivery Scope is opened. SeniorMeet remains unchanged.

## 10. Conclusion

The study finds operational value in the Adoption model's safe-stops and traceability, but provides no new evidence of end-to-end efficiency.

The priority question is no longer whether to write another general-purpose Guide, but **how to obtain a genuinely verifiable Application case**, without turning a provisional Decision into automation or forcing a consumer modification.
