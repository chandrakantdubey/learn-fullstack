# Browser Architecture

The browser is a runtime, not merely a place where React renders.

## Mental model

```text
URL / Navigation
      ↓
DNS → TCP/TLS → HTTP
      ↓
Response
      ↓
HTML / CSS / JS / Images
      ↓
Parse
      ↓
DOM + CSSOM
      ↓
Render tree
      ↓
Layout
      ↓
Paint
      ↓
Composite
      ↓
Pixels
```

JavaScript runs alongside this pipeline and interacts with browser APIs.

## Core concepts

- DOM and CSSOM
- rendering pipeline
- event loop and task queues
- browser event propagation
- Fetch and streams
- cookies and storage
- same-origin policy
- CORS
- Content Security Policy
- service workers
- Web Workers
- WebSockets and SSE
- browser caching
- navigation and history

## Network boundary

A browser application is a distributed system with an unreliable client and network boundary.

Design for:

- slow networks
- retries and duplicated requests
- partial failures
- stale data
- expired authentication
- interrupted uploads/downloads
- users navigating away during work

## State categories

Separate state by ownership:

| State | Examples | Primary owner |
| --- | --- | --- |
| URL state | filters, pagination, route | browser/router |
| Server state | users, orders, feeds | backend |
| UI state | modal open, selected tab | client |
| Form state | draft fields, validation | client |
| Durable client state | preferences, offline data | browser storage |

A common architectural mistake is putting all of these into one global client store.

## Performance model

Optimize the critical path rather than chasing framework micro-optimizations.

```text
Request
  ↓
HTML
  ↓
Critical CSS / JS
  ↓
Data dependencies
  ↓
Render
  ↓
Interaction
```

Pay attention to:

- network round trips
- payload size
- JavaScript execution
- layout and paint work
- image sizes
- caching
- hydration cost
- unnecessary client components

## Security model

Treat all browser-controlled input as untrusted.

Important boundaries:

- DOM injection → XSS risk
- cross-site requests → CSRF risk
- cross-origin requests → CORS policy
- embedded content → clickjacking risk
- tokens in browser storage → theft impact

Prefer secure, HttpOnly cookies for browser sessions when they fit the authentication architecture.

## Framework connection

React, Next.js and other UI frameworks provide abstractions over this runtime. They do not replace knowledge of the browser.

Before learning framework patterns, be able to explain:

- why a component re-renders
- what a network request does
- why a page becomes slow
- why a browser blocks a request
- what happens when JavaScript crashes

## Production checklist

- responsive behavior
- accessibility
- cache headers
- compression
- secure headers
- error and loading states
- observability for client failures
- source maps without leaking secrets
- performance budgets
