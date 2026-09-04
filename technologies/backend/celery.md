# Celery

**Role:** Primary | **Layer:** Background jobs

## Mental model
Celery distributes task execution from producers to workers through a broker, with optional result storage. A task is a message plus execution policy, not simply a background thread.

## Learn
- brokers and workers
- task acknowledgement
- retries and exponential backoff
- idempotency
- routing and queues
- concurrency models
- scheduled tasks

## Production
Make tasks idempotent, bound execution time, control retries, use dead-letter/error handling where supported, monitor queue age and worker health, and never assume exactly-once execution.

## Related
Redis, SQS, Kafka, reliability patterns.
