# Pino

**Role:** Primary | **Layer:** Backend observability

## Mental model
Pino is a high-performance structured logger. Logs are events represented as structured data rather than strings intended only for humans.

## Learn
- levels and structured fields
- child loggers
- serializers
- request correlation
- redaction
- transports

## Production
Log stable event names, request/trace IDs, latency and relevant dimensions. Redact credentials, tokens and sensitive payloads. Avoid expensive string construction on hot paths.

## Related
Node.js, Fastify, OpenTelemetry, Grafana/Loki.
