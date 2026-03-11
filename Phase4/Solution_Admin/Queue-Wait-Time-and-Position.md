---
title: "Queue Wait Time and Position"
summary: "Reference for the Queue Wait Time and Position feature in ExpertFlow CX — how the API notifies customers of their estimated wait time and queue position while waiting for an agent, and current availability status."
audience: [solution-admin, developer]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["queue wait time CX", "queue position CX", "estimated wait time CX", "customer queue notification", "queue position API CX", "wait time API CX", "customer waiting CX", "queue EWT"]
aliases: ["queue wait time CX", "EWT queue CX", "queue position notification CX"]
last-updated: 2026-03-10
---

# Queue Wait Time and Position

The Queue Wait Time and Position feature allows customers to see their **estimated wait time (EWT)** and **position in the queue** while waiting for an agent. The system notifies the customer periodically with updated values as their position changes.

## How It Works

When a customer is waiting in a queue:

1. The customer receives an initial notification showing their estimated wait time and queue position.
2. After a configurable interval (in seconds or minutes), the system sends updated notifications with the current position and recalculated estimated wait time.
3. Updates continue until the customer is connected to an agent or leaves the queue.

## Current Availability

| Component | Status |
|---|---|
| **API** | Available — see the Queue Wait Time and Position API reference in the ExpertFlow API documentation. |
| **Customer Web Widget** | Not yet embedded — planned for a future release. |

## Use Cases

- Reduce customer drop-off by showing transparent wait information.
- Allow customers to make an informed decision to stay in queue or call back later.
- Improve perceived service quality by keeping customers informed.

## Related Articles

- [Customer Inactivity SLA](../Supervisor/Customer-Inactivity-SLA.md)
- [SLA Calculations](../Supervisor/SLA-Calculations.md)
- [Media Routing Domains (MRD) Overview](Media-Routing-Domains-MRD-Overview.md)
- [Routing Attributes and Queues](Routing-Attributes-and-Queues.md)
