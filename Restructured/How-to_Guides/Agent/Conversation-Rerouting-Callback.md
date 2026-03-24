---
title: "Conversation Rerouting on Callback State"
summary: "Explanation of how ExpertFlow CX automatically reroutes active conversations when an agent changes their state to Not Ready — Callback, and how to configure this feature."
audience: [agent]
product-area: [channels, digital]
doc-type: explanation
difficulty: intermediate
keywords: ["conversation rerouting", "callback state agent", "not ready callback", "agent state change rerouting", "CX callback reason", "conversation auto-reroute", "callback not ready reason"]
aliases: ["callback rerouting", "agent callback state", "reroute on callback CX"]
last-updated: 2026-03-10
---

# Conversation Rerouting on Callback State

Available from **CX 4.10.5** onwards.

When an agent changes their MRD state to **Not Ready — Callback**, all of their active conversations are automatically rerouted to the original queue. This enables agents to step away for a callback without leaving customers waiting in an unhandled conversation.

## How It Works

1. The agent selects **Not Ready** with the reason **Callback**.
2. All active conversations currently assigned to that agent are immediately rerouted to the same queue they came from.
3. The conversations re-enter the queue as new requests, where they will be assigned to the next available agent.

## Configuration

### Step 1: Create the Callback Reason

1. Log in to **Unified Admin**.
2. Navigate to **Routing Engine → Not Ready Reasons** (or the applicable menu for reason codes).
3. Create a new reason with the type **Callback**.
4. Save.

### Step 2: Configure the Conversation Studio Flow

The rerouting behaviour is handled by a dedicated flow in Conversation Studio that responds to the agent state-change-to-Callback event.

- **Default training**: The Callback handling flow is already included. No additional action required.
- **Custom training**: Refer to the Conversation Studio default flows documentation — locate the **"Agent State Changed"** section (flow 17: _Task State Changed_) and update your customized flow to include the Callback scenario.

Once both steps are complete, the rerouting will trigger automatically whenever an agent sets their state to Not Ready — Callback.

## Related Articles

- [Managing Your Presence and States](Managing-Your-Presence-and-States.md)
- [Agent MRD States Reference](Agent-States.md)
- [Configuring Reason Codes](../Administrator/Configuring-Reason-Codes.md)
