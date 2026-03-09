# CX Knowledgebase : Cisco Contact Center Integration with EF CX Cloud

## Establish Connectivity-CX Cloud to Cisco Contact Center

### Network Connectivity

Integrating the on-premises Cisco Contact Center with cloud-based EFCX applications necessitates robust network connectivity to ensure smooth communication and data exchange between the environments. Here's a refined approach to achieve this:

  1. **Assess Network Connectivity Options** : Begin by evaluating whether a direct network connection with Network Address Translation (NAT) or a VPN tunnel is more suitable for integrating the solution.

  2. **Direct Connection with NAT** : If EFCX needs to communicate with Cisco Finesse inside the LAN, consider establishing a direct connection with NAT on the main gateway Router/Firewall. This setup redirects inward traffic to Cisco Finesse within the LAN.

  3. **VPN Tunnel for Security** : If direct inward traffic with NAT poses security concerns, opt for establishing a Site-to-Site VPN to connect the on-premises network with the cloud infrastructure. This secure VPN tunnel can be configured to permit only the necessary protocols, ports, and algorithms for communication. 




### What should be the Prerequisites?

Below are the primary requirements to establish connectivity 

1- Public IP addresses of cloud instance and On-Premises infrastructure ( for VPN tunnel endpoints)

2- TCP / UDP port list for secure communication

3- Internal subnet network ID for LAN and cloud 

4- Finesse Server IP address

### Servers Connectivity

  1. The agent should have access to EFCX-AgentDesk via the internet or VPN site-site tunnel.

  2. EFCX should have access to the Cisco Finesse Servers over ports 443, 7443, and 8445.




### Agents Connectivity

For Agents Connectivity, see the following guides:

  * [Agent Desk Integration with Cisco Finesse](Agent-Desk-Integration-with-Cisco-Finesse_342327334.html)

  * [AgentDesk Environment Configurations for Cisco](Environment-Configurations-for-Cisco_1021575170.html)

  * [Cisco Voice Channel Configuration Guidec](Cisco-Voice-Channel-Configuration-Guide_2527992.html)



