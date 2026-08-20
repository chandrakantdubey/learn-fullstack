# Web Engineering

The web layer connects browsers, services, and infrastructure.

## Core model

```text
URL
 ↓
DNS
 ↓
TCP / QUIC
 ↓
TLS
 ↓
HTTP
 ↓
CDN / Load Balancer / Reverse Proxy
 ↓
Application
```

## Topics

- DNS and naming
- IP, ports, TCP, UDP, QUIC
- TLS and certificates
- HTTP semantics
- HTTP/1.1, HTTP/2, HTTP/3
- REST and resource modeling
- Cookies, sessions, and browser storage
- CORS and same-origin policy
- CSRF, XSS, CSP
- Caching and cache-control
- Compression
- Streaming and SSE
- WebSockets
- Proxies, CDNs, load balancers

## Engineering rule

Before selecting a framework feature, understand the underlying protocol or browser primitive that the feature abstracts.
