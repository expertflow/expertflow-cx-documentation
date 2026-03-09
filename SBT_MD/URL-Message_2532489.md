# CX Knowledgebase : URL Message

**Description**|  URL message is specifically used by Agents and Bots (**Outbound Messages**) to send a URL e.g. for app installation, system/license updates.   
---|---  
  
The method to send URL message is given as follows:

  * Specify the type = "URL". The body should be in JSON format and include the following properties:




**Property**| **Desc.**  
---|---  
type - String - Required| Value = "URL"  
markdownText - String - Optional| Contains custom plain text message sent by Agent and routed from CCM to connector Webhook.  
mediaURL - String - Required| URL  
  
  

[code] 
    "body": {
            "type": "URL",
            "markdownText": "You can download our Android app from this link.",
            "mediaUrl": "https://play.google.com/store/apps/details?id=com.ptcl_app.main&hl=en"
        }
[/code]

  


  


  


  


  

