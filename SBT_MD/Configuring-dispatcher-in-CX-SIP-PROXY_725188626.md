# CX Knowledgebase : Configuring dispatcher in CX SIP PROXY

  1. Login to the cxSIPproxy control panel by visiting <http://host-ip/cp> (replace host-ip with the actual IP of your VM) and use the following credentials( username: efuser, password: efuser)  
  
  2. To add a Dispatcher go to **System** > **Dispatcher**


![image-20241204-104454.png](attachments/725188626/726073372.png?width=1440)

  3. To add a destination click on **Add Destination**.




We need to organize destinations into specific **sets** based on their type. Each destination type will be organized into a distinct set. For example, All CVP destinations will belong to **Set ID 1**. Similarly, other destinations like Cube, VVB, CUCM, and Dialer will have their own respective sets like: 

  * **Set 1** : CVP destinations

  * **Set 2** : Cube destinations

  * **Set 3** : VVB destinations

  * **Set 4** : CUCM

  * **Set 5** : Dialer.




The grouping ensures that when a call is routed to a specific set (e.g., Set ID 1 for CVP), the dispatcher will select the destination within that set according to its weight.

  4. Now add the required information as specified below.




**Parameter**| **Explanation**  
---|---  
Set ID| The **numerical ID** of the dispatcher set/group for the new destination.  
SIP URI| SIP URI pointing to the destination. To define the destination, use the following SIP URI format:`sip:<IP>:<port>`

  * `<IP>`: The destination’s IP address.
  * `<port>`: The port number on which the destination is listening.

Example:  
For a CVP destination with IP `192.168.1.10` and port `5060`, the SIP URI would be:  
`sip:192.168.1.10:5060`  
Socket| The cxSIPproxy network listener (as `sip:<IP>:<port>`) to be used for reaching the destination (leave it empty)  
State| The intial state of the destination.

  1. **Active:** The destination will be shown active and available for call routing. 
  2. **Inactive:** The destination will be shown inactive and will not be available for call routing. You’ll have to edit this destination again to make it active.

Always keep the state active.  
Probing| Probing determines the health status of each destination to ensure calls are not routed to unavailable destinations. There are two probing options to decide either the destination should be probed(for availability) or not.

  1. **Default** : In this mode, the default setting for probing will be used I:e only the destinations with probing state Always will be probed.
  2. **Always** : Always probe this destination, regardless its status.

  
Weight| The weight of a destination is currently used in the hashing algorithms and it increases the probability of the destination being chosen(if we have two destinations with weights 1 respectively 4 then the second one is 4 times more likely to be selected than the other). The sum of all weights does not need to add up to a specific number.  
Attributes| String of custom Attributes, to be passed to the cxSIPproxy script. Leave this column empty.  
Description| The description is in DB and is not used by cxSIPproxy. Provide clear and concise descriptions for each destination. For example, if the destination is a CVP, include "CVP" in its description for easy identification.  
  
After adding the data it should look like this 

![image-20241209-040241.png](attachments/725188626/736362591.png?width=686)

  6. Now click on **Add** to save it and it should look like this.


![image-20241209-040418.png](attachments/725188626/736362599.png?width=1014)

If the memory state indicator is not shown as green, click on the **red** Memory state indicator, and then click **OK** to make it active. If it’s still not green, confirm that the destination is up and accessible.

The dispatcher destination has been added. To add destinations for other sets, repeat these steps for those sets.

  9. Now go to System> Dialplan and click on the gear icon


![image-20241206-115108.png](attachments/725188626/736362529.png?width=1197)

  10. In **General settings** from the **Dialplan attributes modes** drop-down select `Checkboxes`


![image-20241206-115418.png](attachments/725188626/736362535.png?width=529)

  11. Now replace the following attributes into the**Attributes list** data. The code below will add attributes for five groups of load balancers and five sets/groups of dispatchers. You can add more attributes in a similar manner.
[code] {
             "LB-1": "LB-1",
             "LB-2": "LB-2",
             "LB-3": "LB-3",
             "LB-4": "LB-4",
             "LB-5": "LB-5",
             "DS-1": "DS-1",
             "DS-2": "DS-2",
             "DS-3": "DS-3",
             "DS-4": "DS-4",
             "DS-5": "DS-5"
         }
[/code]




It will look like this. Click on **Save** to save these settings. 

![image-20241203-071437.png](attachments/725188626/725614665.png?width=475)

  11. To add a new rule, click on **Add New Rule** in the System > Dialplan section and enter the required information as specified below.




**Parameter**| **Explanation**  
---|---  
Dialplan ID| This is the unique ID that is used in the cxSIPproxy script. Always keep it equal to 1.  
Rule priority| Assign a priority value or level to the rule. Use lower values for higher priority, set it to 0 for the highest priority.  
Matching operator| What method will be used to match the string/username of the “To” header of the SIP message? 

  * REGEX: Use Perl Compatible Regular Expressions to match against the string/username/prefix of the “To” header of the SIP message.
  * EQUAL: Perform a string equality test against the string/username/prefix of the “To” header of the input SIP message. 

Select one of these options accordingly.  
Matching Regular Expression| For this rule, the exact **regex** or **string** used to be matched against the string/username of the incoming message. For regex, you can use [this link](https://regex101.com/) to confirm the regex. For prefix-based routing, a common regex used in SIP proxies is ^<prefix>.*, where, for example, a regex of ^4433.* will capture all traffic that starts with "4433," such as 434466779788@domainA, 4433322344@domainB, and so on.  
Matching Flags| The case of the characters can be ignored by selecting **case insensitive** , or the matching can be kept case sensitive by choosing the **case sensitive** option.  
Match Only| Check this option if you want to route SIP traffic to the next destination without substituting the prefix or username.  
Substitution Regular Expression| If the **Match Only** option is not checked, enter the exact value used in the **Matching Regular Expression** here. This means that the username/prefix part of the “To” header in the SIP message will be updated by the **Replacement Expression** (the value provided below).  
Replacement Expression| Provide the value that will replace the username of the “To” header of the SIP message.   
Please choose **only one attribute** from the list below. Attributes beginning with "DS" will route the call to specific set of dispatcher. For example, select "DS-1" to route the call to Set 1 of the dispatcher, or "DS-2" for Set 2. After adding this information, the final result should resemble the image provided below.  
  
![image-20241204-104205.png](attachments/725188626/725712903.png?width=832)

Click on **Add** to save it.

Prefix-based routing can be implemented for CVPs, CUCM, or any other sets of destinations this way.
