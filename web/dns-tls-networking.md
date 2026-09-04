# DNS, TCP, TLS and Connection Lifecycle

A fullstack engineer should be able to explain how a browser request reaches a service without hiding behind framework abstractions.

## Request path

```text
URL
 ↓
DNS resolution
 ↓
IP route
 ↓
TCP or QUIC connection
 ↓
TLS handshake
 ↓
HTTP request
 ↓
proxy/load balancer
 ↓
application
```

Each layer has different failure modes and observability.

## DNS

DNS maps names to records such as A/AAAA, CNAME and TXT. Resolution can involve local caches, recursive resolvers and authoritative servers.

Caching means a DNS change is not necessarily visible immediately. TTL controls cache lifetime; it is not a guarantee that every resolver refreshes at exactly that interval.

## TCP

TCP provides a reliable ordered byte stream. It does not preserve application message boundaries. Applications therefore need framing when using a raw stream.

Know connection establishment, retransmission, flow control, congestion control, keepalive and connection teardown.

## UDP and QUIC

UDP provides datagrams without TCP's reliability guarantees. QUIC builds reliable streams, congestion control and TLS 1.3 into a UDP-based transport. Understand why HTTP/3 uses QUIC and why transport behavior affects latency and connection migration.

## TLS

TLS authenticates the server through certificate validation and establishes keys for protected transport. Certificate trust, hostname validation, expiry and certificate-chain problems are distinct operational concerns.

TLS does not authenticate your application user and does not authorize API operations.

## Proxies and load balancers

A request may cross several hops:

```text
client → CDN → load balancer → reverse proxy → service
```

Forwarded headers, client IP, scheme and host information are trustworthy only according to the proxy topology. Configure trusted proxy boundaries explicitly.

## Debugging

When a request fails, isolate the layer:

```text
DNS failure?
→ connection failure?
→ TLS/certificate failure?
→ HTTP status?
→ application error?
→ downstream dependency?
```

Use evidence such as DNS lookup results, connection timing, TLS diagnostics, HTTP traces and service telemetry rather than guessing.

## Production checklist

- Define DNS ownership and TTL expectations.
- Reuse connections where appropriate.
- Set connection and request deadlines.
- Monitor connection pools and handshake failures.
- Configure TLS verification correctly; never disable certificate validation as a routine fix.
- Define trusted proxy boundaries.
- Propagate trace context across proxy/service hops.
- Distinguish network failure from application failure in alerts.
