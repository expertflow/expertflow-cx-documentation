# CX Knowledgebase : Priority Routing and Routing Re-initiated Chats on Priority

## **Route re-initiated chats on priority to Agents**  
  
### **Context:**

As a customer, If my chat has been disconnected abruptly just because I couldn't answer in time (due to some distractions) and I started the chat again, my chat should be routed on priority.As a manager, I would like to the chat of those customers to be routed on priority who have re-initiated the chat on the same day and whose chats have been queued to the same queue. For example:  
Customer Alex has started a chat and is routed to the sales queue, his chat was started on the 25th of Feb, 10:55 am and the chat ended at 11:03 am. If Alex starts the chat again, the system should check if his previous chat was within the same day (24 hours time) and whether that chat was on the sales queue. If yes, the chat should be given the priority. If 24 hours time has passed, or the queue is not the same one, the chat should be treated with normal priority, waiting in the queue.

### **Steps to set the re-initiated chat feature:**

  1. **Configure Bot Action**

     1. To route an INBOUND request to an agent, FIND_AGENT action is dispatched from the bot.

     2. `bot_actions_dispatcher.py` in the actions directory is configured to dispatch the FIND_AGENT action.

     3. The data within the body of the FIND_AGENT action contains the parameter 'isReinitiated '.

     4. In order for this feature to be activated, this parameter must be set to 'True'. Otherwise this feature won't be active.

     5. As of now, this parameter is set only for Premium customers. 

     6. In case you want to configure it as per your requirements, edit the bot_actions_dispatcher.py file.

     7. After updating the file, create the docker image of rasa-bot and push it to the expertflow image registry.

        1. For that, you should have docker setup.

        2. Navigate to the actions directory and run the following commands to build and push the docker image.
[code] docker build . -t gitlab.expertflow.com:9242/cim/cim-rasa-bot:<image-tag> // to build the docker image
               
               docker push gitlab.expertflow.com:9242/cim/cim-rasa-bot:<image-tag> // to push the docker image
[/code]

  


        3. This will create the image in the root container registry of cim-rasa-bot repository.

        4. Now go to the deployment instance, navigate to cim-solution/kubernetes/external/rasa-x/ and set the image tag for '[gitimages.expertflow.com/cim/cim-rasa-bot](http://gitimages.expertflow.com/cim/cim-rasa-bot)' in the file 'values-small.yaml'.

        5. Save the changes and then run the following command to deploy rasa-bot after navigating to cim-solution/kubernetes.
[code] helm  upgrade --install=true --wait=true --timeout=10m0s --debug   rasa-x    --namespace rasa-x     --values external/rasa-x/values-small.yaml  external/rasa-x
[/code]

  


  2. **To test the feature:**

     1. start a chat with the highest priority label customer, conversation-manager will check if the conversation exists on the same queue within last 24 hours. If so, the chat will be routed with priority = 10.

     2. You can verify the logs of conversation-manager as well. It receives the data field from the bot which has the 'priority' and 'isReinitiated' flag. If the latter is set to 'true', this implies that the route re-initiated chats on priority feature is active. 

![](attachments/1340867/1340893.png)


