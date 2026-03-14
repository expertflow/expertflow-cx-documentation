---
audience: [solution-admin]
doc-type: reference
difficulty: beginner
aliases: []
---

# YouTube Connector Limitations & Highlights

This document covers the current functional constraints for the YouTube Connector in Expertflow CX.

## Key Limitations

1. **Top-Level Comments**: Agents cannot add new top-level comments from the CX interface.
2. **Engagement Actions**: Agents cannot like, hide, or pin comments via the connector.
3. **Reply Depth**: Only top-level comments and their first-level replies are supported. Third-level replies are flattened and shown at the same level as first-level replies.
4. **Attachments**: Media messages (images/videos) within comments are not supported.

For detailed setup and API permissions, refer to the [YouTube Connector section](../Developer/YouTube-Integration-Configuration-Developer.md) in the Expertflow CX documentation. For technical constraints, see the "Comments" section in the [YouTube Data API Documentation](https://developers.google.com/youtube/v3/docs).
