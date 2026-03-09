# CX Knowledgebase : Duplicate of Media Server Configurations for CX Voice

## Requirements

### Software Requirements

Item| Recommended| Installation guide  
---|---|---  
Media Server| Latest version| [Installation](Media-Server-Deployment-Guide_1344451.html)  
EFCX| 4.10| [Installation](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/2528385)  
  
## Key Points to Remember

  * **Single-Tenant Setup:**

    * The tenant can be of any name, however, tenant name and the realm name must be same.

    * The **SIP_URI** in the Agent Desk configuration should be set to: `tenant name`

    * Since the default configuration is shared, **multiple Voice Connectors** can connect to the **same FreeSWITCH server**.

      * In this setup, there will be **one FreeSWITCH instance** and **multiple Voice Connectors** , all using the **tenant**`expertflow`

  * **Multi-Tenant Setup:**

    * The tenant can be of any name, however, tenant name and the realm name must be same.

    * Dynamic configuration values will be generated.

    * For example:
[code] cxFqdn = https://<TENANT-ID>.<ROOT_DOMAIN>
[/code]

  * In this setup, there will be **one Voice Connector** and **one FreeSWITCH instance** , both configured dynamically based on the tenant.




* * *

# 1\. Default Configuration (Once at the time of Installation of Media Server)

## Install Lua libraries

  * SSH into the Debian server onto which the Media Server is installed.

    * Use command 
[code] ssh username@server-ip
[/code]

    * Enter user password and press **ENTER**.

    * Use command 
[code] su
[/code]

    * Enter root password and press **ENTER**.

  * Run the following commands, one at a time:

  * 
[code]apt install lua-socket
        sudo apt install lua-sec
        sudo apt-get install lua-json
        sudo apt-get install -y lua-dkjson
[/code]




## Configure IVR scripts and recordings (Once at the time of Installation of Media Server)

### Deployment

  * SSH into the Media Server.

    * Use command 
[code] ssh username@server-ip
[/code]

    * Enter user password and press **ENTER**.

    * Use command 
