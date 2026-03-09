# CX Knowledgebase : CX Voice Upgrade to 4.5.2

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
             image: gitimages.expertflow.com/freeswitch/ecx_generic_connector:4.5.2
             container_name: unified-voice-connector
             ports:
               - PORT:8080
             env_file:
               - ./env.txt
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

![Untitled-20240207-065334.png](attachments/412549122/412549149.png?width=736)
  13. Confirm that the container is running correctly by opening the logs with command 
[code] docker logs -f containerID
[/code]

![Untitled-20240207-065355.png](attachments/412549122/412549146.png?width=736)



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
[code] git clone -b 4.5.2 https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/freeswitch-scripts.git
[/code]

  4. Navigate to the cloned repository to access the files:
[code] cd freeswitch-scripts
[/code]

  5. Move scripts to the **Media Server** scripts folder:
[code] mv *.lua /usr/share/freeswitch/scripts
[/code]

  6. Run the following command:
[code] chmod -R 777 /usr/share/freeswitch/scripts
[/code]




![](images/icons/grey_arrow_down.png)Silent Monitoring Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/412549122/474251678.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain being used::


![](attachments/412549122/474251684.png?width=676)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/412549122/474251690.png?width=686)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/412549122/474251696.png?width=696)

  * Fill the form with following details :

    * Name = Silent Monitoring

    * Condition 1 = Select **destination_number** from list and add **^\\*44(\d{2,15})$**

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
  
![image-20240702-060719.png](attachments/412549122/474251702.png?width=600)

  * Set the **Context** field to the value of the **Domain** being used..

  * Set the **Domain** field to the value of the **Domain** being used..

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Conference Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/412549122/474251678.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain being used.:


![](attachments/412549122/474251684.png?width=693)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/412549122/474251690.png?width=686)

  * Add a new Dialplan by pressing the **Add** Button on the top.


![](attachments/412549122/474251696.png?width=676)

  * Fill the form with following details :

    * Name = CustomConf

    * Condition 1 = Select **destination_number** from list and add **^custom_conf_(.*)$**

    * Action 1 = Select first item from the list 

  * Save the form by pressing save button on top right Corner.

  * Re-open CustomConf dialplan.

  * Delete the line with the **Action** tag (Click the **checkbox** in the right and press **SAVE** in the top right)

  * Add the following information to this dialplan:




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| answer| | 0| 10| true  
action| set| session_in_hangup_hook=true| 0| 15| true  
action| export| session_in_hangup_hook=true| 0| 20| true  
action| set| api_hangup_hook=lua cx_hangup.lua $1| 0| 25| true  
action| export| api_hangup_hook=lua cx_hangup.lua $1| 0| 30| true  
action| conference| $1| 0| 35| true  
  
![image-20240702-061432.png](attachments/412549122/474251764.png?width=600)

  * Set the **Context** field to the value of the **Domain** being used..

  * Set the **Domain** field to the value of the **Domain** being used..

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in User Exists Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/412549122/474251770.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain being used.:


![](attachments/412549122/474251776.png?width=670)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/412549122/474251690.png?width=640)

  * Find and open the **user_exists** dialplan.

  * Add the following information(to add custom values in the **Type** column, select a random value then click on it to edit):




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
condition| ${sip_h_X-CallType}| ^CONSULT$| 3| 5| true  
action| bind_meta_app| A a s1 lua::consult_conf.lua CONSULT_TRANSFER| 3| 10| true  
action| bind_meta_app| C a s1 lua::consult_conf.lua CONSULT_CONFERENCE| 3| 15| true  
  
  * The result will look like this:


![image-20240702-062405.png](attachments/412549122/412155924.png?width=600)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in conference profile

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/412549122/474251770.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain being used.:


![](attachments/412549122/474251776.png?width=776)

  * Open the **Conference Profiles** section under the **Applications** tab:


![image-20240822-053906.png](attachments/412549122/475168862.png?width=776)

  * Open the profile named **default** :


![image-20240822-054148.png](attachments/412549122/475168868.png?width=776)

  * Under the **Profile Parameters** , find the following keywords under the **Name** column and click the checkbox:


![image-20240822-054759.png](attachments/412549122/475168874.png?width=776)

  * Press **TOGGLE** in the top right and choose **CONTINUE** in the prompt shown.


![image-20240822-055012.png](attachments/412549122/475168880.png?width=776)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in SIP Profile

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/412549122/475103269.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain being used.:


![](attachments/412549122/475103275.png?width=654)

  * Open **SIP Profiles** under the **Advanced** tab.


![image-20240424-103707.png](attachments/412549122/475103281.png?width=640)

  * Open the **internal** profile, scroll down to the **ws-binding** and **wss-binding** fields, and set their **Enabled** column values to **True**.


![image-20240503-121016.png](attachments/412549122/475103287.png?width=630)

  * Find the **liberal-dtmf** fields and its **Value** and **Enabled** columns to **true**.

  * At the bottom add the data:




**Name**| **Value**| **Enabled**  
---|---|---  
apply-candidate-acl| 0.0.0.0/0| True  
  
  * Press the **SAVE** button on the top right.

  * Open **SIP Status** under the **Status** tab.

  * Locate the line **sofia status profile internal** and to its right press the **RESCAN** button, followed by the **RESTART** button after the page reloads.


![image-20240503-121411.png](attachments/412549122/475103293.png?width=686)
