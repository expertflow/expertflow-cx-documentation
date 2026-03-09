# CX Knowledgebase : CX Voice Recording Components Deployment Guide

## Prerequisites

### Software Requirements

Item| Recommended| Installation guide  
---|---|---  
Operating System| Debian 12| -  
Docker| v24 or higher| -  
MongoDB | Latest version| [Installation](https://www.mongodb.com/docs/manual/administration/install-on-linux/)  
EF CX| Latest version| [Deployment](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/77692941)  
Secondary FQDN for EFCX| -| IT/Customer will provide a separate FQDN routed to the Media Server IP on Middleware Port  
Media Server| Latest version| Media Server [Installation](Media-Server-Deployment-Guide_1344451.html)Media Server [Configuration](75825154.html)  
  
### Port Utilization Requirements

The following ports must be open on the server for the program to function.

Type| Application| Description| Port  
---|---|---|---  
TCP | MongoDB| Database access port| 27017  
TCP| Postgres| Database access port| 5432  
TCP| Postgres| Database access port| 6115  
  
The ports can be opened as follows:

  * SSH into the Media Server.

    * Use command:
[code] ssh username@server-ip
[/code]

    * Enter the ssh password and press _Enter_.

  * Use command:
[code] su
[/code]

  * Enter the root user's password

  * Run the following commands:
[code] sudo iptables -A INPUT -p tcp -m tcp --dport 5432 -j ACCEPT
        sudo iptables -A INPUT -p tcp -m tcp --dport 27017 -j ACCEPT
        sudo iptables -A INPUT -p tcp -m tcp --dport 6115 -j ACCEPT
        sudo iptables-save
[/code]




### Media Server PostgreSQL Configuration

  * SSH into the Media Server.

    * Use command:
[code] ssh username@server-ip
[/code]

    * Enter the ssh password and press _Enter_.

  * Use command:
[code] su
[/code]

  * Enter the root user's password

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

    * 
[code]host    all             all             0.0.0.0/0            md5
[/code]

  * Save and exit by :

    * Press the _**Esc**_**** key.

    * Enter the phrase _**:wq**_ to save and exit.

  * Restart the Postgresql service:

    * 
[code]systemctl restart postgresql
[/code]




### Create MongoDB database

  1. SSH into the Media Server.

     * Use command:
[code] ssh username@server-ip
[/code]

     * Enter the ssh password and press _Enter_.

  2. Use command:
[code] su
[/code]

  3. Enter the root user's password.

  4. Run command:
[code] systemctl enable mongod
[/code]

  5. Open the MongoDB config file:
[code] vi /etc/mongod.conf
[/code]

  6. Locate the field **bindIp** and set its value to the IP address of the current server. find the **#network interfaces** line as example given below
[code] # network interfaces
         net:
           port: 27017
           bindIp: <Your server IP>
[/code]

  7. Note the value of the **port** field as well.

  8. Run command:
[code] systemctl restart mongod
[/code]

  9. Run command:
[code] mongosh --host HOST --port PORT
[/code]

     1. Where **HOST** is the value of the **bindIp** field in Step 3.

     2. **PORT** is the value of the **port** field in Step 4.

  10. In the following text replace **USER** and **PASS** with your choice of **username** and **password** respectively, then copy and paste it in the Mongo CLI opened in the previous step, and press enter:
[code] use recording-link-activities
         db.createUser(
           {
             user: "USER",
             pwd: "PASS",
             roles: []
           }
         )
[/code]

  11. Confirm the user creation with this command. after creating the user with step 10 above. run this command
[code] db.getUsers()
[/code]

  12. Exit with the command:
[code] exit
[/code]




## Container Deployment

  * SSH into the Media Server.

    * Use command:
[code] ssh username@server-ip
[/code]

    * Enter the ssh password and press _Enter_.

  * Use command:
[code] su
[/code]

  * Enter the root user's password.

  * Run the command:
[code] docker login gitimages.expertflow.com
[/code]

    * For the username prompt, enter **efcx** and for the password prompt enter `RecRpsuH34yqp56YRFUb`.




### Link Uploader

  * Create a folder recording-link-uploader with the command:
[code] mkdir recording-link-uploader
[/code]

  * Enter the folder with the command:
[code] cd recording-link-uploader
[/code]

  * Create a file _docker-compose.yml._
[code] vi docker-compose.yml
[/code]

  * Enter editing mode with the _'I'_ or _'Insert'_ keys.

  * Copy the contents below and paste them into the file _docker-compose.yml_ : 
[code] version: "3.8"
        services:
          recording-link-uploader:
            image: gitimages.expertflow.com/voice-recording-solution/recording-link-activities:TAG
            deploy:
              resources:
                limits:
                  memory: 1024m
                reservations:
                  memory: 256m
            container_name: recording-link-uploader
            env_file:
              - ./env.txt
            volumes:
              - /var/lib/freeswitch/recordings/:/var/lib/freeswitch/recordings/
            command: ["java", "-Xms256m", "-Xmx1024m", "-XX:+UseG1GC", "-XX:MinHeapFreeRatio=10", "-XX:MaxHeapFreeRatio=30", "-jar", "/app/recording-link-activities.jar"]
            restart: no
[/code]

    * Where TAG is the image tag required. Click [here](Releases-for-CX-Voice-Components_1342256.html) to see tags compatibility.

  * Save and exit by :

    * Press the _**Esc**_ key.

    * Enter the phrase _**:wq**_ to save and exit.

  * Create a file _env.txt_
[code] vi env.txt
[/code]

  * Enter editing mode with the _'I'_ or _'Insert'_ keys.

  * Copy the contents below and paste them into the file _env.txt_ : 
[code] CX_FQDN=https://ef-cx.expertflow.com
        CX_CONVERSATION_MANAGER=https://ef-cx.expertflow.com/conversation-manager     
        LOG_LEVEL=DEBUG
        MIDDLEWARE_API=https://ef-cx.expertflow.com
        RECORDING_BACKEND=EFSWITCH
        RETRIEVAL_INTERVAL=10
        MONGODB_HOST=192.168.1.10:27017
        MONGODB_PASSWORD=1234
        MONGODB_USERNAME=efcx
        MONGODB_AUTHENTICATION_DATABASE=recording-link-activities
        MONGODB_REPLICASET=none
        MONGODB_READ_PREFERENCE=secondaryPreferred
        MONGODB_ENABLE_SSL=false
        MONGODB_REPLICASET_ENABLED=false
        TRUST_STORE_PASSWORD=none
        KEY_STORE_PASSWORD=none
        DB_IP=192.168.1.10
        DB_NAME=fusionpbx
        DB_PASS=password
        DB_PORT=5432
        DB_USERNAME=fusionpbx
        AUTH_ENABLED=true
        API_USERNAME=admin
        API_PASS=admin
        CX_ROOT_DOMAIN=expertflow.com (tenant-id for on-prem)
        CX_TENANT_URL=https://mtt02.expertflow.com/cx-tenant
[/code]

    * RECORDING_BACKEND: Keep at default **EFSWITCH**.

    * LOG_LEVEL: The amount of detail in the logs. Default is **INFO** , and for more detailed logs the value should be **DEBUG**.

    * CX_FQDN: The address of EF CX. <https://FQDN> for Single Tenant Deployment. For Multi-tenancy should be discarded or kept as, <https://ef-cx.expertflow.com>

    * CX_CONVERSATION_MANAGER: For single tenant deployment, EF CX Conversation Manager endpoint. [https://FQDN/conversation-manager](https://FQDN). For Multi tenant deployment should be discarded or kept as, <https://ef-cx.expertflow.com/conversation-manager>

    * MIDDLEWARE_API: The Secondary EFCX FQDN. <https://FQDN> (register a separate sub-domain in the root domain that points to the port exposed by the middleware container, 6115 default, example: <https://middleware.expertflow.com>. Secondary FQDN should be routed to media server IP on middleware port with **http** method (e.g.6115). The same URL will be used by all tenants as a middleware endpoint for recording, playback, and download.)

    * MONGODB_HOST: IP address and port of the Mongo Database.

    * MONGODB_PASSWORD: Password of the Mongo Database.

    * MONGODB_USERNAME: Username of the Mongo Database.

    * MONGODB_AUTHENTICATION_DATABASE: Keep at the default value **recording-link-activities**.

    * MONGODB_READ_PREFERENCE: Keep at default secondaryPreferred.

    * MONGODB_ENABLE_SSL: Keep at default **false**.

    * MONGODB_REPLICASET_ENABLED: Keep at default **false**.

    * MONGODB_REPLICASET: Keep at the default **none**.

    * TRUST_STORE_PASSWORD: Keep at the default of **none**.

    * KEY_STORE_PASSWORD: Keep at the default of **none**.

    * RETRIEVAL_INTERVAL: The number of past days to push recording links for on startup.

    * DB_NAME: Media Server database name. Keep at default **fusionpbx**.

    * DB_URL: Media Server server IP address.

    * DB_PORT: Media Server database port. Keep at the default 5432

    * DB_USERNAME: Media Server database name. Default is **fusionpbx** unless changed manually in Media Server.

    * DB_PASS: Media Server database password.

    * AUTH_ENABLED: **true** or **false,** depending on whether APISIX authentication is enabled in EFCX. The following settings below are set if this value is **true**.

    * API_USERNAME: The username created in Keycloak for API authentication.

      * On Keycloak, create a user in the Expertflow realm.

      * Assign the **admin** and **default** roles to it .

      * Assign a non-temporary password to this user as well.

    * API_PASS: The password for the above user created in Keycloak for API authentication.

    * CX_ROOT_DOMAIN: For Multitenant Deployment-> expertflow.com (value will be equal to tenantId for on prem deployment)

    * CX_TENANT_URL: CX tenant url to fetch tenants (e.g., <https://tenant4.expertflow.com/cx-tenant/tenant>). We can use any of the tenant subdomains in place of tenant4, which is configured in CX.

  * Within the folder, run the command:
[code] docker compose up --no-start
[/code]

  * Confirm that the docker container is created:
[code] docker ps -a
[/code]




### Middleware

  * Create a folder recording-middleware with the command:
[code] mkdir recording-middleware
[/code]

  * Enter the folder with the command:
[code] cd recording-middleware
[/code]

  * Create a file _docker-compose.yml._
[code] vi docker-compose.yml
[/code]

  * Enter editing mode with the _'I'_ or _'Insert'_ keys.

  * Copy the contents below and paste them into the file _docker-compose.yml_ : 
[code] services:
          recording-middleware:
            image: gitimages.expertflow.com/voice-recording-solution/recording-middleware:TAG
            container_name: recording-middleware
            restart: always
            deploy:
              resources:
                limits:
                  memory: 1024m
                reservations:
                  memory: 256m
            ports:
              - 6115:8080
            env_file:
              - ./env.txt
            volumes:
              - /var/lib/freeswitch/recordings/:/var/lib/freeswitch/recordings/
              - ./decryptionCache:/app/files/wav/decryptionCache
            command: 
              - java
              - -Xms256m
              - -Xmx1024m
              - -XX:+UseG1GC
              - -XX:MinHeapFreeRatio=10
              - -XX:MaxHeapFreeRatio=30
              - -jar
              - /app/recording-middleware.jar
[/code]

    * Where TAG is the image tag required.

  * Save and exit by :

    * Press the _**Esc**_ key.

    * Enter the phrase _**:wq**_ to save and exit.

  * Create a file _env.txt_
[code] vi env.txt 
[/code]

  * Enter editing mode with the _'I'_ or _'Insert'_ keys.

  * Copy the contents below and paste them into the file _env.txt_ : 
[code] LOG_LEVEL=DEBUG
        RECORDING_BACKEND=EFSWITCH
        ENCRYPTION_ENABLED=false
        DB_IP=192.168.1.10
        DB_PORT=5432
        DB_NAME=fusionpbx
        DB_USERNAME=fusionpbx
        DB_PASS=password
[/code]

    * RECORDING_BACKEND: The mechanism for recording files. Keep it at EFSWITCH.

    * LOG_LEVEL: The amount of detail in the logs. Default is **INFO** , and for more detailed logs the value should be **DEBUG**.

    * ENCRYPTION_ENABLED: Whether encryption of recording files is enabled on the Media Server.

    * DB_IP: IP of Media Server

    * DB_NAME: Media Server database name. Keep at default **fusionpbx**.

    * DB_PORT: Media Server database port. Keep at default 5432

    * DB_USERNAME: Media Server database name. Default is **fusionpbx** unless changed manually in Media Server.

    * DB_PASS: Media Server database password.

  * Within the folder run the command:
[code] docker compose up -d
[/code]

  * Confirm that the docker container is running by using the command:
[code] docker ps
[/code]




## Add Indexing in Media Server Database

  * While on the Media Server, run the following command and note the output password:
[code] cat /etc/fusionpbx/config.conf | grep database.0.password
[/code]

  * Run the following command and enter the password noted before:
[code] psql -h 127.0.0.1 -p 5432 -U fusionpbx -d fusionpbx
[/code]

  * Run the following command:
[code] CREATE INDEX idx_mykey ON v_xml_cdr USING GIN (json) WHERE json->'variables' ? 'sip_h_X-CALL-ID';
[/code]

    * **Note:** If the number of calls on the system is too high, then the query will take a long time to execute.




## Create CRON Job

  * SSH into the Media Server.

    * Use command:
[code] ssh username@server-ip
[/code]

    * Enter the ssh password and press _Enter_.

  * Use command:
[code] su
[/code]

  * Enter the root user's password.

  * Run the following command:
[code] echo '*/5 * * * * docker restart recording-link-uploader' > recording-link-uploader.cron
[/code]

    * The **5** can be replaced with any other value to change the interval in minutes between each run of the uploader.

  * Run the following command to load the job into the cron scheduler:
[code] crontab recording-link-uploader.cron
[/code]




## Set Ingress and Service in EF CX

  * SSH into the EF CX server.

    * Use command:
[code] ssh username@server-ip
[/code]

    * Enter the ssh password and press _Enter_.

  * Use command:
[code] su
[/code]

  * Enter the root user's password.

  * Navigate to the **root** folder.

  * Create a file named **ef-recording-middleware-efswitch.yaml** and add the following content:
[code] apiVersion: v1
        kind: Service
        metadata:
          name: efswitch-service
        spec:
          ports:
          - name: https
            port: 6115
            targetPort: 6115
        ---
        apiVersion: discovery.k8s.io/v1
        kind: EndpointSlice
        metadata:
          name: efswitch-service-1
          labels:
            kubernetes.io/service-name: efswitch-service
        addressType: IPv4
        ports:
          - name: ''
            appProtocol: http
            protocol: TCP
            port: 6115
        endpoints:
          - addresses:
              - "<EFSWITCH-SERVER-IP>"
        ---
        apiVersion: networking.k8s.io/v1
        kind: Ingress
        metadata:
          name: efswitch-service
          annotations:
            spec.ingressClassName: "nginx"
        #    nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
        spec:
          rules:
          - host: <SECONDARY-FQDN>
            http:
              paths:
              - pathType: Prefix
                path: "/"
                backend:
                  service:
                    name: efswitch-service
                    port:
                      number: 6115
[/code]

    * Where **EFSWITCH-SERVER-IP** is the IP address of the Media Server.

    * Where **SECONDARY-FQDN** is the secondary fully qualified domain name for the running EFCX deployment. (for **MTT** , it is the separate sub-domain pointing to the middleware port)

  * Run the following command:



[code] 
    kubectl apply -f /root/ef-recording-middleware-efswitch.yaml
[/code]
