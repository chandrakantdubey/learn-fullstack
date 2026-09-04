# RabbitMQ

**Role:** Alternative | **Layer:** Distributed messaging

## Mental model
RabbitMQ is a broker built around exchanges, queues, bindings and acknowledgements. Routing decisions can be separated from queue consumption.

## Learn
- direct/topic/fanout exchanges
- routing keys
- acknowledgements and prefetch
- durable queues/messages
- dead-lettering and retries
- publisher confirms

## Production
Control prefetch, use durable topology where required, make consumers idempotent, design retry/dead-letter flows explicitly, and monitor queue depth and consumer health.

## Tradeoff
RabbitMQ is excellent for broker-centric routing and work queues; Kafka is generally the better mental model for durable high-throughput event logs and replay.
