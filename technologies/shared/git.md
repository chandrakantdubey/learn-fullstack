# Git

**Role:** Primary | **Layer:** Shared

## Mental model
Git is a content-addressed version-control system. Commits form a directed history of snapshots; branches and tags are references to commits.

## Core areas
- working tree, index and commits
- branches, remotes and tracking
- merge, rebase and cherry-pick
- conflict resolution
- tags and releases
- reflog and recovery
- hooks and signing
- bisect and history inspection

## Production workflow
Keep commits coherent, write useful messages, protect main, review changes, and make history understandable. Rebase local work when appropriate; do not rewrite shared history casually.

## Recovery
Know `reflog`, `restore`, `reset`, `revert`, `cherry-pick` and how to inspect object history before destructive operations.

## Related
GitHub, GitHub Actions, CI/CD, release engineering.
