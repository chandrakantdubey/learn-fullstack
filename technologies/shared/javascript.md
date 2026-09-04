# JavaScript

**Role:** Primary | **Layer:** Shared

## Mental model
JavaScript is a dynamically typed, garbage-collected language built around values, lexical environments, functions, objects, prototypes and asynchronous execution. Frameworks do not remove these semantics; they compose them.

## Values and coercion
Know primitives, objects, references, `===`, `Object.is`, truthiness, `null` vs `undefined`, numeric edge cases, strings, symbols and bigint. Avoid relying on implicit coercion in security-sensitive or business-critical code.

## Scope and closures
Understand lexical scope, hoisting, temporal dead zones and closures. A closure captures bindings, which explains callback behavior, factory functions and many memory-retention bugs.

## Objects and prototypes
Objects inherit through the prototype chain. `class` is syntax over prototype-based behavior. Know property descriptors, own vs inherited properties, `Object.create`, getters/setters and why prototype pollution is a security concern.

## Functions
Functions are first-class values. Understand `this`, arrow functions, binding, rest/spread, higher-order functions, generators and async generators.

## Async execution
Promises represent eventual completion. `async/await` is syntax over promises, not a separate concurrency model.

```text
call stack
   |
   +--> async operation
            |
            +--> completion -> task/microtask queue
                                  |
                                  v
                             event loop
```

Microtasks such as promise continuations run at defined points between tasks. This matters for ordering, starvation and latency.

## Concurrency
JavaScript can overlap I/O without executing multiple JavaScript statements simultaneously on one main thread. Use `Promise.all` for independent bounded work, sequential awaits when ordering matters, and concurrency limits for fan-out.

Never turn unbounded user-controlled input into an unbounded `Promise.all`.

## Errors
Understand synchronous exceptions, rejected promises, `try/catch`, error causes and custom error classes. Preserve causal context while avoiding sensitive information in external responses.

## Modules
Know ESM imports/exports, CommonJS, package boundaries, resolution, dynamic imports and circular dependencies. Prefer explicit module ownership and avoid hidden initialization side effects.

## Browser/runtime fundamentals
For frontend work understand DOM events, event propagation, fetch, storage, cookies, Web Workers, service workers, rendering and browser security boundaries. For Node.js, understand the event loop, streams, buffers and process lifecycle.

## Memory and performance
Garbage collection does not make memory management irrelevant. Watch retained closures, listeners, caches, large object graphs and accidental copies. Avoid CPU-heavy work on latency-sensitive event loops.

Measure before optimizing. Use profiling, allocation inspection and realistic workloads rather than intuition.

## Production patterns
- Keep async functions cancellation-aware where the platform supports it.
- Bound concurrency and queue CPU-heavy work.
- Prefer immutable data flow when it reduces accidental coupling.
- Make serialization/deserialization explicit at boundaries.
- Avoid global mutable state.
- Treat external values as untrusted until validated.

## Security
Understand XSS, prototype pollution, unsafe deserialization, dependency supply chain risk, secret exposure and server-side request forgery at the application level. Do not treat JavaScript language features as a security boundary.

## Common mistakes
- forgetting rejected promises
- using `forEach(async () => ...)` when awaiting is required
- assuming `Promise.all` limits concurrency
- accidental shared mutation
- retaining large objects through closures
- confusing browser and Node.js APIs
- relying on implicit coercion

## Interview-level topics
Event loop and microtasks, closures, prototype chain, `this`, promises, async concurrency, streams, garbage collection, ESM/CJS, memory leaks and runtime performance.

## Related
TypeScript, React, Node.js, Next.js, Vitest, Playwright.