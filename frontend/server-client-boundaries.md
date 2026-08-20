# Server and Client Boundaries

Modern web applications are split across at least two execution environments: the browser and the server.

## Mental model

```text
Browser
  ├── presentation
  ├── interaction
  ├── local state
  └── network client
          │
          ▼
      HTTP boundary
          │
          ▼
Server
  ├── authentication
  ├── business rules
  ├── data access
  ├── secrets
  └── privileged operations
```

The browser is an untrusted environment. Secrets and authorization decisions do not belong there.

## What belongs on the server

- database access
- secret material
- privileged credentials
- authoritative authorization
- business invariants
- expensive or sensitive computation

## What belongs on the client

- interaction state
- visual state
- user input drafts
- optimistic UI state
- browser-only capabilities

## Data fetching

Every server interaction should have an explicit contract:

- request shape
- response shape
- authentication
- authorization
- timeout
- retry behavior
- cacheability
- error model

## SSR, SSG, ISR and client rendering

Choose based on data freshness, personalization, latency, and operational cost.

- SSR: compute HTML per request
- SSG: build static output ahead of time
- ISR/revalidation: reuse generated output and refresh it periodically/on demand
- client rendering: fetch and render after JavaScript executes

The decision is architectural, not a branding preference.

## Security rule

Never trust a value because it came from a server-rendered page. The browser can modify every client-controlled value before sending another request.

Authorization must be enforced again at the server boundary.

## API design connection

Frontend and backend should agree on durable API contracts, not internal database shapes.

Prefer domain-oriented responses over exposing arbitrary ORM models.

## Next.js connection

Next.js provides server/client components, routing, caching and rendering strategies. Learn the underlying boundary first so framework behavior is understandable rather than magical.