[code] su
[/code]

    * Enter root password and press **ENTER**.

  * [Confirm ](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html#confirm-git-is-installed)**git** is installed, and [install it](https://docs.gitlab.com/ee/topics/git/how_to_install_git/index.html) if is not.

  * Clone the Media Server scripts repository: 
[code] git clone -b TAG https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/freeswitch-scripts.git
[/code]

    * Where **TAG** is the latest branch tag of the Media Server scripts repository obtained from [here](Releases-for-CX-Voice-Components_1342256.html).

  * Navigate to the cloned repository to access the files:
[code] cd freeswitch-scripts
[/code]

  * Alter the file name of **cx_env.lua** to **cx_env-{Domain-Name}-{DN}.lua** where **{Domain-Name}** is the name of the Domain eg `expertflow`, or `tenant1`, **{DN}** is the **dialing number** of the IVR (Set in the **CxIvr Dialplan** section below).

    * e.g. for an IVR with a **dialing number** of **1555** and **Domain Name** is **tenant1** the file would be named **cx_env-tenant1-1555.lua.**
[code] mv cx_env.lua cx_env-tenant1-1555.lua
[/code]

  * Move the files ending in **.lua** to the **Media Server** scripts folder:

  * 
[code]mv *.lua /usr/share/freeswitch/scripts
[/code]

  * Move any custom IVR scripts to the **Media Server** scripts folder:
[code] mv <custom-lua-IVR-script> /usr/share/freeswitch/scripts
[/code]

  * Move the **ivr_prompts** folder: 
[code] mv ivr_prompts /usr/share/freeswitch/sounds/
[/code]

  * Assign read-write permissions to the **ivr_prompts** and **scripts** folder: 
[code] chmod 777 -R /usr/share/freeswitch/sounds/ivr_prompts
        chmod 777 -R /usr/share/freeswitch/scripts
[/code]

  * Assign the permission to recording directory. run this command to give the permission to recording directory
[code] chmod 777 -R /var/lib/freeswitch/recordings/
[/code]




### Configuration

  1. Open _**cx_env-{Domain-Name}-{DN}.lua**_ : 
[code] vi /usr/share/freeswitch/scripts/cx_env-{Domain-Name}-{DN}.lua
[/code]
[code] local config = {}
         
         local domain = session:getVariable("domain_name")
         
         local cxFqdn = ""
         if domain == "expertflow" then
             cxFqdn = "https://efcx4-voice.expertflow.com"  -- set Default Domain here 
         else
             cxFqdn = "https://" .. domain .. ".expertflow.com"  -- set Tenant based Domian here
         end
         
         config = {
             -- Set to NAME or ID depending on whether queue field contains name or ID of queue
             queueType = 'NAME',
             -- Name or ID of queue to reserve agents from
             queue = 'Test Voice Queue',
             -- NOTE: Keeping queue and queueType as '' will cause CX to use the default queue set in the CX Voice channel
             -- queue = '',
             -- queueType = '',
         
             -- FQDN of EF CX
             cxFqdn = cxFqdn,
             -- API of voice connector for reserving an agent
             voiceConnectorApi = "http://VC-IP:PORT",
             -- Path of folder containing sound files that play during the IVR menu, DO NOT CHANGE
             ivr_prompts_folder = "/usr/share/freeswitch/sounds/ivr_prompts/",
         
             auth_enabled = false,
             auth_realm = "expertflow",
             client_secret = "1234",
             client_id = "cim",
             username = "voice_auth",
             password = "1234"
         }
         
         return config
[/code]

  2. Press the **"I"** key to enter editing mode.

  3. The **cxFqdn** is dynamic in case of MTT, and for Single Tenant its value is hardcoded on **line 7.**

     1. **Single Tenant** : set **cxFqdn** as `https://efcx4-voice.expertflow.com` , replace it with actual FQDN. 

     2. **MTT** : cxFqdn is set dymanically by fetching the domain value form Channel Variables. The Root Domain need to be udpated. `expertflow.com` replace it with actual Domain

  4. The **queueType** field can contain one of two values:

     1. **'NAME'**

     2. **''**

  5. The **queue** field can contain one of **two types** of values, based on what the **queueType** field above contains:

     1. **Name** of the Agent Queue e.g. Support Queue (If **queueType** contains**'NAME'**) This name can be obtained from Unified Admin from the [Queues section](https://expertflow-docs.atlassian.net/wiki/x/94Qm#UnifiedAdminGuide-Step6%3ACreateaQueue).

     2. Empty string i.e. **''**(If **queueType** contains **''**)

  6. If **queue** and **queueType** are set to **''** , then the call will be routed to the default queue set for the [CX Voice channel in Unified Admin](https://expertflow-docs.atlassian.net/wiki/x/w5km).

  7. The **voiceConnectorApi** field will contain a URL in the following format:

     1. <http://VC-IP>:VC-PORT/request-agent

     2. Replace VC-IP and VC-PORT with IP address and port of the [voice connector](Voice-Connector-Deployment-Guide_48268951.html).

  8. The **ivr_prompts_folder** field contains path to the **ivr_prompts** folder. Leave it at the default value.

  9. **AUTH_ENABLED** : **true** or **false** depending on whether APISIX authentication is enabled in EFCX. The four settings below are set if this value is **true**.

  10. **API_USERNAME** : The username created in Keycloak for API authentication.

     * On Keycloak create a user in the Expertflow realm.

     * Assign the **admin** and **default** roles, and have **Email-Verified** option enabled.

     * Assign a non-temporary password to this user as well.

  11. **API_PASS** : The password for the above user created in Keycloak for API authentication

  12. **CLIENT_ID** : Should always be **cim**.

  13. **CLIENT_SECRET** : Found on Keycloak in the **cim** client.

  14. Save and exit the file by pressing the _**Esc** _key, entering _**:wq**_ and pressing **ENTER**.

  15. Steps 16-21 below are optional, in case Post-Call-Survey is in use.

  16. Open _**pcs1_env.lua**_ : 
[code] vi /usr/share/freeswitch/scripts/pcs1_env.lua
[/code]
[code] local config = {}
         config = {
         
             formId = "form-id123",
             cxFqdn = "https://devops.expertflow.com",
             ivr_prompts_folder = "/usr/share/freeswitch/sounds/ivr_prompts/"
         }
         return config
[/code]

  17. Press the **"I"** key to enter editing mode.

  18. The **formId** will contain the ID of the **PCS Survey form** created on Unified Admin (make sure that audio prompts were uploaded for each question).

  19. The **cxFqdn** field contains the fully qualified domain name of the EFCX:

     1. Replace [**devops.expertflow.com**](http://devops.expertflow.com) with the EFCX domain name.

  20. The **ivr_prompts_folder** field contains path to the **ivr_prompts** folder. Leave it at the default value.

  21. Save and exit the file by pressing the _**Esc** _key, entering _**:wq**_ and pressing **ENTER**.

  22. Open **vcApi.lua:**



[code] 
    vi /usr/share/freeswitch/scripts/vcApi.lua
[/code]

  23. Search for `fsIp` and Replace `fsIp = '192.168.1.161'` with your actual Media Server Public IP

  24. Save and exit the file by pressing the _**Esc** _key, entering _**:wq**_ and pressing **ENTER**.




## Multi-Domain Utility Implementaion

For detailed setup instructions and step-by-step process, please refer to the following link:  
👉 [**Multi-Domain Utility Implementation Guide**](https://expertflow-docs.atlassian.net/wiki/x/AQCLSg)

## Configure Dialplans (Global)

![](images/icons/grey_arrow_down.png)Domain Creation

Ignore the following steps if domain is already created using the [**Domain Creation Utility**](https://expertflow-docs.atlassian.net/wiki/spaces/CT/pages/1250623489/Multi-Domain+Utility+Implementaion+for+EF-Switch)

If Domain is not created then

  * Single Tenant: Domain name must be `expertflow`

  * MTT: Domain name can be anythig other than `expertflow`




  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891328.png?width=623)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Select the **Domains** option from the **Advanced** tab.


![](attachments/1468891146/1468891355.png?width=732)

  * Select the ADD button on the top right.


![](attachments/1468891146/1468891352.png?width=716)

  * Add the **Fully Qualified Domain Name(FQDN)** that was provided with the [Media Server](https://expertflow-docs.atlassian.net/wiki/pages/createpage.action?spaceKey=CX&title=EFSwitch%20Installation%20guide), as shown in the image below:


![](attachments/1468891146/1468891193.png?width=676)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Outbound IVR Dialplan

  * This section is optional, depending on whether the CX Dialer for Campaigns is in use.

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891325.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891358.png?width=610)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=658)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/1468891146/1468891271.png?width=658)

  * Fill the form with following details :

    * Name = <Name of your choice>

    * Condition 1 = Select **destination_number** from list and set the value to **out_(.*)**

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open the dialplan.

  * Delete the line with the **Action** tag (Click the **checkbox** in the right and press **SAVE** in the top right).

  * Add the following information to this dialplan:




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| wait_for_answer| | 0| 10| true  
action| set| sip_h_X-Destination-Number=$1| 0| 15| true  
action| lua| <script-name>| 0| 20| true  
  
  * **< script-name>** is the name of the **Outbound** **IVR script(default is outboundIvr.lua)**.

  * Set the **Context** field to the value of **global**.

  * Set the **Domain** field to the value of **global**.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Direct-Transfer Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891184.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891181.png?width=716)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=716)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/1468891146/1468891271.png?width=722)

  * Fill the form with following details :

    * Name = CxQueue

    * Condition 1 = Select **destination_number** from list and add a random number

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open CxQueue dialplan.

  * Change the value of the **Data** column in the **destination_number** row to **^99887766[-0-9a-zA-Z]*$**

  * Change the value of the **Type** column in the **Action** row to **lua** and the **Data** field to **vcApi.lua 'directTransfer'**


![](attachments/1468891146/1468891382.png?width=728)

  * Set the **Context** field to the value of **global**.

  * Set the **Domain** field to the value of **global**.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)External Consult and Transfer Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891184.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891181.png?width=716)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=716)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/1468891146/1468891271.png?width=722)

  * Fill the form with following details :

    * Name = External_Consult_and_Transfer

    * Condition 1 = Select **destination_number** from list and add a random number

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open the created dialplan.

  * Change the value of the **Data** column in the **destination_number** row to **^99887765[-0-9a-zA-Z]*$**

  * Change the value of the **Type** column in the **Action** row to **lua** and the **Data** field to **customTransfer.lua**


