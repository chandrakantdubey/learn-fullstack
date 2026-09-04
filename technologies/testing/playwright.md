# Playwright

**Role:** Primary | **Layer:** End-to-end testing

## Mental model
Playwright drives real browser engines and verifies application behavior across browser, frontend, network and backend boundaries. It is best used for high-value user journeys rather than every unit-level behavior.

## Test layers
```text
unit -> component/integration -> E2E
cheap                         expensive
fast                          slower
```

Use Playwright where browser behavior, routing, authentication, rendering and cross-service integration matter.

## Locators
Prefer semantic, user-facing locators such as roles, labels and stable test IDs. Avoid selectors coupled to CSS implementation or DOM nesting.

## Fixtures and isolation
Fixtures provide reusable setup. Keep tests isolated so failures do not depend on execution order. Use controlled test data and reset state between tests when required.

## Browser contexts
Contexts provide isolated browser state. They are useful for independent users, authentication sessions and parallel execution.

## Authentication
Reuse authenticated state carefully. Do not share mutable sessions across tests when that creates coupling. Test authorization boundaries with distinct users/roles.

## Network behavior
Use request interception for deterministic tests when appropriate, but do not mock every dependency. Critical workflows should exercise real integration paths in a production-like environment.

## Debugging
Use traces, screenshots, console/network diagnostics and video where useful. Avoid `sleep` as a synchronization mechanism; wait for observable application state.

## CI
Run tests against a deterministic deployment, control browser versions, collect traces for failures and shard/parallelize only when test isolation is reliable.

## Production patterns
- Keep the suite focused on business-critical journeys.
- Make test data deterministic.
- Test success, validation, authorization and recovery paths.
- Run browser tests against realistic APIs where contract confidence matters.
- Keep retries limited; retries can hide flaky tests.

## Security
Never place production credentials or real customer data into test environments. Treat browser storage and traces as potentially sensitive.

## Common mistakes
- brittle CSS selectors
- arbitrary sleeps
- shared mutable test state
- mocking everything
- huge E2E suites for logic that belongs in unit tests
- ignoring authorization paths

## Interview-level topics
Browser contexts, isolation, fixtures, locators, network interception, authentication state, parallelism, flaky-test diagnosis and E2E test architecture.

## Related
React, Next.js, Testing Library, Vitest, CI/CD.