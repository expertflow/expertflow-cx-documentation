# CX Knowledgebase : Socket Events

This document describe the emission of events, their triggers and the properties as updated between custom Agent Desk and AgentManager.

The first table describes the events emitted by the custom Agent Desk and second tables enlist events emitted by Agent Manager.

## Agent as Emitter Socket Events

These events are emitted by the Agent/custom Agent Desk and listened by events on Agent Manager. 

Title| Event Description| Emitter  
---|---|---  
[changeAgentState](/wiki/spaces/SBT/pages/2531704/changeAgentState)| When an agent changes its MRD state, state, or logs out from the agent desk, the agent desk requests to agent manager to change its MRD states:

  * ready/not-ready
  * ready/not-ready with or without selecting reason of not ready)
  * log out (with or without selecting reason of logout).

| Agent Desk  
[publishCimEvent](/wiki/spaces/SBT/pages/2531739/publishCimEvent)| Event is emitted when agent requests to agent manager for publishing in-conversation events such as the messages of multiple types such as plain, media, contact, location, URL and WrapUp.| Agent Desk  
[directConferenceRequest](/wiki/spaces/SBT/pages/2531711/directConferenceRequest)| Event is emitted when an agent requests for another agent (from a certain queue) to join the active conversation, the agent desk emits an event of '`directConferenceRequest'.`In response, the Routing Engine will find another available agent until TTL time expires.| Agent Desk  
[consultTransferRequest](/wiki/spaces/SBT/pages/933691449/consultTransferRequest)| Event is emitted when an agent wants to leave the conversation and transfer it to another agent (from a certain queue) to takeover the active conversation; the agent desk emits an event of '`consultTransferRequest'.`In response, the Routing Engine will find another available agent until TTL time expires.| Agent Desk  
[consultConferenceRequest](/wiki/spaces/SBT/pages/933822483/consultConferenceRequest)| Event is emitted when an agent requests for another agent (from a certain queue) to join the active conversation as a consult, the agent desk emits an event of '`consultConferenceRequest'.`In response, the Routing Engine will find another available agent until TTL time expires.| Agent Desk  
[closeWrapup](/wiki/spaces/SBT/pages/933691394/closeWrapup)| Event is emitted when agent requests to agent manager for publishing WrapUp events| Agent Desk  
[directTransferRequest](/wiki/spaces/SBT/pages/2531715/directTransferRequest)| Event is emitted when an agent wants to leave the conversation and transfer it to another agent (from a certain queue) to takeover the active conversation; the agent desk emits an event of '`directTransferRequest'.`In response, the Routing Engine will find another available agent until TTL time expires.| Agent Desk  
[unsubscribePullModeList](/wiki/spaces/SBT/pages/2531766/unsubscribePullModeList)| When an agent unsubscribes to a list the agent desk emits an event of unsubscribePullModeList to the agent manager, agent manager listens to the event and successfully unsubscribes from the list for that agent.| Agent Desk  
[topicUnsubscription_](/wiki/spaces/SBT/pages/2531764/topicUnsubscription_)| Agent requests to agent manager for the topic unsubscription by emitting this event.| Agent Desk  
[topicSubscription](/wiki/spaces/SBT/pages/2531760/topicSubscription)| Agent requests to agent manager for the topic subscription by emitting this event.| Agent Desk  
[JoinAsSilentMonitor](/wiki/spaces/SBT/pages/2528276/JoinAsSilentMonitor)| Event is emitted when supervisor requests to agent manager to join an active conversation of a team member (agent) as a silent member.| Agent Desk  
[subscribePullModeList](/wiki/spaces/SBT/pages/2531752/subscribePullModeList)| When an agent subscribes to a list the agent desk emits an event of subscribePullModeList to the agent manager, agent manager listens to the event and successfully subscribes to the list for that agent.| Agent Desk  
[joinPullModeRequest](/wiki/spaces/SBT/pages/2531724/joinPullModeRequest)| Event is emitted when an agent joins a chat, the agent desk emits an event of joinPullModeRequest to the agent manager, agent manager listens to the event and successfully joins the chat for the agent.| Agent Desk  
[deletePullModeRequest](/wiki/spaces/SBT/pages/2531709/deletePullModeRequest)| Event is emitted when an agent ends a chat the agent desk emits an event of deletePullModeRequest to the agent manager, agent manager listens to the event and successfully ends the chat for the agent.| Agent Desk  
  
