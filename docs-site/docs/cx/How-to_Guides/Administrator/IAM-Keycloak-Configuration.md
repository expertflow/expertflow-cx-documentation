---
audience: [administrator]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# IAM (Keycloak) Configuration Guide

This document covers the setup and import of pre-configured realms in Keycloak for Expertflow CX.

## 1. Download Realm Files
Select the correct realm-export file based on your release version:
- **CX-4.10.1**: Includes API Authorization and standard permissions.
- **CX-4.7 to 4.10**: Does not contain Campaign/Survey permissions (must be imported separately).
- **CX-4.5.2 and earlier**: Standard legacy realm exports.

## 2. Import Process
1. Log in to the Keycloak Administration console (`https://<server-fqdn>/auth`).
2. Default credentials: `admin` / `admin` (or as set in environment variables).
3. Hover over the **Master** realm in the left sidebar and click **Add realm**.
4. Click **Select file**, choose your downloaded `.json` file, and click **Create**.

## 3. User Configuration
Once the realm is imported, create your system users (Agent, Supervisor, Admin).

### Setting Passwords
1. Go to **Users** -> Select User -> **Credentials** tab.
2. Click **Set Password**, enter the password, and toggle **Temporary** to **Off**.

### Role Mappings
Assign the following roles to ensure proper access:
- **Agent**: Assign `agent`, `offline_access`, and `uma_authorization`.
- **Supervisor**: Assign `supervisor`, `offline_access`, and `uma_authorization`.
- **Admin**: Assign `admin`, `offline_access`, `uma_authorization`, and all **realm-management** client roles.

## 4. Team Assignment
- **Mandatory**: All users with `agent` or `supervisor` roles **must** be assigned to a team via the Unified Admin.
- **Optional**: Administrative roles (Admin, Routing Manager) do not require team assignment.

**Note:** A user should only have one primary CX role (Agent, Supervisor, or Admin) assigned to them.
