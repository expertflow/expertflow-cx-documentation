---
title: "Facebook Channel Overview"
summary: "Explanation of ExpertFlow CX Facebook channel integration — covering Direct Message and Social Media comment handling, capabilities, and what agents can do on each sub-channel."

product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["Facebook channel", "Facebook Messenger", "Facebook Direct Message", "Facebook Social Media", "Facebook comments", "Facebook integration", "digital channels"]
aliases: ["Facebook channel", "Facebook connector overview", "Facebook DM and social media"]
last-updated: 2026-03-10
---

# Facebook Channel Overview

The Facebook channel integration in ExpertFlow CX enables businesses to manage customer conversations across two distinct Facebook interaction modes — **Facebook Direct Message (DM)** and **Facebook Social Media Posts/Comments** — all from the same agent desk interface.

## Sub-Channel Types

### Facebook Direct Message

Facebook DM lets agents receive and respond to private messages sent by customers through Facebook Messenger. Each incoming message creates a conversation in the agent desk, routed through the standard queue and skills-based routing mechanism.

**Supported message types:**

| Type | Details |
|---|---|
| **Text** | UTF-8 text up to 2,000 characters |
| **Images** | `image/jpeg`, `image/png` |
| **Audio** | `audio/aac`, `audio/mp4`, `audio/amr`, `audio/mpeg`, `audio/ogg` |
| **Video** | `video/mp4`, `video/3gpp` |
| **Files** | Any valid MIME type; max 25 MB |
| **Stickers** | Receive only |
| **GIFs** | Receive only |
| **Quoted replies** | Agent can reply to a specific customer message |
| **Quick reply buttons** | Pre-defined response buttons; selection sends a reply |
| **URLs** | Rendered as clickable links |

> **Limitation**: Multiple file attachments in a single Messenger message are not supported. Only the first attachment is relayed; the remainder are dropped. This is a platform-level limitation.

### Facebook Social Media Posts/Comments

The Social Media sub-channel enables agents to monitor and respond to **public comments** on the business's Facebook page posts. Each comment from a unique customer creates a new conversation.

**Agent actions on comments:**

| Action | Description |
|---|---|
| **Reply** | Post a public reply to the comment on the Facebook page |
| **Like** | Like the comment on the Facebook page |
| **Hide / Unhide** | Hide or restore visibility of the comment from the public post |
| **Delete** | Remove the comment from the page |
| **View Full Post** | Expand the original post and all first-level comments in context |
| **Private Reply** | Send a one-time private Messenger DM to the commenter instead of replying publicly |
| **Edit** | Edit agent-posted comments (controlled by the `EDIT_MESSAGE_SUPPORT_SM` attribute; enabled by default) |

**Supported multimedia in comments:**
- Photos
- GIFs (displayed as video; playable on click)

> **Limitation**: Video comments are not supported for Social Media. Nested multimedia comments (photos, stickers, GIFs) in nested replies are not returned by the FB Graph API.

## Routing Modes

Both Facebook sub-channels support **PUSH** (queue-based routing to agents) and **PULL** (agents pick conversations from a list). Configuration is done per channel in Unified Admin.

## Prerequisites

To use either Facebook sub-channel, you need:
1. A Facebook Developer account and a configured Facebook App.
2. A Facebook Page the business administers.
3. A Long-Lived Page Access Token generated from the Facebook Graph API.
4. Facebook App permissions approved by Facebook's review team (for public content access).
5. The Facebook connector deployed in your CX environment.

For step-by-step setup, see [Facebook Configuration Guide](Facebook-Configuration-Guide.md).

## Related Articles

- [Facebook Configuration Guide](Facebook-Configuration-Guide.md)
- [Facebook Connector Limitations](Facebook-Connector-Limitations.md)
- [Channel and Connector Setup](../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
- [Handle Multi-channel Conversation](../../How-to_Guides/Agent/Accept-a-Conversation.md)
