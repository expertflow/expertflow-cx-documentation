# CX Knowledgebase : PTCL CX Voice Upgrade 4.5.1 to 4.9.1

## Voice Connector

![](images/icons/grey_arrow_down.png)Voice Connector

  1. SSH onto the Debian server on which the Voice connector is installed.

     1. Use command 
[code] ssh <username>@<server-ip>
[/code]

     2. Enter user password and press **ENTER**.

     3. Use command 
[code] su
[/code]

     4. Enter root password and press **ENTER**.

  2. Run the command __ to see the list of running containers
[code] docker ps
[/code]

  3. Note the container ID of the current deployed 4.5.1 Voice connector.

  4. Note the port of that container i.e. for **0.0.0.0:8116- >8080/tcp, :::8116->8080/tcp**, the port of the container is **8116**.

  5. Run the command to stop the container
[code] docker stop <container-ID>
[/code]

  6. Run the command to remove the container
[code] docker rm <container-ID>
[/code]

  7. Navigate to the folder where the **docker-compose.yml** and **env.txt** files are located for the voice connector.

  8. Open the **docker-compose.yml** file and replace the text inside with text below:
[code] version: "3.8"
         services:
           voice-connector:
             image: gitimages.expertflow.com/freeswitch/ecx_generic_connector:4.9.1
             deploy:
               resources:
                 limits:
                   memory: 1024m
                 reservations:
                   memory: 256m
             container_name: unified-voice-connector
             ports:
               - PORT:8080
             env_file:
               - ./env.txt
             command: ["java", "-Xms256m", "-Xmx1024m", "-XX:+UseG1GC", "-XX:MinHeapFreeRatio=10", "-XX:MaxHeapFreeRatio=30", "-jar", "/app/ecx_generic_connector.jar"]
             restart: always
[/code]

  9. Replace the **PORT** keyword with the port noted above in step 4.

  10. Open the env.txt file and remove the fields **MIDDLEWARE_API, DB_NAME, DB_URL, DB_PORT, DB_USERNAME, DB_PASS, DB_CONN_TIMEOUT** and **DB_DRIVER**.

  11. Run the command 
[code] docker compose up -d
[/code]

  12. Confirm that the docker container is running by using the command 
[code] docker ps
[/code]

![Untitled-20240207-065334.png](attachments/1203830785/1203830831.png?width=736)
  13. Confirm that the container is running correctly by opening the logs with command 
[code] docker logs -f containerID
[/code]

![Untitled-20240207-065355.png](attachments/1203830785/1203830828.png?width=736)



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

     1. Change the field value to [gitimages.expertflow.com/voice-recording-solution/apis:](http://gitlab.expertflow.com:9242/voice-recording-solution/apis:14.3_f-CCC-1096-SR1)14.3.2.1

  5. While in the **recording-solution** folder run:
[code] docker compose -f docker/docker-compose-efcx.yml down
         docker compose -f docker/docker-compose-efcx.yml up -d
[/code]




## Add Indexing in Media Server Database

  * While on the Media Server, run the following command and note the output password:
[code] cat /etc/fusionpbx/config.conf | grep database.0.password
[/code]

  * Run the following command and enter the password noted before:
[code] psql -h 127.0.0.1 -p 5432 -U fusionpbx -d fusionpbx
[/code]

  * Run the following command:
[code] CREATE INDEX idx_mykey ON v_xml_cdr USING GIN (json) WHERE json->'variables' ? 'sip_h_X-CALL-ID';
[/code]

    * **Note:** If the number of calls on the system is too high, then the query will take a long time to execute.




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
[code] git clone -b 4.9.1-ptcl https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/freeswitch-scripts.git
[/code]

  4. Navigate to the cloned repository to access the files:
[code] cd freeswitch-scripts
[/code]

  5. Move **set_recording_name.lua** , **cx_hangup.lua** and **vcApi.lua** to the **Media Server** scripts folder:
[code] mv *.lua /usr/share/freeswitch/scripts/
         chmod -R 777 /usr/share/freeswitch/scripts/
[/code]




![](images/icons/grey_arrow_down.png)Changes in Global Variables dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1203830785/1203273776.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1203830785/1203273782.png?width=665)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1203830785/1203830888.png?width=686)

  * Find and open the **global-variables** dialplan.

  * Add the following information to this dialplan (to add custom values in the **Type** column, select a random value then click on it to edit):




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| set| FreeSWITCH-IPv4=${domain_name}| 0| 20| true  
  
  * The result will look like:


