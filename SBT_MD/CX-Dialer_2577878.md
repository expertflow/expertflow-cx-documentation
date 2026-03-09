# CX Knowledgebase : CX Dialer

CX Dialer is a CX Voice component for outbound dialing. It receives dialing requests via the CX Dialer APIs, enqueues them in its Dialer database, dials out following the **Dialing Flow** , and returns call results to the CX VoiceConnector. For dialing requests where agent reservation is required it initiates agent reservation request to CX Routing via VoiceConnector. 

## Dialing Flow

  1. The dialer will periodically query the database and take note of all the campaigns and the number of their contacts present.

  2. Based on the available Call Slots: 

     1. If the Number of Call Slots are more than the number campaigns

        1. At least one contact picked from each campaign.

        2. Preference given to campaign with least contacts.

        3. Dialing order for each campaign is FIFO, if multiple contacts from same campaign are picked.

        4. Overall dialing order is campaign with lowest contacts first.

     2. If the Number of Call Slots are less than or equal to the number of campaigns

        1. First for each campaign contacts are ordered by **received_time** ascending(from oldest added, to newest added)

        2. For each campaign the oldest added contact is put into a list

        3. This list is sorted by **received_time** ascending(from oldest added, to newest added)

        4. From this list we pick the first X number of contacts where X = free slots

  3. These contacts are then sequentially processed based on the campaign type.




### IVR Campaigns

  1. For IVR based campaigns, the IVR number is taken from the contact entry if set.

  2. If the IVR number is not provided in the contact entry then the default IVR specified in the dialer configuration is used.

  3. The dialer checks via EFSwitch ESL if the gateway provided is valid.

     1. If it is valid, then the following command is sent to EFSwitch to initiate the call: 
[code] originate {session_in_hangup_hook=true,domain_name=EFSWITCH-IP,record_session=true,origination_caller_id_name=IVR-NUMBER,origination_caller_id_number=IVR-NUMBER,call_direction=outbound,origination_uuid=call_uuid}sofia/gateway/GATEWAY-ID/CUSTOMER-NUM IVR-NUMBER XML EFSWITCH-IP
[/code]

     2. If invalid, the contact status is set to 'failed' and it will not be redialed.

     3. If the gateway is down then the contact status is set back to 'pending' to be tried again later.

  4. The call slots are decremented by 1.

  5. Once the call ends, the dialer receives a call-ended event from the EFSwitch ESL and:

     1. Stores the call result in the database and sets the status to 'ended'.

     2. Sends the [call result to the Voice Connector ](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-991f0dc8-333e-45fb-b220-4e4a37896d70?ctx=documentation)for a Delivery notification to be sent to the CCM.

     3. Increments the call slots by 1.




### Agent Campaigns

  1. If the campaign call type is of 'AGENT', then the contact status is set to 'agent_pending' and call information is [posted to the voice connector API](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-877b34b9-e9ce-447c-8c30-48f4c3e0b42d?ctx=documentation).

  2. The call slots are decremented by 1.

  3. The voice connector [sends back the following payload](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-afa78280-28e7-4d82-9265-db6b623b9eb6?ctx=documentation) when it received either an agent reserved or no agent available notification from the CCM:

  4. If no agent was available, the dialer sets the contact status to 'pending' to try again the next time it queries for pending contacts.

  5. If agent was reserved, then the dialer checks via EFSwitch ESL if the gateway provided is valid.

     1. If invalid, the contact status is set to 'failed' and it will not be redialed.

     2. If the gateway is down then the contact status is set back to 'pending' to be tried again later.

     3. In either case call information is [sent to the voice connector](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-bd5ecd82-5531-4109-a283-f44a6ca7023c?ctx=documentation) which will send an END_CHAT payload to the CCM to close the conversation and free up the agent.

  6. The following command is sent to EFSwitch which will call the customer and bridge the answered call to the agent:
