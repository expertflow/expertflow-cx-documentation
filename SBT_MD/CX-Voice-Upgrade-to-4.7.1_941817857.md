# CX Knowledgebase : CX Voice Upgrade to 4.7.1

## Outbound Dialer

![](images/icons/grey_arrow_down.png)Outbound Dialer

  1. SSH onto the Debian server on which the Outbound Dialer is installed.

     1. Use command 
[code] ssh <username>@<server-ip>
[/code]

     2. Enter user password and press **ENTER**.

     3. Use command 
[code] su
[/code]

     4. Enter root password and press **ENTER**.

  2. Navigate to the folder where the **docker-compose.yml** and **env.txt** files are located for the dialer.

  3. Open the **docker-compose.yml** file and replace image tag with **4.7.1**.

  4. Run the command 
[code] docker compose up -d
[/code]

  5. Confirm that the docker container is running by using the command 
[code] docker ps
[/code]

  6. Confirm that the container is running correctly by opening the logs with command 
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
[code] git clone -b 4.7.1 https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/freeswitch-scripts.git
[/code]

  4. Navigate to the cloned repository to access the files:
[code] cd freeswitch-scripts
[/code]

  5. Move the updated scripts and prompts to their respective folders:
[code] mv outboundIvr.lua /usr/share/freeswitch/scripts/
         chmod -R 777 /usr/share/freeswitch/scripts/
         mv ivr_prompts/outbound_prompt.wav /usr/share/freeswitch/sounds/ivr_prompts/
[/code]




![](images/icons/grey_arrow_down.png)Outbound IVR Dialplan

  * This section is optional, depending on whether the CX Dialer for Campaigns is in use.

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/941817857/941523061.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/941817857/941523068.png?width=610)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/941817857/941817885.png?width=658)

  * Add a new Dialplan by pressing the Add Button on the top.


![](attachments/941817857/941817882.png?width=658)

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



  * Set the **Context** field to the value of the **Domain** set in the **Domain creation** section.

  * Set the **Domain** field to the value of the **Domain** set in the **Domain creation** section.

  * Save the changes by pressing **SAVE** button in top right corner.




![](images/icons/grey_arrow_down.png)Changes in Global Variables dialplan

  * Login to Media Server web interface. 

    * Open in browser: <https://IP-addr>, where IP-addr is the IP address of the Media Server.


![](attachments/941817857/960299193.png?width=500)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the Domain creation section above:


![](attachments/941817857/960299199.png?width=665)

  * Open the Dialplan Manager section under the Dialplan tab. 


![](attachments/941817857/941817885.png?width=686)

  * Find and open the **global-variables** dialplan.

  * Add the following information to this dialplan (to add custom values in the **Type** column, select a random value then click on it to edit):




**Tag**| **Type**| **Data**| **Group**| **Order**| **Enabled**  
---|---|---|---|---|---  
action| set| FreeSWITCH-IPv4=${domain_name}| 0| 20| true  
  
  * The result will look like:


![image-20250312-100316.png](attachments/941817857/960299219.png?width=700)

  * Save the changes by pressing **SAVE** button in top right corner.



