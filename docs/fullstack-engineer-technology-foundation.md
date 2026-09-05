# Fullstack Engineer — Technology Foundation

> **Canonical status:** Legacy orientation document. The original long-form technology foundation has been superseded by the structured skill graph and canonical integration documents.

Use these as the current sources of truth:

- [`master-skill-universe.md`](master-skill-universe.md) — complete 20-section capability universe and ownership.
- [`skill-map.md`](skill-map.md) — integrated capability map.
- [`final-skill-graph.md`](final-skill-graph.md) — dependency graph and canonical stack.
- [`learning-model.md`](learning-model.md) — how topics are learned and verified.
- [`architecture-decision-guide.md`](architecture-decision-guide.md) — architecture and trade-off method.
- [`production-verification.md`](production-verification.md) — implementation, failure and operational proof.
- [`interview-map.md`](interview-map.md) — interview and system-design verification.

## Why this file was consolidated

The original document mixed principles, technology inventory, framework choices, architecture, infrastructure and AI into one very large reference. That made ownership and canonical paths harder to maintain.

The durable model is now:

```text
Principles
  ↓
Mental models
  ↓
Mechanisms
  ↓
Canonical technologies
  ↓
Cross-layer patterns
  ↓
Production systems
  ↓
Failure / security / scale
  ↓
Projects
  ↓
Interview defense
```

## Core engineer model

```text
Browser
  ↓
Web protocols
  ↓
Frontend
  ↓
API / backend
  ↓
Data + messaging
  ↓
Linux / runtime
  ↓
Containers / cloud / IaC
  ↓
Testing / security / observability / SRE
  ↓
AI systems
  ↓
Architecture + system design
```

The nine specialized repositories provide deep implementation knowledge. `learn-fullstack` owns the connections, invariants, production behavior, architecture and verification.

## Final principle

Do not optimize for the number of technologies you can name. Optimize for the number of production problems you can **understand, implement, debug, measure, secure, test, scale, operate, recover from and defend**.
