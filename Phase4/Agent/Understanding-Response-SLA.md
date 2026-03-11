---
title: "Understanding Response SLA"
summary: "Explanation of how the Agent Response Time (SLA) works to ensure prompt customer service across digital channels."
audience: [agent]
product-area: [agent-desk]
doc-type: explanation
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Understanding Response SLA

As an Agent (Amy), your **Agent Response Time** is a key performance metric that tracks how quickly you respond to customer messages. This SLA (Service Level Agreement) ensures that customers are not left waiting for a reply.

## 1. How the SLA Timer Works
When a customer sends a message, a countdown timer starts on top of your **Message Composer**.
- **Visual Feedback:** The timer changes color based on the time left to respond. 
- **The Trigger:** The timer only starts when a customer sends a message and there is no active voice call session.
- **The Reset:** The timer stops and resets as soon as you send a reply to the customer.

### Multi-Agent Conversations:
The SLA is at the **conversation level**, not per agent.
- **Team Effort:** If multiple agents are in a chat, any response from a primary agent will reset the timer for everyone.
- **Consequences:** If the timer expires in a multi-agent chat, the system may remove all agents and reroute the conversation back to the queue.

## 2. SLA Thresholds & Actions
Your administrator (Olivia) can configure what happens when the timer reaches certain thresholds.

| Threshold | Visual Color | Action Taken |
| :--- | :--- | :--- |
| **0%** | Green | Timer starts. |
| **50%** | Yellow | Visual warning (Change Color). |
| **75%** | Red | Urgent warning (Change Color). |
| **100%** | - | **Reroute:** All agents are removed and the conversation is returned to the queue. |

## 3. The Warning Popup
In some cases, the system may show a **Warning Popup** before the timer expires.
- **Decision:** You must choose to "Stay in Conversation" to reset the timer.
- **Default:** If you do not respond to the popup, the system will automatically unsubscribe you from the conversation.

### Pro-Tips for Amy:
- **Conversation Hold:** If you place a conversation on hold, the SLA timer stops and will reset only when the conversation is resumed. 
- **Voice Calls:** The Response SLA is typically disabled for voice channels, as voice interactions are handled in real-time.

---

*To see how your response times impact your performance, check your [Agent Performance Dashboard](../Supervisor/Agent-Performance-Dashboard-Reference.md).*
