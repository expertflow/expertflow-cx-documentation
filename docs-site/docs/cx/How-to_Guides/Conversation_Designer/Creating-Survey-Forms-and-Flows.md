---
title: "Creating Survey Forms and Flows"
summary: "Guide for Conversation Designers to build customer feedback surveys and trigger them within interaction flows."
audience: [conversation-designer]
product-area: [surveys, studio, form-builder]
doc-type: how-to
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Creating Survey Forms and Flows

As a Conversation Designer (Dave), you can collect valuable customer sentiment by building post-interaction surveys. This process involves two steps: designing the form and deploying it within a flow.

## 1. Designing the Survey Form
Surveys are created in the **Unified Admin > Forms** module.
1.  Click **+ New Form** to enter the Form Builder.
2.  **Add Question Types:** Choose from NPS (Net Promoter Score), 5-Star Ratings, or MCQs.
3.  **Validate:** Ensure your question logic is sound. For more form options, see the [Form Builder Schema Reference](Creating-Survey-Forms-and-Flows.md).

## 2. Triggering the Survey in a Flow
Once your form is saved, you must tell the system when to show it to the customer using **Conversation Studio**.
1.  Open the desired control flow in Conversation Studio.
2.  Insert the **Survey Message Node** at the point where you want the feedback to be collected (e.g., after the agent leaves the conversation).
3.  **Configure Node:** Select your pre-built survey form from the dropdown menu.
4.  **Deploy:** Hit the **Deploy** button to make the survey live.

## 3. Platform Limitations
- **Concurrency:** By default, the system supports only one active survey per interaction. 
- **Data Persistence:** In the event of a server crash, incomplete survey responses (hash-map data) will be lost and cannot be recovered.

---

*Need to configure specialized bot interactions before the survey? See [Registering Bot Connectors](Registering-Bot-Connectors.md).*
