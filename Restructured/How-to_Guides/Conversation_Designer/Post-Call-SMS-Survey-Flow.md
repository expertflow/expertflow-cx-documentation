---
title: "Designing a Post-Call SMS Survey Flow"
summary: "Step-by-step guide for Conversation Designers to create a campaign, build a survey form, and design the multi-reply SMS flow for post-call customer feedback."
audience: [conversation-designer]
product-area: [surveys, sms, campaigns, voc]
doc-type: how-to
difficulty: intermediate
keywords: ["post-call survey", "SMS survey flow", "campaign flow builder", "NPS", "CSAT", "survey init node", "form message node", "VOC"]
aliases: ["post call SMS flow", "SMS survey setup", "multi-reply survey flow"]
last-updated: 2026-04-09
---

# Designing a Post-Call SMS Survey Flow

This guide walks you through the end-to-end process of deploying a Post-Call SMS Survey — from creating the campaign to building and connecting the flow nodes. By the end, eligible callers will automatically receive an SMS-based NPS and CSAT survey after their call ends.

**Prerequisites:**
- SMS channel is configured (see [SMPP Configuration Guide](../Administrator/SMPP-Configuration-Guide.md))
- You have Campaign Manager access in Unified Admin
- You understand the [Post-Call SMS Survey](../../Capabilities/Digital_Channels/SMS/Post-Call-SMS-Survey.md) feature overview

---

## Step 1: Create the Campaign

A dedicated Campaign houses the survey flow and connects it to the triggering service.

1. In **Unified Admin**, navigate to **Campaigns** and click **+ New Campaign**.
2. Give the campaign a descriptive name (e.g., *Post-Call NPS Survey — Inbound Support*).
3. Set the campaign type to **SMS Survey**.
4. Save the campaign. You will configure the flow inside it in Step 3.

---

## Step 2: Create the Survey Form

Before building the flow, create the form that holds your survey questions. The Flow Builder references this form when sending messages to customers.

1. In **Unified Admin**, navigate to **Forms** and click **+ New Form**.
2. Name the form clearly (e.g., *Post-Call Feedback Form*).
3. Add your survey questions. A typical post-call survey includes:
   - An **opt-in question** (e.g., *"Reply 1 to take a quick survey, Reply 2 to skip, Reply 3 to stop receiving messages."*)
   - An **NPS question** (e.g., *"On a scale of 0–10, how likely are you to recommend us?"*)
   - A **CSAT question** (e.g., *"How satisfied were you with your experience? Reply 1 (Very Satisfied) to 5 (Very Dissatisfied)."*)
4. Save the form.

:::tip
All question text and response options in this form are fully editable at any time without requiring changes to the flow itself.
:::

---

## Step 3: Design the Flow

Open the Flow Builder for the campaign you created in Step 1 by clicking **View Flow Builder** inside the campaign's settings. Connect nodes in the sequence described below.

### 3.1 Survey Init Node

The Survey Init node is the mandatory starting point of every post-call SMS flow.

**How to add:**
1. Drag the **Survey Init** node onto the canvas. This must be the first node — it cannot be placed after any other node.
2. Click the node to configure it:

| Setting | Description |
|---|---|
| **Apply DNC** | Check this to skip any customer flagged as Do Not Contact. Recommended for compliance. |
| **Select Service** | Choose the CX service (e.g., *Inbound Support*) that should trigger this survey when a call ends. |

3. Connect the node's output to your first **Form Message** node (the opt-in question).

:::note
The Post-Call SMS Survey currently only supports flows triggered after **UCCX 15** services.
:::

---

### 3.2 Form Message Node

The Form Message node sends a question from your survey form and branches the flow based on the customer's reply. You will use one Form Message node per survey question.

**How to add:**
1. Drag a **Form Message** node onto the canvas and connect it to the previous node.
2. Configure the node:

| Setting | Description |
|---|---|
| **Node Name** | Give it a recognizable name (e.g., *Opt-In Question*, *NPS Question*). |
| **Select Form** | Choose the form you created in Step 2. |
| **Select Question** | Choose the specific question to send at this stage. |
| **Channel** | Select **SMS** (or WhatsApp if applicable). |
| **Customer Identifier** | Select the custom attribute that holds the customer's mobile number. |
| **Channel Identifier Index** | If the attribute holds multiple numbers, specify the index position to use. |
| **Timeout (Minutes)** | Set how long to wait for a reply before automatically ending the flow. |

**Node Outputs (dynamic branching):**

The node generates one output branch for each possible answer option in the selected question, plus:
- **Delivery Notification** — fires as soon as the message is sent.
- **Other** — fires if the customer replies with an unrecognized value (use this to loop back or send an error message).

Connect each answer branch to the appropriate next node (e.g., a "Reply 3 to Stop" branch → **Survey Opt-Out** node; low NPS scores → a **Plain Message** apology node).

---

### 3.3 Survey Opt-Out Node

Use this node when a customer indicates they no longer want to receive survey messages.

**How to add:**
1. Drag the **Survey Opt-Out** node onto the canvas.
2. Connect it from the answer branch that represents the customer's opt-out reply (e.g., the "3" output of your opt-in Form Message node).
3. No additional configuration is required.

**What it does:**
- Applies a DNC label to the customer's profile for the relevant channel (SMS or WhatsApp).
- Permanently excludes them from future survey campaigns (the Survey Init node will skip them automatically if DNC is checked).

**Connect its output** directly to an **End Survey** node.

---

### 3.4 End Survey Node

The End Survey node formally closes the customer's survey journey and stops all further survey timers and messages.

**How to add:**
1. Drag an **End Survey** node onto the canvas.
2. Connect it at the end of each completed flow branch (after the final thank-you message, and after the Survey Opt-Out node).
3. No customer-facing configuration is required.

**Optional — Backend integrations:**
If you need to trigger a backend action after the survey ends (e.g., log the result in a CRM or fire a webhook), connect the End Survey node's output to a custom integration node. The customer will receive no further messages, but your backend systems will still be updated.

---

### 3.5 Additional Nodes

#### Plain Message Node

Sends a plain text message without expecting a reply. Use it for auto-replies between questions, such as:
- *"Thank you for your high score!"* (after a positive NPS)
- *"We're sorry to hear about your experience."* (after a low NPS)
- A final closing message at the end of the survey

After a Plain Message node, add a **Post-Attempt Decision** node to handle delivery success or failure.

#### Post-Attempt Decision Node

Evaluates the delivery status of the previous Plain Message node and routes accordingly:
- **Success** → continue to the next question or End Survey
- **Failure** → route to an End Survey node to gracefully terminate

---

## Example Flow Structure

```
Survey Init
  └── Form Message (Opt-In Question)
        ├── [1] Opted In → Form Message (NPS Question)
        │     ├── [0–6] Low Score → Plain Message (Apology) → Post-Attempt Decision → [VOC Integration] → End Survey
        │     └── [7–10] High Score → Plain Message (Thank You) → Post-Attempt Decision → End Survey
        ├── [2] Skipped → End Survey
        └── [3] Opt-Out → Survey Opt-Out → End Survey
```

---

## Related Articles

- [Post-Call SMS Survey](../../Capabilities/Digital_Channels/SMS/Post-Call-SMS-Survey.md) — Feature overview, key features, and node reference table
- [Creating Survey Forms and Flows](Creating-Survey-Forms-and-Flows.md) — General guide to building survey forms
- [Post-Conversation Analytics](../../Capabilities/Reporting_and_Analytics/Post-Conversation-Analytics.md) — How survey results feed into post-interaction analytics
