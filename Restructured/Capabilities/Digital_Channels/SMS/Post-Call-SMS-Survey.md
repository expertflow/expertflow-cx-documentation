---
title: "Post-Call SMS Survey"
summary: "Overview of the Automated Multi-reply Post-Call SMS Survey — how ExpertFlow CX triggers NPS and CSAT feedback flows via SMS immediately after an inbound call ends."
product-area: [channels, digital, sms, surveys, voc]
doc-type: explanation
difficulty: intermediate
keywords: ["post-call survey", "SMS survey", "NPS", "CSAT", "VOC", "voice of customer", "customer feedback", "multi-reply SMS"]
aliases: ["post call SMS survey", "automated SMS survey", "VOC SMS"]
last-updated: 2026-04-09
---

# Post-Call SMS Survey

The Post-Call SMS Survey automatically triggers an SMS-based feedback flow immediately after an inbound call ends. Eligible mobile callers receive an opt-in message followed by NPS and CSAT questions. Optionally, low scores can trigger automatic VOC ticket creation for immediate follow-up, and all survey data is available for export to external reporting tools such as Power BI.

The feature is designed to close the loop on customer experience in near real time, giving business teams full control over survey questions, responses, and downstream data usage — without requiring code changes.

## Key Features

- **Intelligent Triggering:** Automatically initiates surveys based on call completion, client type (Transactional or Foundational), and device type (mobile numbers only).
- **Dynamic Conversational Flow:** Multi-step branching logic handles opt-ins, Net Promoter Score (NPS) questions, and Customer Satisfaction (CSAT) questions within a single SMS thread.
- **Automated VOC Ticketing / CRM Integration:** Optionally generates tickets or deals in a third-party ticketing system or CRM when scores fall below configured thresholds. This is a custom integration depending on your use case.
- **Customizable Content:** All SMS messages — questions, auto-replies, and closing messages — are fully editable by administrators without code changes.
- **Seamless Data Export:** Built-in API capabilities push survey data directly to external reporting tools such as Power BI.

## How It Works

1. An inbound call handled on a configured service (e.g., UCCX 15) ends.
2. The platform checks whether the caller's number is a mobile number and is not flagged as Do Not Contact (DNC).
3. An opt-in SMS is sent to the customer asking if they are willing to complete a short survey.
4. Based on the customer's reply, the flow branches into NPS and CSAT question steps.
5. Low scores can automatically route to a VOC ticket node that creates a follow-up ticket in your CRM.
6. The survey closes with a thank-you message, and all response data is logged and available for export.

:::note Current Limitation
The Post-Call SMS Survey currently only supports flows triggered after **UCCX 15** services. Support for additional services is on the roadmap.
:::

## Survey Flow Overview

The survey is built in the **Campaign Flow Builder** using a set of dedicated nodes:

| Node | Purpose |
|---|---|
| **Survey Init** | Entry point — selects the service to monitor and applies DNC checks |
| **Form Message** | Sends a question from a pre-built form and branches on the customer's reply |
| **Survey Opt-Out** | Tags the customer as DNC and ends the flow if they choose to stop |
| **End Survey** | Formally terminates the survey; optionally triggers backend integrations |
| **Plain Message** | Sends a non-question message (e.g., thank-you or apology auto-reply) |
| **Post-Attempt Decision** | Routes the flow based on message delivery status |

## Related Articles

- [Designing a Post-Call SMS Survey Flow](../../../How-to_Guides/Conversation_Designer/Post-Call-SMS-Survey-Flow.md) — Step-by-step guide to building the campaign, form, and flow in the Flow Builder
- [Creating Survey Forms and Flows](../../../How-to_Guides/Conversation_Designer/Creating-Survey-Forms-and-Flows.md) — General guide to building survey forms in the Form Builder
- [Post-Conversation Analytics](../../Reporting_and_Analytics/Post-Conversation-Analytics.md) — NLP/ML insights including sentiment and VOC signals captured post-interaction
- [SMPP Configuration Guide](../../../How-to_Guides/Administrator/SMPP-Configuration-Guide.md) — SMS gateway setup required before using any SMS feature
