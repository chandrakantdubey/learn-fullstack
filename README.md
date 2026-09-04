# Learn Fullstack

A production-oriented Fullstack + AI Engineering knowledge base.

The goal is not to memorize frameworks. The goal is to understand how modern software systems are designed, built, tested, secured, deployed, observed, scaled and evolved.

## The nine-repository system

`learn-fullstack` is the integration layer across the specialized repositories:

| Repository | Deep source |
|---|---|
| `learn-js-ts` | JavaScript / TypeScript |
| `learn-frontend` | Browser / frontend / React / Next.js |
| `learn-backend` | Backend / APIs / services / distributed systems |
| `learn-python` | Python |
| `learn-sql` | SQL / PostgreSQL |
| `learn-docker` | Containers / Docker |
| `learn-ai` | AI / ML / LLM engineering |
| `learn-dsa` | DSA / algorithms — complete |
| `learn-fullstack` | Cross-layer synthesis and production engineering |

The source repositories remain specialized. This repository connects them into one engineering mental model instead of copying nine courses into one place.

## Core learning model

```text
Principles
   ↓
Mental models
   ↓
Systems
   ↓
Concepts
   ↓
Canonical technologies
   ↓
Production patterns
   ↓
End-to-end projects
   ↓
Interview defense
```

## Fullstack engineer model

```text
                         PRODUCT / SYSTEM
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
       FRONTEND              BACKEND                DATA
          │                     │                     │
    Browser / UI          APIs / Services       SQL / NoSQL
    React / Next          Async / Workers       Cache / Search
    State / UX            Domain Logic          Queues / Events
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                │
                    SYSTEMS + NETWORKING
                                │
                  Linux / OS / DNS / TLS / HTTP
                                │
                       INFRASTRUCTURE
                                │
                 Docker / Kubernetes / Cloud
                         Terraform / CI/CD
                                │
                    PRODUCTION ENGINEERING
                                │
          Security / Testing / Observability / SRE
                                │
                              AI
                                │
            ML / LLMs / RAG / Agents / Inference
```

## Repository structure

```text
learn-fullstack/
├── foundations/       # programming, CS, security, cross-cutting fundamentals
├── web/               # HTTP, DNS, TLS, networking, browser boundaries
├── frontend/          # frontend architecture and patterns
├── backend/           # APIs, services, async and backend patterns
├── data/              # SQL, PostgreSQL, Redis, search and vectors
├── systems/           # OS, memory, processes, concurrency and performance
├── infrastructure/    # Docker, Kubernetes, cloud, IaC and CI/CD
├── production/        # security, testing, observability and reliability
├── python/            # Python integration path
├── typescript/        # TypeScript integration path
├── architecture/      # system design and architectural trade-offs
├── fullstack-patterns/ # cross-layer application patterns
├── technologies/      # one canonical note per technology
├── projects/          # production-oriented integration projects
└── docs/              # skill map, source map, module map and gap tracking
```

## Cross-cutting knowledge owned here

Some capabilities do not belong exclusively to frontend, backend, Python, SQL, Docker or AI. They are intentionally first-class Fullstack material:

- regex and text processing
- Unicode, encoding and serialization
- cryptography and security mental models
- DNS, TCP/UDP/QUIC and TLS
- HTTP semantics and protocol behavior
- browser trust boundaries
- API contracts and schema evolution
- authentication and authorization architecture
- idempotency, retries, timeouts and cancellation
- caching and rate limiting
- queues, events and distributed failure models
- concurrency, processes, memory and resource lifecycles
- observability, SLOs, capacity and incident response
- architecture and system-design trade-offs
- AI integration, evaluation, security and cost

## Canonical technology rule

One technology gets one canonical note under `technologies/` even when it is used in several layers. Zod is the canonical example: `technologies/shared/zod.md` is the single source instead of separate frontend/backend copies.

Concepts remain separate from technology notes.

## Learning style

This is deliberately **not a conventional course**. A strong topic should answer:

1. What problem does this solve?
2. What mental model explains it?
3. What invariants and trade-offs matter?
4. Where is the trust boundary?
5. How does it work internally?
6. Which technology implements it?
7. What can fail?
8. How does it behave under scale?
9. How do we secure, test and observe it?
10. What should I build to prove I understand it?

## Deep ingestion

The eight non-DSA repositories are analyzed as source material, then consolidated by ownership and dependency rather than copied wholesale.

- [`docs/source-ingestion.md`](docs/source-ingestion.md) — source-by-source ingestion and consolidation matrix
- [`docs/skill-map.md`](docs/skill-map.md) — complete capability map
- [`docs/module-map.md`](docs/module-map.md) — nine-source ownership model
- [`docs/source-map.md`](docs/source-map.md) — what belongs where
- [`docs/cross-cutting-gaps.md`](docs/cross-cutting-gaps.md) — missing cross-layer knowledge
- [`docs/integration-status.md`](docs/integration-status.md) — integration status and quality bar
- [`docs/interview-map.md`](docs/interview-map.md) — interview and system-design verification
- [`technologies/README.md`](technologies/README.md) — canonical technology notes
- [`technologies/registry.md`](technologies/registry.md) — technology inventory
- [`projects/README.md`](projects/README.md) — production project portfolio
- [`projects/project-specs.md`](projects/project-specs.md) — detailed project acceptance criteria

## Status

The integration architecture is established and the first cross-cutting gaps are implemented. The current pass is deep ingestion of the eight non-DSA source repositories, followed by strengthening canonical technology notes, wiring source references into the skill graph, and building the project/interview/production verification layer.

The rule remains: specialized repositories own depth; `learn-fullstack` owns synthesis, cross-layer behavior and production judgment. `learn-dsa` remains complete.
