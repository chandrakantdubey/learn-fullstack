# Realtime, Streaming and Long-Lived Connections

Realtime features are a combination of transport semantics, connection lifecycle, state management and failure handling.

## Choose the transport by requirement

| Need | Typical choice |
|---|---|
| request/response | HTTP |
| server → client event stream | SSE |
| bidirectional interactive session | WebSocket |
| large response/body | HTTP streaming |
| durable asynchronous work | queue/event system |

Do not use WebSockets merely because the product says "realtime". A polling or SSE design may be simpler and more reliable.

## SSE

Server-Sent Events keep an HTTP response open and send named events to the browser. They are useful for notifications, progress updates and streamed model output.

Design reconnect behavior, event IDs, heartbeat/keepalive and authorization carefully.

## WebSockets

WebSockets provide a long-lived bidirectional channel. The application must define message schemas, authentication, authorization, heartbeats, reconnect behavior, ordering expectations and backpressure.

A WebSocket connection is not a durable message queue. Messages can be lost when a client disconnects unless the application provides persistence/replay semantics.

## Streaming AI responses

A common fullstack path is:

```text
browser
  ↓
HTTP/SSE stream
  ↓
API
  ↓
model provider / inference server
```

Cancellation must propagate when the user stops generation. The server should not continue expensive model work indefinitely after the browser has abandoned the request.

## Backpressure

Slow clients can cause buffers to grow. Bound output queues and define behavior when consumers cannot keep up: pause, drop, disconnect, or persist for later delivery.

## Reconnection

Clients should assume connections fail. Use bounded exponential backoff with jitter, prevent reconnect storms, and make resumed delivery explicit when the product requires it.

## Security

Authenticate the connection and authorize every operation. Validate message size and schema. Never treat a connected socket as permanently trusted: credentials expire and tenant context must remain enforced.

## Testing

Test disconnects, reconnects, duplicate events, out-of-order delivery where possible, slow consumers, expired credentials, server restarts and partial downstream failures.
