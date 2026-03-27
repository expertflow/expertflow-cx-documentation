---
title: "Conversation Studio Fundamentals"
summary: "Introduction to the low-code design environment for building inbound and outbound interaction flows."
audience: [conversation-designer]
product-area: [ivr, studio]
doc-type: explanation
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Conversation Studio Fundamentals

Conversation Studio is the low-code, event-driven authoring environment for ExpertFlow CX. It allows Conversation Designers (Dave) to build complex logical flows for IVR, Chatbots, and Outbound campaigns using a visual, node-based interface.

## 1. The Design Environment
Conversation Studio is powered by Node-RED and is accessible via your platform FQDN:
`https://<FQDN>/conversation-studio`

### Key User Roles:
- **Authoring:** Requires the `conversation-studio-admin` role in Keycloak.
- **Viewing:** Read-only access for auditing existing logic.

## 2. Core Building Blocks
Logic in Conversation Studio is organized into **Flows** and **Nodes**.

- **Flows:** A collection of nodes that define a specific business process (e.g., "Main Inbound Greeting").
- **Nodes:** Individual logical blocks that perform actions (e.g., "Transfer to Queue", "Send Message", "Request API").
- **Events:** Flows are triggered by platform events, such as `Participant Role Changed` or `New Message Received`.

## 3. Designing Post-Interaction Surveys (CX 5.0+)
As of release 5.0, surveys are managed via a dedicated **Survey Message** node.

### How it works:
1.  The node retrieves survey forms pre-configured in **Unified Admin**.
2.  The Designer selects the desired form from a dropdown menu.
3.  Upon deployment, the system automatically triggers the survey message when the interaction meets the flow's criteria (e.g., when the agent leaves).

**Important:** The dedicated Survey Message node replaces the legacy "Evaluation" function node used in older versions.

## 4. Authoring Best Practices
1.  **Modular Design:** Break large logic chains into sub-flows to improve maintainability.
2.  **Version Control:** Always comment on your changes before hitting **Deploy** to maintain a clear audit trail.
3.  **DNC Validation:** For outbound flows, ensure a DNC (Do Not Call) check is performed early in the sequence.

---

*Ready to build? Follow the [Creating Your First Simple Flow](Conversation-Studio-Configuration-Guide.md) tutorial or explore the [Full Studio Node Library](../../Reference/Archive-Notice.md).*
