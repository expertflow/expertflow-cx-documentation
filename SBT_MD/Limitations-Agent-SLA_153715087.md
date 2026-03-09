# CX Knowledgebase : Limitations Agent SLA

  * As of the 4.5 release, when an agent applies a wrap-up to a conversation, that wrap-up is sent as an agent message in the system. In scenarios with multiple agents, if the agent SLA (Service Level Agreement) is active and one agent leaves the conversation and provides the wrap-up, it is treated as an agent message. Consequently, the agent SLA is stopped for the other agent involved in the conversation.

  * By default, no thresholds are set in the system for actions Change Color and Show Popup. By using API these actions are configured and tested.