![image-20250313-085303.png](attachments/1468891146/1468891598.png?width=700)

  * Set the **Context** field to the value of **global**.

  * Set the **Domain** field to the value of **global**.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Progressive Outbound Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891331.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891370.png?width=658)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=654)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/1468891146/1468891271.png?width=642)

  * Fill the form with following details :

    * Name = Progressive Outbound Agent Transfer

    * Condition 1 = Select **destination_number** from list and set the value to **^agent$**

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open the Progressive Outbound Agent Transfer dialplan.

  * Set the **Context** field to the value of **global**.

  * Set the **Domain** field to the value of **global**.

  * Change the value of the **Type** column in the **Action** row to **bridge** and the **Data** field to **user/${sip_h_X-agentExtension}@${domain_name}**

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Manual Outbound Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891184.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891181.png?width=676)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=686)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/1468891146/1468891271.png?width=696)

  * Fill the form with following details :

    * Name = Manual_Outbound

    * Condition 1 = Click the black arrow to the right of the first field. In the first field enter **${sip_h_X-CallType}** and in the second field enter **^OUT$**.

    * Condition 2 = Click the black arrow to the right of the first field. In the first field enter **${customer_leg_uuid}** and in the second field enter **^$**.

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open Manual_Outbound dialplan.

  * Delete the line with the **Action** tag (Click the **checkbox** in the right and press **SAVE** in the top right)

  * Add the following information to this dialplan:




**Tag**| **Type**| **Data**| **Break**| **Inline**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---|---|---  
condition| **${sip_h_X-CallType}**|  ^OUT$| on-false| | 0| 5| true  
condition| **${customer_leg_uuid}**|  ^$| never| | 0| 10| true  
action| set| custom_origination_uuid=${create_uuid()}| | true| 0| 15| true  
action| set| customer_leg_uuid=${custom_origination_uuid}| | true| 0| 20| true  
action| export| customer_leg_uuid=${custom_origination_uuid}| | true| 0| 25| true  
anti-action| set| custom_origination_uuid=${create_uuid()}| | true| 0| 30| true  
  
![image-20250722-101756.png](attachments/1468891146/1468891622.png?width=700)

  * Set the **Context** field to the value of **global**.

  * Set the **Domain** field to the value of **global**.

  * Set the **Order** field to **49**.

  * Set the **Continue** field to **True**.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Custom Hangup Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891184.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891181.png?width=676)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=686)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/1468891146/1468891271.png?width=696)

  * Fill the form with following details :

    * Name = Custom_Hangup

    * Condition 1 = Click the black arrow to the right of the first field. In the first field enter **${user_exists}** and in the second field enter **${user_exists}**.

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open Custom_Hangup dialplan.

  * Delete the line with the **Action** tag (Click the **checkbox** in the right and press **SAVE** in the top right)

  * Add the following information to this dialplan:




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
condition| **${user_exists}**| **${user_exists}**|  0| 5| true  
action| set| sip_rh_X-CALL-DROPPED-CUSTOM-REASON=NO-DIALPLAN-FOUND| 0| 10| true  
action| sleep| 1000| 0| 12| true  
action| hangup| | 0| 15| true  
  
![Screenshot 2025-02-25 141521.png](attachments/1468891146/1468891595.png?width=851)

  * Set the **Context** field to **global**.

  * Set the **Domain** field to **Global**.

  * Set the **Order** field to **999**.

  * Set the **Continue** field to **False**.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Silent Monitoring Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891184.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891181.png?width=676)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=686)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/1468891146/1468891271.png?width=696)

  * Fill the form with following details :

    * Name = Silent Monitoring

    * Condition 1 = Select **destination_number** from list and add **^\\*44(.+)$**

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open Silent Monitoring dialplan.

  * Delete the line with the **Action** tag (Click the **checkbox** in the right and press **SAVE** in the top right)

  * Add the following information to this dialplan:




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| set| sip_h_X-CallType=MONITOR| 0| 10| true  
action| export| sip_h_X-CallType=MONITOR| 0| 15| true  
action| lua| eavesdrop_custom.lua $1| 0| 20| true  
  
![image-20241106-132815.png](attachments/1468891146/1468891568.png?width=750)

  * Set the **Context** field to the value of **global**.

  * Set the **Domain** field to the value of **global**.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Conference Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891184.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891181.png?width=693)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=686)

  * Add a new Dialplan by pressing the **Add** Button on the top.


![](attachments/1468891146/1468891271.png?width=676)

  * Fill the form with following details :

    * Name = CustomConf

    * Condition 1 = Select **destination_number** from list and add **^custom_conf_(.*)$**

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open **CustomConf** dialplan.

  * Delete the line with the **Action** tag (Click the **checkbox** in the right and press **SAVE** in the top right)

  * Add the following information to this dialplan:




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| answer| | 0| 10| true  
action| set| session_in_hangup_hook=true| 0| 15| true  
action| export| session_in_hangup_hook=true| 0| 20| true  
action| set| api_hangup_hook=lua cx_hangup.lua $1| 0| 25| true  
action| export| api_hangup_hook=lua cx_hangup.lua $1| 0| 30| true  
action| set| absolute_codec_string=G7221@32000h,G7221@16000h,G722,PCMU,PCMA| 0| 31| true  
action| export| absolute_codec_string=G7221@32000h,G7221@16000h,G722,PCMU,PCMA| 0| 32| true  
action| conference| $1| 0| 35| true  
  
![image-20250425-113642.png](attachments/1468891146/1468891613.png?width=1083)

  * Set the **Context** field to the value of **global**.

  * Set the **Domain** field to the value of **global**.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in User Exists Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891337.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891367.png?width=670)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=640)

  * Find and open the **user_exists** dialplan.

  * Add the following information(to add custom values in the **Type** column, select a random value then click on it to edit):




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
condition| ${sip_h_X-CallType}| ^CONSULT$| 3| 5| true  
action| bind_meta_app| A a s1 lua::consult_conf.lua CONSULT_TRANSFER| 3| 10| true  
action| bind_meta_app| C a s1 lua::consult_conf.lua CONSULT_CONFERENCE| 3| 15| true  
  
  * The result will look like this:


![image-20240702-062405.png](attachments/1468891146/1468891508.png?width=600)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in Local extension Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891337.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891367.png?width=670)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=640)

  * Find and open the **local_extension** dialplan.

  * Add the following information to the last group:




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| set| transfer_after_bridge=pcs1| 1| 73| true  
action| ring_ready| true| 1| 74| true  
action| lua| vcApi.lua 'rona'| 1| 76| true  
  
  * **Action:** Set `transfer_after_bridge=pcs1` and enable it (`true`) **only when PCS is required.**

  * Secondly, replace the **Data** field in the line with **Order 75** with: **{origination_uuid=${custom_origination_uuid}}user/${destination_number}@${domain_name}**

  * The result will look like this:


![image-20241211-061407.png](attachments/1468891146/1468891571.png?width=750)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in Global Variables dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891340.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891379.png?width=665)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=686)

  * Find and open the **global-variables** dialplan.

  * Add the following information to this dialplan (to add custom values in the **Type** column, select a random value then click on it to edit):




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| set| FreeSWITCH-IPv4=${domain_name}| 0| 20| true  
  
