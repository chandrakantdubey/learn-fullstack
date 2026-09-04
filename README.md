# Learn Fullstack

A production-oriented Fullstack + AI Engineering knowledge base.

The goal is not to memorize frameworks. The goal is to understand how modern software systems are designed, built, tested, secured, deployed, observed, scaled and evolved.

## The nine-repository system

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

The source repositories remain specialized. This repository connects them into one engineering mental model instead of copying nine courses together.

## Canonical master checklist

**[`docs/master-skill-universe.md`](docs/master-skill-universe.md)** is the single 20-section checklist. It is the authoritative placement map for the complete skill universe.

`MASTER-COVERAGE.md` and each specialized repository's `MASTER-COVERAGE.md` make the ownership explicit at repository level.

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
├── projects/           # production-oriented integration projects
└── docs/               # master map, skill graph, source map, audits and verification
```

## Cross-cutting knowledge owned here

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

## Verification and integration

- [`docs/master-skill-universe.md`](docs/master-skill-universe.md) — canonical 20-section master checklist
- [`docs/coverage-matrix.md`](docs/coverage-matrix.md) — section-by-section ownership
- [`docs/final-skill-graph.md`](docs/final-skill-graph.md) — dependency graph
- [`docs/source-ingestion.md`](docs/source-ingestion.md) — source consolidation rules
- [`docs/module-map.md`](docs/module-map.md) — module ownership
- [`docs/source-map.md`](docs/source-map.md) — what belongs where
- [`docs/cross-cutting-gaps.md`](docs/cross-cutting-gaps.md) — cross-layer gaps
- [`docs/integration-status.md`](docs/integration-status.md) — integration status
- [`docs/interview-map.md`](docs/interview-map.md) — interview/system-design verification
- [`technologies/README.md`](technologies/README.md) — canonical technology notes
- [`technologies/registry.md`](technologies/registry.md) — technology inventory
- [`projects/README.md`](projects/README.md) — production project portfolio
- [`projects/project-specs.md`](projects/project-specs.md) — project acceptance criteria

## Status

The nine-repository integration and master ownership map are now established. Specialized repositories own their domain depth; `learn-fullstack` owns cross-layer synthesis, production engineering, architecture, projects and verification.
