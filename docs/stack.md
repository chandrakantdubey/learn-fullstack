# Canonical Stack

The stack is intentionally opinionated. Alternatives are introduced only when they illuminate a meaningful engineering trade-off.

## Languages

| Role | Default | Why |
| --- | --- | --- |
| Browser + typed application code | TypeScript | Strong web ecosystem and end-to-end typing |
| Backend + AI | Python | Excellent ecosystem for APIs, data, ML, and AI |
| Systems exposure | C/C++ concepts | Understand memory, compilation, and low-level behavior without making it a primary application language |

## Web / Frontend

| Layer | Default |
| --- | --- |
| HTML | HTML5 |
| CSS | CSS + Tailwind CSS where appropriate |
| UI | React |
| Fullstack React framework | Next.js |
| Component primitives | Radix UI + shadcn/ui |
| Client state | Zustand; Redux Toolkit when complexity justifies it |
| Server state | TanStack Query |
| Forms | React Hook Form |
| Runtime validation | **Zod** |
| Browser testing | Playwright |
| Unit/component testing | Vitest + Testing Library |
| Build tooling | Vite where a standalone frontend is appropriate; Next.js tooling otherwise |
| Package manager | pnpm |

## TypeScript Backend

| Layer | Default |
| --- | --- |
| Runtime | Node.js |
| HTTP service | Fastify |
| Runtime validation | **Zod** |
| API contract | OpenAPI where REST is used |
| HTTP client | native `fetch` |
| PostgreSQL | `pg` |
| SQL / ORM | Drizzle or Prisma when ORM features are justified |
| Cache | Redis |
| Background jobs | BullMQ or a focused worker |
| Logging | Pino |

## Python Backend / AI

| Layer | Default |
| --- | --- |
| API | FastAPI |
| Validation | Pydantic |
| HTTP client | httpx |
| Database | SQLAlchemy + psycopg |
| Migrations | Alembic |
| Background work | Celery or a focused worker |
| Testing | pytest |
| AI / ML | PyTorch + scikit-learn |

## Validation rule

Zod and Pydantic are runtime boundary tools, not substitutes for domain modeling.

```text
untrusted input
      ↓
Zod / Pydantic
      ↓
validated command
      ↓
authentication / authorization
      ↓
domain/application logic
      ↓
data / external systems
```

See:

- `frontend/concepts/runtime-validation.md`
- `backend/concepts/api-contracts-and-validation.md`

## Data

| Purpose | Default |
| --- | --- |
| Relational DB | PostgreSQL |
| SQL access | SQLAlchemy/psycopg in Python; pg + Drizzle/Prisma in TypeScript |
| Cache | Redis |
| Search | OpenSearch/Elasticsearch concepts |
| Vector search | pgvector first; dedicated vector DB when justified |

## Distributed systems

| Purpose | Default |
| --- | --- |
| Cloud queue | SQS |
| Event streaming | Kafka |
| Event-driven AWS integration | EventBridge |
| Reliability patterns | Idempotency, outbox, bounded retries, circuit breakers, backpressure |

## Infrastructure

| Layer | Default |
| --- | --- |
| OS | Linux |
| Containers | Docker |
| Orchestration | Kubernetes |
| Cloud | AWS |
| IaC | Terraform |
| CI/CD | GitHub Actions |

## Production engineering

| Capability | Default |
| --- | --- |
| Telemetry | OpenTelemetry |
| Metrics | Prometheus |
| Dashboards | Grafana |
| Logs | Structured JSON logs + centralized aggregation |
| Tracing | OpenTelemetry + Tempo/Jaeger concepts |
| Security | OWASP guidance + cloud IAM + secrets management |
| Load testing | k6 |

## AI extension

| Capability | Default |
| --- | --- |
| ML | scikit-learn + PyTorch |
| Model ecosystem | Hugging Face Transformers |
| LLM APIs | Provider SDKs behind a stable application boundary |
| Embeddings/vector search | pgvector initially |
| RAG | Retrieval + ranking + context construction + generation + evaluation |
| Agent workflows | Explicit workflows first; agents where dynamic behavior is justified |
| Evaluation | Offline datasets + task-specific evals + traces |
| Serving | vLLM or managed model inference where appropriate |
