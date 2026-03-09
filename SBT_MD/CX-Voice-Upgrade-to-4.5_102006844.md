# CX Knowledgebase : CX Voice Upgrade to 4.5

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

  3. Note the container ID of the current deployed 4.4 Voice connector.

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
             image: gitimages.expertflow.com/freeswitch/ecx_generic_connector:TAG
             container_name: unified-voice-connector
             ports:
               - PORT:8080
             env_file:
               - ./env.txt
             restart: always
[/code]

     1. Replace the **TAG** keyword with the required image tag obtained from the releases page [here](https://expertflow-docs.atlassian.net/wiki/spaces/CIMT/pages/1342256). 

     2. Replace the **PORT** keyword with the port noted above in step 4.

  9. Open the env.txt file.

     1. Remove the fields **CCM_API, SPRING_PORT, DB_DIALECT** and **DB_DRIVER** and add the following fields:

        1. **CX_FQDN** = The address of EF CX. <https://FQDN>

        2. **MIDDLEWARE_API** = Set at 1.1.1.1 and do not change.

        3. **LOG_LEVEL** = The amount of detail in the logs. Default is **INFO** , and for more detailed logs the value should be **DEBUG**.

  10. Run the command 
[code] docker compose up -d
[/code]

  11. Confirm that the docker container is running by using the command 
[code] docker ps
[/code]

![Untitled-20240207-065334.png](attachments/102006844/102334495.png?width=736)
  12. Confirm that the container is running correctly by opening the logs with command 
[code] docker logs -f containerID
[/code]

![Untitled-20240207-065355.png](attachments/102006844/102367257.png?width=736)



## Outbound Dialer

Follow the guide [here](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2529764).

## Media Server configuration

  1. Note the service identifier of the [CX Voice channel](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2529731) in Unified Admin.

  2. SSH onto the Debian server on which the Voice connector is installed.

     1. Use command 
[code] ssh <username>@<server-ip>
[/code]

     2. Enter user password and press **ENTER**.

     3. Use command 
[code] su
[/code]

     4. Enter root password and press **ENTER**.

  3. Run the command 
[code] rm -r /usr/share/freeswitch/sounds/ivr_prompts
[/code]

  4. Navigate to the folder**/usr/share/freeswitch/scripts**.

  5. Delete the file **cx_env{DN}.lua** where**{DN}** is the service identifier noted in step 1.

  6. Login to Media Server web interface. 

     * Open in browser: [**https://IP-addr**](https://IP-addr), where **IP-addr** is the IP address of the Media Server.

![image2024-1-29_18-39-3-20240207-070032.png](attachments/102006844/101908601.png?width=450)

     * Add the **username** and **password** that was shown upon [installation of ](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/1344451)Media Server and press **LOGIN**.

  7. Press the IP address in the top right and select the Domain that was c[reated during 4.4 Voice configuration](https://expertflow-docs.atlassian.net/wiki/spaces/CIMT/pages/1341516).

  8. Open the Dialplan Manager section under the Dialplan tab.   


![](attachments/102006844/102203494?width=400)

  9. Locate the **CxIvr** dialplan whose **destination_number** matches the **service identifier** noted in step 1.

  10. Delete this dialplan.

  11. Note the **STATIC_QUEUE_TRANSFER_DN** field in the [Agent Desk config-map](https://expertflow-docs.atlassian.net/wiki/x/moVa):

     1. SSH into the EFCX server by using the command **ssh username@IP-addr**

     2. Where username is the EFCX SSH username and IP-addr is the EFCX server IP address

     3. Run the command **vi cim-solution/kubernetes/cim/ConfigMaps/ef-unified-agent-configmap.yaml**

     4. Scroll down to find the **STATIC_QUEUE_TRANSFER_DN** field and note down its value.

  12. On **Media Server** in the dialplan section, locate the **CxQueue** dialplan whose destination_number field contains the value **^NUMBER[-0-9a-zA-Z]*$** where **NUMBER** is the **STATIC_QUEUE_TRANSFER_DN** noted in the previous step.

  13. Delete this dialplan.

  14. Locate the **local_extension** dialplan.

  15. Locate the following information in the dialplan and delete it (check the **Delete** column checkbox for each row and press **SAVE** in the top right):




action| set | sip_h_X-CALL-VARIABLE0=${uuid}| 0| 25| true  
---|---|---|---|---|---  
action| set | sip_rh_X-CALL-VARIABLE0=${uuid}| 0| 35| true  
action| set | sip_h_X-CALL-ID=${sip_call_id}| 0| 45| true  
action| lua| vcApi${sip_h_X-Destination-Number}.lua 'rona'| 1| 76| true  
  
  16. Follow the new Media Server configuration guide [here](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/75825154).



