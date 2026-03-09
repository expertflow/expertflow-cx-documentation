# CX Knowledgebase : CX Voice Upgrade to 4.5.1

## Voice Connector

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

  3. Note the container ID of the current deployed 4.5 Voice connector.

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
             image: gitimages.expertflow.com/freeswitch/ecx_generic_connector:4.5.1
             container_name: unified-voice-connector
             ports:
               - PORT:8080
             env_file:
               - ./env.txt
             restart: always
[/code]

  9. Replace the **PORT** keyword with the port noted above in step 4.

  10. Run the command 
[code] docker compose up -d
[/code]

  11. Confirm that the docker container is running by using the command 
[code] docker ps
[/code]

![Untitled-20240207-065334.png](attachments/428802049/428802064.png?width=736)
  12. Confirm that the container is running correctly by opening the logs with command 
[code] docker logs -f containerID
[/code]

![Untitled-20240207-065355.png](attachments/428802049/428802067.png?width=736)



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
[code] git clone -b 4.5.1 https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/freeswitch-scripts.git
[/code]

  4. Navigate to the cloned repository to access the files:
[code] cd freeswitch-scripts
[/code]

  5. Move **hangup_event.lua** to the **Media Server** scripts folder:
[code] mv hangup_event.lua /usr/share/freeswitch/scripts/
         chmod -R 777 /usr/share/freeswitch/scripts/
[/code]

  6. Move **no-agent-available.wav** to the **Media Server** prompts folder:
[code] mv ivr_prompts/no_agent_available.wav /usr/share/freeswitch/sounds/ivr_prompts/
[/code]




![](images/icons/grey_arrow_down.png)Changes in SIP Profile

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/428802049/475201671.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/428802049/475201677.png?width=654)

  * Open **SIP Profiles** under the **Advanced** tab.


![image-20240424-103707.png](attachments/428802049/475201683.png?width=640)

  * Open the **internal** profile, scroll down to the **ws-binding** and **wss-binding** fields, and set their **Enabled** column values to **True**.


![image-20240503-121016.png](attachments/428802049/475201689.png?width=630)

  * Find the **disable-transcoding** field and its **Value** and **Enabled** columns to **true**.

  * Fine the **nat-options-ping** fields and its **Value** and **Enabled** columns to **true**.

  * Press the **SAVE** button on the top right.

  * Open **SIP Status** under the **Status** tab.

  * Locate the line **sofia status profile internal** and to its right press the **RESCAN** button, followed by the **RESTART** button after the page reloads.


![image-20240503-121411.png](attachments/428802049/475201695.png?width=686)

![](images/icons/grey_arrow_down.png)Changes in Media Server Config

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
[/code]

  * Run the command: 



[code] 
    systemctl restart freeswitch
[/code]
