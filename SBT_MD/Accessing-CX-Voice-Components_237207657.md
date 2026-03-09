# CX Knowledgebase : Accessing CX Voice Components

## SSH into server

  1. Run command: 
[code] ssh username@IP-addr
[/code]

  2. **username** is the server SSH username provided.

  3. **IP-addr** is the IP address of the server.

  4. Enter the SSH password and press ENTER.

  5. If the username provided is not root, type and enter 'su', enter the SSH password, and press ENTER.




## Open a port

  1. Run the command
[code] sudo iptables -S
[/code]

  2. Search your required port in the resulting text. If it is listed, then the port is already opened, otherwise, open it with the following steps.

  3. SSH into the server whose port is to be opened.

  4. Run the command :
[code] sudo iptables -A INPUT -p tcp -m tcp --dport PORT -j ACCEPT
[/code]

  5. **PORT** is the server port to be opened.

  6. Run the command 
[code] sudo iptables-save
[/code]

  7. Test the port with the command 
[code] telnet server-IP-addr PORT
[/code]

  8. **server-IP-addr** is the IP address of the server.

  9. **PORT** is the server port to be opened.

  10. If the connection succeeds then you may exit the connection by using the command combination **Ctrl+]** followed by entering **close** and pressing **ENTER**.

  11. If the connection time is out or refused:

     1. Run the command:
[code] sudo reboot
[/code]

  12. After a short duration _ssh into the server_ again.

  13. Open ports **8021,** and **5432** via **step 2.**

  14. Open your required voice connector plus dialer ports via **step 2**.




## Get VC/Dialer details

  1. Obtain the details of your deployment.

  2. Note the container name.

  3. _SSH into the server_ where the component is deployed.

  4. Locate the component Docker folder and navigate within it.

  5. Open the docker-compose.yml file by running the command:
[code] vi docker-compose.yml
[/code]

  6. The environment variables file is set in the **env_file** field.

  7. The port is set in the **ports** field on the left-hand side of the colon i.e. for “3001:8080”, the component's port will be 3001.




## Media Server logs

  1.  _SSH into Media Server._

  2. Run command: 
[code] fs_cli -p PASSWORD
[/code]

  3. **PASSWORD** is the Media Server password provided.

  4. If error occurs, run the following command: 
[code] systemctl restart freeswitch
[/code]

  5. Run step 2 again. If an error is still shown, consult the Support team.




## Dialer logs

  1.  _SSH into the dialer server._

  2. Run command: 
[code] docker ps
[/code]

  3. Note the container ID of the dialer container you are using.

  4. Run command: 
[code] docker logs -f ID
[/code]

  5. **ID** is the container ID of your used dialer container.

  6. To exit these logs at any time, use the key combination **Ctrl+C**.




## Voice Connector logs

  1.  _SSH into the voice connector server._

  2. Run command: 
[code] docker ps
[/code]

  3. Note the container ID of the VC container you are using.

  4. Run command:
[code] docker logs -f ID
[/code]

  5. **ID** is the container ID of your used voice connector container.

  6. To exit these logs at any time, use the key combination **Ctrl+C**.




## CCM Logs

  1.  _SSH into the EF CX server._

  2. Run the following command, to get the list of pods:
[code] kubectl get pods -n expertflow
[/code]

  3. Copy the**NAME** field that starts with **ef-ccm** e.g. **ef-ccm-77bd79ccbc-6jdnk**.

  4. Run the following command: 
[code] kubectl logs -f POD_NAME -n expertflow
[/code]

  5. **POD_NAME** is the NAME field copied in step 3




## Agent Desk config-map

  1.  _SSH into the EF CX server._

  2. Run the commands:
[code] cd cim-solution/kubernetes/cim/ConfigMaps
         vi ef-unified-agent-configmap.yaml
[/code]




## Contacts database

### Access the database

  1.  _SSH into server._

  2. Run the command: 
[code] psql -h 127.0.0.1 -p 5432 -U USERNAME -d DB_NAME
[/code]

  3. **USERNAME** is the database username

  4. **DB_NAME** is the database name

  5. Enter the database password when prompted.

  6. If there is an error when using the previous command :

     1. Run the following command : 
[code] systemctl status postgresql
[/code]

  7. If error is shown then run command : 
[code] systemctl restart postgresql
[/code]

  8. Try step 2 again.

  9. If an error occurs then consult with the Support team.




