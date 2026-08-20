# Performance and Capacity Engineering

Performance is predictable system behavior under a defined workload. Capacity planning turns vague scale claims into resource estimates and limits.

## Start with workload

Define:

- requests/second
- peak requests/second
- concurrency
- payload sizes
- read/write ratio
- database operations/request
- cache hit rate
- background work rate
- latency targets
- availability target

A useful first-pass estimate:

```text
concurrency ≈ throughput × average latency
```

Use measured values, then validate with load tests.

## Latency budget

```text
Total request budget
 ├── CDN/network
 ├── frontend/server rendering
 ├── API processing
 ├── database
 └── external dependencies
```

Optimize the dominant contributor, not the most interesting component.

## Backend bottlenecks

Look for:

- N+1 queries
- missing/poor indexes
- oversized payloads
- excessive serialization
- connection-pool exhaustion
- CPU saturation
- memory pressure
- lock contention
- external dependency latency

## Caching

Cache only when the consistency model is understood.

Measure:

- hit rate
- miss latency
- eviction rate
- memory usage
- stale-read impact

## Load testing

Use k6 or an equivalent tool to test:

- steady-state load
- ramp-up
- peak burst
- sustained stress
- dependency degradation

Do not confuse a synthetic benchmark with production behavior.

## Autoscaling

Scaling signals should reflect the bottleneck: CPU, memory, request concurrency, queue depth, or custom application metrics.

Set both scale-up and scale-down behavior deliberately to avoid oscillation.

## SLI / SLO

Examples:

- availability SLI: successful requests / total requests
- latency SLI: request latency under target
- freshness SLI: data age under target

SLOs create a reliability budget that helps prioritize engineering work.

## Profiling

Use tracing, CPU profiles, memory profiles, query plans, and runtime metrics to find actual bottlenecks before optimizing.
