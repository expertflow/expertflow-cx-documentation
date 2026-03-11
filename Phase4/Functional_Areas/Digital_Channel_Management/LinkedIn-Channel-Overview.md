---
title: "LinkedIn Channel Overview"
summary: "Explanation of the LinkedIn channel integration in ExpertFlow CX — covering Social Media comment handling, agent capabilities, supported multimedia, and known limitations."
audience: [solution-admin, supervisor, agent]
product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["LinkedIn channel", "LinkedIn integration", "LinkedIn social media", "LinkedIn comments", "LinkedIn connector", "digital channels"]
aliases: ["LinkedIn channel overview", "LinkedIn connector", "LinkedIn for CX"]
last-updated: 2026-03-10
---

# LinkedIn Channel Overview

The LinkedIn channel integration in ExpertFlow CX enables businesses to manage public comments on their company LinkedIn page posts — all from the same agent desk interface used for other digital channels.

## How It Works

The integration connects to the LinkedIn Community Management API via a LinkedIn App. When a customer posts a comment on a company LinkedIn page post:
1. The comment is received by the CX LinkedIn Connector.
2. A new conversation is created in the platform, associated with the customer's LinkedIn name (if public).
3. The conversation is routed to an available agent.
4. The agent responds through the Agent Desk; the reply is posted publicly on LinkedIn.

## Current Integration Scope

| Sub-Channel | Status |
|---|---|
| **Social Media Posts/Comments** | Supported |
| **LinkedIn Direct Message (DM)** | Not available in this version |

## Agent Capabilities

Once an agent accepts a LinkedIn comment request, they can perform the following actions:

| Action | Description |
|---|---|
| **Reply** | Post a public reply to the comment on the company's LinkedIn page |
| **Edit comment** | Edit the agent's own comment (plain text only; available from version 4.10.1+) |
| **Like** | Like the customer's comment on LinkedIn |
| **Delete** | Delete the agent's comment from LinkedIn |
| **View Full Post** | View the original LinkedIn post and all first-level comments in context |

### View Full Post

The View Full Post panel displays the LinkedIn post with its comments, supporting:
- Single and multi-image posts
- Video posts
- Text posts with first-level comments

## Supported Multimedia Comments

| Media Type | Support |
|---|---|
| Images | Yes |
| Videos | Yes |
| Polls | No |
| Documents | No |

## Routing and Channel Mode

The LinkedIn channel supports both **PUSH** (queue routing) and **PULL** (agent-selected from a list) routing modes. Configure in Unified Admin during channel setup.

## Known Limitations

| Limitation | Detail |
|---|---|
| **No Direct Messages** | LinkedIn DM is not available in the current connector version. |
| **Multimedia limited** | Only images and videos are supported. Polls and documents are not supported in View Full Post. |
| **User profile photos** | The LinkedIn user's profile photo is not shown on the Agent Desk. |
| **Anonymous customers** | If a LinkedIn user has a private profile, their name is not shown — the conversation appears anonymous. |
| **Cannot unlike** | Once an agent likes a comment, it cannot be unliked. |
| **Reactions** | Only the "Like" reaction is supported. Other reaction types are not available. |
| **Delete from LinkedIn directly** | Do not delete comments directly from the LinkedIn admin panel — always delete from the Agent Desk to maintain data consistency. |
| **Tagging** | Agents cannot tag customers from the Agent Desk. |

## Related Articles

- [LinkedIn Account Onboarding](LinkedIn-Account-Onboarding.md)
- [LinkedIn Configuration Guide](LinkedIn-Configuration-Guide.md)
- [Channel and Connector Setup](../../Solution_Admin/Channel-and-Connector-Setup.md)
