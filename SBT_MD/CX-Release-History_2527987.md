# CX Knowledgebase : CX Release History

Title| Release Date| Release Name| Release Summary  
---|---|---|---  
[(4.10) Patch Release CX4.10.6](/wiki/spaces/CX/pages/1562116112/4.10+Patch+Release+CX4.10.6)| 19 Feb 2026 | CX4.10.6| Enhances agent productivity and bot compatibility while strengthening data integrity and reporting accuracy.  
Also fixes issues causing orphaned agent task entries, missing task dispositions, and inaccurate “Oldest Queued Time” values in dashboards.  
[(5.0) Patch Release CX5.0.3](/wiki/spaces/CX/pages/1693483009/5.0+Patch+Release+CX5.0.3)|  30 Jan 2026 | CX5.0.3| Adds tenant-level 2FA for Agent Desk and Unified Admin logins.  
[(5.0) Patch Release CX5.0.2](/wiki/spaces/CX/pages/1671626753/5.0+Patch+Release+CX5.0.2)| 27 Jan 2026 | CX5.0.2| Introduces Google Play Store as a new channel  
[(5.0) Patch Release CX5.0.1](/wiki/spaces/CX/pages/1539440678/5.0+Patch+Release+CX5.0.1)| 20 Jan 2026 | CX5.0.1| Includes an update to the Email Connector (IMAP/SMTP) to improve compatibility and reliability. Also, delivers critical fixes for 2FA login flows and localisation issues to display Arabic customer names correctly.  
[CX Release Notes 5.0](/wiki/spaces/CX/pages/1342767105/CX+Release+Notes+5.0)| 24 Nov 2025 | CX5.0| CX now supports multi-tenancy, enabling CCaaS providers to host multiple tenants from the same underlying infrastructure securely. In addition, there are some technical improvements in the core platform stability and maintainability.  
[(4.9) Patch Release CX4.9.6](/wiki/spaces/CX/pages/1400832006/4.9+Patch+Release+CX4.9.6)| 04 Nov 2025 | CX4.9.6|  Introduces key enhancements to the customer widget, including improved survey handling and cleaner menu interactions. The release also resolves critical issues related to widget layout, mobile connectivity, and agent name display, ensuring a smoother and more reliable user experience.  
[(4.6) Patch Release Notes 4.6.2](/wiki/spaces/CX/pages/1353482272/4.6+Patch+Release+Notes+4.6.2)| 16 Oct 2025 | CX4.6.2| Provides the fix for the incorrect conversation disposition  
[(4.10) Patch Release CX4.10.3](/wiki/spaces/CX/pages/1307869208/4.10+Patch+Release+CX4.10.3)| 01 Oct 2025 | CX4.10.3|  Includes multi-level pagination, infinite scroll in wrap-up forms, and adds a keyword search bar for quicker wrap-up code selection. Partial form updates streamline minor edits. Adds Agent Hand Raise, allowing agents to request help during ongoing conversations.Brings a redesigned suite of dashboards for supervisors to gain real-time and historical insights, while agents can monitor their daily metrics and team stats directly within the Agent Desk. Introduces message-level ETL for comprehensive extraction and reporting of all communication data. Key fixes include accurate email session end reporting, protection of the wrap-up form during admin pod restarts, clearer agent identification through full-name display, and resolution of chat closure issues when the MRD is absent.  
[(4.10) Patch Release CX4.10.2](/wiki/spaces/CX/pages/1297416214/4.10+Patch+Release+CX4.10.2)| 17 Sep 2025 | CX4.10.2| Includes an update of all core Java components to the GraalVM JDK 21 (LTS) base image. Additionally, Conversation Studio now supports connections to MongoDB that use self-signed TLS certificates. The update also includes performance fixes.  
[(4.4) Patch Release CX4.4.14](/wiki/spaces/CX/pages/1298923553/4.4+Patch+Release+CX4.4.14)| 12 Sep 2025 | CX4.4.14| Includes synchronous processing of****`AGENT_UNSUBSCRIBED `and handles race conditions while publishing `TASK_STATE_CHANGE` to `RESERVED`  
[(4.10) Patch Release CX4.10.1](/wiki/spaces/CX/pages/1229291521/4.10+Patch+Release+CX4.10.1)| 18 Aug 2025 | CX4.10.1| Introduces secure APIs with role-based authorization and token enforcement, along with improved protection for customer widget data. QM authentication now routes through the Application Gateway for added security. Agent Desk sees multiple upgrades, including basic table support, real-time spell check, and a streamlined email thread view. A visible TAT timer now displays on emails to support better prioritization. Email conversations can be added directly to QM. LinkedIn enhancements improve comment handling,Critical bug fixes include support for partial updates in the CX-Customer API and improved formatting logic that ignores empty markers.  
[(4.10) CX Release Notes](/wiki/spaces/CX/pages/1238302847/4.10+CX+Release+Notes)|  13 Aug 2025 | CX4.10| This release delivers a wide range of enhancements across CX, data, UI, and platform performance. Key updates include LinkedIn integration, a redesigned Form Builder experience, and support for initiating WebRTC audio/video calls. CX and Eleveo now support multi-leg call recording, while Cisco Agent and Teams benefit from one-way sync.   
Conversation Studio replaces the Conversation Controller, and dashboards see real-time performance improvements. Historical stats (SLA, AHT, AWT) are now calculated via ETL jobs, and Conversation Search APIs have migrated to GraphQL.  
  