![image-20250312-100316.png](attachments/1203830785/1202978899.png?width=700)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Manual Outbound Dialplan

  * Login to Media Server web interface. 

    * Open in browser: [https://IP-addr](https://ip-addr/), where IP-addr is the IP address of the Media Server.


![](attachments/1203830785/1203830882.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1203830785/1203830885.png?width=676)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1203830785/1203830888.png?width=686)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/1203830785/1203830891.png?width=696)

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
  
![image-20250722-101756.png](attachments/1203830785/1203339336.png?width=700)

  * Set the **Context** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Domain** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Order** field to **49**.

  * Set the **Continue** field to **True**.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in Local extension Dialplan

  * Login to Media Server web interface. 

    * Open in browser: [https://IP-addr](https://ip-addr/), where IP-addr is the IP address of the Media Server.


![](attachments/614170650/614170688.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/614170650/614170685.png?width=670)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1203830785/1203830888.png?width=640)

  * Find and open the **local_extension** dialplan.

  * Add the following information to the last group:




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| ring_ready| true| 1| 74| true  
  
  * Secondly, replace the **Data** field in the line with **Order 75** with: **{origination_uuid=${custom_origination_uuid}}user/${destination_number}@${domain_name}**

  * The result will look like this:


![image-20241023-080154.png](attachments/614170650/613056630.png?width=750)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Configuring route For Outbound calls

  * Login to Media Server web interface. 

    * Open in browser: [https://IP-addr](https://ip-addr/), where IP-addr is the IP address of the Media Server.


![](attachments/614170650/614170676.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/614170650/614170673.png?width=658)

  * Open the **Outbound Routes** section under the **Dialplans** tab.


![](attachments/614170650/614170670.png?width=658)

  * Press the **ADD** button in the top right.


![](attachments/614170650/614170667.png?width=658)

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


![image-20241023-080613.png](attachments/1203830785/1203568690.png?width=750)

![](images/icons/grey_arrow_down.png)Changes in SIP Profile

  * Login to Media Server web interface. 

    * Open in browser: [https://IP-addr](https://ip-addr/), where IP-addr is the IP address of the Media Server.


![](attachments/412549122/475103269.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain being used:


![](attachments/412549122/474251684.png?width=676)

  * Open **SIP Profiles** under the **Advanced** tab.


![image-20240424-103707.png](attachments/412549122/475103281.png?width=640)

  * Open the **newtest** profile, scroll down to the **ws-binding** and **wss-binding** fields, and set their **Enabled** column values to **True**.


![image-20240503-121016.png](attachments/412549122/475103287.png?width=630)

  * Find the **liberal-dtmf** fields and its **Value** and **Enabled** columns to **true**.

  * At the bottom add the data:




**Name**| **Value**| **Enabled**  
---|---|---  
apply-candidate-acl| 0.0.0.0/0| True  
  
  * Press the **SAVE** button on the top right.

  * Open **SIP Status** under the **Status** tab.

  * Locate the line **sofia status profile newtest** and to its right press the **RESCAN** button, followed by the **RESTART** button after the page reloads.




![](images/icons/grey_arrow_down.png)External Consult and Transfer Dialplan

  * Login to Media Server web interface. 

    * Open in browser: [https://IP-addr](https://ip-addr/), where IP-addr is the IP address of the Media Server.


![](attachments/75825154/87654405.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/75825154/87326743.png?width=716)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/75825154/87752729.png?width=716)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/75825154/75825274.png?width=722)

  * Fill the form with following details :

    * Name = External_Consult_and_Transfer

    * Condition 1 = Select **destination_number** from list and add a random number

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open the created dialplan.

  * Change the value of the **Data** column in the **destination_number** row to **^99887765[-0-9a-zA-Z]*$**

  * Change the value of the **Type** column in the **Action** row to **lua** and the **Data** field to **customTransfer.lua**


![image-20250313-085303.png](attachments/75825154/964296714.png?width=700)

  * Set the **Context** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Domain** field to the value of the **Domain** set in the **Domain creation** section.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Custom Hangup Dialplan

  * Login to Media Server web interface. 

    * Open in browser: [https://IP-addr](https://ip-addr/), where IP-addr is the IP address of the Media Server.


![](attachments/75825154/87654405.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/75825154/87326743.png?width=676)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/75825154/87752729.png?width=686)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/75825154/75825274.png?width=696)

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
  
![Screenshot 2025-02-25 141521.png](attachments/75825154/924549180.png?width=851)

  * Set the **Context** field to **global**.

  * Set the **Domain** field to **Global**.

  * Set the **Order** field to **999**.

  * Set the **Continue** field to **False**.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Silent Monitoring Dialplan

  * Login to Media Server web interface. 

    * Open in browser: [https://IP-addr](https://ip-addr/), where IP-addr is the IP address of the Media Server.


![](attachments/75825154/87654405.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/75825154/87326743.png?width=676)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/75825154/87752729.png?width=686)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/75825154/75825274.png?width=696)

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
  
