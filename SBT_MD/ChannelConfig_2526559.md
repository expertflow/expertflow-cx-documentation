# CX Knowledgebase : ChannelConfig

Object Name| ChannelConfig  
---|---  
Description| This object contains the attributes of the channel configuration object. It represents configurations related to a particular channel.  
  
  


Parameter| Type| Description  
---|---|---  
`id `REQUIRED``| String| This is the UUID. Sample format is `a5c80b3f-ea41-4caf-979d-641a1c32f9bd`  
`channelMode `OPTIONAL``| ChannelMode| Three channel mode are offered for dealing with the customers: 1\. BOT - only BOT is conversing 2\. AGENT - only AGENT is conversing3\. HYBRID - both BOT and AGENT are conversing with the customer  
``conversationBot REQUIRED``| String| Name of the bot for this particular channel  
`responseSla `REQUIRED``| int| Returns the response time SLA for the particular channel  
``customerActivityTimeout REQUIRED``| int| For customer activity timeout i.e. for how long was the customer inactive or non-responsive in the channel. This is used to trigger some activity/event in the system in case of in-activity.  
``customerIdentificationCriteria UNDEFINED``| customerIdentificationCriteria| undefined for now  
`routingPolicy `REQUIRED``| RoutingPolicy| Define routing policy such as agent routing, internet based routing.   
`botId `OPTIONAL``| String| ID of the bot. Currently for chat channels only.
[code]
      
    
[/code]
