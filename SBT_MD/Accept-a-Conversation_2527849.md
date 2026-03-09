# CX Knowledgebase : Accept a Conversation

Enables agents to auto-answer, receive a conversation from queues, handle an ongoing conversation, view, update and link customer profiles, view conversation history, and view active channels.  
  
## Auto-answer

With Auto-answer enabled, a new incoming Conversation request is automatically accepted by the agent. The agent does not need to see incoming notifications.

Auto-answer is not yet available for the Cisco Voice channel.

### To enable/disable Auto-answer

On the Unified Admin, go to **AgentDesk** and switch on/off the feature `Auto Answer.`

![Screenshot 2024-03-07 140510.png](attachments/2527849/151552258.png?width=792)

If Auto-answer is disabled, then agents will receive new requests from the queue, based on the routing logic. This is called **Push Routing** or **Precision Routing** where new requests are pushed or assigned to agents. Following are the details of how agents can answer a Push-based request.

## Answer a Push-based Request

Once an agent receives a new request, it is assigned to an agent, and the agent is reserved. An incoming chat notification appears on the Agent Desk, with a button to **Accept** the request.

The notification contains the name of the customer (if identified), or "Jane Doe" (if an exact match was not found), with a channel type icon to determine the channel through which the request was received (such as Web, WhatsApp channel icons).

