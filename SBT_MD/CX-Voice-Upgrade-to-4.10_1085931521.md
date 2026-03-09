# CX Knowledgebase : CX Voice Upgrade to 4.10

## CX Voice Recording Components  
  
Follow the guide [here](CX-Voice-Recording-Components-Deployment-Guide_161842333.html) to deploy the recording link uploader and middleware components.

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

  2. Navigate to the folder where the **docker-compose.yml** and **env.txt** files are located for the voice connector.

  3. Open the **docker-compose.yml** file and replace the image tag with 4.10.

  4. Save and close the file.

  5. Run the command 
[code] docker compose up -d
[/code]

  6. Confirm that the docker container is running by using the command 
[code] docker ps
[/code]

  7. Confirm that the container is running correctly by opening the logs with command 
[code] docker logs -f containerID
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
[code] git clone -b 4.10 https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/freeswitch-scripts.git
[/code]

  4. Navigate to the cloned repository to access the files:
[code] cd freeswitch-scripts
[/code]

  5. Move the updated scripts and prompts to their respective folders:
[code] mv consult_conf.lua barge.lua channel_* cx_hangup.lua /usr/share/freeswitch/scripts/
         chmod -R 777 /usr/share/freeswitch/scripts/
[/code]




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




![](images/icons/grey_arrow_down.png)Add recording event hooks

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
[code] <hook event="CHANNEL_BRIDGE" subclass="" script="channel_bridge.lua"/>
        <hook event="CHANNEL_UNBRIDGE" subclass="" script="channel_unbridge.lua"/>
        <hook event="CHANNEL_CALLSTATE" subclass="" script="channel_state.lua"/>
[/code]

  * Save the file.

  * Run the command: 



[code] 
    systemctl restart freeswitch
[/code]
