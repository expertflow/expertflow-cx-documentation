# CX Knowledgebase : CX Dialer Deployment Guide

## Prerequisites

### Software Requirements

Item| Recommended| Installation guide  
---|---|---  
Operating System| Debian 12|  -  
Docker| v24 or higher| <https://docs.docker.com/engine/install/debian/>  
Postgres| v13 or higher| <https://www.postgresql.org/download/linux/debian/>  
Media Server| Latest version| [Installation](Media-Server-Deployment-Guide_1344451.html)[Configuration](75825154.html)  
Voice Connector| 4.5| [Deployment](Voice-Connector-Deployment-Guide_48268951.html)  
  
### Port Utilization Requirements

The following ports must be open on the server for the dialer to function.

Type| Application| Description| Port  
---|---|---|---  
TCP| Media Server| ESL port| 8021  
TCP| Media Server| Websocket port| 7443  
TCP| Dialer| Access port| 6666  
TCP| Postgres| Database access port| 5432  
  
The ports can be opened as follows:

  * SSH into the Debian server.

    * Use command: 

      * 
[code]ssh username@server-ip
[/code]

    * Enter the ssh password.

    * Use command 

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

  * Save this port configuration with command: _**sudo iptables-save**._




## Set up Postgresql database and table

  * Navigate to the Postgresql folder.

    * 
[code]cd /etc/postgresql/<version>/main/
[/code]

    * Where <version> is the version of Postgresql being used.

  * Open the file **postgresql.conf**.

    * 
[code]vi postgresql.conf
[/code]

    * Scroll down to find the line _**#listen_addresses='*'**_ and remove the _**#**_ symbol.

  * Save and exit by :

    * Press the _**Esc**_**** key.

    * Enter the phrase _**:wq**_ to save and exit.

  * Open the file **pg_hba.conf**.

    * 
[code]vi pg_hba.conf
[/code]

    * Scroll down to the bottom and add the line:

      * _**host all all 0.0.0.0/0 md5**_

  * Save and exit by :

    * Press the _**Esc**_**** key.

    * Enter the phrase _**:wq**_ to save and exit.

  * Restart the Postgresql service:

    * 
[code]systemctl restart postgresql
[/code]

  * Create user 'efswitch':

    * 
[code]su - postgres
          createuser efswitch
[/code]

  * Create database 'efcx'

    * 
[code]createdb efcx
[/code]

  * Assign password 'PASSWORD' to user 'efswitch':

    * 
[code]psql
          alter user efswitch with password 'PASSWORD';
[/code]

      * Change PASSWORD to any password of your choice.

  * Assign control of database 'efcx' to user 'efswitch':

    * 
[code]ALTER DATABASE efcx OWNER TO efswitch;
          grant all privileges on database efcx to efswitch;
[/code]

  * Exit back to root with command (twice) 

    * 
[code]exit
          exit
[/code]

  * Login to database 'efcx' with user 'efswitch':

    * 
[code]psql -h 127.0.0.1 -p 5432 -U efswitch -d efcx
[/code]

    * Enter the password set earlier.

  * Create table 'contacts' by running the command:

    * 
[code]CREATE TABLE contacts (id varchar(40) PRIMARY KEY NOT NULL, customer_number varchar(20) NOT NULL, campaign_type varchar(20) NOT NULL, ivr varchar(20), gateway_id varchar(40) NOT NULL, tenant_id varchar(40) NOT NULL, status varchar(20), call_result varchar(40), received_time timestamp with time zone, dial_time timestamp with time zone, campaign_id varchar(40) NOT NULL, campaign_contact_id varchar(40), start_time timestamp with time zone, end_time timestamp with time zone, priority integer, dialing_mode varchar(20), routing_mode varchar(20), resource_id varchar(40), queue_name varchar(20));
[/code]

  * Table can be queried after logging in to database with SQL commands such as:

    * 
[code]SELECT * FROM contacts;
          DELETE FROM contacts;
