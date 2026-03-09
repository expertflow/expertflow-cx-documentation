# CX Knowledgebase : Cisco Voice Channel Configuration Guide

## Recommendations

  *  _Finesse and CX Server**Time** should be synced._

  * _Always keep the**Customer Activity Timeout** greater than the configured call timeout on Cisco (finesse) for the Cisco voice channel._




## System Configurations

  * The Cisco Finesse admin should be contacted for the configuration of the Finesse agents and gadgets.

  * Once those are set up, the following [guide](Deploying-Finesse-Gadget_2526405.html) can be used to update and integrate with CX.




# Unified Admin Configurations

## Channel Manager Config

  * The following variables need to be added in the _channel provider_ for the _**CISCO_CC**_ channel type on unified-admin**.** The provider webhook is not required in this case 


![image-20250723-081032.png](attachments/2527992/1205403690.png?width=1270)

  * Add a channel connector for the _provider_ configured above for the _CISCO_CC_ channel type on unified-admin. 


![image-20250723-081137.png](attachments/2527992/1206059009.png?width=556)

  


  * Add a channel for _CISCO_CC_ channel type on unified-admin.

    * Add the desired channel name.

    * You can add any number as a service identifier for the channel. (_The same identifier should be used in the Agent Desk configurations for the attribute_ `CISCO_SERVICE_IDENTIFIER`)

    * Select the configured Bot.

    * Select the configured channel connector.

    * Configure the activity timeout. (The recommended value for the _**customer inactivity timeout**_ should be greater than the one configured for a call in the contact center; otherwise, the system may cause issues.)  
  


![image-20250723-081450.png](attachments/2527992/1205600322.png?width=570)

    * Select Channel Mode, i.e., _HYBRID. (_ supported by the system as of yet.)

    * Set the _**Routing Mode** _as  _EXTERNAL._

    * To configure an Outbound conversation, enable the **Default Outbound Channel** for the Cisco voice channel being used. 




## Channel Category Config

  * Set the _**ManagedByRoutingEngine, Autosync state with the parent state & Interruptible** _flag to _**false**_ for the default CISCO CC category. 

  * The _**MaxTaskRequest**_ should be set to 1.   
  


![image-20250714-072711.png](attachments/2527992/1190363260.png?width=498)




## Agent Channel Categories Config

  * For each user, the max task request should be set to 1 for _CISCO CC_ mrd.  


![](attachments/2527992/2557723.png?width=68)



  


  


  


  


  


  


  

