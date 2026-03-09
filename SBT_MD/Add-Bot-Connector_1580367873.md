# CX Knowledgebase : Add Bot Connector

Make sure that your bot is trained with the essential training data (or is up with the default bot training) to handle self-service customer requests. 

You must have a bot configured in the system to start creating new channels. 

To learn more about Bot-controlled conversations, see [Conversation Studio](https://expertflow-docs.atlassian.net/wiki/spaces/CXDOC/pages/75503829/Understanding+Conversation+Studio). To learn more about Bot training, see [Custom Connector-Bot Communication](Custom-Connector-Bot-Communication_2527859.html)

![image-20251218-090035.png](attachments/1580367873/1580433409.png?width=659)

Expand the **Rasa** type and click, **Add Bot** to add the default bot.

**Field**| **Description**  
---|---  
**Bot Name**|  Specify a name to be given to the bot.   
**API URL**|  Enabled only if the Bot Type is **Rasa** or **Custom**. Provide the URL where the default bot connector is running._Example:_ `http://server-ip:30800`  
  
If a Bot Connector is being used with a Channel or anywhere else, the system does not allow to delete such a Bot until this association is removed.
