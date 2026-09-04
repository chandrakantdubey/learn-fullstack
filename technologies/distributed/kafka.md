# Kafka

**Role:** Primary | **Layer:** Distributed messaging

## Mental model
Kafka is a distributed append-only log. Producers write records to partitions; consumers track offsets and process records independently.

## Learn
- topics and partitions
- keys and ordering
- consumer groups and offsets
- retention and compaction
- replication and leader election
- delivery semantics
- schemas and compatibility

## Production
Partition from access/order requirements, use stable keys, commit offsets according to processing semantics, make consumers idempotent, monitor consumer lag and avoid oversized messages.

## Related
Event-driven architecture, SQS, EventBridge, outbox pattern, stream processing.
