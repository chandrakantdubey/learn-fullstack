# Disaster Recovery and Business Continuity

Disaster recovery is the engineering plan for restoring service and data after failures larger than a normal request or process failure.

## Core terms

- **RPO:** maximum acceptable data loss measured in time.
- **RTO:** maximum acceptable restoration time.
- **Backup:** a recoverable copy of data.
- **Restore:** proving that a backup can actually produce usable state.
- **Failover:** moving service to an alternate capacity or location.

## Recovery model

```text
failure
  ↓
detect + declare incident
  ↓
protect remaining data
  ↓
restore infrastructure/data
  ↓
validate integrity
  ↓
restore traffic gradually
  ↓
observe + reconcile
  ↓
post-incident review
```

## Production requirements

- Define RPO/RTO per critical capability, not one number for the whole product.
- Back up databases and important object data.
- Encrypt backups and control access to them.
- Test restores regularly; an untested backup is an assumption.
- Document dependencies required during recovery.
- Define degraded-mode behavior when optional dependencies are unavailable.
- Keep recovery procedures versioned and executable.
- Consider multi-AZ or multi-region only when the availability requirement justifies the cost and complexity.

## Fullstack responsibility

Database repositories own backup primitives; cloud/container repositories own infrastructure mechanics. `learn-fullstack` owns the business recovery requirement, dependency graph, recovery sequence and trade-off reasoning.

## Related concepts

- SLOs and error budgets
- capacity planning
- deployment and rollback
- data consistency
- observability
- incident response
