# Node.js

**Role:** Primary | **Layer:** Backend/runtime

## Mental model
Node.js runs JavaScript on a V8 engine with an event-driven runtime. I/O is generally asynchronous while JavaScript execution on the main thread remains synchronous unless work is delegated.

## Learn
- event loop and microtasks
- streams and backpressure
- buffers and binary data
- HTTP and networking
- filesystem/process APIs
- worker threads and child processes
- module systems
- graceful shutdown

## Production
Bound concurrency, propagate cancellation, stream large payloads, handle signals, expose health/readiness endpoints, and avoid CPU-heavy work on the event loop.

## Related
TypeScript, Fastify, PostgreSQL, Redis, Pino, Docker.