**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
condition| ${sip_h_X-CALL-ID}| ^$| 2| 5| true  
action| set| sip_h_X-CALL-ID=${sip_call_id}| 2| 10| true  
action| set| sip_rh_X-CALL-ID=${sip_call_id}| 2| 15| true  
  
**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
condition| ${sip_h_X-CALL-VARIABLE0}| ^$| 3| 5| true  
action| set| sip_h_X-CALL-VARIABLE0=${uuid}| 3| 10| true  
action| set| sip_rh_X-CALL-VARIABLE0=${uuid}| 3| 15| true  
  
**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| export| sip_h_X-CALL-ID=${sip_h_X-CALL-ID}| 4| 5| true  
action| export| sip_rh_X-CALL-ID=${sip_h_X-CALL-ID}| 4| 10| true  
action| export| sip_h_X-CALL-VARIABLE0=${sip_h_X-CALL-VARIABLE0}| 4| 15| true  
action| export| sip_rh_X-CALL-VARIABLE0=${sip_h_X-CALL-VARIABLE0}| 4| 20| true  
  
  * The result will look like:


![image-20250505-082711.png](attachments/1468891146/1468891616.png?width=800)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in Call Recording Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1085931521/1085931591.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1085931521/1085931594.png?width=776)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1085931521/1085931624.png?width=726)

  * Find and open the **user_record** dialplan.

  * Make sure to **delete the lines present previously in** **Group 9 apart from the first one** , and NOT in the table and image below.

  * Add the following data to the table, such that the final version of**Group 9** looks like the image below: 




**Tag**| **Type**| **Data**| **Inline**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---|---  
condition| ${record_session}| ^true$| | 9| 5| true  
action| set| record_path=${recordings_dir}/${domain_name}/archive/${strftime(%Y)}/${strftime(%b)}/${strftime(%d)}| true| 9| 10| true  
action| export| record_path=${recordings_dir}/${domain_name}/archive/${strftime(%Y)}/${strftime(%b)}/${strftime(%d)}| true| 9| 15| true  
action| set| record_name=${uuid}.${record_ext}| true| 9| 20| true  
action| set| recording_follow_transfer=false| true| 9| 25| true  
action| export| recording_follow_transfer=false| true| 9| 30| true  
action| set| record_append=true| true| 9| 35| true  
action| export| record_append=true| true| 9| 40| true  
action| set| record_in_progress=true| true| 9| 45| true  
action| set| RECORD_ANSWER_REQ=true| -| 9| 50| true  
action| export| RECORD_ANSWER_REQ=true| -| 9| 55| true  
  
![image-20250430-135151.png](attachments/1085931521/1085571142.png?width=900)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Codec Configuration

### **Steps to Verify and Add H.264 Codec**  


For WebRTC video calls we need H.264 Codec. Follow the steps to configure the H.264 codec. In case WebRTC video calls are not required move to next step

  1. Go to **Status → SIP Status**

  2. Click on **Sofia Status Profile Internal,** and then **Sofia Status Profile External**  
Check the loaded codecs for both **Internal** and **External** profiles.

  3. If **H.264** is showing, stop here — everything is fine.  
If **H.264** is not listed, continue to the next steps.

  4. Go to **Advanced → Variables**

  5. In the search bar, type **global_codec_prefs**

  6. Open the variable and add **H264** at the end of the list  
(for example: `PCMU,PCMA,OPUS,H264`)

  7. Do the same for **outbound_codec_prefs**  
(add `H264` at the end)

  8. Go back to **Advance → SIP Profile**

  9. Find internal and external. Go to **Internal**

  10. Find the variables **inbound_codec_prefs** and **outbound_codec_prefs**

  11. Change their value to **123** temporarily

  12. Do same for the **external**

  13. Go to **Status → SIP Status**

  14. Stop both **Internal** and **External** SIP profiles

  15. Start both profiles again

  16. Go back to **Status → SIP Status**

  17. Go to **Sofia Status Profile External** and check  
Now the codec values should show **123**

  18. Check for **Sofia Status Profile Internal** as well 

  19. Go to **Advanced → SIP Profiles → Internal**

  20. Find the field for codec preferences and change the value from **123** to  
`$${global_codec_prefs}`

  21. Go to **Advanced → SIP Profiles → External**

  22. Change the value from **123** to  
`$${outbound_codec_prefs}`

  23. Save both profiles

  24. Go to **Status → SIP Status** again

  25. Stop and start both **Internal** and **External** profiles

  26. Check the loaded codecs again  
You should now see **H.264** listed for both profiles.




![](images/icons/grey_arrow_down.png)Turn OFF the voicemail dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891184.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891181.png?width=693)

  * Once the domain is selected then click on the dilaplan menu and on the drop down section click the dialplan manager. once the dial plan are open search for the `voicemail `dilaplan

![image-20251104-103050.png](attachments/1468891146/1468891178.png?width=1240)
  * Cline on the voicemail dialplan is opened like below, then turned off the `Enabled` button to make the dialplan false/turnoff

![image-20251104-103332.png](attachments/1468891146/1468891175.png?width=1320)



## Changes in conference profile

![](images/icons/grey_arrow_down.png)Changes in conference profile

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891337.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891367.png?width=776)

  * Open the **Conference Profiles** section under the **Applications** tab:


![image-20240822-053906.png](attachments/1468891146/1468891523.png?width=776)

  * Open the profile named **default** :


![image-20240822-054148.png](attachments/1468891146/1468891520.png?width=776)

  * Under the **Profile Parameters** , find the following keywords under the **Name** column and click the checkbox:


![image-20241129-135352.png](attachments/1468891146/1468891562.png?width=770)

  * Press **TOGGLE** in the top right and choose **CONTINUE** in the prompt shown.


![image-20241129-135211.png](attachments/1468891146/1468891565.png?width=770)

  * Save the changes by pressing **SAVE** button in top right corner.




## Changes in SIP Profile

![](images/icons/grey_arrow_down.png)Changes in SIP Profile

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891346.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891370.png?width=654)

  * Open **SIP Profiles** under the **Advanced** tab.


![image-20240424-103707.png](attachments/1468891146/1468891445.png?width=640)

  * Open the **internal** profile, scroll down to the **ws-binding** and **wss-binding** fields, and set their **Enabled** column values to **True**.


![image-20240503-121016.png](attachments/1468891146/1468891478.png?width=630)

  * Find the **disable-transcoding** field and its **Value** and **Enabled** columns to **true**.

  * Find the **nat-options-ping** fields and its **Value** and **Enabled** columns to **true**.

  * Find the **liberal-dtmf** fields and its **Value** and **Enabled** columns to **true**.

  * At the bottom add the data:




