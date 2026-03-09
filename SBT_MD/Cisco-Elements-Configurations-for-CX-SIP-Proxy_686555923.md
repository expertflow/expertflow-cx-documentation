# CX Knowledgebase : Cisco Elements Configurations for CX SIP Proxy

# Inbound Call Configuration

### CUBE (Cisco Unified Border Element) Settings

  * **Incoming Dial-Peer Configuration**

    * Set the destination IP address of the SIP Proxy in the `session target ipv4` field.

  * **Add SIP Proxy to the trusted List**

    * Add the CX SIP Proxy server IP(s) to the trusted list for security purposes.




**CVP (Cisco Voice Portal) Settings:**

  * **SIP Proxy Group Assignment:**

    * Create a group containing the CVP IP addresses.

    * Map this group to a Dial Number (DN) on the SIP Proxy from the CUBE.

  * **CVP OAMP (Operations, Administration, Maintenance, and Provisioning) Configuration:**

    * Configure the IP address of the SIP Proxy for specific labels (45199, 9191, 9292) in CVP. 

    * These labels correspond to configurations in the EF SIP Proxy.

  * **VVB (Cisco Voice Browser) Integration:**

    * On the SIP Proxy, assign a group containing VVB IP addresses to the labels mentioned above.

  * **CUCM (Cisco Unified Communications Manager) Integration:**

    * In CVP OAMP, set the SIP Proxy IP against the Extension Numbers of the CUCM.

    * On the SIP Proxy, assign a group containing CUCM IP addresses to handle call routing to the CUCM.




## **_Outbound Call Configuration_**

**Manual Outbound Call:**

**CUCM Settings:**

  * **SIP Trunk Creation:**

    * Create a SIP Trunk on the CUCM that connects to the SIP Proxy.

  * **Group and Pattern Mapping on SIP Proxy:**

    * Create a group on the SIP Proxy containing the IP addresses of the CUBE.

    * Map this group to specific dialing prefixes of the Outbound Call. e.g. (96***********)




**Dialer Connected Call:**

**Cisco Dialer Settings:**

  * **Registry Configuration:**

    * Set the IP address of the SIP Proxy Server in the `SIPServerAddress` field in the Cisco Dialer Registry settings.




**SIP Proxy Settings:**

  * **Group and Pattern Mapping:**

    * Similar to manual outbound, create a group containing the IP addresses of CUBE.

    * Map this group to specific dialing patterns on the SIP Proxy.




These configurations are essential for ensuring proper routing and security of SIP-based calls in a Cisco network environment. The settings in CUBE, CVP, and CUCM need to be precisely configured to ensure seamless communication between these components and the SIP Proxy.
