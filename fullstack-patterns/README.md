# Fullstack Patterns

Cross-layer patterns that connect frontend, backend, data, infrastructure, and production concerns.

These are not framework tutorials. Each pattern explains a system boundary and the trade-offs behind it.

## Patterns

- [Runtime validation and API contracts](validation-and-api-contracts.md)
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

## Pattern template

```text
Problem
  ↓
Boundary
  ↓
Invariant
  ↓
Implementation
  ↓
Failure modes
  ↓
Security
  ↓
Performance
  ↓
Operational signals
```
