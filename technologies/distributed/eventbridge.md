# Amazon EventBridge

**Role:** Primary | **Layer:** Distributed events

## Mental model
EventBridge routes events from producers to targets using event buses and rules. It is useful when producers should not know consumers.

## Learn
- event envelopes and schemas
- event buses and rules
- filtering
- retries and dead-letter handling
- scheduled events
- cross-account/event-driven designs

## Production
Define stable event contracts, include event IDs and timestamps, design consumers for duplicates, keep events integration-focused, and monitor failed deliveries.

## Related
AWS, SQS, Kafka, event-driven architecture.
