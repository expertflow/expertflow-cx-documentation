---
title: "Consult, Transfer, and Conference"
summary: "How-to guide for agents using consult, transfer, and conference features in ExpertFlow CX — covering queue and agent consult, direct and consult transfers, conference calls, and external number support for both chat and voice."
audience: [agent, supervisor]
product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["consult transfer", "conference call CX", "agent consult", "queue consult", "direct transfer", "agent transfer", "voice conference", "chat transfer", "whisper message", "CX Agent Desk transfer"]
aliases: ["transfer conversation", "consult agent", "conference chat", "transfer chat CX"]
last-updated: 2026-03-10
---

# Consult, Transfer, and Conference

ExpertFlow CX agents can consult another agent during an active conversation, transfer the conversation to a queue or named agent, or add an agent to the conversation in conference mode. All three operations are available for both chat and CX Voice sessions, with some differences per channel.

---

## Consult on a Conversation

Consulting allows a primary agent to get help from a second agent while the customer conversation remains active. The consulted agent joins as an **ASSISTANT** — they can see the conversation history but the customer is unaware of the assistant unless the conversation is conferenced.

### Queue Consult

1. Click the **Agent Assistance** button on the conversation control toolbar.
2. A dropdown appears listing all queues linked to the CX Voice or CHAT MRD, showing each queue's name and the number of available agents.
3. Select a queue and click **Consult**.
4. Optionally enter a note for the receiving agent in the Queue Consult dialog (chat only), then click **Consult Request**.
5. The system places the request in the queue at priority and looks for an available agent.
   - If an agent accepts, they join the conversation as an **ASSISTANT**.
   - If no agent is available before the TTL expires, a **"No Agent Available"** notification appears in the interaction history.
6. The consulting agent receives a notification: _"Queue Consult Request has been placed."_

### Agent Consult

1. Click the **Agent Assistance** button on the control toolbar.
2. In the queue list, expand a queue to view individual available agents.
3. Hover over an agent and click **Consult**.
4. The request is routed to the selected agent.
5. The receiving agent sees a notification with the channel icon, an Accept button, the primary agent's name, and any optional notes (chat only).
6. Click **Accept** to join the conversation as an **ASSISTANT**.

### Consult on an External Number

1. Click the **Agent Assistance** button.
2. Navigate to the **Dialpad** in the dropdown.
3. Enter a number (2–18 digits).
4. Click **Consult** to place the request.
5. A notification confirms: _"Consult request placed successfully."_

### Consult Limitations

- Optional notes are only available for chat sessions (not voice).
- If a consult is already in progress on chat and a voice session becomes active, the consult remains limited to the chat channel.
- Repeated simultaneous consult requests are not supported; the system returns a generic error.
- No external leg data is stored in CX.

---

## Transfer a Conversation

Transferring moves the conversation away from the primary agent to a new agent or queue.

### Direct Queue Transfer

1. Click the **Agent Assistance** button.
2. Select a queue from the dropdown and choose **Transfer**.
3. Optionally enter a note for the receiving agent in the Transfer dialog.
4. Click **Transfer**.
5. The conversation is closed for the primary agent (notification: _"Conversation closed due to CHAT TRANSFERRED"_) and placed in the target queue.
6. The customer sees: _"Your request is being transferred to [queue-name], please wait!"_
7. When an agent accepts, the customer is notified: _"Agent has joined the conversation."_
8. If no agent accepts before the TTL expires, the customer sees: _"No agents were available."_

### Direct Agent Transfer

1. Click the **Agent Assistance** button.
2. Expand a queue to view available agents.
3. Hover over the target agent and click **Transfer**.
4. The request is routed to the selected agent based on availability.
5. The receiving agent sees a notification with channel icon, customer name, customer number, and an Accept button.

### Direct Transfer to an External Number

