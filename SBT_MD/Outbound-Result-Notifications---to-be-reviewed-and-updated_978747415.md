# CX Knowledgebase : Outbound Result Notifications - to be reviewed and updated

## Call Results Mapping

**CX Delivery Notification**| | | | |   
---|---|---|---|---|---  
**Status Code**| **Reason Code**| **Call Result description**| **CX Dialer Call Results**| **UCCX**| **CCE**| **Webex CC**  
DELIVERED| PENDING DIALING| Contact is added to the database and pending dialing. A 200 OK response is sent to the scheduler which is considered as a DELIVERED delivery notification.| PENDING DIALING| N/A|  N/A|   
CONNECTED| NORMAL_CLEARING| Call has been answered by the customer.| NORMAL_CLEARING|  10| 1 |   
FAILED| NO_ANSWER| The call rang on the customer's phone but they did not respond before the timeout.| NO_ANSWER|  15|  8|   
FAILED| USER_BUSY| The customer declined the call, was busy on another call or manually rejected the call.| USER_BUSY| 11|  9|   
FAILED| ANSWERING_MACHINE| An answering machine was detected| ANSWERING_MACHINE| 3| 12|   
FAILED| FAX_MACHINE| A fax machine was detected| FAX_MACHINE| 2| 11|   
FAILED| INVALID_NUMBER| Number reported as invalid by the network.| INVALID_NUMBER| 4| 7|   
FAILED| {As received from the Dialer}| There are many other call results possible depending on what the network responds with. | [Miscellaneous Dialer Call Results](Miscellaneous-Dialer-Call-Results_1086029830.html)|  |  |   
  
## Message Result Notifications

**Results**| **Message result description**| **Additional Parameters**  
---|---|---  
DELIVERED| The message was successfully delivered to the customer| -  
FAILED| The message could not be delivered due to an invalid recipient number.| -  
READ| The message has been read by the customer.| -  
PLAIN| The customer sent a plain message reply that references a specific previous message.| markdownText
