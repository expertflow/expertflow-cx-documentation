# CX Knowledgebase : CX Voice Upgrade to 4.7

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

  3. Note the container ID of the current deployed 4.6 Voice connector.

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
             image: gitimages.expertflow.com/freeswitch/ecx_generic_connector:4.7
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

  10. Run the command 
[code] docker compose up -d
[/code]

  11. Confirm that the docker container is running by using the command 
[code] docker ps
[/code]

![Untitled-20240207-065334.png](attachments/721944577/721944614.png?width=736)
  12. Confirm that the container is running correctly by opening the logs with command 
[code] docker logs -f containerID
[/code]

![Untitled-20240207-065355.png](attachments/721944577/721944611.png?width=736)



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
[code] git clone -b 4.7 https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/freeswitch-scripts.git
[/code]

  4. Navigate to the cloned repository to access the files:
[code] cd freeswitch-scripts
[/code]

  5. Move **set_recording_name.lua** , **cx_hangup.lua** and **vcApi.lua** to the **Media Server** scripts folder:
[code] mv consult_conf.lua set_recording_name.lua cx_hangup.lua vcApi.lua /usr/share/freeswitch/scripts/
         chmod -R 777 /usr/share/freeswitch/scripts/
[/code]

  6. Edit the configuration scripts of your specific **DNs** i.e. for a **DN** of **1555** the configuration script will be named **cx_env1555.lua**.
[code] vi /usr/share/freeswitch/scripts/cx_env1555.lua
[/code]

  7. Edit the value of the field **voiceConnectorApi** such that it matches the format: **“http://VC-IP:VC-PORT”** i.e. for a Voice Connector deployed on server **192.168.1.120** , using the docker container port **8115** , the value of **voiceConnectorApi** will be **"http://192.168.1.120:8115"**.

  8. Save the file.




![](images/icons/grey_arrow_down.png)Changes in conference profile

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/721944577/722108421.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain being used.:


![](attachments/721944577/722108428.png?width=776)

  * Open the **Conference Profiles** section under the **Applications** tab:


![image-20240822-053906.png](attachments/721944577/722108434.png?width=776)

  * Open the profile named **default** :


![image-20240822-054148.png](attachments/721944577/722108440.png?width=776)

  * Under the **Profile Parameters** , find the **caller-controls** keyword under the **Name** column and click the checkbox:


![image-20241203-072119.png](attachments/721944577/722010123.png?width=776)

  * Press **TOGGLE** in the top right and choose **CONTINUE** in the prompt shown.


![image-20241203-072152.png](attachments/721944577/721781127.png?width=776)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in Call Recording Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/721944577/722108421.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/721944577/722108428.png?width=776)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/721944577/745439262.png?width=726)

  * Find and open the **user_record** dialplan.

  * Add the following data to the table(ignore any data already added), such that the final version looks like the image below: 




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
  
![image-20250127-071327.png](attachments/721944577/834666724.png?width=750)

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in conference Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/721944577/772964753.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/721944577/772964759.png?width=693)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/721944577/745439262.png?width=686)

  * Find and open the **CustomConf** dialplan.

  * Add the following information to this dialplan:




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| set| absolute_codec_string=G7221@32000h,G7221@16000h,G722,PCMU,PCMA| 0| 31| true  
action| export| absolute_codec_string=G7221@32000h,G7221@16000h,G722,PCMU,PCMA| 0| 32| true  
  
![image-20250101-060339.png](attachments/721944577/772964785.png?width=650)

  * Save the changes by pressing **SAVE** button in top right corner.



