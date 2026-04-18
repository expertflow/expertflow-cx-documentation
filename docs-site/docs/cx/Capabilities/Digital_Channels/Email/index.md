---
title: "Email Channel Overview"
summary: "Explanation of the Email channel in ExpertFlow CX — covering supported capabilities, email threading, attachments, signatures, outbound email, and routing behaviour."

product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["Email channel", "email integration", "email threading", "email connector", "outbound email", "email signature", "email forwarding", "email reply"]
aliases: ["email channel", "email connector overview", "CX email"]
last-updated: 2026-03-10
---

# Email Channel Overview

The Email channel in ExpertFlow CX enables agents to receive and respond to customer emails directly from the Agent Desk. It supports full email threading, attachments, CC/BCC, forwarding, and agent signatures — providing a familiar email experience within the contact centre workflow.

## Supported Capabilities

| Capability | Supported |
|---|---|
| Receive incoming emails | Yes |
| Reply to incoming email | Yes |
| Reply All (with CC/BCC) | Yes |
| Send new email to ongoing session customer | Yes |
| Initiate outbound email to any customer | Yes |
| Attachments (inbound and outbound) | Yes |
| Rich text styling | Yes |
| Agent signature (with dynamic agent details) | Yes |
| Email threading | Yes |
| Reply at any level of email thread | Yes |
| Forward emails | Yes |
| Forward any level of email thread | Yes |
| CC and BCC support | Yes |

## Email Threading

Each email conversation in CX is treated as a thread. Agents can:
- Reply to any message in the thread at any level.
- Forward any message in the thread to an external recipient.
- View the full conversation history in chronological order in the Conversation View.

## Attachments

**Tested supported formats (Agent Desk to Email):**
`png, jpg/jpeg, pdf, doc/docx, ppt/pptx, xls/xlsx, txt, mp4, mp3`

**Tested supported formats (Email to Agent Desk):**
`png, jpg/jpeg, pdf, doc/docx, ppt/pptx, xls/xlsx, txt, mp4, mp3, gif`

Additional formats may work but have not been formally validated.

## Outbound Email

Agents can initiate outbound email in two ways:
1. **To an ongoing session's customer**: From the active conversation view using the Email icon. This sends a new email to the customer involved in the current interaction.
2. **To any email address**: Available for fully outbound use cases (subject to system configuration).

## Routing

Email routing uses a **PULL** mode polling mechanism by default. The connector polls the configured mailbox at a set interval to fetch new messages. The polling interval is configurable via `SCHEDULER_FIXED_RATE_IN_MS`.

> For Exchange-based deployments, the connector applies a 1-minute buffer to account for Exchange processing time. See [Email Limitations](../Email-Limitations.md) for details.

## Supported Email Server Types

| Type | Configuration Guide |
|---|---|
| **IMAP/SMTP (Gmail and others)** | [Email Configuration — IMAP/SMTP](../Email-Configuration-IMAP-SMTP.md) |
| **Microsoft Exchange (EWS)** | [Email Configuration — MS Exchange](../Email-Configuration-MS-Exchange.md) |

## Related Articles

- [Routing Strategy: Pull Mode](../../../How-to_Guides/Administrator/Routing-Strategy-Pull-Mode.md)
- [Email Configuration — IMAP/SMTP](../Email-Configuration-IMAP-SMTP.md)
- [Email Limitations](../Email-Limitations.md)
- [Channel and Connector Setup](../../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
- [Configuring Wrap-up Forms](../../../How-to_Guides/Administrator/Configuring-Wrap-up-Forms.md)
