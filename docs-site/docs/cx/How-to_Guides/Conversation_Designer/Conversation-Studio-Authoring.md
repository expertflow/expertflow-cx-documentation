---
title: "Authoring in Conversation Studio"
summary: "Practical guidance for designing flows in Conversation Studio, including surveys and authoring best practices."
audience: [conversation-designer]
product-area: [ivr, studio]
doc-type: how-to
difficulty: intermediate
aliases: []
last-updated: 2026-03-30
---

# Authoring in Conversation Studio

## Designing Post-Interaction Surveys (CX 5.0+)

Surveys are managed via a dedicated **Survey Message** node.

1. The node retrieves survey forms pre-configured in **Unified Admin**.
2. Select the desired form from the dropdown menu in the node's properties.
3. On deployment, the system automatically triggers the survey when the interaction meets the flow's criteria (e.g., when the agent leaves).

**Note:** The Survey Message node replaces the legacy "Evaluation" function node used in older versions.

## Authoring Best Practices

1. **Modular design** — break large logic chains into sub-flows to improve maintainability.
2. **Version control** — always add a comment before hitting **Deploy** to maintain a clear audit trail.
3. **DNC validation** — for outbound flows, perform a DNC (Do Not Call) check early in the sequence.
