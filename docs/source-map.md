# Source Map

`learn-fullstack` is the integration layer for the nine-repository learning system. Specialized repositories remain the deep sources of truth. This repository connects them, removes duplication, fills cross-domain gaps and turns the knowledge into production-oriented engineering capability.

## Nine repositories

| Source | Owns | Fullstack responsibility |
| --- | --- | --- |
| `learn-js-ts` | JavaScript and TypeScript language/runtime | shared programming mental models and application-level TS/JS integration |
| `learn-frontend` | browser, HTML/CSS, React, Next.js | end-to-end browser/API architecture, frontend/backend boundaries |
| `learn-backend` | APIs, services, backend architecture, distributed systems | cross-layer service/data/reliability design |
| `learn-python` | Python language/runtime/ecosystem | Python implementation path and comparison with TypeScript |
| `learn-sql` | SQL/PostgreSQL | application data lifecycle and consistency decisions |
| `learn-docker` | Docker/container operations | application-to-container-to-cloud deployment model |
| `learn-ai` | ML, deep learning, LLMs, RAG, agents, inference | AI features integrated into fullstack products |
| `learn-dsa` | algorithms/data structures/interview problem solving | complexity judgment and interview preparation; **complete** |
| `learn-fullstack` | integration layer | cross-cutting engineering, architecture, production, projects and skill synthesis |

## What belongs in Fullstack

A concept belongs here when it is either:

1. language/framework agnostic,
2. shared by several layers,
3. a connection between specialized domains, or
4. required for production engineering but not owned deeply by a source repository.

Examples: regex, cryptography, encoding, HTTP semantics, DNS/TLS, browser trust boundaries, API contracts, idempotency, retries, timeouts, concurrency, capacity planning, SLOs and system design.

## What stays in specialized repositories

Do not duplicate deep implementation material merely because Fullstack uses the technology. Examples:

- detailed TypeScript language study → `learn-js-ts`
- detailed React study → `learn-frontend`
- detailed SQL exercises → `learn-sql`
- detailed Docker command/reference material → `learn-docker`
- detailed transformer/LLM foundations → `learn-ai`
- DSA problem sets → `learn-dsa`

Fullstack should link/reference those subjects and teach how they interact.

## Integration rules

### Principles before products

- HTTP before FastAPI/Fastify.
- SQL before ORMs.
- browser architecture before React.
- containers before Kubernetes.
- Linux/networking before cloud abstractions.
- distributed-system failure models before Kafka/SQS.
- model/inference fundamentals before LLM frameworks.

### One concept, one canonical explanation

If multiple sources explain the same concept, keep one authoritative integrated explanation and reference the specialized source for depth.

### One technology, one canonical note

Technology-specific material lives under `technologies/`. A technology used in several layers gets one canonical note. Zod is the canonical example: `technologies/shared/zod.md` rather than frontend/backend copies.

### Production context is mandatory

Important capabilities should eventually cover failure modes, security, observability, performance, scale, cost, testing and operations.

### Projects are the integration test

The strongest projects cross several boundaries:

```text
Browser
  ↓
API / Auth
  ↓
Domain logic
  ↓
PostgreSQL + Redis
  ↓
Queue / Event
  ↓
Worker
  ↓
AI / Search
  ↓
Observability / Security
  ↓
Deployment
```

## Current execution order

1. Programming foundations: JS/TS + Python.
2. Web platform and frontend.
3. Backend/API engineering.
4. SQL/data.
5. Docker/infrastructure.
6. AI engineering.
7. DSA verification — complete.
8. Cross-layer architecture, security, reliability and projects.

See [`docs/module-map.md`](module-map.md), [`docs/skill-map.md`](skill-map.md), and [`docs/cross-cutting-gaps.md`](cross-cutting-gaps.md).