1. Click the **Agent Assistance** button and navigate to the **Dialpad**.
2. Enter a number (2–18 digits).
3. Click **Transfer**.
4. Notification confirms: _"Transfer request placed successfully."_
5. The primary agent is unsubscribed from the conversation in CX.

> **Prerequisite**: A CX Voice session must be active for external number transfer. Internal DNs are not supported.

### Transfer Limitations

- No external leg data is stored in CX.
- No error is displayed when the Transfer button is clicked while the gateway is down (CCC-1625).
- No error is shown when an invalid external number is dialed — the customer call drops (CCC-1622).

---

## Consult Transfer

After a consult is established, the primary agent can transfer the conversation to the consulted agent (ASSISTANT).

### Consult Transfer — Chat

1. In the active conversation, click the **Participants list** button on the toolbar.
2. Locate the participant with the **ASSISTANT** role.
3. Click **Transfer** next to the ASSISTANT.
4. Notification: _"Consult transfer request has been placed."_
5. The primary agent is unsubscribed. The ASSISTANT becomes the new **PRIMARY** agent and can interact directly with the customer.

### Consult Transfer — CX Voice

1. During an active consult call, click the **Consult Transfer** button on the CTI toolbar.
2. Notification: _"Consult transfer request has been placed."_
3. The primary agent is unsubscribed. The ASSISTANT becomes the new PRIMARY agent.

### Consult Transfer — External Number

1. With an active external consult call, click **Consult Transfer** on the Call Control bar.
2. The transfer is forwarded to the external number.
3. Notification: _"Transfer request placed successfully."_
4. The primary agent is unsubscribed.

> **Note**: Consult Transfer on a voice session should only be done if the consulted agent is also part of the voice call. The primary agent is the only one who can initiate the transfer.

---

## Consult Conference

Consult Conference adds the ASSISTANT agent directly to the customer conversation as a co-primary participant. Both agents can interact with the customer simultaneously.

### Consult Conference — Chat

1. Click the **Participants list** button.
2. Locate the ASSISTANT participant.
3. Click **Conference**.
4. Notification: _"Consult Conference request has been placed."_
5. The ASSISTANT becomes a PRIMARY agent and can interact directly with the customer.

### Consult Conference — CX Voice

1. During an active consult call, click the **Consult Conference** button on the CTI toolbar.
2. Notification: _"Consult Conference request has been placed."_
3. The ASSISTANT joins the call as a PRIMARY participant alongside the original primary agent.

### Consult Conference — External Number

1. During an active external consult call, click **Consult Conference** on the Call Control bar.
2. The external number is added to the customer call.
3. The consult leg is dropped, and the external party joins the live call.

> **Maximum participants**: 4 agents can be in a conference call simultaneously.

---

## Add Agents to Conference (Queue-Based)

Agents can add additional agents to an ongoing conversation via a queue conference request, without first consulting.

1. Click the **Agent Assistance** button. A dropdown shows all available queues.
2. Select a queue and click **Queue Conference**.
3. Optionally type a message for the incoming agent. Click **Add to Conference**.
4. The system routes the request to an available agent in the selected queue.
5. The receiving agent (Agent 2) sees a conference request notification with:
   - A special indication that it is a Conference Chat request from Agent 1
   - The customer's identified name (if available)
   - Agent 1's optional note
   - An **Accept** button
6. Agent 2 joins as a PRIMARY participant with the same rights as Agent 1.
7. Agent 2 can see the full conversation history, customer profile, and active sessions.
8. If Agent 2 leaves, the conference continues with remaining participants.
9. If no agent accepts before the TTL expires, Agent 1 sees: _"No agents were available to join the conference conversation."_

---

## Related Articles

- [CTI Call Controls](../Voice_Real_Time_Media/CTI-Call-Controls.md)
- [Barge-in and Intervention](../../Supervisor/Barge-in-and-Intervention.md)
- [Agent Hand Raise](Agent-Hand-Raise.md)
- [Handling Customer Interactions](../../Agent/Handling-Customer-Interactions.md)
