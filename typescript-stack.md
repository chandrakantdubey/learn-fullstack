# TypeScript Stack in Fullstack Engineering

This repo treats `learn-js-ts` as the language-depth source of truth. This file explains the TypeScript stack used for production browser and server work.

## Canonical path

```text
TypeScript
  ↓
strict types / modules / async
  ↓
Node.js runtime
  ↓
Fastify or framework boundary
  ↓
validation
  ↓
PostgreSQL client / ORM
  ↓
Redis
  ↓
Vitest + Playwright
  ↓
pnpm + package scripts
  ↓
Docker + observability
```

## Default choices

| Need | Default |
| --- | --- |
| Runtime | Node.js |
| Package manager | pnpm |
| Language | TypeScript with strict mode |
| HTTP | native `fetch` for outbound calls; Fastify for focused HTTP services |
| Validation | Zod |
| PostgreSQL | `pg` plus Drizzle or Prisma when ORM features are justified |
| Testing | Vitest |
| E2E | Playwright |
| Lint/format | ESLint + Prettier or a unified modern toolchain where appropriate |
| Logging | Pino |
| Async runtime | Node.js event loop |

## Engineering focus

Focus on runtime behavior, the event loop, promises, streams, type boundaries, error handling, module architecture, dependency ownership, testing, and operational behavior.

Deep JavaScript and TypeScript language coverage remains in `learn-js-ts`.
