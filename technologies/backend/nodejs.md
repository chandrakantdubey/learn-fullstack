# Node.js

**Role:** Primary | **Layer:** Backend/runtime

## Mental model
Node.js executes JavaScript on V8 with an event-driven runtime. JavaScript execution is generally single-threaded per process, while the runtime and operating system provide asynchronous I/O and worker mechanisms.

```text
request -> event loop -> async I/O -> continuation
                         |
                         +-> worker pool for selected operations
```

The key engineering constraint is not simply "Node is single threaded". It is that CPU-heavy JavaScript blocks the event loop and therefore delays unrelated requests.

## Event loop
Understand timers, I/O callbacks, poll phases, `process.nextTick`, promise microtasks and how long synchronous work affects tail latency. A service can have low average latency while suffering severe p99 latency from event-loop blocking.

## Async and concurrency
Promises provide composition, not automatic parallelism. Bound concurrency when fan-out depends on user input or large datasets. Use cancellation/abort signals for requests whose results are no longer needed.

## Streams and backpressure
Streams allow data to move incrementally without buffering an entire payload in memory. Backpressure prevents a fast producer from overwhelming a slower consumer.

Use streams for large files, proxies and data pipelines where memory and latency matter.

## HTTP services
Understand request parsing, headers, keep-alive, connection limits, timeouts, body limits and graceful shutdown. Every outbound dependency needs explicit timeout behavior.

## Buffers
Buffers represent binary data. Be careful with unbounded body reads, base64 expansion and file uploads. Set size limits at the HTTP boundary.

## Worker threads and processes
Use worker threads or separate processes/services for CPU-intensive work. Processes also provide stronger isolation. For durable background work, prefer an explicit queue rather than relying on in-process memory.

## Module systems
Understand ESM/CJS interoperability, package exports, module initialization and circular dependencies. Keep startup side effects controlled.

## Process lifecycle
Handle `SIGTERM` and `SIGINT`, stop accepting new work, drain in-flight requests where possible, close database/message connections and exit within a bounded grace period.

## Production patterns
- Set request, connection and outbound timeouts.
- Bound request body sizes and concurrency.
- Avoid synchronous CPU-heavy APIs on hot paths.
- Use structured logging with correlation/trace context.
- Expose health/readiness semantics appropriate to deployment.
- Keep configuration external to the image.
- Monitor event-loop delay and memory usage.

## Failure modes
Watch for event-loop stalls, memory leaks, unhandled rejections, connection-pool exhaustion, slow upstreams, retry storms and process crashes. A retry without a timeout is not a reliability strategy.

## Performance
Track throughput, p50/p95/p99 latency, event-loop utilization/delay, heap usage, GC behavior, open connections and outbound dependency latency. Optimize allocations and serialization only after profiling identifies them.

## Security
Avoid dynamic code execution, unsafe child-process arguments, arbitrary filesystem paths and untrusted deserialization. Keep dependencies patched and secrets out of logs/environment exposure to clients.

## Testing
Unit-test application logic, integration-test HTTP/database boundaries and use browser tests for user journeys. Test timeout and shutdown behavior explicitly for critical services.

## Common mistakes
- unbounded `Promise.all`
- missing timeouts
- CPU-heavy work in request handlers
- buffering huge responses
- assuming async means non-blocking CPU execution
- graceful shutdown that only closes the HTTP listener

## Interview-level topics
Event loop phases, microtasks, streams/backpressure, worker threads, process lifecycle, connection pooling, cancellation, memory leaks, tail latency and graceful shutdown.

## Related
TypeScript, Fastify, PostgreSQL, Redis, Pino, Docker.