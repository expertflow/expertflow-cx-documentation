# CX Knowledgebase : Join Pull-based Requests

Enables agents to pull requests from Pull-based Lists that they are subscribed to and join a conversation.In this pull-based policy, the customer's requests land on the list instead of the queue. Agents are supposed to subscribe to the list(s) they want to join. Once the List is subscribed, they will automatically receive a new request notification on the List. They can then **Join** the request or **Dismiss** to join later whenever they are convenient.

## Subscribed Lists

All pull-based requests are parked to a **List** defined by the system administrator. If you want to receive notifications for new incoming pull-based requests, make sure that you are subscribed to the desired Pull-based Lists. 

To subscribe to a List, open the burger menu and click on the **Subscribed Lists** option.

Click on the**Manage Subscriptions** button and choose the lists to subscribe to from the dialogue box. The lists that you subscribe to will start appearing on the list view. 

To unsubscribe, choose the lists to unsubscribe from the same **Manage** **Subscriptions** dialogue and uncheck the Lists.

## Join A Pull-based Request

When a customer's request is received from the List that the agent had subscribed to, the new request notification will appear as an alert with a cross icon to dismiss the notification.

![](attachments/2528122/2563894.png?width=1796)

In the notification, the identified customer name (or Jane Doe if anonymous) will be shown along with the name of the List on which the request was received. Click the cross icon to dismiss the notification. It won't disappear automatically unless the agent close it.

To join the conversation, go to the Subscribed Lists and open the List mentioned in the notification. On the **Inbox** view, hover the mouse over the request that needs to be joined. Click on **Join.**

#### Inbox View

![](attachments/2528122/2563878.png?width=680)

See the following table to understand the different columns on the **Inbox** view.

**Field**| **Description**  
---|---  
Status| This shows the current state of a request state. A Pull-based request can be in one of the following states; i.e.

  * RED (UNREAD) - until no agent has joined it
  * GREEN (ACTIVE) - when at least one agent is working on it
  * GREY (INACTIVE)- when no agent is currently working on this request. However, at least one agent joined this request earlier and left without closing it.
  * CLOSED - when the request is closed. Closed requests do not appear on the Inbox View. 

  
Customer| In this column, the following information is displayed to help understand agents about the customer:

  * Channel Type - it could be WhatsApp, Web, Facebook depending upon the channel used by the customer to initiate the request 
  * Customer Name - If identified. If not identified, this displays Jane Doe (or whatever is the value of the **First Name** attribute defined in Customer Schema by the administrator)
  * Channel Identity - This is the customer's identity that was used to initiate the conversation and to look up the customer. It could be the customer's WhatsApp number, Facebook ID, etc. 

A  _Joined_ text in green is displayed next to the customer info to show that this conversation is already joined by you.  
Time| This column shows when the request was received - (how much time ago)  
List| This is the name of the List on which the chat landed.  
Filter| Requests can be filtered in two ways:

  * Status wise (active, inactive, unread)
  * List wise (all subscribed lists are shown in the dropdown, choose a list to see only requests on that list)

  
  
On the Inbox, the latest chat will appear at the bottom of the list by default.
