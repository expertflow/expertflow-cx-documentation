---
title: "Backup and Restore"
summary: "How-to guide for platform operators — covers backup scope, backup commands for each data store, restore procedures, and backup verification."
audience: [administrator, hosting-partner, platform-operator]
doc-type: how-to
difficulty: intermediate
keywords: [backup, restore, data recovery]
aliases: []
last-updated: 2026-03-24
status: placeholder
---

# Backup and Restore

> **Placeholder** — This document needs to be written. See the outline below for intended content.

This guide covers the backup and restore procedures for all stateful components in an ExpertFlow CX deployment.

## What Needs to Be Backed Up

| Component | Data at risk | Backup method |
| --- | --- | --- |
| MongoDB | Conversations, tenant config, user data | mongodump / Atlas backup |
| Redis | Session state, queues (if persistent) | RDB snapshot |
| PostgreSQL | Vault secrets, reporting data | pg_dump |
| Kubernetes config | Helm values, secrets, ingress rules | etcd snapshot / Velero |
| Media files | Recordings, attachments | Object storage backup |

## Backup Procedures

### MongoDB

```bash
# Example — fill in actual connection string and target path
mongodump --uri="<connection-string>" --out=/backups/mongo/$(date +%Y%m%d)
```

- Frequency recommendation
- Retention policy

### Redis

- When Redis persistence matters (AOF vs RDB)
- How to trigger a manual RDB snapshot

### PostgreSQL

```bash
pg_dump -h <host> -U <user> <database> > /backups/pg/$(date +%Y%m%d).sql
```

### Kubernetes / etcd

- RKE2 etcd snapshot commands
- Storing snapshots off-node

## Restore Procedures

### Restoring MongoDB

```bash
mongorestore --uri="<connection-string>" /backups/mongo/<date>
```

- Expected restore time for typical dataset sizes
- How to verify data integrity after restore

### Restoring PostgreSQL

```bash
psql -h <host> -U <user> <database> < /backups/pg/<date>.sql
```

### Restoring Kubernetes State

- etcd restore sequence
- Re-applying Helm releases after cluster restore

## Backup Verification

- How to test a backup without taking down production
- Verification checklist after any restore

## Disaster Recovery Checklist

- [ ] MongoDB backup verified
- [ ] PostgreSQL backup verified
- [ ] etcd snapshot taken and stored off-node
- [ ] Restore procedure tested in staging in the last 90 days
