# API Contracts and Validation

An API contract defines what a client may send, what the server accepts, what it returns, and how failures are represented.

## Boundary model

```text
HTTP request
    ↓
transport parsing
    ↓
runtime schema validation
    ↓
authentication / authorization
    ↓
application command
    ↓
domain logic
    ↓
repository / external service
```

Validation belongs near the boundary. Domain invariants still belong in domain/application logic.

## Runtime validation

The concrete validation technology depends on the implementation language:

```text
TypeScript service → Zod
Python service     → Pydantic
```

The repository keeps the detailed technology notes in one canonical location rather than duplicating them across frontend/backend concept files.

See `technologies/shared/zod.md` for Zod and the Python technology notes for Pydantic.

## Compile-time vs runtime

```text
TypeScript type
  = compile-time contract

Runtime schema
  = executable boundary check
```

Generated TypeScript types do not validate network data at runtime.

## OpenAPI

For REST APIs, the externally visible contract should be representable through OpenAPI.

```text
schema / contract
      ↓
request + response definitions
      ↓
OpenAPI
      ↓
client integration
```

OpenAPI describes the external HTTP contract; runtime validation enforces data at execution time.

## Request validation

Validate:

- path parameters
- query parameters
- headers where application semantics depend on them
- request bodies
- pagination bounds
- sorting/filter fields
- uploaded file metadata and limits

Reject malformed input before expensive work.

## Response validation

Response validation is especially useful when consuming third-party services, provider APIs, or unstable internal dependencies.

```text
external response
      ↓
runtime validation / normalization
      ↓
internal model
      ↓
domain logic
```

## Validation vs business rules

A schema can enforce:

- required fields
- types
- formats
- ranges
- string lengths
- allowed values

Business logic may require:

- user owns the resource
- inventory is available
- state transition is legal
- payment is authorized

Do not put all business rules into a schema simply because the schema library can express them.

## Error contract

A production API should expose predictable errors.

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "fields": {
      "email": ["Invalid email"]
    },
    "request_id": "..."
  }
}
```

Avoid leaking stack traces, database errors, credentials, or internal implementation details.

## Contract evolution

Treat API schemas as compatibility boundaries.

Prefer additive changes. When breaking changes are unavoidable, version the contract and migrate clients deliberately.

## Production checklist

- Validate every untrusted boundary.
- Keep validation separate from authorization.
- Bound input sizes and collection lengths.
- Normalize data before domain processing.
- Return stable error codes.
- Correlate failures with request IDs.
- Test invalid inputs as aggressively as happy paths.
- Keep Python and TypeScript services aligned on the same business contract.

## Related

- `technologies/shared/zod.md`
- `backend/concepts/service-architecture.md`
- `backend/concepts/authentication-and-security.md`
- `docs/stack.md`
