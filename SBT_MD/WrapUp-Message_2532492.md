# CX Knowledgebase : WrapUp Message

When an agent wants to tag full or portions of a conversation by attaching admin-defined categories (from the UI) to it, Wrap Up message API is used.

**Property**| **Desc.**  
---|---  
type - String - Required| value = "WRAPUP"  
wrapups- Array - Required| more than one category can be attached._Parameters:_

  * categoryName - Required - category as selected by the agent
  * value - Required - any value as specified by the agent

  
markdownText - String - Optional| contains custom plain text sent by end user.  
note - String - Optional| Additional details as added by the agent.
[code] 
    {
            "markdownText": " ",
                "type": "WRAPUP",
                "wrapups": [
                {
                    "categoryName": "Category1",
                    "value": "internet disconnectivity"
                },
                {
                    "categoryName": "Category2",
                    "value": "plan upgradation"
                }
               ],
            "note": "optional"
    
    }
[/code]
