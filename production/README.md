# Production Engineering

Production engineering is where correctness becomes operational reliability.

## Core areas

- Testing strategy
- Security
- Authentication and authorization
- Secrets management
- Structured logging
- Metrics
- Distributed tracing
- OpenTelemetry
- Alerting
- Reliability patterns
- Timeouts and retries
- Idempotency
- Rate limiting
- Capacity planning
- Performance engineering
- Graceful degradation
- Disaster recovery

## Production loop

```text
Build
 ↓
Test
 ↓
Deploy
 ↓
Observe
 ↓
Detect
 ↓
Diagnose
 ↓
Recover
 ↓
Improve
```

A feature is not complete when it works locally. It is complete when the team can operate it safely and understand how it behaves under failure.
