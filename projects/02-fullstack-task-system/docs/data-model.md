# Data Model

## Core entities

```text
users 1 ─── N tasks
users 1 ─── N refresh_sessions
users 1 ─── N audit_events
outbox_events N ─── 1 task (optional)
```

## PostgreSQL schema sketch

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TYPE task_status AS ENUM ('todo', 'in_progress', 'done');

CREATE TABLE tasks (
  id UUID PRIMARY KEY,
  owner_id UUID NOT NULL REFERENCES users(id),
  title TEXT NOT NULL,
  description TEXT NOT NULL DEFAULT '',
  status task_status NOT NULL DEFAULT 'todo',
  version BIGINT NOT NULL DEFAULT 1,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX tasks_owner_updated_idx
  ON tasks (owner_id, updated_at DESC, id DESC);

CREATE TABLE outbox_events (
  id UUID PRIMARY KEY,
  aggregate_type TEXT NOT NULL,
  aggregate_id UUID NOT NULL,
  event_type TEXT NOT NULL,
  payload JSONB NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  published_at TIMESTAMPTZ
);

CREATE INDEX outbox_unpublished_idx
  ON outbox_events (created_at)
  WHERE published_at IS NULL;
```

## Invariants

- email is globally unique
- every task has exactly one owner
- callers can only access their authorized tasks
- task version increases on every successful mutation
- state transitions that must be atomic happen inside a transaction
- outbox rows are committed in the same transaction as the state change when durable asynchronous delivery is required

## Why the outbox exists

Writing a row to PostgreSQL and then publishing a queue message in a separate step creates a dual-write failure window. The outbox makes the event durable with the business transaction. A publisher later retries delivery until it succeeds.

The consumer must still be idempotent. The outbox removes one failure mode; it does not magically create exactly-once side effects.
