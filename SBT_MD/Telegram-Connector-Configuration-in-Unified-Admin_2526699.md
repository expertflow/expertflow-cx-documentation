# CX Knowledgebase : Telegram Connector Configuration in Unified Admin

This section provides detailed steps to set up Telegram Configurations in CIM Unified Admin Console.  
  
If you have been redirected to this page, we now assume that you have already created a telegram application and have received the following details to set up the Telegram Connector in the Unified Admin Console.

  1. **BOT-TOKEN**



If you don't have any details of the above-mentioned, please look into our guide _[here](https://expertflow-docs.atlassian.net/wiki/x/mowm)_ to help you create a Telegram Account and Application.

First of all, go to Unified Admin Console ([https://<fqdn>/unified-admin](https://fqdn/unified-admin)) and create an **MRD** , **Routing Attribute** , **Queue** specifically for Telegram Channel so that we can assign these dedicated items for Telegram Channel. Then **assign** the **MRD** to the selected **agent** and set up the **agent** **attributes**. All these steps will be performed in the same way as we usually set up for any other channel or even for a basic unified-admin setup. If you have any confusion in setting up things mentioned in this step, you can review the [Unified Admin Setup Guide](https://expertflow-docs.atlassian.net/l/cp/jD1rammN).

### Channel Type Configuration

  1. The Telegram channel type will be automatically bootstrapped by the system in the same way as the other channels.
  2. You can select the associated **MRD** to your Telegram channel connector.
  3. The Telegram Icon will be automatically bootstrapped but you can as well upload your own icon.  
  
![](attachments/2526699/2551863.png?height=400)  
  
  
  




### Channel Provider Configuration

It's recommended to use the service name of the component in the **"Channel Provider - > Provider's Webhook"** field. However, FQDN can also be used with some additional custom configurations.

  1. Click on add new channel provider to create a new Telegram channel provider.(ie name can be Telegram Channel Provider)  
![](attachments/2526699/2551868.png?width=866)
  2. Select Channel Type as "TELEGRAM" from the drop-down menu.
  3. Provide the service name of Telegram Connector in the **Provider Webhook** field as http://{SERVICE-NAME}:{SERVICE-PORT}. Replace the {**SERVICE-NAME} and**{**SERVICE-PORT}** in the URL with the component's k3s-based service name and port _(It can be fetched using_** _k get svc -n expertflow_** _)_**E.g:**  
For K3s:__[http://ef-telegram-connector-svc:8080](http://ef-viber-connector-svc:8080)  
For Helm Based: [http://cx-channels-telegram-connector-svc:8](http://cx-channels-viber-connector-svc:8080)664




![](attachments/2526699/494469250.png?width=800)

  
  


  1. Click on **Add Custom Attribute** and add the following attributes.  
\- **BOT-TOKEN  
  
NB: **These attributes should be named as above while configuring them to the system.

**Attribute Name**|  Description| Type| Required| Example  
---|---|---|---|---  
**BOT-TOKEN**|  It's a unique key that is used to identify specific resources on Telegram.forgot your bot token? please visit _[here](https://expertflow-docs.atlassian.net/l/cp/F0N8NuZY)_ to get your token.| String100| Yes| FGad**********34***OA  
  



### Channel Connector Configuration

  1. Add a new Channel Connector. Name can be eg. **Telegram Channel Connector**.
  2. Select Channel Provider Interface as the one we created in previous step. (I.e. Telegram Channel Provider)
  3. Once you select the channel provider interface value, then the respective custom attribute fields will appear. These fields will be those which we added in the previous step as part of custom attributes. 
  4. Enter the **BOT-TOKEN** values in it from the one that we extracted while setting up Telegram Developer Account.  
  
![](attachments/2526699/14123069.png?width=791)  




### Channel Configurations

  1. Now in the **Channel** menu, you should see a channel named "TELEGRAM". Expand the collapsible menu and click on "**Add new channel** ".
  2. The name can be "Telegram DM".
  3. In the Service Identifier field, you will need to call the below api to get your service identifier.  
\- Make a **GET** Method call to this API. <https://api.telegram.org/bot><telegram-botToken>[/getMe](https://docs.expertflow.com/getMe) eg.[](https://api.telegram.org/botBF34Ds7dFD/getMe)<https://api.telegram.org/bot>BF34Ds7dFD/getMe  
\- Replace <telegram-botToken> with your actual telegram bot token. forgot your bot token ? click [here](https://expertflow-docs.atlassian.net/l/cp/F0N8NuZY)  
\- Once you call the above API, you will receive a response containing your bot id.   
This id highlighted in red from the response below will be placed in your**service identifier** field.   


{ "ok": true, "result": { "id": 7747304660, "is_bot": true, "first_name": "test", "username": "test_bot", "can_join_groups": true, "can_read_all_group_messages": false, "supports_inline_queries": false }}  
---  
  
  4. Select the default bot from the **Bot ID** drop down values. It could be named as "EF-Bot".
  5. Select "Telegram Channel Connector" that we created in previous step in **Channel Connector** field.
  6. **Customer Activity Timeout** can be set as 180 seconds.
  7. **Channel Mode** can be used as default value. i.e. HYBRID.
  8. **Agent Selection Policy** field value can be used as default value. i.e. LONGEST AVAILABLE.
  9. **Agent Request TTL** can be set as 100 seconds.
  10. Routing Mode can be selected as **PUSH** or **PULL.** Based on this selection, you can select the **Queue** or**List** in the next field value.



### Webhook Registration

  1. Make a **POST** rest API call to one of the exposed API's in telegram connector. **< FQDN>**/telegram-connector/register-webhook. see example [here](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-7cd66254-4e75-434b-9340-0239c2a8ddc6).
  2. Configure the request body as shown below. Example  


{  
"**botToken** ":"4892363233:WEMWDEfwefwe43New9-qghSwA",  
"url" : "<https://example.com>"  
}  
---  
  
  3. On the url set it to the fqdn of the machine that you are running telegram. **NB**. only https urls are supported. eg <https://helloworld.com>
  4. Provide a valid [bot token](https://expertflow-docs.atlassian.net/l/cp/F0N8NuZY) while registering.
  5. Once you send the request, you will receive a response 200 Ok as below only when the registration is successful.

**{**** "ok": true,**** "result": true,**** "description": "Success",**** "errorCode": null,**** "status": "OK"****}**  
---  
  



After completing the steps above, The telegram connector is able to receive and send messages to and from telegram users.

You can now search the name of your bot in telegram search bar and start a chat.  
![](attachments/2526699/2558147.png?width=476)

  


  

