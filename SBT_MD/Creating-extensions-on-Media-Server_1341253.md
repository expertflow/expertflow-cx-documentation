# CX Knowledgebase : Creating extensions on Media Server

  * Login to Media Server web interface. 

    * Open in browser: [**https://IP-addr**](https://IP-addr), where **IP-addr** is the IP address of the server that Media Server is deployed on.


![](attachments/1341253/87621806.png?width=408)

  * Add the **username** and **password** that was shown upon [installation of ](Media-Server-Deployment-Guide_1344451.html)Media Server and press **LOGIN**.

  * Press the IP address in the top right and select the Domain created in the [configuration document](75825154.html):


![](attachments/1341253/87621811.png?width=1010)

  * Open the Extensions section under the Accounts tab.


![](attachments/1341253/87621832.png?width=994)

  * Press the **ADD** button.


![](attachments/1341253/87359630.png?width=982)

  * Add a number in the **Extension** field e.g. 4000.


![](attachments/1341253/87621847.png?width=994)

  * Scroll down to the **Record** option, select the **All** option and press the **SAVE** button in the top right.


![](attachments/1341253/87621864.png?width=986)

  * Also note the Call Timeout field, which is used to set how long calls will ring on this extension before timing out. Changing this affects the RONA (Re-route on no anwer) timer when using the extension with EF CX Voice agents.


![image-20240312-081403.png](attachments/1341253/160661505.png?width=1182)

  *   * Re-open that **Extension** created e.g. 4000, change the **Password** field value to a password of your choice and press the **SAVE** button in the top right.


![](attachments/1341253/88047685.png?width=1025)

For multi-tenant (domain-based) setups, extensions must be created within their respective domains.  
For example, if CX has two tenants — **mtt01** and **mtt02** — create agent extensions under the corresponding domain for each tenant.
