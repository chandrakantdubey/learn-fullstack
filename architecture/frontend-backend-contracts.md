# Frontend–Backend Contracts

A fullstack system works when independently evolving layers agree on explicit contracts rather than sharing accidental implementation details.

## Contract layers

```text
UI intent
  ↓
HTTP / event contract
  ↓
transport DTO
  ↓
application command/query
  ↓
domain model
  ↓
persistence model
```

These models may overlap in simple features, but they should not be coupled by default.

## Validate at boundaries

The browser is an untrusted client. Client validation improves UX; server validation establishes correctness. Authorization must happen on the server.

For TypeScript applications, the canonical runtime schema is Zod. Keep transport validation separate from deeper domain invariants.

## API evolution

Prefer additive, backward-compatible changes when old clients may remain deployed. Consider:

- new optional fields
- tolerant readers
- explicit deprecation
- enum evolution
- pagination semantics
- error-code stability
- idempotency keys
- versioning only when compatibility cannot otherwise be maintained

## Errors

A client needs a stable machine-readable error contract. Separate validation errors, authentication failures, authorization failures, conflicts, rate limits, dependency failures and unexpected server errors.

Do not expose internal stack traces, SQL details, provider credentials or sensitive dependency responses.

## Pagination

Choose pagination from workload and product semantics. Offset pagination is simple but can become expensive or unstable under changing datasets. Cursor/keyset pagination requires a stable ordering and an opaque cursor contract.

## Mutations

A mutation contract should define authentication, authorization, validation, concurrency behavior, idempotency and response semantics. Retries are part of the contract because clients, proxies and workers can retry.

## Generated clients and OpenAPI

OpenAPI can make transport contracts discoverable and support generated clients. Generated types do not replace runtime validation or server authorization.

## Fullstack testing

Test the contract from both sides:

```text
frontend request
 → API contract
 → backend handler
 → application service
 → response contract
 → frontend state/update
```

Use contract/integration tests for compatibility and end-to-end tests for critical user journeys.

## Production checklist

- Contract ownership is explicit.
- Runtime validation exists at trust boundaries.
- Authorization is server-side.
- Errors are stable and non-sensitive.
- Mutations are retry-safe where required.
- Schema evolution is backward-compatible where possible.
- API and event contracts are tested.
- DTOs are not forced to become domain models.
