---
title: "Browser and Sound Notifications"
summary: "Explanation of browser and sound notifications in ExpertFlow CX Agent Desk — how to enable browser notifications and understand alert behaviour for incoming interactions."
audience: [agent, supervisor]
product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["browser notifications", "sound notifications agent desk", "CX notifications", "agent desktop alerts", "enable notifications CX", "incoming chat alert"]
aliases: ["enable browser alerts", "agent desk notifications", "CX sound alert"]
last-updated: 2026-03-10
---

# Browser and Sound Notifications

ExpertFlow CX Agent Desk uses browser notifications and sound alerts to notify agents and supervisors of incoming interactions and key events — even when the Agent Desk tab is not in focus.

## Enabling Browser Notifications

Browser notifications must be explicitly permitted in the browser for the Agent Desk origin.

1. Open the Agent Desk in your browser.
2. Click the **lock icon** (or site information icon) in the browser's address bar.
3. Find the **Notifications** permission setting.
4. Set it to **Allow**.
5. Reload the Agent Desk.

Once enabled, the browser will display pop-up notifications for new incoming interactions when the Agent Desk tab is not the active tab.

> **Note**: Browser notification permissions are stored per browser and per device. If an agent uses multiple browsers or machines, notifications must be enabled on each.

## Sound Alerts

Agent Desk plays an audio alert when new interaction requests arrive. Sound alerts work independently of browser notification permissions but require the browser tab to be open.

- For the **Hand Raise** feature, a sound alert plays once when a supervisor receives a hand raise request. The sound stops when all active hand raise notifications are cleared or dismissed.

## Troubleshooting Notifications

| Issue | Resolution |
|---|---|
| No browser pop-ups for new chats | Check the browser's notification permission for the Agent Desk URL — set to **Allow** |
| Permission prompt never appeared | Some browsers suppress the permission prompt if the site is accessed over HTTP (not HTTPS) |
| Notifications appear but no sound | Check your OS-level notification sound settings and browser audio permissions |

## Related Articles

- [Agent Hand Raise](Agent-Hand-Raise.md)
- [Accept a Conversation](../../Agent/Accept-a-Conversation.md)
- [Managing Your Presence and States](../../Agent/Managing-Your-Presence-and-States.md)
