# CX Knowledgebase : Send a Media message

  


A Channel Connector can send a file message to Hybrid Chat. There are two ways to upload a file:

  1. Specify the fileStream object to be uploaded
  2. Specify the fileURL 



## To send a file using filesStream Object

  1. Call [Upload a file](https://api.expertflow.com/#406ad9dd-83fb-4a7d-ac06-40607df4b858) API with the fileStream object. Upon success you'll get the `filename` from the server.
  2. Create a [Download File Stream](https://api.expertflow.com/#be71cf16-a559-4429-83d0-4cf53b04eaae) URL and specify the `filename` from step# 1 as a query param.
  3. Create a [Media message](Multimedia-Messages_2525501.html) and specify `mediaUrl` containing the URL created in step# 2.



  


**Request Query Params**

**Property**|  Type| **Desc.**  
---|---|---  
conversationId REQUIRED| String| Unique id of the file.   
file REQUIRED| FileStream Object | The file stream object of the file that should be uploaded on Hybrid Chat.   
  
**Response**

**Status**| **Description**|  Response  
---|---|---  
Success| Code 200 for success loading of file on server.| Message - String - Required - "File uploaded successfully."etag - String - Required - HTTP response header is an identifier for a specific version of a resource and used for tracking purposes.name - String - Optional - this is the unique file name.type - String - Optional - type and extension of the file e.g. image/pngsize - Numeric \- Required - size of the uploaded file.  
Internal Server Error| Code 500 when a server error occurs.| Message: "An error occurred while uploading file."  
Bad Request| Code 404 when there is a problem uploading file.| Message: "An error occurred while uploading file."  
  
  


## To send a file using File URL

  1. Call [Upload a file from URL](https://api.expertflow.com/#51a50cb9-9afc-44fb-9c9c-f84511bec927) API and specify `sourceUrl` (the media URL to upload).
  2. Create a [Download File Stream](https://api.expertflow.com/#be71cf16-a559-4429-83d0-4cf53b04eaae) URL and specify the `filename` from step# 1 as a query param.
  3. Create a [Media message](Multimedia-Messages_2525501.html) and specify `mediaUrl` containing the URL created in step# 2.



  


### Request parameters

**Property**| **Desc.**  
---|---  
conversationId - String - Optional| ID for tagging media.  
sourceUrl - URL - Required| get file from the given URL  
channel - String - Required| The channel where conversation is in progress.  
fileName - String - Optional| to be specified by user. Appended with conversationId in response. If no name is specified, file name is extracted from the URL.  
oauth - Object - Optional| When OAuth is required to download the file from the specified URL mentioned in `sourceURL` property.   
APIKey360 - String - Required for 360 DialogFlow Connector| The connector API Key for authorization to 360 connector.Required only for 360Dialog connector for WhatsApp   
mime_type - String - Optional| type and extension of the file e.g. image/png  
  
  


### Response

**Status**| **Description**|  Response body  
---|---|---  
Success| Code 200| Message - String - Required - "File uploaded successfully."etag - String - Required - HTTP response header is an identifier for a specific version of a resource and used for tracking purposes.name - String - Optional - name can be specified by the user. It is saved with conversation ID appended to it e.g. 11111_filename.exttype - String - Optional - type and extension of the file e.g. image/pngsize - Numeric - Required - size of the uploaded file.  
Internal Server Error| Code 500| Message: "An error occurred while uploading file."  
Bad Request| Code 404| Message: "An error occurred while uploading file."  
  
Assumptions and Constraints

  * Maximum file size is 5Mb. The size is configurable and can be changed based on the business need.
  * There is no restriction of file type/extension in HyrbidChat. It is also configurable based on the business requirements. 
  * Uploaded files can be stored indefinitely on server if required. Time limit for file storage on server is dependent upon the space requirements for the business deploying the HyrbidChat solution. 
  * For downloading media, only filename needs to be specified. Example is available on [Expertflow Public Workspace](http://api.expertflow.com).


