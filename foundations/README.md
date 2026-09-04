# Foundations

The foundational layer explains the mechanics underneath frontend, backend, databases, containers, cloud and AI applications.

## Topics

### Programming

- values, references, mutability and memory
- functions, closures, modules and errors
- types and generics
- collections and complexity
- parsing vs validation
- regular expressions
- Unicode and text processing
- bytes, encoding and serialization
- hashing and checksums
- randomness and secure randomness
- numeric precision
- dates, time zones and clocks

### Systems

- processes and threads
- virtual memory
- filesystems and file descriptors
- event loops
- concurrency and synchronization
- CPU vs I/O
- resource limits and lifecycle
- signals and graceful shutdown

### Security

- threat modeling
- authentication and authorization
- cryptographic primitives
- password hashing
- sessions/tokens
- secrets and key management
- common web attack classes

### Engineering

- Git and collaboration
- testing fundamentals
- debugging
- API contracts
- error handling
- observability
- performance reasoning

## Dependency map

```text
Programming
   ├── Data Structures
   ├── Runtime
   ├── Text / Encoding
   └── Concurrency

Operating Systems ──┐
                    ├── Networking ── Web / HTTP ── Frontend / Backend
Security ───────────┘

Git ── Testing ── Observability ── Production
```

## Principle

Learn the mechanism before the abstraction. Framework knowledge becomes much easier once the underlying boundary is understood.