## Agent Manager as Emitter Socket Events

These events are emitted by the Agent Manager and listened by events on custom Agent Desk. 

Title| Event Description| Emitter  
---|---|---  
[removePullModeSubscribedListRequests](/wiki/spaces/SBT/pages/2531746/removePullModeSubscribedListRequests)| Event is triggered when agent unsubscribes to a list.| Agent Manager  
[onPullModeSubscribedListRequest](/wiki/spaces/SBT/pages/2531734/onPullModeSubscribedListRequest)| Event is triggered when a new chat is initiated by the customer in one of the subscribed lists. It is also triggered when an agent leaves a chat| Agent Manager  
[onPullModeSubscribedListRequest](/wiki/spaces/SBT/pages/2531734/onPullModeSubscribedListRequest)| Event is triggered when a new chat is initiated by the customer in one of the subscribed lists. It is also triggered when an agent leaves a chat| Agent Manager  
[wrapupTimerStarted](/wiki/spaces/SBT/pages/935100435/wrapupTimerStarted)| Event is triggered to start the wrapup timer| Agent Manager  
[consulTransferRequestSuccess](/wiki/spaces/SBT/pages/934346772/consulTransferRequestSuccess)| Event is triggered when an agent assigned to the conversation in response of consult transfer request| Agent Manager  
[agentAssistanceRequestPlaced](/wiki/spaces/SBT/pages/935100417/agentAssistanceRequestPlaced)| Event is triggered in response of direct conference and direct transfer request| Agent Manager  
[agentAssignedForAssistance](/wiki/spaces/SBT/pages/934346754/agentAssignedForAssistance)| Event is triggered when an agent assigned to the conversation in response of consult transfer or direct transfer| Agent Manager  
[topicUnsubscription](/wiki/spaces/SBT/pages/2531762/topicUnsubscription)| Event is triggered when an agent leaves the conversation. Event returns a success message in case of success.| Agent Manager  
[topicClosed](/wiki/spaces/SBT/pages/2531758/topicClosed)| Event is triggered to notify the agent whenever a topic is closed.| Agent Manager  
[socketSessionRemoved](/wiki/spaces/SBT/pages/2531750/socketSessionRemoved)| Event is triggered when agent switches to another tab. The Agent desk listens to the event and removes the agent from the previous session. Automatically logs the agent out from the previous session.| Agent Manager  
[revokeTask](/wiki/spaces/SBT/pages/2531748/revokeTask)| Event is triggered to revoke the new task request from the agent if not accepted within the configured accept time. | Agent Manager  
[onTopicData](/wiki/spaces/SBT/pages/2531736/onTopicData)| Event is triggered when agent subscribes to a topic| Agent Manager  
[taskRequest](/wiki/spaces/SBT/pages/2531754/taskRequest)| Event is triggered on a new conversation request.| Agent Manager  
[agentPresence_](/wiki/spaces/SBT/pages/2531701/agentPresence_)| Event triggered to update agent state information.| Agent Manager  
[onCimEvent](/wiki/spaces/SBT/pages/2531728/onCimEvent)| The agent manager sends the real-time CIM Events to the agent through this event.| Agent Manager  
[onChannelTypes](/wiki/spaces/SBT/pages/2531726/onChannelTypes)| Event is triggered once connection is established through a channel| Agent Manager  
[errors](/wiki/spaces/SBT/pages/2531722/errors)| Event is triggered to notify the agent whenever any error occurs in the system or on any request | Agent Manager  
[connect_error](/wiki/spaces/SBT/pages/2531707/connect_error)| Event is triggered to notify the agent whenever any error occurs during handshake of socket connection establishment  
  
  
e.g, unauthorized user, invalid data etc.| Agent Manager  
[addPullModeSubscribedListRequests](/wiki/spaces/SBT/pages/2531698/addPullModeSubscribedListRequests)| Event is triggered when an agent subscribes to a list. If it contains chats, then a list of conversations is returned else the array is returned empty.| Agent Manager  
[onPullModeSubscribedList](/wiki/spaces/SBT/pages/2531732/onPullModeSubscribedList)| Triggered when the agent unsubscribes or subscribes to the list where certain customer-agent conversations are maintained.| Agent Manager  
[pullModeSubscribedListRequests](/wiki/spaces/SBT/pages/2531743/pullModeSubscribedListRequests)| Event is triggered if there are chat requests present in a list subscribed by the agent.| Agent Manager  
  
  

