# CX Knowledgebase : Make a Manual Outbound Contact

Allows agents to initiate contact with a customer even if no conversation with the customer is going on.

Agents can initiate contact with a customer by clicking the '**+'** icon at the top. This will drop a panel carrying two options, to dial a number, or choose a customer to be contacted from the customer list.

Manual outbound is initiated using the following API: [Out-Bound CIM Messages](https://api.expertflow.com/#a8792cd5-5714-44c9-a5c1-2dbfce7d0d18)

![image-20240802-055431.png](attachments/2528797/424018001.png?width=395)

### Make an Outbound Call: 

It is important to note that the availability of the tones depends on the network provider. If the provider does not offer ringing or voicemail tones after the customer decline, the system cannot generate them independently.

Before initiating an outbound call, agents must ensure they are connected to the EFSWITCH.

On initiating an outbound call, the agent’s MRD will automatically be changed to **Not Ready** state so that no inbound call conflicts with the Outbound request and the agent doesn't get reserved for that and as a result there will be no MRD state changes for duration of the call.

Once connected, follow these steps:

  1. Click the '**+'** button on the top header.

  2. A panel is dropped showing two tabs, one for selecting an existing customer from the customer list and the other, for dialing a number manually through the dialpad.

  3. Agents can enter the number they wish to dial through the dialpad. On entering the number, a customer list will be shown matching the entered digits to find the customer along with the name if it already exists. 

  4. If the number is new and does not already exist, agents can dial the number manually. A new customer profile will automatically be created on the call initiation. The agent can then later,[ update profile information](Accept-a-Conversation_2527849.html#Update-A-Customer-Profile).

  5. Select a customer from the suggestions list once the number is matched with any of the customer profiles. Click the 'Call' button on the dialpad to initiate an Outbound call.

  6. You can also dial a call by selecting an existing customer in the Customer list tab alongside the dial pad tab. 

     1. Search the customer by name or number. 

     2. Choose a customer best matched with the specified search string. 

     3. Click to drop the customer details pane and choose the call button again the number field of the customer profile to dial out a call.

  7. As the customer accepts the call, the conversation view opens and the agent can view the customer details along with the draggable CTI toolbar with three major call controls. (mute/unmute, hold/resume, end)


![image-20240801-114320.png](attachments/2528797/429522985.png?width=497)

Agents can also establish a new call during an active conversation with a customer. For instance, if a customer and agents are communicating on WhatsApp, the Web, or any chat channel, agents can also place a new voice call to the customer number by following the same steps mentioned above. Once the call is connected, the voice session will be active and can be viewed in the “Active Channels Pane” on the right-hand side panel. 

On initiating an outbound call, the agent’s Voice MRD will automatically be changed to “Not Ready” state so that no inbound call conflicts with the outbound call and the agent doesn't get reserved for that.

### Limitations 

  * Special characters are not supported when dialing numbers except ***** , **#,** and **+**.

  * Agent-agent manual outbound call is not supported.

  * Direct extension-to-extension calls are not supported.

  * When a customer declines a call, a notification is received on the Agent Desk from Sip.js. Due to this error message, Agent State is set to Not-Ready.




### Make an Outbound Chat (WhatsApp only)

Agents may initiate outbound contact with customers on other supported channels as well, such as WhatsApp. To send a WhatsApp message to a customer when there’s no active conversation going on with the customer,

  1. Click the '**+'** button to initiate an outbound contact and click the customer list tab alongside the dialpad tab.

  2. Search for the desired customer via the search bar or, choose a customer directly from the customer list. 

  3. If the typed string in the search bar does not match with any of the existing customers, i.e. if the customer profile does not exist, there are two options,

     1. If the agent enters a valid number, two options are shown, I) Create Customer ii) Voice Call 

        1. On clicking this, the “Create Customer” dialogue will appear. The specified number in the search bar will automatically appear in the “Voice” attribute. 

        2. On clicking this, an outbound call will be initiated on the number

     2. If the agent enters an invalid number, only the option to create a new customer will be shown.

  4. If the customer already exists, click the drop-down beside the name of the desired customer in the customer list to see the available outbound options. 

  5. Clicking the **Voice** button against the customer number will initiate a new conversation and start a call with the customer.

  6. Clicking on the **Whatsapp** icon will start a new conversation on the Whatsapp channel.


![](attachments/2528797/429064227.png?width=632)

  * Currently, the outbound can only be initiated via “WhatsApp” and “Voice” channel for now.

  * To send an outbound SMS, use the SMS icon on the top beside the '+' button and make sure that the SMS channel via Twilio is properly configured for sending an outbound SMS.




### Limitations related to Whatsapp OB conversation

  * To initiate a new conversation on WhatsApp or, to send a new message via WhatsApp in an existing conversation, there must already be a customer session opened with the business, in the last 24 hours. 

  * To be able to initiate a conversation or send a WhatsApp message after 24 hours time, the business would need to buy template messages from WhatsApp. 

  * If the customer does not join the conversation (reply to agent message) within the predefined timeout of the channel (as defined by the system administrator in Unified Admin), the conversation will automatically be closed.




### Send an Outbound SMS

Agents can also send SMS messages to customers if the SMS channel is enabled.

  1. To send a message, click the SMS icon on the top header on the Customer Conversation View.

  2. Upon clicking, a dialog box will open. Agents can enter the customer number. On entering the number, a suggestion list will pop up matching the entered digits to find the customer along with the name if it already exists.

  3. Select a customer from the list if it already exists. Upon selection, another button appears on the dialogue, captioned, **See Conversation History.** Select this button to see the conversation history of the selected customer. Note that from this view, you can only see the history of past conversations and cannot send a message from this view directly.

  4. If the entered digits do not match, a new customer profile will be created upon sending the message. 




This feature works only when the SMS channel is configured via Twilio. 

![send sms.png](attachments/2528797/185106593.png?width=962)

This feature can be enabled or disabled from Unified Admin → **Agent Desk Settings**.

![Outbound SMS config.png](attachments/2528797/185892867.png?width=1068)

Turn on the **Outbound SMS** toggle to enable the feature. 

Add the default prefix in the **Add Prefix Code.** By default, the prefix given is +1. 

Enable the **Close Send SMS Dialog** if you want to close the dialog automatically upon sending the message. Turn it off to keep opening the dialog.

## Send WhatsApp

### When there is no active conversation

Agents can initiate new conversations with a customer via the WhatsApp channel. To do so, click the **Start New Conversation** button on the Conversation View in case of no conversations, and in case of other active conversations in hand, click the **(+)** icon on the left sidebar.  
  


![](attachments/2528797/2568474.png?width=306)

Look for the desired customer record on the Customer List that opens up and click the contact icon against the record. This will open up the customer profile on the Conversation View with Message Composer disabled. This is because no conversation is currently active with this customer. Expand the right panel and choose the WhatsApp channel icon to start a conversation over WhatsApp.

Also, by default, the customer history is hidden. Agents can load the history of the customer by clicking the link, based on the permissions to do so. 

### Adding a new channel session in the active conversation

Expand the right side and click the **Media Channels** pane. Choose the channel identity (for now, only the phone number) for the WhatsApp channel, click the dropdown, and click the chat icon against the **WhatsApp** channel.

![](attachments/2528797/2568477.png?width=510)

Clicking the chat icon will initiate a new conversation with the selected customer on WhatsApp. 
