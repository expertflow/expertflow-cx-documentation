# CX Knowledgebase : Button Message

**Description**|  The button message is used to provide pre-defined options to the customer and is specifically for Agents and Conversational Bots (**Outbound Message**). The button API can be customized to send either a single option (as button) or a multiple options (list of buttons).  
---|---  
  
For button message:

  * Specify the type = "BUTTON". The body should be in JSON format and include the following properties:




**Property**| **Desc.**  
---|---  
type - String - Required| Value = "BUTTON"  
markdownText - String - Optional| contains custom plain text sent by Agent.  
buttonMessageType - String - Required| Possible Values:

  * Quick_Replies - 
  * Button - 

  
buttons - List - Required| More than one button can be added. Parameters:****

  * Title - String - Required - Label of the button
  * Type - String - Required - Type of the button. Can be user defined.
  * Payload - String - Required - 
  * additionalButtonDetails - String - Optional

  
additionalDetails - String - Optional| Additional details such head, body, footer etc.

  * A field “defaultIntent” is also passed by RASA in the additionalDetails section that is used in case customer has selected the option which is out of the button range.



  * “textAlignment“: “left“ / “center“ / “right“
    * We can specify any of the above values for text alignment. Front end will align the button text accordingly.

  
  
  

[code] 
      "body": {
            "type": "BUTTON",
            "markdownText": "Hi",
            "buttonMessageType": "BUTTON",
            "additionalDetails": {
                "interactive": {
                    "type": "list",
                    "button": "Main Menue",
                    "header": {
                        "type": "text",
                        "text": "<Header List Message>"
                    },
                    "body": {
                        "text": "<List Body Message>"
                    },
                    "footer": {
                        "text": "<Footer Message>"
                    }
                }
            },
            "buttons": [
                {
                    "type": "String",
                    "title": "Button 1",
                    "payload": "{{$guid}}",
                    "additionalButtonDetails": {
                        "sectionNo": 1,
                        "sectionTitle": "menue 1",
                        "description": "this is description"
                    }
                },
                {
                    "type": "String",
                    "title": "Button 1",
                    "payload": "{{$guid}}",
                    "additionalButtonDetails": {
                        "sectionNo": 2,
                        "sectionTitle": "menue 2",
                        "description": "this is description"
                    }
                },
                {
                    "type": "String",
                    "title": "Button 2",
                    "payload": "{{$guid}}",
                    "additionalButtonDetails": {
                        "sectionNo": 1,
                        "sectionTitle": "menue 2",
                        "description": "this is description"
                    }
                }
            ]
        }
[/code]

  


  


  


  