Security and session handling are strengthened with encryption at rest for CX messages, secure messaging via EventBroker, secure transcript URLs, and persistent sessions using refresh tokens. Agents can now be force-logged out, pause conversations, and view active session data.UI enhancements include auto-expanding panels, RTL support, plus updates to Quality Management with real-time alerts, and upgraded reporting through gold query campaigns and new EF data pipelines.   
[CX Release Notes 4.10](/wiki/spaces/CX/pages/1126105089/CX+Release+Notes+4.10)|  13 Aug 2025 | CX4.10| This release delivers a wide range of enhancements across CX, data, UI, and platform performance. Key updates include LinkedIn integration, a redesigned Form Builder experience, and support for initiating WebRTC audio/video calls. CX and Eleveo now support multi-leg call recording, while Cisco Agent and Teams benefit from one-way sync.   
Conversation Studio replaces the Conversation Controller, and dashboards see real-time performance improvements. Historical stats (SLA, AHT, AWT) are now calculated via ETL jobs, and Conversation Search APIs have migrated to GraphQL.  
Security and session handling are strengthened with encryption at rest for CX messages, secure messaging via EventBroker, secure transcript URLs, and persistent sessions using refresh tokens. Agents can now be force-logged out, pause conversations, and view active session data.UI enhancements include auto-expanding panels, RTL support, plus updates to Quality Management with real-time alerts, and upgraded reporting through gold query campaigns and new EF data pipelines.   
[(4.9) Patch Release CX4.9.5](/wiki/spaces/CX/pages/1205633025/4.9+Patch+Release+CX4.9.5)| 31 Jul 2025 | CX4.9.5| Introduces enhanced LinkedIn integration through webhook subscriptions and reinforces API security for Unified Admin through integration of Application Gateway. Also addresses high-priority bug fixes, including:

  * Resolved issues with email transcripts.
  * Fixed errors in the Realtime Dashboard’s team dropdown behaviour.
  * Disabled the 'Hide Comment' action for LinkedIn messages to maintain message visibility.
  * Restricted attachment functionality to valid LinkedIn replies only.

  
[(4.4) Patch Release CX4.4.12](/wiki/spaces/CX/pages/1199341601/4.4+Patch+Release+CX4.4.12)| 18 Jul 2025 | CX4.4.12| 

  * Redis exception handling
  * Redis key not expiring as expected

  
