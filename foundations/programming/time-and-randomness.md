# Time, Clocks and Randomness

Production software fails when it treats time and randomness as simple primitives. They are environmental inputs with different guarantees.

## Time is not one thing

Distinguish:

- **wall-clock time** — calendar time used for timestamps and user-visible dates
- **monotonic time** — elapsed-time measurement that should not move backward when the system clock changes
- **duration** — an interval, not a timestamp
- **timezone** — a rule set for mapping local civil time to instants

Use monotonic clocks for deadlines, timeouts and latency measurement. Use wall-clock time for persisted business timestamps.

## UTC and time zones

Persist instants in a well-defined representation, normally UTC, and apply a user's timezone at the presentation boundary. A local time such as `09:00` is not an instant until a timezone and date are known.

DST transitions can create missing or repeated local times. Business rules such as "every day at 9 AM" therefore need explicit timezone semantics.

## Deadlines

Prefer a deadline that propagates through a call graph:

```text
request deadline
  -> service
     -> database
     -> HTTP dependency
     -> queue / worker
```

A child operation should not receive a timeout longer than the remaining caller budget.

## Randomness

Separate:

- ordinary pseudo-randomness for simulations and non-security features
- cryptographically secure randomness for secrets, session identifiers, reset tokens and security-sensitive identifiers

Never use predictable application randomness for authentication or authorization material.

## IDs and ordering

An identifier does not automatically provide ordering, uniqueness across systems, or secrecy. Choose identifiers based on the actual requirement: uniqueness, locality, sortability, opacity, or coordination.

## Production checklist

- Use monotonic time for elapsed-time measurements.
- Define timestamp precision and timezone semantics.
- Make timeout/deadline propagation explicit.
- Test DST and boundary dates for user-facing scheduling.
- Use a CSPRNG for security tokens.
- Do not infer security from an opaque-looking identifier.
- Keep time-dependent tests deterministic with injectable clocks.
