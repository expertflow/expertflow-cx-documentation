# CX Knowledgebase : Retail Queue Management

Retail Queue Management is a solution for walk-in customers visiting branches. [Expertflow Conversation Studio](https://expertflow-docs.atlassian.net/wiki/x/1RiAB) maintains the flow of customers as they visit the branch.  
  
The customer queuing element is a mobile app or website rendered on a terminal in the branch office. The [customer identifier](https://expertflow-docs.atlassian.net/wiki/x/nIkm) can be a

  * permanent PII identifier (such as Name, customer number, phone number, mobile app)

  * a temporary anonymous identifier such as a name or queue position, plus a token such as a secret PIN or printed-out queue number/ name.




Scheduling of appointments is possible via the **Expertflow Scheduler** , which can schedule and reserve [sessions](https://expertflow-docs.atlassian.net/wiki/x/DoCOBQ) in both the customer and agent or company calendar.

The agent user interface is identical to a normal contact center (with the counter/ ID number replacing a phone number/channel device). Agents can work either in skill-based push or pull routing mode. When an agent accepts a [conversation](https://expertflow-docs.atlassian.net/wiki/x/LACOBQ), this can trigger a webhook in the Expertflow Conversation Studio. This webhook can then trigger a verbal announcement or visual notification in a room.

Wallboards display the queued conversations for certain agent groups (ie, physical location) and their destination (counter or agent ID) once they have been routed. 

A [customer form](https://expertflow-docs.atlassian.net/wiki/x/YIDVBw) can be added/ scheduled in the Conversation Studio to collect feedback from the customer through any [channel](https://expertflow-docs.atlassian.net/wiki/x/Vpgm) once the on-site session terminates to conduct a [Post Collaboration survey](https://expertflow-docs.atlassian.net/wiki/x/YIDVBw).

If customers fail to appear to the agent and re-appear again later, an agent might choose to create a new manual conversation.

**Limitation**

POS (point of sales) hardware such as wallboard displays, tablets, and token printers are not part of the solution.
