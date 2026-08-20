# Authentication and Security

Security is a system property, not a middleware package.

## Identity vs authorization

Authentication answers:

> Who is this principal?

Authorization answers:

> Is this principal allowed to perform this action on this resource?

Keep those concepts separate.

## Session model

Common patterns:

```text
Browser
  ↓
Secure, HttpOnly cookie
  ↓
Server-side session
```

or:

```text
Client
  ↓
access token
  ↓
API
```

Choose based on client type, threat model, revocation requirements, and architecture. Do not select JWTs simply because they are popular.

## Passwords

Never store plaintext passwords. Use a password hashing algorithm designed for password storage, with appropriate cost parameters.

## Authorization

Model authorization as explicit policy.

```text
principal
  + action
  + resource
  + context
  → allow / deny
```

RBAC is useful for coarse role boundaries. Resource-level authorization is often still required.

## Common attack classes

Know how to prevent and detect:

- SQL injection
- XSS
- CSRF
- SSRF
- broken access control
- insecure direct object references
- credential stuffing
- secret leakage
- unsafe file upload
- command injection

## API security defaults

- validate untrusted input
- use parameterized SQL
- enforce authorization server-side
- rate-limit sensitive endpoints
- set bounded request sizes
- use TLS
- protect credentials with secure storage
- avoid logging tokens and secrets
- rotate secrets when exposure is suspected

## Token handling

Treat access tokens as credentials. Minimize lifetime, scope, and exposure.

Refresh-token systems need rotation/reuse detection and a revocation strategy appropriate to the threat model.

## Production review

For each endpoint ask:

1. What is untrusted input?
2. Who can call it?
3. Which resource is being accessed?
4. What invariant must hold?
5. What information could leak through errors/logs?
6. What abuse could become expensive?
7. How can credentials be revoked?

## Connects to

`web/http`, `backend/service-architecture.md`, `production/observability.md`, and `infrastructure/secrets.md`.
