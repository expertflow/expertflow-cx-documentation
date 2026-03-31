---
audience: [solution-admin]
doc-type: reference
difficulty: beginner
aliases: []
---

# Twitter Connector Limitations & Highlights

The Twitter connector in Expertflow CX allows for managing public social interactions. However, it has specific constraints compared to other digital channels.

## Key Limitations

### 1. Bot Responses
The Twitter connector **does not support automated bot responses**. While bot replies may appear in the Agent Desk for internal tracking, they are not forwarded to Twitter as public comments or DMs.

### 2. Direct Messaging (DM)
- Twitter DMs are **not supported**.
- Only public comments and social posts are captured and processed.

### 3. Media Handling
- **View Full Post**: Posts containing media do not show the image/video in the "Full Post" view; a link to the original tweet is provided instead.
- **Comment Media**: Media within comments *is* displayed properly.
- **Single Attachment**: Although Twitter supports multiple images per tweet, Expertflow CX only displays **one** media file per comment due to current message structure limits.

## Technical Constraints
- **Image Size**: Max 5 MB.
- **GIF Size**: Max 15 MB.
- **Video Size**: Max 25 MB for uploads (Twitter supports up to 512 MB, but the connector is limited).
- **Channel Mode**: Operates in **PULL MODE**, fetching updates periodically.
