# Rate Limiting

Rate limiting protects capacity and makes resource ownership explicit.

## Problem

Without limits, one client, tenant, endpoint, or dependency can consume disproportionate resources and turn normal load into an outage.

## Boundary

Choose the resource being protected and the identity used for accounting: IP, user, API key, tenant, endpoint, or a weighted combination.

## Invariants

- Limits are enforced at the correct trust boundary.
- A limit has a defined time/window or token budget.
- Distributed instances share state when global enforcement is required.
- Exceeding a limit has deterministic API semantics.
- Critical internal traffic is not accidentally starved by a broad public limit.

## Algorithms

**Fixed window** is simple but permits bursts at window boundaries.

**Sliding window** smooths boundary behavior at higher implementation cost.

**Token bucket** allows controlled bursts while enforcing a long-term rate and is a useful general-purpose model.

## Implementation choices

Apply coarse limits at the edge and finer limits inside the application. Return `429` for rejected requests and communicate retry timing when appropriate.

For distributed services, use an atomic shared counter/token mechanism or accept explicitly local semantics. Rate limits should not depend on a single application process's memory.

## Failure modes

- rate limiter itself becomes a bottleneck
- trusting spoofable identity headers
- one global bucket causing tenant starvation
- retries multiplying traffic after `429`
- expensive requests charged as if they were cheap
- fail-open behavior during limiter outages without capacity protection

## Security

Authenticate before using user/tenant identity for privileged limits. Defend against identity spoofing at proxy boundaries. Combine rate limiting with authorization, quotas, and abuse detection rather than treating it as the whole security model.

## Performance

Measure limiter latency and cardinality. Prefer constant-time operations and bounded state. Weight limits when operations have dramatically different cost.

## Operational signals

Track allowed/rejected rates, hot identities, limiter errors, latency, and capacity consumption by tenant/endpoint.
