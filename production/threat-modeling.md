# Threat Modeling for Fullstack Systems

Threat modeling turns “security” into concrete design decisions. Do it before implementation for high-risk features and revisit it when trust boundaries or data flows change.

## 1. Inventory

Identify:

- assets: credentials, PII, business data, payments, source code, models, documents
- actors: anonymous users, authenticated users, admins, workers, service accounts, vendors
- entry points: HTTP, uploads, webhooks, queues, files, model/tool interfaces
- privileged actions: data export, payments, account changes, code execution, destructive tools
- trust boundaries: browser/server, service/service, tenant/tenant, app/provider, CI/runtime

## 2. Draw data flows

```text
untrusted actor
   ↓
edge
   ↓
API
   ├── identity
   ├── authorization
   ├── database
   ├── queue
   └── external service
```

Mark where data becomes trusted and why. In most applications, validation changes the shape of data but does not make the actor trustworthy.

## 3. Abuse cases

For each entry point ask:

- Can an attacker impersonate someone?
- Can they access another resource or tenant?
- Can they inject data interpreted by another component?
- Can they force expensive work?
- Can they cause duplicate side effects?
- Can they exfiltrate secrets or sensitive data?
- Can they bypass rate/resource limits?
- Can they make operators lose visibility?

## 4. STRIDE as a checklist

Use STRIDE when useful:

- **Spoofing** — fake identity
- **Tampering** — unauthorized modification
- **Repudiation** — inability to establish what happened
- **Information disclosure** — data exposure
- **Denial of service** — resource exhaustion
- **Elevation of privilege** — unauthorized capability

Do not treat STRIDE as the deliverable. The deliverable is a concrete set of mitigations tied to real assets and abuse cases.

## 5. Authorization model

For each protected operation define:

```text
principal
 + action
 + resource
 + tenant/context
 + policy
 = allow/deny
```

Check authorization server-side at the operation boundary. UI controls are convenience, not security.

## 6. Common application attacks

### Injection

Parameterize SQL and commands. Avoid constructing interpretable syntax from untrusted input.

### XSS

Treat output context as part of the security boundary. Use framework escaping correctly and add defense-in-depth CSP where appropriate.

### CSRF

For cookie-authenticated state-changing requests, design an explicit CSRF defense appropriate to the application architecture.

### SSRF

Do not let user-controlled URLs freely reach internal networks or cloud metadata endpoints. Use allowlists, network egress controls and URL/IP validation appropriate to the use case.

### IDOR / broken object authorization

Never equate “resource exists” with “principal may access resource.”

### Request smuggling

Avoid inconsistent parsing between proxies and application servers. Keep proxy/application HTTP handling aligned and patched.

### Upload attacks

Limit size/type, avoid trusting filenames, store outside executable paths, scan where required, and process asynchronously when expensive.

## 7. AI-specific threats

Treat prompts, retrieved documents, model output and tool results as untrusted data.

Threats include:

- direct prompt injection
- indirect injection in retrieved documents/web content
- sensitive-data leakage
- unauthorized retrieval
- unsafe tool use
- excessive agency
- denial of service through expensive inference
- secret exposure through prompts/logs

The model must not be the authorization authority.

## 8. Supply chain

Protect:

- package dependencies
- container base images
- CI workflows
- build credentials
- registries
- deployment credentials

Use dependency/image scanning, protected release paths, least-privilege CI identities and reproducible/traceable artifacts where practical.

## 9. Security controls matrix

| Threat | Primary control | Verification |
|---|---|---|
| account takeover | secure credential/session lifecycle | auth abuse tests |
| IDOR | resource authorization | cross-resource tests |
| injection | parameterization/escaping | malicious-input tests |
| SSRF | egress + URL policy | internal-target tests |
| DoS | rate/resource/concurrency limits | load/abuse tests |
| secret leakage | secret manager + redaction | log/config scans |
| tenant crossing | scoped queries/policies | cross-tenant tests |
| unsafe AI tool | allowlist + auth + approval | adversarial tool tests |
| supply chain | dependency/CI/image controls | security pipeline |

## 10. Security review output

For each feature record:

```text
assets
actors
entry points
trust boundaries
abuse cases
controls
residual risk
verification tests
owner
revisit trigger
```

Security is complete enough only when the important abuse cases have explicit controls and executable verification.
