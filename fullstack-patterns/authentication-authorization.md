# Authentication and Authorization Boundaries

Identity and permission are different problems.

```text
Credential
  → authentication
  → principal / session
  → authorization policy
  → resource + action decision
  → audit / telemetry
```

## Problem

Applications become insecure when authentication, authorization, tenant isolation, and UI visibility are treated as one concern.

## Boundary

Authentication answers **who are you?**

Authorization answers **are you allowed to perform this action on this resource?**

Session management answers **how does that identity remain trustworthy across requests?**

Tenant isolation answers **which data is inside that principal's authority?**

## Invariants

- The server is the authority for access decisions.
- Every protected operation derives authorization from trusted server-side identity and resource state.
- Tenant/user identifiers supplied by the client are selectors, not proof of access.
- Privilege is explicit and least-privileged.
- Sensitive authorization decisions are auditable.

## Implementation choices

Prefer a clear authentication middleware/dependency that produces a principal, followed by authorization checks close to the resource or use case.

For sessions, choose secure cookie-backed sessions or a carefully designed token model based on the threat model. For OAuth/OIDC, distinguish the identity provider from your application's authorization model.

For multi-tenancy, enforce tenant scope in application queries and, where appropriate, database policies or constraints as defense in depth.

## Failure modes

- checking roles only in the frontend
- IDOR caused by loading `/users/:id` without ownership checks
- accepting a tenant ID from the request body as authority
- long-lived tokens without revocation strategy
- confusing authentication failure with authorization failure
- inconsistent authorization rules between endpoints
- missing authorization on background jobs or internal APIs

## Security

Protect session cookies with appropriate `Secure`, `HttpOnly`, and `SameSite` settings. Protect state-changing browser flows against CSRF where cookies are ambient credentials. Store passwords using a dedicated password-hashing algorithm; never encrypt passwords for later recovery.

Do not put secrets into browser-accessible storage without a deliberate threat-model justification. Rotate credentials and provide revocation for high-risk sessions.

## Performance

Avoid repeated identity and permission lookups when safe to cache, but define invalidation semantics. Do not trade authorization correctness for a micro-optimization.

## Operational signals

Audit sensitive grants/denials, authentication failures, session revocations, privilege changes, and suspicious access patterns. Avoid logging raw credentials, session tokens, or unnecessary personal data.
