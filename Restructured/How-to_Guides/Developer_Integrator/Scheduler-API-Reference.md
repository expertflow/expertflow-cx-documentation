---
title: "Scheduler API & Workflow Reference"
summary: "Technical reference for the ExpertFlow CX Scheduler API, covering the scheduled activity lifecycle, 10-step message flow, and webhook status tracking."
audience: [developer-integrator]
product-area: [api, outbound, platform]
doc-type: reference
difficulty: advanced
last-updated: 2026-03-11
---

# Scheduler API & Workflow Reference

The ExpertFlow CX Scheduler API enables third-party applications (e.g., Marketing Automation, CRM) to schedule customer interactions for execution at a future date and time. These activities are integrated into the **Unified Customer Activity Timeline**, providing agents with a 360-degree view of both past and future engagements.

## 1. Scheduler API Lifecycle
The API manages the complete lifecycle of a scheduled interaction through the following states:

| Status | Description |
| :--- | :--- |
| **Scheduled** | The activity is successfully registered in the Scheduler database and pending execution. |
| **Queued** | The scheduled time has been reached; the activity is waiting for processing by the Channel Manager. |
| **Delivered** | The message has been successfully handed over to the external channel (e.g., WhatsApp, SMS). |
| **Connected** | For voice/outbound calls, the customer has answered and the call is active. |
| **Failed** | The activity could not be executed (e.g., invalid destination, channel down). |
| **Read/Replied** | The customer has engaged with the scheduled digital message. |

---

## 2. The 10-Step Message Flow
The following sequence defines how a scheduled digital activity (e.g., a WhatsApp notification) is processed through the platform:

1.  **Initiation:** A third-party system calls the Scheduler API with the payload and execution timestamp.
2.  **Activity Registration:** The Scheduler pushes the event to the **CX Activities** service to populate the customer timeline.
3.  **Queueing:** The activity is held in the Scheduler queue until the target date/time is reached.
4.  **Dispatch:** The Scheduler pushes the activity to the **Customer Channel Manager (CCM)**.
5.  **Connector Handoff:** CCM proxies the request to the relevant **Channel Connector** (e.g., Twilio, WhatsApp Cloud API).
6.  **Delivery Confirmation:** The Connector returns a delivery status to CCM, which forwards it to the Scheduler.
7.  **Timeline Update:** The Scheduler updates the interaction status in the CX Activity timeline.
8.  **Webhook Notification:** The Scheduler notifies the registered third-party webhook of the delivery status.
9.  **Engagement Tracking:** If the interaction is a chat message, CCM monitors for `READ` or `REPLY` events.
10. **Final Sync:** Engagement events are pushed back to the Scheduler and subsequently to the originating system's webhook.

---

## 3. Webhook Registration & Management
To receive real-time status updates, developers must register an endpoint via the Webhook API.

*   **Registration (POST):** Define the target URL and the event types to monitor (e.g., `DELIVERY_SUCCESS`, `DELIVERY_FAILURE`).
*   **Status Tracking:** The Scheduler sends a JSON payload to the webhook for every state change in the lifecycle.
*   **CRUD Operations:** The API supports retrieving current webhook configurations, updating target URLs, and deleting registrations.

---

## 4. Key Developer Features
*   **Named Agent Scheduling:** Provision to schedule an activity and automatically route it to a specific agent when they become available.
*   **Queue-Specific Scheduling:** Send scheduled interactions to a high-priority queue for immediate handling upon execution.
*   **CRUD for Activities:** Full support for updating (e.g., rescheduling the time) or deleting already planned activities.

---

## Related Guides
*   [CIM Message Schema Master](../../Reference/Schemas_and_Data_Model/CIM_Message_Schema/CIM-Messages.md)
*   [Agent Task Routing Lifecycle](Agent-Task-Routing-Lifecycle.md)
*   [Interaction Model Overview](../../Reference/Schemas_and_Data_Model/Socket_Events/index.md)
