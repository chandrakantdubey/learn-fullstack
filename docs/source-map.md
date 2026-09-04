# Source Map

`learn-fullstack` is the integration layer for the nine learning repositories. The specialized repositories remain the deep sources of truth; this repository turns their knowledge into one coherent Fullstack + AI Engineering skill system.

## Nine source repositories

| Source repository | Primary material | Integration into `learn-fullstack` |
| --- | --- | --- |
| `learn-js-ts` | JavaScript/TypeScript language and runtime | Programming foundations, JS runtime, TypeScript application engineering |
| `learn-frontend` | Browser, HTML/CSS, React, frontend architecture | Web platform, UI architecture, rendering, performance, accessibility |
| `learn-backend` | Backend engineering, APIs, services, distributed systems | HTTP/API design, service architecture, async systems, reliability |
| `learn-python` | Python language, stdlib, async, packaging, production | Python engineering and the Python backend/AI path |
| `learn-sql` | SQL and PostgreSQL | Relational modeling, SQL, transactions, indexing, query planning |
| `learn-docker` | Containers and Docker operations | Container fundamentals, image engineering, networking and deployment |
| `learn-dsa` | Data structures and algorithms | Interview problem solving and engineering complexity judgment |
| `learn-ai` | AI/ML/LLM engineering | AI engineering foundations, LLM applications, RAG, agents, inference and evaluation |
| `learn-fullstack` | Existing integrated material | Canonical cross-layer architecture, stack decisions, projects and preparation plan |

## Integration rules

### 1. Principles before products

Teach the underlying system before the framework:

- HTTP before FastAPI/Fastify
- SQL before SQLAlchemy/ORMs
- browser architecture before React
- containers before Kubernetes
- Linux/networking before cloud abstractions
- distributed-systems principles before Kafka/SQS
- model/inference fundamentals before LLM frameworks

### 2. One concept, one canonical explanation

If several source repositories explain the same concept, consolidate the strongest explanation here. Do not create competing copies.

### 3. Specialized depth stays specialized

Do not blindly copy entire source repositories. Preserve them as deep references and pull the material that is necessary to make a fullstack engineer understand how layers connect.

### 4. One technology, one canonical technology note

Technology-specific material belongs under `technologies/`. A technology used by multiple layers gets one canonical file. For example, Zod lives in `technologies/shared/zod.md`, not separate frontend and backend copies.

### 5. Production context is mandatory

Important topics should eventually cover failure modes, security, observability, performance, scalability, cost, deployment and testing.

### 6. Projects integrate layers

Prefer projects that force boundaries to work together:

```text
Browser → API → Database → Cache → Queue → Worker → AI → Observability
```

## Planned ingestion order

1. Programming: `learn-js-ts`, `learn-python`
2. Web platform and frontend: `learn-frontend`
3. Backend and distributed systems: `learn-backend`
4. Data: `learn-sql`
5. Containers/infrastructure: `learn-docker`
6. AI engineering: `learn-ai`
7. Interview problem solving: `learn-dsa`
8. Cross-layer synthesis: existing `learn-fullstack` material

The result should be a coherent skill graph, not nine pasted courses.
