# CX Knowledgebase : Adding Agent Extensions for CX Voice

To configure the extensions available for the _**Media Server**_ for each agent,

  * Navigate to the following path for your CX deployment, https://<FQDN>/auth.

  * Select the _**Expertflow**_ realm, and navigate to _**Users.**_

  * Select the user for which the extension is to be configured.

  * Navigate to the user _Attributes_ tab.

  * Add the extension for the user as an attribute.

  * Set _**agentExtension**_ as the key and the extension as the value.  
![](attachments/2526927/2558974.png?height=175)  
  


Limtations

    * The extension will only be reflected once the user re-logins after the extension setup.
    * Only one extension is to be configured per user.
    * Same extension should not be assigned to multiple users



