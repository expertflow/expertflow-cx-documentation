# CX Knowledgebase : Agent Desk Integration with Cisco Finesse

## Prerequisites

For Agent Desk integration with Cisco Finesse, the following are the prerequisites:

### Access Credentials

  * Cisco Finesse `admin` credentials are required.

  * The Agent Desk uses Cisco Finesse Agent credentials to monitor this agent’s Finesse CTI events.




### Port Utilization

The following ports must be open for communication between Cisco and CX components.

**Source**| **Destination**| **Protocol**| **Source Port**| **Destination Port**| **Description**  
---|---|---|---|---|---  
Agent Desk| Cisco Finesse| REST via HTTPS| any| Finesse REST API (8445)| Agent Desk sends agents state change requests (Voice MRD) for Media Blending to Cisco Finesse. It bypasses SSL certificate verification.  
KeyCloak| Cisco Finesse| REST via HTTPS| any| Finesse REST API (8445)| To synchronize the Cisco Finesse agent with KeyCloak.  
Cisco Finesse XMPP Server| Agent Desk| XMPP|  | 5222 (un-secure)| Agent Desk subscribes to Finesse XMPP service for the logged-in Cisco Contact Center Agent State change events. This communication is insecure, and the Cisco Contact Center Agent’s Finesse credentials are used to subscribe for XMPP events.
