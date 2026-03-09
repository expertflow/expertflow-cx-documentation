# CX Knowledgebase : Customer Inactivity SLA

Indicates the time limit in seconds that the customer has responded to the agent within the specified duration.   
  
The system starts the countdown of the customer SLA timer as soon as the agent sends a message to the customer.

In case of lack of customer response till the end of the timer, the conversation controller sends a channel session ended event and the conversation is over.

The system supports defining different thresholds to send reminders or take necessary actions.. For example, 3 thresholds can be added: 50%, 80% and 100% of the customer activity timeout. After every threshold , an action can be taken like notifying the customer on the first couple of threshold, and end the conversation on the last one when the time is over. 

## How to Setup Customer SLA

  1. **Configure the Customer SLA time on Channel**

     1. Login to unified Admin.

     2. Go to the Channel tab.

     3. Select the desired channel and edit the Customer Activity Timeout (It should be in Seconds).




![image-20240505-122931.png](attachments/246743058/246580514.png?width=683)

  2. **Defining Thresholds:**

     1. The customer SLA feature is implemented to take action based on the configured thresholds.

     2. A POST API on Conversation-Monitor is exposed to configure threshold values.
[code] POST    {{conversation-monitor-url}}/customer-sla-thresholds
[/code]



  1. For internal usage, you can refer to [this](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/folder/21457238-7a6a0ca2-b84e-4284-87d1-c3d6427b918b?ctx=documentation) EF Postman collection.

  2. Please **NOTE** that at the moment the system does not have any front-end implementation for customer sla.




**View Thresholds:**

You can also view the configured Customer SLA thresholds. For this, another API is exposed on Conversation-Monitor

  1. 
[code]GET    {{conversation-monitor-url}}/customer-sla-thresholds
[/code]




**Delete Thresholds:**

To delete existing thresholds in the system, call the same create thresholds API with an empty list object as the body just like below:
[code] 
    Endpoint: POST {{conversation-monitor-url}}/customer-sla-thresholds
    Body:
    [
    ]
[/code]

In case no thresholds are defined in the system, the agent sla will run for the complete duration specified on the queue/list without any intermediate action

  3. It is important to know that CCM can understand 2 actions sent from the conversation controller for now: Send notification/reminder message to customer or end channel session.




In case if no thresholds are defined in system, the customer SLA will run for the complete duration specified on the channel config without any intermediate action. 
