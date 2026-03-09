# CX Knowledgebase : SLA Calculations

**Case**| **Impact**  
---|---  
  
  1. If a conversation is routed to an agent within the SL threshold and the agent accepts (whenever it is accepted)

| chats_offered =1 chats_answered=1chats_abandoned = 0service_level_offered = 1 service_level_answered = 1service_level_abandoned= 0  
  
  2. If a conversation is queued, the customer abandons before it got routed to the agent and before the SL threshold expires

| chats_offered =1 chats_answered=0chats_abandoned = 1service_level_offered = 1 service_level_abandoned = 1service_level_answered =0  
  
  3. If a conversation is queued, routed to an agent within the SL threshold but the customer abandoned before the agent accepted

| chats_offered = 1 chats_answered=0chats_abandoned = 1service_level_offered = 1 service_level_abandoned = 1service_level_answered =0  
  
  4. If a conversation is queued, routed to an agent after the SL threshold but the customer abandoned before the agent accepted

| chats_offered =1 chats_answered=0chats_abandoned = 1service_level_offered = 0 service_level_abandoned = 0service_level_answered =0  
  
  5. If a conversation is queued, routed to an agent after the SL threshold and the agent accepted

| chats_offered =1 chats_answered=1chats_abandoned = 0service_level_offered = 0 service_level_abandoned = 0service_level_answered =0  
  
  6. if the conversation is routed to an agent after the SL threshold, the agent does not accept (RONA)? 

| chats_offered =1chats_rona =1chats_answered=0chats_abandoned = 0service_level_offered = 0 service_level_abandoned = 0service_level_rona=0service_level_answered =0  
  
  7. If the conversation is routed to an agent within the SL threshold, the agent does not accept (RONA)? 

| chats_offered =1chats_rona =1chats_answered=0chats_abandoned = 0service_level_offered = 1 service_level_abandoned = 0service_level_rona=1service_level_answered =0  
  
  8. If the conversation is queued, but no agents were available (all agents are busy)

| chats_offered =1chats_rona =0service_level_rona=0chats_answered=0chats_abandoned = 0**NoAgentAvailable =1** service_level_offered = 0 service_level_abandoned = 0service_level_answered =0
