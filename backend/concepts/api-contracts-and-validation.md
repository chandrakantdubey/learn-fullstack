# API Contracts and Validation

An API contract defines what a client may send, what the server accepts, what it returns, and how failures are represented.

## Boundary model

```text
HTTP request
    ↓
transport parsing
    ↓
validation
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

## TypeScript

Use **Zod** for runtime validation in TypeScript services.

```ts
import { z } from "zod";

const CreateUser = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
});

type CreateUser = z.infer<typeof CreateUser>;

const input = CreateUser.parse(request.body);
```

The important distinction is:

```text
TypeScript type
  = compile-time contract

Zod schema
  = runtime contract
```

## Python

Use **Pydantic** for the equivalent boundary validation in FastAPI/Python services.

```text
TypeScript service → Zod
Python service     → Pydantic
```

Both should produce the same conceptual API contract even when the implementation language differs.

## OpenAPI

For REST APIs, the externally visible contract should be representable through OpenAPI.

```text
Schema
  ↓
validation
  ↓
request / response contract
  ↓
OpenAPI documentation
  ↓
client integration
```

Do not assume generated types remove the need for runtime validation. Generated TypeScript types are still compile-time artifacts.

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
validation
      ↓
normalized internal model
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

## Connects to

- `backend/concepts/service-architecture.md`
- `backend/concepts/authentication-and-security.md`
- `frontend/concepts/runtime-validation.md`
- `docs/stack.md`
