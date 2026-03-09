# CX Knowledgebase : Location Message

**Description**|  Location message is primarily used to send location coordinates to the recipient.   
---|---  
  
The method to send location message is given as follows:

  * Specify the type = "LOCATION". The body should be in JSON format and include the following properties:




**Property**| **Desc.**  
---|---  
type - String - Required| Value = "LOCATION"  
location - Numeric - Required|  _Parameters:_

  * Latitude - Required = 31.51335334777832
  * Longitude - Required = 74.3333969116211

  
markdownText - String - Optional| contains custom plain text sent by end user.  
additionalDetails - String - Optional| Additional details such as name, address, url can be passed.  
  
  

[code] 
    "body": {
            "type": "LOCATION",
            "location": {
                "latitude": 31.51335334777832,
                "longitude": 74.3333969116211
            },
            "markdownText": null,
            "additionalDetails": {
                "name": "Gaddafi Stadium",
                "address": "Hafeez Kardar Road",
                "url": null
            }
        }
[/code]

  


  


  


  

