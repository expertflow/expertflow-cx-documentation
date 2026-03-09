# CX Knowledgebase : Cisco Outbound Connector

A connector to handle outbound communication with customers via Cisco.

## Pre-Requisites

  * An outbound campaign should be created in Cisco CCE/CCX.

  * The Cisco outbound connector should be configured for CCX or CCE via the **CISCO_TYPE** environment variable.




# Proposed Solution

  1. A list of campaigns is obtained from the Cisco [CCX](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-f731aae8-0cac-4576-ab25-98abe3f2bbba?action=share&creator=21457238&ctx=documentation) or [CCE ](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-374cbf69-0f46-4aeb-9fa5-f1ba0506ac0f?action=share&creator=21457238&ctx=documentation)API.

  2. The campaign ID of the chosen campaign is noted.

  3. The [Scheduler API](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-f137cd22-83ad-4d74-ad97-c53cc7936974?action=share&creator=21457238&ctx=documentation) is called with the contact information i.e. name and contact number, campaign ID.

  4. The Scheduler sends the contact to the CCM at the scheduled time, which forwards it to the connector.

  5. The connector sends this information to Cisco CCX or CCE to add that contact to the required campaign.

  6. The connector also saves the call ID to a Redis cache.

  7. The result can be verified by receiving a 200 OK response to the previous request as well as using the List-Campaign-Contacts API for [CCX ](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-59fbee63-7764-4716-8061-0f236b68fd01?action=share&creator=21457238&ctx=documentation)or [CCE](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-d285415a-98fa-428b-a9ce-36e5c118dda5?action=share&creator=21457238&ctx=documentation).

  8. Periodically the connector checks the cache and retrieves the call IDs present. For each ID the result is read from the Cisco database.

  9. If there is no result for the ID and an hour has passed since the key was inserted in the cache, the ID is removed from the cache and the result is noted as **DIAL_TIMEOUT**.

  10. The results are sent as Delivery notifications to the CCM.



