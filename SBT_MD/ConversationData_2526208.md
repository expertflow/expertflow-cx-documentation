# CX Knowledgebase : ConversationData

Conversation Data is managed via [**Conversation Control APIs**.](https://api.expertflow.com/#a3f55c68-437e-4b66-946d-4083866709be) It consists of **Attribute** objects , where each Attribute has the following fields.

**Filed Name**| **Data Type**  
---|---  
key| String  
value| Object  
type| ValueType (Enum), which includes:

  * `Alphanum100`
  * `AlphanumSpecial200`
  * `String2000`
  * `String50`
  * `String100`
  * `PositiveNumber`
  * `IP`
  * `Number`
  * `PhoneNumber`
  * `URL`
  * `Boolean`
  * `Email`
  * `Password`
  * `StringList`

  
  
## Use Cases for ConversationData

Conversation Data is useful for providing agents with real-time context and for reporting. Some key usecases include:

  * **Authentication Status:** Setting a customer's authentication status via an IVR or a bot.

  * **Customer Journey:** Setting a customer journey trail on an IVR application or a web-app so the agent knows the customer's history.

  * **Intent for Routing:** Setting a customer's intent for agent selection via a Conversation bot.

  * **Agent Assistance:** Setting a **URL** in the conversation via a bot to assist the agent in better handling the customer.

  * **Post-Conversation Data:** Storing an agent's wrap-up , a survey score , or any filled form.




## Visibility and Reporting

Conversation Data is visible to agents and available for reporting:

  * **Real-time Agent View:** Agents handling a conversation can see the real-time information passed into the ConversationData on Agent Desk.

**Reporting:** Conversation Data is part of the **Conversation object** for all kinds of **historical and real-time reports**




  

