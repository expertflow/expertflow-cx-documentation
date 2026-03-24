---
title: "Email Limitations"
summary: "Reference listing known limitations of the Email channel connector in ExpertFlow CX, covering attachment types, email formatting, outbound restrictions, Exchange polling behaviour, and alias handling."

product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["Email limitations", "email connector known issues", "email attachment types", "email formatting", "Exchange email limitations", "email alias limitations"]
aliases: ["email connector limitations", "email known issues", "CX email limitations"]
last-updated: 2026-03-10
---

# Email Limitations

This page documents known limitations of the ExpertFlow CX Email channel connector.

## Attachment Limitations

Only attachment formats tested and confirmed to work are listed below. Other formats may or may not work.

| Direction | Supported Formats |
|---|---|
| **Agent Desk → Email** | `png`, `jpg/jpeg`, `pdf`, `doc/docx`, `ppt/pptx`, `xls/xlsx`, `txt`, `mp4`, `mp3` |
| **Email → Agent Desk** | `png`, `jpg/jpeg`, `pdf`, `doc/docx`, `ppt/pptx`, `xls/xlsx`, `txt`, `mp4`, `mp3`, `gif` |

## Email Formatting and Indentation

- Email indentation (reply and forward formatting) may not match all email clients. Gmail, MS Exchange, and other clients format quoted reply blocks differently.
- The content of emails is always 100% correct. Only the visual indentation and quote-line styling may appear slightly distorted depending on the recipient's email client.

## Outbound Email Restrictions

- Sending an outbound email to an arbitrary email address is not directly supported from the Agent Desk interface. Agents can only send a new email to a customer who is part of an **ongoing conversation session**.
- This is accessed via the Email icon in the active conversation's customer interaction panel on the Agent Desk.

## Exchange Server Polling Behaviour

For **MS Exchange (EWS) based deployments**, the connector applies a 1-minute window buffer to the polling interval:

- When polling is configured to run every X minutes, the connector retrieves emails from `(last_poll_time - 1 minute)` to `(current_time - 1 minute)` instead of the exact window.
- This buffer allows the Exchange server sufficient time to receive, process, index, and make newly arrived emails available before the query runs.
- From the customer's perspective, this has no noticeable impact. Internally it ensures no email is missed due to Exchange indexing lag.

**Example**: If the first poll runs at 00:00:00 and the interval is 5 minutes, the next poll at 00:05:00 fetches emails from 23:59:00 to 00:04:00. The subsequent poll fetches from 00:04:00 to 00:09:00, and so on.

## Email Alias Limitations

Using two different email aliases for the same underlying email address produces unexpected behaviour in Reply All:

**Scenario**: If the Service Identifier in Unified Admin is `abc@email.com` and the mailbox also receives emails sent to an alias `abc2@email.com`:
- Agents can receive emails sent to the alias.
- When the agent uses **Reply All**, the `From` address will be `abc@email.com` (the Service Identifier), but the `To`/`CC` fields will include `abc2@email.com` from the original message.
- This means agents may receive their own reply as an incoming email.

**Recommendation**: Use a single email address per channel, without aliases, to avoid Reply All inconsistencies.

## Related Articles

- [Email Channel Overview](Email-Channel-Overview.md)
- [Email Configuration — IMAP/SMTP](Email-Configuration-IMAP-SMTP.md)
- [Channel and Connector Setup](../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
