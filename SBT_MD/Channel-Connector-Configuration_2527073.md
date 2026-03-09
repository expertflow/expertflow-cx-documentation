# CX Knowledgebase : Channel Connector Configuration

The channel configurations are the custom attributes that are defined in Unified Admin > Add Channel Provider, as mentioned in [Register Channel Connector](Register-Channel-Connector_2528408.html). These custom attributes are required by channel provider to integrate the channel with channel connector. For example, in order to integrate with Facebook chat, API Key is required. This is a custom attribute that can be added in Unified Admin when defining Facebook as channel provider. There are two API's available to interact with the channel configurations:  
  
## Add Channel Configuration (Push-based API)

This API needs to be exposed by 3rd-party channel connector and will be used by CCM to push updates to the 3rd-party connectors in case of any changes/updates made on Unified Admin console. The endpoint is fixed as `connector-configurations`. FQDN can be specified by the connector.

This will be a POST/`connector-configurations `API call. The request body will contain the following information:

**Property**|  Type| **Description**  
---|---|---  
serviceIdentifier REQUIRED| String| Id of the channel  
connectorConfigurationsREQUIRED | List<Attribute>| to update custom attribute in Unified Admin.Attributes are:

  * key - String
  * type - ValueType
  * value - Object

  
  
![](images/icons/grey_arrow_down.png)Payload
[code] 
    {
        "serviceIdentifier": "123124",
        "connectorConfigurations": [
            {
                "key": "HOST-URL",
                "type": "String100",
                "value": "https://waba-sandbox.360dialog.io"
            },
            {
                "key": "API-KEY",
                "type": "String100",
                "value": "X4IpWk_sandbox"
            }
        ]
    }
[/code]

## Get Channel Configuration (Pull-based API)

This API will be available to 3rd-party channel connectors to get channel connector configurations from CCM. 

This will be a `GET {{FQDN}}/ccm/channel-connectors/configurations/:serviceIdentifier `API call. The response will include the following properties:

**Property**|  Type  
---|---  
key | String  
type| ValueType  
value| Object  
  
![](images/icons/grey_arrow_down.png)Payload
