# CX Knowledgebase : Add Agents, Supervisors, and Teams

An AgentTeam consists of agents managed by one primary and optionally multiple secondary supervisors. Agents join queues based on the routing attributes assigned to them and defined in the queues' routing logic. Queues are automatically associated with Teams based on the agents assigned to them.

Supervisors of the team can then monitor queues assigned to the team agents to monitor the performance of the queues.

Agent Teams in EFCX are set up in the unified admin. See [Team Configuration in Unified Admin](Unified-Admin-Guide_2524407.html).

<https://expertflow-docs.atlassian.net/wiki/spaces/SBT/whiteboard/1606221998>

Legend:  
(1,1) = Exactly one (mandatory)  
(0,N) = Zero or many  
(1,N) = One or many

### ![\(blue star\)](images/icons/emoticons/72/1f511.png) Key Points for the Team Concept

  * A Team is supervised by one or more supervisors, where one is primary, and others are supposed to be secondary. 

  * Primary and secondary supervisors are the users who have the “Supervisor” role in IAM.

  * The difference between primary and secondary supervisors is that a primary supervisor supervises the whole team, but a secondary supervisor manages only their own assigned agents and can only optionally monitor other agents.

  * Primary and secondary supervisors have identical capabilities and feature access.

  * A team can include one or multiple agents, but each agent belongs to only one team.

  * Queues join a team based on logical grouping with agents; queues of team agents automatically belong to the team.

  * A supervisor can also be an agent in the same or a different team.

  * A user can be a primary supervisor for one team and, at the same time, may be added as a secondary supervisor in another.




  * To change an agent's team, remove the agent from the current team before adding to another.

  * Log into Unified Admin to manage agents' skills or assigned queues as a Supervisor. 

  * Supervisors utilize real-time dashboards to oversee agent and queue performance metrics. They can update agent statuses to "Not Ready," forcibly logging out agents who remain in the Not_Ready state, monitoring active conversations, and performing silent monitoring if and when necessary.




  * A user assigned as primary supervisor cannot be a secondary supervisor in the same team, and vice versa.

  * All contact center users must belong to a team to log into AgentDesk.

  * Supervisors can create new teams and delete only the teams that they created.

  * After an admin creates a team, supervisors see changes upon logging out and back into unified admin.

  * Remove users from CX Teams before deleting them from Keycloak.

  * Deleting an agent from Keycloak does not immediately update Unified Admin; deleted agents still appear when creating Teams. Users must re-login to see changes.




## ![\(blue star\)](images/icons/emoticons/72/1f504.png) Team Information Syncing

**System**| **Behavior**| **Details**  
---|---|---  
EFCX to CISCO| No automatic sync| Users can update team info in EFCX, but changes do not sync automatically with CISCO.  
CISCO to EFCX| One-way syncing enabled| Changes in CISCO team attributes are reflected in EFCX.  
Adding and removing Agents, Supervisors | Updates EFCX on Finesse login| Adding or removing agents or supervisors in CISCO is reflcted in EFCX teams only when the user is logged in to Finesse.
