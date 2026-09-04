# LiteLLM

**Role:** Primary | **Layer:** AI gateway/integration

## Mental model
LiteLLM provides a common interface and gateway pattern across model providers. Its value is centralized routing, policy, observability and usage control; its cost is another compatibility and operational layer.

```text
applications
    -> AI gateway
       -> provider/model A
       -> provider/model B
       -> self-hosted model
```

## When it helps
Use a gateway when multiple providers, centralized budgets, routing, fallbacks, tenant policy or unified telemetry materially reduce application complexity.

For a single provider with simple requirements, direct SDK usage may be simpler.

## Routing
Understand model aliases, routing policies, weighted selection, latency/cost routing and fallbacks. Routing must preserve semantic requirements; a fallback that is cheaper but incompatible with the task is not a successful fallback.

## Reliability
Set bounded timeouts and retries. Avoid retry amplification across application, gateway and provider layers. Track retry counts and distinguish transient rate limits from permanent validation/authentication failures.

## Cost and budgets
Centralize token/cost accounting where possible. Define limits by service, user or tenant and fail gracefully when budgets are exhausted.

## Compatibility
Provider normalization can hide meaningful differences in context limits, structured output guarantees, tool calling, streaming, safety behavior and error semantics. Do not assume APIs are behaviorally identical because they share a wrapper.

## Production architecture
```text
request
 -> auth/tenant policy
 -> model selection
 -> gateway
 -> provider
 -> response validation
 -> telemetry/cost accounting
```

Keep application-level authorization and domain logic outside the gateway.

## Security
Protect gateway credentials, restrict model access, enforce tenant isolation and prevent arbitrary user-selected model/provider access unless explicitly intended.

## Observability
Record selected model, provider, latency, token usage, retries, fallback reason and outcome. Correlate with application traces and evaluation runs.

## Testing
Test routing policies deterministically. Contract-test critical providers and evaluate fallbacks for quality, not only API compatibility.

## Common mistakes
- adding a gateway before there is a routing/policy problem
- treating providers as behaviorally identical
- unlimited fallbacks
- retrying at every layer
- hiding model identity from evaluation
- allowing clients to choose privileged models directly

## Interview-level topics
Gateway architecture, provider abstraction, routing, fallback semantics, retry amplification, cost controls and multi-provider trade-offs.

## Related
OpenAI SDK, LangGraph, Langfuse, Kubernetes, observability.