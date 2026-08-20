# JavaScript and TypeScript Engineering

JavaScript is the runtime language of the browser and Node.js. TypeScript adds static analysis; it does not change JavaScript runtime semantics.

## JavaScript mental model

Understand:

- lexical scope
- closures
- objects and prototypes
- functions as values
- `this`
- modules
- promises
- event loop
- microtasks and tasks
- exceptions
- streams and async iteration

```text
Call Stack
    ↓
JavaScript execution
    ↓
Web APIs / Node APIs
    ↓
Tasks + Microtasks
    ↓
Event Loop
```

## Async programming

Use promises and `async`/`await` for ordinary asynchronous control flow.

Know the difference between:

- sequential awaits
- concurrent independent work
- cancellation/abandonment
- timeouts
- retries
- backpressure

Do not confuse asynchronous I/O with parallel CPU execution.

## TypeScript mental model

TypeScript provides compile-time constraints around JavaScript programs.

Important concepts:

- structural typing
- type inference
- unions and intersections
- discriminated unions
- generics
- narrowing
- utility types
- interfaces vs type aliases
- `unknown` vs `any`
- strict mode
- runtime validation

TypeScript types disappear at runtime. External data must therefore be validated at runtime.

## Runtime boundaries

Validate data crossing boundaries:

```text
HTTP request
   ↓
Runtime schema validation
   ↓
Typed application data
   ↓
Business logic
   ↓
Database
```

Useful tooling includes Zod, Valibot, or equivalent schema libraries.

## Node.js connection

Node.js uses V8 for JavaScript execution and provides asynchronous I/O through its runtime/platform APIs.

Understand:

- process lifecycle
- event loop
- streams
- buffers
- filesystem APIs
- HTTP server APIs
- worker threads
- child processes
- environment variables

For CPU-heavy work, consider worker threads, separate workers, or another service rather than blocking the event loop.

## Production conventions

- enable strict TypeScript settings
- avoid `any` at application boundaries
- validate external input
- preserve error context
- set request timeouts
- use structured logging
- keep dependencies minimal
- pin and audit production dependencies
- test both type-level assumptions and runtime behavior

## Stack direction

The canonical server-side TypeScript stack for this repository is:

- Node.js
- TypeScript
- Fastify or a similarly lightweight HTTP framework
- PostgreSQL via `pg` plus a deliberate query/data layer
- Redis when caching or coordination is required
- Vitest for unit/integration tests
- Playwright for end-to-end browser tests
