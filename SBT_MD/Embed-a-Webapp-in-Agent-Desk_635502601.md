# CX Knowledgebase : Embed a Webapp in Agent Desk

Enables agents to switch to third-party applications by simply switching tabs in the **Conversation View**

Depending upon the scripting, the EFCX Controller may also suggest multiple applications that can be opened within the conversation view. See the details to [embed a Web Application](/wiki/pages/createpage.action?spaceKey=CX&title=Embed%20a%20Web%20Application)

![3rd party embedding-numbered.png](attachments/635502601/635437106.png?width=895)

While in the conversation view, you can view the following options, as per the illustration above.

![\(blue star\)](images/icons/emoticons/72/31-20e3.png) Embedded browser tab (an iFrame)

![\(blue star\)](images/icons/emoticons/72/32-20e3.png) Conversation Panel 

![\(blue star\)](images/icons/emoticons/72/33-20e3.png) Button to hide/show the Conversation Panel 

![\(blue star\)](images/icons/emoticons/72/34-20e3.png) Button to hide/show the Third-party Panel 

Agents may choose to maximize the Conversation Panel (activities timeline), maximize the Third-party Application Panel by hiding the Conversation Panel or show all panels to be viewed side-by-side as illustrated in the screenshot above. 

When a conversation lands, the agent will by default, see the Third-party Application panel in a maximized view, with the Conversation Panel hidden. However, it can be shown alongside the third-party panel by clicking on the Conversation Panel button.

**Limitations**

  * As these external apps are embedded in the **Conversation View** , in case of having multiple conversations on the Agent Desk, every conversation may have various app openings suggested by the controller. Therefore, the external applications will follow the life cycle of the conversation view; i.e. if the user switches from one view to another or jumps to another conversation, the 3rd-party application will be reloaded. 

  * Any saved data or changes made to the external application will also be lost.

  * CORS support must be enabled by the third-party applications for them to be opened within the Agent Desk.

  * For now, only an application can be opened, side-by-side with the conversation. No communication layer is established back and forth for data exchange between the Agent Desk and the third-party application.

  * AgentDesk runs in Https. For any third-party applications to open up in AgentDesk, they should also be running on Https.



