---
title: "Precision Routing"
summary: "Explanation of Precision Routing (Push-based) in ExpertFlow CX — how the Routing Engine matches incoming customer requests to the most suitable agent using queue steps, routing attributes, and agent selection criteria."
audience: [administrator]
product-area: [channels, digital]
doc-type: explanation
difficulty: intermediate
keywords: ["precision routing CX", "push routing CX", "routing engine CX", "queue steps routing", "routing attributes CX", "agent selection criteria", "push mode routing", "skills-based routing CX"]
aliases: ["push-based routing CX", "precision routing CX", "skills routing CX"]
last-updated: 2026-03-10
---

# Precision Routing

Precision Routing is the **push-based** routing mode in ExpertFlow CX. When a new customer request arrives on a channel, the Routing Engine automatically assigns the request to the most suitable available agent based on criteria defined in the queue's **Steps** configuration. The agent has no option to accept or decline — the request is pushed directly to them.

## How It Works

1. A customer message arrives on a channel (e.g., WhatsApp).
2. The system creates a new conversation and enqueues the request in the channel's associated queue.
3. The Routing Engine evaluates active agents against the queue's routing logic (Steps).
4. The engine selects the best-matching agent who is in **Ready** or **Active** state with the fewest active tasks.
5. The request is assigned to the agent, and their MRD state transitions from `READY` to `ACTIVE`.
6. When the conversation ends, the agent's state returns to `READY`.

## Configuration Components

### Media Routing Domain (MRD)

Groups agents by channel category (Chat, Email, Voice, etc.). The MRD controls which agents can receive which types of requests.

### Channel Type and Channel

Each channel is linked to an MRD and an associated default queue. All incoming requests on that channel are routed to that queue.

### Routing Attributes

Skill-like attributes assigned to agents. Used in queue steps to filter eligible agents.

| Attribute Type | Example | Usage |
|---|---|---|
| **Boolean** | `English`, `Los Angeles` | Agent must match: `English == true` |
| **Proficiency** | `Broadband` | Agent must meet threshold: `Broadband >= 7` |

### Queue Steps

Queue steps define the routing criteria. Example:

```
(English == true) AND (Los Angeles == true) AND (Broadband >= 7)
```

The Routing Engine evaluates agents in sequence through the queue steps until a matching agent is found.

## Example Use Case

**Scenario:** Customers calling about broadband issues from Los Angeles need to be routed to agents fluent in English with broadband technical skills.

**Admin configuration:**
1. Create an MRD for Chat.
2. Create a WhatsApp Channel Type linked to the MRD.
3. Create Queue `Q1` for broadband inquiries, linked to the MRD.
4. Create routing attributes: `English` (Boolean), `Los Angeles` (Boolean), `Broadband` (Proficiency).
5. Define queue step criteria: `(English == true) AND (Los Angeles == true) AND (Broadband >= 7)`.
6. Create Channel `C1` (WhatsApp), set Routing Mode to **Push**, and assign `Q1` as the default queue.

**At runtime:**
- Customer John from Los Angeles sends a WhatsApp message to channel `C1`.
- The request is enqueued in `Q1`.
- The Routing Engine finds agent Susanne who meets all criteria and is `Longest Available`.
- Susanne receives the request and accepts it.
- Susanne's state changes from `READY` to `ACTIVE`.

## Related Articles

- [Routing Attributes and Queues](Routing-Attributes-and-Queues.md)
- [Pull-Mode Routing](Routing-Strategy-Pull-Mode.md)
- [Priority Routing](Priority-Routing.md)
- [Media Routing Domains (MRD) Overview](Media-Routing-Domains-MRD-Overview.md)
