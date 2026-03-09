# CX Knowledgebase : 360-Connector Configuration Guide

This document provides the necessary endpoints, parameters, and configuration details to help organizations set up seamless messaging between customers, agents, and bots through WhatsApp using the 360-connector.

## Register Webhook

360-connector expects an HTTP POST request to this endpoint {FQDN}/configs/webhook with the following query params

**Query Param**| **Description**  
---|---  
**url**|  This represents the URL of 360-connector, where notifications from 360Dialog will be received.  
e-g {FQDN}/360notifications   
**hostUrl**|  The default base URL for the 360dialog WhatsApp API i-e [https://waba.360dialog.io](https://waba.360dialog.io)Use the following URL for the 360dialog sandbox [https://waba-sandbox.360dialog.io](https://waba.360dialog.io)  
**apiKey**|  the key/token of the WhatsApp account. To get the key for the sandbox, add the 360dialog sandbox number in your WhatsApp contact and send a WhatsApp message from your phone to the phone number `4930609859535`**** with the content `START `(`START`must be in all UPPERCASE).  
**authorization**|  This is the WhatsApp number, which is used to authenticate the header whenever 360-connector receives a notification from 360Dialog. Its format should be the same as defined in serviceIdentifier in Channel Configuration in Unified-Admin.  
e-g 41762884806  
  
## Get Webhook

If the webhook URL is already set, make a GET request to this endpoint {FQDN}/configs/webhook, to retrieve the existing resource.

**Query Param**| **Description**  
---|---  
**hostUrl**|  The default base URL for the 360dialog WhatsApp API i-e <https://waba.360dialog.io>  
Use the following URL for the 360dialog sandbox [https://waba-sandbox.360dialog.io](https://waba.360dialog.io)  
**apiKey**|  the key/token of the WhatsApp number.  
  
## Unified Admin Configurations

### Channel Manager Configs

  * The following variables first need to be added as "customer-attributes" in "channel provider" on **unified-admin.**

  * Provide the service name of 360 Connector in the **Provider Webhook** field as http://{SERVICE-NAME}:{SERVICE-PORT}. Replace the {**SERVICE-NAME} and**{**SERVICE-PORT}** in the URL with the component's k3s-based service name and port _(It can be fetched using**k get svc -n expertflow**) _**E.g:**  
For K3s:__[http://ef-360-connector-svc:8080](http://ef-viber-connector-svc:8080)  
For Helm Based: [http://cx-channels-connect360-svc:8080](http://cx-channels-viber-connector-svc:8080)  


![360-connector.png](attachments/2531584/483754242.png?width=998)
  * Then we need to set their values in "channel-connector" on unified-admin.


![](attachments/2531584/2551234.png?width=476)

  


  


**Variable Name**| **Description**| **Size**| **Required**| **Example**  
---|---|---|---|---  
HOST-URL| HOST-URL contains the URL of the Channel Provider such as 360Dialog. | String100| YES| <https://waba.360dialog.io>  
API-KEY| API-KEY contains the token/key for the Channel Provider.  
| String100| YES| Q*****************HAK  
  
  

