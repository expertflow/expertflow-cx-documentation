# CX Knowledgebase : System Behaviour incase of Failover

## **Overview**

This document provides an analysis of failover scenarios across various communication channels within a High Availability (HA) deployment. It outlines how an active or a new conversation across each channel behaves when a failover event occurs.

The goal is to give stakeholders—including system architects, DevOps engineers, QA teams, and product managers—a clear understanding of:

  * The specific failover mechanism and behavior associated with each supported channel (e.g., Voice, Chat, Email, Social, etc.).

  * The expected system response and any temporary service interruptions or degradation during the failover process.

  * The impact on in-progress customer interactions and session persistence.

  * Recommendations or considerations for minimizing downtime or data loss.




## **Failure Scenarios & Limitations**

### Email Channel

**Scenario**| **Current Behavior**| **Improvements on Roadmap**  
---|---|---  
The customer sends a new email/reply to an existing email thread, and the system is down| As the system is down, EFCX is unable to fetch new emails from the email exchange. So there will be no incoming emails into EFCX. However, Emails from customers will still be received on the Email exchange. When the system is up again, currently it will **NOT** be able to fetch those emails that have arrived on the email exchange during the downtime. | Store the timestamp in the system when the email connector last fetched emails from the Exchange Server and successfully forwarded them to CCM. This will ensure that, in case the email connector is down, it will fetch all the downtime emails once it comes up again. **Tentative Timelines:** 30 Aug 2025  
The email was fetched by the email connector, but was not successfully sent to CCM yet. | If the system is down at this stage, the email will not be processed. Once the system comes up again, the system will **NOT** process this email again. | Same as above. Once the above improvements are implemented, that will resolve this case as well and will ensure the email is fetched again and will be sent to the bot/agent for a proper response.  
The email was successfully fetched and sent to CCM, but the conversation has not been created yet. | In this case, when the system comes up again, the emails will be processed and routed to the available agents/bot.|   
CCM has received the email, has created a conversation, and routed it to a chatbot.| In this case, if the chatbot has NOT responded yet and the system goes down, the bot will not respond to the email when the system comes up again.| **Tentative Timelines:** Q4, 2025  
A Conversation has been created and is waiting in the queue to be routed to the available agent.| When the system comes up again, the routing engine will restore all queued conversations and will be routed to the available agents.|   
A conversation has been offered to the agent, is ringing, and the agent has yet to accept it.| If the system goes down, the agent will see an error message and will not be able to accept the chat.  
When the system comes up again, the conversation will ring again on that agent for him/her to accept.|   
The agent has accepted the conversation and is in an active state.| If the system goes down, the agent will see an error message and will not be able to respond.  
When the system comes up again, all active chats will be restored. | All timers should start from the point when the system went down.**Tentative Timelines:** Q4, 2025  
The conversation is in a wrap-up state.| If the system goes down, the agent will see an error message and will not be able to apply wrapup.When the system comes up again, all wrap-up state conversations will be restored.|   
  
### Web Channel

**Scenario**| **Current Behavior**| **Improvements on Roadmap**  
---|---|---  
The customer wants to initiate the chat, and the system is down.| As the system is down, EFCX is unable to fetch the web widget. So the customer did not even initiate the chat.|   
The customer opens the web widget, fills out the form, and starts the chat, but the system is down.| If the system is down at this stage, the request will not be received by the connector. Once the system comes up again, the system will **NOT** process this request again.|   
The request was received by the connector but has not been successfully sent to CCM yet. | If the system is down at this stage, the request will not be processed. Once the system comes up again, the system will **NOT** process this request again. |   
CCM has received the START_CHAT intent, but the system is down| If the system is down at this stage, the request will not be processed. Once the system comes up again, the system will **NOT** process this request again.  
|   
On reciving START_CHAT intent and CCM publishes CHANNEL_SESSION_STARTED,| When the system comes up again, all active sessions will be restored. |   
CCM has created the conversation, and a welcome message was received by the customer, and the customer sent the first message (customer message must publish on topic), but the system is down| When the system comes up again, all active chats will be restored. And the customer message was also restored from AMQ.|   
Bot-Framework has received the customer message and routed it to a chatbot.| In this case, if the chatbot has NOT responded yet and the system goes down, the bot will not respond to the customer message when the system comes up again.|   
Chatbot message received on the customer side, and the customer wants to route to an agent, but the system is down| When the system comes up again, all active chats will be restored. And the customer message was also restored from AMQ.|   
System received the customer message and is waiting in the queue to be routed to the available agent, but the system is down| When the system comes up again, the routing engine will restore all queued conversations and will be routed to the available agents.|   
A conversation has been offered to the agent, is ringing, and the agent has yet to accept it.| If the system goes down, the agent will see an error message and will not be able to accept the chat.  
When the system comes up again, the conversation will ring again on that agent for him/her to accept.|   
The agent has accepted the conversation and is in an active state.| If the system goes down, the agent will see an error message and will not be able to respond.  
When the system comes up again, all active chats will be restored. |   
The conversation is in a wrap-up state.| If the system goes down, the agent will see an error message and will not be able to apply wrapup.When the system comes up again, all wrap-up state conversations will be restored.|   
  
  * We are assuming that Redis, ActiveMQ/PostgreSQL, and MongoDB are deployed out of a Kubernetes cluster and are a single point of failure. If one or all of these components go down, for ongoing conversations:

    * The system will have unexpected behavior.

    * All existing conversations will be lost permanently even after the components are up again.

  * The system will not accept any new conversation as long as one or all of the above components are down. 

  * To overcome this, stateful sets must be deployed in HA as well.



