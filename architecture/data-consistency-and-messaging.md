# Data Consistency, Queues and Messaging

Distributed applications become difficult when one business operation crosses database, cache, queue and service boundaries.

## Start with the invariant

Before choosing Kafka, SQS, a transaction or a distributed lock, state what must remain true.

Examples:

- an order cannot be charged twice
- a published event must correspond to committed state
- a user can access only its tenant's records
- inventory cannot become negative

The mechanism follows from the invariant.

## Synchronous vs asynchronous

Use synchronous work when the caller needs an immediate result and the operation fits the request latency budget. Use asynchronous work when processing can continue independently, is expensive, or benefits from buffering/retries.

```text
synchronous:
request → service → DB → response

asynchronous:
request → DB + enqueue → response
                    ↓
                  worker → side effect
```

## Delivery semantics

At-most-once can lose work. At-least-once can duplicate work. Exactly-once claims must be examined across the complete system; a broker guarantee does not automatically make an external side effect exactly once.

Design consumers to be idempotent and use deduplication when duplicate delivery is possible.

## Transactional outbox

When a database update and event publication must agree, a common pattern is:

```text
transaction
  ├─ update domain state
  └─ insert outbox event
          ↓
      outbox publisher
          ↓
       broker/topic
```

The publisher retries unsent events. Consumers still need idempotency.

## Ordering

Global ordering is expensive and often unnecessary. Define the ordering requirement precisely: per entity, per partition, per tenant, or none. Partitioning and consumer concurrency should follow that requirement.

## Cache consistency

A cache is another copy of state. Define ownership, freshness, invalidation and behavior when the cache is stale or unavailable. Never let cache availability become an accidental correctness dependency unless the system explicitly requires it.

## Sagas and workflows

A multi-step business process may need explicit state and compensation rather than one giant distributed transaction. Compensation is not a magical rollback: some external effects cannot be undone exactly.

## Failure handling

Every message workflow needs answers for:

- retries
- poison messages
- dead-letter handling
- visibility/lease expiry
- duplicate delivery
- consumer restart
- backlog growth
- schema evolution
- dependency outage

## Production checklist

- Define the business invariant first.
- Make delivery semantics explicit.
- Make consumers idempotent.
- Use an outbox when DB/event atomicity matters.
- Bound retries and queue growth.
- Monitor queue age and consumer lag.
- Version message schemas.
- Test duplicate, delayed and reordered messages.
