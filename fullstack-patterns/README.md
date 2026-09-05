# Fullstack Patterns

Cross-layer patterns that connect frontend, backend, data, infrastructure, and production concerns.

These are not technology tutorials. Each pattern explains a system boundary, the invariant it protects, and the trade-offs behind it.

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

## Pattern template

```text
Problem
  ↓
Boundary
  ↓
Invariant
  ↓
Contract
  ↓
Implementation choices
  ↓
Failure modes
  ↓
Security
  ↓
Performance / scale
  ↓
Operational signals
```

## Technology ownership

Technology-specific knowledge belongs under `technologies/`. Patterns may reference technologies, but they should not duplicate technology-specific notes.

## Verification

A pattern is not considered understood because its diagram is familiar. Prove it through the relevant project and the final verification loop:

**Understand → Implement → Debug → Measure → Secure → Test → Scale → Operate → Recover → Defend trade-offs.**

See [`../docs/production-verification.md`](../docs/production-verification.md).