**Name**| **Value**| **Enabled**  
---|---|---  
apply-candidate-acl| 0.0.0.0/0| True  
  
  * Press the **SAVE** button on the top right.

  * Open **SIP Status** under the **Status** tab.

  * Locate the line **sofia status profile internal** and to its right press the **RESCAN** button, followed by the **RESTART** button after the page reloads.


![image-20240503-121411.png](attachments/1468891146/1468891475.png?width=686)

## Configure Access Control List (ACL)

![](images/icons/grey_arrow_down.png)Configure Access Control List (ACL)

Repeat this step for each single tenant, only once for MTT.

For the Voice Connector and Dialer to be able to access the Freeswitch ESL for communicating with Media Server, their IP address must be added to the ACL.

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891346.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891370.png?width=686)

  * Open the **Access Control List** from the **Advanced** tab.


![](attachments/1468891146/1468891394.png?width=692)

  * Create a new **ACL** with the **Add** button.


![](attachments/1468891146/1468891406.png?width=716)

  * Set the name to **esl** , the **Default** to **deny** and add the following IP addresses, with the **Type** fields set to **allow** :

    * 127.0.0.1

    * The IP address of the Media Server e.g. 192.168.1.17.

    * The IP address of the server the Voice connector is running on e.g. 192.168.1.201.

    * The IP address of the server the Dialer is running on e.g. 192.168.1.106.

    * Lastly, add the IP addresses of the docker containers for the **Voice connector** and **Dialer**.

      * On the Voice connector and Dialer servers, use the command **docker ps** to list the containers.


![](attachments/1468891146/1468891256.png?width=832)

  * Run the command: 

    * 
[code]docker inspect containerID
[/code]

    * Scroll down to the Networks object and find the Gateway and IPAddress fields.


![](attachments/1468891146/1468891259.png?width=750)

  * Copy these two addresses to the **esl** ACL.

    * Make sure to do this process for both the Voice connector and dialer.

  * Click the **Save** button and go to the **SIP Status** with from the **Status** tab.


![](attachments/1468891146/1468891403.png?width=693)

  * Click the **Reload ACL** button on the top right.


![](attachments/1468891146/1468891250.png?width=658)

## Configure Event Socket Library (ESL)

![](images/icons/grey_arrow_down.png)Configure Event Socket Library (ESL)

  1. Login to Media Server web interface. 

     * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891343.png?width=500)

  1. Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  2. Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891376.png?width=689)

  1. Open **Settings** from the **Advanced** tab. (If the option is unavailable, skip to step 6)


![](attachments/1468891146/1468891400.png?width=693)

  1. Change the **Event Socket IP Address** to **0.0.0.0** , and the **Event Socket ACL** to **esl**.


![](attachments/1468891146/1468891277.png?width=654)

  1. Optionally, change the **Event Socket Password** to the a different value, or leave as default **ClueCon**.

     * If the password is changed, then the same must be set in the environment files for the [voice connector](Voice-Connector-Deployment-Guide_48268951.html) and [dialer](CX-Dialer-Deployment-Guide_2529764.html).

     * If the password is changed, update it in the environment variables for the and Dialer docker containers.

  2. SSH into the Media Server.
[code] ssh username@server-ip
[/code]

  3. Enter user password and press **ENTER**.

  4. Use command 
[code] su
[/code]

  5. Enter root password and press **ENTER**.

  6. If the **Settings** option in **Step 4** was unavailable, then run the following command
[code] echo '<configuration name="event_socket.conf" description="Socket Client">
           <settings>
             <param name="nat-map" value="false"/>
             <param name="listen-ip" value="0.0.0.0"/>
             <param name="listen-port" value="8021"/>
             <param name="password" value="PASSWORD"/>
             <param name="apply-inbound-acl" value="esl"/>
           </settings>
         </configuration>' > /etc/freeswitch/autoload_configs/event_socket.conf.xml
[/code]

     1. In following command replace **customEslPass** with your chosen password, then run the command
[code] sed -i 's/PASSWORD/customEslPass/g' /etc/freeswitch/autoload_configs/event_socket.conf.xml
[/code]

  7. Run the command to restart Media Server with the new ESL settings: 
[code] systemctl restart freeswitch
[/code]

  8. Run the following command:
[code] echo "switch.event_socket.host = 0.0.0.0
         switch.event_socket.port = 8021
         switch.event_socket.password = EslPass" | sudo tee -a /etc/fusionpbx/config.conf
[/code]

     1. In following command replace **customEslPass** with the password chosen in Step 6a, then run the command
[code] sed -i 's/EslPass/customEslPass/g' /etc/fusionpbx/config.conf
[/code]

  9. Log out of the Media Server web interface and log back in.




## Media Server Config Files

![](images/icons/grey_arrow_down.png)Set Media Server Call Limits

  * SSH into the Media Server.

    * Use command 
[code] ssh username@server-ip
[/code]

    * Enter user password and press **ENTER**.

    * Use command 
[code] su
[/code]

    * Enter root password and press **ENTER**.

  * Open the Media Server config file
[code] vi /etc/freeswitch/autoload_configs/switch.conf.xml
[/code]

  * Locate the following line and replace 1000 with 100000
[code] <param name="max-sessions" value="1000"/>
[/code]

  * Locate the following line and replace 30 with 100000
[code] <param name="sessions-per-second" value="30"/>
[/code]

  * Run the command to restart Media Server with the new ESL settings: 
[code] systemctl restart freeswitch
[/code]




![](images/icons/grey_arrow_down.png)Add call ending event hook

  * SSH into the Media Server.

    * Use command 
[code] ssh username@server-ip
[/code]

    * Enter user password and press **ENTER**.

    * Use command 
[code] su
[/code]

    * Enter root password and press **ENTER**.

  * Open **/etc/freeswitch/autoload_configs/lua.conf.xml**

  * Find the line near the end containing **<!-- Subscribe to events -->**

  * Insert the following under it:
[code] <hook event="CHANNEL_HANGUP_COMPLETE" subclass="" script="hangup_event.lua"/>
        <hook event="CHANNEL_BRIDGE" subclass="" script="channel_bridge.lua"/>
        <hook event="CHANNEL_UNBRIDGE" subclass="" script="channel_unbridge.lua"/>
        <hook event="CHANNEL_CALLSTATE" subclass="" script="channel_state.lua"/>
[/code]

  * Save the file.

  * Run the command: 



[code] 
    systemctl restart freeswitch
