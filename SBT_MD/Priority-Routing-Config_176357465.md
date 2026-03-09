# CX Knowledgebase : Priority Routing Config

## **Priority Routing to agents**

### **Context:**

As a manager, I would like to route customer requests to agents based on the customer's status, so that for those customers, the requests can be transferred to relevant queue on priority, thus bypassing the queue waiting.

  * When a customer has been successfully identified, using the relevant interaction data the system must determine whether the interaction has a specific label/tag.

  * If the customer has a label, his/her priority level must be passed to the Precision Queue/Routing Engine to skip the queue waiting based on the priority and be allocated to the next available consultant.




### **Step to set the priority routing feature:**

  1. **Configure Bot Action**

     1. To route an INBOUND request to an agent, FIND_AGENT action is dispatched from the bot.

     2. `bot_actions_dispatcher.py` in the actions directory is configured to dispatch the FIND_AGENT action.

     3. We have configured the priorities based on the customer label. Right now the priorities are as:

        1. 'Premium' : 10

        2. 'Gold' : 8

        3. 'Standard' : 6

     4. We can configure the priority here as per our requirement.

     5. This priority is then passed as the parameter in the body for the FIND_AGENT action.

     6. If you want to configure the priorities, edit the bot_actions_dispatcher.py file.

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

        6. For more details related to bot actions and communication please read:

           1. [RASA Connector Bot Communication.](http://RASA)

           2. [RASA Bot Training.](https://docs.expertflow.com/display/CIMT/Rasa+Bot+Training)

  2. **Configure labels on Agent Desk**

     1. Create labels in Agent Desk. Currently we have set 'Premium', 'Gold', and 'Standard'.

![](attachments/176357465/176062853.png?width=250)
     2. Assign these label to a customer you can assign one or more than one labels to a single customer 

![](attachments/176357465/176062859.png?width=70)

     3. if customer has no label then it's priority will be 1, which is the default priority.

     4. If a customer has any label from the specified labels then the priority will be as follows:

        1. Premium = 10, Gold = 8, Standard = 6

     5. If multiple labels are assigned to a single customer then the highest priority label will be considered for routing the chat to the agent e.g If a customer has 'Premium' and 'Gold' at the same time then the customer priority will be '10' which is the highest priority label among others.

  3. **To test the feature**

     1. Start a chat with a customer having any label assigned.

     2. The request will be routed with the priority based on the assigned customer label.



