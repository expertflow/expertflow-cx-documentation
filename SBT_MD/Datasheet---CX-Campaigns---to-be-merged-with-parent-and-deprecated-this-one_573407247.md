# CX Knowledgebase : Datasheet - CX Campaigns---to be merged with parent and deprecated this one

**Outbound**  
  
Expertflow CX Outbound provides tools to design, execute, and monitor multi-channel outbound communication campaigns, enabling outreach to contacts via calls, SMS, WhatsApp, and other digital channels. A key aspect of the solution is ensuring compliance through features like robust contact validation against internal and public Do Not Contact (DNC) lists. The system utilizes **Conversation Studio** , a flow-based interface for configuring outbound interaction logic without requiring traditional programming. Core to this are the **Seize** , **Wait** , and **Init** nodes, which control agent and communication port allocation and the controlled initiation of customer interactions for campaign effectiveness. 

**Feature Name**| **Description**  
---|---  
Multi-channel Campaign Management| Support voice, and digital channels to connect through the customer’s preferred channel: SMS, WhatsApp, Telegram, Facebook Messenger or Voice calls.  
Campaign Flow in the Conversation Studio| Designs and manages campaign flows in Conversation Studio, enabling visual mapping and automation of customer interactions throughout the campaign.

  * [**Conversation Studio**](https://expertflow-docs.atlassian.net/l/cp/ok4XTZrc)**:** Use drag-and-drop elements (nodes) to create customized interaction sequences that guide customers through specific touchpoints (e.g., call > follow-up SMS).
  * **Dynamic Decision Points:** Incorporate decision nodes into the flow, enabling the system to trigger different actions based on customer responses or call outcomes.

  
Dialing modes| 

  * **EFCC** currently supports Progressive Dialing:
    * **Progressive Dialing** places one call for every one available agent. In the current version, the user cannot set the dialling ratio. It is set at 1:1 (one call per available agent). 
  * **Cisco CC:** You can link your Cisco campaign to the Conversation Studio and setup either in preview, predictive or progressive mode.

  
Campaign Contacts | Manage and import contact list. 

  * **Import capabilities:** Upload CSV files with support for multiple uploads. The system can handle up to 50,000 contacts per upload.
  * **Contact attributes:** You can use our pre-defined contact attributes to segregate/ group contacts, listed [here](As-a-Campaign-Manager_308510727.html#Contact-CSV-Upload%3A).
  * **Custom fields:** You can use our custom fields configuration if there is a need for additional contact attributes.

  
Campaign Controls | Campaign control allows you to tailor your campaign based on specific business needs. The user can:

  * Publish / Unpublish the campaign.
  * Edit the campaign.
  * Delete / End the campaign.

  
Integration with Cisco Dialer| Integrates with Cisco Dialer, enabling outbound campaigns to fully leverage Cisco’s dialing capabilities.  
Reporting| Provides a comprehensive suite of reports designed to provide detailed insights into outbound campaigns. Supervisors can monitor the performance of outbound campaigns in real-time. The dashboard offers insight into key metrics such as call completion rates, agent performance, and customer feedback. 

  * Advanced reporting tools allow historical data analysis to improve campaign strategies. 
  * These reports can be customized based on specific organizational needs, offering detailed insights into customer interactions and feedback.

  
  
### **Future Enhancements**

  * Using CX Customers, enable advanced filters, segments/saved filters and bulk customer import with contact deduplication. 

    * Compliance with local telemarketing regulations and Do Not Contact (DNC) lists.

  * Improvements on the Schedular (delete multiple scheduled activities, scheduling of executed activities)

  * The ability to duplicate a Campaign and its strategy.

  * Validity

    * Days of the week

    * Date Range

    * Start and end time

  * Email Campaigns 



