# Alembic

**Role:** Primary | **Layer:** Database migrations

## Mental model
Alembic records versioned schema transformations so application code and database schema evolve together.

## Learn
- migration revisions
- upgrade/downgrade
- autogeneration and review
- branching/merging migration histories
- data migrations vs schema migrations
- transactional DDL behavior

## Production
Review generated migrations manually, make destructive changes staged, backfill large datasets asynchronously, and ensure deploy/rollback sequencing is compatible with running application versions.

## Related
SQLAlchemy, PostgreSQL, deployment engineering.
