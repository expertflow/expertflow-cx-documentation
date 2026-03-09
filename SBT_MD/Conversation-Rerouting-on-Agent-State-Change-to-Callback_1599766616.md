# CX Knowledgebase : Conversation Rerouting on Agent State Change to Callback

This feature is available on CX4.10.5 and onwards.

Conversations can now be rerouted when an agent changes their state to **Not Ready** \- **Callback**. To enable this feature, first create a **Callback** reason in **Unified Admin** , as shown in **Figure 1** below.

![image-20251229-110929.png](attachments/1599766616/1600323586.png?width=936)

A new flow has been added in **Conversation Studio** to handle all events related to an agent’s state change to Callback. If you are using the **default training** , this flow is already included. If you are using **custom training** , please refer to the Conversation Studio default flows [documentation](https://expertflow-docs.atlassian.net/wiki/spaces/CXDOC/pages/1144094757/Default+Flows#15.-Task-State-Changed) (see the **“Agent State Changed”** section — 17th heading) and update your customized flow accordingly.

Once the above changes are done, whenever the agent changes the state to Not Ready with reason Callback, all of its active conversations will be re-routed to the original queue.
