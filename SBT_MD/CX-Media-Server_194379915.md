# CX Knowledgebase : CX Media Server

The CX Media Server handles and manages the multimedia interactions. It is a class-5 switch that manages voice calling features such as traffic termination by**** establishing SIP trunk with Carrier/Service provider for voice traffic and acts as the primary bi-directional SIP B2BUA for SIP or WebRTC calls for call management.

To establish connection between Agent Desk and Media Server for voice and video calls, please read the [CX Media Server API](CX-Media-Server-API_499253250.html) document.

## Functional Capabilities

  1. **CX Calls Handling:** The Media Server handles inbound and outbound calls, managing SIP registrations, and call routing efficiently. It ensures high call volume management without compromising call quality or stability. It integrates with CX to queue calls and route them based on predefined criteria such as agent availability and caller priority. The server can also stream hold music or announcements during queue times. The Media Server can also record calls for compliance and quality assurance.

  2. **Active Media Handling:** The IVR system within the Media Server enables the creation of IVR scripts, interaction with databases and external applications via APIs and handling of user input through DTMF. The Media Server sits in the pathway of the RTP stream and integrates with automated speech engines (ASRs) and natural language understanding (NLUs) tools to support Conversational IVR or recording of the RTP Stream, facilitating tasks such as transcription, language translation, and sentiment analysis.

  3. **Passive Media Handling:** The Media Server can handle RTP stream for recording or other features like translation, transcription etc. This includes direct integrations for capturing streams from various sources, including IP-based telephony systems and direct SIP endpoints.

  4. **WebRTC:** Media Server supports WebRTC that enables devices to be registered through WSS. This enables agents to log in their devices on web applications. It also supports features like WebRTC to SIP where a caller can initiate a call from a web page or customer application to land on any SIP endpoint e.g. Cisco agent.




|   
---|---  
user needs CUSP-like solution| Only SIP needed  
user needs voice recording| media server needed  
user needs conversational IVR | media server needed  
user needs WebRTC 2 SIP | media server needed  
user needs CPA| media server needed
