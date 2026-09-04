# TypeScript Stack in Fullstack Engineering

This repo treats `learn-js-ts` as the language-depth source of truth. This file describes the TypeScript stack used for production browser and server work.

Technology-specific notes live under `technologies/`, with one canonical file per technology.

## Canonical application path

```text
TypeScript
  ↓
React + Next.js
  ↓
TanStack Query / Zustand / React Hook Form
  ↓
Zod (shared runtime schema)
  ↓
API contract
  ↓
Node.js + Fastify
  ↓
PostgreSQL + Redis
  ↓
Vitest + Playwright
  ↓
pnpm
  ↓
Docker + observability
```

Zod appears in both frontend and TypeScript backend systems because it serves the same cross-layer role: runtime schemas at trust boundaries. The repository maintains a single Zod note at `technologies/shared/zod.md`.

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
| Runtime schemas | Zod |
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

## Engineering focus

Focus on runtime behavior, the event loop, promises, streams, type boundaries, runtime schemas, API contracts, error handling, module architecture, dependency ownership, testing, performance, security, and operational behavior.

Deep JavaScript and TypeScript language coverage remains in `learn-js-ts`.
