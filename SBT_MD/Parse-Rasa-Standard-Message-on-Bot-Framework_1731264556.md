# CX Knowledgebase : Parse Rasa Standard Message on Bot-Framework

## **Current Workflow**

The Bot-Framework component manages the message flow between the customer and the bot. It routes the bot’s response to the customer as a direct message and to the agent as a suggested response.

## **The Problem: Schema Rigidity**

Previously, the Bot-Framework strictly expected responses from Rasa to follow the CX structure (CIM-Message). If Rasa sent a response in its Standard Message Structure, the Bot-Framework would ignore it. This resulted in messages failing to reach the customer or the agent.

## **Why Standard Structure Support is Required**

We encountered specific cases where using the Rasa Standard Structure is mandatory:

  1. **RasaX UI Compatibility:** For customers using the RasaX UI, the bot must communicate in the standard structure; otherwise, messages will not render on the UI.

  2. **Customer Maintenance:** To support future clients who maintain their own Rasa instances, our framework must be compatible with Rasa’s native message format.




## **The Solution: Parser Layer implementation**

To bridge this gap, we have implemented a **Parser Layer** within the Bot-Framework.

  * **Functionality:** This layer is designed to detect and parse Rasa’s standard message format.

  * **Result:** The Bot-Framework can now process and deliver both CIM-Messages and Standard Rasa Messages seamlessly, ensuring no communication is dropped regardless of the training structure used.