![image-20241106-132815.png](attachments/75825154/654573942.png?width=750)

  * Set the **Context** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Domain** field to the value of the **Domain** set in the **Domain creation** section.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Conference Dialplan

  * Login to Media Server web interface. 

    * Open in browser: [https://IP-addr](https://ip-addr/), where IP-addr is the IP address of the Media Server.


![](attachments/75825154/87654405.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/75825154/87326743.png?width=693)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/75825154/87752729.png?width=686)

  * Add a new Dialplan by pressing the **Add** Button on the top.


![](attachments/75825154/75825274.png?width=676)

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
  
![image-20250425-113642.png](attachments/75825154/1046642807.png?width=1083)

  * Set the **Context** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Domain** field to the value of the **Domain** set in the **Domain creation** section.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in User Exists Dialplan

  * Login to Media Server web interface. 

    * Open in browser: [https://IP-addr](https://ip-addr/), where IP-addr is the IP address of the Media Server.


![](attachments/75825154/87490564.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/75825154/87654416.png?width=670)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/75825154/87752729.png?width=640)

  * Find and open the **user_exists** dialplan.

  * Add the following information(to add custom values in the **Type** column, select a random value then click on it to edit):




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
condition| ${sip_h_X-CallType}| ^CONSULT$| 3| 5| true  
action| bind_meta_app| A a s1 lua::consult_conf.lua CONSULT_TRANSFER| 3| 10| true  
action| bind_meta_app| C a s1 lua::consult_conf.lua CONSULT_CONFERENCE| 3| 15| true  
  
  * The result will look like this:


![image-20240702-062405.png](attachments/75825154/362741779.png?width=600)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in Call Recording Dialplan

  * Login to Media Server web interface. 

    * Open in browser: [https://IP-addr](https://ip-addr/), where IP-addr is the IP address of the Media Server.


![](attachments/75825154/87490564.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/75825154/87654416.png?width=776)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/75825154/87752729.png?width=726)

  * Find and open the **user_record** dialplan.

  * Make sure to **delete the lines present previously in** **Group 9** , and NOT in the table and image below.

  * Add the following data to the table, such that the final version of**Group 9** looks like the image below: 




**Tag**| **Type**| **Data**| **Inline**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---|---  
action| set| record_path=${recordings_dir}/${domain_name}/archive/${strftime(%Y)}/${strftime(%b)}/${strftime(%d)}| true| 9| 10| true  
action| export| record_path=${recordings_dir}/${domain_name}/archive/${strftime(%Y)}/${strftime(%b)}/${strftime(%d)}| true| 9| 15| true  
action| set| record_name=${uuid}.${record_ext}| true| 9| 20| true  
action| mkdir| ${record_path}| -| 9| 25| true  
action| set| recording_follow_transfer=false| true| 9| 30| true  
action| export| recording_follow_transfer=false| true| 9| 35| true  
action| set| record_append=false| true| 9| 40| true  
action| set| record_in_progress=true| true| 9| 45| true  
action| set| RECORD_ANSWER_REQ=true| -| 9| 50| true  
action| lua| set_recording_name.lua| -| 9| 55| true  
action| export| ${recording_command}| -| 9| 60| true  
action| export| recording_filename=${recording_filename}| -| 9| 65| true  
  
![Untitled-20250219-101017.png](attachments/75825154/907673783.png?width=800)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in conference profile

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1203830785/1203830855.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1203830785/1203830858.png?width=776)

  * Open the **Conference Profiles** section under the **Applications** tab:


![image-20240822-053906.png](attachments/1203830785/1203830837.png?width=776)

  * Open the profile named **default** :


![image-20240822-054148.png](attachments/1203830785/1203830840.png?width=776)

  * Under the **Profile Parameters** , find the following keywords under the **Name** column and click the checkbox:


![image-20241129-135352.png](attachments/1203830785/1203077256.png?width=770)

  * Press **TOGGLE** in the top right and choose **CONTINUE** in the prompt shown.


![image-20241129-135211.png](attachments/1203830785/1203077262.png?width=770)

  * Save the changes by pressing **SAVE** button in top right corner.



