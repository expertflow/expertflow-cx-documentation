# CX Knowledgebase : Pull-Mode Routing

Enables small-scale businesses to broadcast customer requests to a List. Agents can pull requests from the List whenever they are convenient to join the conversation.

### List

Lists allow the system to park requests of certain channels. Agents then subscribe to the List and get notified about each incoming request being landed on the List. 

To learn how to create new lists and assign them to certain channels, see [Admin Guide -> Pull Mode](Unified-Admin-Guide_2524407.html)

### Request

A **Request** (a List entry or a new conversation in the list) can be in any one of the following states:

  * **UNREAD** \- until no agent has joined the conversation

  * **ACTIVE** \- when at least one agent has joined the conversation

  * **INACTIVE** \- when there's no agent currently present in the conversation but, at least one agent had joined this request earlier and left without closing it. In this case, if a customer sends a message to request a new agent, no new notification is published on the List since the conversation is already listed there. 

  * **CLOSED** \- upon closure of the request when the request was removed, i.e. when the conversation is closed.




### Agent-List Subscription

Agents subscribed to a List get real-time notifications of new conversations being landed on the List. Agents may subscribe to one or multiple Lists to answer requests published on those lists. One or more agents may **Join** a request simultaneously and may also choose to leave at any time. 

To see how agents subscribe to Lists and join pull-based conversations, see [Agent Capabilities -> Subscribe Lists](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/edit-v2/2528122#Subscribed-Lists)

### Workflow

#### Admin Configurations

The same level of configurations are done in Unified Admin, for this scenario as done for [Push-based Routing](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/2525641/Precision+Routing), except for the following differences:

  1. The admin creates an MRD to capture Social media requests from customers.

  2. Adds a new [Channel Type](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/276594689/Channel+Related+Objects) `Face Page Comments`.

  3. The admin adds a new [List](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/2524407/Unified+Admin+Guide#Add-Lists) `L1`.

  4. Creates a new [Channel](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/276594689/Channel+Related+Objects) `C2`, sets the **Routing Mode** as **Pull** (instead of Push), and, maps the Channel `C2` to the List `L1`. This channel is supposed to receive all customer comments posted on the Facebook page. The channel should then publish all new requests on the List `L1`.




#### Example Chat.

  * A new comment is posted on the company's Facebook Page mentioned in the **Service Identifier** field of the channel configs. See the [Administrator Guide](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/2524407/Unified+Admin+Guide) to learn more. 

  * The system publishes the request to the list associated with the channel, i.e. `L1`. 

  * All agents subscribed to the List `L1` get the new incoming request notification. 

  * One or more agents try to join the Conversation. 

  * The agent(s) who joined the chat are subscribed to the Conversation notifications such as, Agent joining, and Agent leaving notifications that are flown through during the conversation.




**Flow Diagram**
