# Security Engineering

Security is a system property, not a middleware checkbox. A Fullstack Engineer should reason about trust boundaries from browser to database and infrastructure.

## Core model

```text
Browser
  ↓ untrusted input
Edge / CDN / WAF
  ↓
Application
  ↓
Identity + Authorization
  ↓
Data / Services
  ↓
Infrastructure
```

## Application threats

Understand and prevent:

- SQL injection
- XSS: reflected, stored, DOM-based
- CSRF
- SSRF
- command injection
- path traversal
- unsafe deserialization
- broken object-level authorization
- insecure direct object references
- request smuggling and parser disagreement
- dependency and supply-chain compromise

## Identity

Know the difference between authentication and authorization.

Understand:

- sessions and secure cookies
- OAuth 2.0
- OpenID Connect
- access vs refresh tokens
- JWT trade-offs
- password hashing with Argon2/bcrypt
- MFA
- service-to-service identity
- RBAC and ABAC
- tenant isolation

Prefer secure, short-lived credentials and server-side authorization checks. Do not rely on hidden UI controls for access control.

## Browser security

- same-origin policy
- CORS
- CSP
- `HttpOnly`, `Secure`, and `SameSite` cookies
- clickjacking protection
- origin and redirect validation
- safe file uploads

## Secrets and cryptography

- never commit secrets
- use a secrets manager
- rotate credentials
- encrypt in transit and at rest
- understand hashing vs encryption vs signing
- use vetted cryptographic libraries rather than custom algorithms

## Infrastructure security

- least-privilege IAM
- private subnets for data services
- security groups and network policies
- TLS everywhere practical
- container non-root execution
- dependency/image scanning
- audit logs
- controlled administrative access

## Production security checklist

Before production, verify:

1. every resource access is authorized server-side
2. untrusted input is validated at boundaries
3. secrets are externalized
4. security-sensitive events are logged without leaking secrets
5. dependencies and images are scanned
6. database roles are least-privilege
7. public network exposure is intentional
8. incident credentials can be revoked and rotated

Security decisions should be documented with the threat they address, not just the tool being used.
