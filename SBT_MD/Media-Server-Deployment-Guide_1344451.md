# CX Knowledgebase : Media Server Deployment Guide

## Prerequisites  
  
### Software Requirements

Item| Recommended| Installation guide  
---|---|---  
Operating System| Debian 12| -  
  
### Hardware Requirements

**Item**| **Minimum**  
---|---  
RAM| 16GB  
Disk space| 150GB  
CPU| 8 cores  
  
### Port Utilization Requirements

The following ports must be open on the server for the voice connector to function.

**FireWall Ports/Port range**  
| **Network Protocol**| **Description**  
---|---|---  
5060:5091| udp| Used for SIP signaling.  
5060:5091| tcp| Used for SIP signaling.  
8021| tcp| Media Server Event Socket  
16384:32768| udp| Used for audio/video data in SIP, WSS, and other protocols  
7443| tcp| Used for WebRTC  
8115| tcp| Voice Connector API  
5432| tcp| Postgresql Database  
3000| tcp| Outbound Dialer API  
22| tcp| SSH  
80| tcp| HTTP  
443| tcp| HTTPS  
1194| udp| OpenVPN  
  
The ports can be opened as follows:

  1. SSH into the Debian server.

     1. Use command 
[code] ssh username@server-ip
[/code]

     2. Enter user password.

     3. Use command 
[code] su
[/code]

     4. Enter root password

  2. Verify whether iptables is installed. If it is not installed, proceed with the installation.

  3. 
[code]sudo apt update
         sudo apt install iptables
[/code]

  4. Run the following command for each port listed in the table above, replacing the port number <PORT> and PROTOCOL as needed.



  * 
[code]sudo iptables -A INPUT -p PROTOCOL -m PROTOCOL --dport <PORT> -j ACCEPT
        
        Example:
        sudo iptables -A INPUT -p tcp -m tcp --dport 8021 -j ACCEPT
[/code]




These <**PORT >** are the required **Firewall port/port range** and **PROTOCOL** is the associated **Network Protocol.**

  4. Save this port configuration with command:
[code] sudo iptables-save
[/code]




### Additional Firewall Rules

  * `iptables -A INPUT -i lo -j ACCEPT`

  * `iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT`

  * `iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT`

  * `iptables -P INPUT DROP`

  * `iptables -P FORWARD DROP`

  * `iptables -P OUTPUT ACCEPT`




## Install Media Server

  1. Run commands:

     * 
[code]sudo apt update
           sudo apt install -y lua-sec certbot lua-socket lua-json lua-dkjson git lsb-release
           mkdir /usr/src/fusionpbx-install.sh
           git clone -b 5.2 https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/media-server-setup.git "/usr/src/fusionpbx-install.sh"
           chmod -R 777 /usr/src/fusionpbx-install.sh
           cd /usr/src/fusionpbx-install.sh/debian && ./install.sh
[/code]

  2. Once the installation has finished, some information will be shown as below Copy and save the username and password:


![](attachments/1344451/1344465.png?width=272)

  4. In a web browser, open the domain name URL and use the provided username and password to log on.

     1. A screen like below should open for a successful installation:


![](attachments/1344451/89227365.png?width=510)

  5. If the page does not open, then go to the command line and run
[code] systemctl stop apache2
         systemctl restart nginx
[/code]

  6. In the command line, use the command to access the Freeswitch command line as shown below:
[code] fs_cli
[/code]


![](attachments/1344451/1344481.png?width=306)
