---
title: "Message Schema Interoperability: Rasa and CIM"
summary: "Technical explanation of the Bot-Framework Parser Layer, enabling seamless communication between Rasa Standard and ExpertFlow CIM schemas."
audience: [conversation-designer]
product-area: [bots, sdk]
doc-type: explanation
difficulty: advanced
last-updated: 2026-03-11
---

# Message Schema Interoperability: Rasa and CIM

ExpertFlow CX provides a flexible communication layer that allows the platform to interact with multiple message schemas simultaneously. This is primarily handled by the **Parser Layer** within the Bot-Framework, ensuring that external AI engines can communicate with the CX platform without proprietary formatting constraints.

## 1. Parser Layer Architecture
The Parser Layer acts as a middleware between the **ExpertFlow Bot Connector** and the **NLU Engine (Rasa)**. 

### **The Translation Workflow:**
1.  **Ingress:** The Bot Connector receives a response from the Rasa API.
2.  **Detection:** The Parser detects if the payload is in **Rasa Standard** or **ExpertFlow CIM** format.
3.  **Transformation:** If Rasa Standard is detected, the Parser maps the Rasa keys (e.g., `text`, `buttons`, `image`) to their corresponding CIM attributes.
4.  **Egress:** The normalized CIM event is forwarded to the `conversation-manager`.

---

## 2. Schema Comparison Table
The following table illustrates how the Parser Layer maps common interaction elements:

| Interaction Element | Rasa Standard Key | ExpertFlow CIM Equivalent |
| :--- | :--- | :--- |
| **Plain Text** | `text: "Hello"` | `body.type: "PLAIN"`, `body.markdownText: "Hello"` |
| **Quick Replies** | `buttons: [...]` | `body.type: "BUTTON"`, `body.buttons: [...]` |
| **Media/Images** | `image: "url"` | `body.type: "MEDIA"`, `body.attachment.mediaUrl: "url"` |
| **Custom Data** | `custom: {...}` | `header.customAttributes: {...}` |

---

## 3. Supported Engines & UI Compatibility
The Parser Layer is designed to support various deployment scenarios:

*   **RasaX UI Compatibility:** Enables bots to communicate in the Rasa standard structure required for rendering within the RasaX training interface, while maintaining full compatibility with the ExpertFlow Agent Desk.
*   **Standalone Rasa Instances:** Provides seamless integration for customers who maintain their own external Rasa clusters or utilize pre-existing Rasa models.
*   **Vendor Agnostic Design:** The architecture allows for the future addition of other NLU engines (e.g., Dialogflow, Lex) by simply adding a new mapping profile to the Parser Layer.

---

## 4. Operational Benefits
- **Zero-Drop Messaging:** Ensures no communication is ignored due to format mismatches.
- **Developer Efficiency:** Specialists can train bots using standard Rasa documentation without learning proprietary ExpertFlow schemas.
- **Hybrid Support:** Allows for a mix of CIM-native and Rasa-native bots within the same multi-tenant environment.

---

## Related Guides
*   [CIM Message Schema Master](../../Reference/Schemas_and_Data_Model/CIM_Message_Schema/CIM-Messages.md)
*   [RASA-X Deployment Guide](../Hosting_Partner/RASA-X-Deployment.md)
*   [Custom Bot Connector Development](../Developer_Integrator/Custom-Bot-Connector-Development.md)
