# Transaction + Outbox

The outbox pattern connects a database transaction to asynchronous messaging without pretending two systems share one transaction.

## Problem

A service may need to update PostgreSQL and publish an event. If the database commit succeeds and publishing fails, downstream systems never learn about the change. If publishing succeeds first and the transaction rolls back, consumers see a fact that never became true.

## Boundary

```text
business mutation + outbox row
          ↓ one DB transaction
      committed state
          ↓
    outbox publisher
          ↓
      broker/queue
          ↓
        consumer
```

## Invariants

- The business mutation and outbox record commit atomically.
- An outbox record describes a fact that exists in committed state.
- Delivery is treated as at-least-once unless stronger semantics are explicitly implemented.
- Consumers are idempotent.

## Implementation choices

Write an immutable event record containing an event ID, aggregate/resource identity, event type, payload or reference, schema version, and creation time.

A publisher polls or streams unpublished rows, publishes them, and records delivery state. For high throughput, batch work and use indexes designed around unpublished/ready records.

Consumers deduplicate by event ID or use an idempotent business operation. If ordering matters, define the ordering key and partitioning strategy explicitly.

## Failure modes

- publishing before commit
- deleting outbox rows before durable delivery
- assuming one publish means one consumer execution
- payload containing data that is already stale or unauthorized
- no schema version
- unbounded outbox growth
- poison messages repeatedly blocking progress

## Security

Avoid putting secrets or unnecessary personal data into durable events. Authorize consumers and protect event channels. Treat event payloads as untrusted input at consumer boundaries.

## Performance

Use indexes, batching, backoff, retention policies, and partitioning where needed. Monitor publisher lag and consumer lag rather than only API latency.

## Operational signals

Measure outbox age, publish failures, queue depth, consumer lag, duplicate deliveries, dead-letter volume, and processing latency.
