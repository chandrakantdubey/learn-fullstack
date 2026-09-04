# Fullstack Patterns

Cross-layer patterns that connect frontend, backend, data, infrastructure, and production concerns.

These are not technology tutorials. Each pattern explains a system boundary and the trade-offs behind it.

## Patterns

- Request lifecycle and error propagation
- Authentication and authorization boundaries
- Client/server state separation
- Caching and invalidation
- Idempotent commands
- Transaction + outbox
- Background job processing
- Pagination and cursor design
- File upload pipelines
- Webhook ingestion
- Rate limiting
- Retries, timeouts, and circuit breakers
- Observability propagation
- Async event-driven workflows
- AI/RAG request pipelines

## Technology ownership

Technology-specific knowledge belongs under `technologies/`.

For example, Zod has one canonical technology note at:

`technologies/shared/zod.md`

Patterns may reference technologies, but they should not duplicate their technology-specific notes.

## Pattern template

```text
Problem
  ↓
Boundary
  ↓
Invariant
  ↓
Implementation choices
  ↓
Failure modes
  ↓
Security
  ↓
Performance
  ↓
Operational signals
```
