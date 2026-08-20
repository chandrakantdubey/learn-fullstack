# Learn Fullstack

A production-oriented Fullstack Engineering knowledge base.

The goal is to understand how software systems are designed, built, secured, tested, deployed, observed, and evolved — then learn the frameworks, tools, and libraries that implement those ideas.

## The Learning Model

Every domain is organized in this order:

```text
CONCEPTS
  ↓
FRAMEWORKS
  ↓
TOOLS
  ↓
LIBRARIES
  ↓
PROJECTS
```

### 1. Concepts

The engineering knowledge comes first:

- principles
- mental models
- system behavior
- interfaces and contracts
- trade-offs
- failure modes
- security
- performance
- operational concerns

A framework should be understandable as an implementation of concepts you already know.

### 2. Frameworks

Frameworks provide application structure and conventions.

Examples: React, Next.js, FastAPI, Fastify, Django, Kubernetes.

### 3. Tools

Tools help you build, debug, package, test, deploy, and operate systems.

Examples: Git, curl, Docker, kubectl, Terraform, Helm, GitHub Actions.

### 4. Libraries

Libraries provide focused reusable capabilities inside an application.

Examples: SQLAlchemy, psycopg, Pydantic, Zod, Redis clients, OpenTelemetry SDKs.

## Repository Structure

```text
learn-fullstack/
├── foundations/
│   └── programming/
├── web/
├── frontend/
├── backend/
├── data/
├── systems/
├── infrastructure/
├── production/
├── architecture/
├── python/
├── typescript/
├── projects/
└── docs/
```

Each engineering domain follows the same internal structure:

```text
<domain>/
├── concepts/
├── frameworks/
├── tools/
└── libraries/
```

Not every category needs content immediately. The structure exists to keep responsibilities clear.

## Core Domains

| Domain | What it covers |
| --- | --- |
| `foundations` | programming, CS, engineering fundamentals |
| `web` | HTTP, DNS, TLS, browser/network primitives |
| `frontend` | browser applications, UI architecture, React, web performance |
| `backend` | APIs, services, concurrency, distributed systems, messaging |
| `data` | relational data, PostgreSQL, caching, NoSQL, search, vectors |
| `systems` | Linux, networking, processes, concurrency, performance |
| `infrastructure` | containers, orchestration, cloud, IaC, CI/CD |
| `production` | security, testing, observability, reliability, capacity |
| `architecture` | system design, boundaries, scalability, trade-offs |
| `python` | Python implementation stack for backend and AI engineering |
| `typescript` | TypeScript/JavaScript implementation stack for browser and server |

## Canonical Stack

The default implementation stack is intentionally small:

- **Frontend:** TypeScript, React, Next.js
- **Backend:** Python/FastAPI and TypeScript/Node.js/Fastify
- **Database:** PostgreSQL
- **Cache:** Redis
- **Search:** OpenSearch/Elasticsearch concepts
- **Messaging:** Kafka and cloud queues
- **Containers:** Docker
- **Orchestration:** Kubernetes
- **Cloud:** AWS
- **IaC:** Terraform
- **CI/CD:** GitHub Actions
- **Observability:** OpenTelemetry, Prometheus, Grafana
- **Testing:** pytest, Vitest/Jest, Playwright

## Specialized Repositories

This repository is the integration layer, not a replacement for the deep-dive repositories:

| Repository | Role |
| --- | --- |
| `learn-python` | Python language and ecosystem depth |
| `learn-js-ts` | JavaScript and TypeScript depth |
| `learn-frontend` | frontend/browser/React/Next.js depth |
| `learn-backend` | backend/services/distributed systems depth |
| `learn-sql` | SQL and relational database depth |
| `learn-docker` | Docker/container depth |
| `learn-dsa` | DSA and CS problem-solving depth |
| `learn-ai` | AI/ML/LLM engineering depth |

## Rule

**Do not start with a framework. Start with the engineering problem the framework solves.**
