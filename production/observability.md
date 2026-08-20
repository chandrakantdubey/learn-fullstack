# Observability

Observability is the ability to infer system behavior from emitted telemetry.

## Three signals

### Logs

Use structured logs for discrete events and diagnostics.

Include fields such as:

- timestamp
- service
- environment
- severity
- request_id
- trace_id
- user/tenant identifier when safe
- event name
- error type

Do not put passwords, tokens, or sensitive payloads into logs.

### Metrics

Use metrics for aggregate behavior.

Important families:

- request rate
- error rate
- latency distributions
- saturation
- queue depth
- worker throughput
- database pool utilization
- cache hit rate

### Traces

Distributed traces connect work across services and dependencies.

```text
HTTP request
   ├── API span
   │    ├── DB span
   │    ├── Redis span
   │    └── queue publish span
   └── worker trace
        └── external API span
```

## OpenTelemetry

Use OpenTelemetry as the instrumentation boundary where practical. It provides portable APIs/SDKs for traces, metrics, and logs so application code is less coupled to a vendor.

## Alerting

Alert on symptoms that require action, not every internal fluctuation.

Good alert:

> API error budget burn is high enough that the current incident threatens the service objective.

Poor alert:

> CPU crossed 70% for five minutes.

CPU may be healthy while latency and errors remain normal.

## Golden signals

For request-serving systems, start with:

- latency
- traffic
- errors
- saturation

Then add domain metrics such as completed orders, failed jobs, or queue age.

## Project proof

Instrument the task platform end-to-end with OpenTelemetry. Expose request latency/error metrics, trace API→PostgreSQL→Redis→worker flows, centralize structured logs, and create actionable alerts.