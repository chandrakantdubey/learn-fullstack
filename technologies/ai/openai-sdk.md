# OpenAI SDK

**Role:** Primary | **Layer:** AI application integration

## Mental model
An AI SDK is an application boundary around model APIs. The SDK handles transport and provider-specific protocol details; the application still owns prompts, schemas, authorization, retries, budgets, tool policies, evaluation and business behavior.

```text
application
  -> request policy
  -> SDK
  -> provider API
  -> model
  -> structured/streamed result
  -> validation + policy
  -> application
```

## Core capabilities
Learn text generation, structured outputs, streaming, embeddings, tool/function calling, request metadata, error handling and asynchronous execution.

## Structured outputs
Prefer constrained structured responses when downstream code needs machine-readable data. Validate outputs at the runtime boundary rather than assuming the model followed instructions.

## Streaming
Streaming improves perceived latency by delivering output incrementally. It does not automatically reduce total generation time or cost. Design cancellation, disconnect handling and partial-output semantics explicitly.

## Tool calling
A model suggesting a tool call is not authorization. Treat the model output as an untrusted request:

```text
model proposes tool call
        -> validate arguments
        -> authenticate user
        -> authorize action
        -> enforce policy/limits
        -> execute
        -> validate result
        -> return controlled result to model
```

## Reliability
Set explicit timeouts, classify retryable errors, bound retries with backoff/jitter and avoid retrying non-idempotent side effects blindly. Provider rate limits require application-level concurrency and quota control.

## Cost control
Track input/output tokens, request counts, model choice and latency. Define budgets by user, tenant, workflow or service where required. Route simple tasks to cheaper models only when quality is acceptable.

## Prompt engineering as software engineering
Version prompts, keep them testable, separate instructions from untrusted content, and evaluate changes against representative datasets. Prompt text alone is not a security boundary.

## Security
Keep credentials server-side. Protect against prompt injection, data leakage and tool abuse. Never let model-generated content directly become SQL, shell commands, privileged API calls or filesystem paths without deterministic validation and authorization.

## Observability
Record provider/model/version, latency, token usage, finish reason, retry count and workflow identifiers. Redact sensitive inputs/outputs according to data policy.

## Testing
Use mocked provider responses for deterministic unit tests, contract/integration tests for API wiring and evaluation datasets for model behavior. Test malformed structured output, tool failures, timeouts and rate limits.

## Common mistakes
- trusting model output as typed data
- exposing API keys to browsers
- unlimited retries
- allowing arbitrary tool execution
- no model/prompt version tracking
- measuring only average latency
- treating streaming as a correctness guarantee

## Interview-level topics
Structured outputs, streaming, tool calling, retries, rate limits, token economics, prompt/version management, model evaluation and secure AI application boundaries.

## Related
Zod, OpenAPI, LiteLLM, LangGraph, Langfuse, MCP.