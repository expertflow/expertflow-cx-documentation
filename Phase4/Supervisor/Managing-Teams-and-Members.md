---
title: "Managing Teams and Members"
summary: "How-to guide for supervisors to manage team assignments, supervisor roles, and agent skill grouping."
audience: [supervisor]
product-area: [admin, team-management]
doc-type: how-to
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Managing Teams and Members

As a Supervisor (Sam), you manage your team's structure in the **Unified Admin** console. An **AgentTeam** consists of a primary supervisor, optional secondary supervisors, and the agents they manage.

## 1. The Team Hierarchy
ExpertFlow CX uses a clear structure for team leadership.
- **Primary Supervisor:** The main leader responsible for the entire team.
- **Secondary Supervisor:** Can manage specific assigned agents or optionally monitor all agents.
- **Agents:** Individual contributors assigned to the team. 

### Rules for Sam:
1. **One Team per Agent:** Every agent must belong to exactly one team to log into the Agent Desk.
2. **Dual Roles:** You can be a supervisor for one team while being an agent in another.
3. **Queue Assignment:** Your agents' queues are automatically associated with your team—you can monitor these queues as long as you have the supervisor role.

## 2. Managing Team Assignments
All team management is performed under the **Teams** tab in Unified Admin.

### To Create or Update a Team:
1.  **Define Roles:** Select the **Primary** and **Secondary** supervisors from the list of users synced from Keycloak.
2.  **Add Agents:** Select the agents you want to include in the team.
3.  **Syncing:** Changes made in Unified Admin are visible to agents after their next login. 

## 3. Important Notes for Supervisors
- **System Syncing:** While you can update team info in ExpertFlow CX, these changes do not sync back to Cisco (UCCE/X) automatically. 
- **User Removal:** Always remove an agent from their ExpertFlow team before deleting their account in Keycloak. 
- **Rerouting:** If you need to change an agent's team, you must first remove them from their current team.

---

*Ready to start monitoring? Check the [Monitoring Your Team in Real-Time](../Getting_Started/Monitoring-Your-Team-in-Real-Time.md) guide.*
