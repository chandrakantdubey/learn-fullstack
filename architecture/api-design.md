# API Design and Contracts

An API is a contract between independently evolving components. Good API design minimizes ambiguity, makes failures explicit and allows clients and servers to evolve without synchronized releases.

## Contract model

```text
transport
  ↓
request schema
  ↓
authentication / authorization
  ↓
application command
  ↓
domain operation
  ↓
response schema
```

Keep transport concerns separate from domain models when that separation prevents accidental coupling.

## Resource and command semantics

REST works well when resources and HTTP semantics fit the domain. Not every operation must be forced into CRUD. Explicit commands can be clearer for state transitions such as `cancel`, `publish` or `rotate`.

## Input design

Define:

- required vs optional fields
- null semantics
- enum/version behavior
- size and cardinality limits
- pagination rules
- sorting/filtering semantics
- idempotency behavior
- authorization requirements

Validate syntax and shape at the boundary. Enforce business invariants inside the application/domain layer and critical integrity constraints in the database.

## Errors

Use a stable error envelope with a machine-readable code, safe human-readable message, request/correlation identifier and optional field-level details. Do not expose stack traces, SQL, secrets or internal topology to clients.

## Pagination

Offset pagination is simple but can become unstable or expensive on large, changing datasets. Cursor/keyset pagination can provide better consistency and performance when ordering is well-defined. Always document ordering and cursor semantics.

## Evolution

Prefer additive changes. Adding optional response fields is generally safer than renaming/removing fields. Treat enum expansion carefully because some clients incorrectly assume exhaustive values. Breaking changes require an explicit migration/version strategy.

## Idempotency

For operations that create side effects, an idempotency key can allow a client to safely retry after network ambiguity. The server must define the scope, retention window, request equivalence and result replay semantics.

## Security

Authorization must be evaluated on the server against the authenticated principal and target resource. Avoid IDOR by checking ownership/access, not merely by checking that an object exists.

Apply rate limits, payload limits, timeouts and abuse controls according to endpoint risk.

## Observability

Every request should be traceable across frontend, gateway, service, database and asynchronous work. Record latency, status, route template, dependency failures and safe business dimensions; avoid logging secrets and sensitive payloads.

## Contract tooling

OpenAPI can describe HTTP contracts. TypeScript runtime schemas such as Zod and Python models such as Pydantic can enforce runtime boundaries. These are complementary concerns: schema generation, runtime validation and business invariants should not be conflated.

## Production checklist

- Explicit semantics.
- Stable error model.
- Runtime validation.
- Authorization at every protected operation.
- Pagination and payload limits.
- Idempotency for retryable side effects.
- Backward-compatible evolution.
- Timeouts and rate limits.
- Contract tests.
- Observability and auditability.
