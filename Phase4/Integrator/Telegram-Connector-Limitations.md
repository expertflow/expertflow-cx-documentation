---
title: "Telegram Connector Limitations"
summary: "Known limitations of the ExpertFlow CX Telegram connector — covering delivery notifications, typing indicators, media file handling, quoted replies, emoji support, and audio navigation."
audience: [integrator, solution-admin, agent]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["telegram connector limitations CX", "telegram CX limitations", "telegram delivery notification CX", "telegram typing indicator CX", "telegram emoji CX", "telegram media CX", "telegram quoted reply CX"]
aliases: ["telegram limitations CX", "telegram connector known issues CX"]
last-updated: 2026-03-10
---

# Telegram Connector Limitations

The following limitations apply to the ExpertFlow CX Telegram connector.

## Known Limitations

1. **No delivery notifications** — The Telegram connector does not support message delivery notifications.

2. **One-way typing indicator** — Customers can see the agent typing indicator. Agents cannot see when customers are typing — the Telegram API does not provide this information.

3. **Files sent as file type display incorrectly** — When images, videos, and audio are sent from Telegram as files (rather than native media), they do not display correctly on Agent Desk.

4. **No quoted reply** — Agents cannot use the quoted reply feature when the customer is on Telegram.

5. **No emoji support on Agent Desk** — Emojis sent from Telegram are not displayed on Agent Desk.

6. **Unsupported media formats** — Some media file formats sent from Telegram are not supported on Agent Desk. Affected formats include `mp3`, `jpeg`, and `rtf`. See [Telegram Connector Media Types Support](Telegram-Connector-Media-Types-Support.md) for the full compatibility matrix.

7. **Audio navigation not supported** — Agents cannot seek or navigate (fast-forward/rewind) through audio files received from Telegram on Agent Desk.

## Related Articles

- [Telegram Connector Configuration Guide](Telegram-Connector-Configuration-Guide.md)
- [Telegram Connector Media Types Support](Telegram-Connector-Media-Types-Support.md)
- [Channel and Connector Setup](../Solution_Admin/Channel-and-Connector-Setup.md)
