# Money and Numeric Precision

Money and measurements are boundary problems: the representation chosen in code must preserve the business invariant.

## Core model

Binary floating-point represents many decimal fractions approximately. That makes ordinary floating-point values unsafe for exact monetary equality, totals, and accounting rules.

Prefer one of these designs:

- integer minor units (`cents`, `paise`) for fixed-precision currencies;
- a decimal/numeric type when decimal arithmetic is required;
- an explicit domain value object that carries amount + currency.

Do not silently mix currencies or precision rules.

## Engineering rules

- Define rounding policy explicitly: half-up, half-even, floor, ceiling, etc.
- Round at the business boundary where the rule requires it, not arbitrarily after every operation.
- Store currency separately from amount unless the representation makes the currency unambiguous.
- Keep database, API and UI precision rules consistent.
- Never trust client-side arithmetic for authoritative financial state.
- Test boundary values, negative values, large values and repeated calculations.

## Cross-layer path

```text
UI input
  ↓
validated API value
  ↓
domain money type
  ↓
transaction
  ↓
PostgreSQL numeric/integer representation
  ↓
serialized response
```

The frontend repository owns display formatting; `learn-sql` owns database numeric types; this document owns the cross-layer invariant.

## Related concepts

- serialization and schema evolution
- validation at trust boundaries
- transactions and invariants
- localization and currency formatting
- auditability
