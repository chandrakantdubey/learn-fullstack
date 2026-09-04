# Production Project Portfolio

These projects are integration proofs, not course exercises. Each should force multiple engineering boundaries to work together and should be built with production constraints, tests, observability and failure handling.

## 1. Multi-tenant SaaS

React/Next.js + FastAPI/Node + PostgreSQL + Redis.

Prove authentication, tenant isolation, RBAC, API contracts, validation, transactions, caching, migrations, audit logs and end-to-end testing.

## 2. Realtime Collaboration Platform

Browser + WebSockets/SSE + API + Redis + PostgreSQL.

Prove connection lifecycle, presence, optimistic updates, ordering, reconnects, authorization, fan-out and backpressure.

## 3. Event-Driven Order Platform

API + PostgreSQL + outbox + Kafka/SQS + workers.

Prove idempotency, delivery semantics, retries, dead-letter handling, transactional boundaries, eventual consistency and observability.

## 4. Search Platform

Ingestion + PostgreSQL + OpenSearch.

Prove indexing pipelines, analyzers, filtering, pagination, ranking, reindexing, aliases/versioning and failure recovery.

## 5. AI Knowledge Assistant

Next.js + API + document ingestion + embeddings + pgvector + LLM.

Prove chunking, metadata, retrieval, authorization-aware filtering, citations, streaming, prompt injection defenses, evaluation and cost controls.

## 6. Agentic Operations Assistant

LLM + tool layer + workflow/state machine + approval UI.

Prove deterministic workflows, bounded tool execution, human approval, retries, idempotency, auditability, prompt/tool security and evaluation.

## 7. Background Job Platform

API + queue + worker fleet + Redis/PostgreSQL.

Prove scheduling, leases, retries, deduplication, concurrency limits, backpressure, graceful shutdown and worker recovery.

## 8. Media/File Processing Pipeline

Browser uploads + object storage + asynchronous processing + status API.

Prove streaming, signed URLs, size/type validation, virus/scanning boundary awareness, durable jobs, progress reporting and cleanup.

## 9. Observability-First URL/Link Service

High-throughput API + PostgreSQL/Redis + async analytics.

Prove caching, rate limiting, idempotent creation, hot-key behavior, metrics, traces, structured logs, load testing and capacity planning.

## 10. Production AI Application Platform

A complete product combining frontend, APIs, PostgreSQL, Redis, queues, RAG, model routing, evaluation and deployment.

Prove the complete path:

```text
Browser
 → API
 → Auth
 → Domain
 → PostgreSQL
 → Redis
 → Queue
 → Worker
 → Retrieval
 → Model
 → Streaming response
 → Evaluation
 → Observability
 → CI/CD
 → Cloud
```

## Project quality bar

Every serious project should include:

- architecture decision record
- threat model
- API contract
- database schema and migration strategy
- local development environment
- automated tests
- contract/integration tests
- end-to-end tests where applicable
- structured logs, metrics and traces
- rate/resource limits
- failure injection plan
- load test and capacity estimate
- backup/recovery consideration
- CI/CD
- deployment strategy
- runbook
- known trade-offs

A project is not finished because the happy path works. It is finished when failure, security, scale and operations have been designed and tested.
