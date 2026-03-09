# CX Knowledgebase : Priority Routing

Priority Routing enables the business administrator/supervisor/manager to route a customer's request on priority, avoiding Queue wait Time. This priority is set based on the customer's type label i.e. defined [here](https://docs.expertflow.com/display/CX/Supervisor+Guide#SupervisorGuide-CustomerLabels) by business administrators**.** The admin/supervisor can [create Customer Labels](https://docs.expertflow.com/display/CX/Supervisor+Guide#SupervisorGuide-CustomerLabels) and set the priority as per business requirements . The agent can [assign labels](https://docs.expertflow.com/display/CX/Agent+Guide#AgentGuide-AssignLabelstoCustomers) to the customer. This prior request will then directly land on the relevant queue bypassing wait time. The system reserves an agent to serve this request priorly.

## To Set the Priority Routing

  * Configure customer labels in [AgentDesk](https://docs.expertflow.com/display/CX/Supervisor+Guide#SupervisorGuide-CustomerLabels) as shown below


![](attachments/2529105/2569954.png?width=530)

  * Assign labels to a customer. One or more than one label can be assigned to a single customer at a time.


![](attachments/2529105/2569949.png?width=530)

  * If a customer has no label, the priority will be considered '1' as the default priority.

  * If multiple labels are assigned to any customer, the highest priority will be considered for routing the request to the agent.




The business admin/supervisor can create the customer label and set the priority such as

**Labels**| **Priority**  
---|---  
Premium| 10  
Gold| 8  
Standard| 6  
  
In case of multiple labels assigned to a customer, the highest priority label will be served first. For example, the customer is labeled with 'Premium' and 'Standard', In this case, Premium has the priority '10' and 'Standard' has priority '6', so the customer will be served as 'Premium' customer that has priority '10', the highest priority. 

  

