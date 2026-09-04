# Deep Source Ingestion Matrix

This document is the working contract for consolidating the eight non-DSA repositories into `learn-fullstack`.

The specialized repositories remain the deep reference implementations. `learn-fullstack` owns the connections, invariants, production behavior, architecture and gaps that span multiple domains.

## 1. Ingestion order

```text
learn-js-ts
    ↓
learn-python
    ↓
learn-frontend
    ↓
learn-backend
    ↓
learn-sql
    ↓
learn-docker
    ↓
learn-ai
    ↓
FULLSTACK SYNTHESIS
    ↓
projects + interview + production
```

The order is deliberate: language/runtime mental models precede browser and service behavior; service behavior precedes data and deployment; AI is integrated after the underlying application system is understood.

## 2. Source → synthesis rules

| Source | Deep material to preserve there | Fullstack synthesis | Avoid copying |
|---|---|---|---|
| `learn-js-ts` | JS/TS language, runtime, modules, async, types, tooling | browser/runtime boundaries, shared type contracts, concurrency implications | full language reference |
| `learn-python` | Python language, stdlib, async, packaging, ecosystem | Python service architecture, Python↔TS trade-offs, AI/backend integration | Python tutorial duplication |
| `learn-frontend` | browser platform, HTML/CSS, React, Next.js, frontend tooling | frontend↔API contracts, rendering/data boundaries, security, performance and end-to-end state flow | framework API reference |
| `learn-backend` | APIs, services, auth, jobs, messaging, distributed systems | cross-layer request lifecycle, reliability, domain/data boundaries and architecture | another backend course |
| `learn-sql` | SQL, PostgreSQL, relational internals and query behavior | application data lifecycle, transaction boundaries, consistency, cache/search integration | SQL syntax dump |
| `learn-docker` | images, containers, Compose, registries, deployment mechanics | application→container→cloud path, release strategy, runtime configuration and failure recovery | Docker command catalog |
| `learn-ai` | ML/DL, transformers, LLMs, RAG, agents, inference, evaluation | AI feature architecture, trust boundaries, streaming, cost/latency, observability and product integration | AI framework encyclopedia |

## 3. What every source must contribute

For each source, extract four layers:

1. **Fundamentals** — concepts and mental models that explain the domain.
2. **Mechanisms** — how the runtime/framework/database/container/model actually behaves.
3. **Production** — security, failure modes, testing, observability, performance and operations.
4. **Integration points** — where the domain crosses into another repository.

A topic moves into `learn-fullstack` when it is language/framework agnostic, shared by several domains, or primarily about a cross-layer decision.

## 4. Current high-value findings

### JavaScript / TypeScript

The source domain should remain the authority for language depth. Fullstack needs only the consequences that affect application architecture: runtime vs compile-time guarantees, serialization boundaries, async concurrency, cancellation, streams, memory/resource behavior and shared contracts.

### Python

The source covers a very broad progression from fundamentals through async, concurrency, networking, databases, FastAPI, testing, security, production and AI. The important synthesis is not another Python roadmap; it is choosing Python where it improves backend/AI workloads and making its runtime behavior explicit alongside Node.js. The source itself already includes bytes/Unicode, regex, asyncio, concurrency, SQLAlchemy, FastAPI and AI tooling. fileciteturn388file0L2-L2

### Frontend

The synthesis target is the browser-to-service boundary: rendering model, browser security, client/server state, API contracts, loading/error behavior, streaming and performance. Framework-specific mastery stays in the frontend repository.

### Backend

The backend source is broad enough to cover HTTP, APIs, databases, auth, caching, jobs, messaging, WebSockets, system design, DevOps and AI backend work. The fullstack layer should therefore emphasize the decisions between these pieces: transaction boundaries, sync vs async, idempotency, retries, deadlines, events and end-to-end observability. The source explicitly frames production REST APIs, PostgreSQL/Redis, auth, Kafka/queues, system design, Docker/cloud and AI/LLM backend work as one progression. fileciteturn396file0L2-L2

### SQL / PostgreSQL

The source has a strong SQL-first progression and explicitly separates ANSI SQL practice from PostgreSQL production features. Fullstack should connect SQL semantics to application behavior: constraints, transactions, isolation, indexes, query plans, migrations, pooling, caching, search and consistency. fileciteturn389file0L2-L2

### Docker

The source already spans setup, images, volumes, networking, Compose, secrets, logs, registries, multi-stage builds, security, performance, debugging, CI/CD, cloud, Kubernetes, AI containers, microservices and full-stack deployment. Fullstack should use it as the deployment mechanism, not duplicate the tutorial. fileciteturn390file0L2-L2

### AI

The source has broad coverage from AI/ML foundations through transformers, foundation models, generative AI, RAG, tool use, agents, training, inference, evaluation, serving, observability and safety. Fullstack should focus on integrating those capabilities into a product with deterministic authorization, validated outputs, retrieval ACLs, streaming, fallbacks, cost controls and evaluation. fileciteturn391file0L2-L2

## 5. Consolidation decisions

### Keep specialized

- language syntax and language-specific internals
- framework APIs and framework-specific tutorials
- SQL syntax drills
- Docker command/reference material
- model architecture deep dives and ML mathematics
- DSA problem sets

### Move / synthesize in Fullstack

- regex and text-processing mental models
- bytes, encoding and serialization
- time, clocks and randomness
- cryptography and trust boundaries
- HTTP/DNS/TLS/networking semantics
- browser trust boundaries
- API contracts and schema evolution
- auth/authz architecture
- idempotency, retries, deadlines and cancellation
- caching and rate limiting
- messaging semantics and consistency
- concurrency/resource lifecycle
- observability/SLOs/capacity/incident response
- frontend/backend architecture
- AI application architecture
- production-grade end-to-end projects
- interview and system-design verification

## 6. Definition of done for ingestion

A source is considered deeply ingested only when:

- its major concepts are represented in the integrated skill graph;
- duplicates are removed or explicitly delegated to the source repository;
- cross-domain dependencies are documented;
- canonical technologies have one home;
- production concerns are connected to the relevant concepts;
- at least one project exercises the important cross-domain paths;
- interview/system-design prompts can verify the resulting skill;
- the learner can trace a real request from browser to runtime, service, data, infrastructure and (when applicable) AI.

## 7. Final architecture

```text
                 SPECIALIZED KNOWLEDGE
  JS/TS · Python · Frontend · Backend · SQL · Docker · AI
                         │
                         ▼
              FULLSTACK SYNTHESIS LAYER
  foundations · web · systems · architecture · production
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        INTEGRATION PROJECTS   INTERVIEW DEFENSE
              │                     │
              └──────────┬──────────┘
                         ▼
                 PRODUCTION ENGINEER
```
