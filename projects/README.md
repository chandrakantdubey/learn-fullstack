# Production Project Portfolio

These projects are integration proofs, not course exercises. Each should force multiple engineering boundaries to work together and should be built with production constraints, tests, observability and failure handling.

## Projects

1. **Multi-tenant SaaS** — Next.js + FastAPI/Node + PostgreSQL + Redis. Prove identity, tenant isolation, RBAC, contracts, transactions, caching and E2E behavior.
2. **Realtime Collaboration Platform** — browser + WebSockets/SSE + API + Redis + PostgreSQL. Prove connection lifecycle, presence, ordering, reconnects and backpressure.
3. **Event-Driven Order Platform** — API + PostgreSQL + outbox + Kafka/SQS + workers. Prove idempotency, delivery semantics, retries, DLQ, ordering and eventual consistency.
4. **Search Platform** — ingestion + PostgreSQL + OpenSearch. Prove analyzers, filtering, ranking, reindexing, versioning and recovery.
5. **AI Knowledge Assistant** — Next.js + API + document ingestion + embeddings + pgvector + LLM. Prove ACL-aware retrieval, citations, streaming, prompt-injection resistance, evaluation and cost controls.
6. **Agentic Operations Assistant** — LLM + tool layer + workflow/state machine + approval UI. Prove bounded execution, authorization, human approval, idempotency, auditability and evaluation.
7. **Background Job Platform** — API + queue + worker fleet + Redis/PostgreSQL. Prove scheduling, leases, retries, deduplication, concurrency limits, backpressure and recovery.
8. **Media/File Processing Pipeline** — browser uploads + object storage + asynchronous processing + status API. Prove streaming, signed URLs, validation, durable jobs, progress and cleanup.
9. **Observability-First URL/Link Service** — high-throughput API + PostgreSQL/Redis + async analytics. Prove caching, rate limiting, hot-key behavior, telemetry, load testing and capacity planning.
10. **Production AI Application Platform** — complete frontend/backend/data/queue/RAG/agent/evaluation/deployment synthesis.

## Canonical documents

- [`project-specs.md`](project-specs.md) — product goals, boundaries, failure cases and senior-defense topics.
- [`build-playbook.md`](build-playbook.md) — implementation slices, invariants, break tests and promotion order.
- [`../docs/production-verification.md`](../docs/production-verification.md) — universal acceptance standard.
- [`../docs/completion-ledger.md`](../docs/completion-ledger.md) — evidence tracking semantics.

## Shared quality bar

Every serious project should include:

- requirements and non-goals
- architecture diagram and ADRs
- threat model
- API/event contract
- schema and migration strategy
- local development environment
- unit/integration/contract/E2E tests as appropriate
- structured logs, metrics and traces
- rate/resource limits
- failure injection
- load test and capacity estimate
- backup/recovery consideration
- CI/CD
- deployment strategy
- runbook and rollback
- known trade-offs

A project is not finished because the happy path works. It is finished when failure, security, scale and operations have been designed and tested.

## Recommended build order

`01 → 02 → 03 → 07 → 08 → 09 → 04 → 05 → 06 → 10`

Do not build all ten shallowly. Build the smallest set deeply enough to demonstrate the complete skill graph, then use the remaining projects to close specific evidence gaps.