[(4.9) Patch Release CX4.9.4](/wiki/spaces/CX/pages/1163984903/4.9+Patch+Release+CX4.9.4)| 08 Jul 2025 | CX4.9.4| Includes force logout agent from any state  
[(4.9) Patch Release CX4.9.3](/wiki/spaces/CX/pages/1085931718/4.9+Patch+Release+CX4.9.3)| 24 Jun 2025 | CX4.9.3| Introduces the Proxy API for formData transmission to the Form API, enhances security and authentication for file engine APIs using APISIX, implements IP-based rate limiting for the Message Send API to optimize traffic control, and integrates RSA SecureID support for 2-FA in CX Apps to reinforce security measures.Resolved various issues in the Email connector, supervisor login, and agent reply**.**  
[(4.7) Patch Release CX4.7.3](/wiki/spaces/CX/pages/1028063233/4.7+Patch+Release+CX4.7.3)| 05 Jun 2025 | CX4.7.3| Includes Interruptible/Non-Interruptible feature without Cisco Integration and fix vulnerabilities in CX4.7.2 and CX4.7.3  
[(4.9) Patch Release CX4.9.2](/wiki/spaces/CX/pages/1049460737/4.9+Patch+Release+CX4.9.2)| 09 May 2025 | CX4.9.2| Includes CXAPI security via user authentication, License Consumption status tracking, enhancements to the pause/resume conversation feature, and new functionalities in CX Campaigns.   
Also addresses a bug fix/ improvements to the MS Exchange-based email.   
[(4.9) Patch Release CX4.9.1](/wiki/spaces/CX/pages/1044185090/4.9+Patch+Release+CX4.9.1)| 30 Apr 2025 | CX4.9.1| Includes Consult Conference on External Numbers, and ETL for Campaigns Data  
[(4.9) CX Release Notes 4.9](/wiki/spaces/CX/pages/1042317970/4.9+CX+Release+Notes+4.9)|  23 Apr 2025 | CX4.9| Includes more channels, such as Email, WhatsApp, LinkedIn, and YouTube, while enhancing Facebook and Instagram functionality with Button Message support. Optimizes performance through SLA improvements and automates MRD synchronization. Enhances agent capabilities by enabling conference call updates and refining dashboard settings. Improves existing reports by modifying External Transfer Reason Codes and adding detailed Outbound Campaign Reports. Additionally, reinforces security by implementing two-factor authentication via Microsoft Authenticator.  
[(4.7) Patch Release CX4.7.2](/wiki/spaces/CX/pages/980189190/4.7+Patch+Release+CX4.7.2)| 25 Mar 2025 | CX4.7.2| Customer Widget Enhancements

  * Customizable text
  * Text alignment
  * Sound notifications

  
[(4.8) CX Release Notes 4.8](/wiki/spaces/CX/pages/976751452/4.8+CX+Release+Notes+4.8)|  19 Mar 2025 | CX4.8| 

  * Quality Management 
  * Business Calendars
  * Add Support for Media Controls on the Agent Desk for Recordings
  * Eleveo Support in Recording Middleware
  * Consult Transfer to external Numbers

  
[(4.7) Patch Release CX4.7.1](/wiki/spaces/CX/pages/921239553/4.7+Patch+Release+CX4.7.1)| 10 Mar 2025 | CX4.7.1| 

  * MSSQL Target Support in ETL
  * Routing bug fixes
  * Campaigns bug fixes
  * All fixes from [CX4.4.11](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/899121153/4.4+Patch+Release+CX4.4.11)
  * All fixes from [CX4.5.5.1](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/895123816/4.5.3+Upgrade+Guide+CX-4.5.5+to+CX-4.5.5.1)

  
[(4.4) Patch Release CX4.4.11](/wiki/spaces/CX/pages/899121153/4.4+Patch+Release+CX4.4.11)|  19 Feb 2025 | CX4.4.11| 

  * Incorrect Conversation Dispositions
  * Increase in Agent Manager Memory

  
[(4.7) CX Release Notes 4.7](/wiki/spaces/CX/pages/832243451/4.7+CX+Release+Notes+4.7)| 24 Jan 2025 | CX4.7| 

  * Security Enhancements
  * Deployment Optimization
  * Performance Improvements
  * Agent Experience Improvements
  * Supervisor Experience Improvements
  * ETL Enhancements

  
