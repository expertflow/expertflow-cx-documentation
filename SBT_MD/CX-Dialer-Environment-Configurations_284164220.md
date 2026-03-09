# CX Knowledgebase : CX Dialer Environment Configurations

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
