# Frontend Performance

Frontend performance is primarily a systems problem: network, bytes, CPU, rendering, and caching all contribute to perceived latency.

## Mental model

```text
User action
  ↓
Network latency
  ↓
Server response
  ↓
Download / parse
  ↓
JavaScript execution
  ↓
Render / layout / paint
  ↓
Interaction readiness
```

## Core Web Vitals

Track the major user-facing signals:

- Largest Contentful Paint (LCP): loading performance
- Cumulative Layout Shift (CLS): visual stability
- Interaction to Next Paint (INP): interaction responsiveness

Use field data when possible; synthetic tools are diagnostics, not proof of real-user behavior.

## Main levers

### Network

- reduce round trips
- compress responses
- use appropriate cache headers
- use a CDN for static assets
- avoid serial data dependencies where requests can run concurrently

### JavaScript

- remove unnecessary dependencies
- code split large routes/features
- lazy load non-critical features
- avoid shipping server-only code to the browser
- measure bundle composition

### Images

- serve appropriately sized images
- use modern formats where supported
- reserve dimensions to avoid layout shifts
- lazy load below-the-fold media

### Rendering

- reduce unnecessary rerenders
- avoid forced synchronous layout
- avoid long tasks on the main thread
- move suitable CPU-heavy work to Workers or the server

## Caching hierarchy

```text
Browser cache
    ↓
CDN cache
    ↓
Application cache
    ↓
Database
```

Every cache adds complexity. Define invalidation and freshness rules before adding it.

## Measurement tools

- browser Performance panel
- Lighthouse
- WebPageTest
- bundle analyzers
- production RUM

## Rule

Measure first. Optimize the dominant bottleneck. Re-measure after the change.
