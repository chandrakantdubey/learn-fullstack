# Amazon SQS

**Role:** Primary | **Layer:** Distributed messaging

## Mental model
SQS is a managed queue that decouples producers from consumers. Standard queues favor scale and at-least-once delivery; FIFO queues add stronger ordering/deduplication semantics with different throughput characteristics.

## Learn
- visibility timeout
- long polling
- dead-letter queues
- retries and redrive
- standard vs FIFO
- idempotent consumers
- message size and batching

## Production
Set visibility timeout above normal processing time, extend it for long work, use DLQs, bound retries, monitor age of oldest message, and make handlers idempotent.

## Related
AWS, Celery, EventBridge, outbox pattern.
