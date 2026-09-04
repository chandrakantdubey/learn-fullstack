# TypeScript Stack in Fullstack Engineering

This repo treats `learn-js-ts` as the language-depth source of truth. This file explains the TypeScript stack used for production browser and server work.

## Canonical application path

```text
TypeScript
  ↓
strict types / modules / async
  ↓
React + Next.js
  ↓
TanStack Query / Zustand / React Hook Form
  ↓
Zod runtime validation
  ↓
API contract
  ↓
Node.js + Fastify
  ↓
Zod runtime validation
  ↓
PostgreSQL + Redis
  ↓
Vitest + Playwright
  ↓
pnpm
  ↓
Docker + observability
```

## Default choices

| Need | Default |
| --- | --- |
| Runtime | Node.js |
| Package manager | pnpm |
| Language | TypeScript with strict mode |
| UI | React |
| Fullstack framework | Next.js |
| Component primitives | Radix UI + shadcn/ui |
| Client state | Zustand; Redux Toolkit when justified |
| Server state | TanStack Query |
| Forms | React Hook Form |
| Runtime validation | **Zod** |
| HTTP service | Fastify |
| Outbound HTTP | native `fetch` |
| API contract | OpenAPI for REST |
| PostgreSQL | `pg` |
| SQL / ORM | Drizzle or Prisma when ORM features are justified |
| Cache | Redis |
| Background jobs | BullMQ or a focused worker |
| Testing | Vitest |
| E2E | Playwright |
| Logging | Pino |
| Async runtime | Node.js event loop |

## Zod's role

TypeScript gives compile-time guarantees. Zod validates actual runtime data.

```text
unknown data
    ↓
Zod schema
    ↓
validated value
    ↓
typed application logic
```

Use it at trust boundaries such as:

- form submissions
- API request bodies
- query/path parameters
- environment configuration
- third-party API responses
- webhook payloads
- persisted data that may have changed shape

Do not use Zod as a replacement for authorization or domain rules.

## Engineering focus

Focus on runtime behavior, the event loop, promises, streams, type boundaries, runtime validation, API contracts, error handling, module architecture, dependency ownership, testing, performance, security, and operational behavior.

Deep JavaScript and TypeScript language coverage remains in `learn-js-ts`.
