# CX Knowledgebase : Cisco Outbound Connector Docker Deployment Guide

# Prerequisites

## Software Requirements

Item| Recommended| Installation guide  
---|---|---  
Operating System| Debian 12|  -  
Docker| v24 or higher| <https://docs.docker.com/engine/install/debian/>  
EF CX| Latest version| <https://expertflow-docs.atlassian.net/l/cp/hHy74HdV>  
Cisco UCCX/UCCE| Latest version| <https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-installation-guides-list.html>  
Redis| Latest version| [Install guide](https://redis.io/docs/install/install-redis/)  
  
## Port Utilization Requirements

The following ports must be open on the server for the cisco connector to function.

Type| Application| Description| Port  
---|---|---|---  
TCP| Cisco Connector| Access port| 7115/ (set in docker-compose.yml)  
TCP| Redis| Redis access port| 6379 (default Redis server port)  
  
The ports can be opened as follows:

  * SSH into the Debian server.

    * Use command 
[code] ssh username@server-ip
[/code]

    * Enter the SSH password and press _Enter_.

    * Use command 
[code] su
[/code]

    * Enter the root user's password

  * Run the following command and replace **PORT** with each of the required ports listed above:

    * 
[code]sudo iptables -A INPUT -p tcp -m tcp --dport PORT-j ACCEPT
[/code]

      * Example: 
[code] sudo iptables -A INPUT -p tcp -m tcp --dport 8021 -j ACCEPT
[/code]

  * Save this port configuration with the command: 
[code] sudo iptables-save
[/code]




## Redis Setup

  * After installing Redis, enable it:
[code] systemctl enable redis
        systemctl start redis
        systemctl enable redis-server
        systemctl start redis-server
[/code]

  * Run the following commands:
[code] sed -i '/protected-mode/c\protected-mode no' /etc/redis/redis.conf
        sed -i '/bind 127.0.0.1 -::1/c\# bind 127.0.0.1 -::1' /etc/redis/redis.conf
        sed -i '/bind 127.0.0.1 ::1/c\# bind 127.0.0.1 ::1' /etc/redis/redis.conf
[/code]

  * Run the following command, but replace **PASSWORD** with your desired Redis password:
[code] sed -i '/# requirepass/c\requirepass PASSWORD' /etc/redis/redis.conf
[/code]

  * Restart Redis:
[code] systemctl restart redis-server
        systemctl restart redis
[/code]




## Container Deployment

The Cisco connector is deployed as a docker image.

  * Create a folder _cisco-outbound-connector_ with the command 
[code] mkdir cisco-outbound-connector
[/code]

  * Enter the folder with the command 
[code] cd cisco-outbound-connector
[/code]

  * Create a file _docker-compose.yml._

    * 
[code]vi docker-compose.yml
[/code]

  * Enter editing mode with the _'I'_ or _'Insert'_ keys.

  * Copy the contents below and paste them into the file _docker-compose.yml_ : 
[code] version: "3"
        services:
          cisco-outbound-connector:
            image: gitimages.expertflow.com/rtc/cisco-outbound-connector:1.1
            container_name: cisco-outbound-connector
            ports:
              - 7115:8080
            env_file:
              - docker-variables.env
            restart: always
[/code]

  * Save and exit by :

    * Press the _**Esc**_**** key.

    * Enter the phrase _**:wq**_ to save and exit.

  * Create a file docker-_variables.env_

    * 
[code]vi docker-variables.env
[/code]

  * Enter editing mode with the _'I'_ or _'Insert'_ keys.

  * Copy the contents below and paste them into the file _env.txt_ : 
[code] CISCO_FQDN=https://uccx.test
        CISCO_PASS=1234
        CISCO_TYPE=CCX
        CISCO_USERNAME=administrator
        CX_FQDN=https://efcx.com
        DB_IP=192.168.1.10
        DB_NAME=dbname
        DB_PASS=1234
        DB_PORT=1504
        DB_USERNAME=user
        LOG_LEVEL=DEBUG
        REDIS_DB=0
        REDIS_HOST=localhost
        REDIS_PASS=1234
        REDIS_PORT=6379
        REDIS_DELAY=10
        SERVICE_ID=1234
[/code]

    * CISCO_FQDN: The address of the Cisco deployment.

    * CISCO_USERNAME: The admin username of the Cisco deployment.

    * CISCO_PASS: The admin password of the Cisco deployment.

    * CISCO_TYPE: CCX or CCE, depending on the Cisco deployment.

    * CX_FQDN: The address of EF CX. <https://FQDN>

    * DB_IP: The server IP address of the Cisco database.

    * DB_NAME: The name of the Cisco database where the **dialinglist**(CCX) or **Dialer_Detail**(CCE) tables are located.

    * DB_PASS: The password of the Cisco database.

    * DB_PORT: The port of the Cisco database. For CCX the default is 1504. For CCE the default is 1433.

    * DB_USERNAME: The username of the Cisco database.

    * LOG_LEVEL: The amount of detail in the logs. Default is **INFO** , and for more detailed logs the value should be **DEBUG**.

    * REDIS_DB: The index of the Redis cache where call IDs will be stored. Can be a number from 0 through 16.

    * REDIS_HOST: The server IP address of the Redis cache. Leave at **localhost** if the Redis cache is deployed on the same server as the connector.

    * REDIS_PASS: The password of the Redis cache. 

    * REDIS_PORT: The port of the Redis cache. The default is 6379. 

    * REDIS_DELAY: The time in minutes the connector will wait between checking call results for the call IDs stored in the Redis cache.

    * SERVICE_ID: Service Identifier for the connector set in the EF CX channel settings.

  * Within the folder run the command 
[code] docker compose up -d
[/code]

  * Confirm that the docker container is running by using the command 
[code] docker ps
[/code]

  * Confirm that the container is running correctly by opening the logs with the command 
[code] docker logs -f containerID
[/code]



