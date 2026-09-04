# LangGraph

**Role:** Primary | **Layer:** Agentic AI

## Mental model
LangGraph models an agent/workflow as a graph of stateful nodes and transitions, making control flow, persistence, retries and human intervention explicit.

## Learn
- graph/state/node/edge concepts
- conditional routing
- checkpoints and persistence
- interrupts and human-in-the-loop
- tool execution
- retries and failure handling
- streaming

## Production
Prefer explicit deterministic workflows where possible, constrain tool permissions, validate tool arguments/results, persist only necessary state, and make every side effect idempotent.

## Important distinction
An agent is not simply an LLM in a loop. Production agent systems need bounded execution, state, tools, policies, observability and evaluation.

## Related
OpenAI SDK, MCP, Langfuse, RAG, security.
