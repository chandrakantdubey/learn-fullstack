# Senior/Staff Fullstack + AI Engineering Preparation Plan

This plan is the planning layer for `learn-fullstack`. It is derived from the existing **Plan Fullstack AI Preparation** discussion and the nine specialized learning repositories.

## Target

Become capable of interviewing and operating as a Senior/Staff-level Fullstack + AI Engineer who can design, build, debug and scale production systems across:

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

The goal is not framework memorization. The goal is a connected engineering mental model.

## Daily operating model

The agreed hard-grind schedule is:

- **6h learning**
- **6h deliberate practice/building**
- **1h DSA**
- **3 major topics/day**, roughly 2h learning + 2h practice per topic

The work should alternate between understanding and implementation rather than spending entire days reading.

## 12-week structure

### Weeks 1–4 — Foundations and deep learning

Rebuild the mental model across the stack.

**Primary areas**
- JavaScript and TypeScript runtime/language fundamentals
- Python fundamentals and production Python
- browser and web platform
- React and Next.js architecture
- HTTP/API design
- backend service architecture
- SQL/PostgreSQL
- Redis and caching
- Docker/Linux/networking fundamentals
- AI/ML foundations
- tokens, embeddings, attention, transformers and language models

**Expected outcome:** explain how a request moves through a modern application and how the same system changes when AI is introduced.

### Weeks 5–8 — Production projects

Build integrated applications rather than isolated technology demos.

Every serious project should exercise multiple boundaries:

```text
UI → API → validation → auth → database → cache → async work → AI → telemetry
```

Focus on:
- API contracts
- authentication/authorization
- transactions and consistency
- caching and invalidation
- queues and idempotency
- background workers
- RAG ingestion/retrieval/generation
- tool calling and agent workflows
- evaluation
- observability
- security
- deployment
- failure handling

The ten AI projects already present in `learn-ai` become candidates for the AI-heavy project track; they should be strengthened with fullstack concerns rather than copied wholesale.

### Weeks 9–12 — Interview, system design and project defense

Shift from learning new material to proving mastery.

**System design**
- requirements and constraints
- capacity estimation
- API/data contracts
- storage choices
- caching
- async/event-driven design
- consistency
- partitioning/sharding
- reliability and failure domains
- observability
- security
- cost
- multi-region trade-offs
- AI-specific latency, token, retrieval and inference constraints

**Interview engineering**
- DSA daily
- JavaScript/TypeScript internals
- Python internals
- React/Next.js architecture
- backend/API design
- PostgreSQL internals
- distributed systems
- cloud/container fundamentals
- AI/LLM engineering

**Project defense**
For every major project, be able to explain:
1. requirements
2. architecture
3. data model
4. API contracts
5. scaling assumptions
6. failure modes
7. security model
8. observability
9. cost model
10. alternatives and rejected designs
11. production incidents you would expect
12. how you would evolve the system

## Repository-to-plan mapping

| Preparation area | Source |
| --- | --- |
| JS/TS | `learn-js-ts` |
| Frontend | `learn-frontend` |
| Backend/distributed | `learn-backend` |
| Python | `learn-python` |
| SQL/PostgreSQL | `learn-sql` |
| Containers | `learn-docker` |
| AI/LLM | `learn-ai` |
| DSA | `learn-dsa` |
| Integration/project architecture | `learn-fullstack` |

## Learning architecture for this repository

Do not turn the repository into nine copied courses.

Use four layers:

### 1. Concepts

Technology-agnostic mental models:

- HTTP
- rendering
- state
- API contracts
- authentication
- transactions
- caching
- queues
- consistency
- concurrency
- distributed systems
- RAG
- agents
- evaluation

### 2. Technologies

One canonical note per technology under `technologies/`.

Example:

```text
concept: runtime validation
        ↓
technology: Zod
        ↓
frontend: React Hook Form
        ↓
backend: Fastify
        ↓
contract: OpenAPI
```

### 3. Patterns

Cross-layer engineering patterns:

- repository/service boundaries
- API versioning
- idempotency
- outbox/inbox
- retries/backoff
- circuit breaking
- cache-aside
- pagination
- rate limiting
- background jobs
- RAG pipelines
- agent orchestration
- evaluation loops

### 4. Projects

Projects are the integration tests for the skill map. They should progressively combine more layers and force production decisions.

## Resource strategy

The preparation plan uses:

- specialized repositories as the primary internal knowledge base
- official documentation and free practical resources for implementation
- **one Udemy anchor per major domain** where paid material is useful
- free vendor/practical platforms alongside it

Do not create a giant resource list without a reason to use each resource.

## Definition of mastery

A topic is not complete because a note was read.

A topic is complete when the engineer can:

```text
Explain it
   ↓
Implement it
   ↓
Debug it
   ↓
Measure it
   ↓
Secure it
   ↓
Scale it
   ↓
Defend the trade-offs
```

## Next repository work

The next phase is to build the actual integrated skill graph from the nine repositories:

1. inventory source material
2. identify overlap and contradictions
3. map each source topic to a canonical concept
4. map technologies to the single `technologies/` registry
5. identify missing senior/staff-level topics
6. define the final learning progression
7. map projects to capability gaps
8. add interview/system-design coverage
9. add practical exercises for every major capability
10. continuously prune duplicated or low-value material

This is the planning source of truth for the next evolution of `learn-fullstack`.
