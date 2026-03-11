---
title: "Synchronizing Cisco Users and Teams"
summary: "Guide for Integration Specialists to configure and troubleshoot the one-way sync from Cisco UCCE/X to ExpertFlow CX."
audience: [integrator, admin]
product-area: [cisco-integration, iam]
doc-type: how-to
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Synchronizing Cisco Users and Teams

The **Cisco Sync Service** provides a one-way synchronization from Cisco Contact Center environments into ExpertFlow CX. This ensures that your agents and teams are automatically mirrored in CX for quality monitoring, campaigns, and reporting.

## 1. How the Sync Works
- **Direction:** One-way (Cisco -> CX).
- **Scope:** Syncs both individual users (Agents/Supervisors) and Team structures.
- **Identity:** Users are synced into the **CX-IAM (Keycloak)** for authentication, while teams are mirrored directly in the CX Core.

## 2. Expected Behaviors
| Scenario | Behavior |
| :--- | :--- |
| **New User in Cisco** | Automatically created in CX during the next sync cycle. |
| **User Team Change** | Agent/Supervisor is removed from their old team and moved to the new one in CX. |
| **User Deletion** | The user is **disabled** in CX but not deleted. |
| **Team Deletion** | **Manual Action Required:** Team deletions in Cisco do not trigger deletions in CX. |
| **Multiple Supervisors** | One is designated as Primary in CX; others are set as Secondary. |

## 3. Conflict Prevention
- **Unique Naming:** Ensure you do not have manually created teams in CX with the same name as Cisco teams. This will trigger a `409 Conflict` error during the sync.
- **Role Sync:** For agents to appear in the Keycloak groups after sync, they must perform a **one-time login** to Cisco Finesse.

## 4. Deployment & Monitoring
The sync service is managed via the **EF Data Platform** pipelines. 
- **Validation:** Check the sync logs in the Data Platform UI to verify that all records were processed without errors.

---

*For technical troubleshooting of the sync pipeline, see the [EF Data Platform Deployment Guide](https://expertflow-docs.atlassian.net/wiki/spaces/EF/pages/772243470/EF+Data+Platform+Deployment).*
