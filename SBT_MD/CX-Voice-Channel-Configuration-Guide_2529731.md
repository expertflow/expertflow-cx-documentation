# CX Knowledgebase : CX Voice Channel Configuration Guide

## Recommendations

  *  _Media Server and Expertflow CX Server**Time** should be synced._

  * It is not recommended to enable **CX** and **Cisco Voice Channel** simultaneously; only one voice channel should be configured at any given time.

  * The recommended value for the _**customer inactivity timeout**_ and _**Agent Request TTL**_ should be greater than the configured value for a call in the contact center, if any; otherwise, 1 hour (3600 sec) should be set as a minimum value, after which the session expires in our system. 




### Limitations

  * The limitations of the multi-channel are mentioned [here](CX-Voice-Limitations_74448913.html).

  * Direct ext-to-ext calls are not supported. 

  * Any private browser window is not supported.




## System Configurations

  * The media server connection details need to be updated in the relevant tenant settings, following this [guide](Updating-Media-Server-Configs-in-Tenant-Settings_1668251717.html).

  * To update the CTI config variables added in the unified-agent config map, follow this [guide](Updating-AgentDesk-Environment-Variables-for-CX-Voice_2529026.html).

  * For user extension configuration, follow this [guide](Adding-Agent-Extensions-for-CX-Voice_2526927.html).




## Unified Admin Configurations

### CX Voice Queue

  * Create a **Routing Attribute** called **CX Voice** with the type of **Boolean**.


![image-20240319-100706.png](attachments/2529731/173899858.png?width=818)

  * Create a **CX Voice Queue** with the following settings.


![image-20240319-100829.png](attachments/2529731/173932618.png?width=814)

  * Once the queue is created, click on drop-down, then click on **Add Step,** and set the following steps


![image-20240319-100951.png](attachments/2529731/174456855.png?width=814)

  * Open the **Agent Attributes** section and assign the **CX Voice attribute** to your desired agent.


![image-20240319-101113.png](attachments/2529731/174620693.png?width=828)

### Channel Manager Config

  * The following variables need to be added in the _channel provider_ for the _**CX_VOICE**_ channel type on the unified-admin**.**

    * The provider webhook is required in this case and is the callback URL exposed by the **Voice** connector in the format: **http://VC-IP:VC-PORT/ccm-msg/receive**


![](attachments/2529731/2558856.png?width=533)

  * Add a channel connector for the _provider_ configured above for the****_**CX_VOICE**_**** channel type on the unified-admin.


![](attachments/2529731/2558861.png?width=429)

  * Add a channel for the _**CX_VOICE**_**** channel type on the unified-admin.

    * Add the desired channel name.

    * Add the configured DN(Dial Number) for the contact center(the same as that set in Media Server [for inbound IVR](75825154.html)) as a _**Service identifier**_ for the channel.

    * Select the configured Bot.

    * Select the configured channel connector.

    * Select Channel Mode, i.e., _HYBRID._(supported by the system as of yet.)

    * Select Agent Selection Policy, i.e., _LONGEST AVAILABLE_(supported by the system as of yet.)

    * Configure the activity timeout. 

    * Set _**Routing Mode** to PUSH_  
![](attachments/2529731/2558871.png?height=91)

    * Select the queue that is associated with the _CX VOICE_ MRD.

    * Configure the _Agent Request TTL_.

    * To configure Outbound conversation, enable the **Default Outbound Channel** for the CX Voice channel being used.   


![](attachments/2529731/2551981.png?width=553)



  


  


  

