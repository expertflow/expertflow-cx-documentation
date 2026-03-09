# CX Knowledgebase : PII Data Masking of Customer Attributes in AgentDesk

This feature enables admins to mark customer attributes as **PII**. All attributes marked as **PII** are restricted and displayed only to the users who can view the attribute's contents. 

Attributes can be marked as PII, under the Customer Attributes page, while editing or creating an attribute.

![](attachments/698089579/697991391.png?width=1124)

By default, agents are segregated based on their access levels, divided into two groups; Senior Agents and Junior Agents. 

For more on the permission levels of the two agent types, see <https://expertflow-docs.atlassian.net/wiki/x/jpMm>

For those who do not have access, the customer data along those attributes will be displayed as masked while some of the data will still be visible, such as:

  * First 4 and last 4 characters of an email. Abdu*****.com

  * Last 2 digits of a Phone Number - ********80

  * The first 3 characters of a string of all other types


![](attachments/698089579/697860259.png?width=1124)

The data masking is only done on the client side. The data on the database or on the API logs will not be masked.

**Limitations**

  * Currently, only the data stored in customer attributes can be masked. The data in the dashboards or, in the conversation data/channel session data will not be masked as those are not a part of Customer Schema Attributes.

  * If a supervisor marked/unmarked any attribute as PII, the agents must refresh the Agent Desk to get the latest attribute settings.

  * If the admin changes the permissions of agents from Keycloak, then agents will have to re-login to get the latest permission set.

  * In the quoted message area, the agent’s first name will also be masked if the **First Name** attribute in the **Customer Schema** is marked as PII.

  * If the **Voice** attribute is marked as PII, then the agent extension will also automatically be masked in the active call view.

  * If the value of a schema attribute contains a comma, “,” the next 3 characters after the comma will not be masked.

  * If the pod restarts, then the system attributes will be reset. If some of the attributes were marked as PII before the POD restarted, you’ll need to set them as PII again.



