# HTTP Engineering

HTTP is the application protocol connecting browsers, APIs, services and many infrastructure components.

## Mental model

```text
request = method + target + headers + optional body
response = status + headers + optional body
```

The semantics matter more than memorizing endpoint conventions.

## Methods

- `GET`: retrieve a representation; should be safe and normally idempotent.
- `POST`: create or trigger processing; generally not idempotent by default.
- `PUT`: replace a resource representation; defined as idempotent.
- `PATCH`: partial modification; idempotency depends on operation design.
- `DELETE`: remove a resource; defined as idempotent in HTTP semantics.
- `HEAD`: metadata equivalent of GET without response content.
- `OPTIONS`: capability/preflight negotiation.

Idempotency is a semantic property, not a guarantee that a network request is sent only once.

## Status classes

- `2xx`: successful processing.
- `3xx`: redirection/cache behavior.
- `4xx`: request/client-side problem or authorization/resource semantics.
- `5xx`: server-side failure or inability to fulfill the request.

Use status codes consistently and return a stable machine-readable error shape.

## Headers

Important categories include caching (`Cache-Control`, `ETag`), content negotiation (`Accept`, `Content-Type`), authentication, cookies, forwarding/proxy information and conditional requests.

## Caching

HTTP caching is a protocol feature, not merely a Redis-like application cache. Understand freshness, validators, `ETag`, `Last-Modified`, `Vary`, private/public caching and invalidation semantics.

## Streaming and realtime

SSE streams server-to-client events over HTTP. WebSockets establish a bidirectional application channel. Streaming HTTP responses can reduce time-to-first-byte and improve perceived latency but require correct cancellation and buffering behavior.

## Security

HTTPS protects transport, but application security still requires authentication, authorization, CSRF defenses where applicable, input validation, output encoding, safe redirects, secure cookies and correct CORS/CSP policy.

Never trust `Host`, `Origin`, `Referer`, `X-Forwarded-*` or similar headers merely because they look authoritative; trust depends on your proxy topology.

## Production checklist

- Define timeouts and request-size limits.
- Make retryable operations explicit.
- Design idempotency keys for unsafe operations that may be retried.
- Use structured error responses.
- Define cache behavior intentionally.
- Propagate trace/request IDs.
- Measure status, latency, bytes and downstream failures.
