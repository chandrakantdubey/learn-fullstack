# Senior/Staff Fullstack + AI Engineering Preparation Plan

This is the planning layer for the nine-repository system. It is derived from the existing **Plan Fullstack AI Preparation** discussion and the nine specialized learning repositories.

## Target

Become capable of operating and interviewing as a Senior/Staff Fullstack + AI Engineer who can design, build, debug and scale production systems across:

```text
Web Platform
  ↓
TypeScript / Python
  ↓
React / Next.js
  ↓
Node.js / Fastify + FastAPI
  ↓
PostgreSQL / Redis
  ↓
Queues / Events / Workers
  ↓
Docker / Kubernetes / AWS / Terraform
  ↓
Observability / Security / Testing
  ↓
ML / LLMs / RAG / Agents / MCP / Inference
```

The goal is a connected engineering mental model, not framework memorization.

## Daily operating model

The agreed hard-grind schedule is:

- **6h learning**
- **6h deliberate practice/building**
- **1h DSA**
- **3 major topics/day**, roughly 2h learning + 2h practice per topic

The work should alternate between understanding and implementation rather than spending entire days reading.

## 12-week structure

### Weeks 1–4 — Foundations

Rebuild the mental model across the stack:

- JavaScript/TypeScript and Python runtime fundamentals
- browser and web platform
- React/Next.js architecture
- HTTP/API design
- backend service architecture
- SQL/PostgreSQL and Redis
- Linux/networking/container fundamentals
- AI/ML foundations
- tokens, embeddings, attention, Transformers and language models

Expected outcome: explain a request from browser through runtime, service and data layers and explain where AI changes the architecture.

### Weeks 5–8 — Production systems

Build integrated applications, not isolated demos.

Every serious project should exercise multiple boundaries:

```text
UI → API → validation → auth → database → cache → async work → AI/search → telemetry
```

Focus on:

- API contracts
- authentication/authorization
- transactions and consistency
- caching/invalidation
- queues/idempotency
- workers and graceful shutdown
- RAG and retrieval authorization
- tools and bounded agent workflows
- evaluation
- observability
- security
- deployment
- failure injection

Use [`docs/production-verification.md`](production-verification.md) as the acceptance standard.

### Weeks 9–12 — Verification and defense

Stop adding breadth unless implementation exposes a real gap.

Focus on:

- DSA and coding
- debugging drills
- system design
- project defense
- architecture trade-offs
- incident/recovery drills
- security scenarios
- load/capacity analysis
- AI evaluation and model/provider trade-offs

## Project strategy

There are ten integration projects in `projects/project-specs.md`. Do not build all ten shallowly.

Build enough projects deeply to cover the complete graph:

1. multi-tenant SaaS
2. realtime collaboration
3. event-driven order platform
4. search platform
5. AI knowledge assistant
6. agentic operations assistant
7. background job platform
8. file/media pipeline
9. high-throughput URL service
10. production AI application platform

Every project should leave behind architecture, contracts, tests, telemetry, failure evidence, deployment/recovery procedures and trade-off documentation.

## Repository mapping

| Area | Source |
|---|---|
| JS/TS | `learn-js-ts` |
| Frontend | `learn-frontend` |
| Backend/distributed | `learn-backend` |
| Python | `learn-python` |
| SQL/PostgreSQL | `learn-sql` |
| Containers/Kubernetes | `learn-docker` |
| AI/LLM | `learn-ai` |
| DSA | `learn-dsa` |
| Cross-layer synthesis | `learn-fullstack` |

## Canonical learning architecture

```text
Principles
 ↓
Mental models
 ↓
Mechanisms
 ↓
Canonical technologies
 ↓
Cross-layer patterns
 ↓
Production systems
 ↓
Failure/security/scale
 ↓
Projects
 ↓
Interview defense
```

Use:

- `docs/master-skill-universe.md` for the complete capability universe.
- `docs/skill-map.md` for capability coverage.
- `docs/final-skill-graph.md` for dependencies.
- `docs/source-map.md` for ownership.
- `docs/architecture-decision-guide.md` for design decisions.
- `docs/production-verification.md` for implementation evidence.
- `docs/interview-map.md` for interview/system-design verification.

## Resource strategy

Use specialized repositories as the primary internal knowledge base, official/free resources for implementation details, and one Udemy anchor per major domain where paid material is useful.

Do not create resource lists for their own sake. Every resource should answer a specific learning or implementation need.

## Completion standard

A capability is complete only when it passes:

**Understand → Implement → Debug → Measure → Secure → Test → Scale → Operate → Recover → Defend trade-offs.**

Reading creates familiarity. Implementation creates competence. Failure testing creates production judgment. Architecture defense demonstrates senior-level understanding.

## Current phase

The repository's knowledge architecture and integration map are complete. The active phase is **evidence generation through projects, failure drills, load tests, recovery exercises and interview defense**.

Do not expand the curriculum unless an implementation or verification exercise exposes a genuine missing capability.
