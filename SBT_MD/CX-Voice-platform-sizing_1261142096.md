# CX Knowledgebase : CX-Voice platform sizing

The CX Voice Platform is a core component of Expertflow’s Expert for CX, enabling enterprises to handle customer voice interactions as part of their omnichannel engagement strategy.

This document describes on-premise deployment options for the CX Voice Platform. It outlines the main deployment scenarios, required infrastructure, SIP trunking considerations, and additional aspects such as high availability (HA).

## Hardware Requirements

**Category**| **< 100 concurrent calls **| **< 300 concurrent calls**| **< 500 concurrent calls**| **> 1000 concurrent calls**  
---|---|---|---|---  
Voice platform| **CPU:** 4 Core  
**RAM:** 8 GB  
**Storage:** 100 GB SSD| **CPU:** 8 Core  
**RAM:** 16 GB  
**Storage:** 200 GB SSD| **CPU:** 12 Core  
**RAM:** 24 GB  
**Storage:** 300 GB SSD| **CPU:** 16 Core  
**RAM:** 32 GB  
**Storage:** 500 GB SSD  
  
## Software Prerequisites

  * Debian 12+




## Deployment Scenarios

### Baseline Voice Deployment (CX Voice with Legacy IVR)

**Purpose** : Standard voice platform deployment for inbound/outbound calls, including legacy IVR (DTMF menus), announcements, conferencing, and voice recording.

**Required Components**

  * CX Core Platform (mandatory foundation)

  * Media Server (handles RTP streams, IVR prompts, conferencing, and voice recording)




**Voice Recording (VRS)** : Part of the Media Server, no extra server required.

**Links to Prerequisites**

  * [CX Voice – Media Server Hardware Prerequisites](https://expertflow-docs.atlassian.net/wiki/x/w4MU)

  * [VRS - Hardware Requirements](https://expertflow-docs.atlassian.net/wiki/spaces/VRS/pages/1252983037/14.5+Solution+Prerequisites)




### AI-Powered Voice Deployment (Voicebots, Transcription & Translation)

**Purpose** : Advanced, AI-driven voice experience enabling conversational IVR, voicebots, speech-to-text transcription, and text-to-speech translation.

**Required Components**

  * CX Core Platform

  * Media Server

  * Jambonz

  * AI Engines




**Additional AI Services Required**

  * ASR (Automatic Speech Recognition) – hardware/software prerequisites TBD

  * NLU (Natural Language Understanding) – prerequisites TBD

  * TTS (Text-to-Speech) – prerequisites TBD

  * LLM/AI connectors (optional for advanced language use cases)




**Links to Prerequisites**

  * Media Server Hardware Prerequisites

  * Jambons Hardware Prerequisites

  * ASR Prerequisites – Placeholder

  * TTS Prerequisites – Placeholder




### WebRTC Voice and Video Deployment

**Purpose** : Enables customers to make voice and video calls directly from web or mobile applications. This allows seamless browser-to-agent or app-to-agent communication without requiring traditional SIP hardphones or softphones.

**Required Components**

  * CX Core Platform

  * Media Server (handles RTP streams for voice and video)

  * Customer Widget (provides the WebRTC client interface embedded in browser or mobile apps)




**Additional Considerations**

  * Requires TURN/STUN configuration for NAT traversal.

  * SIP trunking is still required if WebRTC calls need to connect to PSTN.

  * Bandwidth requirements should be validated in video-heavy use cases.




**Links to Prerequisites**

  * Customer Widget Documentation

  * Media Server Prerequisites




## SIP Trunking

The CX Voice Platform integrates with SIP trunks to connect with the PSTN or the customer’s telephony provider.

  * Customer-Provided SIP Trunks: Customer contracts with their own provider; Expertflow integrates with it.

  * Expertflow-Provided SIP Trunks: Available in selected geographies (to be confirmed per opportunity).




## High Availability (HA)

For mission-critical deployments, CX Voice supports HA configurations.

  * CX Core Cluster – redundant application servers

  * Media Server HA – active-passive or active-active clustering

  * CX SIP Proxy (OpenSIPS) HA – load balancing and failover for SIP signaling

  * Database Redundancy – clustering for data consistency and failover




## Deployment Summary (At-a-Glance)

Deployment Type| Required Servers & Components| Notes  
---|---|---  
Baseline Voice| CX Core Platform + Media Server| Includes Legacy IVR (DTMF) and Voice Recording  
AI-Powered Voice| CX Core Platform + Media Server + Jambons + AI Engines| Conversational IVR, Voicebots, Transcription & Translation; requires ASR, NLU, TTS  
With HA| CX Core Cluster + Media Server HA + CX SIP Proxy HA| Ensures redundancy and failover for mission-critical environments  
  
Mention platform components and services that are provisioned by this installation. 

## ![\(blue star\)](images/icons/emoticons/72/2753.png) Questions

Are there multiple deployment configurations as they are in [CX-Core platform](CX-Core-platform_1261142050.html)

  * Questions: SIP trunks, IVR, etc., - Presales know what sort of documents are needed based on Cisco contact center deployment planning experience

  * voice recording [y/n] - sizing

  * transcription [y/n] - sizingBHCA plus other variables to estimate call-volume for inbound and outbound 

  * HA

  * what else?




## System Prerequisites and Installation Steps
