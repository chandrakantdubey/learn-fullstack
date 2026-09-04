# Networking for Fullstack Engineers

Networking is the substrate underneath every web request, database connection, queue and cloud service.

## Layered mental model

```text
Application: HTTP / DNS / WebSocket / gRPC
Transport:   TCP / UDP / QUIC
Internet:    IP
Link:        Ethernet / Wi-Fi
```

The layers are abstractions, not independent boxes. Application behavior is affected by connection setup, packet loss, congestion, MTU, routing and middleboxes.

## DNS

DNS maps names to records and supports delegation, caching and service discovery. Understand A/AAAA, CNAME, TXT, NS, TTL and recursive resolution. DNS caching means a configuration change is not necessarily visible everywhere immediately.

## TCP

TCP provides an ordered byte stream with reliability and congestion control. It does not preserve application message boundaries. HTTP/1.1 uses framing on top of that stream.

Connection establishment, retransmission, slow start and connection reuse all influence latency.

## UDP and QUIC

UDP provides datagrams without TCP's delivery guarantees. QUIC builds reliable, encrypted transport semantics over UDP and is the transport used by HTTP/3.

## Ports and connections

A connection is identified by endpoint information including IP addresses and ports. Servers listen on ports; clients use ephemeral ports. Connection pools reduce repeated handshake costs but consume finite resources.

## Proxies and load balancers

A request can traverse:

```text
browser → DNS → CDN → load balancer → reverse proxy → service → database
```

Every hop can terminate TLS, change headers, enforce limits, cache responses or introduce latency.

## Production concerns

- Connection pooling and keep-alive.
- DNS caching and failure behavior.
- Timeouts at every network boundary.
- Maximum request/response sizes.
- Retries with exponential backoff and jitter.
- Avoiding retry storms.
- Observing latency per hop.
- IPv4/IPv6 behavior.
- TLS certificate validation.
- Proxy and forwarded-header trust.

## Debugging sequence

When an endpoint is slow, separate DNS time, connection time, TLS handshake, server processing, downstream time and response transfer. A single aggregate latency number hides the real bottleneck.
