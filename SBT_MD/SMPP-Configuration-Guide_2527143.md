# CX Knowledgebase : SMPP Configuration Guide

## Unified Admin Configurations

### Channel Manager Configs

#### Channel Type

  * SMPP channel type must be already created as part of bootstrapping of the Channels Connector.




#### Channel Provider 

It's recommended to use the service name of the component in the **"Channel Provider - > Provider's Webhook"** field. However, FQDN can also be used with some additional custom configurations.

  * The name can be any. **E.g.** SMPP Provider.

  * Supported Channel Types will be selected as "SMS"  _(If you want to setup any one only, then select any one)_.

  * Provide the service name of SMPP Connector in the **Provider Webhook** field as http://{SERVICE-NAME}:{SERVICE-PORT}. Replace the {**SERVICE-NAME} and**{**SERVICE-PORT}** in the URL with the component's k3s-based service name and port _(It can be fetched using**k get svc -n expertflow**) _**E.g:**  
For K3s:__[http://ef-smpp-connector-svc:8](http://ef-viber-connector-svc:8080)115  
For Helm Based: [http://cx-channels-smpp-connector-svc:8](http://cx-channels-viber-connector-svc:8080)115


![smpp-2.png](attachments/2527143/494239956.png?width=745)

  


### Channel Connector

  * The name can be any. E.g: SMPP Connector

  * The Channel Provider Interface must be the same as created in the previous step.

  * Provide the values  


![smpp-1.png](attachments/2527143/483983414.png?width=1022)



#### Channel

  * Here we will be creating channels. If we want to set up SMS, we will create a channel under the "SMS" channel type.

  * The name of the channel can be any. **E.g:** SMPP SMS Channel

  * Service identifier:  


    * **For SMS:** it will be the active phone number we have bind for cim.__

  * The rest of the fields are the same as all other connectors. The sample is shown in the image below.


![](attachments/2527143/2566337.png?width=800)

  


### Service Identifier

You need to add a service identifier in the configMap also because on the first call of the API to get Unified Admin configuration we need to add API to get configs

## Configuration Variables

**Variable Name**| **Description**| **Value**| **Type**  
---|---|---|---  
**CCM-API**|  FQDN of the machine where Customer-Channel-Manager is deployed.| _https://cimdemo.expertflow.com_|  String100  
**SMPP-SECURE**|  Is Smpp secured| false| Boolean  
**SMPP-REMOTE-IP-ADDRESS**|  Smpp remote IP address| 127.0.0.1| String100  
**SMPP-REMOTE-PORT**|  Smpp remote port| 2775| PositiveNumber  
**SMPP-FROM-NUMBER**|  This is the source address (range) that will be used to send messages via SMPP. Customer replies will also be received on the same address.| 1218 or any| String100  
**SMPP-SYSTEM-ID**|  Smpp System Id| smppclient1| String100  
**SMPP-PASSWORD**|  Smpp password| password| String100  
**SMPP-SYSTEM-TYPE**|  The SMPP system administrator will provide this value, which when required, is usually a short text string.| SMS| String100  
**SMPP-BIND-TYPE**|  For Transmitter bind (TX) set 0, for Receiver bind (RX) set 1, and for Transceiver bind (TRX) set 2| 2| String100  
**SMPP-NUMBER-TYPE**|  For numeric format set 0, for alphanumeric format set 1| 0| String100  
**PUBLISHER-ENABLE**|  If you want to publish delivery sms| true/false| Boolean  
  
  

