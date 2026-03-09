# CX Knowledgebase : Channel Related Objects

Expertflow CX uses the following objects for customer channels and related.

**ChannelType**|  A ChannelType represents the type of communication channel, e.g., WhatsApp, Viber, or Webchat. There can be multiple channels of the same Channel Type.  
---|---  
**Channel**|  A Channel is a set of configurations defining:

  * Service Identifier: uniquely identifies a channel and is available in channel data parameters. This is used by customers to initiate requests from this channel to the business.
  * Routing Mode: determines if channel requests should be pushed to agents (Push mode), or should be parked to a List where agents can pull them off (Pull mode)
  * Customer Inactivity Timeout: determines the customer's inactivity duration on this channel. Once this time is reached, the channel session of the customer is automatically closed by the system.
  * Channel Connector: the authorized integration interface for the customer channel

  
**ChannelSession**|  A ChannelSession is a logical object that represents that the customer is currently active on the respective Channel with the system. It is contained within a [Conversation](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/155222046/4.5+Conversation+Objects).On receiving a new inbound/outbound event, the ChannelManager creates a ChannelSession with the customer, with an inactivity expiry duration; i.e. the time until the ChannelManager waits for the customer to reply before closing this session, due to inactivity. Each **Channel Session** contains some channel data passed to it by the ChannelConnector. It's a set of key-value pairs that a ChannelConnector can set at the time of sending the message. For example, for web chat, the channel data includes the browser info (Chrome, Safari), locale info of the customer, and, any pre-chat form data that was submitted while initiating the chat.The channel data is available to agents on the Agent Desk under the [Active Channels pane](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2527849/Accept+a+Conversation#View-Active-Channels).   
**Channel Connector**|  A **Channel Connector** is a wrapper implementation between a **Customer Channel** and Expertflow CX to exchange customer communication on the channel.For each new request received from a customer on a channel, it is received on the respective channel connector for that channel. Channel Connectors receive new requests from a respective customer channel, transform them in a format readable by Expertflow CX components, and forward them to the ChannelManager to process the request. Responses from the business (i.e. messages sent by the conversation bot or agents) to customers are received by the Channel Connector and transferred to the customer in the customer-facing channel format.  
**Channel Provider**|  A ChannelProvider is a third-party service provider for a customer channel. For example, Dialog360 and Twilio are channel providers for WhatsApp. A ChannelProvider defines the integration interface for channel connectivity. Channel Providers are configured and attached to **Channel Connectors** of the respective Channel.  
  
**Related Topics**

  * See [Channel Connector Developer Guide](Channel-Connector-Developer-Guide_2528843.html) for developing a new Channel Connector.

  * See how to create new Channel Types, Channels, and Channel Connectors from the [Unified Admin App.](Unified-Admin-Guide_2524407.html)



