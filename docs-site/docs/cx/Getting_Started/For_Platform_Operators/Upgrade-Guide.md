---
title: "Upgrade Guide"
summary: "End-to-end guide for platform operators upgrading an existing ExpertFlow CX deployment — from pre-upgrade validation through the upgrade procedure and post-upgrade verification."
audience: [platform-operator]
doc-type: tutorial
last-updated: 2026-04-08
---

This document sequences an ExpertFlow CX upgrade on an already-running platform. It assumes you have a healthy deployment and are moving to a newer version.

For a fresh deployment from scratch, see [Installation Guide](Installation-Guide.md).

---

## Stage 1 — Pre-Upgrade Validation

Confirm your platform is in a healthy state before making any changes.

### Current platform health

- [ ] All pods running and ready — `kubectl get pods -A` shows no CrashLoopBackOff or Pending
- [ ] All Helm releases in `deployed` state — `helm list -A`
- [ ] No active alerts firing in your monitoring stack
- [ ] Sufficient free disk space for upgrade artefacts

### Compatibility and release notes

- [ ] Release notes reviewed for breaking changes and required upgrade order
- [ ] `kubectl` and Helm versions confirmed compatible with the target release
- [ ] Any dependent component versions (MongoDB, PostgreSQL) checked against the new version's requirements

### Backup

Take a verified backup before proceeding. If the upgrade fails and rollback is insufficient, this is your recovery point:

→ [Backup and Restore](../../How-to_Guides/Platform_Operator/Backup-and-Restore.md)

- [ ] Backup completed and integrity verified
- [ ] Backup stored in a location independent of the cluster

### Operational readiness

- [ ] Maintenance window agreed with tenants
- [ ] Rollback plan confirmed — conditions that trigger rollback and step-by-step procedure documented
- [ ] Support contact available for the duration of the maintenance window

---

## Stage 2 — Run the Upgrade

Follow the upgrade procedure in the order specified. Component upgrade order matters — dependencies must be upgraded before the services that rely on them.

→ [Upgrading the Platform](../../How-to_Guides/Platform_Operator/Upgrading-the-Platform.md)

If the release includes a MongoDB version bump:

→ [Upgrade to MongoDB Version 8.x](../../How-to_Guides/Platform_Operator/Upgrade-to-MongoDB-Version-8.x.md)

---

## Stage 3 — Post-Upgrade Verification

Confirm the upgraded platform is healthy before ending the maintenance window.

**Platform health**
- [ ] All pods running and ready — `kubectl get pods -A`
- [ ] All Helm releases show the new version — `helm list -A`
- [ ] No new ERROR or WARN patterns in logs introduced by the upgrade
- [ ] Ingress and TLS still valid

**Tenant and configuration integrity**
- [ ] All tenant configurations intact — spot-check queue routing and channel settings
- [ ] Agent Desk loads and admin login succeeds for each tenant

**Functional smoke test**
- [ ] Agent login → inbound interaction → queue routing → wrap-up completes successfully
- [ ] If voice is deployed: SIP registration and a test call succeed
- [ ] If MongoDB was upgraded: replica set status is healthy (`rs.status()`)

---

## What's next

If all checks pass, end the maintenance window and notify tenants.

For day-to-day platform operations:

→ [Platform Operator How-to Guides](../../How-to_Guides/Platform_Operator/index.md)
