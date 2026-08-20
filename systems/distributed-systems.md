# Distributed Systems

Distributed systems fail differently from single-process applications because communication, timing, and partial failure become part of the design.

## Core model

```text
Client → Service A → Service B → Database
            │             │
            └── network ──┘
```

Any network call can be slow, duplicated, reordered, dropped, or partially successful.

## Concepts

- latency and tail latency
- partial failure
- timeouts
- retries with exponential backoff and jitter
- idempotency
- load shedding
- backpressure
- circuit breakers
- bulkheads
- replication
- sharding
- leader/follower
- quorum reads/writes
- strong vs eventual consistency
- CAP trade-offs
- distributed transactions
- consensus concepts

## Consistency

Choose consistency per business invariant rather than globally.

Examples:

- account balance: strong consistency
- analytics dashboard: eventual consistency
- search index: eventually consistent projection
- notification delivery: at-least-once with idempotent consumer

## Idempotency

A retry must not accidentally apply a business operation twice.

Typical pattern:

```text
request + idempotency key
        ↓
check durable record
        ↓
perform operation once
        ↓
store result
        ↓
return same result on retry
```

## Failure design

Every cross-service dependency should define:

- timeout
- retry policy
- retryable errors
- maximum retry budget
- fallback or degraded behavior
- observability signal
- idempotency behavior

Never blindly retry non-idempotent mutations.

## Replication and sharding

Replication improves availability/read capacity but introduces lag and failover complexity. Sharding increases write/storage scale but makes routing, rebalancing, joins, and transactions harder.

Do not introduce either until a single-node architecture is a measured bottleneck.

## Practical patterns

- transactional outbox
- inbox/idempotency record
- saga for multi-service workflows
- CQRS when read/write models have materially different needs
- cache-aside
- lease/heartbeat for worker ownership

The goal is not to use every pattern. The goal is to understand the failure mode each pattern addresses.
