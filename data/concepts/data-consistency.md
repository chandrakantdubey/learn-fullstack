# Data Consistency

Consistency is about what state different parts of a system are allowed to observe and when.

## Start with the business invariant

Ask:

> What must never be false?

Examples:

- an order cannot be paid twice
- a username is unique
- inventory cannot be reserved twice for the same unit

Then choose the mechanism that protects that invariant.

## Strong consistency

The caller observes the latest committed state according to the chosen transaction semantics.

Useful when stale data can cause an incorrect business decision.

## Eventual consistency

Different representations may temporarily disagree and converge later.

Useful for:

- search indexes
- analytics
- derived caches
- notifications

Eventual consistency is not automatically bad. It becomes dangerous when the business invariant depends on freshness.

## Transaction + event

A common reliable pattern is the transactional outbox:

```text
BEGIN
  update business state
  insert outbox event
COMMIT

worker reads outbox
  ↓
publish / process
```

This avoids the failure window where a database transaction succeeds but event publication does not.

## Idempotency

Distributed systems commonly deliver work more than once. Consumers should be safe to retry when possible.

An idempotent operation produces the same final business state when the same request is applied repeatedly.

Typical mechanism:

```text
idempotency_key
  ↓
lookup prior result
  ├── exists → return prior result
  └── absent → execute once and persist result
```

## Read-after-write expectations

A user may create a record and immediately expect to see it. If reads go to a lagging replica or stale cache, the system can appear broken.

Choose a consistency model intentionally for each read path.

## Connects to

`data/postgresql.md`, `data/redis.md`, `backend/service-architecture.md`, and `architecture/system-design.md`.
