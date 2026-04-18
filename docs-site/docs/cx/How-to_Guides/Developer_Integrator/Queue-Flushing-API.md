---
title: "Queue Flushing API"
summary: "Reference for the Queue Flushing API in ExpertFlow CX — an API that clears all interactions from one or all queues with a configurable customer-facing closure message."
audience: [developer-integrator]
product-area: [routing]
doc-type: reference
difficulty: intermediate
keywords: ["queue flushing API CX", "flush queue CX", "clear queue CX", "queue API CX", "close all chats queue CX"]
aliases: ["CX queue flush API", "flush queue CX API", "clear queue API CX"]
last-updated: 2026-03-10
---

# Queue Flushing API

The Queue Flushing API clears all interactions from a specific queue or from all queues simultaneously. When triggered, each interaction in the queue is closed and the customer receives a configurable closure message.

---

## Behavior

When the Queue Flushing API is called:

1. All interactions in the targeted queue(s) transition to **CLOSED** state.
2. Each customer receives a configurable message, for example:
   > *"Your chat has been ended due to technical issues. Please come back later at a convenient time."*
3. Agents are not assigned to the flushed interactions.

---

## API Reference

Full API specification (request format, parameters, and response schema):

**API Documentation**: `https://api.expertflow.com/#194367d0-9c5a-4f80-b6ef-85a004d206d1`

---

## Use Cases

- Emergency maintenance — flush queues before taking the system offline.
- Queue overflow — administratively clear a backlogged queue.
- Testing and development — reset queue state between test runs.

---

## Related Articles

- [Routing Attributes and Queues](../Administrator/Routing-Attributes-and-Queues.md)
- [Queue Priority](../Administrator/Queue-Priority.md)
- [Routing Engine Developer Guide](Routing-Engine-Developer-Guide.md)
