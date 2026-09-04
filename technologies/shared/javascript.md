# JavaScript

**Role:** Primary | **Layer:** Shared

## Mental model
JavaScript is a dynamically typed, garbage-collected language whose execution is organized around values, lexical environments, functions, objects, the prototype chain and an event loop.

## Core areas
- primitives vs objects
- equality, coercion and truthiness
- scope, closures and `this`
- prototypes and classes
- modules and package boundaries
- promises, async/await and errors
- event loop, tasks, microtasks and I/O
- iterators, generators and async iterators
- memory, garbage collection and performance

## Production rules
Prefer explicit data flow, immutable-by-default application state, async error handling, bounded concurrency and clear module ownership. Avoid accidental global state, implicit coercion and unbounded promise creation.

## Full-stack importance
The same language semantics appear in browsers, Node.js services, build tooling and tests. Deep JavaScript knowledge makes framework behavior predictable instead of magical.

## Related
TypeScript, React, Node.js, Next.js, Vitest, Playwright.
