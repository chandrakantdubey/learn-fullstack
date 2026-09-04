# Security Engineering for Fullstack Systems

Security is a system property. Framework configuration helps, but the architecture must establish trust boundaries, least privilege and safe failure behavior.

## Threat model

For each feature identify assets, actors, trust levels, entry points, privileged operations, data flows, abuse cases and impact. Use STRIDE-style analysis where useful, but also write concrete abuse cases for authentication, authorization, data access and resource exhaustion.

## Identity

```text
Who are you?       → authentication
What may you do?   → authorization
```

Authentication establishes a principal. Authorization must still be checked for the requested action and resource.

## Credentials and sessions

Secrets should be scoped, short-lived where practical and rotated. Session identifiers must be unpredictable. Password-reset and verification tokens need expiry, single-use semantics and safe storage.

## Input and output

Treat browser input, headers, cookies, uploads, webhooks, queue messages, model output and third-party responses as untrusted. Validate structure and bounds at boundaries and encode output for its context.

## Common web risks

Know the mechanisms behind XSS, CSRF, SQL injection, command injection, SSRF, path traversal, insecure deserialization, broken access control/IDOR, request smuggling, supply-chain attacks, secret leakage and denial of service.

There is no universal `sanitize()` function. The defense must match the data context and vulnerability.

## Cryptography

Use standard cryptographic libraries and protocols. Passwords require password hashing/KDFs; confidentiality requires authenticated encryption; transport security normally comes from TLS; integrity/authenticity may use signatures or MACs.

See [`foundations/security/cryptography.md`](../foundations/security/cryptography.md) from this file's directory hierarchy.

## Authorization architecture

Prefer explicit policy decisions with resource checks. Consider tenant boundaries, object ownership, service identity and administrative operations separately. Never rely on client-side route guards or hidden UI controls for authorization.

## Secrets and supply chain

Never commit credentials or log tokens. Keep production secrets outside source control and restrict retrieval. Design rotation/revocation before a leak occurs. Pin or constrain dependencies, scan dependencies/images, protect CI credentials and keep build provenance auditable.

## Production checklist

- Threat model important features.
- Least privilege everywhere.
- Server-side authorization.
- Secure session/token lifecycle.
- Input validation and output encoding.
- Rate/resource limits.
- TLS and secure cookies.
- Dependency/image scanning.
- Secret rotation and audit logs.
- Abuse-case security tests.
- Safe error messages.
