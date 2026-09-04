# Temporal

**Role:** Awareness | **Layer:** Workflow orchestration

## Mental model
Temporal persists workflow execution state so long-running, failure-prone business processes can resume deterministically after crashes.

## Learn
- workflows vs activities
- deterministic workflow code
- retries and timeouts
- signals and queries
- timers and cancellation
- durable execution and versioning

## Production
Keep side effects inside activities, define explicit retry policies and timeouts, understand workflow history growth, and version workflow behavior safely.

## When useful
Use for multi-step durable business workflows where ordinary queues and cron jobs become fragile; do not introduce it merely to run simple background jobs.
