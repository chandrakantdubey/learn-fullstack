# Idempotent Commands

An idempotent command can be retried without producing unintended additional effects.

## Problem

Networks fail after a server performs work but before the client receives the response. A client then retries. Without idempotency, one user action can create duplicate orders, charges, jobs, or messages.

## Boundary

The command boundary needs a stable idempotency key, an operation identity, and a durable record of the outcome.

```text
client
  → idempotency key
  → API
  → durable deduplication record
  → transaction / side effect
  → stored result
```

## Invariants

- The same key represents the same logical operation within a defined scope.
- Replays do not execute the protected side effect twice.
- Concurrent requests using the same key cannot both win.
- A key cannot be reused for a materially different payload.

## Implementation choices

Store the key with tenant/user scope, request fingerprint where appropriate, status, and result metadata. Enforce uniqueness in durable storage rather than relying on an in-memory map.

For database work, the idempotency record and business mutation can often share one transaction. For external side effects, combine idempotency with provider-supported idempotency keys or an outbox/worker design.

## Failure modes

- key stored only after the side effect
- no uniqueness constraint
- same key accepted for different payloads
- long-running request holds locks unnecessarily
- ambiguous `in-progress` state treated as success
- dedupe records expire before legitimate retries complete

## Security

Scope keys to the authenticated principal or tenant. Do not let one user probe another user's operation results. Treat idempotency keys as opaque identifiers, not credentials.

## Performance

Use indexed keys and bounded retention. High-volume systems may partition or archive old records. Do not make the dedupe store a single unbounded hot table.

## Operational signals

Track duplicate attempts, conflict rates, in-progress replays, dedupe-store latency, and expired-key incidents.
