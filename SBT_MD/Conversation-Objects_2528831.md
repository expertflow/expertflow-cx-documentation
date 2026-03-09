# CX Knowledgebase : Conversation Objects

Expertflow CX is a contact center conversation platform where customers interact with business through a media channel. Different actors such as contact center agents, conversation bots, or third party apps may participate in a conversation in any of the following Conversation Participant roles.

### **Customer**

|  A user of any of the supported [Customer Channels](Omnichannel-Engagement_2529366.html) communicating as a Customer. The user is identified as a Customer following [Customer Identification](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2525785/Customer+Identification). All customer conversations are stored in a [Room](Room_64356457.html).   
---|---  
  
### **Conversation Bot**

|  A 3rd party application acting as a Conversation Bot connects via the bot framework and provides customer self-services such as Conversational IVR, bot messages. The Conversation Bot acts as an assistant to participating contact center agents.Expertflow supports Rasa, Amazon Lex out-of-the-box.  
  
### **Agent**

|  One or more participants acting as a contact center agent serving on behalf of the business responding to customer queries or engaged in an outbound conversation with customers.  
  
### **App**

|  An app interface for API based access to conversation.  
  
### **Controller**

|  It's a universal participant that stays in the background to control the whole flow of conversation and is responsible for taking dynamic actions based on the training to ensure the smooth flow of communication between the customer and the business. This may include request to route to a different agent if the first agent has left and the customer needs more info, closing the conversation when the customer has already left.   
  
  1. A ChannelSession object to track active customer's presence on a media channel. This ChannelSession object is created following the configurations of a Channel as defined in Unified Admin. For more about Channel configurations, see [Unified Admin guide](Unified-Admin-Guide_2524407.html).

  2. Identifies a customer via CX-Customer APIs.

  3. Creates a Conversation object for this customer if no active conversation object for this customer exists in the system. 

  4. For a customer conversation, the Controller may invite a Conversation Bot or a human agent. 

  5. If and when a human agent is required in a conversation, the Conversation is assigned to an agent as an AgentTask. For more details about Agent Tasks, see [Reporting Database Schema -> agent_task](Reporting-Database-Schema_2526317.html) table. 



