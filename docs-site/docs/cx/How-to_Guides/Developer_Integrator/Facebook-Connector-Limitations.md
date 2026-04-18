---
title: "Facebook Connector Limitations"
summary: "Known limitations of the ExpertFlow CX Facebook connector — covering Graph API restrictions for nested comments, video comments, profile photos, GIFs, highlighted text, emoji support, and menu buttons."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["facebook connector limitations CX", "facebook CX limitations", "facebook graph API limitations", "facebook DM limitations CX", "facebook comment limitations CX", "facebook emoji CX", "facebook GIF CX"]
aliases: ["facebook limitations CX", "facebook connector known issues CX"]
last-updated: 2026-03-10
---

# Facebook Connector Limitations

The following limitations apply to the ExpertFlow CX Facebook connector for both Page Comments and Messenger Direct Messages.

## Known Limitations

1. **Nested comments with media** — Nested comments containing photos, videos, stickers, and GIFs are not always returned by the Facebook Graph API (used for the **View Full Post** feature). Only their text captions are returned in these cases.

2. **Video comments limited to page admin posts** — The Facebook Graph API currently returns first-level video comments only when posted by the page admin. Comments from other users on videos are not returned.

3. **No profile photos in comments** — The Facebook Graph API does not return the profile photos of users commenting on posts. Profile images are not displayed on Agent Desk for comment interactions.

4. **Some GIFs may not appear** — For single Facebook comments, some GIFs will not appear on the agent desk due to a broken payload returned from the Facebook API.

5. **No page context for single comments** — When a single comment arrives on the agent's desk, the source Facebook Page is not shown because the payload does not include Facebook page information.

6. **Highlighted text not supported on Facebook DM** — Text formatting using highlight is not supported in the Messenger Direct Message channel.

7. **Emojis not supported on Agent Desk** — Emojis sent via Facebook are not displayed on Agent Desk.

8. **Menu buttons not supported** — Interactive menu buttons (e.g., persistent menu) are not supported by the connector.

## Related Articles

- [Facebook Channel Configuration Guide](../Administrator/Facebook-Configuration-Guide.md)
- [Channel and Connector Setup](../Administrator/Channel-and-Connector-Setup.md)
- [Instagram Connector Configuration Guide](../Administrator/Instagram-Connector-Configuration-Guide.md)
