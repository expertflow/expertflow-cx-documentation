# CX Knowledgebase : Conversation

A customer interacts with the business over a media channel such as a phone call, WhatsApp, SMS, email, web chat, or a mobile app. All customer interaction events of a customer are pushed to a randomly generated unique subscription topic, called Conversation.   
  
A Conversation is a subscription topic where all customer interaction events are published. Agents and Conversation bots connect to this Conversation topic to receive all customer activities. Agents, Conversation bots, and other possible actors use the same Conversation topic to publish events for a connected customer channel.

A Conversation topic remains alive until the last connected subscriber (customer on a media channel, agent, or a Conversation bot). 

Typically, there is only one Conversation topic per Customer Room at a time. 

is linked to a **Customer**  
---  
contains **ChannelSessions** \- a ChannelSession represents a customer's presence in this conversation on one channel. A customer can reach the contact center using more than one channel at any point in time. All active customer channels are linked to the same customer Conversation.  
contains **Conversation Participants** \- including customer channel sessions, agents, and the Conversation bot  
  
### Conversation States

A Conversation object may be in any of the following states at any point in time. 

**Created**| **Active**| **On Hold**| **Customer Left**| **Wrap-up**| **Inactive**| **Closing**| **Closed**  
---|---|---|---|---|---|---|---  
When topic is created. In this state BOT will join the conversation and can respond to the customer.| When at least one agent in present in the conversation.| When the Agent puts the conversation on hold.  
  
The Agent SLA and the Customer inactivity timers are stopped when the conversation is put on hold. | When all channel sessions of customer are closed.| When all channel sessions of customer are closed and there are agents in the conversation and wrap up is configured.| When all agents left the conversation but the customer is still available.| When the customer and agents have left the conversation.On Closing, the TopicMonitor starts house-keeping such as moving all the topic activities to permanent storage. When the TopicMonitor has completed its house-keeping on the topic, it marks the Topic-state to **Closed** and unsubscribes.| When the controller bot has also been unsubscribed after CIMEvent handler unsubscribe.