[/code]




## Container Deployment

The dialer is deployed as a docker image.

  * Create a folder outbound-dialer with the command 

    * 
[code]mkdir outbound-dialer
[/code]

  * Enter the folder with the command 

    * 
[code]cd outbound-dialer
[/code]

  * Create a file _docker-compose.yml._

    * 
[code]vi docker-compose.yml
[/code]

  * Enter editing mode with the _'I'_ or _'Insert'_ keys.

  * Copy the contents below and paste them into the file _docker-compose.yml_ : 
[code] version: "3"
        services:
          outbound-dialer:
            image: gitimages.expertflow.com/rtc/outbound-dialer:TAG
            container_name: outbound-dialer
            ports:
              - 6666:8080
            env_file:
              - docker-variables.env
            restart: always
[/code]

    * Replace the 'TAG' keyword with the required image tag obtained from the releases page [here](Releases-for-CX-Voice-Components_1342256.html).

  * Save and exit by :

    * Press the _**Esc**_**** key.

    * Enter the phrase _**:wq**_ to save and exit.

  * Create a file docker-_variables.env_

    * 
[code]vi docker-variables.env
[/code]

  * Enter editing mode with the _'I'_ or _'Insert'_ keys.

  * Copy the contents below and paste them into the file _docker-variables.env_ : 
[code] DB_URL=192.168.1.10
        DB_USERNAME=username
        DB_PASS=password
        DB_PORT=5432
        DB_NAME=name
        DB_DDL_AUTO=update
        DB_CONN_TIMEOUT=3000
        ESL_IP=192.168.1.10
        ESL_PORT=8021
        ESL_PASSWORD=ClueCon
        DEFAULT_IVR=*9664
        VOICE_CONNECTOR=http://192.168.1.10:8115
        ESL_CONNECT_DELAY=60
        CONTACT_RETRIEVAL_DELAY=20
        LOG_LEVEL=INFO
        ROOT_DOMAIN=NIL # for MTT it will be the root domain of the cx solution eg. expertflow. for On-prem it will be equal to `tenantId` defined in cx 
        CX_TENANT_URL=https://tenant3.expertflow.com/cx-tenant/tenant
[/code]

    *   * Set these according to the following table: 




**Config Params**| **Expected Values**| **Notes**  
---|---|---  
**DB_URL**|  IP Address e.g. 192.168.1.2| The URL of the database from which contacts are to be pulled. Change this to the IP address of the current server  
**DB_USERNAME**|  Text e.g. admin| The dialer database username  
**MAX_CONCURRENT_CALLS**|  Number e.g. 10| Maximum number of calls that can be active at a timeThis value must **always** be less than the maximum concurrent calls allowed on the EFSwitch SIP trunk in use for outbound calls. If set higher, then the extra calls created by the dialer will be **stuck** in the database on the **dialed** state. These stuck calls can only be removed by directly interacting with the database. Before setting this value also account for the call volumes and speed of the **other types of calls** taking place on the EFSwitch (manual outbound, IVR inbound etc).To confirm the maximum concurrent calls allowed by the trunk, contact your SIP Trunk provider.  
**DB_PASS**|  Text e.g. abc123| The dialer database password  
**DB_PORT**|  Number e.g. 5432| The dialer database port (Default 5432)  
**DB_NAME**|  Text e.g. dialer| The dialer database name  
**DB_CONN_TIMEOUT**|  Number e.g. 3000| Maximum time allowed (in milliseconds) for connecting to the database. (Default 3000)  
**ESL_IP**|  IP Address e.g. 192.168.1.2| IP address of the EFSwitch ESL to use. (The IP of the server that EFSwitch is deployed on)  
**ESL_PORT**|  Number e.g. 8021| Port of the EFSwitch ESL. (Default 8021, Same as in EFSwitch settings [here](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/75825154))  
**ESL_PASSWORD**|  Text e.g. ClueCon| Password for the EFSwitch ESL. (Default ClueCon, Same as in EFSwitch settings [here](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/75825154))  
**DEFAULT_IVR**|  IVR Dialing number e.g. *9664| Default IVR to play in case of none provided for outbound call (Default *9664)  
**SERVICE_IDENTIFIER**|  Number e.g. 1218| Service Identifier for the voice connector. (Default 1218, set in EFSwitch IVR settings [here](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/75825154))  
**VOICE_CONNECTOR**|  FQDN with IP Address and port e.g. <http://192.168.1.2:4321>| Webhook of the voice connector. Format: [http://VC-IP:Port](http://VC-IPPort)  
**ESL_CONNECT_DELAY**|  Number e.g. 60| Delay in seconds between checking EFSwitch ESL connection status  
**CONTACT_RETRIEVAL_DELAY**|  Number e.g. 20| Delay in seconds before retrieving contacts from the dialer database  
**CALLS_PER_SECOND**|  Number e.g. 10| The maximum number of calls that can be generated in a secondThis value must **always** be less than the **sessions-per-second** value in **EFSwitch** otherwise the excess calls created per second by the dialer will be **stuck** in the database on the **dialed** state. These stuck calls can only be removed by directly interacting with the database. To confirm the value of **sessions-per-second** on **EFSwitch** :

  * Open the EFSwitch command line on the EFSwitch server via the command**fs_cli -p <EFSwitch-CLI-Password> **
  * Run the command **fsctl sps** and note the value displayed.
  * Before setting this value also account for the call volumes and speed of the **other types of calls** taking place on the EFSwitch (manual outbound, IVR inbound etc).

  
