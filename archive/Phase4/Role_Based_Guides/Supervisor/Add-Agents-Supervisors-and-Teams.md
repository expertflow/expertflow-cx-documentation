---
title: "Add Agents, Supervisors, and Teams"
summary: "How-to reference for team structure in ExpertFlow CX — explaining Agent Teams, primary vs. secondary supervisors, team membership rules, queue associations, and team information syncing behavior with Cisco."
audience: [supervisor, solution-admin]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["add agents CX", "add supervisors CX", "create team CX", "agent team CX", "primary supervisor CX", "secondary supervisor CX", "team management CX", "team structure CX"]
aliases: ["team management CX", "create agent team CX", "add team members CX"]
last-updated: 2026-03-10
---

# Add Agents, Supervisors, and Teams

An **Agent Team** in ExpertFlow CX consists of agents managed by one primary supervisor and optionally multiple secondary supervisors. Teams are configured in Unified Admin.

## Team Structure

- A team is supervised by **one primary** and optionally **one or more secondary** supervisors.
- Primary and secondary supervisors must have the **Supervisor** role in Keycloak/IAM.
- **Primary supervisors** oversee the entire team.
- **Secondary supervisors** manage only their specifically assigned agents within the team, with an optional filter to view other agents.
- Primary and secondary supervisors have identical feature access and capabilities.

## Key Rules

| Rule | Details |
|---|---|
| **One team per agent** | An agent can belong to only one team. To move an agent, remove them from the current team first. |
| **Supervisor can also be an agent** | A supervisor can be an agent in the same or a different team. |
| **Cross-team supervisor roles** | A user can be a primary supervisor for one team and a secondary supervisor in another — but not both roles in the same team. |
| **Queue association** | Queues are automatically associated with teams based on the agents assigned to them — no manual queue-to-team mapping is needed. |
| **All users need a team** | All contact center users must belong to a team to log in to Agent Desk. |
| **Team creation permissions** | Supervisors can create new teams and delete only the teams they personally created. |
| **Admin-created teams** | After an admin creates a team, supervisors see the changes after logging out and back into Unified Admin. |
| **Keycloak deletion** | Remove users from CX Teams before deleting them from Keycloak. Deleted Keycloak users still appear in Team creation until users re-login. |

## Configuring Teams in Unified Admin

Team configuration — creating teams, adding agents, assigning supervisors, and managing routing attributes — is performed in **Unified Admin**. Contact your Unified Admin guide for step-by-step configuration instructions.

## Team Information Syncing (Cisco Environments)

| Direction | Behavior | Details |
|---|---|---|
| **EFCX → Cisco** | No automatic sync | Team changes in EFCX do not automatically sync to Cisco. |
| **Cisco → EFCX** | One-way sync enabled | Changes in Cisco team attributes are reflected in EFCX. |
| **Agent/Supervisor add or remove** | Updates on Finesse login | Adding or removing agents/supervisors in Cisco is reflected in EFCX teams when the user next logs into Finesse. |

## Related Articles

- [As a Supervisor](As-a-Supervisor.md)
- [Managing Teams and Members](Managing-Teams-and-Members.md)
- [Impact of Team Structure on Dashboards](Impact-of-Team-Structure-on-Dashboards.md)
- [Synchronizing Cisco Users and Teams](../Integrator/Synchronizing-Cisco-Users-and-Teams.md)
