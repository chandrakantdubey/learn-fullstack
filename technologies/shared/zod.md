# Zod

> TypeScript-first runtime schema validation.

**Status:** Primary
**Used by:** Frontend + TypeScript backend
**Canonical note:** This is the only technology note for Zod in the repository.

## What it is

Zod lets us describe data schemas and execute those schemas at runtime. It also infers TypeScript types from the schemas.

```text
TypeScript
  └── compile-time types

Zod
  └── runtime schemas

External data
  ↓
Zod schema
  ↓
validated data
  ↓
application code
```

## Why we use it

TypeScript does not validate data at runtime. HTTP bodies, query parameters, forms, environment variables, webhooks, third-party responses, and persisted data can all violate the types our code expects.

Zod gives the TypeScript stack a single executable schema that can act as the runtime boundary and provide an inferred static type.

## Where it belongs

Use Zod at **trust boundaries**:

- API request bodies
- API query/path parameters
- browser form input
- environment configuration
- webhook payloads
- third-party API responses
- untrusted persisted/cached data
- structured external model/tool output when appropriate

Do not put Zod validation around every internal function. Once data has crossed the boundary and has been normalized, domain/application code should use domain types and invariants.

## Core API

The notes we will build here should cover:

- primitives
- objects and arrays
- enums and literals
- unions/discriminated unions
- optional / nullable / nullish
- defaults
- records / maps / sets / tuples
- refinements and checks
- transforms
- coercion
- parsing
- `safeParse`
- asynchronous parsing
- error handling and formatting
- type inference
- input vs output types
- JSON Schema interoperability
- codecs and advanced composition

## Basic shape

```ts
import * as z from "zod";

const UserSchema = z.object({
  id: z.string(),
  email: z.email(),
  name: z.string().min(1),
});

type User = z.infer<typeof UserSchema>;

const result = UserSchema.safeParse(input);

if (!result.success) {
  // controlled validation failure
} else {
  const user: User = result.data;
}
```

## Frontend role

Zod is the schema layer. Other frontend technologies own their own responsibilities:

```text
React Hook Form → form state / submission lifecycle
Zod             → schema + runtime validation
React            → UI
TanStack Query   → server state
```

The schema should not become the form state manager or authorization layer.

## TypeScript backend role

```text
HTTP request
    ↓
transport parsing
    ↓
Zod
    ↓
validated command
    ↓
authentication / authorization
    ↓
application/domain logic
```

The same Zod technology can therefore appear on both sides of a TypeScript fullstack system without creating two Zod notes.

## What Zod does not replace

- TypeScript's static type system
- authentication
- authorization
- domain invariants
- database constraints
- API versioning
- OpenAPI as an external REST contract
- business logic

## Production concerns

- Validate at boundaries rather than everywhere.
- Bound externally controlled strings, arrays, files, and numbers.
- Decide explicitly whether malformed input is expected (`safeParse`) or exceptional (`parse`).
- Never log secrets or sensitive payloads merely because validation failed.
- Keep stable error codes at API boundaries instead of exposing internal schema details as a public contract.
- Be deliberate about transforms/coercion because they change the relationship between input and output types.
- Keep schemas owned by the boundary/domain that owns the contract; avoid an enormous global schema package by default.

## Alternatives

The repository inventory also tracks libraries such as Valibot, Joi, Yup, Ajv, and TypeBox. They are alternatives, not additional validation systems that must be learned to the same depth.

## Official reference

- https://zod.dev/
- https://zod.dev/basics
- https://zod.dev/api
- https://zod.dev/json-schema

## Related repository notes

- `technologies/frontend/react-hook-form.md`
- `technologies/backend/fastify.md`
- `technologies/shared/typescript.md`
- `backend/concepts/api-contracts-and-validation.md`
