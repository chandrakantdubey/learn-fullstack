# Model Context Protocol (MCP)

**Role:** Primary | **Layer:** AI/tool integration

## Mental model
MCP defines a standardized way for AI applications to discover and interact with external tools, resources and prompts through explicit protocol boundaries.

## Learn
- hosts, clients and servers
- tools and structured arguments
- resources and prompts
- transport and lifecycle
- capability negotiation
- authorization and trust boundaries

## Production
Treat every tool as a privileged API. Validate arguments, authenticate and authorize calls, constrain outputs, audit execution, and assume tool descriptions or returned data can contain adversarial content.

## Related
LangGraph, OpenAI SDK, OWASP, agentic AI.