**MAX_CALL_TIME**|  Number e.g. 60| The time in minutes for which each contact in the database is allowed to stay on the **dialed** or **agent_pending** states, after which it’s state is manually updated to **pending** state to be retriedThis value must **always** be greater that the**Agent TTL** value in the **EF CX** **Channel Settings** in **Unified Admin**.  
**LOG_LEVEL**|  INFO/DEBUG| Determines the amount of detail in the logs. Default is **INFO** , and for more detailed logs the value should be **DEBUG**.  
  
  * Save and exit by :

    * Press the _**Esc**_**** key.

    * Enter the phrase _**:wq**_ to save and exit

  * Apart from above following configuration should be set during tenant registeration and bootstraping. Visit [this](Tenant-Onboarding--To-be-removed_1015775291.html). Below setting will be there by default but if needed to update any, [this](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-7285ff3f-d54f-49e0-9bb3-7c45f4a68687) api can be used to update the settingw. For this one first need to fetch tenants with [this](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-24bdd065-9f95-43b8-8859-9a5ccb3d12f2) api, copy the desired tenant payload and tenantId, and send it in as payload with updated values. Following is sample dialer object.
[code] "dialer": {
                    "serviceIdentifier": "8224",
                    "maxConcurrentCalls": "5",
                    "maxCallTime": "60",
                    "callsPerSecond": "15"
                }
[/code]

  * Need to call CX Tenant webhook registeration api with following payload, to register a webhook. Make sure to replace the host ip accordingly.
[code] {
            "clientName": "Dialer",
            "webHookURL": "http://<IP>:<Port>",
            "createdBy": "admin",
            "updatedBy": "admin"
        }
[/code]

  * Run the command: 

    * 
[code]docker login gitimages.expertflow.com
[/code]

    * Enter your username and password as prompted (make sure that you were granted access to the repository).

  * Within the folder run the command: 
[code] docker compose up -d
[/code]

  * Confirm that the docker container is running by using the command: 

    * 
[code]docker ps
[/code]

  * Confirm that the container is running correctly by opening the logs with command: 

    * 
[code]docker logs -f containerID
[/code]

  * Add the dialer server IP and dialer container port to the voice connector environment file and run the following command within the voice connector folder:
[code] docker compose up -d
[/code]



