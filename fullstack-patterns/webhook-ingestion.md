# Webhook Ingestion

Webhooks are untrusted, duplicated, delayed, and sometimes reordered messages from another system.

## Boundary

```text
provider
 → HTTPS endpoint
 → authenticate/verify signature
 → persist event
 → acknowledge quickly
 → async processing
 → idempotent domain action
```

## Invariants

- Signature/authenticity is verified before trusting the event.
- Events are durably recorded before acknowledging when loss is unacceptable.
- Processing is idempotent.
- Provider event IDs are deduplicated.
- Slow business work does not block the provider callback unnecessarily.

## Implementation choices

Verify signatures over the exact raw request body when the provider requires it. Record provider, event ID, event type, received time, payload or safe reference, and processing state.

Return a fast success only after reaching the chosen durability point. Process asynchronously with bounded retries and dead-letter handling.

Do not assume delivery order. If order matters, reconstruct state using provider versions/sequences or query authoritative state.

## Failure modes

- parsing/modifying body before signature verification
- duplicate events creating duplicate effects
- acknowledging before durable persistence
- retrying permanently invalid events forever
- assuming event order
- coupling provider payload shape directly to domain models

## Security

Authenticate the sender, protect the endpoint from replay where supported, limit payload size, and treat event data as untrusted input. Never execute arbitrary commands from a webhook payload.

## Operational signals

Track verification failures, accepted events, duplicates, processing lag, retry counts, dead letters, and provider delivery latency.
