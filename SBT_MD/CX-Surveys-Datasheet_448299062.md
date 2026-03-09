# CX Knowledgebase : CX Surveys Datasheet

This page provides the business features of our CX Survey Solution. 

**Feature Name**| **Description**  
---|---  
**Survey Form**|  Allows the creation of customized [survey form](Web-Published-Forms_392298524.html) with various question types, including NPS (Net Promoter Score), 5-star ratings, multiple-choice questions (MCQs), Boolean (Yes/No options), and input fields. Survey Designers can also attach audio prompts to each question for IVR.

  * These survey forms are available for all digital channels and third-party applications (Cisco voice channel).

  
**Survey Distribution via Digital Channels**|  Distributes surveys as URL messages on all digital channels (Web Chat, SMS, WhatsApp, and Viber) and voice channels. These surveys can be triggered by specific events, such as conversation inactivity or when all agents leave the chat, etc. The survey URL directs customers to a web form where they can submit their responses.

  * Surveys are subject to conditions such as avoiding repeat surveys within a certain time, adhering to specific time frames for survey distribution, and limiting the total number of surveys sent within a 24-hour period.

  
**Survey Execution via an IVR**|  Surveys can be conducted through an IVR (CX Voice) using the attached audio prompts. These surveys can be triggered by specific events in the call flow, such as call end, agent disconnection, or predefined call outcomes. They are compatible with Expertflow Contact Center (EFCX) and *limited support for Cisco IVR Surveys using SDKs.

  * Audio prompts guide respondents through the survey, ensuring clear and consistent data collection.
  * Integration with IVR systems enables voice-based feedback collection alongside digital channels.

  
**Survey Message Node in the Conversation Studio**|  The [Survey Message Node](https://expertflow-docs.atlassian.net/wiki/spaces/CXDOC/pages/1351025594/Survey+Message) allows Conversation Designers to embed surveys into any stage of a customer interaction. Surveys can be triggered automatically based on predefined conditions, such as when a conversation is marked as inactive. Surveys can be delivered as a full web form via a URL or as individual questions presented sequentially as structured messages (roadmap).

  * Decision-making logic can be applied after each question in structured messages. This allows the conversation designer to send the next question based upon the response of the previous question.

  
**Form Submission and Data Handling**|  Survey responses are stored as both Conversation Data and as a Conversation Activity. This allows agents and supervisors to view all survey results. Multiple submissions are recorded as separate entries, ensuring that all feedback is captured and stored in the conversation record.

  * Streamlines data collection and reporting processes, ensuring all feedback is accounted for.
  * Facilitates accurate reporting and analysis by maintaining a detailed record of all submitted surveys.

  
**Reporting**|  The solution provides essential reporting that allow businesses to analyse survey data effectively. Reports can be generated to check customer satisfaction, track the performance of agents, and analyse trends over time. These reports can be customized based on specific organizational needs, offering detailed insights into customer interactions and feedback.  
To know more about our available reports, refer to [Survey reports](Reports-and-Analytics_2526384.html#Survey-Reports) document.
