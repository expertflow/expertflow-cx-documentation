# CX Knowledgebase : CX Voice Upgrade to 4.5.3

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

  3. Note the container ID of the current deployed 4.5.2 Voice connector.

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
             image: gitimages.expertflow.com/freeswitch/ecx_generic_connector:4.5.3
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

![Untitled-20240207-065334.png](attachments/554827778/554827794.png?width=736)
  12. Confirm that the container is running correctly by opening the logs with command 
[code] docker logs -f containerID
[/code]

![Untitled-20240207-065355.png](attachments/554827778/554827791.png?width=736)



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



