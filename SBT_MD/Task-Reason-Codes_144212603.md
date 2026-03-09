# CX Knowledgebase : Task Reason Codes

**Scenario**| **Task State**| **Reason Code**| **Disposition**| **Change in ETL**  
---|---|---|---|---  
  
  * Chat is active on agent
  * Agent clicks leave-conversation button
  * Agent goes in wrap-up
  * Agent clicks **leave-without-wrap-up** button

| CLOSED| DONE| `AGENT-HANDLED` | updated  
  
  * Chat is active on agent
  * Agent clicks leave-conversation button
  * Agent goes in wrap-up
  * Agent clicks **add-wrap-up** button

| CLOSED| DONE| `AGENT-HANDLED` | updated  
  
  * Chat is active on agent
  * Agent clicks leave-conversation button
  * Agent goes in wrap-up
  * Wrap-up timer expires

| CLOSED| DONE| `AGENT-HANDLED` | updated  
  
  * Wrap-Up is off
  * Chat is active on agent
  * Agent clicks leave-conversation button

| CLOSED| DONE| `AGENT-HANDLED` | updated  
  
  * Chat is active on agent
  * Agent Logout from Agent Desk

| CLOSED| AGENT_LOGOUT | `AGENT-HANDLED`| updated  
  
  * Chat is ringing/enqueue on agent
  * Customer ends chat

| CLOSED| CANCELED| `ABANDONED`| updated  
  
  * Chat is in queue 
  * Agent request TTL expires 

| CLOSED| NO_AGENT_AVAILABLE| `ABANDONED`| updated  
  
  * Chat is ringing on agent
  * Agent request TTL expires 
  * RONA expires 

| CLOSED| NO_AGENT_AVAILABLE| `ABANDONED`| updated  
  
  * Chat is ringing on agent
  * RONA expires

| CLOSED| RONA| `RONA`| updated  
  
  * Chat is in queue/ringing
  * Voice call starts

| CHAT TASK : CLOSED| CANCELED| | data segregation not available  
  
  * Chat is ringing/active with agent
  * Agent closes the browser
  * Socket disconnect time expires 

| CLOSED| AGENT_LOGOUT| `ABANDONED`| data segregation not available  
  
  * Chat is active with agent
  * Agent SLA expires 

| CLOSED| DONE| `AGENT-SLA_EXPIRED `| data segregation not available  
Unknown reason| CLOSED| null| `UNKNOWN `| updated  
  
  * Chat is active with agent

| ACTIVE| null| `AGENT-HANDLED`| updated  
  
Related Jira Issues 

[CIM-13580](http://project.expertflow.com:8080/browse/CIM-13580?src=confmacro) \- Jira returned an error: Bad Gateway 

We
