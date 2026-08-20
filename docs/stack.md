# Canonical Stack

The stack is intentionally opinionated. Alternatives are introduced only when they illuminate a meaningful engineering trade-off.

## Languages

| Role | Default | Why |
| --- | --- | --- |
| Browser + typed application code | TypeScript | Strong web ecosystem and end-to-end typing |
| Backend + AI | Python | Excellent ecosystem for APIs, data, ML, and AI |
| Systems exposure | C/C++ concepts | Understand memory, compilation, and low-level behavior without making it a primary application language |

## Web

| Layer | Default |
| --- | --- |
| HTML | HTML5 |
| CSS | CSS + Tailwind where appropriate |
| UI | React |
| Fullstack React framework | Next.js |
| Browser testing | Playwright |

## Backend

| Layer | Default |
| --- | --- |
| Python API | FastAPI |
| TypeScript API | Node.js + Fastify |
| Validation | Pydantic / Zod |
| HTTP client | httpx / fetch |
| Background work | Celery or a focused queue worker |

## Data

| Purpose | Default |
| --- | --- |
| Relational DB | PostgreSQL |
| SQL access | SQLAlchemy / psycopg; Prisma/Drizzle where appropriate in TypeScript |
| Cache | Redis |
| Search | OpenSearch/Elasticsearch concepts |
| Vector search | pgvector first; dedicated vector DB when justified |

## Distributed systems

| Purpose | Default |
| --- | --- |
| Cloud queue | SQS |
| Event streaming | Kafka |
| Event-driven AWS integration | EventBridge |

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
