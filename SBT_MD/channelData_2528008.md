# CX Knowledgebase : channelData

**Object Name**|  channelData  
---|---  
**Description**|  This object contains the channel related data.   
  
**Parameter**| **Type**| **Description**  
---|---|---  
channelCustomerIdentifier` `REQUIRED| String| It is a unique ID to identify a customer for a channel. For example, for WhatsApp, MSISDN/cell number will be used. For facebook, facebook ID will be used.   
serviceIdentifier REQUIRED| String| This is the service identifier of the service that the customer dialed or reached. It could be a DN (Dialed Number) such as a WhatsApp number, any website URL, Facebook ID, Viber ID.   
requestPriority` `OPTIONAL| Int| By default, the routing priority for every request is “FIFO - first in, first out”. However, request priority can be set by the client. 10 means highest priority and 0 means least priority.  
customerfirstName OPTIONAL | String| Channel connector sets the first name of the customer from channel profile. E.g. Display name from WhatsApp and Facebook is set here in this field.   
customerLastName OPTIONAL | String| Channel connector sets the last name of the customer from channel profile. E.g. Display name from WhatsApp and Facebook is set here in this field.   
additionalAttributes OPTIONAL| List| Any information related to the particular channel can be sent here in the form of `key: value` pairs.
