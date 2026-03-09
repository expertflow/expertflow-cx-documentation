# CX Knowledgebase : Third Party Activies API

The purpose of this guide is to provide information on how third party applications can connect with Expertflow CX to push activities through the Expertflow CX interface. 

## Technical Overview

The activities that can be pushed by 3rd-party applications can be categorized into following types:

  * **_Stand-alone activities:_** These are activities independent of a customer conversation. For example, a 3rd party scheduler pushes a scheduled activity for preserving history of actions against a customer in CX Activities. 

  * **_Conversation-based activities:_** These are activities associated with a Conversation. For example, an agent's outbound activity, a survey activity, etc.

  * **_Channel-specific activities:_** These activities are related to a customer's ChannelSession. For example, an activity to push a call recording link in form of [URL Message ](URL-Message_2532489.html)for a call.




  * 3rd-party applications can push activities in the form of [CIM Messages](CIM-Messages_2530195.html).

  * The `Sender, Body` and any attribute from `Customer`, `Channel Session ID `or` Conversation ID` is mandatory for pushing third-party activities. 




**Header Attributes**| **Description**  
---|---  
`Customer`| Pass customer object (only Id) in the header to push a stand-alone activity. It will be a conversation/session less activity.  
`Conversation ID`| Pass `ConversationID` in the header to push the activity into an ongoing or past conversation.  
`Channel Session ID `| Pass `ChannelSessionID ` in the header to link the activity with a specific channel. The client can also pass the `ConversationID`. If the `ConversationID` is not present in the request, the system will find and link the activity with the relevant conversation  
  
  * Upon receiving the request, the API:

    1. Validates the request i.e. if user has passed the val`id `[CIM Messages](CIM-Messages_2530195.html)`.`

    2. Transform the the activity into THIRD_PARTY_ACTIVITY event. See [CX Activities](Messages%2C-Events%2C-and-Activities_2528021.html) document for events detail.

    3. If the conversation is active, publish the activity on the conversation topic. Otherwise, it pushes the activity to Conversations store.




### Example - Push Recording Link

The following example shows required parameters for pushing a recording link as an activity to CX.

#### Request Details

**Name**| **Type**| **Value**  
---|---|---  
URL| Post| {FQDN}/conversation-manager/activities  
Body| Object| [URL Message](URL-Message_2532489.html)  
  
#### Sample Request
[code] 
    {
        "id": "{{$guid}}",
        "header": {
            "sender": {
                "id": "460df46c-adf9-11ed-afa1-0242ac120002",
                "type": "APP",
                "senderName": "APPName",
                "additionalDetail": null
            },
            "channelData": {
                "channelCustomerIdentifier": "",
                "serviceIdentifier": "",
                "requestPriority": 0,
                "additionalAttributes": []
            },
            "language": {},
            "timestamp": {{$timestamp}},
            "securityInfo": {},
            "stamps": [],
            "entities": {},
            "channelSessionId": "ede4d48306cd47e39b2ec362759c632f",
            "conversationId": null,
            "customer":  null,
            "schedulingMetaData": null,
            "replyToMessageId": null,
            "providerMessageId": null
        },
        "body": {
            "type": "VOICE_RECORDING",
            "markdownText": "",
            "mediaUrl": "https://play.google.com/store/apps/details?id=com.ptcl_app.main&hl=en"
        }
    }
[/code]

  

