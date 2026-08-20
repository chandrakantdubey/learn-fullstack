# Distributed Systems

A distributed system is a system whose important state or execution spans multiple failure domains.

## Core mental model

```text
Request
  ↓
Service A ─── Service B
  │               │
  ↓               ↓
 DB A            DB B
  │               │
  └──── Network ──┘

Any network call can be slow, duplicated, reordered, or unavailable.
```

## Core concepts

- latency and tail latency
- partial failure
- timeouts
- retries and exponential backoff with jitter
- idempotency
- ordering
- consistency
- availability
- replication
- partitioning/sharding
- leader/follower systems
- quorum concepts
- distributed coordination
- backpressure
- load shedding
- cascading failure

## CAP

CAP is a reasoning tool about network partitions and trade-offs between consistency and availability. Do not use it as a slogan to classify every database.

## Consistency

Distinguish:

- strong consistency
- read-your-writes
- monotonic reads
- eventual consistency
- bounded staleness

Choose the weakest model that preserves the product invariant; stronger consistency can cost latency, availability, or operational complexity.

## Reliability patterns

### Timeout
Every remote call needs a bounded deadline.

### Retry
Retry only failures that are plausibly transient and only when the operation is safe to repeat.

### Idempotency
Use an idempotency key or deterministic operation identifier when clients may retry a mutation.

### Circuit breaker
Stop repeatedly calling a failing dependency and recover after a controlled interval.

### Bulkhead
Isolate resource pools so failure in one workload cannot exhaust all capacity.

### Outbox
Commit business state and an outbound event in one local transaction; publish from the outbox asynchronously.

### Saga
Coordinate a multi-service business workflow with explicit compensating actions instead of assuming a distributed transaction.

## Scaling

- horizontal replication for stateless services
- partition hot data by a stable key
- avoid global coordination on the hot path
- cache only when consistency behavior is understood
- protect dependencies with concurrency limits

## Failure reasoning

For each dependency ask:

```text
What happens if it is:
- slow?
- unavailable?
- returning stale data?
- returning duplicate responses?
- partially successful?
- recovering after a long outage?
```

The answer should be visible in the design, not discovered during the incident.
