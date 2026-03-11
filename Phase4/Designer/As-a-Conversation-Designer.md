---
title: "As a Conversation Designer"
summary: "Introduction to the Conversation Designer role in ExpertFlow CX — covering access to Unified Admin, creating forms and surveys using the Form Builder, inserting a Survey Message node in Conversation Studio, and known survey limitations."
audience: [designer]
product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["conversation designer CX", "Unified Admin designer CX", "form builder CX", "survey CX conversation studio", "conversation designer role CX"]
aliases: ["designer role CX", "conversation designer overview CX"]
last-updated: 2026-03-10
---

# As a Conversation Designer

As a Conversation Designer in ExpertFlow CX, your primary workspace is **Unified Admin** and **Conversation Studio**. You design the flows and forms that determine how customers interact with automated bots and agents.

---

## Accessing Unified Admin

Log in to Unified Admin using your administrator credentials. After logging in, the dashboard provides access to the main solution areas, including **Forms**, **Surveys**, **Campaigns**, and more.

---

## Creating a Form

Forms define the structure of customer surveys and evaluation questions.

1. From the dashboard, click **Forms**.
2. Click **+ New Form** to open the Form Builder.
3. Add question blocks — supported types include NPS, multiple choice (MCQ), 5-Star rating, and others.

For a full reference on question types, weightage, and form structure, see [Form Builder User Guide](../Solution_Admin/Form-Builder-User-Guide.md).

---

## Adding a Survey to a Conversation Flow

Surveys are triggered within a Conversation Studio flow using the **Message Survey** node.

1. Open the relevant conversation flow in Conversation Studio.
2. Insert a **Message Survey** node at the point in the flow where you want the survey to run (e.g., at the end of a conversation).
3. Configure the node to reference the form you created.
4. Click **Deploy** to activate the flow with the survey.

---

## Known Survey Limitations

- By default, the system supports only **one active survey at a time**.
- If the server crashes, all in-memory hash-map data is lost and the form becomes inaccessible until the system recovers.

---

## Related Articles

- [Form Builder User Guide](../Solution_Admin/Form-Builder-User-Guide.md)
- [Creating Survey Forms and Flows](Creating-Survey-Forms-and-Flows.md)
- [Conversation Flow for Outbound Dialing Modes](Conversation-Flow-for-Outbound-Dialing-Modes.md)
- [Outbound Flows Limitations](Outbound-Flows-Limitations.md)
