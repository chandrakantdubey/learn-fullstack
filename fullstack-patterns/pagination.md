# Pagination and Cursor Design

Pagination is a data-access contract, not just a UI convenience.

## Problem

Offset pagination is simple but becomes inefficient or unstable for large, frequently changing datasets. Cursor pagination can provide stable traversal but requires a well-defined ordering.

## Boundary

The API contract should define page size limits, ordering, cursor encoding, filtering, and what consistency guarantees apply between pages.

## Invariants

- Ordering is deterministic.
- A cursor encodes enough position information to continue from a known point.
- The server enforces maximum page size.
- Cursor contents are treated as untrusted input.
- Authorization and tenant scope are applied before pagination semantics.

## Implementation choices

Offset pagination works well for small administrative lists and direct page navigation.

Cursor pagination is usually preferable for large feeds. A common design uses a compound key such as `(created_at, id)` and queries rows after that tuple in the requested order. The unique ID breaks timestamp ties.

Opaque, signed or otherwise integrity-protected cursors prevent clients from casually modifying internal positions. Cursors should have a version so the encoding can evolve.

## Failure modes

- ordering only by a non-unique timestamp
- changing filters between pages
- cursor based on mutable fields
- returning huge pages
- leaking database IDs or internal state unnecessarily
- using `OFFSET` on very large tables without understanding its cost

## Security

Never let a cursor bypass authorization. Treat decoded cursor fields as attacker-controlled. Avoid embedding sensitive information in opaque cursors unless encrypted and justified.

## Performance

Index the filter and ordering columns together. Select only required columns. Measure database work and tail latency at realistic depths.

## Operational signals

Track page-size distribution, slow queries, deep-offset usage, cursor decode failures, and high-cardinality query patterns.