[code] originate {ignore_early_media=true,session_in_hangup_hook=true,sip_h_X-Destination-Number=SERVICE-IDENTIFIER,sip_h_X-CallType=PROGRESSIVE,customer_number=CUSTOMER-NUM,sip_h_X-CALL-VARIABLE0=CALL-ID,sip_h_X-Call-Id=CALL-ID,domain_name=EFSWITCH-IP,record_session=true,call_direction=outbound,sip_h_X-queueType=NAME,sip_h_X-queue='QUEUE_NAME',origination_uuid=CALL-ID,origination_caller_id_name=AGENT-EXTENSION,origination_caller_id_number=AGENT-EXTENSION,sip_h_X-agentExtension=AGENT-EXTENSION}sofia/gateway/GATEWAY-ID/CUSTOMER-NUM agent XML EFSWITCH-IP
[/code]

  7. Once the call ends, the dialer receives a call-ended event from the EFSwitch ESL and:

     1. Stores the call result in the database and sets the status to 'ended'.

     2. Sends the call result [to the Voice Connector](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-991f0dc8-333e-45fb-b220-4e4a37896d70?ctx=documentation) for a Delivery notification to be sent to the CCM.

     3. Increments the call slots by 1.

     4. If the customer had dropped the call after answering (before the agent could be bridged):

        1. The dialer detects the case via the call variables in the call-ended event.

        2. Call information is [sent to the voice connector](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-bd5ecd82-5531-4109-a283-f44a6ca7023c?ctx=documentation) which will send an END_CHAT payload to the CCM to close the conversation.




## Database Structure and Management

### Schema

There is a single table named **contacts** in the dialer database with the following schema:

**Field**| **Description**| **Type**| **Provided By**  
---|---|---|---  
id| Unique UUID identifier used to identify this contact and call| VARCHAR(40) Not Null| Campaign Manager  
customer_number| The number to be dialed| VARCHAR(20) Not Null| Campaign Manager  
campaign_type| Describes whether happens when the called number will be played an IVR menu or bridged to an agent. Can be set to IVR or AGENT| VARCHAR(20) Not Null| Campaign Manager  
gateway_id| The UUID of the EFSwitch gateway to be used to dial the customer number| VARCHAR(40) Not Null| Campaign Manager  
campaign_id| The campaign id| VARCHAR(40)Not Null| Campaign Manager  
status| The state the contact is in. Can be any of the following: 

  * **pending** : awaiting processing by the dialer
  * **agent_pending** : awaiting an agent to be received from voice connector
  * **dialed** : contact has been sent to EFSwitch for dialing and is now waiting for result
  * **ended** : call result for this contact was received from EFSwitch
  * **stopped** : stopped via the campaign Stop API
  * **failed** : an error occured while dialing e.g. EFSwitch connection failed, Invalid gateway etc

| VARCHAR(20)| Dialer  
call_result| The result of a call as received from EFSwitch e.g. NORMAL_CLEARING, USER_BUSY etc| VARCHAR(40)| Dialer  
received_time| The time at which the contact was received by the dialer| DateTime| Dialer  
dial_time| The time at which:

  * the contact was sent by the dialer to EFSwitch to be dialed or
  * an agent was requested from the CCM against this contact

| DateTime| Dialer  
ivr| An extension number that determines the IVR to be played when the customer answers. Optionally set if the **campaign_type** field is set to **IVR**|  VARCHAR(20)| Campaign Manager  
dialing_mode| The dialing mode of this agent-based contact. Can be PREDICTIVE, PREVIEW or PROGRESSIVE. Currently only PROGRESSIVE is supported. Required if the **campaign_type** field is set to **AGENT**|  VARCHAR(20)| Campaign Manager  
routing_mode| Determines whether the agent-based contact will be routed to an agent picked from a certain queue or to a specific agent. Can be AGENT or QUEUE. Currently only QUEUE is supported. Required if the **campaign_type** field is set to **AGENT**|  VARCHAR(20)| Campaign Manager  
queue_name| The name of the queue from which the agent will be picked from for the agent-based contact if routing_mode is set to QUEUE. If left empty, the default queue set in the CX Voice channel will be used| VARCHAR(20)| Campaign Manager  
resource_id| Required if the **campaign_type** field is set to **AGENT**. If the routing_mode field is set to:

  * AGENT, then this must contain the CX Agent ID
  * QUEUE, then this can optionally be set to the CX queue ID from which the agent will be picked

