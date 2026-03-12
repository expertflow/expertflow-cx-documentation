# CX Knowledgebase : topicClosed

**Event Name**|  topicClosed  
---|---  
**Event Description**|  Event is triggered to notify the agent whenever a topic is closed.  
**Emitter**|  Agent Manager  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
task| type: StringValue is topicClosed is this case| -  
conversationId| type: StringID of the conversation to be closed| -  
statusCode| type: NumericReturn value 200 in case of topic closure| -
[code] 
    {
        "task": "topicClosed",
        "conversationId": "97f460f1-42b5-4970-b77b-0985b17e562c",
        "statusCode": 200
    }
[/code]