[/code]

![](images/icons/grey_arrow_down.png)Enable mod

  * SSH into the Media Server.

    * Use command 
[code] ssh username@server-ip
[/code]

    * Enter user password and press **ENTER**.

    * Use command 
[code] su
[/code]

    * Enter root password and press **ENTER**.

  * Open **/etc/freeswitch/autoload_configs/modules.conf.xml**

  * Find the line near the top containing **<!-- Applications -->**

  * Insert the following under it:
[code] <load module="mod_httapi"/>
[/code]

  * Save the file.

  * Run the command: 



[code] 
    systemctl restart freeswitch
[/code]

![](images/icons/grey_arrow_down.png)Configuring Nginx for WSS Path (/wss) in FusionPBX

  * SSH into the Media Server.

    * Use command 
[code] ssh username@server-ip
[/code]

    * Enter user password and press **ENTER**.

    * Use command 
[code] su
[/code]

    * Enter root password and press **ENTER**.

  * **Locate Nginx Configuration**




On most FusionPBX systems, Nginx configuration files are located at:
[code] 
    /etc/nginx/sites-available/fusionpbx
[/code]

or
[code] 
    /etc/nginx/sites-enabled/fusionpbx
[/code]

### **2\. Add the /wss Location Block**

Inside the main `server { }` block that handles HTTPS (`listen [::]:443 ssl;` ), add the following configuration:
[code] 
    location /wss {
        proxy_pass https://<IP>:7443;
        proxy_pass_header Authorization;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_read_timeout 600s;
        proxy_send_timeout 600s;
        client_body_timeout 600s;
        send_timeout 300s;
    }
[/code]

Replace `<IP>` with your **FreeSWITCH IP** (usually `192.168.1.17`).

### **3\. Test Nginx Configuration**

Run the following command to check for syntax errors:
[code] 
    sudo nginx -t
[/code]

If successful, reload Nginx:
[code] 
    sudo systemctl reload nginx
[/code]

* * *

# 2\. Configuration (on Each Domain)

### Configuration

  1. Open _**cx_env-{Domain-Name}-{DN}.lua**_ :
[code] vi /usr/share/freeswitch/scripts/cx_env-{Domain-Name}-{DN}.lua
[/code]
[code] local config = {}
         local domain = session:getVariable("domain_name")
         local cxFqdn = ""
         if domain == "expertflow" then
             cxFqdn = "https://efcx4-voice.expertflow.com"  -- set Default Domain here 
         else
             cxFqdn = "https://" .. domain .. ".expertflow.com"  -- set Tenant based Domian here
         end
         config = {
             -- Set to NAME or ID depending on whether queue field contains name or ID of queue
             queueType = 'NAME',
             -- Name or ID of queue to reserve agents from
             queue = 'Test Voice Queue',
             -- NOTE: Keeping queue and queueType as '' will cause CX to use the default queue set in the CX Voice channel
             -- queue = '',
             -- queueType = '',
             -- FQDN of EF CX
             cxFqdn = cxFqdn,
             -- API of voice connector for reserving an agent
             voiceConnectorApi = "http://VC-IP:PORT",
             -- Path of folder containing sound files that play during the IVR menu, DO NOT CHANGE
             ivr_prompts_folder = "/usr/share/freeswitch/sounds/ivr_prompts/",
             auth_enabled = false,
             auth_realm = "expertflow",
             client_secret = "1234",
             client_id = "cim",
             username = "voice_auth",
             password = "1234"
         }
         return config
[/code]

  2. Press the **"I"** key to enter editing mode.

  3. The **cxFqdn** is dynamic in case of MTT, and for Single Tenant its value is hardcoded on **line 7.**

     1. **Single Tenant** : set **cxFqdn** as `https://efcx4-voice.expertflow.com` , replace it with actual FQDN.

     2. **MTT** : cxFqdn is set dymanically by fetching the domain value form Channel Variables. The Root Domain need to be udpated. `expertflow.com` replace it with actual Domain

  4. The **queueType** field can contain one of two values:

     1. **'NAME'**

     2. **''**

  5. The **queue** field can contain one of **two types** of values, based on what the **queueType** field above contains:

     1. **Name** of the Agent Queue e.g. Support Queue (If **queueType** contains**'NAME'**) This name can be obtained from Unified Admin from the [_Queues section_](https://expertflow-docs.atlassian.net/wiki/x/94Qm#UnifiedAdminGuide-Step6%3ACreateaQueue).

     2. Empty string i.e. **''**(If **queueType** contains **''**)

  6. If **queue** and **queueType** are set to **''** , then the call will be routed to the default queue set for the [_CX Voice channel in Unified Admin_](https://expertflow-docs.atlassian.net/wiki/x/w5km).

  7. The **voiceConnectorApi** field will contain a URL in the following format:

     1. [_http://VC-IP_](http://vc-ip/):VC-PORT/request-agent

     2. Replace VC-IP and VC-PORT with IP address and port of the [_voice connector_](Voice-Connector-Deployment-Guide_48268951.html).

  8. The **ivr_prompts_folder** field contains path to the **ivr_prompts** folder. Leave it at the default value.

  9. **AUTH_ENABLED** : **true** or **false** depending on whether APISIX authentication is enabled in EFCX. The four settings below are set if this value is **true**.

  10. **API_USERNAME** : The username created in Keycloak for API authentication.

     * On Keycloak create a user in the Expertflow realm.

     * Assign the **admin** and **default** roles, and have **Email-Verified** option enabled.

     * Assign a non-temporary password to this user as well.

  11. **API_PASS** : The password for the above user created in Keycloak for API authentication

  12. **CLIENT_ID** : Should always be **cim**.

  13. **CLIENT_SECRET** : Found on Keycloak in the **cim** client.

  14. Save and exit the file by pressing the _**Esc** _key, entering _**:wq**_ and pressing **ENTER**.

  15. Steps 16-21 below are optional, in case Post-Call-Survey is in use.

  16. Open _**pcs1_env.lua**_ :
[code] vi /usr/share/freeswitch/scripts/pcs1_env.lua
[/code]
[code] local config = {}
         config = {
             formId = "form-id123",
             cxFqdn = "https://devops.expertflow.com",
             ivr_prompts_folder = "/usr/share/freeswitch/sounds/ivr_prompts/"
         }
         return config
[/code]

  17. Press the **"I"** key to enter editing mode.

  18. The **formId** will contain the ID of the **PCS Survey form** created on Unified Admin (make sure that audio prompts were uploaded for each question).

  19. The **cxFqdn** field contains the fully qualified domain name of the EFCX:

     1. Replace [**_devops.expertflow.com_**](http://devops.expertflow.com/) with the EFCX domain name.

  20. The **ivr_prompts_folder** field contains path to the **ivr_prompts** folder. Leave it at the default value.

  21. Save and exit the file by pressing the _**Esc** _key, entering _**:wq**_ and pressing **ENTER**.

  22. Open **vcApi.lua:**



[code] 
    vi /usr/share/freeswitch/scripts/vcApi.lua
[/code]

  23. Search for `fsIp` and Replace `fsIp = '192.168.1.161'` with your actual Media Server Public IP

  24. Save and exit the file by pressing the _**Esc** _key, entering _**:wq**_ and pressing **ENTER**.




## Configure Dialplans

![](images/icons/grey_arrow_down.png)Domain Creation

Ignore the following steps if domain is already created using the [**Domain Creation Utility**](https://expertflow-docs.atlassian.net/wiki/x/AQCLSg)

If Domain is not created then

  * Single Tenant: Domain name must be `expertflow`, if its already exist then dont create new

  * MTT: Domain name can be anythig other than `expertflow`




  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891328.png?width=623)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Select the **Domains** option from the **Advanced** tab.


![](attachments/1468891146/1468891355.png?width=732)

  * Select the ADD button on the top right.


![](attachments/1468891146/1468891352.png?width=716)

  * Add the **Fully Qualified Domain Name(FQDN)** that was provided with the [Media Server](https://expertflow-docs.atlassian.net/wiki/pages/createpage.action?spaceKey=CX&title=EFSwitch%20Installation%20guide), as shown in the image below:


![](attachments/1468891146/1468891193.png?width=676)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Inbound IVR Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891325.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891358.png?width=610)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=658)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/1468891146/1468891271.png?width=658)

  * Fill the form with following details :

    * Name = <Name of your choice>

    * Condition 1 = Select **destination_number** from list and add a dialing number in the format **^dialing_number$** , matching the **{DN}** value in the **cx_env{DN}lua** script filename set in the **IVR scripts** section above.

      * e.g. for a dialing number of 1218, the field must have the value**^5555$**.

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open the dialplan.

  * Change action from **transfer** to **lua** and add the name of the custom **Inbound** **IVR script(default is cxIvr.lua)** into data column so the result looks like this:


![image-20250304-074926.png](attachments/1468891146/1468891589.png?width=700)

  * Set the **Context** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Domain** field to the value of the **Domain** set in the **Domain creation** section.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)WebRTC Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891334.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891364.png?width=696)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=674)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/1468891146/1468891271.png?width=676)

  * Fill the form with following details:

    * Name = Name of your choice

    * Condition 1 = Select **destination_number** from list and add the **webRTC dialing number(Set in Unified Admin, under Web Widget settings)** in the format **^dialing_number$**.

      * e.g. for a dialing number of 123456, the field must have the value**^123456$**.

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open the dialplan.

    * Change action from **transfer** to **lua** and add **vcApi.lua 'webrtc'** into data column so the result looks like this:

