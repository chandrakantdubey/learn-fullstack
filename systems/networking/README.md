# Networking for Fullstack Engineers

Networking is the path between every component in a modern application. A browser request can cross DNS, a CDN, a load balancer, a reverse proxy, a service, a cache, and a database before returning a response.

## Mental model

```text
Client
  -> DNS
  -> IP
  -> TCP / QUIC
  -> TLS
  -> HTTP
  -> Load balancer / proxy
  -> Application
  -> Internal dependencies
```

Every arrow introduces latency and failure modes.

## Core layers

You do not need to memorize every detail of the OSI model, but you should understand the practical layers:

```text
Application   HTTP, DNS, TLS, WebSocket
Transport     TCP, UDP, QUIC
Internet      IP, routing
Link          Ethernet, Wi-Fi
```

## IP and ports

Understand:

- IPv4 and IPv6
- Private vs public addresses
- Ports
- Sockets
- Subnets
- CIDR
- Routing
- NAT
- Security groups / firewalls

A service is generally reachable only when:

```text
Route exists
AND
network policy allows traffic
AND
process is listening
AND
protocol matches
```

## TCP

Know the practical properties:

- Connection-oriented
- Reliable byte stream
- Ordered delivery
- Congestion control
- Retransmission
- Connection setup and teardown

This matters when reasoning about latency, connection pools, keep-alive, and load.

## UDP and QUIC

UDP provides datagrams without TCP's delivery guarantees.

QUIC builds modern transport behavior on UDP and enables HTTP/3. You do not need to implement QUIC, but you should understand why modern web stacks can avoid some TCP limitations.

## DNS

Understand the resolution path:

```text
Application
  -> resolver
  -> recursive DNS
  -> authoritative DNS
  -> answer
```

Know:

- A / AAAA
- CNAME
- TXT
- MX
- TTL
- Recursive vs authoritative servers
- Caching
- DNS failure modes

Useful debugging:

```bash
dig example.com
dig +trace example.com
nslookup example.com
```

## TLS

Understand the purpose and high-level handshake:

- Server authentication
- Certificate chain
- Key exchange
- Symmetric encryption after handshake
- Certificate validity and renewal
- SNI
- mTLS for service-to-service authentication

For application engineers, the important operational question is often: where does TLS terminate?

```text
Browser
  --TLS-->
CDN / Load Balancer
  --HTTP or TLS-->
Service
```

## HTTP

HTTP is covered in depth in `web/http`, but networking study should connect it to sockets, latency, and proxies.

Understand:

- Request/response
- Methods
- Status codes
- Headers
- Connection reuse
- Compression
- Streaming
- HTTP/1.1
- HTTP/2 multiplexing
- HTTP/3 over QUIC

## Proxies and load balancers

Know the difference between:

### Reverse proxy

Sits in front of services and can provide:

- TLS termination
- Routing
- Compression
- Authentication hooks
- Request limits
- Static asset delivery

### Load balancer

Distributes traffic across healthy instances.

Understand:

- L4 vs L7 load balancing
- Health checks
- Connection draining
- Algorithms such as round-robin and least connections
- Sticky sessions and why they complicate scaling

## Latency model

A request's latency is not only application compute.

```text
Total latency ≈
DNS
+ connection setup
+ TLS
+ network RTTs
+ queueing
+ application work
+ database work
+ response transfer
```

At scale, milliseconds multiply quickly across downstream calls.

## Debugging workflow

When an endpoint cannot be reached:

```text
DNS resolves?
  -> Correct IP?
  -> Route exists?
  -> Port reachable?
  -> Process listening?
  -> TLS works?
  -> HTTP response received?
  -> Application dependency healthy?
```

Useful tools:

```bash
curl -v
curl -I
dig
ss
nc
ping
traceroute
tcpdump
```

## Production connection

Networking is the foundation underneath:

- CDN architecture
- API gateways
- Kubernetes Services and Ingress
- VPCs and subnets
- Service meshes
- Database connectivity
- Redis and queues
- Multi-region systems

The goal is to know where a packet goes and where it can fail.
