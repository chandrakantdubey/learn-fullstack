# Security Engineering

Security is a property of the whole system, not a library you install.

## Mental model

```text
Identity → Authentication → Authorization → Data access → Audit
                    │
                    └── Trust boundaries
```

Threat-model every boundary: browser/server, service/service, service/database, workload/cloud, and human/admin access.

## Application security

Understand and prevent:

- SQL injection
- XSS
- CSRF
- SSRF
- command injection
- path traversal
- insecure deserialization
- broken access control
- authentication/session flaws
- sensitive-data exposure
- rate-limit bypass

## Authentication

Know the difference between:

- password authentication
- session cookies
- bearer access tokens
- refresh tokens
- OAuth 2.0
- OpenID Connect
- API keys
- service-to-service identity

For browser applications, prefer secure, HttpOnly, SameSite cookies when a server-managed session is appropriate. Avoid storing long-lived sensitive credentials in browser local storage.

## Authorization

Authentication answers **who are you?** Authorization answers **what may you do to this resource?**

Enforce authorization at the backend resource boundary:

```text
GET /users/123/tasks/42
              │
              └── verify caller may access task 42
```

Never rely on hidden UI controls for security.

## Passwords and secrets

- use a modern password hashing algorithm such as Argon2id where supported
- never log passwords, tokens, or secrets
- use a secret manager in production
- rotate credentials
- use short-lived credentials where practical
- least privilege by default

## Transport and data protection

- TLS for network paths
- encryption at rest for sensitive stores
- strict certificate validation
- avoid plaintext internal traffic unless the threat model explicitly permits it
- redact sensitive fields from logs and traces

## Cloud security

- IAM roles over static credentials
- least privilege policies
- separate production and non-production accounts/environments
- private subnets for databases where appropriate
- security groups as explicit network boundaries
- centralized audit logging
- deny-by-default network posture

## Secure defaults

- validate input at boundaries
- use parameterized SQL
- constrain file uploads
- apply rate limits
- set security headers
- configure CORS narrowly
- use dependency and image scanning
- patch base images and libraries

## Production proof

For every application, document:

1. trust boundaries
2. authentication mechanism
3. authorization rules
4. secret lifecycle
5. abuse cases
6. audit events
7. incident response path
