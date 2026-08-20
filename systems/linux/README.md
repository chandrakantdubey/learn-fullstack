# Linux for Fullstack Engineers

Linux is the execution environment behind a large share of production software. A Fullstack Engineer should be able to inspect a running system, understand process and filesystem behavior, diagnose basic failures, and operate services without treating the OS as magic.

## Mental model

```text
Hardware
  -> Kernel
  -> Processes
  -> Filesystems / sockets / devices
  -> Services
  -> Applications
```

The shell is an interface to these primitives.

## Processes

Understand:

- Process vs thread
- PID and parent/child relationships
- Process lifecycle
- Signals
- Exit codes
- Foreground/background execution
- Environment variables
- File descriptors
- stdin/stdout/stderr

Useful commands:

```bash
ps aux
pstree
pgrep
kill
kill -TERM <pid>
kill -KILL <pid>
top
htop
```

## Filesystem

Know the purpose of:

```text
/
├── etc
├── var
├── home
├── tmp
├── usr
├── opt
├── proc
├── sys
└── dev
```

Understand:

- Paths
- Permissions
- Ownership
- Symbolic links
- Mounts
- Disk usage
- Inodes
- Temporary files

Useful commands:

```bash
ls -la
find
stat
df -h
du -sh
mount
ln -s
```

## Permissions and security

Understand:

- User/group ownership
- Read/write/execute permissions
- `chmod`
- `chown`
- `umask`
- Least privilege
- SSH keys
- `sudo`

Never solve an application problem by making everything world-writable.

## Services and logs

Understand the relationship between a long-running application and the service manager.

With systemd, know:

```bash
systemctl status my-service
systemctl restart my-service
systemctl enable my-service
journalctl -u my-service
```

The debugging loop is:

```text
Is the process running?
  -> Is it listening?
  -> Can I reach it locally?
  -> What do the logs say?
  -> What dependencies are failing?
  -> What resource is exhausted?
```

## Networking from Linux

Useful commands:

```bash
ss -lntp
curl -v https://example.com
dig example.com
nc -vz host 443
ip addr
ip route
traceroute example.com
```

Understand:

- Interface
- IP address
- Routing table
- Listening socket
- TCP connection
- DNS resolution
- TLS termination

## Shell fundamentals

A Fullstack Engineer should be comfortable composing commands:

```bash
grep
sed
awk
cut
sort
uniq
xargs
jq
tee
head
tail
less
```

The important skill is turning many small tools into a reliable debugging or automation pipeline.

## Resource debugging

When a service is slow or failing, check:

### CPU

```bash
top
htop
pidstat
```

### Memory

```bash
free -h
vmstat
```

### Disk

```bash
df -h
du -sh /var/*
```

### Network

```bash
ss -s
ss -lntp
```

### Open files

```bash
lsof -p <pid>
```

## Production connection

Linux knowledge directly supports:

```text
Application
   ↓
Process
   ↓
Container
   ↓
Node / VM
   ↓
Cloud infrastructure
```

Docker abstracts some Linux primitives; Kubernetes orchestrates them. Neither removes the need to understand the underlying OS.

## Minimum standard

You should be able to:

- SSH into a Linux machine
- Find a process
- Inspect CPU and memory usage
- Find where logs are going
- Test a local and remote port
- Diagnose DNS resolution
- Inspect filesystem usage
- Fix a permission problem safely
- Restart a service
- Identify whether a failure is application, OS, network, or dependency related
