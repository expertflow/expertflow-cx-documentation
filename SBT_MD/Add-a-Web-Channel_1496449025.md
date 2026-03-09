# CX Knowledgebase : Add a Web Channel

The Web Channel is a communication medium that allows customers to interact with your business directly through a conversation widget (also known as the **Customer Widget**).  
The Web Channel serves as the bridge between the **frontend chat interface** on your website and the **backend CX system** that manages conversations, routing, and agents availability.

This allows customers to interact with virtual assistants or live agents seamlessly, ensuring timely support, consistent conversation continuity, and an improved overall customer experience.

Follow these steps to set up a web channel in CX. 

### Step 1: Set Up a Web Channel

Before configuring the web channel make sure that

  * Your bot is trained with the essential training data (or is up with the default bot training)




Learn more about bot training here. 

[Unified Admin Guide](Unified-Admin-Guide_2524407.html#Step-1%3A-Add-Bot-Connector)

### **Select the Channel Type**

When creating a new channel, the first step is to select the channel type.  
You can find this option inside the Channel Manager section of the Unified Admin.

The channel type defines the **medium of communication** between customers and your CX system.  
You can choose from multiple options, such as:

  * **Facebook** – for Messenger-based interactions

  * **WhatsApp** – for WhatsApp business integration

  * **Web** – for web chat widgets (used for browser-based chat)




Since we’re embedding a **Web Widget** , select Web as your channel type.

Now click on the **New Channel Type** button.  
You’ll be prompted to enter:

  * **Name** – give your channel a clear, descriptive name (for example, `Web`).

  * **Media Routing Domain (MRD)** – from the dropdown, select **Chat**.




This tells the CX routing engine that this channel will handle **chat-based interactions** rather than voice or social media messages.

### **Channel Provider**

The Channel Provider represents the backend service responsible for handling communication between CX and the external platform (for example, Facebook or WhatsApp).  
For a Web Channel, the provider is the **Web Connector** , which connects the widget with the backend messaging service.

To locate the **Provider Webhook URL** :

  1. SSH to you server and run the following command to list all services in the CX namespace:
[code] kubectl get svc -n expertflow
[/code]

  2. Identify the **connector service** (for example, `ef-cx-web-channel-manager-svc`).

  3. Copy the service URL and port — this forms the **Webhook URL**.

     * This is the endpoint through which the CX system receives events or messages from the web widget.

     * Example:
[code] ef-cx-web-channel-manager-svc:<port>
[/code]

  4. Ensure that this URL is accessible and exposed properly — this is where the connector listens for incoming communication.




### **Channel Connector**

After defining the provider, you must configure the **Channel Connector**.

In simple terms:

  * The **Provider** defines the _structure_ (what fields are needed).

  * The **Connector** provides the _actual values_ for those fields (like webhook URLs, tokens, or credentials).




Fill in all required parameters as per your connector definition.  
These details ensure smooth message exchange between your web widget and the CX backend.

## **Creation of the Channel**

Once the connector has been created, the next step is to add the actual communication channel.  
This channel acts as the main route for all customer conversations between the web widget and the CX platform.

Follow the steps below to configure your Web Channel inside Unified Admin.

In the Unified Admin interface, go to the **Channel** section.  
From the list of available communication types (for example, Web, WhatsApp, Facebook, etc.), expand the**“Web”** section.  
Then click on **Add New Channel** to create a new Web Channel.

In the new channel form, fill out the following details carefully:

  * **Channel Name** – Give your channel a clear and descriptive name.  
For example, `Web Channel`, `Customer Support Web`, or any naming convention your team follows.

  * **Service Identifier** –  
This is a **unique numeric value** that identifies your web channel.  
The entire communication flow between the widget and CX will rely on this identifier.

🔹 _Tip:_ The Service Identifier must be numeric and unique across all channels.

  * **Calendar (Optional)** –  
You can associate an existing **calendar** if you want to define specific operating hours that appear in the web widget. By default, None is selected in the Calendars drop down if you don’t want to show the business hours.




Learn more about Business Calendars in this guide. 

[Business Calendars](Business-Calendars_687244862.html)

  * **Bot ID** –  
Enter the **Bot ID** that was created earlier during bot configuration.  
This step is mandatory if your channel involves a bot (for example, Rasa or Dialogflow).

  * **Channel Connector** – link the Channel Connector you configured earlier.  
This ensures the channel uses the correct backend service for message routing and integration.

Select your connector from the dropdown list.




> 🔹 _Example:_ If your connector was named `WebConnector_Main`, select it here.

  * **Customer Activity Timeout** –  
The **Customer Activity Timeout** defines how long a chat session remains active when the customer is inactive.

For example, if this value is set to `300` seconds (5 minutes), the widget will automatically close the chat session if no messages are exchanged within that time.

  * **Channel Mode** –  
Next, select the **Channel Mode** according to your communication strategy.  
This determines how the system handles conversations between bots and agents.

    * Hybrid Mode – Allows both **Bot and Agent** participation.  
The bot handles the conversation first, and if escalation is needed, it transfers to a live agent.

  * **Routing Mode** –  
Defines how conversations are distributed either these are push mode or pull mode. 




Want to explore Routing Engine in detail, explore this guide for better understanding.   
<https://expertflow-docs.atlassian.net/wiki/x/F4sm>

  * **Default Queue** –  
Select the queue where new customer conversations should be routed.  
For example, `WebSupportQueue` or `GeneralChatQueue`.




Get further information how queues works and configured in this guide. 

<https://expertflow-docs.atlassian.net/wiki/x/3uom>

  * **Agent Selection Policy –**  
The Agent Selection Policy controls how CX decides which agent should handle a new request. Select **Longest Available Agent** which assigns the chat to the agent who has been idle the longest.  
This ensures balanced workload distribution among the team.

  * **Agent Request TTL (Time To Live) –**  
The **Agent Request TTL** defines how long CX will search for an available agent once a customer request enters the queue.

For example:

    * If **Agent Request TTL = 30** , the system will attempt to find an available agent for 30 seconds.

    * If no agent is found within that time, the system automatically returns a “No Agents Available” message to the customer.

This helps control response times and system efficiency.

  * **Route to Last Agent –**  
Enable this option if you want CX to route repeat customers to the **same agent** who handled them previously — provided that agent is currently online.

This setting enhances continuity and customer satisfaction, as returning users will speak with someone familiar with their past conversation.




**Next Step → Add a Web Widget**  
The next guide will show you how to **add a Web Widget** to complete this setup:

[Add a Customer Widget](Add-a-Customer-Widget_1553367051.html)

## 
