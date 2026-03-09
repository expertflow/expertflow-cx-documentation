# CX Knowledgebase : Use case with Pull-based Routing

#### Admin Configurations

The same level of configurations are done in Unified Admin, for this scenario as done for [Push-based Routing](Precision-Routing_2525641.html), except for the following differences:

  1. The admin creates an MRD to capture Social media requests from customers.

  2. Adds a new [Channel Type](Channel-Related-Objects_276594689.html) `Face Page Comments`.

  3. The admin adds a new [List](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/2524407/Unified+Admin+Guide#Add-Lists) `L1`.

  4. Creates a new [Channel](Channel-Related-Objects_276594689.html) `C2`, sets the **Routing Mode** as **Pull** (instead of Push), and, maps the Channel `C2` to the List `L1`. This channel is supposed to receive all customer comments posted on the Facebook page. The channel should then publish all new requests on the List `L1`.




#### Example Chat.

  * A new comment is posted on the company's Facebook Page mentioned in the **Service Identifier** field of the channel configs. See the [Administrator Guide](Unified-Admin-Guide_2524407.html) to learn more. 

  * The system publishes the request to the list associated with the channel, i.e. `L1`. 

  * All agents subscribed to the List `L1` get the new incoming request notification. 

  * One or more agents try to join the Conversation. 

  * The agent(s) who joined the chat are subscribed to the Conversation notifications such as, Agent joining, and Agent leaving notifications that are flown through during the conversation.




**Flow Diagram**
