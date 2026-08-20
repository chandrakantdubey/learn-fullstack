# HTTP for Fullstack Engineers

HTTP is the contract that connects browsers, APIs, services, gateways, and many infrastructure components.

A Fullstack Engineer should understand HTTP well enough to design APIs, debug production traffic, reason about latency and caching, and understand what frameworks are doing underneath.

## Mental model

```text
HTTP request
  ├── method
  ├── target / URL
  ├── headers
  ├── optional body
  │
  ▼
HTTP response
  ├── status
  ├── headers
  └── optional body
```

The protocol itself is deliberately simple. Complexity comes from application semantics, authentication, caching, proxies, retries, and distributed systems built on top of it.

## Methods

Know the semantics of:

- `GET` — retrieve a representation
- `POST` — create/process with server-defined semantics
- `PUT` — replace a resource representation
- `PATCH` — partially modify a resource
- `DELETE` — remove a resource
- `HEAD` — retrieve headers without the response body
- `OPTIONS` — discover communication options

The important engineering concept is **idempotency**, not memorizing method names.

## Status codes

Think in classes first:

```text
2xx -> success
3xx -> redirection / cache-related behavior
4xx -> client/request problem
5xx -> server/dependency problem
```

Important examples:

```text
200 OK
201 Created
202 Accepted
204 No Content
301/308 Redirect
304 Not Modified
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
412 Precondition Failed
422 Unprocessable Content
429 Too Many Requests
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```

Choose status codes as part of the API contract. Do not return `200` for every outcome just because the framework makes it easy.

## Headers

Know why these matter:

### Representation

```text
Content-Type
Content-Length
Content-Encoding
Accept
Accept-Encoding
```

### Caching

```text
Cache-Control
ETag
If-None-Match
Last-Modified
If-Modified-Since
Age
Vary
```

### Security

```text
Authorization
Set-Cookie
Cookie
Origin
Content-Security-Policy
Strict-Transport-Security
```

### Tracing / operational context

```text
traceparent
request-id
x-request-id
```

## URLs and resources

For REST APIs, model URLs around stable resources and relationships.

Prefer:

```text
GET /users/123
GET /users/123/orders
POST /orders
GET /orders/456
```

over RPC-like URLs unless the operation truly represents a command:

```text
POST /orders/456/cancel
```

There is no universal rule. The design should make semantics obvious.

## Request bodies and serialization

Common formats:

- JSON
- form URL encoded
- multipart form data
- plain text
- binary streams

Understand that serialization has costs:

```text
Object
 -> serialization
 -> bytes
 -> network
 -> parsing
 -> object
```

Large payloads affect latency, memory, bandwidth, and CPU.

## Cookies and sessions

Cookies are browser-managed state sent with HTTP requests.

Understand:

- `Secure`
- `HttpOnly`
- `SameSite`
- Domain
- Path
- Expiration

A traditional session architecture is:

```text
Browser
  -> session cookie
  -> application
  -> server-side session store
```

A token-based architecture may instead encode identity/claims in a token, but that does not make authentication state-free in every system.

## CORS

CORS is a browser security mechanism. It is not an API authentication mechanism and not a server-to-server networking feature.

Understand:

- Origin
- Simple request
- Preflight
- `Access-Control-Allow-Origin`
- Allowed methods
- Allowed headers
- Credentialed requests

The correct mental model is:

```text
Browser enforces origin policy
      ↓
Server declares which cross-origin requests are allowed
```

## Caching

A cache is a correctness decision as much as a performance decision.

Understand:

- Freshness
- TTL
- Validation
- `ETag`
- Conditional requests
- Cache-Control directives
- Public vs private caches
- CDN behavior
- Cache invalidation

Example:

```text
Client
  ├── fresh -> use cached response
  └── stale -> conditional request
                 ├── 304 -> keep old response
                 └── 200 -> replace cached response
```

## Retries and idempotency

Retries amplify traffic.

Never blindly retry every request.

Reason about:

- Timeout
- Idempotency
- Backoff
- Jitter
- Maximum attempts
- Retry budgets
- Load on dependencies

For a retriable operation, an idempotency key can protect against duplicate effects:

```text
POST /payments
Idempotency-Key: 7b5...
```

The server records the result associated with the key and safely reuses it for duplicate submissions.

## Streaming and real-time HTTP

Understand:

- Chunked transfer
- Server-Sent Events
- WebSockets
- Long polling

These are useful for different interaction patterns.

For AI applications in particular:

```text
User
  -> API
  -> model inference
  -> token stream
  -> browser
```

SSE is often sufficient for one-way token streaming from server to browser.

## HTTP versions

### HTTP/1.1

Text-based request/response protocol with connection reuse and persistent connections.

### HTTP/2

Adds binary framing and multiplexing over a connection, reducing some head-of-line problems at the HTTP layer.

### HTTP/3

Uses QUIC over UDP and provides modern transport behavior for web traffic.

You should understand the trade-offs without needing to implement any of the protocols.

## API design checklist

Before shipping an endpoint, define:

- Resource / operation semantics
- Request schema
- Response schema
- Error contract
- Authentication
- Authorization
- Idempotency
- Pagination
- Rate limiting
- Caching behavior
- Timeouts
- Observability fields
- Backward compatibility

## Debugging

Use raw HTTP tools before blaming the framework:

```bash
curl -v https://api.example.com/users/123
curl -I https://example.com
curl -X POST ...
```

Browser DevTools should be used to inspect:

- Request headers
- Response headers
- Payloads
- Timing
- Redirects
- CORS failures
- Cache hits/misses

## Connection to the rest of the repo

```text
Networking
   ↓
HTTP
   ↓
API design
   ↓
Frontend data fetching
   ↓
Backend services
   ↓
Authentication / caching / retries
   ↓
Distributed systems
```

Frameworks such as FastAPI, Express, Next.js, and browser `fetch` sit on top of this layer. Learn the protocol first; the abstractions then become much easier to reason about.
