---
title: "Routing Strategy: Pull Mode"
summary: "Explanation of the Pull-Mode Routing strategy — a channel-agnostic concept where interactions are parked on a List for agents to self-select and join at their convenience."
audience: [administrator]
product-area: [routing, channels]
doc-type: explanation
difficulty: intermediate
last-updated: 2026-03-11
---

# Routing Strategy: Pull Mode

Pull Mode is a **channel-agnostic routing concept** in ExpertFlow CX. Unlike traditional "Push" routing, where the system automatically assigns tasks to specific agents, Pull Mode parks incoming interactions on a shared **List**. This allows agents to self-select which interactions to handle and when to join them.

## 1. Core Philosophy: The Broadcast Model
In Pull Mode, the system treats interaction requests as a broadcast. When a customer interaction arrives via a channel configured for Pull Mode, it is immediately published to an associated List rather than being offered to a single agent's desk.

### Key Benefits:
*   **Flexibility:** Agents can manage their own workload based on complexity or subject matter expertise.
*   **Collaboration:** Multiple agents can join the same interaction simultaneously, which is ideal for social media community management.
*   **Asynchronous Handling:** Perfect for channels where immediate response is not required (e.g., non-SLA social media comments).

---

## 2. Technical Concepts

### The "List"
A **List** acts as a virtual parking lot for interactions. Every channel in Pull Mode must be mapped to at least one List.

### Interaction States on a List:
| State | Description |
| :--- | :--- |
| **UNREAD** | The interaction is new and no agent has joined yet. |
| **ACTIVE** | One or more agents are currently participating in the interaction. |
| **INACTIVE** | Agents have participated but left without closing the interaction. It remains on the List for future follow-up. |
| **CLOSED** | The interaction is finalized and removed from the List. |

---

## 3. Configuration & Mapping
Pull Mode is configured at the **Channel** level within the Unified Admin. 

1.  **Define the List:** Create a target List in the Pull Mode configuration section.
2.  **Assign the Channel:** When creating or editing a channel (e.g., Twitter, Email, or SMS), set the **Routing Mode** to `PULL`.
3.  **Map to List:** Select the previously created List as the destination for all incoming traffic from that channel.

---

## 4. Channel-Agnostic Application
While frequently used for social media, Pull Mode can be applied to any digital channel:
*   **Twitter:** Monitor public mentions and choose which ones to engage with.
*   **Email:** Handle shared mailboxes where multiple agents pick from a common pool.
*   **SMS:** Manage high-volume marketing replies.

---

## Related Guides

*   [Twitter Channel Overview](../../Capabilities/Digital_Channels/Twitter/index.md)
*   [Email Channel Overview](../../Capabilities/Digital_Channels/Email/index.md)
*   [Twilio SMS/MMS Configuration](Twilio-SMS-MMS-Configuration-Guide.md)
*   [Precision Routing (Push Mode)](Precision-Routing.md)
