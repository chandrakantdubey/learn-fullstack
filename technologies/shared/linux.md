# Linux

**Role:** Primary | **Layer:** Shared/runtime

## Mental model
Linux exposes processes, files, sockets, users, permissions, namespaces, cgroups and system calls as the foundation beneath most cloud workloads.

## Core areas
- filesystem and permissions
- processes, signals and job control
- stdout/stderr and pipes
- networking and sockets
- environment variables and service configuration
- systemd and logs
- namespaces and cgroups
- resource inspection with `ps`, `top`, `ss`, `lsof`, `df`, `du`, `free` and `strace`

## Production patterns
Run least privilege, bound CPU/memory, make signals and shutdown behavior correct, inspect file descriptors and sockets, and understand the OS before debugging containers or Kubernetes.

## Related
Docker, Kubernetes, networking, observability, security.
