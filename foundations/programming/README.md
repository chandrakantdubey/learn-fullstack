# Programming Foundations

Programming is the first layer of the Fullstack Engineer mental model.

This section is not a syntax course. The goal is to understand how programs represent state, transform data, handle failure, perform work concurrently, and expose boundaries that remain maintainable as systems grow.

## Core mental model

A production program is a combination of:

```text
Input
  -> validation
  -> state / data
  -> computation
  -> side effects
  -> output
```

Around that flow are the engineering concerns:

```text
Correctness
Reliability
Performance
Security
Observability
Maintainability
Testability
```

## What a Fullstack Engineer should understand

### 1. Data and state

- Primitive vs compound values
- Mutable vs immutable state
- Value semantics vs reference semantics
- Data structures and their access costs
- Serialization and deserialization
- In-memory state vs durable state
- Ownership and lifetime of data

### 2. Control flow

- Branching
- Iteration
- Recursion
- Exceptions
- Early returns
- State machines
- Event-driven control flow

The key question is not "what syntax does the language use?" but "what execution path exists, and what happens when it fails?"

### 3. Functions and boundaries

Functions are the smallest useful abstraction boundary.

A good function has:

- Explicit inputs
- Explicit output
- Limited side effects
- A clear responsibility
- Predictable failure behavior

As systems grow, the same idea becomes:

```text
function
  -> module
  -> package
  -> library
  -> service
  -> system boundary
```

### 4. Errors

Treat errors as part of the contract.

Distinguish between:

- Programmer errors
- Invalid input
- Missing resources
- Dependency failures
- Timeouts
- Conflicts
- Authorization failures
- Transient failures
- Permanent failures

A production engineer must know which errors should be retried, surfaced to a caller, converted into a domain error, logged, or ignored.

### 5. Concurrency

Understand the difference between:

- Sequential execution
- Concurrency
- Parallelism
- Asynchronous I/O
- Threads
- Processes
- Event loops
- Worker pools

A useful model is:

```text
CPU-bound work   -> use CPU parallelism
I/O-bound work   -> use asynchronous/concurrent I/O
Long-running job -> move work outside request path
```

### 6. Complexity

Know how to reason about:

- Time complexity
- Space complexity
- Throughput
- Latency
- Allocation cost
- Network cost
- Database cost

Big-O is useful, but production engineering also requires asking which resource is actually limiting the system.

### 7. Testing

Test behavior at the right boundary.

- Unit tests for local logic
- Integration tests for real boundaries
- Contract tests for service interfaces
- End-to-end tests for critical user journeys
- Load tests for capacity assumptions

Avoid testing implementation details when behavior is what matters.

## Python and TypeScript

This repository uses two canonical implementation stacks:

- Python for backend, automation, data, and AI engineering
- TypeScript for frontend and Node.js backend engineering

Learn the language deeply enough to understand its runtime, type system, concurrency model, package ecosystem, and failure modes.

## Connection to the rest of the repo

Programming foundations support:

```text
Programming
   |
   +--> Web and HTTP
   +--> Frontend architecture
   +--> Backend architecture
   +--> Databases
   +--> Linux and networking
   +--> Distributed systems
   +--> Production engineering
```

A framework should make these ideas easier to implement, not replace the need to understand them.
