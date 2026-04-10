---
title: "Post-Collaboration Surveys"
summary: "How ExpertFlow CX automatically triggers NPS, CSAT, and structured feedback collection at the end of every customer interaction — across voice, chat, email, and social channels."
doc-type: explanation
last-updated: 2026-04-10
---

<!-- CONTENT STATUS: Skeleton — section headers and intent defined. Full narrative to be written. -->
<!-- SOURCE: Confluence page 131432544 — Surveys -->

## The Business Problem

_What pain does this solve? e.g. agents forget to send feedback links, response rates are low, no unified view of satisfaction across channels._

## What You Can Build

_One paragraph establishing that post-collaboration surveys are platform-triggered automatically when a conversation ends — no manual agent action needed._

## How It Works

_Simple 3-step flow (not a config guide). e.g.:_
_1. A conversation ends (agent leaves, SLA expires, or customer disconnects)._
_2. Conversation Studio detects the trigger and initiates the survey in the same session or via a follow-up channel (e.g. SMS after a voice call)._
_3. Customer responses are stored in unified interaction history as CX Activities._

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
- **Capability docs:** [AI and Automation](../../../Capabilities/AI_and_Automation/index.md) · [Digital Channels](../../../Capabilities/Digital_Channels/index.md) · [Voice and Video](../../../Capabilities/Voice_and_Video/index.md)
- **Configure it:** [Creating Survey Forms and Flows](../../../How-to_Guides/Conversation_Designer/Creating-Survey-Forms-and-Flows.md) · [Designing a Post-Call SMS Survey Flow](../../../How-to_Guides/Conversation_Designer/Designing-Post-Call-SMS-Survey-Flow.md)
