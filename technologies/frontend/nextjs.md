# Next.js

**Role:** Primary | **Layer:** Frontend/full-stack web

## Mental model
Next.js is an application framework around React. Its important architectural decision is where work happens: browser, server, edge/runtime, cache, database or external service.

```text
Browser
  -> route/render boundary
  -> server work
      -> cache
      -> API/domain
      -> database/external services
```

Do not treat framework defaults as business semantics. Make rendering, caching and authorization behavior explicit.

## App Router
Learn layouts, pages, route segments, loading boundaries, error boundaries, not-found handling, route handlers and metadata. Nested layouts provide stable UI structure while route segments define navigation and data boundaries.

## Server and Client Components
Server Components reduce browser JavaScript and can access server-only resources. Client Components are required for browser state, event handlers and APIs unavailable on the server.

Use the smallest client boundary that satisfies the interaction. Do not move an entire page to the client merely because one control is interactive.

## Data fetching
Understand where requests execute, request waterfalls, parallel fetching, caching and revalidation. Keep data access close to the boundary that owns it while maintaining a clean domain/application layer.

## Caching
Caching is a correctness decision as well as a performance decision. Define:
- what is cached
- cache key
- lifetime
- invalidation trigger
- authorization scope
- acceptable staleness

Never allow user-specific data to become accidentally shared through an incorrectly scoped cache.

## Mutations
Mutations need authentication, authorization, input validation, idempotency where retries are possible, clear error handling and cache invalidation. Server-side authorization is mandatory even when the UI hides controls.

## Streaming
Streaming lets the server progressively deliver UI/data instead of waiting for the entire tree. Use loading boundaries intentionally and design partial states as real product states.

## Route handlers
Treat route handlers as HTTP adapters. Parse/validate inputs, authenticate, authorize, invoke application logic, then serialize a stable response. Avoid putting large business workflows directly into route handlers.

## Middleware/proxy concerns
Use request interception only for concerns that belong at that boundary. Avoid turning middleware into a hidden application server with database calls and complex business logic.

## Performance
Measure:
- server response latency
- TTFB
- browser JavaScript shipped
- cache hit rate
- database latency
- external API latency
- hydration/client work
- network waterfalls

Optimize the dominant bottleneck, not the framework abstraction you happen to notice first.

## Security
Keep secrets server-side. Treat cookies, redirects, headers, file uploads, URL parameters and server actions as security-sensitive boundaries. Validate input and authorize every mutation/resource access.

## Deployment
Understand Node/server deployments, static assets, environment variables, build-time vs runtime configuration, health checks and graceful shutdown. Framework behavior can differ between development and production builds.

## Common mistakes
- using client components by default
- unclear cache semantics
- authorization implemented only in the UI
- duplicated data-fetching layers
- giant route handlers
- exposing secrets through environment variables intended for the browser
- ignoring loading/error states

## Interview-level topics
Server/client component boundaries, rendering strategies, caching and revalidation, streaming, route handlers, data waterfalls, bundle boundaries, authorization, deployment architecture and failure behavior.

## Related
React, TypeScript, Zod, OpenAPI, TanStack Query, Playwright.