Not in use| VARCHAR(40)| Campaign Manager  
priority| The contact priority between 1-10. Currently not in use| Integer| Campaign Manager  
campaign_contact_id| Not in use| VARCHAR(40)| Campaign Manager  
start_time| The contact cannot be dialed before this time. Currently not in use| DateTime| Campaign Manager  
end_time| The contact cannot be dialed after this time. Currently not in use| DateTime| Campaign Manager  
scheduling_metadata| The schedulingMetadata JSON object from the CX Contact Message. Contains info that can be used when dialing IVR calls. To Be added in future version.| JSONB| Campaign Manager  
tenant_metadata| Optional. Contains extra tenant info e.g. Media Server domain used for dialing. To Be added in future version.| JSONB| Campaign Manager  
tenant_id| CX Tenant ID. To Be added in future version.| VARCHAR(40)| Campaign Manager  
  
### Start/Stop/Purge Campaigns from database

The dialer exposes three APIs that can be called by the campaign manager to start, stop or purge campaigns:

  * Set this campaign's [stopped contacts' status to 'pending'](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-cad99748-79d9-4ed2-a1c6-427197a0ded6?ctx=documentation).

  * Set this campaign's [pending contacts' status to 'stopped'](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-2caafdd0-e6cc-4790-a5eb-ca44d7f501d3?ctx=documentation).

  * [Remove all pending contacts](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-35b26aa7-15fc-4f42-986d-d9c8e94a896c?ctx=documentation) of a campaign with this campaign ID.




### Data Lifetime

There is no limit to the data that can be stored in the database, nor is there any expiry/archival time for entries. However there is a scheduled task dedicated to the following case:

  * If the dialer either sends a contact to EFSwitch for dialing, or requests an agent for a contact from the voice connector, the status of that contact will be set to **dialed** or **agent_pending** respectively. 

  * Subsequently if the database connection is lost when either EFSwitch publishes the call result or the agent information is received by dialer from the voice connector, then the dialer will not be able to access the respective contact and its status will therefore stay stuck on the **dialed** or **agent_pending** status. 

  * A periodic function checks each 10 minutes(non-configurable) for contacts for which the (configurable) `MAX_CALL_TIME` limit has exceeded, i.e. the difference between the current time and the contact’s **dialed_time** field is greater than the `MAX_CALL_TIME`.

  * If the `MAX_CALL_TIME` limit is reached, then the contact is set back to the pending status to be processed again.




## Additional/Miscellaneous Behavior

### Throttling

In order to prevent the dialing speed from exceeding the value allowed by the SIP trunk or EFSwitch, the dialer throttles it dialing speed via the environment variable `CALLS_PER_SECOND`.

### Dialer Status

[This API](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-801e3f2a-a33e-4d5a-819c-31b90851c707?action=share&source=copy-link&creator=21457238&ctx=documentation) can be used to check the configured value of **MAX_CONCURRENT_CALLS** and the current number of active calls i.e. contacts with the **dialed** or **agent_pending** state.

## Terminologies

### Call Slots

The number of contacts that will be chosen for dialing from the pool of contacts in the database. This value is calculated by subtracting the number of contacts in the **dialed** or **agent_pending** state from the environment variable `MAX_CONCURRENT_CALLS`.

## Dialer Configuration Parameters

The configuration parameters and their expected values are described in this table: 

