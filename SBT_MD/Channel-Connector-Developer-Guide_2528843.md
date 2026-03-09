# CX Knowledgebase : Channel Connector Developer Guide

## Purpose

The purpose of this guide is to provide developers with information on how to create a channel connector that connects multiple media [channels](Omnichannel-Engagement_2529366.html) with Expertflow CX for conducting customer interactions.Audience

By using this guide, developers can create REST API clients and expose specific webhooks for a channel connector.

### Assumptions and Constraints

It should be noted that Expertflow CX is a channel-agnostic chat solution, which means that Channel Connector Developers can connect using any chat and voice media channels. The integration of channels with the connector is left at the discretion of the developer and not included in this guide.

## Getting Started

Expertflow CX comes out of the box with some channel connectors for some channel types. You can add more channels of certain types following this guide.

A Channel Connector communicates with Expertflow CX over REST APIs. The connector must expose a webhook to receive events from Expertflow CX. The connector must call the endpoint `cim-messages` for the webhook to work properly. ` `

1| **CCM**|  CCM stands for Customer Channel Manager.   
---|---|---  
2| **Channel Connector**|  Allows media interfacing with CCM (Expertflow CX).  
3| **Customer Channels**|  Please see [here](Omnichannel-Engagement_2529366.html) for details on media channels.  
  
## Next Steps

**1.**| [**Register Channel Connector**](Register-Channel-Connector_2528408.html)|  Define a ChannelConnector in Unified Admin to send and receive customer messages to and from Expertflow.  
---|---|---  
**2.**| [**Channel Connector Configurations**](Channel-Connector-Configuration_2527073.html)|  The channel connectors needs to update configurations in case of any changes/updates made in Unified Admin console.   
**3.**| **Sending**[**messages**](CIM-Messages_2530195.html)|  The channel connector needs to call Post **_/message_** REST APIs to send messages to CCM. The format of the messages is described in detail in [Messages](CIM-Messages_2530195.html) section.  
**4.**| **Receiving**[**messages**](CIM-Messages_2530195.html)|  The connector needs to expose a Webhook to receive messages from CCM. The URL for the webhook will be specified in the Unified Admin Console as explained in [Register Channel Connector](Register-Channel-Connector_2528408.html).  The format of the messages is described in detail in [Messages](CIM-Messages_2530195.html) section.  
  
  


  


  


  


  

