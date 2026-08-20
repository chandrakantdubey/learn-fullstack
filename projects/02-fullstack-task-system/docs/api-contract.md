# API Contract

Base path: `/api/v1`

## Authentication

`POST /auth/register`

`POST /auth/login`

`POST /auth/refresh`

`POST /auth/logout`

Access tokens should be short-lived. Refresh tokens should use secure, httpOnly cookies when browser sessions are used.

## Tasks

`GET /tasks?status=todo&limit=50&cursor=...`

`POST /tasks`

`GET /tasks/{task_id}`

`PATCH /tasks/{task_id}`

`DELETE /tasks/{task_id}`

Every task endpoint is authenticated and authorization-scoped to the current user/tenant.

## Mutation contract

Mutation requests may include:

```http
Idempotency-Key: 01J...
```

For retryable creates/commands, the server stores the key with the resulting operation identity and returns the same semantic result for duplicate requests.

## Error shape

```json
{
  "error": {
    "code": "TASK_NOT_FOUND",
    "message": "Task not found",
    "request_id": "req_123"
  }
}
```

Clients branch on stable `code`, not human-readable `message`.

## Pagination

Prefer cursor pagination for mutable, high-volume collections. The cursor is opaque to clients and encodes enough state to preserve a stable traversal boundary.

## Concurrency

Use conditional updates for state transitions where concurrent writers matter, for example:

```sql
UPDATE tasks
SET status = $new_status,
    version = version + 1
WHERE id = $id
  AND owner_id = $owner
  AND version = $expected_version;
```

A zero-row update becomes a conflict instead of silently overwriting another writer.
