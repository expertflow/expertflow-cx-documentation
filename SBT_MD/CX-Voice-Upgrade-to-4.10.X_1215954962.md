# CX Knowledgebase : CX Voice Upgrade to 4.10.X

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

  3. Open the **docker-compose.yml** file and replace the image tag with 4.10.X or 5.X.

  4. Save and close the file.

  5. Open the **env.txt** file and add the following variables.

     1. 
[code]AUTH_ENABLED=true
            API_USERNAME=voice_auth
            API_PASS=pass
            CLIENT_ID=cim
            CLIENT_SECRET=secret
[/code]

  6. Set the above variables as described:

     1. AUTH_ENABLED: **true** or **false** depending on whether APISIX authentication is enabled in EFCX. The four settings below are set if this value is **true**.

     2. API_USERNAME: The username created in Keycloak for API authentication. 

        * On Keycloak create a user in the Expertflow realm.

        * Assign the **admin** and **default** roles, and have **Email-Verified** option enabled.

        * Assign a non-temporary password to this user as well.

     3. API_PASS: The password for the above user created in Keycloak for API authentication

     4. CLIENT_ID: Should always be **cim**.

     5. CLIENT_SECRET: Found on Keycloak in the **cim** client.

  7. Run the command 
[code] docker compose up -d
[/code]

  8. Confirm that the docker container is running by using the command 
[code] docker ps
[/code]

  9. Confirm that the container is running correctly by opening the logs with command 
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
[code] git clone -b 4.10.X https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/freeswitch-scripts.git
[/code]

  4. Navigate to the cloned repository to access the files:
[code] cd freeswitch-scripts
[/code]

  5. Move the updated scripts and prompts to their respective folders:
[code] mv cxIvr.lua cx_hangup.lua hangup_event.lua outboundIvr.lua vcApi.lua pcs.lua /usr/share/freeswitch/scripts/
         chmod -R 777 /usr/share/freeswitch/scripts/
[/code]

  6. Open the cx_env.lua file for your DNs e.g. for DN 1122 open cx_env.lua.

  7. Add the following text under the line with **config = {**

     1. 
[code]auth_enabled = true
            auth_realm = "expertflow",
            client_secret = "1234",
            client_id = "cim",
            username = "voice_auth",
            password = "1234",
[/code]

  8. Set the above variables as described:

     1. auth_enabled: **true** or **false** depending on whether APISIX authentication is enabled in EFCX. The four settings below are set if this value is **true**.

     2. auth_realm: Keep at **expertflow**.

     3. username: Same as API_USERNAME in voice connector.

     4. password: Same as API_PASS in voice connector.

     5. client_id: Should always be **cim**.

     6. client_secret: Same as CLIENT_SECRET in voice connector.




## Link Uploader

![](images/icons/grey_arrow_down.png)Link Uploader

  1. SSH onto the Debian server on which the Link Uploader is installed.

     1. Use command 
[code] ssh <username>@<server-ip>
[/code]

     2. Enter user password and press **ENTER**.

     3. Use command 
[code] su
[/code]

     4. Enter root password and press **ENTER**.

  2. Navigate to the folder where the **docker-compose.yml** and **env.txt** files are located for the link uploader.

  3. Open the **docker-compose.yml** file and replace the image tag with 4.10.X.

  4. Save and close the file.

  5. Open the **env.txt** file and add the following variables.

     1. 
[code]AUTH_ENABLED=true
            API_USERNAME=voice_auth
            API_PASS=pass
            CLIENT_ID=cim
            CLIENT_SECRET=secret
[/code]

  6. Set the above variables as described:

     1. AUTH_ENABLED: **true** or **false** depending on whether APISIX authentication is enabled in EFCX. The four settings below are set if this value is **true**.

     2. API_USERNAME: Same as API_USERNAME in voice connector.

     3. API_PASS: Same as API_PASS in voice connector.

     4. CLIENT_ID: Should always be **cim**.

     5. CLIENT_SECRET: Same as CLIENT_SECRET in voice connector.

  7. Run the command 
[code] docker compose up --no-start
[/code]