[(4.4) Patch Release CX4.4.10](/wiki/spaces/CX/pages/558366740/4.4+Patch+Release+CX4.4.10)|  30 Dec 2024 | CX4.4.10| Enable External MongoDB Connectivity with Replica-set   
[(4.6) Patch Release Notes 4.6.1](/wiki/spaces/CX/pages/690323457/4.6+Patch+Release+Notes+4.6.1)| 19 Dec 2024 | CX4.6.1| 

  * Update Form Data Submission
  * Add FormID in Survey Distribution
  * Bug Fixes

  
[(4.5.3) Patch Release CX4.5.7](/wiki/spaces/CX/pages/664993793/4.5.3+Patch+Release+CX4.5.7)|  11 Nov 2024 | CX4.5.7| Data Binding Vulnerability Fix  
[(4.5.3) Patch Release CX4.5.5](/wiki/spaces/CX/pages/595886081/4.5.3+Patch+Release+CX4.5.5)|  17 Oct 2024| CX 4.5.5| Delay in receiving notification on the Agent Desk  
[(4.5.3) Patch Release CX4.5.4](/wiki/spaces/CX/pages/232685588/4.5.3+Patch+Release+CX4.5.4)| 10 Oct 2024 | CX4.5.4| 

  * Multi-language Support in Conversation Data 
  * Media-blending Bugs
  * CX-Voice Bugs

  
[(4.4) Patch Release CX4.4.8.1](/wiki/spaces/CX/pages/561512459/4.4+Patch+Release+CX4.4.8.1)|  01 Oct 2024 | CX 4.4.8.1| 

  * Queue Blocking and Advisor Blocking Fix

  
[(4.5.2) CX Release Notes 4.5.2](/wiki/spaces/CX/pages/520749423/4.5.2+CX+Release+Notes+4.5.2)| 16 Sep 2024 | CX 4.5.2| 

  * Consult, Consult Transfer
  * Security Enhancements
  * Performance Improvements
  * Agent Experience Improvements
  * Supervisor Experience Improvements
  * Administrator Experience Improvements
  * Reporting Enhancements

  
[(4.5.1) CX Release Notes 4.5.1](/wiki/spaces/CX/pages/430866876/4.5.1+CX+Release+Notes+4.5.1)|  16 Aug 2024 | CX 4.5.1| 

  * All stability fixes until the latest patch release of CX4.4.8
  * View and Play Recording Links
  * Canned Message on the Agent Desk
  * Batch data processing in reporting connector 
  * Conversation disposition bug fixes
  * Set ActiveMQ Maximum Connections Limit
  * Enhancements 

  
[(4.4) Patch Release CX4.4.9](/wiki/spaces/CX/pages/301137922/4.4+Patch+Release+CX4.4.9)| 02 Aug 2024 | CX 4.4.9| 

  * Security Fix in MongoDB
  * Finesse Login

  
[(4.4) Patch Release CX4.4.8](/wiki/spaces/CX/pages/301203457/4.4+Patch+Release+CX4.4.8)|  13 Jun 2024 | CX 4.4.8| 

  * Conversation Disposition Calculation Fix
  * Agent Getting More Chats than Max Limit

  
[(4.4) Patch Release CX4.4.7](/wiki/spaces/CX/pages/284196908/4.4+Patch+Release+CX4.4.7)|  23 May 2024 | CX 4.4.7| Agent state fixed on Grafana dashboard  
[(4.4) Patch Release CX4.4.6](/wiki/spaces/CX/pages/229703681/4.4+Patch+Release+CX4.4.6)|  20 May 2024 | CX4.4.6| 

  * Horizontal scaling of controller 
  * Removal of controller tracker from Redis on Conversation End 
  * Grafana Dashboard Slowness Issue

  
[(4.4) Patch Release CX4.4.5](/wiki/spaces/CX/pages/219807766/4.4+Patch+Release+CX4.4.5)| 04 May 2024 | CX 4.4.5| 

  * Use a uniform Log Pattern 
  * Remove Message content from Logs
  * Improve Agent Manager Logs

  
