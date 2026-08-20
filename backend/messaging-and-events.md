# Messaging and Event-Driven Systems

Queues and streams decouple producers from consumers and turn synchronous work into asynchronous workflows.

## Primitives

- queue
- topic
- producer
- consumer
- partition
- offset
- consumer group
- acknowledgement
- dead-letter queue
- retry queue

## Delivery semantics

Most production systems should assume **at-least-once** delivery.

Therefore consumers must be idempotent:

```text
message M
  ↓
process(M)
  ↓
ack

If ack is lost:
M is delivered again
```

Design `process(M)` so the second execution is safe.

## Ordering

Ordering is usually scoped, not global. Partition or key messages by the entity whose order matters.

Example:

```text
account_id=42 → same partition
account_id=99 → another partition
```

## Kafka vs queues

Kafka is useful when durable ordered streams, replay, and multiple independent consumers matter. Cloud queues such as SQS are often simpler for work distribution where replayable log semantics are unnecessary.

## Retry strategy

```text
consumer
  ↓
transient failure
  ↓
retry with backoff
  ↓
retry budget exhausted
  ↓
DLQ / operator action
```

Never create an unbounded retry loop.

## Backpressure

A producer may generate work faster than consumers can process it. Control this with bounded queues, consumer concurrency, rate limits, and load shedding.

## Outbox pattern

```text
DB transaction
 ├── update business state
 └── insert outbox event

commit
  ↓
outbox publisher
  ↓
queue / stream
```

This avoids committing business state while losing the event.

## Common choices

- SQS for managed background work
- Kafka for durable event streams and replay
- EventBridge for event routing across AWS services
- Redis Streams for focused low-complexity stream use cases
- Celery/BullMQ/worker frameworks when the application needs a job abstraction

## Production concerns

Monitor queue depth, age of oldest message, processing latency, consumer errors, retry count, DLQ growth, and consumer lag.
