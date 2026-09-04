# TypeScript

**Role:** Primary | **Layer:** Shared

## What it is
TypeScript is JavaScript with a static type system and tooling. Types are primarily removed during compilation; they do not validate runtime input.

## Mental model
Think in three boundaries: source types help humans and tooling, the compiler checks relationships before execution, and runtime validation protects the application from untrusted data.

## Core areas
- primitives, objects, arrays, tuples, unions and intersections
- narrowing, discriminated unions, generics and utility types
- functions, overloads and variance
- modules, ESM/CJS interoperability and package exports
- `tsconfig`, declaration files and project references
- type inference, `unknown`, `never`, `any` and strict mode

## Production patterns
Prefer strict mode, small domain types, discriminated unions for state machines, `unknown` at untrusted boundaries, and explicit public interfaces. Keep business types separate from transport DTOs when their lifecycles differ.

## Do not confuse
TypeScript types are not schemas, validation, authorization, database constraints, or API contracts. Pair runtime boundaries with the canonical Zod note.

## Testing/tooling
Use the compiler as a fast static check, then unit/integration/e2e tests for behavior. Avoid using type assertions to silence design problems.

## Learn deeply
Understand structural typing, narrowing, generic constraints, conditional/mapped types, module resolution, build output, declaration generation and type-safe API boundaries.

## Related
JavaScript, Zod, OpenAPI, React, Node.js, Fastify.
