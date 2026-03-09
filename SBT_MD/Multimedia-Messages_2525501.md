# CX Knowledgebase : Multimedia Messages

**Description**|  Media Messages consist of the following types: 

  * Image 
  * Video 
  * Audio
  * File
  * Sticker

  
---|---  
  
The response and request structure is given in the tabs below according to each type of message.

### Assumptions and Constraints

  * Maximum file size is 5Mb. The size is configurable and can be changed based on the business need.

  * There is no restriction of file type/extension in Expertflow CX. It is also configurable based on the business requirements. 

  * File exchange between conversation participants is carried out by first uploading the media file to a server space in Expertflow CX. The process for uploading the file is described in [Send a Media Message](Send-a-Media-message_2532588.html). 




  


**Image Message Format**

  


![](images/icons/grey_arrow_down.png)Click here to expand...

## Image Message

  * Specify the type = "IMAGE". Body should be in JSON format with following properties:



**Property**| **Desc.**  
---|---  
type - String - Required| Value = "IMAGE"  
caption - String - Optional| contains caption specified by end user for the image.  
attachment \- Object: 

  * mediaUrl - URL - Req - URL where media is located
  * thumbnail - Image - Optional - resized image 
  * mimeType - String - Optional - type and extension of the file e.g. image/png
  * size - Numeric - Optional - size of the uploaded file

| Contains media object attachment details. For file upload and processing, please see [Send a Media Message](Send-a-Media-message_2532588.html).  
markdownText - String - Optional| contains custom plain text sent by end user.  
additionalDetails - String - Optional| Additional details such as timedate object values can be passed.  
  
  

[code] 
    "body": {
            "type": "IMAGE",
            "caption": "Screenshot",
            "attachment": {
                "mediaUrl": "https://cim.expertflow.com/file-engine/api/downloadFileStream?filename=743dc126-24fa-41f2-88fc-11b964e64ee8",
                "thumbnail": null,
                "mimeType": "image/jpeg",
                "size": 41047
            },
            "markdownText": null,
            "additionalDetails": {
                "timestamp": "1652080145"
            }
        }
[/code]

  


  


**Video Message Format**

  


![](images/icons/grey_arrow_down.png)Click here to expand...

## Video Message

  * Specify the type = "VIDEO". Body should be in JSON format with following properties: 



**Property**| **Desc.**  
---|---  
type - String - Required| Value = "VIDEO"  
caption - String - Optional| contains caption specified by end user for the video  
attachment \- Object: 

  * mediaUrl - URL - Req - URL where media is located
  * thumbnail - Image - Optional - resized image 
  * mimeType - String - Optional - type and extension of the file e.g. image/png
  * size - Numeric - Optional - size of the uploaded file

| Contains media object attachment details. For file upload and processing, please see [Send a Media Message](Send-a-Media-message_2532588.html).  
markdownText - String - Optional| contains custom plain text sent by end user.  
additionalDetails - String - Optional| Additional details such as timedate object values can be passed.  
  
  

[code] 
    "body": {
            "type": "VIDEO",
            "caption": "sample video message",
            "attachment": {
                "mediaUrl": "https://cim.expertflow.com/file-engine/api/downloadFileStream?filename=9960d501-092d-4758-81f6-e008758593f3",
                "thumbnail": null,
                "mimeType": "video/mp4",
                "size": 3114398
            },
            "markdownText": null,
            "additionalDetails": {
                "timestamp": "1652177594"
            }
        }
[/code]

  


  


**Audio Message Format**

  


![](images/icons/grey_arrow_down.png)Click here to expand...

## Audio Message

  * Specify the type = "AUDIO". Body should be in JSON format with following properties: 



  


**Property**| **Desc.**  
---|---  
type - String - Required| Value = "AUDIO"  
caption - String - Optional| contains caption specified by end user for the audio  
attachment \- Object: 

  * mediaUrl - URL - Req - URL where media is located
  * thumbnail - Image - Optional - resized image 
  * mimeType - String - Optional - type and extension of the file e.g. audio/codec
  * size - Numeric - Optional - size of the uploaded file

| Contains media object attachment details. For file upload and processing, please see [Send a Media Message](Send-a-Media-message_2532588.html).  
markdownText - String - Optional| contains custom plain text sent by end user.  
additionalDetails - String - Optional| Additional details such as timedate object values can be passed.  
  
  

[code] 
    "body": {
            "type": "AUDIO",
            "caption": "sample video message",
            "attachment": {
                "mediaUrl": "https://cim.expertflow.com/file-engine/api/downloadFileStream?filename=9960d501-092d-4758-81f6-e008758593f3",
                "thumbnail": null,
                "mimeType": "video/mp4",
                "size": 3114398
            },
            "markdownText": null,
            "additionalDetails": {
                "timestamp": "1652177594"
            }
        }
[/code]

  


  


**File Message Format**

  


![](images/icons/grey_arrow_down.png)Click here to expand...

## File Message

  * Specify the type = "FILE". Body should be in JSON format with following properties:



**Property**| **Desc.**  
---|---  
type - String - Required| Value = "FILE"  
caption - String - Optional| contains caption specified by end user for the file  
attachment \- Object: 

  * mediaUrl - URL - Req - URL where media is located
  * thumbnail - Image - Optional - resized image 
  * mimeType - String - Optional - type and extension of the file e.g. file/pdf
  * size - Numeric - Optional - size of the uploaded file

| Contains media object attachment details. For file upload and processing, please see [Send a Media Message](Send-a-Media-message_2532588.html).  
markdownText - String - Optional| contains custom plain text sent by end user.  
additionalDetails - String - Optional| Additional details such as timedate object values or file name can be passed.
[code] 
    "body": {
            "type": "FILE",
            "caption": "sample.pdf",
            "attachment": {
                "mediaUrl": "https://cim.expertflow.com/file-engine/api/downloadFileStream?filename=96460746-9a80-4bc8-bba1-87b93e39c245",
                "thumbnail": null,
                "mimeType": "application/pdf",
                "size": 3028
            },
            "markdownText": null,
            "additionalDetails": {
                "timestamp": "1652177308",
                "fileName": "sample.pdf"
            }
[/code]  
  
  


  


**Sticker Message Format**

  


![](images/icons/grey_arrow_down.png)Click here to expand...

## Sticker Message

  * Specify the type = "STICKER". Body should be in JSON format with following properties: 



**Property**| **Desc.**  
---|---  
type - String - Required| Value = "STICKER"  
mediaUrl - URL - Required| Contains media object URL: mediaUrl = "http://..."For file upload and processing, please see [Send a Media Message](Send-a-Media-message_2532588.html)..  
stickerId - String - Optional| contains ID of the sticker as provided by the channel.   
markdownText - String - Optional| contains custom plain text sent by end user.  
additionalDetails - String - Optional| Additional details such as: - timedate object - **metadata** : - emojis - contains available emojis
[code] 
    "body": {
            "type": "STICKER",
            "mediaUrl": "https://cim.expertflow.com/file-engine/api/downloadFileStream?filename=9870130c-a862-4e9e-a5a6-a0f7420008f0",
            "stickerId": null,
            "markdownText": null,
            "additionalDetails": {
                "timestamp": "1652178293",
                "metadata": {
                    "emojis": [
                        "☕",
                        "🙂"
                    ],
                    "is-first-party-sticker": 1,
                    "sticker-pack-id": "whatsappcuppy"
                }
            }
        }
[/code]  
  
  


  


  


  


  


  

