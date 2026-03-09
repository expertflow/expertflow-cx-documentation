# CX Knowledgebase : Voice Connector Deployment Guide

## Prerequisites

### Software Requirements

Item| Recommended| Installation guide  
---|---|---  
Operating System| Debian 12|  -  
Docker| v24 or higher| <https://docs.docker.com/engine/install/debian/>  
Media Server| Latest version| [Installation](Media-Server-Deployment-Guide_1344451.html)[Configuration](75825154.html)  
EF CX| Latest version| [Deployment](https://expertflow-docs.atlassian.net/wiki/pages/createpage.action?spaceKey=kb&title=CX%20Deployment%20on%20Kubernetes&linkCreation=true&fromPageId=48268951)  
Dialer and database(For outbound only)| 4.5| [Deployment ](CX-Dialer-Deployment-Guide_2529764.html)  
  
### Port Utilization Requirements

The following ports must be open on the server for the voice connector to function.

Type| Application| Description| Port  
---|---|---|---  
TCP| Media Server| ESL port| 8021  
TCP| Media Server| Websocket port| 7443  
TCP| Voice Connector| Access port| any/ (set in docker-compose.yml)  
TCP| Postgres| Database access port| 5432  
TCP| Dialer| Access port| any/ (configured in dialer)  
  
The ports can be opened as follows:

  * SSH into the Debian server.

    * Use command: 

      * 
[code]ssh username@server-ip
[/code]

    * Enter the ssh password and press _Enter_.

    * Use command: 

      * 
[code]su
[/code]

    * Enter the root user's password

  * Run the following command and replace **PORT** with each of the required ports listed above:

    * 
[code]sudo iptables -A INPUT -p tcp -m tcp --dport PORT-j ACCEPT
[/code]

    * Example: 
[code] sudo iptables -A INPUT -p tcp -m tcp --dport 8021 -j ACCEPT
[/code]

  * Save this port configuration with command: 

    * 
[code]sudo iptables-save
[/code]




## Container Deployment

The voice connector is deployed as a docker image.

  * Create a folder voice-connector with the command: 

    * 
[code]mkdir voice-connector
[/code]

  * Enter the folder with the command: 

    * 
[code]cd voice-connector
[/code]

  * Create a file _docker-compose.yml._

    * 
[code]vi docker-compose.yml
[/code]

  * Enter editing mode with the _'I'_ or _'Insert'_ keys.

  * Copy the contents below and paste them into the file _docker-compose.yml_ : 
[code] version: "3.8"
        services:
          voice-connector:
            image: gitimages.expertflow.com/freeswitch/ecx_generic_connector:TAG
            deploy:
              resources:
                limits:
                  memory: 1024m
                reservations:
                  memory: 256m
            container_name: unified-voice-connector
            ports:
              - 8115:8080
            env_file:
              - ./env.txt
            command: ["java", "-Xms256m", "-Xmx1024m", "-XX:+UseG1GC", "-XX:MinHeapFreeRatio=10", "-XX:MaxHeapFreeRatio=30", "-jar", "/app/ecx_generic_connector.jar"]
            restart: always
[/code]

    * Replace the 'TAG' keyword with the required image tag obtained from the releases page [here](Releases-for-CX-Voice-Components_1342256.html).

  * Save and exit by :

    * Press the _**Esc**_ key.

    * Enter the phrase _**:wq**_ to save and exit.

  * Create a file _env.txt_

    * 
[code]vi env.txt
[/code]

  * Enter editing mode with the _'I'_ or _'Insert'_ keys.

  * Copy the contents below and paste them into the file _env.txt_ : 
[code] CX_FQDN=https://cim.expertflow.com
        ESL_PORT=8021
        ESL_PASSWORD=MyEslPass
        DIALER_API=http://192.168.1.10:6666
        LOG_LEVEL=INFO
        AUTH_ENABLED=true
        API_USERNAME=admin
        API_PASS=admin
        ROOT_DOMAIN=tenant-id # for MTT tenancy it will be rootdomain of efcx solution (eg.. expertflow.com)
        ESL_DEFAULT_DOMAIN=192.168.1.17
[/code]

    * CX_FQDN: The address of EF CX. <https://FQDN>. In case of Multitenants it should be: <https://<TENANT-ID>>.<ROOT_DOMAIN>

    * ESL_PORT: The port of Media Server ESL (Default 8021, Same as in Media Server settings [here](75825154.html))

    * ESL_PASSWORD: Media Server ESL password (Use the same password set in the Media Server settings [here](75825154.html))

    * DIALER_API: API link of the dialer in format: [http://IP:PORT](http://IP:PORT/dialer) (Fill in IP and PORT of [dialer](CX-Dialer-Deployment-Guide_2529764.html))

      * Where IP is the IP address of the current server.

      * And PORT is the external port of the dialer container.

      * Leave at default value if not using the progressive outbound feature.

    * LOG_LEVEL: The amount of detail in the logs. Default is **INFO** , and for more detailed logs the value should be **DEBUG**.

    * AUTH_ENABLED: **true** or **false** depending on whether APISIX authentication is enabled in EFCX. The following settings below are set if this value is **true**.

    * API_USERNAME: The username created in Keycloak for API authentication. 

      * On Keycloak create a user in the Expertflow realm.

      * Assign the **admin** and **default** roles to it 

      * Assign a non-temporary password to this user as well.

    * API_PASS: The password for the above user created in Keycloak for API authentication

    * ROOT_DOMAIN: For Multitenant Deployment-> [expertflow.com](http://expertflow.com) (value will be equal to tenantId for on prem deployment)

    * ESL_DEFAULT_DOMAIN: Media Server IP through which ESL connection can be established 

  * Run the command: 

    * 
[code]docker login gitimages.expertflow.com
[/code]

    * Enter your username and password as prompted (make sure that you were granted access to the repository).

  * Within the folder run the command: 

    * 
[code]docker compose up -d
[/code]

  * Confirm that the docker container is running by using the command: 

    * 
[code]docker ps
[/code]


![](attachments/48268951/48400145?width=760)

  * Confirm that the container is running correctly by opening the logs with command: 

    * 
[code]docker logs -f containerID
[/code]


![](attachments/48268951/48400151?width=782)