### Database commands

  * List contacts via this query: 
[code] SELECT * from contacts;
[/code]

  * Clear database via the query: 
[code] DELETE FROM contacts;
[/code]




### Troubleshoot database connection

  1.  _Open port_ 5432 on the database server.

  2. Verify that the database details in the _environment variable_ files of the VC and Dialer are the same as those described for your deployment.




## Media Server in browser

Open in browser: [**https://IP-addr**](https://IP-addr), where IP-addr is the IP address Media Server.

### Add IP to Media Server ACL

  1. Open Settings under the Advanced tab.

     1. Note the value of the Event Socket ACL field.

  2. Open Access controls under the Advanced tab.

  3. Open the entry that matches the aforementioned Event Socket ACL field.

     1. In the CIDR field add the IP address that you wish to unblock from Media Server.

     2. Set the type for this row to 'allow'.

  4. Click **Save** on the top right.

  5. Open SIP Status under the Status tab.

  6. Press the Reload ACL button at the top.




### Check Media Server gateway status and ID

  1. Open the Gateways section under the Accounts tab.

  2. Note the State value of the gateway you wish to check.

     1. NOREG/REG means there is no issue.

     2. FAIL_WAIT means there is an issue, consult the Support team.

  3. To check gateway ID, click on any gateway to open its details and note down the value after “**?id=** ”.

  4. To restart the gateway, press the **Stop** button under the **Action** column, followed by the **Start** button after refreshing.




### Check Media Server Inbound IVR dialplan

  1. Open the Dialplan Manager section under the Dialplan tab.

  2. Open the cxIvr dialplan which has your dialing number.

  3. The IVR script that runs is specified in the Data column where the Type is **lua**.




### Check Media Server Outbound IVR

  1. Open the IVR Menus section under the Applications tab.

  2. The IVR menus are listed along with their extension numbers.




### Check Media Server RONA dialplan

  1. Open the Dialplan Manager section under the Dialplans tab.

  2. Search and open the **local_extension** dialplan. 

  3. Scroll down to the row available at the bottom, containing “**app.lua failure_handler** ” and ensure the previous row has set **vcApi.lua ‘rona’**.




### Check Queue Transfer extension in Media Server Dialplan

  1. Open the Dialplan Manager section under the Dialplans tab.

  2. Verify that there is a cxQueue dialplan with the direct transfer DN that has been set in the _Agent Desk config map_.

  3. If there is none then request the Support team to create one.




### Check agent extension registered on Media Server

  1. Check extension of agent on Agent Desk(Click on profile icon).

  2. On Media Server open Registrations under the Status tab.

  3. Check if the extension is listed under the User column.




## Media Server Scripts

  1.  _SSH_ into the Media Server.

  2. Navigate to the script folder via the command: 
[code] cd /usr/share/freeswitch/scripts
[/code]

  3. The scripts for a certain dialing number e.g. 1333 would be: 

     1. cx_env1333.lua

     2. cxIvr.lua

     3. vcApi.lua

     4. cx_hangup.lua

  4. The environment variables in the cx_env file will have the following structure:

![Untitled-20240423-083935.png](attachments/237207657/237174898.png?width=500)



## CX Unified Admin

  1. Open the Unified Admin in the browser.

     1. On the browser open the link CX-FQDN/unified-admin.

     2. Login with admin credentials.

  2. Open the Channel Provider section.

     1. Open the CX Voice provider settings.

     2. Confirm that the Provider webhook contains the IP and port of the correct Voice connector.

  3. Open the Channel connector section.

     1. Open the CX Voice connector settings.

     2. Confirm that the correct provider is set.

  4. Open the Channel section.

     1. Open the CX Voice channel settings.

     2. Confirm that the correct Service Identifier has been set.

     3. Confirm that the correct default queue has been set.

  5. Open the Routing Engine section.

     1. Under the 'Agent Attributes' section check that your agent has been [assigned the correct skill](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2524407/Unified+Admin+Guide#Step-5%3A-Assign-Attributes-to-Agents) for Voice calls.

     2. In the Queue section, confirm MRD that the Voice queue has the correct '[Associated MRD](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2524407/Unified+Admin+Guide#Step-6%3A-Create-a-Queue)' i.e. CX Voice.

     3. Confirm that the Voice queue is using the [correct skill](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2524407/Unified+Admin+Guide#Step-7%3A-Add-Steps-to-the-Queue) from step 5a.



