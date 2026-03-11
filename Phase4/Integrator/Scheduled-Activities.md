---
title: "Scheduled Activities"
summary: "Reference guide for the ExpertFlow CX Scheduled Activities API — covering how third parties schedule future customer activities via any channel, the 10-step delivery and notification flow, and the Scheduler feature set including webhook registration, delivery notifications, and activity management."
audience: [developer, integrator]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["scheduled activities API CX", "scheduler API CX", "schedule customer activity CX", "delivery notification CX scheduler", "webhook registration CX scheduler"]
aliases: ["scheduler API CX", "scheduled activity CX", "CX activity scheduler"]
last-updated: 2026-03-10
---

# Scheduled Activities

A **scheduled activity** is a customer interaction scheduled for a future date and time. When executed, scheduled activities appear in the **Customer Activity Timeline** in the Agent Desk alongside past conversation history, giving agents a complete 360-degree view of past and upcoming customer touchpoints.

The **Scheduler API** allows third-party systems (such as campaign managers or CRM platforms) to push scheduled activities into ExpertFlow CX. When the scheduled time arrives, the Scheduler executes the activity and publishes results to registered webhooks.

For the full API reference, see the [Scheduler API documentation](https://api.expertflow.com/#a6e51948-0ff3-4817-a91e-3c452d7df028).

---

## How It Works

1. A third party schedules an activity by calling the Scheduler API, specifying the channel, customer identifier, date/time, and optional agent or queue.
2. The Scheduler pushes the activity to **CX Activities** — it becomes visible in the Customer Activity Timeline with status `Scheduled`.
3. The Scheduler queues the activity internally and waits for the scheduled date/time.
4. At the scheduled time, the Scheduler forwards the activity to **CCM (Channel Manager)**.
5. CCM routes the activity to the relevant **channel connector** based on the specified channel.
6. When the activity is delivered, CCM sends a delivery notification back to the Scheduler.
7. The Scheduler updates the activity status in **CX Activities** (e.g., `Delivered`, `Failed`).
8. The Scheduler also publishes the delivery notification to all **registered webhooks**.
9. If the activity was a chat message:
   - CCM sends a `READ` notification once the customer has read the message or replied.
   - If the customer replies, CCM forwards the response to the Scheduler.
10. The Scheduler pushes the `READ` notification and customer response to both **CX Activities** and the **registered webhooks**.

---

## Feature Reference

| Feature | Description |
|---|---|
| **Scheduler API** | Schedule an activity via any supported channel to any customer channel identifier |
| **Delivery Notifications** | Receive delivery status (`delivered`, `failed`) from channel connectors and relay to CX Activities and registered webhooks |
| **Scheduled Activities in CX Activities** | Push scheduled activities to the customer activity feed so agents can see upcoming interactions |
| **Named Agent or Queue** | Schedule an activity with a specific named agent or a queue |
| **Webhook Registration API** | `POST`, `GET`, `DELETE` endpoints to manage webhook registrations for delivery notifications |
| **Delete a Scheduled Activity** | Remove an already-planned activity before it executes |
| **Update a Scheduled Activity** | Modify a scheduled activity — for example, change the scheduled time |

---

## Related Articles

- [Integrations Overview](Integrations.md)
- [Channel Connector Developer Guide](Channel-Connector-Developer-Guide.md)
- [Register Channel Connector](Register-Channel-Connector.md)
