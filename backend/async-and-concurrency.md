# Async and Concurrency

Concurrency is about structuring multiple units of work so they can make progress without waiting unnecessarily. Parallelism is simultaneous execution. They are related, but not interchangeable.

## Mental model

```text
CPU-bound work
  → parallel CPU execution

I/O-bound work
  → concurrent waiting
```

For typical web services, most latency is waiting on network, database, filesystem, or another service. Async I/O can improve throughput by allowing a worker to make progress on other requests while one operation waits.

## Python

The central model is `asyncio`:

```text
Event loop
  ├── request A → waiting for DB
  ├── request B → running application code
  └── request C → waiting for HTTP
```

Async code does not make CPU work magically faster. CPU-heavy work may require processes, native extensions, or a separate worker pool.

## TypeScript / Node.js

Node.js uses an event loop with non-blocking I/O. A single JavaScript thread can coordinate many I/O-bound operations, while the runtime delegates suitable work to the operating system or worker pool.

Blocking the event loop is therefore a production problem.

## Concurrency hazards

- race conditions
- shared mutable state
- deadlocks
- starvation
- unbounded task creation
- connection-pool exhaustion
- retry storms
- backpressure failure

## Backpressure

If producers create work faster than consumers can process it, the system needs a limit.

```text
producer → bounded queue → consumers
```

Bound queues, cap concurrency, and decide what happens when capacity is exhausted.

## Request fan-out

A common service pattern is:

```text
request
 ├── user service
 ├── pricing service
 └── inventory service
```

Run independent calls concurrently, but enforce an overall deadline. The slowest dependency often dominates tail latency.

## Practical rule

Use concurrency because it matches the workload, not because async syntax looks modern. Measure latency, throughput, CPU, memory, and dependency behavior.

## Connects to

`backend/service-architecture.md`, `systems/networking.md`, `data/postgresql.md`, and `production/reliability.md`.
