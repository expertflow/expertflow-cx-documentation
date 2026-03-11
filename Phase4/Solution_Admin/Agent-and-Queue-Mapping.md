---
title: "Agent and Queue Mapping"
summary: "Explanation of the logical mapping between agents, attributes, and precision queues in the routing engine."
audience: [admin, supervisor]
product-area: [routing, platform]
doc-type: explanation
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Agent and Queue Mapping

ExpertFlow CX uses a skills-based routing model that connects customer requests with the most qualified available agent. This mapping is achieved through a hierarchy of **Attributes, Steps, and Queues.**

## 1. The Core Abstractions
- **Agents:** The actual users (e.g., Amy) who answer requests via the Agent Desk. 
- **Routing Attributes:** The "Skills" assigned to agents (e.g., "English", "Sales", "Advanced Troubleshooting").
- **Precision Queues:** The logical groups that customer requests enter to wait for an agent.

## 2. How the Mapping Works
Instead of manually adding agents to a queue, you map them dynamically using **Steps.**

### The Step Evaluation Logic:
1.  **Incoming Request:** A customer request enters a queue (e.g., "Support-English").
2.  **Step Evaluation:** The routing engine looks at the first **Step** in the queue's logic (e.g., `English == 10`).
3.  **Attribute Matching:** The engine searches for all available agents who possess the required attribute at the specified proficiency level.
4.  **Assignment:** The task is pushed to the agent matching the criteria.

## 3. Dynamic Rerouting (The Overflow Model)
If no agent matches the criteria in the first step, the queue logic can include a **Timeout.**
- **Overflow:** After the timeout (e.g., 30s), the engine evaluates the next step in the queue, which may have relaxed criteria (e.g., `English >= 7`). 
- **Goal:** This ensuring that even if the "ideal" agent is busy, the customer eventually reaches someone qualified to help.

### Operational Syncing
- **Identity Sync:** Agents are synced from **Keycloak** or an **Active Directory.**
- **Attribute Assignment:** Solution Admins (Olivia) assign the specific routing attributes in the Unified Admin. 
- **Supervisor Role:** Supervisors (Sam) can monitor this mapping in real-time to ensure that no queue is left with zero qualified agents available.

---

*Ready to configure your first queue? Follow the [Routing Attributes and Precision Queues](Routing-Attributes-and-Queues.md) guide.*
