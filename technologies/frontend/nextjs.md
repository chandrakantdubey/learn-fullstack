# Next.js

**Role:** Primary | **Layer:** Frontend/full-stack web

## Mental model
Next.js is an application framework around React that combines routing, server rendering, server components, data fetching, caching/revalidation, static generation and deployment conventions.

## Core areas
- App Router and layouts
- Server vs Client Components
- route handlers and middleware
- server actions/forms
- loading, error and not-found boundaries
- metadata and streaming
- caching, revalidation and invalidation
- image/font optimization and bundling

## Production patterns
Keep server-only code out of client bundles, define explicit cache semantics, validate route inputs, protect mutations, and treat authorization as server-side logic. Design loading/error states as part of the UI contract.

## Performance
Optimize network waterfalls, server work, JavaScript shipped to browsers, cache hit rates and database access. Do not add client components merely for convenience.

## Related
React, TypeScript, Zod, OpenAPI, TanStack Query, Playwright.
