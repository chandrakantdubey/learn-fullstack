# Distributed Systems Mental Model

A distributed system is multiple independently executing components that communicate over a network. The network introduces latency, partial failure, reordering, duplication and ambiguity that do not exist in the same way inside one process.

## Failure model

Assume:

- a request can be lost
- a response can be lost after the server commits work
- a dependency can be slow without being completely down
- messages can be duplicated
- consumers can restart
- clocks can disagree
- machines can fail independently

Therefore "the client timed out" does not mean "the operation did not happen."

## Core patterns

### Idempotency

Make repeated delivery safe. Store idempotency keys/results or design operations so duplicates converge to the same state.

### Timeouts and deadlines

Every network call should have a bounded lifetime. Prefer propagating an overall deadline so downstream services do not continue work after the caller has already abandoned the request.

### Retries

Retry only operations that are safe or explicitly idempotent. Use exponential backoff with jitter and cap attempts. Retries amplify load during incidents, so combine them with circuit breaking and budgets.

### Queue and worker

```text
API → durable queue → worker → database/external service
```

This decouples request latency from slow work and absorbs bursts, but introduces eventual consistency, duplicate delivery and operational complexity.

### Outbox

When a database transaction and event publication must correspond, write the business change and an outbox record in the same transaction. A separate publisher delivers the event and marks it processed. Consumers still need idempotency.

### Saga

A saga coordinates a multi-step business operation without one global database transaction. Each step has a compensating action or explicit failure state. It is a business workflow pattern, not a magical replacement for transactions.

## Consistency

Choose consistency based on the invariant. User-facing reads may tolerate eventual consistency while balances, uniqueness and authorization generally require stronger guarantees at the authoritative boundary.

## Ordering

Global ordering is expensive. Prefer ordering only where a business key requires it, such as per-account events. Partitioning can preserve local order while scaling consumers.

## Backpressure and load shedding

When demand exceeds capacity, queues and concurrency limits protect the system. Load shedding rejects lower-value work before the entire service collapses.

## Scaling

Scale the actual bottleneck. Stateless application replicas are easy to scale horizontally; databases, ordered streams and external APIs often impose harder limits. Capacity planning must account for peak concurrency, connection limits, memory, queue depth and downstream quotas.

## Production questions

For every distributed feature ask:

1. What happens if the response is lost?
2. What happens if the message is delivered twice?
3. What happens if the consumer crashes halfway through?
4. What is the authoritative source of truth?
5. Which operations may be eventually consistent?
6. Where are deadlines enforced?
7. What protects dependencies from overload?
8. How is recovery observed and tested?