**Config Params**| **Expected Values**| **Notes**  
---|---|---  
**DB_URL**|  IP Address e.g. 192.168.1.2| The URL of the database from which contacts are to be pulled. Change this to the IP address of the current server  
**DB_USERNAME**|  Text e.g. admin| The dialer database username  
**MAX_CONCURRENT_CALLS**|  Number e.g. 10| Maximum number of calls that can be active at a timeThis value must **always** be less than the maximum concurrent calls allowed on the EFSwitch SIP trunk in use for outbound calls. If set higher, then the extra calls created by the dialer will be **stuck** in the database on the **dialed** state. These stuck calls can only be removed by directly interacting with the database. Before setting this value also account for the call volumes and speed of the **other types of calls** taking place on the EFSwitch (manual outbound, IVR inbound etc).To confirm the maximum concurrent calls allowed by the trunk, contact your SIP Trunk provider.  
**DB_PASS**|  Text e.g. abc123| The dialer database password  
**DB_PORT**|  Number e.g. 5432| The dialer database port (Default 5432)  
**DB_NAME**|  Text e.g. dialer| The dialer database name  
**DB_CONN_TIMEOUT**|  Number e.g. 3000| Maximum time allowed (in milliseconds) for connecting to the database. (Default 3000)  
**ESL_IP**|  IP Address e.g. 192.168.1.2| IP address of the EFSwitch ESL to use. (The IP of the server that EFSwitch is deployed on)  
**ESL_PORT**|  Number e.g. 8021| Port of the EFSwitch ESL. (Default 8021, Same as in EFSwitch settings [here](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/75825154))  
**ESL_PASSWORD**|  Text e.g. ClueCon| Password for the EFSwitch ESL. (Default ClueCon, Same as in EFSwitch settings [here](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/75825154))  
**DEFAULT_IVR**|  IVR Dialing number e.g. *9664| Default IVR to play in case of none provided for outbound call (Default *9664)  
**SERVICE_IDENTIFIER**|  Number e.g. 1218| Service Identifier for the voice connector. (Default 1218, set in EFSwitch IVR settings [here](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/75825154))  
**VOICE_CONNECTOR**|  FQDN with IP Address and port e.g. <http://192.168.1.2:4321>| Webhook of the voice connector. Format: [http://VC-IP:Port](http://VC-IPPort)  
**ESL_CONNECT_DELAY**|  Number e.g. 60| Delay in seconds between checking EFSwitch ESL connection status  
**CONTACT_RETRIEVAL_DELAY**|  Number e.g. 20| Delay in seconds before retrieving contacts from the dialer database  
**CALLS_PER_SECOND**|  Number e.g. 10| The maximum number of calls that can be generated in a secondThis value must **always** be less than the **sessions-per-second** value in **EFSwitch** otherwise the excess calls created per second by the dialer will be **stuck** in the database on the **dialed** state. These stuck calls can only be removed by directly interacting with the database. To confirm the value of **sessions-per-second** on **EFSwitch** :

  * Open the EFSwitch command line on the EFSwitch server via the command**fs_cli -p <EFSwitch-CLI-Password> **
  * Run the command **fsctl sps** and note the value displayed.
  * Before setting this value also account for the call volumes and speed of the **other types of calls** taking place on the EFSwitch (manual outbound, IVR inbound etc).

  
**MAX_CALL_TIME**|  Number e.g. 60| The time in minutes for which each contact in the database is allowed to stay on the **dialed** or **agent_pending** states, after which it’s state is manually updated to **pending** state to be retriedThis value must **always** be greater that the**Agent TTL** value in the **EF CX** **Channel Settings** in **Unified Admin**.  
**LOG_LEVEL**|  INFO/DEBUG| Determines the amount of detail in the logs. Default is **INFO** , and for more detailed logs the value should be **DEBUG**.  
  
Includes Outbound campaign dialing (IVR and Agent-based), Multiple campaign handling, Call result saving, Returning call results to CX, Campaign controls(start, stop, purge)

## Features

**Features**| **Description**  
---|---  
**Outbound IVR campaigns**|  Dial out a call to the customer and play a specified IVR menu.  
**Outbound Agent-based campaigns****(Progressive Mode)**|  Reserve an agent against a customer, dial a call to the customer, and connect them to the reserved agent.  
**Multiple campaign dialing**| 

  * Algorithm decides how many calls per campaign to dial out for any given number of free call slots.
  * If free slots greater than total campaigns, then contacts are picked from each campaign in order of smallest campaign to largest.
  * Within a campaign, contacts are picked according to the FIFO order(queue).
  * If free slots lesser than or equal to total campaigns then 1 contact each picked from as many campaigns as there are slots, in order of smallest campaign to largest.

  
**Record call results**|  Record result of each call e.g. Normal clearing, user busy, invalid gateway etc and store in database along with other contact information.  
**Send call results to CX**|  Send result of each agent-based call as Delivery notifications to EFCX via the voice connector.  
**Campaign controls**| 

  * Stop pending contacts of a campaign.
  * Start stopped contacts of a campaign.
  * Purge pending contacts of a campaign.

  
  
## Limitations

  * No way to switch between LIFO/FIFO/priority when select contacts from within a campaign.

  * No priority when allotting call slots to campaigns.

  * Cannot add more than 1 contact at a time to database.

  * If EFswitch connection is lost, then call counter will be initialized to zero as a precaution, however this may mean that total calls will go over the set limit.

  * Contacts do not have any expiry time.

  * Before dialing each contact, the dialer checks if the gateway on EFSwitch is up. If it is down, the contact status is set back to **pending**. There is no limit set for how many retries are allowed.

  * Multiple campaigns cannot have the same contact number.

  * There is no way to detect invalid IVR numbers and call results for invalid IVR calls will be successful results(NORMAL_CLEARING).




  


  

