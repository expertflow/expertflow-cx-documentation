# CX Knowledgebase : Call Forking Concepts

## Introduction

The term call forking refers to the process of splitting a single incoming call into multiple parallel sessions, allowing it to be directed to different destinations simultaneously. This technique is widely used in contact centers, voice communication systems, and various telephony applications to enhance efficiency and provide diverse services. 

[CX Media Server ](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2527403/Voice+and+Video#CX-Media-Server)receives media stream that can either be SIPREC from:

  * a third-party gateway such as Cisco CUBE

  * [CX SIP Proxy](CX-SIP-Proxy_31719845.html)

  * forking at the level of the phone such as Cisco BIB




During a call, the [CX Media Server](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2527403/Voice+and+Video#CX-Media-Server) can extract information in real-time and make the same available to any [participant/actor](Conversation-Objects_2528831.html) in a conversation. It can then integrate with [NLU engines](150503736.html) to respond back within a conversation. Expertflow CX has several use cases for call forking which are defined here.

## How Call Forking Works

The fundamental concept behind call forking involves duplicating an incoming call and routing each duplicate to a different endpoint or application. This is achieved through the use of specialized software or hardware components in the communication infrastructure.

The process generally involves the following steps:

  1. **Incoming Call** : When a call is received, the system initiates the call forking process.

  2. **Duplication** : The system duplicates the call, creating identical copies of the original call.

  3. **Routing to Endpoints** : Each duplicate call is then independently routed to different endpoints or applications. These endpoints can include various devices, applications, or even external systems.

  4. **Parallel Processing** : The duplicated calls can now be processed concurrently, enabling parallel interactions and services.




![Desktop-34.png](attachments/130252894/391217158.png?width=698)

## Use Cases of Call Forking

### 1\. Voice Biometrics and Authentication:

Call forking is often employed in voice biometrics systems. The original call is sent to an interactive voice response (IVR) system for user authentication, while a duplicate call is simultaneously directed to a voice biometrics engine for real-time verification.

### 2\. Agent Assist and Transcription:

Call forking sends a copy of the call to a Voice AI bot for real-time transcriptions, translations, or suggestions to be provided to the agent during the conversation.

### 3\. Recording/Quality Monitoring:

In contact centers, call forking is utilized for call recording in which one copy of the call leg is sent to the recording server. 
