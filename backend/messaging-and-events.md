# Messaging and Events

Queues and event streams decouple producers from consumers, absorb bursts, and move slow side effects out of request paths.

## Core concepts

- producer
- consumer
- queue
- topic
- partition
- offset
- consumer group
- ordering
- delivery semantics
- dead-letter queue
- visibility timeout
- retry policy
- backpressure

## Delivery semantics

Design around at-least-once delivery in most practical systems. Consumers must therefore be idempotent.

Exactly-once claims are usually narrower than they sound; understand the storage and side-effect boundaries before relying on them.

## Queue vs stream

Use a queue when work should generally be processed once by one consumer group. Use a stream when ordered records, replay, multiple independent consumers, or event history matter.

Typical choices:

- SQS for managed task queues
- Kafka for high-throughput event streams and replay
- Redis Streams for focused lightweight workloads
- EventBridge for AWS event routing

## Production worker

```text
API
 ↓
transaction + outbox/event
 ↓
queue
 ↓
worker
 ├── validate
 ├── process
 ├── commit durable result
 └── ack
```

Only acknowledge after the durable side effect succeeds. Poison messages need bounded retries and a dead-letter path.

## Design questions

Before introducing a broker, answer:

1. Why is synchronous processing insufficient?
2. What ordering is required?
3. What happens on duplicate delivery?
4. What happens when consumers are down?
5. How is backlog measured?
6. How is replay handled?
7. How is schema evolution managed?

## Project proof

The task system uses a background audit/notification job with explicit idempotency and retry behavior.
