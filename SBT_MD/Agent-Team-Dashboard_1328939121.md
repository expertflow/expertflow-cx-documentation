# CX Knowledgebase : Agent Team Dashboard

Provides supervisors with detailed insights into the performance of individual agents within a team.  
  
This helps track conversation handling, service levels, response times, and agent status to evaluate productivity and efficiency.

## **Dashboard Panels**

### **Agent Performance Table**

The central panel displays a tabular view of all agents in the selected team. It provides performance metrics for each agent across conversations handled. The columns include:

**Team Name**|  The team name to which the agent belongs.  
---|---  
**Agent Name**|  The full name of the agent.  
**Agent ID**|  A unique system identifier for the agent.  
**Answered Conversations**|  Number of conversations successfully answered by the agent.  
**Abandoned Conversations**|  Number of conversations that were abandoned before resolution.  
**Service Level %**|  The percentage of conversations answered within the defined service threshold.  
**Average Time Response**|  The average time taken by the agent to respond to conversations (HH:MM:SS)  
**Status**|  Current status of the agent (e.g., LOGOUT, READY, NOT_READY, BUSY).  
  
  * Service Level is calculated based on the team’s predefined threshold and reflects the agent’s efficiency.

  * Average Time Response helps identify agents who may require additional training or workload balancing.

  * Status values give supervisors real-time insights into agent availability.

  * Data refresh frequency depends on the system’s ETL data source configuration.



