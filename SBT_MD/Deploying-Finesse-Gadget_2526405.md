# CX Knowledgebase : Deploying Finesse Gadget

  1. On the CX deployment machine, get the finesse gadget file by navigating to: 

`cd kubernetes/post-deployment/3rdPartyResources/Finesse-gadget`  
---  
  
  2. Edit the _**AgentGadget.js**_ file and replace the value of _agentGadgetURL_ with your CX FQDN.   
  


![](attachments/2526405/2550938.png?width=1280)

  3. Open any FTP client and connect with the Finesse FTP Server. Add Finesse IP in the host, the user credentials(t _o be provided by the System/IT admin_).  
  
![](attachments/2526405/2550932.png?width=500)  


  4. After successful connectivity with the Finesse FTP Server, you will see the folder “files” highlighted above.

  5. Create a new folder under the file with the name “AgentGadget”.   
  
![](attachments/2526405/2550935.png?height=400)  
  


  6. Transfer all files from <cx-install-dir>/3rdPartyResources/Finesse-gadget to Cisco Finesse /3rdpartygadget/files/AgentGadget directory using an FTP client.

  7. Open finesse `cfadmin`, and navigate to the desktop layout. Add “<gadget>/3rdpartygadget/files/AgentGadget/AgentGadget.xml</gadget>”.

  8. Save the settings.

  9. Then update **the CTI config variables** added in the unified-agent/Agent desk environment variables according to the environment available by following this [doc](Environment-Configurations-for-Cisco_1021575170.html).

  10. Now log in. The agent gadget will appear.




  


  

