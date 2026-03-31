---
title: "Supervisor Access to Unified Admin"
summary: "How-to guide for supervisors using Unified Admin — covering the four areas supervisors can access: Agent Channel Categories, Agent Attributes, Queues, and Teams, with scope and permission notes."
audience: [supervisor]
product-area: [channels, digital]
doc-type: how-to
difficulty: beginner
keywords: ["supervisor unified admin CX", "supervisor admin access CX", "agent channel categories supervisor", "agent attributes supervisor CX", "supervisor queue settings CX", "supervisor team management CX"]
aliases: ["supervisor admin CX", "supervisor unified admin access CX"]
last-updated: 2026-03-10
---

# Supervisor Access to Unified Admin

Supervisors can log in to Unified Admin to view and manage their team agents and skill sets. Supervisor access is scoped — you can only see and modify settings for the teams and agents you supervise.

## Accessible Areas

Supervisors have access to four areas in Unified Admin:

| Area | Path | Scope |
|---|---|---|
| **Agent Channel Categories** | Routing Engine → Agent Channel Categories | Your supervised teams only |
| **Agent Attributes** | Routing Engine → Agent Attributes | Your supervised teams only |
| **Queues** | Routing Engine → Queues | Queues assigned to your teams only |
| **Teams** | Teams | Teams you supervise; can create new teams |

---

## Change Agent Channel Categories

1. Expand the **Routing Engine** tab in the left navigation and go to **Agent Channel Categories**.
2. Select the desired team from the **Teams** dropdown (shows only your supervised teams).
3. Search by agent username to find the target agent.
4. Update the channel category (MRD) settings as needed.

---

## Change Agent Attributes

1. Expand **Routing Engine** and go to **Agent Attributes**.
2. Select the desired team from the **Teams** dropdown.
3. Search by agent username.
4. Update routing attribute values (proficiency levels, boolean flags) for the agent.

---

## Change Queue Settings

Supervisors can edit the settings of queues assigned to their teams. You **cannot** edit other supervisors' queues or create new queues.

1. Expand **Routing Engine** and go to **Queues**.
2. Select the desired team from the **Teams** dropdown.
3. Search by queue name to find the target queue.
4. Edit the queue configuration as needed.

---

## Manage Team Settings

Supervisors can modify their team definitions, add or remove agents, and create new teams.

1. Go to **Teams** in the left navigation.
2. The Teams list shows all teams you supervise.
3. Click **New Team** to create a new team (it will automatically be assigned to you).
4. Click an existing team to update its definition — add or remove agents and supervisors.

> Teams created by an admin are visible to you after logging out and back in to Unified Admin.

---

## Related Articles

- [Add Agents, Supervisors, and Teams](Add-Agents-Supervisors-and-Teams.md)
- [Managing Teams and Members](Managing-Teams-and-Members.md)
- [As a Supervisor](As-a-Supervisor.md)
- [Routing Attributes and Queues](../Solution_Admin/Routing-Attributes-and-Queues.md)
