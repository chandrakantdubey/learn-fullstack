# Systems Foundations

Understand the machine and network before relying on infrastructure abstractions.

## Core areas

- Linux fundamentals, shell/Bash and environment variables
- Processes, threads, signals and file descriptors
- Filesystems, permissions, users/groups and process lifecycle
- Services with systemd, scheduled work with cron
- SSH and remote administration concepts
- stdin/stdout/stderr, pipes and process composition
- CPU, memory, disk, virtual memory and resource limits
- TCP/IP, UDP, sockets and ports
- IPv4/IPv6, IP/subnets, CIDR, routing and NAT
- DNS and DHCP mental models
- TLS and how secure transport fits above networking
- HTTP/1.1, HTTP/2, HTTP/3 and QUIC concepts
- Reverse proxies, load balancers, CDNs and service-to-service networking
- WebSockets and SSE as application-level realtime transports
- Concurrency, parallelism, synchronization and cancellation
- Async I/O and event loops
- Backpressure, load shedding and graceful shutdown
- Profiling and performance analysis
- CPU/memory/disk/network troubleshooting

## Practical diagnostics

Know the role of tools such as:

`grep`, `sed`, `awk`, `find`, `xargs`, `curl`, `jq`, `ssh`, `scp`, `rsync`, `tar`, `ps`, `top`, `htop`, `lsof`, `ss`, `df`, `du`, `free`, `journalctl`, `dig`, `nslookup`, `ping`, `traceroute`, `nc`, `tcpdump`.

The goal is understanding what evidence each tool provides, not memorizing command flags.

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

## Fullstack boundary

Protocol and OS mental models live here. Deep Docker/Kubernetes mechanics live in `learn-docker`; application API behavior lives in `learn-backend`; cloud architecture lives in the infrastructure layer.

The objective is to diagnose from evidence rather than guess from the framework layer.
