# Parsing vs Validation

Parsing answers **what structure can be extracted from this input?** Validation answers **is that parsed value allowed by the application's rules?**

They are related but should not be collapsed into one concept.

## Examples

- JSON parsing turns bytes/text into values; schema validation checks required fields and types.
- URL parsing identifies components; application validation decides whether a URL is an allowed destination.
- SQL parsing builds a query representation; authorization decides whether the operation is permitted.
- A JWT can be structurally decoded; signature, issuer, audience, expiry and authorization still need verification.

## Trust-boundary model

```text
raw bytes / text
      ↓
parse
      ↓
structured value
      ↓
validate shape + constraints
      ↓
authorized domain operation
```

Never treat successful parsing as proof of safety or correctness.

## Production rules

- Parse according to the protocol's grammar.
- Validate size, shape, ranges, invariants and allowed values.
- Normalize only when the domain explicitly requires normalization.
- Perform authorization separately from parsing and validation.
- Reject ambiguous or malformed representations rather than guessing.
- Preserve useful error semantics without leaking sensitive internals.

## Cross-layer ownership

Language repositories own language-specific parsers and APIs. `learn-fullstack` owns the trust-boundary mental model. API contracts and Zod/Pydantic notes describe implementation choices.

## Related concepts

- regex and text processing
- Unicode and encoding
- serialization
- API contracts
- authentication and authorization
- cryptography
