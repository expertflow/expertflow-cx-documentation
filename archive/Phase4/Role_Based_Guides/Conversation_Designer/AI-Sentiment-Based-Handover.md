---
title: "AI Sentiment-Based Handover"
summary: "Explanation of how AI analytics and real-time sentiment detection trigger proactive handovers from bots to human agents."
audience: [designer, ai-specialist]
product-area: [bots, analytics, studio]
doc-type: explanation
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# AI Sentiment-Based Handover

The goal of ExpertFlow AI is to prevent customer frustration by ensuring that complex or emotionally charged issues are handled by human experts. This is achieved through **Real-time Sentiment Detection.**

## 1. How It Works
The AI Analyzer component monitors every message exchanged between a customer and a virtual agent (bot).
1.  **NLP Processing:** The system analyzes the customer's text for keywords and tone that indicate frustration, anger, or urgency.
2.  **Sentiment Scoring:** Each interaction is assigned a sentiment score.
3.  **Trigger Threshold:** If the score drops below a preconfigured threshold (Negative Sentiment), the system initiates a handover.

## 2. The Proactive Handover Experience
Unlike traditional bots that require the customer to type "Agent," the ExpertFlow system is proactive.
- **The Offer:** The bot detects the negativity and automatically asks: *"I see this is frustrating. Would you like me to connect you with a human specialist who can help?"*
- **Seamless Context:** If the customer accepts, the entire transcript and the sentiment analysis are passed to the **Agent (Amy)**, so the customer doesn't have to repeat themselves.

## 3. Configuration in Studio
Conversation Designers (Dave) can customize this behavior in **Conversation Studio**:
- **Handover Node:** Insert an "AI Analytics" node within your flow to receive real-time sentiment flags.
- **Conditional Branching:** Use the `sentiment == negative` flag to route the customer to a high-priority queue.

---

*For technical details on the underlying data model, see [Conversation Life-Cycle Objects](../Developer/Conversation-Life-Cycle-Objects.md).*
