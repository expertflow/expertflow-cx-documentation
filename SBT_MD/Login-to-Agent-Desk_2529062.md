# CX Knowledgebase : Login to Agent Desk

The agent can login to Agent Desk using the user's login credentials defined in the Keycloak. When integrated with Cisco Finesse, the agent must specify Cisco login credentials. When the Agent Desk is embedded in Cisco Finesse, the agent is automatically logged in to the Agent Desk.Expertflow CX uses Keycloak for centralized IAM (Identity and Access Management) functions. All application users' roles and permissions are defined in Keycloak. 

See [Security and User Permissions](/wiki/pages/createpage.action?spaceKey=SBT&title=Security%20and%20User%20Permissions&linkCreation=true&fromPageId=2529062) for more details on user authorization with Agent Desk.

**Login Options**| **Description**  
---|---  
Login with Cisco Finesse | This is available in the following modes,

  * **When** _**Agent Desk**_**is embedded in Cisco Finesse**
    * Once logged in to Cisco Finesse, agents automatically get logged in to the Agent Desk. This automatic login to the application is supported in the case of both SSO and non-SSO environments. 
    * When agents log in, their login details are synchronized with KeyCloak so that the agents' profiles also get created in KeyCloak with the same credentials as Cisco. Upon login, agents are allowed to get logged into the Agent Desk with restricted access to the application resources.
  * **When** _**Agent Desk**_**is integrated with Cisco Finesse as a standalone application**
    * Users need to add their Cisco Finesse credentials (including extension) to login. This login to the application is supported for _Non-SSO_ environments as of now. 
    * When agents log in, their login details are synchronized with KeyCloak so that the agents' profiles also get created in KeyCloak with the same credentials as Cisco. Upon login, agents are allowed to get logged into the Agent Desk with restricted access to the application resources.



  * Finesse call controls are to be used for call handling.
  * Cisco Contact Center Details are can be checked [here](Cisco-Contact-center-integration_2525072.html).

  
Login with Keycloak | If Cisco integration is not enabled, agents provide their KeyCloak username and password while logging in to Agent Desk. The user authentication request is redirected to Keycloak for request verification. Upon confirmation, agents get logged in to the Agent Desk with access to the permitted resources.   
  
The agent logs into the Agent Desk Application using [extensions](Creating-extensions-on-Media-Server_1341253.html) created by the business administrators. The user authentication request is redirected to KeyCloak for request verification. Upon confirmation, agents get logged in to the Agent Desk with access to the permitted resources.

![agent logs in with state ready-1.png](attachments/2529062/136511572.png?width=600)

  * Agents are in a **Not-Ready** state by default. They need to change their state to **Ready** to receive requests from the assigned MRDs. There are[ two levels of state changes](Change-Agent-State_2524603.html) in the Agent Desk.

  * When using with Cisco Finesse, Agent state is synced with Finesse Agent state.




**Logout Options**| **Description**  
---|---  
Logout| To [log out](Logout_2525352.html), click the profile menu at the top right on the Agent Desk and click the **Logout** button.  
Logout when integrated with Cisco Finesse| To logout, users need to logout from the finesse application resulting in logout from _Agent Desk_ as well.
