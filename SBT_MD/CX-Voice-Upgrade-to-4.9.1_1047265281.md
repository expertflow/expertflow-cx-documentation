# CX Knowledgebase : CX Voice Upgrade to 4.9.1

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

  3. Open the **docker-compose.yml** file and replace the image tag with 4.9.1.

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
[code] git clone -b 4.9.1 https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/freeswitch-scripts.git
[/code]

  4. Navigate to the cloned repository to access the files:
[code] cd freeswitch-scripts
[/code]

  5. Move the updated scripts and prompts to their respective folders:
[code] mv consult_conf.lua cx_hangup.lua set_recording_name.lua /usr/share/freeswitch/scripts/
         chmod -R 777 /usr/share/freeswitch/scripts/
[/code]




![](images/icons/grey_arrow_down.png)Changes in Conference Dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/1047265281/1047265306.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/1047265281/1047265303.png?width=693)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/1047265281/1047265300.png?width=686)

  * Open the **CustomConf** dialplan.

  * Modify the last line to:




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| conference| $1| 0| 35| true  
  
![image-20250425-113715.png](attachments/1047265281/1046610009.png?width=1083)

  * Save the changes by pressing **SAVE** button in top right corner.



