---
title: "Conversation Flow for Outbound Dialing Modes"
summary: "Reference guide for designing conversation flows in Conversation Studio for outbound dialing — covering the Power/Predictive flow (agent seize before dialing) and the Preview/Progressive flow (agent assigned before call initiation), with DNC validation, CPA, routing logic, and screen pop steps."
audience: [conversation-designer]
product-area: [channels, voice]
doc-type: reference
difficulty: intermediate
keywords: ["outbound conversation flow CX", "power dialing flow CX", "predictive dialing flow CX", "preview dialing flow CX", "progressive dialing flow CX", "CPA conversation studio CX", "outbound flow designer CX"]
aliases: ["outbound dialing flow CX", "conversation studio outbound CX", "dialing mode flow CX"]
last-updated: 2026-03-10
---

# Conversation Flow for Outbound Dialing Modes

A **Conversation Flow** in Conversation Studio defines the sequence of nodes that control how outbound interactions are initiated, managed, and routed. The flow structure differs depending on the dialing mode: **Power/Predictive** (agent seized before calls are initiated) vs **Preview/Progressive** (agent assigned before the call is placed).

> **DNC Validation**: Every outbound flow should include a DNC check — typically inside the **WAIT** node — that verifies the contact does not have a DNC label assigned in CX-Customers before the call is initiated. See [DNC Lists](../Administrator/Managing-Outbound-Campaigns.md).

---

## Power and Predictive Dialing Flow

This flow reserves agent capacity first, then initiates multiple simultaneous calls.

### Steps

1. **Outbound SEIZE Node** — An agent (or a fraction of their capacity) from a specified skill group is seized. The agent is reserved for a _skill_ or as a _named individual_, but not yet assigned to a specific conversation.

2. **Optional WAIT Node** — Final conditional check before dialing. Use this node to:
   - Confirm current time is within permitted calling hours.
   - Verify campaign status is "active".
   - Check that the contact does not have a DNC label.

3. **INIT Node** — Initiates `x` interaction sessions (voice calls). The value of `x` is determined by the Power or Predictive dialing algorithm.

4. **Call Progress Analysis (CPA) — IVR/Chatbot** — An IVR (voice) or chatbot (messaging) performs CPA. Detected outcomes:
   - Busy
   - Answering machine
   - Fax
   - No answer
   - Live answer
   - Customer requests opt-out

5. **Branch on CPA Outcome**:
   - **Answering machine** → Route to a voicebot to leave a message.
   - **Busy / No answer** → Schedule a re-attempt after a defined interval using flow logic.
   - **Customer requests opt-out** → Use the **Add Contact Label** node to assign a DNC label, preventing future outreach from relevant campaigns.

6. **ROUTING Node** (live customer reached) — Routes the connected call based on the initial seizure strategy:
   - **Queue-based / Shared** — Routes to an available agent in the seized skill group (e.g., longest idle, skill match).
   - **Direct Agent / Personal Callback** — Routes to the specifically reserved agent from the SEIZE step.
   - **Mixed** — Initial IVR qualification before routing to a specific agent or queue.
   - Routing attempts have a configurable timeout; on timeout, the call can be transferred to an alternate queue/IVR or abandoned.

7. **Agent Assignment** — The seized agent is formally assigned to the connected call.

8. **Optional Personalized Agent Greeting (IVR)** — A pre-recorded `.wav` file specific to the agent is played to the customer via conference. The file is stored with the agent's profile.

9. **Screen Pop** — Customer data is displayed in the agent's interface when the call connects.

---

## Preview and Progressive Dialing Flow

This flow assigns an agent to a contact record before the call is initiated. DNC checks are performed before the contact is routed to an agent.

### Steps

1. **ROUTING Node (Agent First)** — A customer contact record (as a task) is routed to an agent. Selection strategies:
   - **Queue-based / Shared** — Assigns the next available agent in the relevant queue.
   - **Direct Agent / Personal Callback** — Assigns directly to a pre-determined agent (e.g., for follow-up or a dedicated account manager).
   - **Mixed** — Initial system step before assignment to a specific agent or queue.

   The selected agent is reserved for this interaction.

2. **Screen Pop** — Customer data is displayed in the agent's interface.

3. **Call Initiation** (mode-dependent):
   - **Progressive Mode** — System automatically initiates CPA and dialing.
   - **Preview Mode** — Agent manually triggers CPA and dialing via a "Dial" button.

4. **Call Progress Analysis (CPA)** — Executed the same way as in the Power/Predictive flow (step 4 above).

5. **Customer Reached & Connection** — The dialed party answers.

6. **Optional Personalized Agent Greeting (IVR)** — As in the Power/Predictive flow.

---

## Related Articles

- [Outbound Flows Limitations](Outbound-Flows-Limitations.md)
- [Managing Outbound Campaigns](../Administrator/Managing-Outbound-Campaigns.md)
- [As a Conversation Designer](As-a-Conversation-Designer.md)
