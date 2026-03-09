# CX Knowledgebase : Quality Management - System Limitations

  * QM is only tested for Cisco Voice (UCCE)

  * The hardcoded agent role is automatically assigned to Cisco sync agents and supervisors.



  * Users must manually add the agents to the team on Unified Admin to include them in the **conversation list and create Scheduler view filters**.



  * Conversations will appear in the conversation list only after configuring the DN in the **Channel** section on Unified Admin. However, any conversations before configuring the DN will not be displayed.



  * For the conversation of a _**consult call**_ during an _**outbound**_ call, the consulted leg is not created, and the consulted agent's information is not visible in the created conversation. 



  * If a call is **consulted** to Agent B and Agent B **transfers** the call to Agent C, the conversation for that call will not be created.



  * In an outbound call that is **Consult/Directly** transferred, the original agent's name is replaced with the agent who becomes the primary agent of the call. 



  * The system does not support **Conference calls** , so conversations will not appear on the conversations list.



  * If an agent performs a Consult or Transfer on an inbound or outbound call using a **Queue DN** , the conversation will not be created in QM.

  * Screen recording is currently supported and tested only for **simple inbound** and **simple outbound** calls, including the **hold/resume** scenario.  
Other call scenarios such as **direct transfer, consult, consult transfer, and conference** are **not supported at this time**.



  * Calls that disconnect within a fraction of a second (e.g., 0.4s) result in conversations with a 00:00 duration. The Conversation Manager currently does not account for millisecond-level call durations.

  * Relogin on the unified admin to get the created agents in Reviews and Schedules.

  * Agents deleted in Cisco remain in CX even after the sync job, but those agents are marked as disabled on IAM (Keycloak).

  * If the IAM (Keycloak) server is temporarily unavailable, the sync job fails and only retries in the next scheduled cycle, potentially delaying updates. New data will be shown after the next scheduled sync cycle is successfully executed.

  * If a team on Cisco is created with the same name as exists on CX, the Cisco team will not be synced to avoid duplication. Ensure unique team names across both systems.

  * When a team is deleted in Cisco, it remains in CX after the sync job is executed. The system currently does not support team deletion synchronization, and this needs to be addressed in future updates.

  * QM Reports are only tested for MySQL.

  * In the Team Comparison Report, the system can not separate out questions based on the question group and the questionnaire selected.

  * The selected agent does not get clear in the filter criteria even after switching teams, and does not automatically reset or clear when the team selection is changed.

  * SSE and MS Exchange cannot operate concurrently at this time. Users must choose and configure one integration at a time.

  * Currently, we have inherited the conversation view from Agent Desk. This means that whenever something new is added in Agent Desk, we need to manually replicate it in our conversation view. If the feature is already released in Agent Desk, we can include it; otherwise, that change will not be part of the Unified Admin conversation view 



