# CX Knowledgebase : Channel Session Detail

**Report Summary**|  Provides the details of each individual channel session in a conversation  
---|---  
  
For instance, if there are two channel sessions from two different channels (e.g. webchat and WhatsApp) under one customer conversation, you can see details of each channel session in this report.

See [Conversation](Conversation-Objects_2528831.html) and [Channel-related terms](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2525707) to know more about a conversation and a channel session.

See [Reporting Database Schema -> Channel_Session](Reporting-Database-Schema_2526317.html) table for more details.

## Report Columns

**Fields**| **Description**  
---|---  
Channel Session ID| This is the unique identifier of this channel session.   
Conversation ID| This is the ID of the conversation to which this channel session belongs.   
Channel Type | This is the channel type of the channel which is associated with this channel session. For instance, WhatsApp, and Facebook.  
Channel Name | It determines the channel which is associated with this session. This is the channel name as defined in the [**Unified Admin**](Unified-Admin-Guide_2524407.html) while defining channel settings; such as sales-inquiries, complaint-desk for `WhatsApp` Channel type.  
Channel Session Data| Provides the Data of this channel session. It provides information on the following:

  * **Device** \- the device that is being used for this channel session such as IOS, Android, or Desktop
  * **Browser Type** \- the browser used in this channel session such as Chrome, Firefox, or Edge
  * **Country** \- the country where this channel session is created
  * **Language** \- the language in which this channel session is occurred

  
Start Time| This determines the start time of the channel session  
Duration| This determines the total duration of the channel session, i.e. end time - start time of the channel session.  
End Time| This determines the end time of the channel session  
Channel Session Disposition| Disposition of this channel session. It could be one of the following: 

  * **AGENT** \- the human agent ended the channel session. This is valid in case of Pull-based requests when agents (or authorized users) go to a Subscribed List (Pull mode lists) and close a conversation from the List by clicking the "End" button.
  * **CUSTOMER** \- the customer ended the session. This happens in case when the web chat widget is closed by the customer.
  * **INACTIVITY** \- the channel session was closed because the customer became inactive, as per the customer inactivity timeout defined by the admin in the channel configurations.
  * **NETWORK** \- When the channel session is disconnected due to the network errors on the customer side.
  * **FORCE_CLOSED** -**** When an agent closes the browser tab while the task is active, the task will be closed after a certain time (usually 1 minute) if the agent doesn't return.

  
  
## Report Filters

  * Select Date/time - allows filtering channel sessions falling under a particular date/time range 

  * Channel Type - allows to filter the channel sessions of a particular channel type 

  * Channel Name - Specify the name of the channel to filter channel session details of the mentioned channel

  * Conversation ID - Specify the ID of the conversation to load all channel sessions of the specified conversation


![](attachments/2527421/2578165.gif?width=800)
