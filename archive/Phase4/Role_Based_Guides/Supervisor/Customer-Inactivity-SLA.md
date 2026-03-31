---
title: "Customer Inactivity SLA"
summary: "Explanation of the Customer Inactivity SLA feature in ExpertFlow CX — how the inactivity timer works, how to configure thresholds via the Channel settings and API, and what happens when the timer expires."
audience: [supervisor, solution-admin]
product-area: [channels, digital]
doc-type: explanation
difficulty: intermediate
keywords: ["customer inactivity SLA", "customer activity timeout", "customer SLA timer", "conversation timeout CX", "SLA threshold configuration", "channel activity timeout", "customer inactivity CX"]
aliases: ["customer timeout", "inactivity timer CX", "channel activity timeout CX"]
last-updated: 2026-03-10
---

# Customer Inactivity SLA

The Customer Inactivity SLA sets a time limit for how long CX waits for a customer to respond after an agent sends a message. If the customer does not respond within the configured timeout, the conversation is automatically ended.

## How the Timer Works

1. The countdown begins as soon as the **agent sends a message** to the customer.
2. If the customer responds before the timer expires, the timer resets.
3. If the customer does not respond before the timer reaches zero, the conversation controller sends a **channel session ended** event and closes the conversation.

Multiple intermediate thresholds can be configured — for example, at 50%, 80%, and 100% of the timeout — to trigger reminder messages before ending the conversation.

## Configuring the Timeout

### Step 1: Set the Timeout on the Channel

1. Log in to **Unified Admin**.
2. Navigate to **Channel Manager → Channel**.
3. Select the channel and click **Edit**.
4. Set the **Customer Activity Timeout** value in seconds (e.g., `300` for 5 minutes).
5. Save.

### Step 2: Configure Thresholds (API)

Thresholds control what action is taken at each percentage of the timeout. Currently, there is no front-end interface for threshold configuration — use the API:

**Create or update thresholds:**
```
POST {{conversation-monitor-url}}/customer-sla-thresholds
```

**View current thresholds:**
```
GET {{conversation-monitor-url}}/customer-sla-thresholds
```

**Delete all thresholds** (send empty array):
```
POST {{conversation-monitor-url}}/customer-sla-thresholds
Body: []
```

### Supported Actions at Each Threshold

The system currently supports two actions triggered at each threshold:
- **Send a notification/reminder message to the customer** (e.g., at 50% and 80% of timeout)
- **End the channel session** (e.g., at 100% of timeout)

## Default Behaviour

If no thresholds are configured, the SLA timer runs for the full duration specified in the Channel configuration. The conversation ends when the timeout completes — with no intermediate reminders.

## Related Articles

- [SLA Calculations](SLA-Calculations.md)
- [Channel and Connector Setup](../Solution_Admin/Channel-and-Connector-Setup.md)
- [Understanding Response SLA](../Agent/Understanding-Response-SLA.md)
