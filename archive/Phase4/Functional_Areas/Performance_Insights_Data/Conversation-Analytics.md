---
title: "Conversation Analytics"
summary: "How ExpertFlow CX uses AI and LLMs to analyze customer interactions in real time and post-contact, surfacing sentiment, summaries, compliance risks, and trends."
audience: [supervisor, admin, decision-maker]
product-area: [reporting]
doc-type: explanation
difficulty: intermediate
keywords: ["conversation analytics", "AI analytics", "sentiment analysis", "LLM", "transcription", "compliance monitoring", "trend analysis", "real-time analytics"]
aliases: ["AI analytics", "interaction analytics", "CX analytics"]
last-updated: 2026-03-10
---

# Conversation Analytics

**Conversation Analytics** applies AI and Large Language Model (LLM) technology to every customer interaction — across voice, chat, and digital channels — and transforms those conversations into structured, actionable data. Analysis runs both in real time (during a live interaction) and post-contact (after the interaction ends).

## What Conversation Analytics Produces

Every analyzed interaction generates a set of structured outputs:

| Output | Description |
|---|---|
| **Live Transcript** | A verbatim, real-time record of the conversation as it happens. |
| **Sentiment Classification** | Labels the interaction Positive, Negative, or Neutral based on language and tone. |
| **Emotion Detection** | Identifies underlying customer emotions beyond surface sentiment (frustration, satisfaction, confusion). |
| **Interaction Summary** | A concise AI-generated summary of what was discussed and resolved. |
| **Compliance Flags** | Real-time alerts when detected language suggests a compliance risk (e.g., profanity, prohibited claims). |
| **Trend Highlights** | Emerging topics and recurring issues identified across a set of conversations. |

## How It Is Used Across the Organization

Conversation Analytics outputs power different workflows depending on the audience:

### Supervisors

- Monitor live sentiment scores for active agent conversations and intervene when scores drop
- Use compliance flags to identify interactions requiring immediate attention
- Review AI-generated summaries during coaching sessions instead of replaying full recordings

### Quality Assurance Teams

- Filter the conversation pool by sentiment outlier, risk score, or topic to replace random sampling with targeted review
- Reduce time-to-evaluation by reading summaries before deciding whether to score a full interaction

### Business Leaders and Decision Makers

- Track customer sentiment trends by queue, channel, or time period
- Identify product or service issues emerging in customer language before they appear in formal feedback channels
- Use topic trend data to inform product, process, and training decisions

### Operations and Routing

- Apply real-time intent and sentiment signals to routing decisions — escalate high-frustration contacts to senior agents automatically via Conversation Studio rules

## Real-Time vs. Post-Contact Analysis

| Mode | When It Runs | Primary Use Cases |
|---|---|---|
| **Real-time** | During the live interaction | Live sentiment alerts, compliance flagging, supervisor assist |
| **Post-contact** | After the interaction ends | Summaries, trend analysis, QA filtering, historical reporting |

Both modes produce data accessible via the platform UI and API.

## Related Articles

- [Post-Conversation Analytics](Post-Conversation-Analytics.md)
- [Real-time Contact Center Analytics](Real-time-Contact-Center-Analytics.md)
- [AI Sentiment-Based Handover](../../Designer/AI-Sentiment-Based-Handover.md)
- [Monitoring Your Team in Real-Time](../../Getting_Started/Monitoring-Your-Team-in-Real-Time.md)
- [Historical Reports Reference](../../Supervisor/Historical-Reports-Reference.md)
