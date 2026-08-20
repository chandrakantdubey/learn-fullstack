# Backend Engineering

Backend engineering is the discipline of turning business requirements into reliable services and data flows.

## Core areas

- API contracts and resource design
- Request lifecycle and middleware
- Validation and error contracts
- Authentication and authorization
- Application architecture
- Database access and transactions
- Caching
- Background jobs
- Messaging and event-driven systems
- WebSockets and streaming
- Rate limiting and abuse controls
- Idempotency
- Timeouts and retries
- Graceful shutdown
- Health checks
- Performance and profiling
- Service decomposition
- Distributed systems

## Architecture progression

```text
HTTP handler
   ↓
Application service
   ↓
Domain logic
   ↓
Repository / external clients
   ↓
Database / cache / queue
```

Start with a modular monolith. Introduce separate services only when boundaries, scaling needs, ownership, or failure isolation justify them.
