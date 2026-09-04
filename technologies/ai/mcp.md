# Model Context Protocol (MCP)

**Role:** Primary | **Layer:** AI/tool integration

## Mental model
MCP standardizes communication between AI applications and external capabilities such as tools, resources and prompts. It creates an explicit protocol boundary, but it does not automatically make the capability safe.

```text
AI host
  -> MCP client
      -> MCP server
          -> tool/resource
              -> external system
```

## Core concepts
Understand hosts, clients, servers, tools, resources, prompts, capability negotiation, lifecycle and transport. Know which side owns authentication, authorization and execution policy.

## Tools
A tool is effectively a privileged API exposed to model-driven software. Define narrow schemas, bounded inputs and explicit semantics. Tool descriptions should explain intent without granting authority.

## Resources
Resources provide contextual data. Treat returned content as untrusted input; retrieved instructions can contain prompt injection or misleading commands.

## Security boundary
```text
model proposes action
        -> protocol validation
        -> user/tenant identity
        -> authorization
        -> policy/limits
        -> tool execution
        -> result validation
```

Never equate "the model requested it" with permission.

## Production patterns
- Allowlist servers and tools.
- Validate structured arguments.
- Enforce authentication and authorization outside model reasoning.
- Apply timeouts, rate limits and output-size limits.
- Audit high-impact tool calls.
- Require confirmation for destructive or consequential operations where appropriate.
- Isolate tool execution when capabilities are dangerous.

## Reliability
Tool servers are dependencies. Handle unavailable servers, timeouts, malformed results, partial failures and duplicate calls. Side effects should be idempotent where retries can occur.

## Observability
Trace model decision -> MCP call -> downstream operation. Record tool name, latency, status and policy outcome while redacting sensitive arguments/results.

## Testing
Contract-test schemas and tool behavior. Test malicious arguments, authorization failures, timeouts and duplicate execution. Evaluate agents on correct tool selection and safe behavior, not only final text.

## Common mistakes
- giving tools excessive permissions
- trusting tool descriptions as security policy
- executing arbitrary model-generated arguments
- no authorization context
- no audit trail for high-impact operations
- exposing sensitive resources indiscriminately

## Interview-level topics
Protocol boundaries, tool/resource semantics, capability negotiation, authorization, prompt injection, least privilege, idempotency and agent/tool observability.

## Related
LangGraph, OpenAI SDK, OWASP, agentic AI.