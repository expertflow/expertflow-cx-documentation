# CX Knowledgebase : Key Reporting Metrics

**Handled Conversation**|  A conversation is set to be "Handled" when the disposition of the last task in the conversation is set to CLOSED, with reason code DONE.   
---|---  
**Abandoned Conversation**|  A conversation is considered as abandoned when the customer leaves while waiting in the queue or on ringing (agent alerting). In this case, the agent task in the conversation will be closed with the state CLOSED, with reason code CANCELLED.  
**Service Level Agreement % (SLA%)**|  Service level measures the percentage of incoming conversations that an agent answers within the specified Service Level (SL) threshold defined in the queue configurations. The service level threshold timer starts as soon as the conversation is queued to a precision queue. The service level threshold is the number of seconds you set as a goal for connecting a conversation with an agent. For example, your goal might be to answer 80% of conversations within two minutes. In this case, you would set the service level threshold to 120 seconds. Reports show you the percentage of conversations that are answered within that time threshold, enabling you to see whether you are meeting your goal.  
**AnsweredWithinSL**|  When a conversation is queued and accepted by agent **within** SL threshold, it is said to be answered within the Service Level.  
**AnsweredAfterSL**|  When a conversation is queued and accepted by agent **after** SL threshold, it is said to be answered after the Service Level.  
**AbandonedWithinSL**|  When a conversation is queued and gets abandoned **within** SL threshold,, it is said to be abandoned within the Service Level.  
**AbandonedAfterSL**|  When a conversation is queued and gets abandoned **after** SL threshold,, it is said to be abandoned after the Service Level.  
**OfferedWithinSL**|  The sum of AnsweredWithinSL and AbandonedWithinSL is said to be offered within SL.  
[**Service Level calculations**](SLA-Calculations_2525629.html)|  The calculations for service level are based on the **Service Level Type** defined in the queue configuration. There are three possible Service Level Types:

  * 1 - Ignore Abandoned Conversations : AnsweredWithinSL / (TotalOffered – AbandonedWithinSL) 
  * 2 - Abandoned Conversations have Negative Impact : AnsweredWithinSL / (TotalOffered)
  * 3 - Abandoned Conversations have Positive Impact : (AnsweredWithinSL + AbandonedWithinSL) / TotalOffered


