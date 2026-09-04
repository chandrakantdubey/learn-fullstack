# Regular Expressions

Regular expressions are a compact language for matching text patterns. They are useful for search, extraction, tokenization, log processing and input checks, but they are not a substitute for a parser or domain validation.

## Mental model

A regex engine consumes input and tries to find a path through a pattern. The important ideas are literals, character classes, quantifiers, groups, alternation, anchors and boundaries.

```text
text → pattern → engine → match / captures / failure
```

## Core constructs

- `^` / `$`: start and end anchors; understand multiline semantics.
- `.`: usually any character except line terminators.
- `[]`: character class; use ranges and negation carefully.
- `\d`, `\w`, `\s`: shorthand classes; semantics vary by engine and Unicode mode.
- `*`, `+`, `?`, `{m,n}`: repetition.
- `( ... )`: capture group.
- `(?: ... )`: non-capturing group.
- `(?<name>...)`: named capture where supported.
- `|`: alternation.
- `\b`: word boundary; it is not a universal token boundary.
- lookahead/lookbehind: zero-width assertions supported by many modern engines.

## Engineering use

Use regex for local lexical rules: extracting IDs from logs, checking a simple identifier shape, splitting structured text, or finding references in source. Prefer dedicated parsers for JSON, URLs with complex semantics, programming languages, HTML, SQL and other recursive/grammar-heavy formats.

Validation should usually be layered:

```text
lexical shape → schema/type validation → domain invariants → authorization
```

A regex can establish shape; it cannot establish that an email is deliverable, a username is available, or a user is authorized.

## Security

Untrusted regex patterns can be dangerous. Backtracking engines can exhibit catastrophic backtracking when ambiguous nested repetition creates exponential work. Never accept arbitrary user-controlled patterns without limits and isolation. For security-sensitive matching, keep patterns simple, bound input length, benchmark worst cases, and consider a linear-time regex engine where appropriate.

Do not use regex to "sanitize" HTML or SQL. Use context-aware escaping and parameterized APIs.

## Performance

Prefer anchored patterns when you need full-string validation. Reduce ambiguous alternation and nested quantifiers. Compile/reuse hot patterns when the runtime exposes compilation. Measure against realistic and adversarial input rather than assuming a short pattern is fast.

## Cross-language note

JavaScript, Python and other languages differ in flags, Unicode behavior, named-group syntax, escaping rules and supported lookarounds. Treat the regex dialect as part of the implementation boundary.

## Production checklist

- Bound input size.
- Decide whether matching or full validation is intended.
- Specify Unicode/ASCII behavior.
- Test empty, maximum-length and adversarial input.
- Keep patterns readable and named.
- Document the regex dialect and flags.
- Do not put business logic into unreadable regexes.
