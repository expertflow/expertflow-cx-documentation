# CX Knowledgebase : Scheduled Activities

### Scheduler API

A scheduled activity is an activity that is scheduled to be executed for a later date/time. Activities that are scheduled with a customer ultimately become a part of CX activities to give a complete, 360-degree view of the customer activities (both past and future) to the customer service representatives.

The Scheduled Activities API allows third parties to push activities to be scheduled with a certain date/time via certain channel so that, when the time reaches, the Scheduler executes the activity and pushes the activity results on a registered webhook. Scheduled activities are also pushed to CX Activities with updated activity status (such as Scheduled, Delivered, Failed, Connected).

On the AgentDesk, agents can see all past as well as scheduled upcoming activities on the Customer Activity Timeline view.

For more details to the API, see [Scheduler API ](https://api.expertflow.com/#a6e51948-0ff3-4817-a91e-3c452d7df028)

### Sample Flow

Below is the summary of the flow from scheduling an activity via Digital Marketing tools such as EFCX Campaign Manager solution 

  1. An activity is scheduled by calling exposed scheduler APIs

  2. Scheduler pushes the scheduled activity to CX Activities for it to become a part of customer activities

  3. Scheduler queues the activity and pushes it to CX Channel Manager when the scheduled date time reaches.

  4. CCM acts as a proxy and forwards the scheduled message to the relevant channel connector based on the activity channel specified in the API.

  5. When the activity is delivered, CCM sends back a delivery notification received from the relevant connectors, back to the Schdeuler

  6. Scheduler pushes back the delivery notification to CX Activities

  7. Scheduler also pushes it to the webhooks specified in the API call.

  8. If the scheduled activity was a chat message, CCM sends the delivery notification as READ once the customer has read the message or, replied to the scheduled message. Also, if there was a response to the message, it also sends back the customer response received from connectors to Scheduler.

  9. Scheduler pushes the READ delivery notification as well as the customer responses of the scheduled activity to CX Activities.

  10. Scheduler also publishes the delivery notifications and customer response to the Campaign Manager via the registered webhooks.




## Scheduler Features

See <https://expertflow.aha.io/epics/EFCX-E-4> for a detailed feature list implemented under the epic. 

**Feature**| **Description**  
---|---  
Scheduler API| Schedules an activity via any channel to any customer channel identifier  
Delivery Notifications| 

  1. Support to receive delivery notifications at Scheduler from channel connectors (such as delivered, failed) and the ability to send it back to EFCX Activities

  
Scheduled Activities in CX ActivitIes| Push a scheduled activities to CX customer activities  
Scheduled Activity with a named agent or queue| Provision to create a scheduled activity with a named agent  
Webhook Registration API| (POST, Get, Delete) - to be able to send delivery notifications on a 3rd party webhook  
Delete a scheduled activity| Allows to remove an already planned activity  
Update a scheduled activity| Allows to update a scheduled activity such as the time of schedule 
