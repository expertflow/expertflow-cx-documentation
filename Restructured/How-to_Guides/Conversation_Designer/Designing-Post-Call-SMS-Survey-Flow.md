---
title: "Designing a Post-Call SMS Survey Flow"
summary: "Step-by-step guide to configure and deploy an automated multi-reply SMS survey triggered at the end of an inbound call using Campaign Manager."
audience: [conversation-designer, administrator]
doc-type: how-to
last-updated: 2026-04-10
---

# Designing a Post-Call SMS Survey Flow

This guide walks through configuring an automated multi-reply SMS survey that triggers immediately after an inbound call ends. Eligible mobile callers receive an opt-in message followed by NPS and CSAT questions. Optionally, low scores can automatically create VOC tickets in a third-party CRM.

**Prerequisite — Create the campaign first.** The survey flow lives inside a Campaign. Before continuing here, follow [Managing Outbound Campaigns](../Administrator/Managing-Outbound-Campaigns.md) to create a dedicated campaign for this flow, then return here to build the flow inside it.

---

## Step 1 — Create the Survey Form

Before connecting nodes in the Flow Builder, create the form that stores your survey questions. The Form Message node (Step 3) references this form to know what to send at each stage.

1. Navigate to **Unified Admin → Forms**.
2. Click **Create New Form** and give it a descriptive name (e.g., "Post-Call NPS & CSAT Survey").
3. Add your questions in order:
   - **Opt-In question** — MCQ with options: Yes / No / Stop.
   - **NPS question** — numeric scale 0–10.
   - **CSAT question** — MCQ with options on a 1–3 scale.
4. Click **Save**.

---

## Step 2 — Open the Flow Builder

1. Open the campaign you created in the prerequisite step.
2. Click **View Flow Builder** inside the campaign's settings. You are taken to a canvas where you connect nodes to define the survey logic.

---

## Step 3 — Add the Survey Init Node

The Survey Init node is the entry point for the entire flow. It determines who receives the survey and when.

**Placement:** This must be the very first node on the canvas.

**Configuration:**

| Setting | What to do |
|---|---|
| Apply DNC | Check this box to automatically skip any contact tagged as Do Not Contact. |
| Select Service | Choose the inbound service (e.g., "Inbound Support") whose call completions should trigger the survey. |

**Output:** One output connection — link it to the first Form Message node.

> **Note:** The current release only supports post-call triggers for UCCX 15 services.

---

## Step 4 — Add Form Message Nodes

Add one Form Message node per survey question. Each node sends a message and branches based on the customer's reply.

**Placement:** Connect immediately after Survey Init, then chain subsequent Form Message nodes to handle NPS and CSAT questions.

**Configuration per node:**

| Setting | What to do |
|---|---|
| Node Name | Give each a recognisable name (e.g., "Opt-In Question", "NPS Question"). |
| Select Form | Choose the form you created in Step 1. |
| Select Question | Pick the specific question to send at this point in the flow. |
| Channel | Select **SMS** (or WhatsApp if applicable). |
| Customer Identifier | Choose the CX attribute that stores the customer's mobile number. |
| Channel Identifier Index | If the attribute holds multiple numbers, specify the position (index) of the one to use. |
| Timeout (Minutes) | Set how long to wait for a reply before ending the survey. |

**Outputs (auto-generated per question):**

- One branch per valid answer option (e.g., 0 through 10 for an NPS question).
- **Delivery Notification** — fires as soon as the message is sent.
- **Other** — fallback for invalid replies; use to re-prompt or end the flow.

---

## Step 5 — Handle Opt-Out with the Survey Opt-Out Node

Connect the "Stop" branch of your Opt-In question to a Survey Opt-Out node.

**What it does:** Applies a DNC label for the channel (SMS or WhatsApp) to the customer's profile. Future survey campaigns with DNC checking enabled will automatically skip this contact.

**Output:** One output — link directly to an End Survey node.

---

## Step 6 — Add Plain Message Nodes for Auto-Replies

Use Plain Message nodes to send transitional text between questions or as closing messages. Unlike Form Message, these do not expect a reply.

Common uses:
- "Thank you!" response to a high NPS score.
- "We're sorry to hear that." response to a low NPS score.
- A final closure message after CSAT is captured.

After each Plain Message node, add a **Post-Attempt Decision Node** to check delivery status and route the flow accordingly (success → next step; failure → End Survey).

---

## Step 7 — End the Flow with End Survey Nodes

Place an End Survey node at the end of every branch, including:
- After the final survey closure message.
- After the Survey Opt-Out node.
- On any timeout or failure path.

**Optional — backend integrations:** You can link the End Survey node's output to a custom integration node (e.g., push data to Power BI or create a VOC ticket in a CRM) without sending further messages to the customer.

---

## Resulting Flow Structure

```
Survey Init
└── Form Message: Opt-In
    ├── "Yes" → Form Message: NPS
    │             ├── 0–6 (detractor) → Plain Message: Apology → Post-Attempt Decision → End Survey
    │             │                                               [optional: VOC ticket integration]
    │             └── 7–10 (promoter) → Form Message: CSAT → Plain Message: Thank You → End Survey
    ├── "No"  → End Survey
    └── "Stop" → Survey Opt-Out → End Survey
```

---

## Related

- **Back to:** [Creating Survey Forms and Flows](Creating-Survey-Forms-and-Flows.md)
- **Solution context:** [Post-Collaboration Surveys](../../Solutions/Surveys/Post-Collaboration-Surveys.md)
- **Campaign setup:** [Managing Outbound Campaigns](../Administrator/Managing-Outbound-Campaigns.md)
- **Capability reference:** [AI and Automation](../../Capabilities/AI_and_Automation/index.md) · [Digital Channels](../../Capabilities/Digital_Channels/index.md)
