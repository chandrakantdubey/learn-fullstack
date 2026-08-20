# Python Stack in Fullstack Engineering

This repo treats `learn-python` as the language-depth source of truth. This file explains which Python concepts matter specifically for production Fullstack and AI systems.

## Canonical path

```text
Python
  ↓
typing / dataclasses / exceptions
  ↓
asyncio + concurrency
  ↓
httpx + FastAPI
  ↓
Pydantic
  ↓
SQLAlchemy + psycopg
  ↓
Redis client
  ↓
pytest
  ↓
uv + pyproject.toml
  ↓
Docker + observability
```

## Default choices

| Need | Default |
| --- | --- |
| Runtime | CPython |
| Environment/package workflow | uv + `pyproject.toml` |
| API | FastAPI |
| Validation | Pydantic |
| PostgreSQL | psycopg + SQLAlchemy |
| HTTP client | httpx |
| Testing | pytest |
| Lint/format | Ruff |
| Logging | standard logging or structlog where structured logs justify it |
| Async runtime | asyncio |

## Engineering focus

Do not memorize Python syntax here. Focus on runtime behavior, typing, async I/O, resource ownership, dependency boundaries, testing, packaging, and operational behavior.

Deep language coverage remains in `learn-python`.
