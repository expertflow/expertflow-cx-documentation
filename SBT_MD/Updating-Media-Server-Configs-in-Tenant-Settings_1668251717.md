# CX Knowledgebase : Updating Media Server Configs in Tenant Settings

From CX-5.1 onwards, the media server connection URL is moved from CX Environment Variables to the tenant settings.

To update the media server connection URL using the _CX Tenant_ Api’s for CX Voice configuration,

  * Navigate to the API link available in the CX Api collection on [Postman](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-718c6b84-333f-4973-9a62-b70beb2bc351?action=share&source=copy-link&creator=21457238&ctx=documentation).

  * Update your _**FQDN**_ in the api address bar.

![image-20260122-110805.png](attachments/1668251717/1674543222.png?width=494)

  * Navigate to the _Params_ tab and update the _**Id**_ param with your tenantId in the query parameters.  


![image-20260122-111004.png](attachments/1668251717/1674543228.png?width=566)

  


  * Navigate to the _Body_ tab and select _form-data_ payload type.  


![image-20260122-111146.png](attachments/1668251717/1676738607.png?width=642)
  * Update the _**wssUrl**_ parameter value to update the media server URL in the data object of the API payload.  


![image-20260122-111740.png](attachments/1668251717/1677787158.png?width=738)



  * For reference, the _JSON_ structure is as follows:
[code] {
            "tenantName": "<string>",
            "tenantId": "string",
            "tenantCode": "<string>",
            "tenantSettings": {
                "mediaServer": {
                    "wssUrl": "wss://<FS_IP>",
                     "domainManagerUrl": 
                        "http://<FS_IP>/add-domain/"
                }
            }
        
        }
[/code]



