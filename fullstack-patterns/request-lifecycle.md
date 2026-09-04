# Request Lifecycle and Error Propagation

A production request is a chain of boundaries, not a controller function.

```text
Browser / client
  → DNS / TLS / proxy
  → HTTP server
  → authentication + tenant context
  → validation
  → application/domain logic
  → transaction / external calls
  → response serialization
  → client state update
```

## Problem

A failure can occur at every boundary. If each layer invents its own error semantics, clients receive inconsistent status codes, leaked internals, duplicated logging, and ambiguous retry behavior.

## Boundary

Separate:

- transport concerns: HTTP status, headers, serialization
- application concerns: commands, queries, orchestration
- domain concerns: business rules and invariants
- infrastructure concerns: databases, queues, providers

A domain error should not need to know that HTTP exists.

## Invariants

- Validate untrusted input before business logic.
- Authentication establishes identity; authorization establishes permission.
- Every request has a correlation/trace context.
- Errors are classified by whether the caller can fix, retry, or must escalate them.
- Do not expose stack traces, SQL, provider responses, or secrets to clients.
- Side effects must have explicit transaction and timeout boundaries.

## Error taxonomy

A useful baseline is:

| Class | Typical HTTP mapping | Retry? |
|---|---:|---|
| Invalid input | 400/422 | No |
| Unauthenticated | 401 | Usually no |
| Unauthorized | 403 | No |
| Missing resource | 404 | No |
| Conflict / invariant violation | 409 | Usually no |
| Rate limited | 429 | After server-provided delay |
| Dependency failure | 502/503/504 | Often, with policy |
| Unexpected server failure | 500 | Controlled client retry only |

The mapping is an API concern, not a domain rule.

## Implementation choices

A strong implementation has one request pipeline that establishes context, validates input, executes application logic, translates known errors, and emits structured telemetry.

Keep error responses stable. Include a machine-readable code and a human-safe message. Attach a request/trace identifier when useful.

## Failure modes

Watch for:

- validation occurring after database access
- authorization checked only in the UI
- every error becoming `500`
- retries applied to non-idempotent operations
- logging the same exception at five layers
- losing trace context across queues
- swallowing cancellation or client disconnects
- returning dependency-specific errors directly

## Security

Treat every boundary as untrusted. Never use client-provided tenant/user identifiers as authorization evidence. Redact secrets and sensitive payloads from logs. Make error detail proportional to the caller's trust level.

## Performance

Avoid unnecessary serialization, duplicate database lookups, and synchronous calls to slow dependencies. Set deadlines for the whole request and allocate smaller budgets to downstream calls.

## Operational signals

Track request rate, error rate, latency, saturation, timeout counts, dependency failures, and cancellation. Correlate logs, traces, database operations, and downstream calls with one trace context.

## Related technologies

Use the canonical notes for Fastify/FastAPI, Zod/Pydantic, PostgreSQL, Redis, OpenTelemetry, and the frontend stack rather than duplicating their APIs here.