[(4.5) CX Release Notes 4.5](/wiki/spaces/CX/pages/155255487/4.5+CX+Release+Notes+4.5)| 08 Mar 2024 | CX 4.5| Includes Multi-Channel Handling, Named Agent Transfer, Agent SLA, Customer Rooms, Auto-answer, Pause/Resume a Conversation, Saving Dashboard Filters, Summary Dashboards for Agents, and Cisco Team Sync  
[(4.4) CX Release Notes](/wiki/spaces/CX/pages/81428587/4.4+CX+Release+Notes)| 19 Jan 2024 | CX 4.4| Includes Wrap-up state and timer, Manual outbound CX Voice, Scheduled Activities, enhancement in Grafana Dashboards by providing multi queue selection, enhancements in Historical Reports, Update Conversational Data, Get active conversation, Revamped Customer widget with configuration updates, Send outboud message to anonymous customer, Update Channel Session Data API, Keycloak error handling on AgentDesk/unified-admin, Viber Connctor, Telegram Connector, Customer Profile Information for anonymous users.  
[(4.3) CX Release Notes](/wiki/spaces/CX/pages/6291657/4.3+CX+Release+Notes)| 24 Oct 2023 | CX 4.3| Includes Priority Routing, Route re-initiated chats, Task EWT and Queue Position API, SMS support via SMPP and Twilio, WhatsApp via Twilio, Instagram Direct Message, Instagram Social Media, Custom Message support in Agent Desk, CX Activity APIs, CX Voice Direct Queue Transfer, Progressive OB Calls, IVR activity trail and Cluster Connectivity Support for PostgreSQL, MongoDB, ActiveMQ and Redis.  
[(4.6) CX Release Notes 4.6](/wiki/spaces/CX/pages/686556331/4.6+CX+Release+Notes+4.6)|  | CX 4.6| 

  * Forms Revamp
  * CX Surveys
  * Outbound Campaigns
  * Performance Improvements (Return/Repeat Customer Identification API)
  * Reporting Enhancements

  
[(4.10) Patch Release CX4.10.1.1](/wiki/spaces/CX/pages/1485438977/4.10+Patch+Release+CX4.10.1.1)|  | CX4.10.1.1| Adds (.eml) attachment support for MS Exchange Email, lets business edit Facebook comments, and hides/unhides Facebook/Instagram comments directly in CX.Additionally, fixes multiple stability issues, including chat status synchronization, Conversation Studio memory leaks, Direct Transfer/Consult routing and re-presentation, display email attachment, and more reliable email handling during MS Exchange failover.  
[(4.10) Patch Release CX4.10.1.2](/wiki/spaces/CX/pages/1546452993/4.10+Patch+Release+CX4.10.1.2)|  | CX4.10.1.2| Resolves MS Exchange inline image issues, corrects multilingual email encoding errors, and introduces configurable socket message payload sizing in Agent Manager.  
[Patch Release CX4.10.3.1](/wiki/spaces/CX/pages/1485176910/Patch+Release+CX4.10.3.1)|  | CX4.10.3.1|  Includes improved conversation data retrieval speed and introduced better Instagram message type identification for more accurate routing and analytics. This release also resolves issues with conversation routing after the Routing Engine restarts, ensures reliable processing of team announcements, prevents agent desk refreshes and draft losses caused by large email images, and enhances system stability when handling invalid data.   
[(4.10) Patch Release CX4.10.5](/wiki/spaces/CX/pages/1449885714/4.10+Patch+Release+CX4.10.5)|  | CX4.10.5| Includes CX platform security with service-based database accounts, Vault-backed credential management, and masking of sensitive connector fields, while expanding Quality Management with screen recording and real-time agent alerts. Also delivers major customer widget and web channel enhancements, including multilingual and encoding fixes, searchable pre-chat dropdowns, and dynamic custom fields.   
Alongside resolves critical fixes for 2FA login flows, SMS auto-close behavior, outbound call MRD handling, Facebook comment truncation, and email/image rendering issues in the MS Email Connector and Agent Desk.  
  
  

