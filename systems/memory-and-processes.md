# Memory, Processes, Threads and Resource Lifecycles

Fullstack engineers need enough operating-system knowledge to understand why applications slow down, crash, leak resources or behave differently in containers.

## Process model

A process is an isolated execution environment with its own virtual address space and OS-managed resources. Threads execute within a process and generally share its memory.

```text
machine
 └─ OS
    ├─ process A
    │  ├─ heap
    │  ├─ stacks
    │  └─ threads
    └─ process B
```

Process isolation improves fault containment but makes shared-memory communication more expensive than in-process communication. Threads can communicate cheaply through shared memory but require synchronization.

## Memory layers

Understand the distinction between:

- stack and heap
- virtual memory and physical memory
- page cache
- memory-mapped files
- resident set size
- garbage-collected memory
- native allocations

A language runtime can reclaim managed objects while the process still holds resources such as file descriptors, sockets, buffers or native memory.

## Resource lifecycle

Treat every external resource as a lifecycle:

```text
acquire → use → release
```

Examples include database connections, HTTP connections, files, locks, subscriptions and worker processes. Leaks often occur when exceptional or cancellation paths skip release.

## Performance

Memory pressure can trigger garbage collection, paging, container eviction or OOM kills. Excessive allocation also increases CPU work and latency. Measure allocation rate, heap/GC behavior, RSS and external resource counts instead of guessing.

## Containers

A container is not a separate kernel. Processes in containers share the host kernel while namespaces and cgroups provide isolation and resource controls. Container memory/CPU limits therefore affect application behavior directly.

## Production checklist

- Set explicit resource limits and requests where appropriate.
- Track memory growth over time.
- Close files, sockets and database connections.
- Understand runtime GC behavior.
- Watch RSS, heap and native memory separately when possible.
- Avoid unbounded queues and caches.
- Test graceful shutdown and cancellation.
- Understand what happens when the process is killed abruptly.
