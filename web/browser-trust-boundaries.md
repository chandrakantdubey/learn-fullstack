# Browser Architecture and Trust Boundaries

A production frontend is not just React components. It is code executing inside a browser security model with its own storage, networking, rendering and lifecycle rules.

## Browser pipeline

```text
URL
 ↓
DNS / connection / TLS
 ↓
HTTP response
 ↓
HTML parse → DOM
CSS parse → CSSOM
 ↓
render tree → layout → paint → compositing
```

JavaScript participates in this lifecycle and can delay rendering when it performs expensive work on the main thread.

## Same-origin policy

The browser separates origins by scheme, host and port. Same-origin policy restricts how documents and scripts interact across origins. CORS is a controlled mechanism for allowing specific cross-origin HTTP reads; it is not a server-side authentication mechanism.

## Storage

Understand cookies, localStorage, sessionStorage, IndexedDB and in-memory state. They have different lifetimes, accessibility and security properties.

Sensitive session material is commonly safer in appropriately scoped, `HttpOnly`, `Secure`, `SameSite` cookies than in JavaScript-readable storage, depending on the architecture and threat model.

## CSRF and XSS

CSRF abuses ambient browser credentials when a victim can be induced to make a request. XSS executes attacker-controlled script in a trusted origin. Their mitigations differ.

- CSRF: SameSite cookies, CSRF tokens and origin checks where appropriate.
- XSS: contextual output encoding, safe DOM APIs, strict content policies and avoiding unsafe HTML injection.

Do not treat one defense as a replacement for the other.

## CSP

Content Security Policy limits which scripts and other resources the browser may load or execute. A strong policy reduces XSS blast radius but must be designed around the application's legitimate execution model.

## Frontend/backend boundary

The browser is an untrusted client. Never rely on hidden UI controls, TypeScript types, client-side validation or route guards for authorization. The server must independently authenticate and authorize every protected operation.

## Performance

Measure Core Web Vitals and the full path to interaction. Common bottlenecks include JavaScript bundle size, hydration/client work, render waterfalls, image/font delivery, excessive re-renders and slow API dependencies.

## Production rule

```text
browser validation = UX
server validation   = correctness
server authorization = security
```
