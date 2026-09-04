# Observability Propagation

A distributed system is debuggable only when context survives the boundaries where work moves.

## Problem

A user request can cross a browser, API, database, queue, worker, model provider, and third-party service. Independent logs are not enough to reconstruct what happened.

## Boundary

Propagate a trace/context identity through synchronous calls and explicitly bridge it across asynchronous boundaries.

```text
request trace
  ├─ API span
  ├─ DB span
  ├─ queue publish
  │    └─ worker span
  ├─ provider call
  └─ response
```

## Invariants

- Correlation context is carried without becoming an authorization credential.
- Logs, traces, and metrics use stable identifiers and controlled cardinality.
- Async jobs preserve enough causality to link producer and consumer work.
- Telemetry never becomes a channel for secrets or unbounded user data.

## Implementation choices

Use OpenTelemetry-style trace/span context for cross-service tracing. Add structured fields such as request ID, tenant-safe identifiers, operation name, and dependency name.

For queues, propagate trace context in message metadata. Start a new consumer span while linking it to the producer context rather than pretending asynchronous execution is synchronous.

Use metrics for aggregates and traces/logs for individual causal investigation. Avoid putting raw prompts, tokens, passwords, or full request bodies into telemetry.

## Failure modes

- trace context dropped at a queue boundary
- every user ID becomes a metric label
- sampling hides the only evidence of an incident
- logging duplicate stack traces at every layer
- sensitive payloads copied into logs
- context propagation trusted as authorization

## Security

Treat trace IDs and correlation IDs as opaque metadata. Do not encode secrets or permissions into them. Redact sensitive attributes at instrumentation boundaries.

## Performance

Instrumentation must be bounded. Use batching, sampling, asynchronous exporters, and sensible attribute limits. Never let telemetry backpressure become application outage pressure.

## Operational signals

Monitor telemetry export failures, dropped spans, queue context continuity, log ingestion lag, metric cardinality, and observability pipeline resource usage.
