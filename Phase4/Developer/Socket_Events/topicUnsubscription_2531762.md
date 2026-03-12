# CX Knowledgebase : topicUnsubscription

**Event Name**|  topicUnsubscription  
---|---  
**Event Description**|  Event is triggered when an agent leaves the conversation. Event returns a success message in case of success.  
**Emitter**|  Agent Manager  
  
**Name**| **Description**  
---|---  
task| type: StringValue is topicUnsubscription is this case  
conversationId| type: StringID of the conversation to be unsubscribed  
statusCode| type: NumericReturn value 200 in case of unsubscription  
roomInfo| type: Object (opt.)  
reason| type: String. (opt.)
[code] 
    {
        "task": "topicUnsubscription",
        "conversationId": "5d37c884-8495-49fd-b6d3-8ef43fe53dc7",
        "statusCode": 200
    }
[/code]
