# CX Knowledgebase : Cisco Voice Channel Limitations

**Tested with**

  * Tested with Cisco UCCX 12.5, UCCX 12.5.1 SU3. For details, see the [compatibility guide](Compatibility-Guides_85983333.html#Phones-Compatibility)

  * Cisco UCCE supported

  * Cisco IP Phones with `CIPC version 8.6.x` and `Jabber 14.x`

  * Hard phones 7965 & 7942 and assumed to work with others.

  * Tested with `Cisco non-SSO` but assumed to work with Cisco SSO as well.




The following are the limitations of the solution. 

**Logout**|  Logging out of Finesse does not log out the agent from CX. It does not have any impact on Finesse users. Agents will be shown only as active agents on the CX Agents Detail dashboard.  
---|---  
**Custom Reason Code**|  Having at least 1 custom reason code for Not Ready and 1 custom reason code for Logout is mandatory.   
**CTI Lib Limitations**|  CTI lib limitations are mentioned [here](https://expertflow-docs.atlassian.net/wiki/x/0wM8)  
  
### Finesse Failover Scenarios

**Agent’s State Not Ready**|  The agent’s state becomes Not Ready when Finesse is restored and the call continues upon a domain shift. This limitation occurs from the Finesse side. For details, see [High Availability (HA) / Duplex Deployment](https://expertflow-docs.atlassian.net/wiki/spaces/MDWEB/pages/259260459/High+Availability+HA+Duplex+Deployment)  
---|---  
**Call Ends During Failover**|  During Finesse failover, if the call ends and the system reconnects to Finesse, the AgentDesk gets the call ending event from the CTI with no dialog info that the call has ended already, and the conversation is closed. The AgentDesk uses the dialog data stored in the cache for the incoming call, and the call duration in the call leg displays as 0 seconds. For details, see [CIM-12031](http://project.expertflow.com:8080/browse/CIM-12031)  
**Direct Transfer**|  During a direct transfer, on an agent extension and queue, if Finesse failover occurs, particularly call the customer number becomes null in the call leg for that particular call, once Finesse is restored. For details, see [CIM-12073](http://project.expertflow.com:8080/browse/CIM-12073)  
  
### [**Cisco Teams Synchronizer**](/wiki/pages/createpage.action?spaceKey=SBT&title=Cisco%20Teams%20Synchronizer&linkCreation=true&fromPageId=74514469)

**Manually Delete Teams/Users from Keycloak**|  If a Cisco team or user is deleted after syncing to KeyCloak, the relevant Group/Team is not deleted from KeyCloak. The KeyCloak admin needs to manually delete it.  
---|---  
**To make Finesse Agent/Supervisors available on KeyCloak**| Finesse supervisors and agents are not going to be synced to Cisco Teams automatically. To make them available on KeyCloak as a part of the Finesse Team, a one-time login to Finesse is required.
