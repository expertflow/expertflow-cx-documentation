# CX Knowledgebase : CX Data Sheet

Expertflow CX is a multi-channel customer-centric contact center solution. It stores customer interactions across all channels and provides a unified interaction history. Conversation control scripting is customizable for dynamic conversation flow. Customer profiles are managed in a way that allows businesses to use this data for outbound calls and campaigns. Secure and highly available, it supports its easy-to-use AgentDesk application, integrated self-service bots with flexible training, interactive voice response (IVR), and computer telephony integration (CTI).  
  
Expertflow CX is available as a cloud subscription and may also be installed on-prem on the Kubernetes Platform.

## Features and Benefits

**Capability**| **Features and Benefits**  
---|---  
**Agent Desk**| 

  * Expertflow CX provides a simple browser-based Agent Desk application for CX agents and supervisors. It includes an intuitive, easy-to-use design that helps improve the performance of customer care representatives for high-quality customer service. 
  * With the Unified Admin Console, business admins can provide easy access to the applications, can configure Expertflow CX services and solution components such as general settings, the configuration of CX Routing Engine, Customer Channel Manager, Bot Framework, and more. 
  * Agent Desk supports inbound and outbound contact center functions. Core features include: Customizable agent and supervisor desktop layout
  * Blended agents: can handle inbound and outbound calls along with chat via any supported channel (such as SMS, WhatsApp, or any supported social media channel
  * Multisession web chat
  * Selection of multiple wrap-up reasons for chat channels
  * Supports light theme - dark theme on the AgentDesk to ensure better visibility
  * Supports case-insensitive login
  * Provides responsive font sizes based on the screen size of the Agent Desk
  * Supports back-to-conversation view
  * Displays the agent’s first name and last name
  * Enables Agent Desk to read complex passwords for CX Voice extensions within configurations. 
  * Adds (RTL) support for right-to-left languages on the Agent Desk, improving accessibility and usability for agents who interact in RTL languages such as Arabic and Urdu. This [document](Updating-the-Language-at-Agent-Desk_424214601.html) outlines the supported languages and provides a detailed setup procedure.

  
**Agent**|  Expertflow CX enables its agents to perform various inbound and outbound contact center functions. Core features include:

  * The CX agent can [login](Login-to-Agent-Desk_2529062.html) to AgentDesk using the user's login credentials defined in Keycloak. 
  * [Manages agents’ state ](Change-Agent-State_2524603.html)on each individual media to make themselves ready on a certain media while not ready on the rest. For instance, agents can make themselves available for Chat and not available for voice calls. 
  * Enables agents to[ receive a conversation from queues ](Accept-a-Conversation_2527849.html)where new requests are pushed to agents.
  * Accredits agents to [pull requests from Pull-based Lists](Join-Pull-based-Requests_2528122.html) that they are subscribed to and join a conversation.
  * Allows agents to[ see and update customer profiles ](Accept-a-Conversation_2527849.html)based on the conversation with the customer and [assign labels](Assign-Labels-to-Customers_434667615.html) to the customers to route the customer's request with priority.
  * Let CX agents [handle ongoing conversations](Accept-a-Conversation_2527849.html), Link Customer Profiles, View Conversation History, View Active channels, View Conversation Data, Receive Delivery Notifications, Typing Indicators, Bot Suggestions, send quoted reply, send file attachments, Send Formatted Text, and View Conversation Notifications
  * Allows agents [to transfer](Consult%2C-Transfer-and-Conference_2528529.html) an active conversation,[ add agents to the conference](Consult%2C-Transfer-and-Conference_2528529.html), and [send a Whisper Message.](Send-a-Whisper-Message_143458310.html)
  * Allows agents to consult the chat with the supervisor and use [Whisper Mode](Send-a-Whisper-Message_143458310.html) to get help from the supervisor.
  * Enables the agent to [change the language](Change-Agent-Desk-Language_2529188.html) of the AgentDesk interface to any preferred language. 
  * Enables agents to [embed a Webapp](Embed-a-Webapp-in-Agent-Desk_635502601.html) in AgentDesk
  * Allows agents [to apply Wrap-up and notes](Apply-Wrap-up-and-Add-Notes_2528747.html) during or after the conversation.
  * Enables the CX agent[ to switch channels](Handle-Multi-channel-Conversation_2528824.html) to make an outbound contact on a different channel in an ongoing conversation.
  * Allows agents to manage calls with [CTI Call Controls](CTI-Call-Controls_140869685.html)
  * Enables agents to access essential [recording controls](Handle-Voice-Recording_796590157.html), such as seeking and navigating within recordings. 
  * Enables the agent [to make a manual outbound contact](Make-a-Manual-Outbound-Contact_2528797.html).
  * Enables agents to [raise a hand](Agent-Hand-Raise_519569565.html) and ask for assistance from a supervisor. Any of the team supervisor(s) can accept the hand-raise request.
  * Allows agents to initiate [consult calls, consult transfers, and direct transfers to external numbers](Consult%2C-Transfer-and-Conference_2528529.html) outside the CX environment. Agents can now connect with third-party contacts, such as external vendors, specialists, or helplines, to assist customers with a better experience.
  * Enables agents to view summary statistics, including queues, their states, and ongoing conversations [on real-time dashboards](View-Agent-Dashboards_283607081.html)
  * Allows the agent to simply [logout ](Logout_2525352.html)from the AgentDesk Application by selecting a logout reason defined by the administrator.

  
  
### Management Roles and Benefits

**Role**| **Benefits**  
---|---  
**Supervisor**| 

  * Allows Expertflow CX supervisors[ to monitor real-time dashboards](Realtime-Reports-and-Dashboards_2529305.html) to view the summary statistics of the contact center, including queues, agent states, and ongoing conversations with agents and bots, enabling them to optimize contact center efficiency. This ability to monitor critical performance metrics allows them to train and encourage agent behavior so that agents can perform consistently and efficiently.
  * Supervisors can [silently monitor](Silent-Monitoring_2529320.html) the conversation. 
  * Supervisors can interrupt an agent's conversation using [Barge In](Barge-in_2529322.html) to interact with both the customer and the agent to resolve [any](Team-Announcements_2523883.html) concerns, if any.
  * Supervisors can [create, edit, and delete announcements ](Team-Announcements_2523883.html)for their team agents. 
  * Allows the supervisor or business administrator to define and customize the customer fields provided in[ the customer schema](Customer-Schema_2525665.html)
  * Allows the supervisor/business administrator to [create new customer labels](Customer-Labels_2529344.html) to categorize customers based on certain characteristics.
  * Supervisor can [end the PULL-based request](End-PULL-based-Requests_2528595.html).

  
**Admin**|  Business administrators can configure Expertflow CX services and solution components from the Unified Admin Console.

  * The business admin can[ login](Unified-Admin-Guide_2524407.html) to the Unified Admin using the user's login credentials defined in Keycloak. 
  * The business admin can [upload](Unified-Admin-Guide_2524407.html) the license information for agents and supervisors.
  * The business administrators can select the time zone as per their server location, [choose the language](Unified-Admin-Guide_2524407.html) that the system should support, and set it as the default language.
  * The administrators can make various configurations to make the system ready, such as [adding a bot connector](Unified-Admin-Guide_2524407.html), [adding media routing domains](Unified-Admin-Guide_2524407.html), [mapping MRDs to the channel type](Unified-Admin-Guide_2524407.html), [creating attributes](Unified-Admin-Guide_2524407.html), [assigning these attributes to agents](Unified-Admin-Guide_2524407.html), [creating queues,](Unified-Admin-Guide_2524407.html) [adding steps to queues](Unified-Admin-Guide_2524407.html), [changing the maximum task limit for agents' MRD](Unified-Admin-Guide_2524407.html), [adding channel providers](Unified-Admin-Guide_2524407.html), and [setting up a new channel.](Unified-Admin-Guide_2524407.html)
  * The business administrator is authorized to make other configurations, such as [adding a Web Widget](Unified-Admin-Guide_2524407.html) for web chat, [adding reason codes](Unified-Admin-Guide_2524407.html) for being not-ready or logout, [adding wrap-up forms](Unified-Admin-Guide_2524407.html), adding [new channel type](Unified-Admin-Guide_2524407.html)s, and [adding lists](Unified-Admin-Guide_2524407.html) to handle PULL-Mode requests.

  
  
### Customer Channels

Expertflow CX integrates with the following customer channels and continues to add more digital channels to its supported media list.

  * [Customer Facing Web SDK for Omni Channel Communication](Customer-Facing-SDK-for-Omnichannel-Communication_2526606.html)

  * [Web Channel](88277014.html)




  * [Voice](Voice-and-Video_2527403.html)

  * [Email](Email_112263260.html)[Voice and Video](Voice-and-Video_2527403.html)

  * [Viber](Viber_68747283.html)

  * [Telegram](Telegram_2526302.html)




  * [WhatsApp](WhatsApp_2526019.html)

  * [WhatsApp-Meta Cloud API](Meta---WhatsApp-Cloud-API_131006630.html)

  * [Twitter](Twitter_2549631.html)



  * [Facebook Direct Message](Facebook-Direct-Message_2526025.html)

  * [Facebook-Social Media](Facebook-Social-Media_2526031.html)

  * [LinkedIn](LinkedIn_784007185.html)

  * [YouTube](YouTube_786859078.html)



  * [Instagram Direct Message](Instagram-Direct-Message_2528238.html)

  * [Instagram Social Media](Instagram-Social-Media_2528131.html)

  * [SMS Via SMPP](SMPP_2528799.html)

  * [SMS/MMS Via Twilio](Twilio_2529622.html)




See [Channel capabilities](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2529090/_Customer+Channels) for an overview, and for details on each supported channel, follow the relevant links above.

### System Capabilities

**Multitenancy**|  With multitenancy, you can set up multiple virtually independent contact centers (tenants) provisioned from the same underlying infrastructure. Each tenant operates as a complete, independent contact center environment possessing its own configurations, agents, teams, customers, and interactions. See [Multitenancy](CCaaS-Provider-Guide_1387593741.html) for more details.  
---|---  
**CX Routing**| 

  * Routes customer interaction requests from any channel to the same conversation and the same agent
  * Introduces two ways of routing the requests. [Precision routing/Push-mode routing](Precision-Routing_2525641.html) and [PULL-mode routing](Pull-Mode-Routing_2529097.html).
  * PULL-mode lists - for certain media channels, customer interaction requests are pushed to pull-mode lists. Agents subscribe to these lists to fetch and process on demand. 
  * CX routing facilitates categorizing and prioritizing customers in a way that best meets the business requirements.
  * A wide range of routing logic that can accurately target and selectively route different classes of customers by [prioritized routing treatment](Priority-Routing_2529105.html)
  * Implements [multi-queue priority](Distribution-Rules_247988291.html) to define priority for each queue (1-10, with 10 being the highest). In cases where multiple queues have the same priority, the system considers an individual task’s priority and longest waiting time, respectively.
  * Introduces [Interruptible and Non-interruptible Channel Categories](https://expertflow-docs.atlassian.net/wiki/x/KQAtIQ) to define whether a chat channel category should be interrupted if there is a voice call and vice versa.
  * Ensures that each customer is routed to the right agent at the right location for, first time to maximize the resolution of the request.
  * Adds [Auto Sync MRD](Auto-Sync-MRD-State_1025802251.html) to automatically sync all associated MRDs.

  
**CX Reporting**| 

  * Provides various tabular and graphical [historical reports, IVR reports ](Reports-and-Analytics_2526384.html)and [real-time dashboards](Realtime-Reports-and-Dashboards_2529305.html) with flexible presentation options using Superset for historical reports and Grafana for dashboards.
  * Existing out-of-the-box reports allow the business to review historical and real-time dashboards or view custom reports to track the information required.

  
**Business Calendars**|  The Business Calendars feature allows administrators to define and manage operational schedules, including working hours, holidays, and out-of-office periods. Businesses can create multiple, distinct calendars to represent the schedules of different sites, channels, or teams.A key benefit is the ability to communicate active working hours to customers, setting clear expectations for availability. This feature replaces the older **EF Business Calendars** module in **SupervisorTools**.  
**CX Survey**|  Conduct surveys through any [Customer Channel](https://expertflow-docs.atlassian.net/wiki/x/Vpgm) ([voice](https://expertflow-docs.atlassian.net/wiki/x/q5Am), chat, [Web](https://expertflow-docs.atlassian.net/wiki/x/IpQm), [Email](https://expertflow-docs.atlassian.net/wiki/x/XACxBg)) after a [Conversation](https://expertflow-docs.atlassian.net/wiki/x/LACOBQ) with an actor ([agent](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2528831/Conversation+Objects#Agent), [chat, or voice bot](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2528831/Conversation+Objects#Conversation-Bot)).As a Conversation Designer, you can use [Expertflow Conversation Studio](https://expertflow-docs.atlassian.net/wiki/x/1RiAB) with prebuilt survey nodes. You may also extend and customize the interaction flow with 3rd party integration that best suits your interaction management requirements.[CX Survey Reports](https://expertflow-docs.atlassian.net/l/cp/B1sJrpkG) provide detailed insights based on surveys.   
**CX Campaigns**|  Expertflow CX Outbound provides tools to design, execute, and monitor multi-channel outbound communication campaigns, enabling outreach to contacts via calls, SMS, WhatsApp, and other digital channels. A key aspect of the solution is ensuring compliance through features like robust contact validation against internal and public Do Not Contact (DNC) lists. The system utilizes **Conversation Studio** , a flow-based interface for configuring outbound interaction logic without requiring traditional programming. Core to this are the **Seize** , **Wait** , and **Init** nodes, which control agent and communication port allocation and the controlled initiation of customer interactions for campaign effectiveness.  
**Quality Management (QM)**|  Error rendering macro 'excerpt-include' : User '712020:14b9c475-fd7c-43f0-8626-9323b451e406' does not have permission to view the page 'QMS:Quality Management'.  
**Performance Improvements**| 

  * Adds [performance improvement features](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/1126105089/CX+Release+Notes+4.10) to enhance the system’s overall performance, such as replacing Conversation Controller with Conversation Studio, [migrating Conversation Search APIs to GraphQL](https://api.expertflow.com/#c94f9abf-5f0a-4667-8d52-4805b9fd7808), and [Bulk upload](https://api.expertflow.com/#795c2fc6-e1f4-4c9d-bd7e-2fa88078c467).

  
**Campaign Manager**| 

  * Allows agents to schedule, view and update a scheduled activity on AgentDesk, with a customer at a scheduled date/time. Exposes[ Campaign Scheduler APIs ](https://www.postman.com/expertflow/workspace/expertflow-s-public-workspace/folder/4288348-a6e51948-0ff3-4817-a91e-3c452d7df028)for third-party CRMs or Campaign Managers to upload contacts or create callback requests/ appointments for customers, optionally with a named agent or on a specified skill. 

While agents are handling customer requests, they can also view all upcoming / scheduled activities planned with a customer, on the Agent Desk in addition to the past customer activities.  
**Workforce Management (WFM)**| 

  * Provides integrations with third-party WFM solutions such as Calabrio and Verint.
  * Provides [WFM Solution](https://docs.expertflow.com/wfms/1.0/)

  
**CX Wallboard**| 

  * Has its own wallboards with intuitive design to provide real-time visualization, assists the business to monitor and manage contact center operations effectively. 

  
**Conversation Studio**| 

  * Conversation Studio scripting for dynamic conversation flow that can be changed according to business requirements - see [Conversation Studio](https://expertflow-docs.atlassian.net/wiki/pages/createpage.action?spaceKey=cx&title=Conversation%20Studio&linkCreation=true&fromPageId=2530132)

  
**Conversational IVR**| <https://expertflow-docs.atlassian.net/wiki/x/K4X7K>  
**Voice Recording**| 

  * Provides Voice Recording Solution that can be deployed along with CX for call recording of CX-Voice or Cisco contact center.

  
**Deployment, Upgrades, and Scalability**| 

  * On-prem, cloud, and hybrid ( mingle-mix of Services ) are supported.
  * Any Kubernetes distribution can be selected to deploy Expertflow CX. Currently tested on [K3s](https://k3s.io/), and [RKE2](https://docs.rke2.io/). ( [kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) or [DigitalOcean Managed Kubernetes](https://www.digitalocean.com/products/kubernetes) can also be used). The [deployment plan](/wiki/pages/createpage.action?spaceKey=SBT&title=Deployment%20Planning&linkCreation=true&fromPageId=2530132) explains the supported distributions and deployment types.
  * Scalability is expandable up to the requirement based on the number of concurrent channels of active conversations.

  
**3rd Party Bot Integrations**| 

  * Provides integrations with Rasa, DialogFlow, and any 3rd party chatbot for chat
  * Provides integration with Expertflow IVR for CX Voice, and CVP for CISCO Voice

  
**Security**| 

  * Expertflow CX offers a centralized Identity and Access Management solution, backed by [Keycloak](https://www.keycloak.org/), for enhanced security. This ensures complete security for users while accessing all Expertflow CX resources by passing a process of User Authentication and Authorization.
  * Users are managed in[ the Keycloak Admin Console](https://www.keycloak.org/docs/latest/server_admin/#assembly-managing-users_server_administration_guide). This allows business administrators to manage users, roles, and permissions.
  * Expertflow CX can be deployed as a standalone web application on-prem or on the cloud. To make authentication work, business administrators need to set up a client (resource server) in the **Keycloak** instance.
  * Apart from standalone deployment, Expertflow CX can be set up within the **Cisco Finesse** environment i.e, UCCE or UCCX. This authenticates users in two ways. Either **Login Finesse (With SSO)** or **Login Finesse (Without SSO).**
  * Expertflow CX provides Permission and Access Management (using Keycloak IAM) to access different application resources. For the top-level roles such as admin, agent, and supervisor,[ role-based permissions ](/wiki/pages/createpage.action?spaceKey=SBT&title=Security%20and%20User%20Permissions&linkCreation=true&fromPageId=2530132)are available, and at granular access levels, group-based implementation is also available.
  * Using an industry-standard encryption algorithm (AES256), Expertflow CX [encrypts](Data-Encryption_884932744.html) certain types of data. 
  * Adds TLS encryption and authentication on all CX core components.
  * Adds [Two-factor Authentication support via Google/Microsoft Authenticator App and Email](Two-Factor-Authentication---User-Guide_1685881100.html)
  * Adds [API Security using Application Gateway](/wiki/pages/createpage.action?spaceKey=SBT&title=API%20Security%20using%20Application%20Gateway&linkCreation=true&fromPageId=2530132)

  
**Licensing and Ordering**| 

  * Provides concurrent user licenses. So businesses can buy concurrent user licenses from the Expertflow Online Shop, for the concurrent number of agents who are going to use the Agent App.

  
  
Expertflow CX provides integration with various CRM Connectors such as

  * [Suite CRM Connector](https://docs.expertflow.com/suite-cisco/1.0.0/)

  * [Zoho Connector](https://docs.expertflow.com/zoho-c-efcx/1.0.0/)

  * [Microsoft Dynamics](https://docs.expertflow.com/dynamics-web/)

  * [Salesforce](https://docs.expertflow.com/salesforce-cti/)

  * [Oracle Siebel](https://docs.expertflow.com/siebel/)

  * [SAP Interaction Center/Hybris C4C](https://docs.expertflow.com/sap/),

  * [Service Cloud CX-CTI Connector](https://docs.expertflow.com/service-cloud/),

  * [JavaScript CTI Toolbar](https://docs.expertflow.com/javascript-cti/)

  * [ServiceNow](https://docs.expertflow.com/servicenow/)

  * [Generic Connector](https://docs.expertflow.com/gc/4.4.12/)




### Add-ons

Expertflow CX provides integration with CISCO Finesse Gadgets including[ Internal Chat Finesse Gadget](https://docs.expertflow.com/inter-chat/) and [Supervisor Whisper Finesse Gadget](https://docs.expertflow.com/super-whisper-gadget/)
