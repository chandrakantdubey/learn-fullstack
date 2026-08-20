# Systems Foundations

Understand the machine and network before relying on infrastructure abstractions.

## Core areas

- Linux processes and threads
- Filesystems and permissions
- Processes, signals, and file descriptors
- Memory and CPU behavior
- TCP/UDP and sockets
- DNS
- Routing, NAT, and subnets
- Concurrency and parallelism
- Async I/O and event loops
- Backpressure
- Profiling and performance
- Resource limits

## Debugging mindset

When a system is slow or broken, move down the stack:

```text
User symptom
  ↓
Application
  ↓
Runtime
  ↓
Process / thread
  ↓
Network
  ↓
OS resources
  ↓
Infrastructure
```

The objective is to diagnose from evidence rather than guess from the framework layer.
