---
title: "User Management"
summary: "How-to guide for creating and configuring users in ExpertFlow CX via Keycloak — covering user creation, credential setup, group assignment, and role mapping for agents, supervisors, evaluators, and administrators."
audience: [administrator]
product-area: [channels, digital]
doc-type: how-to
difficulty: beginner
keywords: ["user management CX", "keycloak user creation", "create agent CX", "add user CX", "keycloak roles CX", "agent permissions keycloak", "supervisor user setup CX", "CX user administration"]
aliases: ["add user CX", "create user keycloak CX", "manage users CX"]
last-updated: 2026-03-10
---

# User Management

User accounts in ExpertFlow CX are managed through **Keycloak** (the IAM service). This guide explains how to create a new user, set credentials, assign groups, and map roles.

## Prerequisites

- Administrator access to the Keycloak Admin Console for the target realm
- Knowledge of the correct realm name
- Defined role model and group structure in place

## Core Concepts

| Concept | Description |
|---|---|
| **Realm** | Tenant or security boundary containing users, roles, clients, and groups. |
| **User** | An individual identity with credentials, roles, and group membership. |
| **Role** | A permissions bundle (realm-level or client-level) that grants capabilities in apps. |
| **Group / Team** | A collection of users; carries role mappings for easier bulk management. |

---

## Step 1: Create a New User

1. Sign in to the **Keycloak Admin Console**.
2. Select the correct **Realm** from the top-left dropdown.
3. Navigate to **Users → Add user**.
4. Fill in the user details:
   - **Username**
   - **First Name**
   - **Last Name**
5. Click **Join Groups** in the Groups field and assign the appropriate group:
   - **Agents**: assign to `agents_permission` group
   - **Senior Agents and Supervisors**: assign to `senior_agents_permission` group
6. Click **Create**.

---

## Step 2: Set Initial Credentials

1. Open the newly created user and click the **Credentials** tab.
2. Click **Set password**.
3. Enter a strong password.
4. Set **Temporary** to **On** so the user is required to change their password at first login.
5. Click **Save**.

---

## Step 3: Assign Roles

1. Go to the **Role mapping** tab for the user.
2. Click **Assign role**.
3. Select the appropriate role(s) from the list.

> Avoid assigning conflicting roles to a single user (e.g., do not combine `admin` and `agent`). Keep `uma_authorization` and `offline_access` as required by your application.

## Role Reference by Persona

| Persona | Realm Roles | Group |
|---|---|---|
| **Administrator** | `admin`, `offline_access`, `uma_authorization` | — |
| **Agent** | `agent`, `offline_access`, `uma_authorization` | `agents_permission` |
| **Supervisor / Evaluator** | `supervisor` or `evaluator`, `offline_access`, `uma_authorization` | `senior_agents_permission` |

---

## Related Articles

- [IAM Keycloak Configuration](IAM-Keycloak-Configuration.md)
- [Migrate EF IAM Users](Migrate-EF-IAM-Users.md)
- [Migrate Keycloak Groups to CX Teams](Migrate-Keycloak-Groups-to-CX-Teams.md)
- [Agent and Queue Mapping](Agent-and-Queue-Mapping.md)
