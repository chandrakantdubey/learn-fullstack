# HTTPX

**Role:** Primary | **Layer:** Python HTTP client

## Mental model
HTTPX provides synchronous and asynchronous HTTP clients with connection pooling, timeouts and HTTP/2 support.

## Learn
- Client lifecycle and pooling
- connect/read/write/pool timeouts
- retries and failure classification
- streaming
- async usage and cancellation
- authentication and proxies

## Production
Reuse clients, set explicit timeouts, bound concurrency, retry only safe/transient failures, propagate request IDs where appropriate, and avoid logging credentials or response bodies by default.

## Related
FastAPI, distributed systems, OpenAPI, service-to-service communication.
