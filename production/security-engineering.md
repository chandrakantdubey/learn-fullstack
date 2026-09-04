# Security Engineering for Fullstack Systems

Security is a system property. Framework configuration helps, but the architecture must establish trust boundaries, least privilege and safe failure behavior.

## Threat model

For each feature identify:

1. assets worth protecting
2. actors and trust levels
3. entry points
4. privileged operations
5. data flows
6. likely abuse cases
7. impact if a control fails

A useful baseline is STRIDE-style threat analysis plus explicit abuse cases for authentication, authorization, data access and resource exhaustion.

## Identity

Separate authentication from authorization:

```text
Who are you?       → authentication
What may you do?   → authorization
```

Authentication can establish a principal, but each protected operation still needs authorization against the requested resource and action.

## Credentials and sessions

Secrets should be short-lived where practical, scoped to the minimum permissions and rotated. Session identifiers must be unpredictable and protected from script access where appropriate. Password reset and email-verification tokens need expiry, single-use semantics and safe storage.

## Input and output

Treat browser input, headers, cookies, uploaded files, webhook payloads, queue messages, model output and third-party responses as untrusted. Validate structure and bounds at boundaries. Encode output according to its context.

## Common web risks

Know the mechanisms behind:

- XSS
- CSRF
- SQL injection
- command injection
- SSRF
- path traversal
- insecure deserialization
- broken access control / IDOR
- request smuggling
- dependency/supply-chain attacks
- secret leakage
- denial of service

The correct defense depends on the vulnerability; there is no universal "sanitize everything" function.

## Cryptography

Use standard cryptographic libraries and protocols. Passwords require password hashing/KDFs; data confidentiality requires authenticated encryption; transport security normally comes from TLS; integrity/authenticity may require signatures or MACs depending on the protocol.

See [`foundations/security/cryptography.md`](../foundations/security/cryptography.md).

## Authorization architecture

Prefer centralized policy decisions with explicit resource checks. Avoid scattering role strings throughout controllers. Consider tenant boundaries, object ownership, service-to-service identity and administrative operations separately.

## Secrets

Never commit credentials. Do not log tokens. Keep production secrets outside source control and restrict who and what can retrieve them. Design rotation and revocation before a credential leak occurs.

## Supply chain

Pin or constrain dependencies, review transitive risk, scan images and dependencies, protect CI credentials and keep build provenance auditable.

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
- Security tests for abuse cases.
- Safe error messages.
