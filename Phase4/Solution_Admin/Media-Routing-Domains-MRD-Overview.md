---
audience: [solution-admin]
doc-type: explanation
difficulty: beginner
aliases: []
---

# Media Routing Domains (MRD)

A **Media Routing Domain (MRD)**, also known as a Channel Category, organizes requests from different communication mediums (e.g., Voice, Chat) and manages independent agent states for each.

## How MRDs Work
MRDs allow agents to manage their availability separately for different channels. For example, an agent can be **READY** for the Chat MRD while remaining **NOT_READY** for the Voice MRD.

### Example Structure
- **Chat MRD**: Groups channels like WhatsApp, Facebook, and Web Chat.
- **Voice MRD**: Handles telephony and WebRTC calls.

## Key Configuration Fields

| Field | Description |
| :--- | :--- |
| **Name** | Identifier for the domain (e.g., "Chat", "Voice"). |
| **Max Task Request** | The maximum number of concurrent tasks an agent can handle in this domain. |
| **Interruptible** | (Future use) Defines if a conversation can be interrupted by a higher-priority one (e.g., a voice call interrupting a chat). |

## Associations
- **Channel Type**: Every channel type (e.g., WhatsApp) is linked to one MRD.
- **Routing Queue**: Queues are associated with an MRD, ensuring that tasks are only routed to agents who are in a "Ready" state for that specific domain.

For more on how MRDs link to other objects, see [Media Channels](../Developer/Conversation-Life-Cycle-Objects.md).
