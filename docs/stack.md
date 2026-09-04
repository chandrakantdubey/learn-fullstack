# Canonical Stack

The stack is intentionally opinionated. Alternatives are introduced only when they illuminate a meaningful engineering trade-off.

Technology-specific notes live under `technologies/`. **One technology has one canonical note**, even when that technology is used by multiple layers.

## Languages

| Role | Default |
| --- | --- |
| Browser + typed application code | TypeScript |
| Backend + AI | Python |
| Systems exposure | C/C++ concepts |

## Shared Technologies

| Technology | Role |
| --- | --- |
| Zod | Runtime schemas for TypeScript applications and services |
| OpenAPI | REST contract description |
| Git | Version control |
| Linux | Operating-system foundation |

See `technologies/registry.md` for the complete working list.

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
| Browser testing | Playwright |
| Unit/component testing | Vitest + Testing Library |
| Build tooling | Vite where a standalone frontend is appropriate; Next.js tooling otherwise |
| Package manager | pnpm |

Zod is shared; it is intentionally not duplicated as a separate frontend technology note.

## TypeScript Backend

| Layer | Default |
| --- | --- |
| Runtime | Node.js |
| HTTP service | Fastify |
| API contract | OpenAPI where REST is used |
| HTTP client | native `fetch` |
| PostgreSQL | `pg` |
| SQL / ORM | Drizzle or Prisma when ORM features are justified |
| Cache | Redis |
| Background jobs | BullMQ or a focused worker |
| Logging | Pino |

Zod is the shared TypeScript runtime-schema technology.

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

## Data

| Purpose | Default |
| --- | --- |
| Relational DB | PostgreSQL |
| SQL access | SQLAlchemy/psycopg in Python; pg + Drizzle/Prisma in TypeScript |
| Cache | Redis |
| Search | OpenSearch/Elasticsearch concepts |
| Vector search | pgvector first; dedicated vector DB when justified |

## Distributed Systems

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
| Local orchestration | Docker Compose |
| Orchestration | Kubernetes |
| Kubernetes packaging | Helm |
| Cloud | AWS |
| IaC | Terraform |
| CI/CD | GitHub Actions |

## Production Engineering

| Capability | Default |
| --- | --- |
| Telemetry | OpenTelemetry |
| Metrics | Prometheus |
| Dashboards | Grafana |
| Logs | Structured JSON logs + centralized aggregation |
| Tracing | OpenTelemetry + Tempo/Jaeger concepts |
| Security | OWASP guidance + cloud IAM + secrets management |
| Load testing | k6 |

## AI Extension

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
