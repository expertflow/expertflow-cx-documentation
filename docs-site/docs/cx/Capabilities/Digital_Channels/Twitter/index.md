---
title: "Twitter Channel Overview"
sidebar_label: "Twitter"
summary: "Explanation of the Twitter social media channel in ExpertFlow CX — covering supported agent actions, operational behaviour, media upload limits, and pull-mode polling."

product-area: [channels, digital]
doc-type: explanation
audience: [agent, administrator]
difficulty: beginner
keywords: ["Twitter channel", "Twitter connector", "Twitter integration", "Twitter CX", "Twitter pull mode", "social media channel", "tweet reply", "hide comment Twitter"]
aliases: ["Twitter connector overview", "CX Twitter channel", "Twitter social media"]
last-updated: 2026-03-10
---

# Twitter Channel Overview

The Twitter connector in ExpertFlow CX enables agents to manage and respond to public Twitter interactions — replies, mentions, and comments — directly from the Agent Desk. The connector operates in **PULL mode**, periodically polling the Twitter API to fetch new messages at configured intervals.

## Supported Agent Actions

| Action | Description |
|---|---|
| **Reply to comment** | Agents reply to tweets and comments as public Twitter replies, visible to all Twitter users. |
| **Hide comment** | Agents can hide a comment from the CX interface. Hidden comments remain visible to the agent but are no longer publicly visible on Twitter. |
| **Like comment** | Agents can like a tweet or comment. The like is reflected on the corresponding post in the Twitter feed. |
| **View full post** | Agents can view the original tweet and recently associated replies. Posts containing media display a link to the Twitter post rather than embedding the media directly. |

## Operational Behaviour

The Twitter connector uses **PULL mode** exclusively:

- The connector polls Twitter's API at scheduled intervals to fetch new tweets, replies, and mentions.
- Message retrieval is subject to Twitter API rate limits and the configured polling interval.
- Once fetched, messages appear as new interaction requests in the Agent Desk queue.

There is no real-time webhook push mode for the Twitter channel. All interaction delivery depends on the polling schedule.

## Media Upload Limits

| Media Type | Limit |
|---|---|
| Images | 5 MB per image |
| GIFs | 15 MB per GIF |
| Videos | 25 MB (Twitter API allows 512 MB; CX limits to 25 MB) |

> **Note**: Twitter supports multiple media items per tweet, but the current CX implementation processes **one attachment per message** due to CIMMessage structure constraints.

## Key Characteristics

- **Interaction model**: Public only. All replies sent through the Agent Desk appear as public Twitter replies — there is no private direct message (DM) channel in the current implementation.
- **Visibility**: Hidden comments are not deleted from Twitter; they are suppressed from the public view while remaining accessible to the page admin.
- **API version**: The connector uses Twitter API v2.

## Related Articles

- [Routing Strategy: Pull Mode](../../../How-to_Guides/Administrator/Routing-Strategy-Pull-Mode.md)
- [Twitter Configuration Guide](../../../How-to_Guides/Administrator/Twitter-Configuration-Guide.md)
- [Twitter Connector Limitations](../../../How-to_Guides/Administrator/Twitter-Connector-Limitations.md)
- [Channel and Connector Setup](../../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
