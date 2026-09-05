# Engineering Practices

Senior/staff engineering is partly technical judgment and partly the ability to make that judgment repeatable for a team.

## Code review

Review in this order:

1. correctness and invariants
2. security and authorization
3. failure behavior
4. data/API compatibility
5. observability and operability
6. performance/resource usage
7. readability and maintainability

Do not spend review time arguing about style already enforced by tooling.

## ADRs

Use an ADR when a decision has meaningful future cost, operational consequences or credible alternatives.

Record:

- context
- constraints
- decision
- alternatives
- trade-offs
- consequences
- revisit conditions

An ADR is useful when someone can later ask “why did we do this?” and get the actual reasoning.

## RFCs

Use an RFC for larger changes that need design review before implementation.

Recommended sections:

```text
problem
requirements
non-goals
current state
proposal
alternatives
migration
security
observability
capacity/cost
failure modes
rollout
rollback
open questions
```

## API evolution

Prefer additive evolution. For breaking changes:

```text
announce
 → dual-read/write or compatibility layer
 → migrate clients/data
 → verify telemetry
 → remove old path
```

Never assume all clients deploy simultaneously.

## Dependency lifecycle

For important dependencies track:

- owner
- reason for use
- version policy
- security advisory path
- upgrade frequency
- migration cost
- replacement candidate

Avoid adding a library for a problem the platform or existing stack already solves adequately.

## Semantic versioning

Treat version numbers as communication about compatibility, not magic automation. Define what your project considers breaking, additive and patch-level changes, especially for APIs and shared packages.

## Technical debt

Prioritize debt by impact:

```text
customer risk
security risk
reliability risk
engineering drag
cost
```

A clever abstraction with no measurable benefit is not automatically debt; neither is old code automatically bad.

## Release management

A release should identify:

- artifact/version
- changes
- migrations
- feature flags
- dependencies
- rollout plan
- monitoring signals
- rollback plan

Prefer immutable artifacts and the same artifact through staging and production.

## Cost-aware engineering

For major architecture decisions estimate:

- compute
- database
- storage
- network/egress
- observability
- third-party APIs
- AI/model usage
- operational headcount/complexity

A technically elegant system that cannot meet its cost constraint is not a successful design.

## Documentation

Document decisions and operational knowledge where future engineers will look for them:

- README for orientation
- concept docs for durable knowledge
- ADRs for decisions
- API specs for contracts
- runbooks for incidents/operations
- dashboards/alerts for live behavior

Avoid documentation that merely restates source code.

## Definition of engineering maturity

A mature team makes important behavior:

- explicit
- testable
- observable
- recoverable
- reviewable
- explainable

That is the standard this repository should teach.
