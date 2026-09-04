# File Upload Pipeline

Large files should usually bypass application servers instead of flowing through every API instance.

## Boundary

```text
browser
  → authorized upload initiation
  → object storage direct upload
  → completion event / API
  → async scan/process
  → metadata + derived assets
  → authorized download
```

## Invariants

- Upload authorization is scoped to the intended user/tenant and object.
- Object keys are server-controlled or safely namespaced.
- Untrusted files are never treated as safe merely because their extension looks valid.
- Metadata becomes authoritative only after the upload is verified.
- Downloads enforce authorization independently.

## Implementation choices

Use short-lived signed upload URLs when object storage supports them. Enforce size, content-type, expiration, and destination constraints. Store application metadata in PostgreSQL and binary content in object storage.

Process expensive work asynchronously: malware scanning, media transcoding, OCR, thumbnail generation, indexing, or embedding. Make processors idempotent.

## Failure modes

- orphaned objects after failed application transactions
- trusting client MIME type or filename
- publicly readable objects by default
- oversized uploads exhausting infrastructure
- processing the same object multiple times
- exposing object-storage credentials to browsers

## Security

Validate file signatures where appropriate, normalize or discard untrusted filenames, scan active/untrusted content, and isolate processing workloads. Prevent path traversal and SSRF-style fetches from document processors.

## Performance

Prefer multipart/resumable uploads for large objects. Stream rather than buffering entire files in application memory. Apply quotas and concurrency limits to processing workers.

## Operational signals

Track upload failures, abandoned objects, processing latency, queue age, scan failures, storage growth, and download authorization failures.
