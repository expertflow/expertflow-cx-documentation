---
title: "Upgrading the Platform"
summary: "Step-by-step guide for platform operators on upgrading an ExpertFlow CX deployment — covers pre-upgrade checks, component upgrade order, rollback procedure, and post-upgrade validation."
audience: [administrator, hosting-partner, platform-operator]
doc-type: how-to
difficulty: advanced
keywords: [upgrade, platform upgrade, migration]
aliases: []
last-updated: 2026-03-24
status: placeholder
---

# Upgrading the Platform

> **Placeholder** — This document needs to be written. See the outline below for intended content.

This guide covers the full upgrade lifecycle for a production ExpertFlow CX deployment.

## Prerequisites

- [ ] Backup completed and verified (see [Backup and Restore](Backup-and-Restore.md))
- [ ] Maintenance window agreed with tenants
- [ ] New version release notes reviewed
- [ ] Rollback plan confirmed

## Pre-Upgrade Checklist

- [ ] Current cluster health is green (all pods running, no alerts firing)
- [ ] Sufficient free disk space for upgrade artefacts
- [ ] `kubectl` and Helm versions compatible with target release

## Component Upgrade Order

Upgrades must follow a specific order to avoid breaking dependencies:

1. Infrastructure layer (RKE2, cert-manager, ingress)
2. Data layer (MongoDB, Redis, PostgreSQL)
3. Core CX services (CX Router, IAM)
4. Channel connectors
5. Media Server (if applicable)
6. Frontend / Agent Desk

_Detail each step — commands, expected output, how to confirm success._

## Upgrading MongoDB

_Cross-reference: [Upgrade to MongoDB Version 8.x](../Hosting_Partner/Upgrade-to-MongoDB-Version-8.x.md)_

## Upgrading PostgreSQL and Vault

_Cross-reference: [Upgrade Guide: Postgres + Vault + Cisco](../Developer_Integrator/Upgrade-Guide-Postgres-Vault-Cisco.md)_

## Post-Upgrade Validation

- Smoke test checklist (agent login, inbound call/chat, queue routing)
- Log check for ERROR/WARN patterns introduced by the upgrade
- Confirm all tenant configurations still intact

## Rollback Procedure

- Conditions that trigger a rollback decision
- Step-by-step rollback commands
- How to restore from backup if rollback is insufficient
