# CX Knowledgebase : Troubleshooting for CX Voice

## Inbound Scenarios

![](images/icons/grey_arrow_down.png)If the call starts and the customer selects to talk to an agent option from IVR and starts waiting for a long time

You can troubleshoot this case on the following ends:

#### AgentDesk

  1. Check if an agent is logged in on the AgentDesk

  2. Check if CX voice MRD is ready for the agent. (Check MRD state for the Agent, should be in the Ready state)

  3. Check if CX Voice is working correctly with no SIP-related errors in the AgentDesk console (F12 in the browser)




#### Voice Connector logs

  1. Open the [Voice Connector logs](Accessing-CX-Voice-Components_237207657.html#Voice-Connector-logs).

  2. Check if the **RECEIVED AGENT RESERVATION REQUEST** is shown and **the call info printed is correct.**

     1. eslHost, callUid",queueType, callingNumber, priority, queue, callSipId, direction, service identifier

  3. See if information in **ASSIGN_RESOURCE_REQUESTED** payload is correct.

     1. ServiceIdentifier must match the dialed number and the serviceIdentifier set for the CX Voice channel in [_Unified Admin_](Accessing-CX-Voice-Components_237207657.html#CX-Unified-Admin)

     2. Check if customerChannelIdentifier is the same as the calling number

     3. Check if queue info is correct (no queue name/type means default queue selected)

        1. If not, check that the correct queue is set in [_Media-Server cx_env file_](Accessing-CX-Voice-Components_237207657.html#Media-Server-Scripts) and that the correct queue is assigned to the agent in [_Unified Admin_](Accessing-CX-Voice-Components_237207657.html#CX-Unified-Admin). (e.g. for DN 1225, env will be cx_env1225.lua)

     4. Check direction (INBOUND/DIRECT TRANSFER) and eslHost (same as IP address of Media-Server of calling number)

  4. If the **RECEIVED AGENT RESERVATION REQUEST** is not shown then:

     1. Check if VC IP/Port in [_Media-Server cx_env file_](Accessing-CX-Voice-Components_237207657.html#Media-Server-Scripts) is correct. (e.g. for DN 1225, env will be cx_env1225.lua)

     2. Verify that the [_VC port_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details) is [_unblocked_](Accessing-CX-Voice-Components_237207657.html#Open-a-port)on the VC server.

  5. Check if CCM API logged is correct (CORRECT IP/PORT OR FQDN)

  6. Check if CCM returns any info (Delivered 200 and CHANNEL_SESSION_STARTED MUST be returned).

     1. Check if the correct [_VC IP/PORT_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details) in [_CX Voice Channel provider_](Accessing-CX-Voice-Components_237207657.html#CX-Unified-Admin) and that the correct provider is set in the Channel connector.

  7. If CCM returns some messages but no agent is reserved, then try switching CX Voice MRD on AgentDesk off and on.

  8. If you can't switch, then hang up the call, consult with the Support team to clear the conversation from the conversation manager API, and start the call again.

  9. Also, make sure that the agents currently logged in and expecting calls have the same queue assigned to them as noted in Step 2.

  10. If the **AGENT_RESERVED** payload from CCM is giving **[agentExtension] not found** error then make sure to assign an Media-Server extension to that reserved agent and log in to that agent.

  11. If the **AGENT_RESERVED** payload from CCM is giving **[uuid] not found** error then there is a mismatch between the EF CX version and the Voice Connector version. Consult the Support team.

  12. Check if **CALL TRANSFERRED** is shown after **AGENT_RESERVED** payload and no error received from Media-Server.

  13. If "rude rejection" shown with "**Received message: [EslMessage** " then add VC server IP and VC docker container IP to [_Media-Server ACL_](Accessing-CX-Voice-Components_237207657.html#Add-IP-to-Media-Server-ACL)

     1. You may obtain the IP address via the command **docker inspect <containerID>** and reading the **Gateway** field.

  14. If an error is shown after "**Opening ESL Connection** " then check if Media-Server is running, and [_unblock port_](Accessing-CX-Voice-Components_237207657.html#Open-a-port) 8021 on the Media-Server server.

  15. Verify **agentExtension** after **AGENT RESERVED** matches your agent extension on Agent Desk.

     1. If it doesn't then check if another agent is logged in with the same queue.

     2. If it matches and no call is received then consult with the Support team.




![](images/icons/grey_arrow_down.png)If a call starts but the menu does not play

  1. Dial *9664 and verify that the audio can be heard.

     1. If not then try reconnecting your VPN(if remote), and reconnecting your extension, or changing your extension.

     2. If audio can be heard, move to Step 2.

     3. If audio still cannot be heard, then consult the Support team.

  2. Check [_dialplan_](Accessing-CX-Voice-Components_237207657.html#Check-Media-Server-Inbound-IVR-dialplan) on Media-Server to see if the cxIvr.lua script is set.

  3. If previous fixes don't work then consult the Support team




![](images/icons/grey_arrow_down.png)If a call starts but after agent option selection, the call drops

  1. Check [_dialplan_](Accessing-CX-Voice-Components_237207657.html#Check-Media-Server-Inbound-IVR-dialplan) on Media-Server to see if the cxIvr.lua script is set.

  2. Check Media-Server logs to see if an error is logged when the call starts.

  3. Consult the Support team to verify if the [_IVR script_](Accessing-CX-Voice-Components_237207657.html#Media-Server-Scripts) is failing when the agent option is selected.




![](images/icons/grey_arrow_down.png)If a call starts but after agent option selection, an error message plays: "We have encountered an error. Please try again later".

You can troubleshoot this case on the following ends:

#### AgentDesk

  1. Check if any agent is logged in on the AgentDesk.

  2. Confirm that all logged in agent have their tabs open, and did not close them during the ringing call.

  3. Make sure that agents used the appropriate log-out feature instead of closing their tab.

  4. Make sure that agents have microphone permission allowed before receiving any call.




#### Media Server

  1. On the AgentDesk note the agent’s voice extension and open the [Registrations section on the Media Server](Accessing-CX-Voice-Components_237207657.html#Check-agent-extension-registered-on-Media-Server).

  2. Check if the agent’s extension is listed under the **User** column.

     1. If it is listed twice then confirm if any other agent is not using the same extension.

     2. If not listed, then reload the agent tab and make sure that the**CX Voice Connected** message pops up at the top of the page.




![](images/icons/grey_arrow_down.png)If a call starts, agent option is selected and then the call drops after connecting to the agent

  1. Verify that the agent did not get logged out.

  2. Consult with the Support to check the details.




![](images/icons/grey_arrow_down.png)Inbound RONA(Reroute on No Answer)

If a call is not routed to any agent (the call ends abruptly)

  1. Refer to the [_RONA dialplan_](Accessing-CX-Voice-Components_237207657.html#Check-EFSwitch-RONA-dialplan) section.

  2. If the dialplan is not set properly as shown in the [_RONA dialplan_](Accessing-CX-Voice-Components_237207657.html#Check-EFSwitch-RONA-dialplan), then add the following line at the end of the **local_extension** dialplan:




action| lua| vcApi.lua 'rona'| 1| 76| true  
---|---|---|---|---|---  
  
![](images/icons/grey_arrow_down.png)In RONA case if new agent is never assigned

If a call is not routed to any agent (the queue music keeps playing and seems the customer is waiting for a long time)

  1. Check if an agent is logged in on the AgentDesk

  2. Check if CX voice MRD is ready for the agent.

  3. Check if CX Voice is working correctly with no SIP-related errors in the AgentDesk console (F12 in the browser)

  4. Check [_Unified Admin_](Accessing-CX-Voice-Components_237207657.html#CX-Unified-Admin) to see if the expected agent has the correct queue assigned.

  5. Check the[ Voice Connector logs](Accessing-CX-Voice-Components_237207657.html#Voice-Connector-logs) for any errors logged.




## Queue Transfer Scenarios

![](images/icons/grey_arrow_down.png)If a call is connected to the first agent but does not get transferred to the second agent

  1. Verify that the second agent was logged in during the transfer.

  2. Check the Voice Connector logs for any errors logged.

  3. Open the [_Agent Desk config map_](Accessing-CX-Voice-Components_237207657.html#Agent-Desk-config-map).

     1. Note the value of the **STATIC_QUEUE_TRANSFER_DN** field.

     2. Verify that the value is the same in the Media-Server [_Queue Transfer dialplan_](Accessing-CX-Voice-Components_237207657.html#Check-Queue-Transfer-extension-in-Media-Server-Dialplan) as well as the **vcApi.lua** Media-Server [_script_](Accessing-CX-Voice-Components_237207657.html#Media-Server-Scripts) file




## IVR-based Outbound

![](images/icons/grey_arrow_down.png)If an error is shown after contact is added via APIs

  1. Note the response error code.

     1. If contact is added via the Voice connector API, then the HTTP error can be seen in the response.

     2. If the contact is added via the CCM API or the scheduler API, then open the [_CCM logs_](Accessing-CX-Voice-Components_237207657.html#CCM-Logs) and check the Voice connector response codes there.




#### Error 406:

This error indicates that there is an ongoing call with the same contact. To resolve this:

  1. Disconnect the previous call with the same contact number.

  2. If the previous call has disconnected and the error persists, consult with the Support team.




#### Error 400:

This indicates that there is an incorrect field/missing field in the contact provided via the API. To resolve this:

  1. Check the missing/incorrect field in the contact payload logged in the [_VC logs_](Accessing-CX-Voice-Components_237207657.html#Voice-Connector-logs)

  2. Correct that field in the contact payload being sent.




#### Error 500:

This indicates an unexpected error has occurred while dialing the contact. To resolve this:

  1. The error should be described in the [_VC logs_](Accessing-CX-Voice-Components_237207657.html#Voice-Connector-logs) and if it is not understandable, consult the Support team.




#### Error 503:

This indicates an issue with the Dialer database. To resolve this:

  1. Follow the steps in the [**_Troubleshoot database connection_**](Accessing-CX-Voice-Components_237207657.html#Troubleshoot-database-connection) section.




![](images/icons/grey_arrow_down.png)If contact was added but no call was received by the customer

There could be multiple reasons that the customer does not receive the call. To check this:

#### Open [_Dialer logs_](Accessing-CX-Voice-Components_237207657.html#Dialer-logs)

**Errors**| **Troubleshooting Steps**  
---|---  
If a database error is logged| Follow the steps in the [**_Troubleshoot database connection_**](Accessing-CX-Voice-Components_237207657.html#Troubleshoot-database-connection) section.  
If no error is logged and no log is shown with “CAMPAIGN TYPE:”| 

  1. Verify the correct database details are set in the [_Dialer environment variables_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details).
  2. Verify that the **MAX_CONCURRENT_CALLS** field in [_Dialer environment variables_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details) is set to 1 or more.
  3. Verify that the **CALLS_PER_SECOND** field in [_Dialer environment variables_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details) is set to 1 or more.

  
If the error NO EFSWITCH CONNECTION is logged| 

  1. Verify the correct Media-Server details are set in the [_Dialer environment variables_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details).
  2. Verify that Media-Server is up and running.
  3. Consult the subsection [**_Add IP to Media-Server ACL_**](Accessing-CX-Voice-Components_237207657.html#Add-IP-to-Media-Server-ACL).
  4. Apply the fix and wait for the contact to be dialed automatically.

  
If the error **INVALID GATEWAY** is shown| Verify that the [_gateway ID_](Accessing-CX-Voice-Components_237207657.html#Check-Media-Server-gateway-status-and-ID) being set in the contact payload is the correct one  
If the error **GATEWAY DOWN** is shown| [ _Restart the gateway_](Accessing-CX-Voice-Components_237207657.html#Check-Media-Server-gateway-status-and-ID) on Media-Server in the browser.  
If “**CALLED THE CUSTOMER** ” is shown but no call is received| 

  1. Open [Media-Server in the browser](Accessing-CX-Voice-Components_237207657.html#Media-Server-in-browser)
  2. Verify that the IVR number set in the contact payload matches the required [_IVR menu_](Accessing-CX-Voice-Components_237207657.html#Check-Media-Server-Outbound-IVR) in Media-Server.
  3. If the numbers match but the call is still not received, consult the Support Team.

  
  
## Progressive Agent-based Outbound

![](images/icons/grey_arrow_down.png)If an error is shown after contact is added via APIs

  1. Note the response error code.

     1. If contact is added via the Voice connector API, then the HTTP error can be seen in the response.

     2. If the contact is added via the CCM API or the scheduler API, then open the [CCM logs ](Accessing-CX-Voice-Components_237207657.html#CCM-Logs)and check the Voice connector response codes there.




#### Error 406:

This error indicates that there is an ongoing call with the same contact. To resolve this:

  1. Disconnect the previous call with the same contact number.

  2. If the previous call has been disconnected and the error persists, consult with the Support team.




#### Error 400:

This indicates that there is an incorrect field/missing field in the contact provided via the API. To resolve this:

  1. Check the missing/incorrect field in the contact payload logged in the [VC logs](Accessing-CX-Voice-Components_237207657.html#Voice-Connector-logs).

  2. Correct that field in the contact payload being sent.




#### Error 500:

This indicates an unexpected error has occurred while dialing the contact. To resolve this:

  1. The error should be described in the VC logs and if it is not understandable, consult the Support team.




#### Error 503:

This indicates an issue with the Dialer database. To resolve this:

  1. Follow the steps in the [**Troubleshoot database connection**](Accessing-CX-Voice-Components_237207657.html#Troubleshoot-database-connection) section.




![](images/icons/grey_arrow_down.png)If a contact was added but no call was received by the customer

**Check the Dialer logs** :

  1. If a database error is logged, then 

     1. Follow the steps in the [**_Troubleshoot database connection_**](Accessing-CX-Voice-Components_237207657.html#Troubleshoot-database-connection) section.

  2. If no error is logged and no log is shown with “**CAMPAIGN TYPE:** ” then

     1. Verify the correct database details are set in the [_Dialer environment variables_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details).

     2. Verify that the **MAX_CONCURRENT_CALLS** field in [_Dialer environment variables_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details) is set to 1 or more.

     3. Verify that the **CALLS_PER_SECOND** field in [_Dialer environment variables_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details) is set to 1 or more.

  3. If **UNABLE TO REQUEST AGENT FROM VOICE CONNECTOR FOR CALL ID** is shown, note the **error code** logged

     1. If **400** , verify that the contact payload contains no missing/incorrect data.

     2. If **503** , verify that the CX is up and that the [_CCM port_](Accessing-CX-Voice-Components_237207657.html#CCM-Port) is correct.

     3. If **500** , open the [_VC logs_](Accessing-CX-Voice-Components_237207657.html#Voice-Connector-logs) to see what error occurred, and if it is not understandable, consult the Support team.

  4. If an error is shown after **AGENT REQUESTED FOR CALL ID** then refer to the [_database troubleshooting section_](Accessing-CX-Voice-Components_237207657.html#Troubleshoot-database-connection).

  5. If **RECEIVED RESERVED AGENT INFO FOR CALL ID** is not shown within a minute of the **AGENT REQUESTED FOR CALL ID** message then refer to the [_Voice Connector logs_](Accessing-CX-Voice-Components_237207657.html#Voice-Connector-logs).

  6. If a **DATABASE CONNECTION ERROR** is shown, refer to the [**_Troubleshoot database connection_**](Accessing-CX-Voice-Components_237207657.html#Troubleshoot-database-connection) section.

  7. If the error **INVALID GATEWAY** is shown then verify that the [_gateway ID_](Accessing-CX-Voice-Components_237207657.html#Check-Media-Server-gateway-status-and-ID) being set in the contact payload is the correct one. 

  8. If the error **GATEWAY DOWN** is shown, [_restart the gateway_](Accessing-CX-Voice-Components_237207657.html#Check-Media-Server-gateway-status-and-ID) on Media-Server in the browser.

  9. If an **UNEXPECTED ERROR** is logged after the **DIALING AGENT-BASED CONTACT WITH ID** , verify that Media-Server is up and consult the subsection [_Add IP to Media-Server ACL_](Accessing-CX-Voice-Components_237207657.html#Add-IP-to-Media-Server-ACL).

  10. If **AGENT-BASED CONTACT WITH ID <ID> SENT TO EFSWITCH** is shown but no call is received,   
Check the contact **call_result** in the [_database_](Accessing-CX-Voice-Components_237207657.html#Database-commands). 

     1. If it is **CALL REJECTED** , or **NO ANSWER** try the call again since this is not a VC or Dialer issue, but a PSTN problem.

     2. If it is a **UNALLOCATED NUMBER** , please use a contact number that exists.




**If there is no output in the dialer logs, then consult the Voice Connector logs:**

  1. Refer to steps 1-9 in the _VC logs subsection_ of the Inbound section.

  2. If **DIALER INTERNAL SERVER ERROR. CODE 500** is shown

     1. Verify the correct Media-Server details are set in the [_Dialer environment variables_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details).

     2. Verify that Media-Server is up and running.

     3. Consult the subsection [**_Add IP to Media-Server ACL_**](Accessing-CX-Voice-Components_237207657.html#Add-IP-to-Media-Server-ACL).

     4. Check that the Dialer container is running.

     5. Verify that the VC [_environment variables_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details) have the correct Dialer IP and port set.

     6. Verify that the [_Dialer port_](Accessing-CX-Voice-Components_237207657.html#Get-VC%2FDialer-details) is [_open_](Accessing-CX-Voice-Components_237207657.html#Open-a-port).

  3. If **DIALER SERVICE ERROR. CODE 503** is shown

     1. Follow the steps in the [**_Troubleshoot database connection_**](Accessing-CX-Voice-Components_237207657.html#Troubleshoot-database-connection) section.




![](images/icons/grey_arrow_down.png)If a call is received by the customer but not bridged to the agent

  1. Note the extension of your agent in AgentDesk.

  2. Open [_Dialer logs_](Accessing-CX-Voice-Components_237207657.html#Dialer-logs).

  3. Note the value of the **agentExtension** field logged after the **RECEIVED RESERVED AGENT INFO FOR CALL ID** message.

  4. If the two extension values do not match, please check if any other agent has logged on to the same CX with the same queue set in [_Unified Admin_](Accessing-CX-Voice-Components_237207657.html#CX-Unified-Admin).




![](images/icons/grey_arrow_down.png)If a call is received by the customer but an error message plays: "We have encountered an error. Please try again later".

You can troubleshoot this case on the following ends:

#### AgentDesk

  1. Check if any agent is logged in on the AgentDesk.

  2. Confirm that all logged in agent have their tabs open, and did not close them during the ringing call.

  3. Make sure that agents used the appropriate log-out feature instead of closing their tab.




#### Media Server

  1. On the AgentDesk note the agent’s voice extension and open the [Registrations section on the Media Server](Accessing-CX-Voice-Components_237207657.html#Check-agent-extension-registered-on-Media-Server).

  2. Check if the agent’s extension is listed under the **User** column.

     1. If it is listed twice then confirm if any other agent is not using the same extension.

     2. If not listed, then reload the agent tab and make sure that the**CX Voice Connected** message pops up at the top of the page.




## Voice Connector & Dialer

![](images/icons/grey_arrow_down.png)If an error is shown after "Opening ESL Connection"

If you encounter an error message right after **“Opening ESL Connection”** , follow these steps to verify and fix the configuration:

#### 🧰 Debugging Steps

  1. **Verify ESL Port (8021)**

     * Confirm that the ESL port `8021` is open and listening:
[code] sudo netstat -tulnp | grep 8021
[/code]

     * If the port isn’t open, ensure FreeSWITCH is running and the ESL module is loaded.

  2. **Add Docker IPs to FreeSWITCH ACL**

     * Identify the container’s IPv4 address and gateway using:
[code] docker inspect <container_name> | grep -E "IPAddress|Gateway"
[/code]

     * Add both the container’s **IPv4** and **gateway IP** to the [**ESL Access Control List**](Media-Server-Configurations-for-CX-Voice_1341259967.html#Configure-Access-Control-List-\(ACL\)) in FusionPBX.

     * After updating the ACL, **restart FreeSWITCH** to apply changes:
[code] sudo systemctl restart freeswitch
[/code]

  3. **Verify ESL Password**

     * Open the ESL configuration file:
[code] sudo nano /etc/freeswitch/autoload_configs/event_socket.conf.xml
[/code]

     * Ensure that the password in this file matches the one defined in your application or Docker environment variables.

  4. **Restart the Containers**

     * Once the IPs and password are verified, restart your Docker containers to refresh the connection:
[code] docker compose down
           docker compose up -d
[/code]

  5. **Recheck the Logs**

     * Monitor the logs again to confirm that the ESL connection is established successfully:
[code] docker logs <container_name> -f
[/code]



