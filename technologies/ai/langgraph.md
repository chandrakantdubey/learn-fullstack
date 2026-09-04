# LangGraph

**Role:** Primary | **Layer:** Agentic AI

## Mental model
LangGraph models an agent or workflow as a state machine/graph. Nodes perform bounded work, edges determine transitions, and persisted state can make long-running execution explicit.

```text
input -> node -> condition -> node -> tool -> node -> final
             \-> retry/error -> recovery
```

The important idea is explicit control flow. An agent is not simply an unbounded loop around an LLM.

## State
Define the smallest useful state. Separate durable business state from transient model context. Persist only what must survive process restarts or human pauses.

## Nodes and edges
Nodes should have clear inputs/outputs and bounded side effects. Conditional edges make routing explicit and testable.

## Tools
Tools are privileged capabilities. Validate arguments, authorize against the current user/tenant, enforce limits and make side effects idempotent where retries are possible.

## Human-in-the-loop
Interrupts can pause execution for approval or clarification. Treat approval as a security boundary and persist enough state to resume safely.

## Persistence and recovery
Durable agent execution needs checkpoints, retry policies and explicit failure states. A process crash should not cause duplicate financial, communication or destructive side effects.

## Deterministic vs agentic control
Prefer deterministic workflow code for known business rules. Use model-driven routing where uncertainty or natural-language reasoning provides real value.

```text
Known workflow -> normal code
Uncertain decision -> model proposal -> policy/validation -> action
```

## Production patterns
- Bound graph steps and total execution time.
- Bound tool calls and token budgets.
- Add per-node timeouts.
- Make external side effects idempotent.
- Persist workflow state deliberately.
- Record model/tool decisions for debugging and evaluation.
- Separate policy from model-generated suggestions.

## Security
Assume model output and retrieved/tool data may contain adversarial instructions. Never let the model bypass authorization. Use allowlisted tools, least privilege, input/output validation and explicit confirmation for high-impact actions.

## Evaluation
Evaluate both final outcomes and trajectories: tool selection, argument correctness, unnecessary loops, latency, cost, policy violations and recovery behavior.

## Common mistakes
- infinite agent loops
- giving agents excessive permissions
- treating model reasoning as authorization
- persisting sensitive context indiscriminately
- retrying non-idempotent side effects
- using agents where a deterministic workflow is simpler

## Interview-level topics
State graphs, checkpoints, durable execution, human approval, retries, idempotency, tool security, deterministic workflows vs agents and trajectory evaluation.

## Related
OpenAI SDK, MCP, Langfuse, RAG, security.