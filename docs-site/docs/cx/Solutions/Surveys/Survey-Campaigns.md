---
title: "Survey Campaigns"
summary: "How ExpertFlow CX enables businesses to run outbound, multi-channel survey campaigns — collecting NPS, CSAT, and structured feedback at scale via SMS, WhatsApp, or Voice."
doc-type: explanation
last-updated: 2026-04-10
---

<!-- SOURCE: Confluence page 1876852738 — Automated Multi-reply Post Call SMS Survey -->

## The Business Problem

After a customer call ends, the window to collect meaningful feedback is short. Traditional follow-up methods — email surveys, manual callbacks — suffer from low response rates, delayed delivery, and no way to scale across hundreds or thousands of daily interactions. Businesses that rely on voice as their primary channel have no automated path to reach mobile customers on the channel they already checked: their phone.

Survey Campaigns solve this by turning call completion into an immediate, conversational feedback trigger — no agent action needed, no email required.

## What You Can Build

Survey Campaigns are outbound, business-initiated feedback flows launched by the ExpertFlow CX platform — distinct from post-collaboration surveys, which fire reactively when a conversation ends. With Survey Campaigns, you define the audience, the channel, the questions, and the trigger; the platform manages delivery, reply branching, opt-out compliance, and result storage automatically.

### SMS Survey Campaign

Immediately after an eligible inbound call ends, mobile callers receive a multi-reply SMS survey. The flow starts with an opt-in prompt, then walks the customer through NPS and CSAT questions one at a time — each reply branches to a tailored response or the next question. No agent involvement is required at any point.

### WhatsApp Survey Campaign

The same conversational survey experience delivered over WhatsApp. Suitable for customers who engage on WhatsApp as their primary messaging channel, using the same flow logic and branching as the SMS campaign.

### Voice (IVR) Survey Campaign

After a call, the customer is transferred to an IVR flow that reads out survey questions. Responses are captured via DTMF keypress or speech recognition, making this the right option when customers do not have or prefer not to use SMS/WhatsApp.

## How It Works

**Step 1 — Build the survey form.**
In Unified Admin → Forms, create the form that defines your questions: an opt-in MCQ, an NPS scale (0–10), a CSAT question (1–3 or 5-star), or any combination. This form is the content layer — it stores the questions the flow will send.

**Step 2 — Design the outbound flow in the Campaign Flow Builder.**
Open Campaign Manager, create a campaign, and open its Flow Builder. Connect nodes in sequence: Survey Init (entry point and trigger configuration) → Form Message nodes (one per question) → Plain Message nodes (auto-replies such as "Thank you" or "We're sorry") → Survey Opt-Out node (for customers who reply "Stop") → End Survey nodes on every branch.

**Step 3 — Set the trigger and go live.**
In the Survey Init node, select the inbound service whose call completions should fire the survey and enable DNC checking. Deploy the flow. From this point, every qualifying call completion automatically initiates the survey — the platform handles delivery, reply routing, opt-outs, and stores all responses as CX Activities.

## Key Features

- **Intelligent triggering** — launch based on call completion, service type, or device type
- **Conversational branching** — multi-step logic: opt-in → NPS → CSAT, with dynamic routing based on responses
- **Opt-out compliance** — DNC tagging built into the flow
- **Customisable content** — all questions and auto-replies editable by administrators without code changes
- **Reporting** — responses stored as CX Activities; exportable to Power BI and other tools

## Supported Channels

| Channel | Supported |
|---|---|
| SMS | Yes |
| WhatsApp | Yes |
| Voice (IVR) | Yes |

---

## Go Deeper

- **Back to:** [Surveys overview](index.md)
- **Capability docs:** [Digital Channels](../../Capabilities/Digital_Channels/index.md) · [AI and Automation](../../Capabilities/AI_and_Automation/index.md)
- **Configure it:** [Creating Survey Forms and Flows](../../How-to_Guides/Conversation_Designer/Creating-Survey-Forms-and-Flows.md)
