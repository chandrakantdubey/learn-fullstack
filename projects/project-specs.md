# Production Project Specifications

These are integration projects. They are not a sequence of small tutorials. Build them as serious systems with explicit requirements, architecture decisions, tests, observability and operational runbooks.

## Shared definition of done

Every project must have:

- requirements and non-goals
- architecture diagram
- ADRs for important trade-offs
- threat model
- API/event contracts
- schema and migration strategy
- authentication/authorization model where relevant
- unit + integration + contract tests
- end-to-end tests where applicable
- structured logs, metrics and traces
- limits, timeouts and cancellation
- failure-injection scenarios
- load/capacity estimate
- backup/recovery or data-loss analysis
- CI/CD and deployment strategy
- runbook and rollback procedure
- known trade-offs

## 1. Multi-tenant SaaS

**Goal:** Build a tenant-isolated business application.

**Core path:** Next.js → API → auth → domain services → PostgreSQL → Redis.

**Must prove:** tenant isolation, RBAC, API contracts, validation, transactions, optimistic UI, cache invalidation, migrations, audit logs and E2E testing.

**Failure cases:** duplicate mutation, stale cache, DB timeout, unauthorized tenant access, partial request failure.

**Senior defense:** shared-schema versus separate-schema tenancy; cache key design; transaction boundaries; session versus token trade-offs.

## 2. Realtime Collaboration

**Goal:** Multiple users edit and observe shared state in realtime.

**Core path:** browser → HTTP bootstrap → WebSocket/SSE → Redis → PostgreSQL.

**Must prove:** connection lifecycle, authentication, authorization, reconnects, ordering, optimistic updates, fan-out and backpressure.

**Failure cases:** duplicate events, slow client, reconnect storm, server restart, lost connection during mutation.

**Senior defense:** WebSocket versus SSE; durable state versus ephemeral presence; ordering guarantees.

## 3. Event-Driven Order Platform

**Goal:** Process orders across independent asynchronous workers.

**Core path:** API → PostgreSQL transaction → outbox → Kafka/SQS → consumers → downstream effects.

**Must prove:** idempotency, delivery semantics, retries, DLQ, ordering, deduplication, eventual consistency and tracing.

**Failure cases:** DB commit succeeds but publish fails; duplicate delivery; poison message; downstream timeout.

**Senior defense:** outbox versus direct publish; partitioning; exactly-once claims versus idempotent effects.

## 4. Search Platform

**Goal:** Build a production search/indexing service.

**Core path:** source data → ingestion worker → index → query API → frontend.

**Must prove:** analyzers, filtering, pagination, ranking, reindexing, versioned indexes and recovery.

**Failure cases:** stale index, failed batch, incompatible schema, hot query, partial reindex.

**Senior defense:** PostgreSQL search versus OpenSearch; consistency expectations; zero-downtime reindexing.

## 5. AI Knowledge Assistant

**Goal:** Build authorization-aware RAG over user documents.

**Core path:** upload → parse → chunk → embed → pgvector → retrieve/filter/rerank → model → citations → stream.

**Must prove:** document lifecycle, metadata, ACL-aware retrieval, provenance, prompt-injection resistance, evaluation, latency and cost controls.

**Failure cases:** stale embeddings, unauthorized retrieval, provider timeout, empty retrieval, malicious document instructions.

**Senior defense:** chunking trade-offs; vector versus lexical retrieval; retrieval evaluation; model fallback.

## 6. Agentic Operations Assistant

**Goal:** Build a bounded tool-using assistant for operational tasks.

**Core path:** UI → API → model → explicit workflow/state machine → validated tool call → approval → execution → audit.

**Must prove:** tool allowlists, argument validation, budgets, timeouts, retries, idempotency, approval gates and complete auditability.

**Failure cases:** prompt injection, destructive tool request, repeated tool call, partial execution, stale state.

**Senior defense:** agent autonomy versus deterministic workflow; where human approval is mandatory.

## 7. Background Job Platform

**Goal:** Build a durable worker platform for asynchronous application work.

**Core path:** API → queue → scheduler/lease → worker fleet → PostgreSQL/Redis.

**Must prove:** retries, leases, deduplication, concurrency limits, backpressure, graceful shutdown and recovery.

**Failure cases:** worker crash mid-job, duplicate execution, queue overload, stuck job, dependency outage.

**Senior defense:** queue semantics, visibility timeout/lease design, fairness and overload control.

## 8. Media/File Processing Pipeline

**Goal:** Safely process large user uploads asynchronously.

**Core path:** browser → signed upload → object storage → job queue → processors → status API.

**Must prove:** streaming, size/type limits, safe filenames, scanning boundary, durable status, progress and cleanup.

**Failure cases:** abandoned upload, partial processing, malformed file, worker crash, storage outage.

**Senior defense:** direct-to-storage versus proxy uploads; synchronous versus async processing; retention policy.

## 9. High-Throughput URL/Link Service

**Goal:** Build a heavily cached redirect and analytics service.

**Core path:** redirect API → Redis → PostgreSQL; analytics → async queue → workers.

**Must prove:** idempotent creation, cache strategy, rate limiting, hot keys, async analytics, metrics/tracing and capacity planning.

**Failure cases:** cache outage, hot URL, duplicate create request, analytics backlog, DB saturation.

**Senior defense:** cache-aside behavior, consistency of redirects, write/read scaling and cost.

## 10. Production AI Application Platform

**Goal:** Combine the entire engineering stack into one product.

**Core path:**

```text
Browser
 → API/Auth
 → Domain
 → PostgreSQL + Redis
 → Queue/Worker
 → Retrieval
 → Model/provider routing
 → Tool/workflow layer
 → Streaming response
 → Evaluation
 → Observability
 → Docker/CI/CD/Cloud
```

**Must prove:** multi-user security, asynchronous ingestion, RAG, model routing, bounded tools, streaming, evaluation, tracing, cost controls, deployment and recovery.

**Failure cases:** provider outage, retrieval outage, queue backlog, model latency spike, unauthorized data access, runaway tool execution.

**Senior defense:** where to place AI boundaries, when to fall back, how to measure quality, and how architecture changes as traffic and model spend grow.

## Portfolio rule

Do not build all ten as shallow demos. Build a smaller number deeply enough to defend every important decision, then use the remaining projects to exercise missing boundaries.
