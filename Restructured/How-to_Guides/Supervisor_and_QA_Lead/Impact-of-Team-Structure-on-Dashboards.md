---
title: "Impact of Team Structure on Dashboards"
summary: "Explanation of how primary and secondary supervisor roles affect the default views and filter options available on the Available Agents Detail and Active Conversation Detail dashboards in ExpertFlow CX."
audience: [supervisor-qa]
product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["team structure dashboard CX", "primary supervisor dashboard CX", "secondary supervisor dashboard CX", "agent visibility dashboard CX", "supervisor dashboard filter CX", "team impact dashboard CX"]
aliases: ["team structure dashboard CX", "supervisor team dashboard view CX"]
last-updated: 2026-03-10
---

# Impact of Team Structure on Dashboards

The supervisor's role within a team (primary or secondary) directly controls which agents and conversations are visible by default on the real-time dashboards. Both dashboards support filters to expand visibility when needed.

## Available Agents Detail Dashboard

| Supervisor Type | Default View | Filter Options |
|---|---|---|
| **Primary Supervisor** | All agents within their team. | Filter by secondary supervisor or select "All Agents". |
| **Secondary Supervisor** | Only the agents assigned to them within the team. | Filter by other secondary supervisors to view their agents; select "All Agents" to see the full team. |

**Filter behavior:**
- Selecting a **team + specific secondary supervisor**: shows only agents assigned to that supervisor.
- Selecting a **team + All Supervisors**: shows all agents and supervisors in the team.

## Active Conversation Detail Dashboard (Ongoing Conversations)

| Supervisor Type | Default View | Filter Options |
|---|---|---|
| **Primary Supervisor** | All agents and their active conversations within the team. | Filter by secondary supervisor or select "All Agents". |
| **Secondary Supervisor** | Only active conversations for their assigned agents. | Filter by other secondary supervisors; select "All Agents" to see the full team. |

**Filter behavior:**
- Selecting a **team + specific secondary supervisor**: shows only conversations from agents assigned to that supervisor.
- Selecting a **team + All Supervisors**: shows all agent conversations in the team.

## Key Takeaway

Both the **Available Agents Detail** and **Ongoing Conversations Detail** dashboards apply the same primary/secondary supervisor scoping logic. Supervisors always have access to expand their view to the full team via the "All Agents" filter, regardless of their primary or secondary role.

## Related Articles

- [Realtime Detailed Dashboards](Realtime-Detailed-Dashboards.md)
- [Add Agents, Supervisors, and Teams](Add-Agents-Supervisors-and-Teams.md)
- [Managing Teams and Members](Managing-Teams-and-Members.md)
- [As a Supervisor](As-a-Supervisor.md)
