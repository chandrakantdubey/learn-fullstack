# TypeScript

**Role:** Primary | **Layer:** Shared

## Mental model
TypeScript is a static type system layered over JavaScript. The compiler checks relationships between values before runtime, but emitted JavaScript has no type enforcement. A production system therefore has two worlds: compile-time guarantees and runtime trust boundaries.

```text
source code
  -> TypeScript compiler -> JavaScript
       |                     |
       | static checks       | runtime behavior
       v                     v
developer confidence      external data must still be validated
```

## Core type model

### Structural typing
TypeScript compares compatible structure rather than nominal identity. This makes composition convenient but means two unrelated objects can satisfy the same interface.

### Unions
Use unions to model alternatives:

```ts
type Result<T> =
  | { ok: true; value: T }
  | { ok: false; error: Error };
```

Prefer discriminated unions for states and protocols because narrowing becomes explicit and exhaustive.

### `unknown`, `any`, `never`
- `unknown`: safe boundary value; must be narrowed before use.
- `any`: disables checking; contain it at integration edges.
- `never`: impossible state or exhaustive branch.

### Generics
Generics express relationships between inputs and outputs rather than simply adding flexibility. Prefer constrained generics when an API depends on a capability:

```ts
function first<T>(items: readonly T[]): T | undefined {
  return items[0];
}
```

### Utility and advanced types
Know `Pick`, `Omit`, `Partial`, `Required`, `Record`, `ReturnType`, `Awaited`, indexed access, mapped types, conditional types, template literal types and `satisfies`. Use them to model real relationships; do not build type puzzles that obscure business logic.

## Narrowing
Narrow with `typeof`, `in`, equality checks, user-defined type guards and discriminants. Treat `unknown` as the normal type for untrusted data until validated.

## Functions
Understand optional/rest parameters, overloads, generic functions, callbacks, contextual typing and variance. Keep public function contracts narrow and avoid accepting more shapes than the implementation can correctly handle.

## Modules and packages
Understand ESM, CommonJS interoperability, package `exports`, `types`, declaration files, module resolution and project references. A type-safe monorepo still needs clear package ownership and dependency direction.

## Compiler configuration
Use strict mode. Know `target`, `module`, `moduleResolution`, `lib`, `noEmit`, `isolatedModules`, `exactOptionalPropertyTypes`, `noUncheckedIndexedAccess`, declaration generation and source maps. Treat compiler configuration as architecture, not boilerplate.

## Runtime boundaries
TypeScript does not validate HTTP requests, database rows, environment variables, webhook payloads or model responses. Use the canonical Zod note for TypeScript runtime schemas.

## API and domain types
Do not automatically reuse one type everywhere. Transport DTOs, domain objects, persistence models and UI view models can have different lifecycles and invariants.

```text
HTTP DTO -> validation -> command/domain model -> persistence model
                                      |
                                      +-> response/view model
```

## Production patterns
- Enable strict checking.
- Prefer `unknown` over `any` at boundaries.
- Use discriminated unions for state machines and result types.
- Keep assertions rare and justified.
- Avoid enums when literals/unions provide a simpler public contract.
- Keep public package APIs intentional.
- Make impossible states difficult to represent.
- Do not encode business rules solely in types when runtime enforcement is required.

## Performance
Type-level complexity can slow builds even though types disappear at runtime. Avoid deeply recursive generic machinery unless it provides real value. At runtime, performance remains JavaScript performance: allocations, serialization, event-loop blocking and network behavior matter.

## Testing
The compiler verifies type relationships, not behavior. Combine type checking with unit, integration and browser tests. Test runtime validation separately from compile-time assumptions.

## Debugging checklist
1. Reproduce runtime behavior.
2. Inspect inferred types in the smallest failing expression.
3. Check whether an assertion or `any` erased useful information.
4. Verify module resolution and generated declarations.
5. Confirm the runtime value actually matches the declared type.

## Common mistakes
- believing interfaces validate JSON
- overusing `as`
- leaking database types into public APIs
- using `any` to unblock builds
- creating giant shared type packages with unclear ownership
- confusing optional properties with nullable values

## Interview-level topics
Structural vs nominal typing, variance, narrowing, generic constraints, conditional/mapped types, module resolution, declaration emit, `unknown` vs `any`, runtime validation, and designing type-safe API boundaries.

## Related
JavaScript, Zod, OpenAPI, React, Node.js, Fastify.