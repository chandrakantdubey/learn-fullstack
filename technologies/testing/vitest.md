# Vitest

**Role:** Primary | **Layer:** Testing

## Mental model
Vitest is a fast JavaScript/TypeScript test runner designed around modern module/build tooling. Use it to verify deterministic application behavior close to the code under test.

## Test design
A useful test has a clear behavior contract, controlled inputs and deterministic outcomes. Prefer testing observable behavior over private implementation details.

## Core capabilities
Understand test lifecycle, assertions, mocks, spies, fake timers, module mocking, coverage, environments and setup files.

## Mocking
Mock at stable boundaries: external APIs, clocks, randomness or expensive integrations. Over-mocking internal modules can make tests pass while production wiring is broken.

## Async tests
Await asynchronous operations explicitly. Avoid tests that pass before a promise settles. Test timeout and rejection behavior for critical asynchronous code.

## Integration tests
Use Vitest for application-level integration tests where appropriate, but use real databases/queues through Testcontainers when the behavior depends on actual infrastructure semantics.

## Coverage
Coverage is a signal, not a quality score. High line coverage can coexist with weak assertions. Prioritize business-critical branches, failure modes and contracts.

## Production patterns
- Keep unit tests fast and deterministic.
- Isolate global state.
- Reset mocks between tests.
- Use fake time only when it clarifies time-dependent behavior.
- Keep external integration tests explicit.
- Run type checking separately from tests.

## Common mistakes
- testing implementation details
- mocking every dependency
- shared mutable fixtures
- assertions that only check that code did not throw
- using coverage percentage as the primary quality metric

## Interview-level topics
Test isolation, mocking boundaries, fake timers, async testing, unit vs integration testing, coverage interpretation and deterministic test architecture.

## Related
TypeScript, React, Testing Library, Playwright, Testcontainers.