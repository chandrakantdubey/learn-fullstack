# Concurrency, Parallelism and Cancellation

Concurrency is about managing multiple in-flight tasks; parallelism is executing work simultaneously on multiple execution resources. They overlap but are not the same.

## Mental model

```text
work
 ├─ CPU-bound → parallel execution may help
 └─ I/O-bound → concurrency can keep resources busy while waiting
```

The right model depends on the runtime. JavaScript commonly coordinates asynchronous I/O through an event loop. Python supports async I/O plus threads/processes and other execution models. Native services may use threads, processes and event-driven I/O.

## Core concepts

- task/future/promise
- event loop
- thread
- process
- mutex/lock
- semaphore
- queue
- atomic operation
- race condition
- deadlock
- starvation
- backpressure
- cancellation

## Correctness before throughput

A concurrent system needs explicit invariants. Typical failures include two workers updating the same state, duplicate message handling, check-then-act races and resource exhaustion.

Use the narrowest synchronization mechanism that protects the invariant. Prefer immutable data, ownership boundaries and message passing when they simplify reasoning.

## Async I/O

Async does not make CPU work faster. It allows a worker to make progress on other tasks while an operation is waiting on I/O. CPU-heavy work can block an event loop unless it is moved to an appropriate worker/process or otherwise bounded.

## Backpressure

If producers can create work faster than consumers can process it, an unbounded queue only moves the failure into memory. Backpressure limits outstanding work.

```text
producer → bounded buffer → consumer
             ↑
          pressure
```

Apply limits to HTTP concurrency, database connections, queue depth, model inference requests and outbound calls.

## Cancellation

Timeouts without cancellation can leave work running after the caller has given up. Propagate cancellation through HTTP requests, database operations, child tasks and downstream work where the runtime supports it. Design cleanup to be safe if cancellation happens at any point.

## Distributed concurrency

A process-local lock does not protect shared state across machines. Distributed coordination requires a shared authority or an architecture that avoids coordination. Even distributed locks need leases, expiry, fencing and failure analysis to be trustworthy.

## Production checklist

- Bound concurrency.
- Bound queues.
- Set deadlines/timeouts.
- Propagate cancellation.
- Avoid blocking event loops.
- Make retries safe through idempotency.
- Instrument queue depth and wait time.
- Test races and overload, not only happy paths.
