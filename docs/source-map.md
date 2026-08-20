# Source Map

`learn-fullstack` integrates existing repositories. It does not replace them and should not become a copy of them.

## Repositories

| Source | Keep as source of truth | Bring into `learn-fullstack` | Treatment |
| --- | --- | --- | --- |
| `learn-python` | Python language depth, stdlib, packaging, async, concurrency | Python-for-fullstack concepts, runtime model, production conventions | Summarize and cross-link; avoid duplicating the full Python curriculum |
| `learn-js-ts` | JS/TS language depth and runtime mechanics | JS runtime model, TypeScript engineering, Node.js fundamentals | Extract principles and stack decisions |
| `learn-frontend` | Browser, HTML/CSS, React, Next.js, frontend architecture | Browser/web fundamentals, frontend architecture, client/server boundaries, performance | Rewrite around capabilities rather than weekly course phases |
| `learn-backend` | APIs, services, backend architecture, databases, distributed systems | Backend principles, API design, async systems, reliability | Merge the strongest concepts; remove duplicated resource lists |
| `learn-sql` | SQL and relational database depth | Data modeling, transactions, indexing, query planning, PostgreSQL engineering | Keep DB-specific depth in source repo and teach integration here |
| `learn-docker` | Docker mechanics and container practice | Container mental model, production image workflow, networking, debugging | Integrate into infrastructure path |
| `learn-dsa` | DSA problem-solving depth | Only CS concepts that improve engineering judgment | Keep full problem set elsewhere |
| `learn-ai` | ML/LLM/AI engineering depth | The bridge from Fullstack Engineering to AI Engineering | Avoid turning this repo into the AI curriculum |

## Integration Rules

### 1. Principles before products

Prefer:

- HTTP before FastAPI/Express
- SQL before SQLAlchemy/Prisma
- browser architecture before React
- containers before Kubernetes
- Linux/networking before cloud abstractions
- distributed-systems principles before Kafka

### 2. One concept, one canonical explanation

When the same concept exists in multiple repositories, `learn-fullstack` should contain the integrated explanation and link back to the specialized deep dive.

### 3. No framework soup

A topic should have a small default stack plus alternatives only when they teach an important trade-off.

### 4. Production context is mandatory

Every significant technology should eventually answer:

- failure modes
- security implications
- observability
- performance
- scalability
- cost
- deployment
- testing

### 5. Projects integrate layers

Projects should cross boundaries. Prefer:

```text
Browser → API → Database → Cache → Queue → Worker → Observability
```

over isolated framework demos.

## Expected Output of a Topic

A mature topic should eventually contain:

```text
concept.md              # mental model and principles
implementation.md       # practical implementation
production.md            # reliability/security/performance concerns
stack.md                 # Python + TypeScript choices
project.md               # applied exercise or project slice
references.md            # selective external references
```
