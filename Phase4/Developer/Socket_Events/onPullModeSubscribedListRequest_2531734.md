# CX Knowledgebase : onPullModeSubscribedListRequest

**Event Name**|  onPullModeSubscribedListRequest  
---|---  
**Event Description**|  Event is triggered when a new chat is initiated by the customer in one of the subscribed lists. It is also triggered when an agent leaves a chat  
**Emitter**|  Agent Manager  
**Action**|  Possible values are:

  * PULL_MODE_LIST_REQUEST_RECEIVED
  * PULL_MODE_LIST_REQUEST_STATE_CHANGED

  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
pullModeEvent| type: Stringdescribes the properties of the chat session| 

  1. id - String - system generated channel session ID
  2. Channel Session - Channel Object - Conversation session details
  3. Service Identifier -

  
type| type: String

  * PULL_MODE_LIST_REQUEST_RECEIVED
  * PULL_MODE_LIST_REQUEST_STATE_CHANGED

|   
conversationId| type: String| 
[code] 
    {
        "pullModeEvent": "{\"id\":\"67c58d36956d765cfc278e0f\",\"channelSession\":{\"participantType\":\"ChannelSession\",\"id\":\"67c58d36d9244213fbf321d0\",\"participantType\":\"ChannelSession\",\"channel\":{\"id\":\"6737304a7f433c0c29ee93b2\",\"name\":\"pull\",\"serviceIdentifier\":\"1133\",\"defaultOutbound\":false,\"tenant\":{\"id\":\"678f7e30f718dd632e3090b4\",\"name\":null},\"channelConfig\":{\"id\":\"678f7e30f718dd632e3090b5\",\"channelMode\":\"HYBRID\",\"conversationBot\":\"\",\"responseSla\":0,\"customerActivityTimeout\":6000,\"customerSla\":{\"totalDuration\":null,\"action\":null,\"startTime\":null},\"customerIdentificationCriteria\":{\"value\":null},\"routingPolicy\":{\"agentSelectionPolicy\":\"LONGEST_AVAILABLE\",\"routeToLastAgent\":true,\"routingMode\":\"PULL\",\"routingObjectId\":\"67372f8d58db250027b8e917\",\"agentRequestTtl\":6000},\"botId\":\"6712cf4bfb156449bb04ce99\"},\"channelConnector\":{\"id\":\"6712cb370b72db03b37236b9\",\"name\":\"web\",\"channelProviderInterface\":{\"id\":\"6712cb300b72db03b37236b7\",\"name\":\"web\",\"supportedChannelTypes\":[{\"id\":\"671270060b72db03b37236ad\",\"name\":\"WEB\",\"channelLogo\":\"_WEB.svg\",\"isInteractive\":true,\"mediaRoutingDomain\":\"6305de07166ba1099d11d8e6\"}],\"providerWebhook\":\"http://ef-web-channel-manager-svc:7000\",\"channelProviderConfigSchema\":[]},\"channelProviderConfigs\":[],\"tenant\":{\"id\":\"67aa110f0bda607923ca9bfa\",\"name\":null}},\"channelType\":{\"id\":\"671270060b72db03b37236ad\",\"name\":\"WEB\",\"channelLogo\":\"_WEB.svg\",\"isInteractive\":true,\"mediaRoutingDomain\":\"6305de07166ba1099d11d8e6\"}},\"customer\":{\"_id\":\"67c58d36d66fbd82f98990cd\",\"firstName\":\"testttt\",\"phoneNumber\":[],\"isAnonymous\":true,\"__v\":0,\"web\":[\"0991222\"],\"urlTest2\":\"https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2528142/Agent+Desk+Permissions+-+Resource+Scope+Groups+Mapping\"},\"customerSuggestions\":[],\"channelData\":{\"channelCustomerIdentifier\":\"0991222\",\"serviceIdentifier\":\"1133\",\"requestPriority\":0,\"customerFirstName\":\"testttt\",\"customerLastName\":null,\"additionalAttributes\":[{\"key\":\"WebChannelData\",\"type\":\"WebChannelData\",\"value\":{\"browserDeviceInfo\":{\"browserId\":null,\"browserIdExpiryTime\":null,\"browserName\":null,\"deviceType\":null},\"queue\":\"\",\"locale\":{\"timezone\":null,\"language\":null,\"country\":null},\"formData\":{\"id\":0.6922185926503306,\"formId\":\"676abb5d245290002736779a\",\"filledBy\":\"web-widget\",\"attributes\":[{\"value\":\"testttt\",\"key\":\"first_name\",\"type\":\"string\"},{\"value\":\"0991222\",\"key\":\"phone\",\"type\":\"string\"}],\"createdOn\":\"2025-03-03T11:06:28.224Z\"}}}]},\"latestIntent\":null,\"customerPresence\":{\"value\":null},\"isActive\":true,\"conversationId\":\"67c58d36956d765cfc278e0f\",\"roomInfo\":{\"id\":\"67c58d36956d765cfc278e0e\",\"mode\":\"CONTACT_CENTER\"},\"state\":{\"name\":\"STARTED\",\"reasonCode\":\"CUSTOMER\"},\"channelSessionDirection\":\"INBOUND\",\"active\":true},\"status\":\"CREATED\",\"listId\":\"67372f8d58db250027b8e917\",\"time\":1740999990727}",
        "type": "PULL_MODE_LIST_REQUEST_RECEIVED",
        "conversationId": "67372f8d58db250027b8e917"
    }
[/code]  
  
**Event Name**|  onPullModeSubscribedListRequest  
---|---  
**Event Description**|  Event is triggered when a new chat is initiated by the customer in one of the subscribed lists. It is also triggered when an agent leaves a chat  
**Emitter**|  Agent Manager  
**Action**|  Possible values are:

  * PULL_MODE_LIST_REQUEST_RECEIVED
  * PULL_MODE_LIST_REQUEST_STATE_CHANGED

  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
pullModeEvent| type: Objectdescribes the properties of the chat session| 

  1. id - String - system generated channel session ID
  2. Channel Session - Channel Object - Conversation session details
  3. Service Identifier -

  
type| type: Objectaction of the event| -  
topicId| type: StringID of the conversation| -
