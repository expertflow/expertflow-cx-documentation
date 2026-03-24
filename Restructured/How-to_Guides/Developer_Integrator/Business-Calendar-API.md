---
title: "Business Calendar API Configurations"
summary: "Overview and API reference for the ExpertFlow CX Business Calendar — covering event management (business hours, holidays, out-of-office), shift scheduling, and links to the full API specification."
audience: [developer-integrator]
product-area: [routing, platform]
doc-type: explanation
difficulty: intermediate
keywords: ["business calendar API CX", "business hours API CX", "holiday calendar CX", "shift management CX", "calendar API CX", "business calendar configuration CX"]
aliases: ["CX calendar API", "business hours CX API", "event calendar CX"]
last-updated: 2026-03-10
---

# Business Calendar API Configurations

The Business Calendar in ExpertFlow CX is a scheduling tool that allows contact centers to define operating hours, holidays, and agent shifts. It is used by the routing engine to determine availability and by supervisors to manage staffing.

---

## Key Features

### Event Management

| Feature | Description |
|---|---|
| Create, update, delete events | Full CRUD operations on calendar events via API |
| Event types | `business_hours`, `holiday`, `out_of_office` |
| Recurring events | Configurable recurrence rules (daily, weekly, custom) |

### Shift Management

| Feature | Description |
|---|---|
| Schedule shifts | Define shifts with start and end times |
| Shift types | Morning, evening, night (or custom labels) |

---

## Technical Stack

| Component | Technology |
|---|---|
| **Backend** | Java |
| **Database** | MongoDB |

---

## API Reference

The full Business Calendar API specification — including endpoints for creating events, querying schedules, managing shifts, and configuring recurrence rules:

**API Documentation**: `https://api.expertflow.com/#587afb9b-0208-44c2-afee-f3a143853dff`

---

## Related Articles

- [Routing Engine Developer Guide](Routing-Engine-Developer-Guide.md)
- [Routing Attributes and Queues](../Administrator/Routing-Attributes-and-Queues.md)
- [Supervisor Assistance](../Supervisor_and_QA_Lead/Supervisor-Assistance.md)
