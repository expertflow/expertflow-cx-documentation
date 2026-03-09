# CX Knowledgebase : Multichannel Session Detail

**Report Summary**|  Provides the details of the Multiple channel sessions in a conversation.  
---|---  
  
## Report Columns

Following are the report columns

**Fields**| **Description**  
---|---  
Conversation ID| This is the ID of the conversation to which this channel session belongs.   
Total Duration| The total duration of all channel sessions within the conversation associated with the channel sessions.  
Channel Session ID| This is the unique identifier of this channel session.  
Channel Name| It determines the channel associated with this session. This is the channel name as defined in the [**Unified Admin**](Unified-Admin-Guide_2524407.html) when defining channel settings, such as sales inquiries and complaint desks for `WhatsApp` Channel type.  
Channel Type| This is the channel type associated with this channel session, such as WhatsApp or Facebook.  
Start Time| This determines the start time of the channel session.  
End Time| This determines the end time of the channel session.  
Disposition| Disposition of this channel session. It can be one of the following: 

  * **AGENT** \- the human agent ends the channel session. This is valid in the case of Pull-based requests when agents (or authorized users) go to a Subscribed List (Pull mode lists) and close a conversation from the List by clicking the "End" button.
  * **CUSTOMER** : the customer ends the session. This happens when the customer closes the web chat widget.
  * **INACTIVITY** \- the channel session ends because the customer became inactive, as per the customer inactivity timeout defined by the admin in the channel configurations.
  * **NETWORK** \- When the channel session is disconnected due to network errors on the customer side.
  * **FORCE_CLOSED** -**** When an agent closes the browser tab while the task is active, the task will be closed after a certain time (usually 1 minute) if the agent doesn't return.

  
Duration| This determines the duration of the channel session, i.e. end time - start time of the channel session.  
  
![Multi channel session report.gif](attachments/436994049/436633612.gif?width=1092)

## Report Filters

The following report filters are available

  * DateTime - allows filtering channel sessions falling under a particular date/time range 

  * Channel Type - allows to filter the channel sessions of a particular channel type 

  * Channel Name - Specify the name of the channel to filter channel session details of the mentioned channel

  * Conversation ID - Specify the ID of the conversation to load all channel sessions of the specified conversation.



