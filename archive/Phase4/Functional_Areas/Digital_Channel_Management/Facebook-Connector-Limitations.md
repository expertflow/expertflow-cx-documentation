---
title: "Facebook Connector Limitations"
summary: "Reference listing known limitations of the Facebook connector in ExpertFlow CX, covering Graph API constraints, unsupported features for DM and social media comments."
audience: [solution-admin, agent, supervisor]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["Facebook connector limitations", "Facebook known issues", "Facebook DM limitations", "Facebook social media limitations", "Facebook Graph API"]
aliases: ["Facebook limitations", "Facebook connector known issues"]
last-updated: 2026-03-10
---

# Facebook Connector Limitations

This page documents known limitations of the ExpertFlow CX Facebook connector across both Direct Message (DM) and Social Media (Comments) sub-channels.

## Graph API Limitations

| Limitation | Detail |
|---|---|
| **Nested multimedia comments** | Nested comments containing photos, videos, stickers, and GIFs are not consistently returned by the FB Graph API. Only the text caption of such comments is returned. |
| **First-level video comments only** | The FB Graph API returns only first-level video comments posted by the page admin. Comments from public users are not returned for video. |
| **Profile photos** | The FB Graph API does not return the profile photo of users commenting on posts. Agent desk shows no avatar for comment authors. |
| **Single comment GIFs** | Some GIFs sent as a single comment will not appear on the agent desk due to a broken payload returned from Facebook. |
| **Comment page source** | When a single comment arrives, the platform cannot determine which Facebook page or post it was posted on because the payload does not include that information. |

## Direct Message (DM) Limitations

| Limitation | Detail |
|---|---|
| **Multiple file attachments** | Only the first file attachment is relayed when a customer sends multiple files in a single Messenger message. The remaining attachments are dropped. This is a combined limitation of the File Engine and CCM API. |
| **Highlighted text** | Highlighted (formatted) text is not supported in Facebook DM. |
| **Emojis** | Emojis are not supported in the agent desk interface for Facebook DM. |
| **Menu buttons** | Interactive menu buttons are not supported. |

## Social Media (Comments) Limitations

| Limitation | Detail |
|---|---|
| **Video comments** | Public video comments on posts are not supported. |
| **Nested multimedia** | Nested comments containing multimedia (photos, stickers, GIFs) are not supported in the View Full Post view. |
| **Profile photos in Full View** | The commenter's profile photo is not shown in the Full View Post panel. |

## Related Articles

- [Facebook Channel Overview](Facebook-Channel-Overview.md)
- [Facebook Configuration Guide](../../Solution_Admin/Facebook-Configuration-Guide.md)
- [Channel and Connector Setup](../../Solution_Admin/Channel-and-Connector-Setup.md)
