# Runtime Validation + API Contracts

A fullstack application has two different type boundaries:

```text
Browser
  │
  │ JSON / FormData / URL
  ▼
TypeScript application
  │
  │ Zod
  ▼
HTTP API contract
  │
  ▼
Python / TypeScript backend
  │
  │ Pydantic / Zod
  ▼
Domain logic
```

## The rule

Compile-time types describe what your code expects. Runtime schemas verify what the outside world actually sent.

Use:

- **Zod** for TypeScript runtime validation.
- **Pydantic** for Python runtime validation.
- **OpenAPI** as the external REST contract where applicable.

## Request flow

```text
request
  ↓
parse transport
  ↓
validate shape + bounds
  ↓
authenticate
  ↓
authorize
  ↓
execute use case
  ↓
transaction / external calls
  ↓
validate or normalize response
  ↓
response
```

## Why this matters

Without runtime validation, a system can accept malformed data despite having excellent TypeScript types. This is particularly dangerous at browser/API boundaries, webhooks, third-party integrations, environment configuration, and persisted data.

## Canonical implementation

```ts
const CreateTask = z.object({
  title: z.string().min(1).max(200),
  priority: z.enum(["low", "medium", "high"]),
});

type CreateTask = z.infer<typeof CreateTask>;
```

The schema is executable validation; the inferred type is the compile-time view.

## Do not over-centralize schemas

A shared schema package can be useful for tightly coupled TypeScript applications, but it also creates deployment and versioning coupling. For independently deployed services, keep the external contract explicit and versioned rather than assuming source-level sharing is always better.

## Production concerns

- Bound all externally controlled collections and strings.
- Return stable validation error codes.
- Never expose secrets or internal stack traces in validation errors.
- Test malformed and adversarial inputs.
- Keep authorization separate from validation.
- Version breaking API changes deliberately.
- Observe validation failures as a useful signal for client bugs and abuse.

## Related topics

- `frontend/concepts/runtime-validation.md`
- `backend/concepts/api-contracts-and-validation.md`
- `docs/stack.md`