See the [Customer Lookup](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/edit-v2/2527849#Customer-Lookup) section below to learn more about how a customer is identified.

In the case of an anonymous customer (or Jane Doe), the incoming notification's background color is set to RED while in the case of an identified customer, the notification's background color changes to GREEN.

![](attachments/2527849/2563837.png?width=801)

 _Answer a conversation_

Upon accepting the requests, agents see the expanded view of the right panel having **Customer Profile** data, **Channel Identifiers** , **Active Sessions**(if enabled)**** and **Conversation Data** details of the customer under the relevant panes. The agent can expand and collapse the right panel by clicking on the arrow button.

The **Customer Info** and **Conversation Data** panes are expanded by default.

![customer info.png](attachments/2527849/1234829331.png?width=700)

The central **Conversation history** view shows all activities exchanged with the underlined customer, including voice calls, chats, wrap-ups/ notes given on a conversation. If enabled, the Channel Session data for the active session(s) is also available under the **Active Sessions** pane. 

### Customer Lookup

Upon the arrival of a new customer request, the application automatically opens up, the best-matched customer profile in the **Customer Profile** pane, based on the channel identity of the customer (such as WhatsApp number, Facebook name, Twitter name, and email ID). During customer lookup, the following scenarios may appear:

**Scenario**| **Description**  
---|---  
**Single/Exact match found**|  This is the case when an exact match is found. However, if you realize that this is a different customer (based on your conversation with the customer), there is a possibility that you can change the customer and link the conversation to a different customer. To do this, click on the **Link Profile** button under the **Customer Profile** pane. From the **Customer List** , you can choose the right customer and click the mouse hover action **Link** against the customer record to link it with the active conversation. See the **Link Profile** **section**.  
**Multiple matches found**|  When multiple matches are found, you will see a list of matches on the right side under the Conversation View, in the **Link Profile** tab. Choose the quick link option from here to link the active conversation with the appropriate match. In case if you need more details on all found matches, click the **View all matches** button to get to the Customer List view where you can see more details of the customers before you actually link the conversation with one. Click the link icon against one customer record in the Customer List view to link the customer with the conversation.  
**No match found**|  When the customer does not exist, the system will create an anonymous profile with the default name, `Jane Doe`. If you think that the customer already exists based on the conversation with the customer, you can click on the **Link Profile** Button in the Customer Profile Pane. This opens up the Customer List view. Click the mouse hover action, **Link** against the desired customer record to link the active conversation with the customer. If no customer exists, you may choose to update the anonymous profile by clicking on the **Update Profile** tab under the **Customer Info** pane. See the section, **_Edit Customer_** for more details.  
  
## View Customer Profile

Allows agents to view the customer profile. To view the profile, expand the arrow on the Conversation view to see the Customer Profile pane on the right-hand side.

![customer info pannel.png](attachments/2527849/1234993176.png?width=341)

_Customer Profile_

In this view, the customer profile data is segregated and divided into two tabs:

### Update A Customer Profile

Agents can see and analyze the conversation and update or link the customer profile accordingly.

Upon receiving the customer's requests, the application associates the request with the best-matched customer profile. All customer data is stored in Expertflow CX except the Channel Identifiers identities (phone number, WhatsApp number, etc.). 

#### To update the Customer Profile

Expand the arrow on the Conversation view to see the Customer Profile pane on the right-hand side.

![](attachments/2527849/125632551.gif?width=770)

Click the **Update Profile** button to update the customer information.

If no data is available in any of the customer fields, those fields will not appear under this tab by default.

### Link Customer Profile

When a request is received (Push or, Pull based), the application associates the active conversation with a best-matched customer profile.

#### To Link a Profile

However, agents may also change this linking by relinking the conversation to a different profile, for reasons listed below:

  * When a customer is not identified but exists - For instance, a customer is calling from an unknown identity. The application links the conversation to an anonymous profile

  * When the actual customer is different from the identified (when the customer calls from a channel identity of a different customer)

  * When multiple matches are found. 




Linking the conversation in this way helps in tracking customers' past conversation history so that it brings up every time a new request from the same customer.

The scenarios of the 'Link Profile' are explained below:

#### When a Customer is not identified but exists

This is the case where a customer contacts the contact center with an identity that is not stored under the customer profile. In this case, the system creates an anonymous profile and shows an anonymous customer to the agent to do the essential updates. The agent then decides that a new profile needs to be created or link the active conversation with an existing customer profile (based on its conversation with the customer).

If the agent comes to know that the profile already exists, she can click the **Link Profile** button under the **Customer Profile pane** on the right and click the "**Link** " icon against a desired customer record on the Customer List view as shown below:

![](attachments/2527849/125632557.png?width=832)

Upon clicking the **Link** option, the agent confirms if she also wants to update the channel identity of the customer in the linked profile. Upon confirmation (check the checkbox in the confirmation dialogue), the channel identity is added to the linked profile so that, next time whenever the customer reaches with the same channel identity, the system will identify this customer profile as an identified customer (if no other profile exists with the same identity).

![](attachments/2527849/125632563.png?width=870)

In case, the customer says that the channel identity does not belong to his/her profile or the agent decides not to add the identity to the linked customer profile, the conversation still gets linked with the profile so that it can be tracked under the linked customer's conversation history.

#### When the actual customer is different from the identified

This happens when a customer has called from an identity that is linked with a different customer profile. For instance, a customer John calls from another customer David's cell number while the number is owned by David.

In this case, the agent may decide if she wants to link the active conversation with a different customer (in this example, John) instead of the identified customer (i.e. David). Also, the agent can decide if she needs to update the channel identity to the linked profile (based on its conversation with the customer).

#### When multiple matches are found

This occurs when multiple matches are found against the customer's channel identity. This happens when the same channel identity exists in multiple customer profiles. In this case, the system creates an anonymous profile and shows all matched customers as suggestions to the agent. The agent will see all matches under another pane, **Link Profile** pane. The agent can select the right customer from the pane and choose the **Link** option against the desired customer. 

![](attachments/2527849/125632569.png?width=300)

To see more details of those matched profiles, click the **View all matches** button to go to the Customer List. Looking at the other attributes from the Customer List, make sure that you click the "Link" icon against the right customer record on the Customer List.

## View Conversation History

The Conversation History enables the agent to provide the record of all the conversations exchanged with the active customer. Each conversation carries activities exchanged over the conversation. These activities include:

  1. Voice calls received/ initiated by the agent to the customer,

  2. Chat messages sent over the conversation (customer/ whisper messages),

  3. Conversation notifications are logged under all conversations with this customer,

  4. playable recording links are visible,

  5. Wrap-up and note activities.


![Conversation.png](attachments/2527849/1236074658.png?width=700)

So when a request is routed to an agent, the agent can only see the current conversation and the activities/messages exchanged for the active conversation before it was routed to the agent.

See more about permissions and scopes in [Security and User Permissions](/wiki/pages/createpage.action?spaceKey=SBT&title=Security%20and%20User%20Permissions&linkCreation=true&fromPageId=2527849).

By default, the past conversations are hidden behind a **Load More** button. If an agent has the permission to load the history, he/she can click this button to load the past conversations of the customer, preserving the current message position while loading the past conversations. To know about the latest query, go to the bottom of the conversation by clicking on **Jump to bottom**

![](attachments/2527849/125632581.png?width=600)

Upon receiving a new message while reading the previous history on the top, the agent will see the **New Message** button popping up. Click on that to read the newly received message.

![](attachments/2527849/125632587.png?width=750)

Media Channels are now renamed to Channel Identifiers

## View Active Sessions

This is the tab where all of the **Active Sessions** of the customer are listed. These are the channels on which the customer is currently active on the system. Since a customer can open multiple channel sessions in a conversation, all those channel sessions are listed here with or without the channel session data (this is the data that is passed by the channel connector to the channel).

In the case of a web channel, the channel session data carries: 

  * Customer's browser info - device type such as mobile, desktop, browser type, time zone, language

  * Customer Identifier 

  * Service Identifier

  * Form data as filled in by the customer while initiating the web chat 


![active sessions.png](attachments/2527849/1236107470.png?width=700)

In the case of the WhatsApp channel, the channel session data carries:

  * Service Identifier 

  * Customer Channel Identifier




In the case of the Facebook channel, the channel session data carries:

  * Service Identifier

  * Customer Channel Identifier




Active Channels are now renamed to Active Sessions
