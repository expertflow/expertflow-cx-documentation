# CX Knowledgebase : Outbound Flows Environment Configurations

Following are the details of all the variables available in **helm chart** of Campaigns (Outbound Flows). 

### Environment Variables for conversation-studio

**Variable**| **Description**  
---|---  
TZ| Timezone to be used by the Campaign Studio component. For a list of all the supported time-zones, refer to this [page](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).  
FQDN| FQDN of the EF CX deployment that you want to integrate campaigns with  
CAMPAIGNS_BACKEND| URL of the campaigns backend service.  
SCHEDULER_URL| URL of the EF CX scheduler service.  
URIForWebhook| Base URL to be used for the registering webhooks on the scheduler. This URL should be accessible by the scheduler for it to deliver notifications successfully.  
GATEWAY_ID| The default gateway id to be displayed in **Action node** for voice based campaigns. This can also be configured later for each action from the nodered UI.  
IVR_EXTENSION| The default IVR extension to be displayed in **Action node** for voice based IVR campaigns. This can also be configured later for each action from the nodered UI.  
UCCE_FQDN| The FQDN/IP Address of the UCCE deployment  
UCCE_USERNAME| The username for the UCCE deployment  
UCCE_PASSWORD| The password of the UCCE deployment  
UCCX_FQDN| The FQDN/IP Address of the UCCX deployment  
UCCX_USERNAME| The username for the UCCX deployment  
UCCX_PASSWORD| The password of the UCCX deployment  
ALLOW_CISCO_SELF_SIGNED_CERTS| When calling the Cisco APIs, should self-signed certificates be ignored. Default value is `true`.  
  
### Environment Variables for campaigns-backend

**Variable**| **Description**  
---|---  
PORT| The port on which the backend server will listen on.  
LOG_LEVEL| The level of logs to print.  
NODERED_URI| Nodred service URL, accessible within the current network.   
NODERED_USERNAME| Username to be used for the Node-RED authentication (If authentication is enabled in Node-RED).  
NODERED_PASS| Password for the Node-RED authentication (If authentication is enabled in Node-RED).  
UPLOAD_CSV_BATCH_SIZE| Size of the batch that will be formed when uploading contacts from a CSV file.  
NODERED_SYNC_BATCH_SIZE| Size of the batch when syncing contacts between backend and relative Node-RED flow.  
CCM_URL| URL of the CCM service.  
SCHEDULER_URL| URL of the scheduler service.
