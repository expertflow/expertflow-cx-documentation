---
title: "Post-Collaboration Surveys"
summary: "How ExpertFlow CX automatically triggers NPS, CSAT, and structured feedback collection at the end of every customer interaction — across voice, chat, email, and social channels."
doc-type: explanation
last-updated: 2026-04-10
---

<!-- SOURCE: Confluence page 131432544 — Surveys -->

## The Business Problem

Without an automated feedback mechanism, collecting post-interaction customer feedback depends entirely on agents remembering to send a link or ask a question before closing a conversation. That rarely happens consistently. The result is low response rates, gaps in satisfaction data, and no reliable way to compare experience quality across voice, chat, email, and social channels from a single view.

ExpertFlow CX solves this by making survey delivery a platform responsibility, not an agent task. Surveys are triggered automatically based on conversation events, ensuring consistent coverage across every interaction regardless of which agent handled it or which channel the customer used.

## What You Can Build

Post-collaboration surveys in ExpertFlow CX are triggered automatically by Conversation Studio when a conversation ends — no manual agent action required. You can collect NPS, CSAT, and free-text feedback through the same channel the customer used (web chat, WhatsApp, voice IVR) or via a follow-up channel (SMS after a voice call). Survey forms are built in the Form Builder with branching logic, and all responses are stored in the customer's unified interaction history as CX Activities. Conversation Designers can extend and customise the flow with third-party integrations to fit any interaction management requirement.

## How It Works

**Step 1 —** A customer starts a session via any supported channel (voice, chat, web, email, or social).

**Step 2 —** Conversation Studio hands the session to a bot or a human agent, who handles the interaction.

**Step 3 —** When the defined trigger fires (agent leaves, all agents have left, or SLA expires), Conversation Studio initiates the survey — either within the same session or as a follow-up (for example, an SMS chat session dispatched after a voice call ends).

**Step 4 —** The session is transferred to an IVR flow or an AI bot (voice or chat), which delivers the survey questions to the customer.

**Step 5 —** Customer responses are collected and stored in their unified interaction history as CX Activities.

**Step 6 —** Conversation Designers and supervisors can analyse the collected CX Activities in Reports to identify trends and drive improvements to customer satisfaction.

## Delivery Methods

### Survey via Structured Message

Questions sent one at a time through the same channel the conversation used. Supports branching — next question depends on previous answer. Works on web chat, WhatsApp, and other digital channels.

### Survey via URL

A link to a web-based survey form sent as a message. Customer fills in the full form in their browser. Useful when the conversation channel doesn't support structured messages.

### IVR Survey (Voice)

After a voice call, the customer is transferred to an IVR flow that reads out survey questions. Responses captured via DTMF or speech recognition.

### Post-Call SMS Survey (Multi-Reply)

Immediately after an inbound voice call ends, eligible mobile callers receive an SMS-based feedback flow managed through Campaign Manager — no agent action required. The flow is conversational: the customer receives an opt-in prompt, then NPS and CSAT questions one at a time, with branching logic driven by each reply.

**Key capabilities:**

- **Intelligent triggering** — surveys fire automatically based on call completion, client type (Transactional or Foundational), and device type (mobile numbers only).
- **DNC compliance** — contacts tagged Do Not Contact are automatically skipped; customers can opt out mid-survey and are permanently excluded from future campaigns.
- **Dynamic branching** — each reply routes the customer to a tailored response (thank-you, apology) or the next question.
- **Customisable content** — all SMS messages are editable by administrators without code changes.
- **VOC ticket creation** — optionally generates a ticket in a third-party CRM when scores fall below a configured threshold. _(Custom integration — scope varies by deployment.)_
- **Data export** — survey results can be pushed to external reporting tools such as Power BI via API.

## Survey Question Types

NPS · CSAT (5-star, 1–3 scale) · MCQ · Free text input

## Trigger Conditions

- Agent leaves the conversation
- All agents have left (conversation becomes inactive)
- SLA expires
- Custom conditions (e.g. suppress survey if customer contacted within last 24 hours)

---

## Go Deeper

- **Back to:** [Surveys overview](index.md)
- **Capability docs:** [AI and Automation](../../Capabilities/AI_and_Automation/index.md) · [Digital Channels](../../Capabilities/Digital_Channels/index.md) · [Voice and Video](../../Capabilities/Voice_and_Video/index.md)
- **Configure it:** [Creating Survey Forms and Flows](../../How-to_Guides/Conversation_Designer/Creating-Survey-Forms-and-Flows.md) · [Designing a Post-Call SMS Survey Flow](../../How-to_Guides/Conversation_Designer/Designing-Post-Call-SMS-Survey-Flow.md)
