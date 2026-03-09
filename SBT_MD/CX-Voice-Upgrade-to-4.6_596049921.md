# CX Knowledgebase : CX Voice Upgrade to 4.6

## Voice Connector

![](images/icons/grey_arrow_down.png)Voice connector upgrade

  1. SSH onto the Debian server on which the Voice connector is installed.

     1. Use command 
[code] ssh <username>@<server-ip>
[/code]

     2. Enter user password and press **ENTER**.

     3. Use command 
[code] su
[/code]

     4. Enter root password and press **ENTER**.

  2. Navigate to the folder where the **docker-compose.yml** and **env.txt** files are located for the voice connector.

  3. Open the **docker-compose.yml** file and replace the image tag with 4.6:
[code] version: "3.8"
         services:
           voice-connector:
             image: gitimages.expertflow.com/freeswitch/ecx_generic_connector:4.6
             container_name: unified-voice-connector
             ports:
               - PORT:8080
             env_file:
               - ./env.txt
             restart: always
[/code]

  4. Run the command 
[code] docker compose up -d
[/code]

  5. Confirm that the docker container is running by using the command 
[code] docker ps
[/code]

  6. Confirm that the container is running correctly by opening the logs with command 
[code] docker logs -f containerID
[/code]




## VRS

![](images/icons/grey_arrow_down.png)Voice Recording Solution upgrade

  1. SSH onto the Debian server on which the Voice connector is installed.

     1. Use command 
[code] ssh <username>@<server-ip>
[/code]

     2. Enter user password and press **ENTER**.

     3. Use command 
[code] su
[/code]

     4. Enter root password and press **ENTER**.

  2. Navigate to the VRS deployment files.

  3. Find the file **docker-compose-efcx.yml** under **recording-solution/docker**

  4. Under the line containing **vrs-apis:** , find the line with **image:**

     1. Change the field value to [gitimages.expertflow.com/voice-recording-solution/apis:](http://gitlab.expertflow.com:9242/voice-recording-solution/apis:14.3_f-CCC-1096-SR1)14.3.1

  5. While in the **recording-solution** folder run:
[code] docker compose -f docker/docker-compose-efcx.yml down
         docker compose -f docker/docker-compose-efcx.yml up -d
[/code]




## Media Server configuration

![](images/icons/grey_arrow_down.png)Scripts

  1. SSH onto the Debian server on which the Voice connector is installed.

     1. Use command 
[code] ssh <username>@<server-ip>
[/code]

     2. Enter user password and press **ENTER**.

     3. Use command 
[code] su
[/code]

     4. Enter root password and press **ENTER**.

  2. [Confirm ](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html#confirm-git-is-installed)**git** is installed, and [install it](https://docs.gitlab.com/ee/topics/git/how_to_install_git/index.html) if is not.

  3. Clone the Media Server scripts repository: 
[code] rm -r freeswitch-scripts
         git clone -b 4.6 https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/freeswitch-scripts.git
[/code]

  4. Navigate to the cloned repository to access the files:
[code] cd freeswitch-scripts
[/code]

  5. Move scripts to the **Media Server** scripts folder:
[code] mv cx_hangup.lua consult_conf.lua set_recording_name.lua /usr/share/freeswitch/scripts
[/code]

  6. Run the following command:
[code] chmod -R 777 /usr/share/freeswitch/scripts
[/code]




![](images/icons/grey_arrow_down.png)Manual Outbound Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/596049921/596049941.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/596049921/596049944.png?width=676)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/596049921/596049962.png?width=686)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/596049921/596049947.png?width=696)

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
condition| ${sip_h_X-CallType}| ^OUT$| on-false| | | 5| true  
condition| ${customer_leg_uuid}| ^$| never| | | 10| true  
action| set| custom_origination_uuid=${create_uuid()}| | true| 0| 15| true  
action| export| customer_leg_uuid=${custom_origination_uuid}| | true| 0| 20| true  
action| set| customer_leg_uuid=${custom_origination_uuid}| | true| 0| 25| true  
anti-action| set| custom_origination_uuid=${create_uuid()}| | | | 30| true  
  
![image-20241015-140734.png](attachments/596049921/595198046.png?width=750)

  * Set the **Context** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Domain** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Order** field to **49**.

  * Set the **Continue** field to **True**.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in Local extension Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/596049921/596049971.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/596049921/596049974.png?width=670)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/596049921/596049962.png?width=640)

  * Find and open the **local_extension** dialplan.

  * Add the following information to the last group:




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| ring_ready| true| 1| 74| true  
  
  * Secondly, replace the **Data** field in the line with **Order 75** with: **{origination_uuid=${custom_origination_uuid}}user/${destination_number}@${domain_name}**

  * The result will look like this:


![image-20241023-080154.png](attachments/596049921/614760563.png?width=750)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in Call Recording Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/596049921/596049971.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/596049921/596049974.png?width=776)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/596049921/596049962.png?width=726)

  * Find and open the **user_record** dialplan.

  * Add the following data to the table, such that the final version looks like the image below: 




**Tag**| **Type**| **Data**| **Inline**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---|---  
action| set| record_path=${recordings_dir}/${domain_name}/archive/${strftime(%Y)}/${strftime(%b)}/${strftime(%d)}| true| 9| 10| true  
action| export| record_path=${recordings_dir}/${domain_name}/archive/${strftime(%Y)}/${strftime(%b)}/${strftime(%d)}| true| 9| 15| true  
action| set| record_name=${uuid}.${record_ext}| true| 9| 20| true  
action| mkdir| ${record_path}| | 9| 25| true  
action| set| recording_follow_transfer=false| true| 9| 30| true  
action| export| recording_follow_transfer=false| true| 9| 35| true  
action| set| record_append=false| true| 9| 40| true  
action| set| record_in_progress=true| true| 9| 45| true  
action| set| RECORD_ANSWER_REQ=true| | 9| 50| true  
action| lua| set_recording_name.lua| | 9| 55| true  
action| export| ${recording_command}| | 9| 60| true  
  
![image-20241016-060412.png](attachments/596049921/596541476.png?width=750)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Configuring route For Outbound calls

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/596049921/596049989.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/596049921/596049992.png?width=658)

  * Open the **Outbound Routes** section under the **Dialplans** tab.


![](attachments/596049921/596606998.png?width=658)

  * Press the **ADD** button in the top right.


![](attachments/596049921/596607004.png?width=658)

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


![image-20241023-080613.png](attachments/596049921/614760681.png?width=750)

![](images/icons/grey_arrow_down.png)Change in Silent Monitoring Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/596049921/596049941.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/596049921/596049944.png?width=676)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/596049921/596049962.png?width=686)

  * Find and open the **Silent_Monitoring** dialplan.



  * Edit the **Data** column of the first row to have the value **^\\*44(.+)$**


![image-20241106-132733.png](attachments/596049921/656474140.png?width=750)
