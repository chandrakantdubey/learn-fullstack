# Fullstack Skill Map

This file is the curated map for the stack represented by this repository. It separates durable engineering capabilities from implementation choices and keeps the default stack intentionally small.

## 1. Foundations

- Programming fundamentals
- Data structures and algorithms
- Type systems and generics
- Error handling
- Testing fundamentals
- Git and GitHub
- Linux and shell
- Processes, memory, files, and networking basics

## 2. Web Platform

- HTML semantics
- CSS layout and rendering
- Browser architecture
- DOM and Web APIs
- HTTP
- DNS
- TLS
- Cookies and sessions
- CORS / CSP / same-origin policy
- WebSockets / SSE
- Browser performance

## 3. TypeScript Application Engineering

**Primary stack:** TypeScript → React → Next.js → Node.js/Fastify

- Strict TypeScript
- Modules and package boundaries
- Runtime vs compile-time types
- Runtime validation
- API contracts
- Error/result modeling
- React component architecture
- Client state vs server state
- TanStack Query
- React Hook Form
- **Zod**
- Tailwind CSS
- Radix UI / shadcn/ui
- Zustand / Redux Toolkit when justified
- Vite
- Vitest
- Playwright
- pnpm

## 4. Python Engineering

**Primary stack:** Python → FastAPI → Pydantic → SQLAlchemy → PostgreSQL

- Python runtime and standard library
- Type hints
- Packaging and dependency management
- asyncio / concurrency
- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- httpx
- Celery / workers
- pytest

## 5. Backend & APIs

- REST
- OpenAPI
- GraphQL
- gRPC
- WebSockets
- API versioning
- Pagination / filtering / sorting
- Validation
- Authentication / authorization
- Idempotency
- Rate limiting
- Timeouts / retries
- Background jobs
- Event-driven architecture
- Modular monoliths
- Service boundaries

## 6. Data

- SQL
- PostgreSQL
- Transactions / isolation / MVCC
- Indexing / query planning
- Redis
- Caching
- MongoDB concepts
- Search / OpenSearch
- pgvector
- Vector retrieval / ANN / HNSW

## 7. Distributed Systems

- Queues and streams
- Kafka
- SQS
- EventBridge
- Delivery semantics
- Ordering
- Consumer groups
- Backpressure
- Outbox pattern
- Sagas
- Circuit breakers
- Load shedding
- Eventual consistency
- Replication / sharding

## 8. Infrastructure & Cloud

- Linux
- Docker
- Docker Compose
- Kubernetes
- Helm
- AWS
- Terraform
- GitHub Actions
- Container registries
- Networking / VPCs
- IAM
- Secrets management

## 9. Production Engineering

- Security
- Testing strategy
- Observability
- OpenTelemetry
- Prometheus
- Grafana
- Structured logging
- Distributed tracing
- Reliability
- SLOs / SLIs
- Capacity planning
- Load testing
- Performance profiling
- Incident response

## 10. AI / ML Engineering

- AI / ML fundamentals
- Neural networks
- Deep learning
- NLP
- Tokenization
- Embeddings
- Attention
- Transformers
- Language models
- LLMs
- Prompt engineering
- Model APIs
- Fine-tuning / LoRA / QLoRA
- Distillation
- RAG
- Retrieval / reranking
- Evaluation
- Guardrails
- Agent workflows
- Tool use / MCP
- Inference optimization
- Model serving

## Cross-layer rule

A technology belongs in the repository only when its role in the system is clear.

```text
Concept
  ↓
Why it exists
  ↓
System boundary
  ↓
Canonical technology
  ↓
Python / TypeScript implementation
  ↓
Failure + security + performance
  ↓
Production usage
```

The goal is not to collect every library. The goal is to know the important concepts deeply and recognize the right tool for the job.
