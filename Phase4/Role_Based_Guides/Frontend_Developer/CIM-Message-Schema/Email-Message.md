---
title: "Email Message"
summary: "CIM schema reference for the Email message type — used to send email content including subject, recipients, HTML body, threading, attachments, and CC/BCC fields."
audience: [developer]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["email message CIM", "CIM email schema", "email message type CX", "CIM message EMAIL", "email body CX schema", "email thread CIM", "attachment CIM message"]
aliases: ["email message CIM", "CIM EMAIL type", "email schema CX"]
last-updated: 2026-03-10
---

# Email Message

The Email message type is used to represent and send email content within the CIM framework, including full threading, HTML body, attachments, and recipient management.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | String | Yes | Must be `"EMAIL"` |
| `subject` | String | No | Email subject line. |
| `from` | String | Yes | Sender email address. |
| `replyTo` | List\<String\> | Yes | One or more reply-to email addresses. |
| `receivingDate` | Long | Yes | Unix timestamp (milliseconds) when the email was received. |
| `htmlBody` | String | No | HTML-formatted email body content. |
| `recipientsTo` | List\<String\> | No | Primary recipient email addresses. |
| `recipientsCc` | List\<String\> | No | CC recipient email addresses. |
| `recipientsBcc` | List\<String\> | No | BCC recipient email addresses. |
| `emailThreads` | List\<String\> | No | Message IDs for email thread chaining. |
| `attachments` | List\<Attachment\> | No | File attachments included in the email. |
| `additionalDetails` | JsonNode | No | Channel-specific additional metadata. |

## Related Articles

- [CIM Messages](CIM-Messages.md)
- [Email Channel Configuration Guide (IMAP/SMTP)](../../Solution_Admin/Email-IMAP-SMTP-Configuration-Guide.md)
- [Message Body](Message-Body.md)
- [Message Header](Message-Header.md)
