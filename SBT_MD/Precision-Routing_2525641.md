# CX Knowledgebase : Precision Routing

Enables the business to make a routing decision of assigning requests to the most suitable agent, based on the agent selection criteria defined under the [queue configurations. ](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2524407/Unified+Admin+Guide#Step-6%3A-Create-a-Queue)

As a new request is received from a channel, it is parked in an associated queue. To learn how to add new channels and associate queues to channels, see [Administrator Guide](http://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2524407).

Based on the routing logic embedded in the Queue **Steps** , the Routing Engine picks an available agent who best matches the criteria and assigns the request. In short, this mode lets the system _push_ a customer request to an agent. The agent has no other option but to 'Accept' such a request. 

To know more about details how this works, please see the section of [Sample Use Case](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/2525641/Precision+Routing#Sample-Use-Case-with-Precision-Mode-Routing), solution component diagram, and sample chat flow.

### Sample Use Case with Precision Mode Routing

### Example Use case

Customers from Los Angeles are facing problems with their broadband devices these days. A special channel and a queue need to be set up to answer customer queries. 

To achieve this, let's see what will be configured and experienced on the Unified Admin and AgentDesk respectively.

#### Admin Configurations

  1. The administrator creates a new [Channel Category (MRD)](http://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2532738) to entertain chat channel requests.

  2. Adds a new [Channel Type](Channel-Related-Objects_276594689.html) `WhatsApp` to handle WhatsApp chats and link this Channel Type to the MRD, `xyz,` created above.

  3. Creates a [Queue](http://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2550494/Queues) `Q1` to enqueue any Broadband-related inquiries coming from WhatsApp. While creating the queue, the admin links the Channel Category `xyz` to the queue `Q1` so that agents who are part of the queue can be assigned chat requests based on the available Channel Category states (i.e. Ready, Active, Busy, etc.).

  4. Creates a new [Channel](Channel-Related-Objects_276594689.html), `C1` of the Channel Type, `WhatsApp`, assuming that this channel is supposed to take customer chat requests from a dedicated WhatsApp number such as `123456`.

  5. Sets the **Routing Mode** of the channel as **Push.**

  6. Adds `Q1`, as the default queue of channel `C1`. This implies that all requests coming on channel `C1` will by default be enqueued to the queue `Q1`




The following diagram depicts the linking of internal solution components and their relationships with each other.

Customers who approach Los Angeles for fixes to their broadband devices should be routed to agents who can speak in English and are skilled enough to answer technical queries related to the Broadband connection. The administrator creates the following [Routing Attributes](http://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2550492/Routing+Attribute). 

  * English (Boolean type)

  * Los Angeles (Boolean type) 

  * Broadband (Proficiency type)` `




So the queue logic would state:

`(English==true) AND (Los Angeles==true) AND (Broadband>=7)`

See [Administrator Guide -> Add Steps to the Queue](http://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2524407/Unified+Admin+Guide) to see how to define queue criteria.

#### Example Chat Flow

Let's see what happens when a new request lands on `C1`:

  1. A customer 'John Williams' sends a WhatsApp message from Los Angeles, to report a problem related to a broadband device and wants to talk to a human agent. 

  2. The chat request is received on the channel `C1`. 

  3. A new channel session for the customer, John is created in the system for the WhatsApp channel request since this is the first message from the customer on this channel.

  4. The customer is identified as John, using his channel identity for `WhatsApp` channel. 

  5. Bot Framework checks if a Conversation from John already exists. If not, it creates a new Conversation for the customer, and the Channel Session is added to the same Conversation.

  6. The chat request landed in the queue `Q1 `which is the default queue for channel `C1.`

  7. The Routing Engine looks for an available agent in the queue based on the routing logic defined in the [Queue Steps](http://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2550494/Queues).

  8. The Routing Engine finds an agent, Sussane who meets the queue criteria, and is the `Longest Available` in `READY` or `Active` state with a minimum number of agent tasks on the MRD `xyz.`

  9. The Routing Engine assigns the chat request to Sussane.

  10. The Routing Engine creates an Agent Task for Sussane to work on this chat request. 

  11. Sussane accepts the request and starts the conversation with John.

  12. Sussane's state turns from `READY` to `ACTIVE `on the MRD `xyz`. See [Agent States](http://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2531294/Agent+States) for details of MRD state transitions.

  13. John gets the answer to his query.

  14. Sussane greets John and leaves the conversation.

  15. John also leaves the conversation.

  16. Sussane's MRD state turns from `ACTIVE `to `READY `on the MRD `xyz.`

  17. The system clears the conversation from Sussane's frontend interface.

  18. The bot framework decides whether or not to close the conversation based on the Bot training/Script (such as closing the conversation when both the customer and the agent leave the conversation).




  

