# Langfuse

**Role:** Primary | **Layer:** LLM observability/evaluation

## Mental model
Langfuse provides an observability and evaluation layer for LLM applications. It connects traces, prompts, model generations, token usage, costs and evaluation scores so teams can debug behavior and measure change.

```text
request
 -> workflow trace
    -> retrieval/tool spans
    -> model generation
    -> output/evaluation
```

## What to capture
Useful metadata includes service, environment, workflow/version, model/provider, latency, token usage, retry count and evaluation identifiers. Capture enough context to debug without collecting sensitive content unnecessarily.

## Prompt management
Treat prompts as versioned artifacts. Changes should be attributable to a version and evaluated against a representative dataset.

## Evaluation
Build datasets from real task distributions and define task-specific criteria. Automated evaluators can help, but important quality claims should be grounded in representative examples and, where needed, human review.

## Cost and latency
Track input/output token usage, provider/model and latency. Compare quality against cost and latency rather than optimizing one metric independently.

## Production patterns
- Correlate traces with application request IDs.
- Redact secrets and sensitive user data.
- Sample high-volume low-value telemetry when necessary.
- Preserve model/prompt/version metadata.
- Separate production monitoring from offline evaluation datasets.
- Alert on meaningful quality/cost/latency regressions.

## Security
Telemetry systems can become a copy of application data. Apply retention, access control, encryption and redaction policies. Do not assume observability data is harmless because it is "only logs."

## Testing
Use evaluation datasets for model behavior and conventional unit/integration tests for application logic. A trace viewer is not a substitute for a regression suite.

## Common mistakes
- logging everything by default
- no prompt/model versioning
- evaluating only cherry-picked examples
- tracking latency without token/cost context
- treating an LLM judge as ground truth

## Interview-level topics
LLM tracing, prompt/version management, evaluation datasets, cost accounting, sampling, redaction and production AI quality monitoring.

## Related
OpenTelemetry, OpenAI SDK, LangGraph, RAG, evaluation.