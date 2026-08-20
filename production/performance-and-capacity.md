# Performance and Capacity

Performance engineering starts with measurement. Capacity planning turns product traffic assumptions into resource requirements and scaling decisions.

## Core metrics

For APIs, track:

- throughput: requests/sec
- latency: median and tail percentiles, especially p95/p99
- error rate
- saturation: CPU, memory, connections, queue depth, I/O

Use RED for services:

```text
Rate
Errors
Duration
```

Use resource signals for infrastructure:

```text
Utilization
Saturation
Errors
```

## Capacity model

Start with a simple model:

```text
requests/sec
× average work/request
× safety factor
= required service capacity
```

For databases, estimate concurrent connections, query rate, storage growth, working set, and I/O rather than only CPU.

For queues, compare arrival rate with sustainable consumer throughput. If arrivals exceed processing rate for long enough, backlog grows without bound.

## Latency budgets

Decompose an end-to-end request:

```text
edge
 + network
 + app queue
 + application
 + cache/DB
 + downstream services
```

A p99 problem can hide inside a p50-looking average. Optimize the actual tail experienced by users.

## Optimization order

1. measure
2. identify the bottleneck
3. change one variable
4. benchmark/load test
5. verify correctness
6. observe production impact

Do not optimize based on intuition alone.

## Common bottlenecks

- N+1 database queries
- missing/incorrect indexes
- exhausted DB connection pool
- oversized payloads
- synchronous work on request path
- cache stampedes
- unbounded queues
- excessive logging
- CPU-heavy serialization or parsing
- memory leaks
- frontend JavaScript and asset cost

## Load testing

Use realistic traffic shape, not only constant load:

- ramp-up
- steady state
- burst/spike
- recovery

Measure saturation and error behavior, not only maximum requests/sec.

Representative tool: k6.

## SLOs

Define service-level objectives around user-visible outcomes, for example:

- successful request rate
- latency target
- availability window

An SLO creates an engineering budget for reliability and change velocity. Error budgets should influence release decisions.

## Project proof

Load test the task API, find the first bottleneck, document the limiting resource, introduce one justified optimization, and compare before/after results.
