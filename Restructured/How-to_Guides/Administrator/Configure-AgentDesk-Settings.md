---
title: "Configure AgentDesk Settings"
summary: "Reference for the AgentDesk Settings configuration in ExpertFlow CX Unified Admin — covering message formatting, file sharing, emoji support, auto-answer, conversation participants, active sessions data, outbound SMS, and pause conversation timer options."
audience: [administrator]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["agentdesk settings CX", "configure agent desk CX", "message formatting CX", "file sharing agent CX", "auto answer agent CX", "outbound SMS agent CX", "pause conversation timer CX", "agent desk admin settings"]
aliases: ["agentdesk config CX", "agent desk settings CX", "configure agent features CX"]
last-updated: 2026-03-10
---

# Configure AgentDesk Settings

The **AgentDesk Settings** section in Unified Admin lets administrators control which features are available to agents in Agent Desk — such as message formatting, file sharing, auto-answer, and pause conversation options.

## Settings Reference

| Setting | Description |
|---|---|
| **Message Formatting** | When enabled, agents can send formatted messages (bold, italic, lists, etc.) in conversations. |
| **File Sharing** | When enabled, agents can share and receive file attachments during conversations. |
| **Emoji** | When enabled, agents can send and receive emojis in conversation messages. |
| **Auto Answer** | When enabled, new incoming conversation requests are automatically accepted — agents do not see an incoming notification. **Not applicable to Cisco voice calls.** |
| **Conversation Participants** | When enabled, agents can see the list of all participants currently in a conversation. |
| **Show Active Sessions Data** | When enabled, agents can view active session data in the **Customer Info** panel on Agent Desk while handling a conversation. (Formerly called "Active Channels" — renamed to Active Sessions.) |
| **Outbound SMS** | When enabled, agents can send outbound SMS messages to a customer independently of an active conversation. |
| **Pause Conversation** | Configures the timer options displayed to agents when pausing a conversation. Only the pause duration options selected here will appear in the agent's pause menu. |

## Notes

- Settings apply globally to all agents in the configured scope — they cannot be set per-agent from this panel.
- **Auto Answer** does not apply to Cisco voice calls. Cisco voice calls follow Cisco's own call acceptance mechanism.
- Enabling **Outbound SMS** requires the SMS channel (Twilio or SMPP) to be configured and active.

## Related Articles

- [Channel and Connector Setup](Channel-and-Connector-Setup.md)
- [Configuring Wrap-up Forms](Configuring-Wrap-up-Forms.md)
- [Configuring Reason Codes](Configuring-Reason-Codes.md)
- [Pause-Resume Conversation](../Agent/Pause-Resume-Conversation.md)
