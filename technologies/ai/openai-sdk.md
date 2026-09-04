# OpenAI SDK

**Role:** Primary | **Layer:** AI application integration

## Mental model
An AI provider SDK is a typed/programmatic boundary to model APIs. The application remains responsible for prompts, schemas, authorization, retries, budgets, observability and business behavior.

## Learn
- client configuration
- text generation and structured outputs
- streaming
- embeddings
- tool/function calling
- timeouts and retries
- request metadata and tracing

## Production
Keep API keys server-side, validate model outputs, set token/time budgets, classify retryable failures, protect against prompt/tool injection, and record cost/latency/model metadata for evaluation.

## Related
Zod, OpenAPI, LiteLLM, LangGraph, Langfuse.