![image-20250304-081009.png](attachments/1468891146/1468891604.png?width=700)
  * Set the **Context** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Domain** field to the value of the **Domain** set in the **Domain creation** section.

  * Save the changes by pressing **SAVE** button in top right corner.

  * Make sure that H264. If not added follow the Codec Configuration step give above in this document. 




![](images/icons/grey_arrow_down.png)Post Call Survey Dialplan

  * This section is optional, in case Post-Call-Survey is in use.

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891184.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891181.png?width=676)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1468891146/1468891409.png?width=686)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/1468891146/1468891271.png?width=696)

  * Fill the form with following details :

    * Name = PCS

    * Condition 1 = Select **destination_number** from list and set the value to **^pcs1$**

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open PCS dialplan.

  * Delete the line with the **Action** tag (Click the **checkbox** in the right and press **SAVE** in the top right)

  * Add the following information to this dialplan:




**Tag**| **Type**| **Data**| **Break**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---|---  
action| lua| pcs.lua| | 0| 10| true  
  
![image-20241211-061748.png](attachments/1468891146/1468891577.png?width=750)

  * Set the **Context** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Domain** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Order** field to **49**.

  * Set the **Continue** field to **True**.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in Call Recording Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1085931521/1085931591.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1085931521/1085931594.png?width=776)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1085931521/1085931624.png?width=726)

  * Find and open the **user_record** dialplan.

  * Make sure to **delete the lines present previously in** **Group 9 apart from the first one** , and NOT in the table and image below.

  * Add the following data to the table, such that the final version of**Group 9** looks like the image below: 




**Tag**| **Type**| **Data**| **Inline**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---|---  
condition| ${record_session}| ^true$| | 9| 5| true  
action| set| record_path=${recordings_dir}/${domain_name}/archive/${strftime(%Y)}/${strftime(%b)}/${strftime(%d)}| true| 9| 10| true  
action| export| record_path=${recordings_dir}/${domain_name}/archive/${strftime(%Y)}/${strftime(%b)}/${strftime(%d)}| true| 9| 15| true  
action| set| record_name=${uuid}.${record_ext}| true| 9| 20| true  
action| set| recording_follow_transfer=false| true| 9| 25| true  
action| export| recording_follow_transfer=false| true| 9| 30| true  
action| set| record_append=true| true| 9| 35| true  
action| export| record_append=true| true| 9| 40| true  
action| set| record_in_progress=true| true| 9| 45| true  
action| set| RECORD_ANSWER_REQ=true| -| 9| 50| true  
action| export| RECORD_ANSWER_REQ=true| -| 9| 55| true  
  
![image-20250430-135151.png](attachments/1085931521/1085571142.png?width=900)

  * Save the changes by pressing **SAVE** button in top right corner.




## Configure SIP Trunk and routes

![](images/icons/grey_arrow_down.png)Configure SIP Trunk(Gateway) for outbound calls

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891346.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891370.png?width=726)

  * Open the **Gateways** section under the **Accounts** tab.


![image-20240424-103321.png](attachments/1468891146/1468891442.png?width=716)

  * Press the **ADD** button in the top right.


![image-20240424-103357.png](attachments/1468891146/1468891439.png?width=732)

  * Set the following fields:

    1. **Gateway** : A name of your choice e.g. MySipTrunk

    2. **Username** : The username of the SIP Trunk. Not needed for **IP-based** SIP trunks.

    3. **Password** : The password of the SIP Trunk. Not needed for**IP-based** SIP trunks.

    4. **Proxy** : The IP address and port of the SIP trunk e.g. 192.168.25.35:5060.

    5. **Register** : Set to **True**. Set to **False** for **IP-based** SIP trunks.

  * Press the **SAVE** button on the top right.


