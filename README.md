# Learn Fullstack

A production-oriented Fullstack + AI Engineering knowledge base.

The goal is not to memorize frameworks. The goal is to understand how modern software systems are designed, built, tested, secured, deployed, observed, scaled and evolved.

## The nine-repository system

| Repository | Deep source |
|---|---|
| `learn-js-ts` | JavaScript / TypeScript |
| `learn-frontend` | Browser / frontend / React / Next.js |
| `learn-backend` | Backend / APIs / distributed systems |
| `learn-python` | Python |
| `learn-sql` | SQL / PostgreSQL |
| `learn-docker` | Containers / Docker / Kubernetes operations |
| `learn-ai` | AI / ML / LLM engineering |
| `learn-dsa` | DSA / algorithms — complete |
| `learn-fullstack` | Cross-layer synthesis and production engineering |

The source repositories remain specialized. This repository connects them into one engineering mental model instead of copying nine courses together.

## Canonical navigation

Start here:

1. **[`docs/master-skill-universe.md`](docs/master-skill-universe.md)** — complete 20-section capability universe.
2. **[`docs/skill-map.md`](docs/skill-map.md)** — integrated capability map.
3. **[`docs/final-skill-graph.md`](docs/final-skill-graph.md)** — dependency graph and canonical stack.
4. **[`docs/learning-model.md`](docs/learning-model.md)** — how to study a capability.
5. **[`docs/architecture-decision-guide.md`](docs/architecture-decision-guide.md)** — how to design and defend systems.
6. **[`docs/production-verification.md`](docs/production-verification.md)** — how to prove production competence.
7. **[`docs/completion-ledger.md`](docs/completion-ledger.md)** — final coverage and evidence ledger.
8. **[`docs/interview-map.md`](docs/interview-map.md)** — interview/system-design verification.
9. **[`projects/project-specs.md`](projects/project-specs.md)** — ten production integration projects.
10. **[`projects/build-playbook.md`](projects/build-playbook.md)** — executable project strategy and acceptance evidence.

## Core learning model

```text
Principles
   ↓
Mental models
   ↓
Mechanisms
   ↓
Canonical technologies
   ↓
Production patterns
   ↓
End-to-end projects
   ↓
Failure / security / scale
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
├── foundations/        # programming, CS, security, cross-cutting fundamentals
├── web/                # HTTP, DNS, TLS, networking, browser boundaries
├── frontend/           # frontend integration and patterns
├── backend/            # API/service integration and patterns
├── data/               # data architecture and consistency
├── systems/            # OS, memory, processes, concurrency and performance
├── infrastructure/     # deployment architecture, cloud, IaC and CI/CD
├── production/         # security, testing, observability, reliability and recovery
├── python/             # Python integration path
├── typescript/         # TypeScript integration path
├── architecture/       # system design and architectural trade-offs
├── fullstack-patterns/ # cross-layer application patterns
├── technologies/       # canonical technology notes
├── projects/           # production-oriented integration projects
└── docs/               # master map, graph, audits and verification
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
3. What mechanism actually produces the behavior?
4. What invariants and trade-offs matter?
5. Where is the trust boundary?
6. Which technology implements it?
7. What can fail?
8. How does it behave under scale?
9. How do we secure, test and observe it?
10. What should I build to prove I understand it?

## Production standard

Every serious project is expected to address:

- requirements and non-goals
- architecture and ADRs
- API/event contracts
- schema/migrations
- authentication/authorization
- unit/integration/contract/E2E testing as appropriate
- failure injection
- observability
- limits/timeouts/cancellation
- capacity and cost
- deployment/rollback
- backup/recovery
- operational runbook

The portfolio is not considered complete because the happy path works. The proof is production behavior under failure, attack, scale and change.

## Completion gate

**Understand → Implement → Debug → Measure → Secure → Test → Scale → Operate → Recover → Defend trade-offs.**

## Status

The **knowledge architecture is complete**: the nine-repository ownership model, 20-section skill universe, dependency graph, cross-cutting gap closure, canonical technology model, production layer, project portfolio and interview verification layer are established.

The remaining state is deliberately tracked as **evidence**, not more curriculum. Use `docs/completion-ledger.md` and `projects/build-playbook.md` to turn the knowledge graph into implementation proof. Do not claim mastery until the verification loop has actually been demonstrated.
