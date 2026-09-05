# Network Debugging Playbook

Use this before blaming the framework, cloud platform or application code.

## Request path

```text
URL
 ↓
DNS
 ↓
TCP/QUIC connection
 ↓
TLS
 ↓
CDN/proxy/load balancer
 ↓
HTTP
 ↓
application
 ↓
downstream network calls
```

## DNS diagnosis

Ask:

- does the name resolve?
- which resolver answered?
- are A/AAAA records correct?
- is stale caching involved?
- is split-horizon/private DNS involved?

Useful tools:

```bash
dig example.com
dig +trace example.com
```

## Connection diagnosis

Determine whether the failure is:

- no route
- refused connection
- connection timeout
- TLS failure
- application timeout

Useful tools:

```bash
ss -lntp
nc -vz host 443
curl -v https://host
```

## HTTP diagnosis

Inspect:

- status code
- response headers
- redirect chain
- content type
- cache headers
- proxy/forwarded headers
- request size
- response size

Compare direct service access with access through the proxy when safe.

## TLS diagnosis

Check:

- certificate hostname
- expiration
- trust chain
- protocol/cipher compatibility
- which hop terminates TLS

Do not disable certificate verification as a “fix.” It removes a security control and hides the real configuration problem.

## Latency decomposition

Measure separately:

```text
DNS
+ connect
+ TLS
+ request upload
+ server wait
+ first byte
+ response transfer
```

The goal is to identify the slowest boundary, not optimize the wrong layer.

## Proxy/load-balancer failures

Common causes:

- no healthy backend
- wrong port
- incorrect health check
- timeout mismatch
- request-size limit
- header normalization/trust issue
- TLS termination mismatch
- connection pool exhaustion

## Service-to-service networking

Verify:

1. DNS/service discovery
2. route/network policy
3. port/listener
4. TLS identity
5. authentication
6. application response

A successful TCP connection does not prove the application request is authorized or correct.

## Production rule

Change one boundary at a time and capture evidence before changing configuration. A sequence of speculative changes destroys the information needed to diagnose the original failure.
