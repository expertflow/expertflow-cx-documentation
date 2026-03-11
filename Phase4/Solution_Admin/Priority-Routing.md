---
title: "Priority Routing"
summary: "Explanation of Priority Routing in ExpertFlow CX — how customer labels are used to assign routing priorities, bypass queue wait time, and ensure high-value customers are served first."
audience: [solution-admin, supervisor]
product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["priority routing CX", "customer label priority", "routing priority CX", "queue priority bypass", "VIP customer routing", "customer label routing", "priority queue CX", "highest priority routing"]
aliases: ["priority routing CX", "label-based routing", "priority queue bypass CX"]
last-updated: 2026-03-10
---

# Priority Routing

Priority Routing enables administrators and supervisors to route customer requests ahead of the standard queue, ensuring high-value or urgent customers are served first without waiting. Priority is determined by **Customer Labels** — labels applied to customers in Agent Desk that carry a numeric priority value.

## How Priority Routing Works

When a conversation enters the system:

1. The system checks whether the customer has any labels assigned.
2. If labels are present, the label's priority value is applied to the routing request.
3. The Routing Engine places the request in the queue at the appropriate priority level, bypassing lower-priority requests.
4. If the customer has **no label**, the system applies the default priority of **1**.

## Setting Up Priority Routing

### Step 1: Configure Customer Labels with Priorities

In Agent Desk (Supervisor view):

1. Navigate to **Customer Labels**.
2. Create labels and assign a numeric priority to each.

Example label configuration:

| Label | Priority |
|---|---|
| Premium | 10 |
| Gold | 8 |
| Standard | 6 |

Higher numbers = higher routing priority.

### Step 2: Assign Labels to Customers

Agents assign labels to customers from the Agent Desk customer profile. One or more labels can be assigned to a single customer at any time.

## Priority Resolution for Multiple Labels

If a customer has multiple labels assigned, the system uses the **highest priority** label for routing.

**Example:** A customer with both `Premium` (priority 10) and `Standard` (priority 6) labels is routed as a Premium customer at priority 10.

## Default Priority

Customers with no labels assigned receive the system default priority of **1** — the lowest — and follow standard queue order.

## Related Articles

- [Customer Labels](../Functional_Areas/Digital_Channel_Management/Customer-Labels.md)
- [Precision Routing](Precision-Routing.md)
- [Pull-Mode Routing](Pull-Mode-Routing.md)
- [Routing Attributes and Queues](Routing-Attributes-and-Queues.md)
