# Encoding, Unicode, Bytes and Serialization

Many production bugs come from confusing four different things: characters, bytes, encodings and serialized representations.

## Mental model

```text
human text
  ↓
characters / Unicode code points
  ↓
encoding (for example UTF-8)
  ↓
bytes
  ↓
transport / storage
```

Serialization is a separate concern:

```text
in-memory value → serialized representation → bytes → transport/storage
```

JSON is a serialization format. UTF-8 is an encoding. Base64 is an encoding of bytes into text. None of these is encryption.

## Unicode

Unicode assigns abstract code points to characters. A visible glyph may be composed from multiple code points, so string length is not always equivalent to the number of user-perceived characters. Unicode normalization can matter when comparing or indexing text.

Fullstack applications should define whether a field is measured in bytes, code points, UTF-16 code units, grapheme clusters or domain-specific units.

## UTF-8

UTF-8 encodes Unicode code points into one to four bytes. It is backward-compatible with ASCII for ASCII characters and is the dominant web encoding.

Never assume one character equals one byte.

## Base64

Base64 converts arbitrary bytes into a text representation. It is useful for transport where binary data is inconvenient, but it provides no secrecy and increases size.

## Serialization choices

JSON is simple and interoperable but has a limited type model. Binary protocols can improve size and speed when contracts are stable and both ends support the protocol. MessagePack, Protocol Buffers and similar formats introduce explicit schema/versioning concerns.

## Boundaries

Validate decoded data at trust boundaries. Treat serialized input as untrusted even when it came from your own system: queues, caches, browser storage and databases can contain stale or malformed data.

Important concerns:

- schema evolution
- unknown fields
- missing/default fields
- numeric precision
- date/time representation
- binary payloads
- backward/forward compatibility
- maximum payload size
- canonicalization when signatures depend on exact bytes

## Production mistakes

- Double-encoding JSON or base64.
- Treating base64 as encryption.
- Comparing Unicode strings without considering normalization.
- Using floating-point JSON values for exact monetary quantities.
- Deserializing untrusted objects into executable or dangerous runtime types.
- Letting payload size be unbounded.
- Changing a message schema without considering old consumers.

## Fullstack contract

A robust request path looks like:

```text
bytes → protocol decode → schema validation → domain model → business logic
```

A response reverses the process. Keep transport DTOs separate from domain objects when their lifecycles or invariants differ.
