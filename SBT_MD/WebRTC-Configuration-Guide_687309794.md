# CX Knowledgebase : WebRTC Configuration Guide

## Prerequisites

Before configuring the WebRTC channel, ensure the following components are properly deployed and configured:

  * [Voice Connector ](CX-Voice-Deployment_1344510.html)

  * [EF Switch](CX-Voice-Deployment_1344510.html)

  * Microphone & camera permissions should be enabled on both the customer and the agent sides.




## Recommendations

  * EF Media Server and Expertflow CX Server **Time** should be synced.

  * It is not recommended to enable **WebRTC** and **Cisco Voice Channel** simultaneously; only one voice channel should be configured at any given time.

  * The recommended value for the _**customer inactivity timeout**_ and _**Agent Request TTL**_ should be greater than the configured value for a call in the contact center, if any; otherwise, 1 hour (3600 sec) should be set as a minimum value, after which the session expires in our system. 




## CX System Configurations

  * To update the CTI config variables added in the unified-agent config map, follow this [guide](Updating-Environment-Variables-for-WebRTC_1186136178.html).

  * For user extension configuration, follow this [guide](https://expertflow-docs.atlassian.net/wiki/x/z44m).




**Disclaimer**

  * A WebRTC call is always a multichannel call because the web session is initiated first; only then can we initiate audio/video or screen sharing calls. Therefore, the Web channel must be configured before the WebRTC channel.




### Limitations

  * The limitations of the multi-channel are mentioned [here](CX-Voice-Limitations_74448913.html).

  * Any private browser window is not supported.




## Unified Admin Configurations

### CX Voice Queue

  * Create a**Routing Attribute** (you may choose any descriptive name, such as `WebRTC Voice`) with the type set to `Boolean`  





![image-20240319-100706.png](attachments/687309794/687309829.png?width=1375)  
---  
  
  * **Create a queue** (you may assign any descriptive name, such as `WebRTC Queue`) and **associate it with the MRD type**`CX Voice`, which is required for routing voice interactions to the Agent Desk.




![image-20240319-100829.png](attachments/687309794/687309826.png?width=1375)  
---  
  
  * Once the queue is created, click on the drop-down, then click on **Add Step,** and set the following steps. Ensure the queue is linked to the routing attribute created earlier..




![image-20240319-100951.png](attachments/687309794/687309823.png?width=1375)  
---  
  
  * Open the **Agent Attributes** section and assign the **WebRTC Voice attribute** to your desired agent.




![image-20240319-101113.png](attachments/687309794/687309820.png?width=1375)  
---  
  
### Channel Manager Configuration  


  * The following variables need to be added in the _channel provider_ for the _**WEB_RTC**_ supported channel type on the unified-admin**.**

    * The provider webhook is required. In this case, it is the callback URL exposed by the **Voice** connector in the format: [**http://VC-IP**](http://VC-IP)**:VC-PORT/ccm-msg/receive**  
  





![Screenshot \(23\).png](attachments/687309794/687309817.png?width=1376)  
---  
  
  * Add a channel connector for the _provider_ configured above for the****_**WEB_RTC**_**** channel type on the unified-admin.




![Screenshot \(24\).png](attachments/687309794/687309814.png?width=1375)  
---  
  
  * Add a channel for the _**WEB_RTC**_**** channel type on the unified-admin.

    * Add the desired channel name.

    * Add the configured DN(Dial Number) for the contact center as a _**Service identifier** (_**Dialing URI** in customer widget) for the channel.

    * Select the configured Bot.

    * Select the configured channel connector.

    * Select Channel Mode, i.e., _HYBRID._(supported by the system as of yet.)

    * Select Agent Selection Policy, i.e., _LONGEST AVAILABLE_(supported by the system as of yet).

    * Configure the activity timeout. 

    * Set _**Routing Mode** to PUSH_  


![](attachments/687309794/687309835?width=250)

    * Select the queue that is associated with the _CX VOICE_ MRD.

    * Configure the _Agent Request TTL_. 




### Pre Chat Form Schema

We have to create a pre-chat form for the customer widget at the Forms tab on the Unified Admin.

  * Pre-chat chat proper format must be followed because this formatted data from the customer server is sent to the FreeSWITCH server, which further sends that data to CCM so it can identify the customer once the call lands on the agent desk.

  * Make sure the proper format is followed for naming conventions.




  * Select the pre-conversation type of forms.

![6-20250512-133712.png](attachments/687309794/1077837829.png?width=997)

  * Now, add the name field in the pre-conversation form schema.

![8.png](attachments/687309794/1018003508.png?width=1072)

  * Now, add the phone field in the pre-conversation form schema.

![7.png](attachments/687309794/1017020736.png?width=1072)



###   
Web Widget Configurations

  * Create a _web widget_ inside the **Channel Manager** tab.

  * Now add details of web identifier, title, form info, language, etc.

![2.png](attachments/687309794/1017086170.png?width=1072)



  * Enable the**"Enable WebRTC".** (Once enabled, additional fields will appear)

  * Enter the **FreeSwitch Server URL & Port** of the FreeSwitch (FS) server connected to your instance.

  * Set the **Dialing URI** as defined in your WebRTC [dial plan](https://expertflow-docs.atlassian.net/wiki/x/AgCFB#Configure-Dialplans).

  * Create a new **SIP Extension** on the FreeSwitch server and provide its corresponding [password](http://password.In) . In case of MTT use **domain** name Instead of **SIP Extension**

  * Specify the name of the **Channel** you created for WebRTC.

  * Add the **WebSocket Server (WSS)** server URL. This is a mandatory requirement for WebRTC to function properly.  


![3.png](attachments/687309794/1017610292.png?width=1072)![4-20250512-134357.png](attachments/687309794/1077870598.png?width=997)

  * Now save the changes.



