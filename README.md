# Learn Fullstack

A production-oriented Fullstack Engineering knowledge base.

The goal is not to memorize frameworks. The goal is to understand how modern software systems are designed, built, tested, secured, deployed, observed, and evolved.

## What This Repository Is

`learn-fullstack` is the integration layer across the existing specialized learning repositories:

| Repository | Role |
| --- | --- |
| `learn-python` | Python language and ecosystem depth |
| `learn-js-ts` | JavaScript and TypeScript depth |
| `learn-frontend` | Frontend, browser, React, and Next.js depth |
| `learn-backend` | Backend, APIs, distributed systems, and services depth |
| `learn-sql` | SQL and database depth |
| `learn-docker` | Containerization and deployment depth |
| `learn-ai` | AI/ML/LLM engineering depth |
| `learn-dsa` | Data structures and algorithms depth |

This repository connects those subjects into one engineering mental model.

## Core Principle

Learn in this order:

**Principles → Mental Models → Systems → Technologies → Tools/Libraries → Production Patterns → Projects**

A framework is never the starting point.

## The Fullstack Engineer Model

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
                         SYSTEMS FOUNDATION
                                │
                   Linux / Networking / OS
                                │
                         INFRASTRUCTURE
                                │
                 Docker / Kubernetes / Cloud
                         Terraform / CI/CD
                                │
                       PRODUCTION ENGINEERING
                                │
              Security / Testing / Observability
                       Reliability / Performance
                                │
                              AI
                                │
              ML / LLMs / RAG / Agents / Serving
```

## Repository Structure

```text
learn-fullstack/
├── foundations/       # programming, CS, web, networking, Linux
├── web/               # HTTP, DNS, TLS, browser and internet fundamentals
├── frontend/          # frontend engineering and architecture
├── backend/           # APIs, services, async, distributed systems
├── data/              # SQL, PostgreSQL, Redis, search, NoSQL, vectors
├── systems/           # OS, networking, concurrency, performance
├── infrastructure/    # Docker, Kubernetes, cloud, Terraform, CI/CD
├── production/        # security, testing, observability, reliability
├── python/            # Python as the primary backend/AI implementation stack
├── typescript/        # TypeScript as the primary browser/server implementation stack
├── architecture/      # system design and architectural trade-offs
├── fullstack-patterns/ # cross-layer patterns used in real applications
├── projects/          # production-oriented end-to-end projects
└── docs/              # curriculum, source map, decisions, glossary
```

## Canonical Stacks

### Primary

- **Frontend:** TypeScript, React, Next.js
- **Backend:** Python/FastAPI and TypeScript/Node.js
- **Database:** PostgreSQL
- **Cache:** Redis
- **Search:** OpenSearch/Elasticsearch concepts
- **Messaging:** Kafka and cloud queues
- **Containers:** Docker
- **Orchestration:** Kubernetes
- **Cloud:** AWS
- **Infrastructure:** Terraform
- **CI/CD:** GitHub Actions
- **Observability:** OpenTelemetry, Prometheus, Grafana
- **Testing:** pytest, Vitest/Jest, Playwright

### AI extension

- PyTorch and scikit-learn foundations
- Transformers and model APIs
- Embeddings and vector search
- RAG
- Evaluation
- Agents/workflows
- Model serving and inference infrastructure

## Learning Style

This is deliberately **not a conventional course**.

A topic should answer:

1. What problem does this solve?
2. What mental model explains it?
3. What are the important invariants and trade-offs?
4. How is it implemented?
5. What can fail in production?
6. Which technology/tool implements it?
7. How do Python and TypeScript differ in implementation?
8. Where does it fit into an end-to-end system?
9. What should I build to prove I understand it?

## Source Repositories

Existing material is treated as source material, not copied blindly. The consolidation rules are documented in [`docs/source-map.md`](docs/source-map.md).

## Status

Initial repository architecture. Content is being consolidated and rewritten around engineering capabilities rather than isolated technologies.
