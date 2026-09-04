# LiteLLM

**Role:** Primary | **Layer:** AI gateway/integration

## Mental model
LiteLLM provides a common interface and gateway pattern across multiple model providers, making routing, fallbacks and usage controls easier to centralize.

## Learn
- provider normalization
- proxy/gateway architecture
- routing and fallbacks
- budgets and rate limits
- retries and timeouts
- logging and cost tracking

## Production
Use explicit provider/model policies, bounded retries, fallback only when semantics permit, and preserve model/version metadata for debugging and evaluation.

## Tradeoff
A gateway adds an operational and compatibility layer. Use it when multi-provider routing or centralized policy is valuable, not automatically for a single-provider application.
