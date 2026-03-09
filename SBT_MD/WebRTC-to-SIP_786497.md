# CX Knowledgebase : WebRTC to SIP

## **ExpertFlow WebRTC**

Providing Video solutions for the web users. Using this solution, a web user can initiate a video call request to the Cisco Contact Center Express (UCCX) and Enterprise (CCE) during an web chat session of Expertflow Hybrid Chat solution.

## **Communication Flow**

  


  1. A web user wants to connect to Cisco Contact Center agent via WebRTC Video without having to download or install any software 
  2. This user request will initiate a call from Customer WebRTC to Cisco Call Center agent
  3. This WebRTC is converted by Expertflow’s WebRTC -SIP gateway to a SIP call, Which is then routed to Cisco Cubes/Gateway from where the routing will be handled by the Cisco end.
  4. The initiating web user will be asked to allow system resources (mic, camera) access from his WebRTC capable web browser
  5. Upon access grant, the video call will be started.



The call is encrypted via WebRTC from the customer’s browser to the EF WebRTC-SIP gateway, and from the gateway to Cisco CUBE using SIP with TLS.

  


![](attachments/786497/786499.png?height=400)

  
  


## **Solution Prerequisite**

Following are the mandatory prerequisites for a smooth installation of the solution up to 50 agents.

### **​Hardware Requirements**

Item| Minimum requirement  
---|---  
**CPU**|  8 cores  
**RAM**|  8 GB  
**Disk**|  250 GB  
  
  


### **​Software Requirements**

Item| Minimum requirement  
---|---  
**OS**|  Debian 10  
**Node**|  Latest  
  
  


### **TLS Requirements**

Certificates from a valid signing authority or Domain signed certificate required for https protocol support.

  


### Port Utilization For Product Installation

We will require Internet access for doing the installation of Expertflow WebRtc Server.

### **For Product connectivity with internal and external components**

Ports mentioned in this section should be open for the mentioned product connectivity with different internal and external components.

  
  
  


**Source Host**| **Destination Host**| **Source Port**| **Destination Port**| **Communication Protocol**| **Scope**| **Description**  
---|---|---|---|---|---|---  
Web Audio Call/video Call| WebRTC Server| any| 7443 | WSS | Public|   
  
Web Audio Call/video Call| WebRTC Server| any| 8021| TCP| Public |   
  
Web Audio Call/video Call| WebRTC Server| any| 3000| HTTPS | Public |   
  
  
  


### **Ports enablement between EF WebRTC Server to Cisco Cube**

**WebRTC Server**| **Network Protocol**| **Application Protocol**| 

### **Destination Server**  
  
---|---|---|---  
1719| UDP| H.323 Gatekeeper RAS port| Cisco Cube   
1720| TCP| H.323 Call Signaling|   
  
2855-2856| TCP| MSRP|   
  
3478| UDP| STUN service|   
  
3479| UDP| STUN service|   
  
5002| TCP| MLP protocol server|   
  
5003| UDP| Neighborhood service|   
  
5060| UDP & TCP| SIP UAS| Cisco Cube  
5070| UDP & TCP| SIP UAS|   
  
5080| UDP & TCP| SIP UAS| Cisco Cube  
8021| TCP| ESL|   
  
16384-32768| UDP| RTP/ RTCP multimedia streaming| Cisco Cube  
5066| TCP| Websocket|   
  
7443| TCP| Websocket|   
  
8081-8082| TCP| Websocket|   
  
  
  


### **Integration on Website**

Expertflow will provide the JS/HTML link to the website owner, which they need to add in the website header. Expertflow will also provide the sample HTML page that can be used as a reference for the website owner/developer. 

  


### **Setting UP a Video Call**

For setting up a video conferencing system , We have a Debian server running the latest stable FreeSWITCH build, IP phones( Zoiper/ Jabber) and Cisco SX set . 

The default port5,060,506,150,805,081

  * codec,H.261 Video (passthru),mod_h26x
  * codec,H.263 Video (passthru),mod_h26x
  * codec,H.263+ Video (passthru),mod_h26x
  * codec,H.263++ Video (passthru),mod_h26x
  * codec,H.264 Video (passthru),mod_h26x  
  
  




![](attachments/786497/786502.png?height=400)
