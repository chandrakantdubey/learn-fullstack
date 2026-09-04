# Runtime Validation with Zod

TypeScript types disappear at runtime. Data crossing a trust boundary is still untyped JavaScript, even when the TypeScript compiler says the shape is correct.

## The problem

External data can come from:

- browser forms
- URL parameters
- cookies and headers
- local storage
- backend APIs
- third-party APIs
- webhooks
- environment variables
- persisted or cached data

A TypeScript interface does not validate any of these values.

## Mental model

```text
untrusted data
     ↓
Zod schema
     ↓
parse / safeParse
     ↓
validated value
     ↓
typed application logic
```

## Why Zod belongs in the canonical stack

Zod provides runtime schemas that can also produce TypeScript types. This makes it useful at application boundaries rather than as a replacement for TypeScript itself.

```ts
import { z } from "zod";

const UserSchema = z.object({
  id: z.string().uuid(),
  name: z.string().min(1),
  email: z.string().email(),
});

type User = z.infer<typeof UserSchema>;

const result = UserSchema.safeParse(input);

if (!result.success) {
  // map validation issues to a stable UI error
} else {
  const user: User = result.data;
}
```

## Where to validate

Validate at boundaries, not everywhere.

### Forms

Use React Hook Form for form state and Zod for the schema.

```text
Form input
  ↓
React Hook Form
  ↓
Zod resolver
  ↓
validated command
```

### API responses

Do not blindly trust a successful HTTP response. When the response is security- or correctness-sensitive, validate the payload before it enters domain logic.

```text
fetch
  ↓
JSON
  ↓
Zod response schema
  ↓
application state
```

### Environment configuration

Environment variables are strings and should be parsed into a typed configuration object before application startup.

## `parse` vs `safeParse`

Use `parse` when invalid data is an exceptional programmer/configuration failure and throwing is appropriate.

Use `safeParse` when invalid input is expected and should become a controlled error response or UI state.

## Zod is not authorization

Validation answers:

> Is this value structurally and semantically valid?

Authorization answers:

> Is this principal allowed to perform this action?

A valid request can still be forbidden.

## Zod and API contracts

For a TypeScript-heavy fullstack system:

```text
React / Next.js
      │
      │ request schema
      ▼
Fastify / Node.js
      │
      │ domain command
      ▼
application service
      │
      ▼
PostgreSQL
```

Zod should sit at the edges. Business rules should remain in the application/domain layer.

## Production considerations

- Reject malformed input early.
- Bound strings, arrays, files, and numeric ranges.
- Never log secrets or full sensitive payloads on validation failure.
- Return stable machine-readable error codes where clients depend on them.
- Keep schemas versioned when API compatibility matters.
- Avoid duplicating validation logic across unrelated layers without a clear ownership model.
- Treat external API responses as untrusted data.

## Connects to

- `frontend/` — forms, data fetching, and client/server boundaries
- `backend/concepts/service-architecture.md` — validation in the request path
- `backend/typescript-technology-inventory.md` — TypeScript backend stack
- `docs/stack.md` — canonical stack