![image-20240424-103500.png](attachments/1468891146/1468891436.png?width=692)

  * Open this newly created gateway and note the **URL** opened in the browser.


![image-20240424-103612.png](attachments/1468891146/1468891451.png?width=676)

  * Add the IP address of the **SIP trunk** to the **Media Server ACL** :

    * Open **SIP Profiles** under the **Advanced** tab.


![](attachments/1468891146/1468891445.png?width=728)

  * Open the **external** profile and note the value of the **apply-register-acl** field.


![image-20240424-103735.png](attachments/1468891146/1468891460.png?width=716)

  * Open **Access controls** under the **Advanced** tab.


![image-20240424-103757.png](attachments/1468891146/1468891457.png?width=640)

  * Open the entry that matches the aforementioned **apply-register-acl** field.


![image-20240424-103813.png](attachments/1468891146/1468891454.png?width=658)

  * At the bottom add an entry where the the **Type** is set to ‘**allow** ’ and the **CIDR** field contains the **address** of the SIP Trunk.

  * Press the **SAVE** button on the top right.

  * Open **SIP Status** under the **Status** tab.


![image-20240424-103838.png](attachments/1468891146/1468891469.png?width=666)

  * Press the **Reload ACL** button at the top right.

  * Open **SIP Profiles** under the **Advanced** tab.


![image-20240424-103707.png](attachments/1468891146/1468891445.png?width=658)

  * Open the **external** profile and note the value of the **sip-port** field.


![image-20240424-103930.png](attachments/1468891146/1468891466.png?width=654)

  *   * Back out via the **BACK** button on the top right.

  * Open the **internal** profile and note the value of the **sip-port** field.


![image-20240424-104001.png](attachments/1468891146/1468891463.png?width=665)

  * Open a terminal and SSH into the Media Server machine via the command

    * 
[code]ssh Media-Server-Username@Media-Server-IP-Address
[/code]

  * Enter the Media Server **SSH password** when prompted.

  * Enter and run the command

    * 
[code]su
[/code]

  * And enter the Media Server **root password**.

  * Run the command

    * 
[code]sudo iptables -A INPUT -p tcp -m tcp --dport PORT -j ACCEPT
[/code]

    * Where **PORT** is the port noted down in the previous steps. Run the command once for each port.

  * Run the command

    * 
[code]sudo iptables-save
[/code]

  * Contact the SIP Trunk provider and have all traffic from the **Media Server** machine **public** IP address allowed.




![](images/icons/grey_arrow_down.png)Configuring route For Outbound calls

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891346.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891370.png?width=658)

  * Open the **Outbound Routes** section under the **Dialplans** tab.


![](attachments/1468891146/1468891424.png?width=658)

  * Press the **ADD** button in the top right.


![](attachments/1468891146/1468891421.png?width=658)

  * Set the following fields :

    * Gateway = The name of the gateway configured above.

    * Dialplan Expression = The format of the number accepted by the SIP trunk e.g. for 11 digits the format is ^(\d{11})$

  * Press the **SAVE** button on top right corner.

  * Re-open this newly created Outbound Route.

  * Add the following information to the last group:




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| ring_ready| true| 0| 125| true  
  
  * To the last row, where the **Type** field is **bridge** , append **{origination_uuid=${custom_origination_uuid}}** to the **start of the field** in the **Data** column. The result will look as below:


![image-20241023-080613.png](attachments/1468891146/1468891553.png?width=750)

  * Set the **Context** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Domain** field to the value of the **Domain** set in the **Domain creation** section.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Configuring route For Inbound calls

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891346.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891370.png?width=689)

  * Open the **Destinations** section under the **Dialplans** tab.


![](attachments/1468891146/1468891430.png?width=676)

  * Press the **ADD** button in the top right.


![](attachments/1468891146/1468891427.png?width=646)

  * In the **Destination** field set the inbound dialing number provided by the SIP trunk provider in the format **^dialing_number$**.

    * e.g. for a dialing number of 1234, the field must have the value**^1234$**.

  * Press the **SAVE** button on top right Corner.

  * Open the **Inbound Routes** section under the **Dialplans** tab.


![](attachments/1468891146/1468891418.png?width=707)

  * Press the **ADD** button in the top right.


![](attachments/1468891146/1468891433.png?width=665)

  * Set the following fields :

    * Name = A name of your choice.

    * Destination Number = The destination created above.

    * Action = From the **Extensions** list select the number chosen as the destination number in the CxIvr dialplan section above.

  * Press the **SAVE** button on top right Corner.




## Configure Access Control List (ACL)

![](images/icons/grey_arrow_down.png)Configure Access Control List (ACL)

Repeat this step for each single tenant, only once for MTT.

Perform this step once VC and Dialer are deployed

For the Voice Connector and Dialer to be able to access the Freeswitch ESL for communicating with Media Server, their IP address must be added to the ACL.

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1468891146/1468891346.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1468891146/1468891370.png?width=686)

  * Open the **Access Control List** from the **Advanced** tab.


![](attachments/1468891146/1468891394.png?width=692)

  * Create a new **ACL** with the **Add** button.


![](attachments/1468891146/1468891406.png?width=716)

  * Set the name to **esl** , the **Default** to **deny** and add the following IP addresses, with the **Type** fields set to **allow** :

    * 127.0.0.1

    * The IP address of the Media Server e.g. 192.168.1.17.

    * The IP address of the server the Voice connector is running on e.g. 192.168.1.201.

    * The IP address of the server the Dialer is running on e.g. 192.168.1.106.

    * Lastly, add the IP addresses of the docker containers for the **Voice connector** and **Dialer**.

      * On the Voice connector and Dialer servers, use the command **docker ps** to list the containers.


![](attachments/1468891146/1468891256.png?width=832)

  * Run the command: 

    * 
[code]docker inspect containerID
[/code]

    * Scroll down to the Networks object and find the Gateway and IPAddress fields.


![](attachments/1468891146/1468891259.png?width=750)

  * Copy these two addresses to the **esl** ACL.

    * Make sure to do this process for both the Voice connector and dialer.

  * Click the **Save** button and go to the **SIP Status** with from the **Status** tab.


![](attachments/1468891146/1468891403.png?width=693)

  * Click the **Reload ACL** button on the top right.


![](attachments/1468891146/1468891250.png?width=658)

* * *

## CX Voice Recording Components

Follow the guide [here](CX-Voice-Recording-Components-Deployment-Guide_161842333.html) to deploy the recording link uploader and middleware components.
