# CX Knowledgebase : Unified Admin Guide

Unified Admin is an Admin console that configures ExpertflowCX services and solution components. 




**Table of Contents:**

  * Getting Started
    * Login
    * Upload License
    * View License Consumption
  * Feature Details
    * Master Key and Product Association
    * Accessing the License Info Page
    * Displayed Information
    * Expiry Warning Banner
  * Configuration Settings
  * Feature Limitations and Operational Considerations
    * 1\. Expiry Warning Precision
    * 2\. License Status Synchronization
    * 3\. Configuration Management
    * 4\. Product Purchase and Activation Workflow
    * 5\. Order Status Reversion Impact
    * Locale Settings
  * Provisioning the system
    * Step 1: Add Bot Connector
    * Step 2: Add Media Routing Domain (MRD)
    * Step 3: Map MRD to Channel Type
    * Step 4: Create Routing Attributes
    * Step 5: Assign Attributes to Agents
    * Step 6: Create a Queue
    * Step 7: Add Steps to the Queue
    * Step 8: Change Max Tasks Limit for Agents MRD
    * Step 9: Add Channel Provider
    * Step 10: Add Channel Connector
    * Step 11: Set up a new Channel
  * Other Configurations
    * Add Web Widget
    * Add Reason Codes
    * Add New Channel Type
    * Pull Mode - No Routing
  * Teams Configuration
    * Create a new team
    * Update a team
    * Delete a team
  * Agent Desk Settings
  * Form Builder
    * Default Wrap-Up Form
    * Pre-Conversation Form
  * Campaign Configuration
    * Create Campaign
    * Campaign Controls
    * Edit Campaign
  * Quality Management
    * Design an Evaluation Form
    * Reviews
    * Schedules
    * Create a New Schedule
    * Conversation List
    * Reviewing Conversations
    * Review Notifications






## Getting Started

Users are created and managed within Keycloak. 

At least one admin user must be created within Keycloak, with `admin` role, to use the Unified Admin application.

See [Keycloak Configuration](/wiki/pages/createpage.action?spaceKey=SBT&title=IAM%20user%20Creation%20guide&linkCreation=true&fromPageId=2524407) to see how to create users and assign roles to users.

See [Security and User Permissions -> User Authorization with Unified Admin](/wiki/pages/createpage.action?spaceKey=SBT&title=Security%20and%20User%20Permissions&linkCreation=true&fromPageId=2524407) to understand the scopes and permissions assigned to the default `admin `role.

### Login

Users can login to Unified Admin using the Keycloak username/password. Once entered, the user authentication request is redirected to Keycloak. Upon verification, the user is allowed to log in. 

![log in.png](attachments/2524407/66879525.png?width=585)

### Upload License

The application for contact center agents and supervisors works with the Concurrent-user-based licensing model that provides simultaneous access to the system to a certain number of users. 

To let agents start using and logging in to , the admin user must upload the license information to Unified Admin by going to  _General - > License Info _page. 

Two flavors of license verification are available.

See [License Manager -> Concurrent user licensing](https://expertflow-docs.atlassian.net/wiki/spaces/LM/pages/3538961/License+Manager) to understand more on how this type of licensing works.

See [License Manager](https://expertflow-docs.atlassian.net/wiki/spaces/LM/pages/3538961/License+Manager) to learn more about the flavors of license verification and key validation workflow.

#### 1) Online verification by uploading License Key

With online verification, you need to upload the license key to Unified Admin to get it verified online.

On **General → License Info** , enter the license key, also known as, the Master API key received from the Expertflow shop in the **Master API Key** field under the **Activate Online** tab, and click **Save**. 

![license info-1.png](attachments/2524407/66519142.png?width=600)

This request is then redirected to the License Manager to be verified. Upon verification, the license key is successfully uploaded.

Once saved, the uploaded key is visible from the front-end. You won't be able to change the license key. 

#### 2) Offline verification with a License File

In case of offline key verification, Expertflow allows you to upload a license file with pre-activated licenses where all license activations are pre-generated.

In this case, click the tab, **Activate Offline** to upload the license file that was downloaded locally, and click the **Upload** button. 

The request is redirected to the License Server to verify the license file. Upon verification, the licenses are stored successfully.

To know more see [Get the offline success file](Getting-the-Offline-License-Encrypted-file_66387975.html)

### View License Consumption

![](images/icons/grey_arrow_down.png)License Consumption Status

This feature allows business administrators to view license details, monitor expiry statuses, and receive proactive warnings for licenses linked to a master key.   
The License Info page now also includes [License product statuses](https://expertflow-docs.atlassian.net/wiki/x/SADDOg) and configurable expiry warnings to help admins manage renewals.

## Feature Details

### Master Key and Product Association

  * A **master key** can be associated with multiple products purchased from the EF shop.

  * Each product’s license details, including expiry status and warnings, are displayed separately under the master key.




### Accessing the License Info Page

  1. Navigate to **Unified Admin → License Info**.

  2. The system automatically displays the uploaded master key and its associated products.




### Displayed Information

Field| Description| Example  
---|---|---  
**Master License Key**|  The uploaded master key.| `MK-XXXX-XXXX-XXXX`  
**Product Name**|  Name of the purchased product.| "EF Analytics Pro"  
**Status**|  Current Order status for your product subscription. See list of possible [License Status](https://expertflow-docs.atlassian.net/wiki/x/SADDOg)| `ACTIVE`  
**Expiry Date**|  Date when the license Subscription expires. | `2024-12-31`  
**License Type**| `Concurrent Users` or `Activities`.| `Concurrent Users`  
**Purchased Licenses**|  Total licenses purchased.| `100`  
**Consumed Licenses**|  Licenses in use/activated.| `75`  
  
![Screenshot 2025-05-08 160651.png](attachments/985595918/1072431383.png?width=940)

### Expiry Warning Banner

  * A warning banner is displayed for licenses with an expiry date **within** the configured `LICENSE_EXPIRY_WARNING_DAYS` threshold.

  * **Warning Message**

 _"Your license will expire soon. Please renew to avoid any service interruption."_

  * **Conditions for Display**

    * Compares the expiry date against the current date. If the remaining days ≤ `LICENSE_EXPIRY_WARNING_DAYS`, the banner appears.

    * Example: If `LICENSE_EXPIRY_WARNING_DAYS = 60`, the banner shows when the license expires in ≤60 days.




## Configuration Settings

  * **ConfigMap Variable** : `LICENSE_EXPIRY_WARNING_DAYS` in unified-admin ConfigMap

    * **Purpose** : Defines the threshold (in days) for displaying the expiry warning.

    * **Validation** :

      * Minimum value: `30` days.

      * Maximum value: `180` days.

    * **Default** : If not configured, the system uses `30` days.

  * **Behavior** :

    * Admins can adjust this value via the platform’s configuration management.

    * Changes require a unified-admin ConfigMap and a Deployment restart to take effect.




## Feature Limitations and Operational Considerations

### 1\. Expiry Warning Precision

**Calendar-Day Calculation**

  * The expiry warning banner calculates days based on **calendar days** (not business days). Weekends and public holidays are **not excluded** from the count.

    * _Example_ : If a license expires in 30 calendar days and the warning threshold is set to 30 days, the banner will trigger immediately, even if weekends fall within that period.




### 2\. License Status Synchronization

**Manual Refresh Required for Status Updates**

  * License status changes (e.g., expiry, consumption updates) are **not displayed in real time**.

  * Users must **refresh the License Info page** to view the latest status.




### 3\. Configuration Management

**Configuration Update Restart Requirement**

  * Changes to the `LICENSE_EXPIRY_WARNING_DAYS` ConfigMap value require a **system restart** to take effect.

  * This applies to both increases and decreases in the threshold.




### 4\. Product Purchase and Activation Workflow

4.1 **Sequential Product Purchase Requirement**

  * Multiple product purchases linked to a single master key **cannot be purchased in a single transaction**. Each product must be procured individually via the EF shop.




**4.2 Agent Login Dependency for Activation Visibility**

  * Newly purchased products **do not appear on the dashboard** until an authorized agent logs into the product at least once; thereafter, license details will be displayed.




4.3 **Product-Specific Login Requirement (Excluding Testing Products)**

  * **Exception** : Testing products purchased from the EF shop are displayed immediately without agent login.

  * **All Other Products** : License details (e.g., consumption, expiry) are visible **only after an agent’s initial login** to the product.




### 5\. Order Status Reversion Impact

**Subscription Renewal Requirement**

  * If an order’s status is reverted from any state (e.g., `suspended`, `pending`) back to `completed`, the customer must **resubscribe to the subscription** via the EF shop to reactivate the license, or the Admin has to manually reactivate the subscription. Here is the [guide](https://expertflow-docs.atlassian.net/wiki/x/8QDkOg).




### Locale Settings

The locale settings allow admins to get provision of the time zone, and language settings system-wide so that each solution component shares the same locale settings wherever required. 

**Field**| **Description**  
---|---  
**Timezone**|  Select a time zone that best suits your servers' location.   
**Supported Languages**|  Choose the languages that the system should support, for instance, for rendering the UI.For now, the only supported languages include:

  * English
  * French
  * Spanish
  * Italian 
  * German 

This setting is currently only used in **Web Widget → Language** settings to show a list of supported languages for the Customer Widget UI. For the other components such as AgentDesk, the UI translation will be available in future updates.  
**Default Languages**|  Based on the supported languages chosen from the dropdown above, choose here the language which should act as a default language. For now, this is set to 'English' by default.  
  
## Provisioning the system

### Step 1: Add Bot Connector

Make sure that your bot is trained with the essential training data (or is up with the default bot training). 

**Tip**

You must have a bot configured in the system to start creating new channels. 

To learn more about Bot-controlled conversations, see [Conversation Studio - Studio Nodes](/wiki/pages/createpage.action?spaceKey=CX&title=Conversation%20Studio). To learn more about Bot training, see [Custom Connector-Bot Communication](Custom-Connector-Bot-Communication_2527859.html)

![add bot connector.png](attachments/2524407/66814006.png?width=600)

Expand the **Rasa** type and click, **Add Bot** to add the default controller bot.

**Field**| **Description**  
---|---  
**Bot Name**|  Specify a name to be given to the bot.   
**API URL**|  Enabled only if the Bot Type is **Rasa** or **Custom**. Provide the URL where the default bot connector is running._Example:_ `http://server-ip:30800`  
**Bot Config JSON**|  Enabled only if the Bot Type is **DialogFlow**.  
  
By default, Rasa Bot is supported as the controller bot with default bot training. _< give a link to the bot training>_

If a Bot Connector is being used with a Channel or anywhere else, the system does not allow to delete of such a Bot until this association is removed.

### Step 2: Add Media Routing Domain (MRD)

You can create, edit, and delete MRDs from the Unified Admin.

**Tip**

See [Precision Routing](Precision-Routing_2525641.html) to learn more about MRDs. 

The MRD for VOICE and CHAT are available by default.

To create an MRD, go to the Routing Engine menu on the left and click **MRDs**.

While creating an MRD, provide the following info:

**Field**| **Description**  
---|---  
**Name**|  Give a name to the MRD.  
**Description**|  Provide an optional description of the MRD.  
**Max Tasks Request **| Specify the maximum number of task requests that any agent can handle on this MRD. When this count reaches, the agent's MRD state will turn to `BUSY` and the agent will no longer receive any new tasks unless an active task is closed.This works in combination with the Agent-MRD tasks limit. See more in **Step 8.** Note that this limit should be greater than or equal to the task limit defined for one agent on this MRD. Therefore, if the maximum tasks count is later modified to make it lesser than an agent's individual tasks limit (during Agent-MRD mapping), an error would be thrown.   
**Interruptible**|  Reserved for future.When available, this will allow us to turn the flag to ON if the requests on this MRD are considered to be interruptible. This means that the system may interrupt the agent on this MRD (during an active conversation) to route him to a conversation from a different MRD if required.  
  
![add MRD in Uni Adm.png](attachments/2524407/66257093.png?width=600)

_Add MRD_

  * If an MRD is associated with a precision queue or with a Channel Type, it cannot be deleted until the association is removed.

  * If some conversations are already active on an MRD, it cannot be deleted.

  * MRD names are case-sensitive.




### Step 3: Map MRD to Channel Type

The next step is to map one Channel Type to the MRD created in the above step.

**Tip**

Learn more about Channel Types in [Channel related terms](Channel-Related-Objects_276594689.html)

The following channel types are available by default.

  * WhatsApp

  * Web

  * Facebook

  * Voice




To map a channel type to an MRD, expand **Channel Manager** from the left and go to **Channel Types**.

Choose a channel type to associate the MRD with. You can map one MRD to multiple channel types.

![map channel MRD.png](attachments/2524407/66257112.png?width=600)

To know how to add more channel types, jump to **Add Channel Type** section.

### Step 4: Create Routing Attributes

Agent attributes are created and assigned to agents so that customers can always get the right agent.

**Tip**

See [Precision Routing](Precision-Routing_2525641.html) to learn more about Agent Attributes.

Go to **Routing Engine - > Routing Attributes **and create a new attribute by clicking on the **Create Attribute** button, using the following table: 

**Field**| **Description**  
---|---  
**Name**|  Give a name to the Routing Attribute.  
**Description**|  Provide an optional description here.  
**Type**|  Choose from one of the following types:

  * Proficiency: Specify a default proficiency on a scale from 1 to 10.
  * Boolean: Select the default value, either `true` or `false`.

  
**Default Value**|  Specify a default value based on the type of attribute. This default value is automatically assigned to an agent when a Routing Attribute is assigned to the agent. You can overwrite the default value at the time of attribute assignment.  
  
![New Attribute.gif](attachments/2524407/2549698.gif?width=600)

### Step 5: Assign Attributes to Agents

On **Routing Engine - >** **Agents Attributes** page, all Keycloak users having specified Keycloak role(s) are shown. By default, it contains the list of agents and supervisors with Keycloak roles `agent`, `supervisor`. 

**Tip**

See [Precision Routing](Precision-Routing_2525641.html) to learn more about how agents or users are synced. 

To assign a routing attribute to an agent, hover your mouse to an agent record and click the **+** icon to assign or remove an attribute to/from the selected agent. 

![assign attributes.gif](attachments/2524407/66355402.gif?width=800)

Click the contact picture against an agent record on the **Agents List** to view the agent's profile in a read-only mode; this information is fetched from Keycloak User Profile since users are created and managed from within Keycloak.

A Routing Attribute assigned to an agent cannot be deleted.

### Step 6: Create a Queue 

Expand the **Routing Engine** menu on the left and click **Queues.**

**Tip**

Learn more about Queues on [Precision Routing](Precision-Routing_2525641.html)

On the **Queues** List, add a new queue with the basic queue details using the following table:

**Field**| **Description**| **Required**  
---|---|---  
**Queue Name**|  Specify a queue name. | ![\(tick\)](images/icons/emoticons/check.png)  
**Associated MRD**  
|  Choose an MRD you created in step 2. | ![\(tick\)](images/icons/emoticons/check.png)  
**Agent Response Time (in seconds)**|  This is when the agent has to respond to a customer message.| ![\(error\)](images/icons/emoticons/error.png)  
**Service Level Type**|  Type one of the following numbers in the field: 

  * 1
  * 2
  * 3

See more details about these in [Key Reporting Concepts](Key-Reporting-Metrics_2526622.html)| ![\(tick\)](images/icons/emoticons/check.png)  
**Service Level Threshold**|  This is the service level threshold in seconds. This determines the time until when all requests being enqueued should ideally be picked up from the queue and routed to agents to be answered. This is set by the business as per their business policies and SLA reporting requirements. If a request gets answered within this time, it is considered to be answered within SL. See more on [Key Reporting Concepts](Key-Reporting-Metrics_2526622.html)| ![\(tick\)](images/icons/emoticons/check.png)  
**EWT (Estimate Wait Time) Min Value**|  This is the minimum estimated wait time in seconds that will be displayed to the customer if the estimated wait time is below this number. The minimum value should be lesser than the maximum value.  
**Minimum Number Limit: 0 or NULL**  
**Maximum Number Limit: 2147483647**| ![\(error\)](images/icons/emoticons/error.png)  
**EWT Max Value (Estimated Wait Time )**|  This is the maximum estimated wait time in seconds that will be displayed to the customer if the estimated wait time is more than this number. The maximum value should be greater than the minimum value.  
**Minimum Number Limit: 0 or NULL**  
**Maximum Number Limit: 2147483647**| ![\(error\)](images/icons/emoticons/error.png)  
  
![create a queue with min-max value.png](attachments/2524407/273711130.png?width=795)

**Keys**| **Fields**  
---|---  
![\(tick\)](images/icons/emoticons/check.png)|  Mandatory  
![\(error\)](images/icons/emoticons/error.png)| Optional  
  
This is an option to add Minimum or Maximum Value. However, adding value in any field can calculate the value of EWT.

The EWT is currently not visible to customers, neither in web chat widget nor for any other channel. The customer-side implementation for EWT is still pending.

### Step 7: Add Steps to the Queue

Once a queue is added with the above settings, the next step is to add _Queue Steps_ in the queue. 

**Tip**

Learn more about **Steps** , **Expressions** , and **Terms** on [Precision Routing](Precision-Routing_2525641.html)

On the Queues list, click **Add Step** option**** against the desired queue to start adding steps in the queue using the following table:

**Field**| **Description**  
---|---  
**Step Timeout**|  This is the timeout for this step. It determines the time the system waits before jumping to the next step when no agent is found.   
**Expression**|  Add a logical expression for the Routing Engine to evaluate and identify an agent matching the criteria.Add the small **+** icon to add another term in the expression. Click **Add Expression** to add another expression to the same step. For instance, the expressions added in the illustration below states: Any agent having `(English== 8 AND Sales == true) OR (Science >= 5 AND Sales == true)`, is best suited to answer the request being enqueued to this queue.  
  
![Add Precision Queue.gif](attachments/2524407/65962274.gif?width=800)

To continue adding more queue steps, go back to the **Queues** List, expand the desired queue, and click **Add Step**.

If the Routing Engine finds an agent matching to the criteria as a result of the first queue step, it won't jump to evaluate the next steps. Therefore, at the point where it gets an agent available matching the criteria, it stops jumping to the next steps.

  * If there're some conversations enqueued to or active against a queue, such a queue cannot be deleted. The reason is, even if the chat request is routed to an agent, there are scenarios where it can be re-routed such as in the case of RONA. So unless all requests are closed, the queue cannot be deleted.

  * A queue cannot be deleted if it is associated with a channel.




### Step 8: Change Max Tasks Limit for Agents MRD

By default, each agent added to the system becomes a part of all MRDs with the default max tasks limit set as per the **Maximum Tasks Requests** per MRD. See **Step 2** for more details. 

To change an agent's tasks limit on each MRD, go to **Routing Engine → Agent MRDs** page. 

All MRDs that are created are listed on **Agent MRDs** along with the list of all users created in the system. By default, all agents who are added become a part of all MRDs.

Select one user to change the maximum number of tasks that the agent can handle on an MRD. The dropdown contains the max limit as per the limit defined in the MRD definition (created in Step 2). Set the limit to 0 to make an agent unavailable for an MRD. 

![agent mrds.PNG](attachments/2524407/2549658.png?width=816)

### Step 9: Add Channel Provider 

Channel providers are supported only for Web, WhatsApp via 360, and Facebook channels. 

Channel providers are used to configure the third-party vendors who will be used to send/receive messages to/from a channel. For instance, Dialog 360 and Twilio could be the two-channel providers for WhatsApp channel. 

**Tip**

Learn more about channel providers in [Channel related terms](Channel-Related-Objects_276594689.html)

To add a new channel provider, go to **Channel Manager →** **Channel Providers**.

While adding a new channel provider, provide the following information.

**Field**| **Description**  
---|---  
**Name**|  Provide a name for the channel provider such as Dialog 360 for WhatsApp.  
**Supported Channel Types**|  This setting is used to determine which channel types this channel provider will support. For instance, you could configure one channel provider to support both WhatsApp and Facebook messages. So one channel provider can be used to serve both types of channels.Based on the supported channel types, you can add corresponding channel connectors and use them while configuring new channels.  
**Provider Webhook**|  Give a webhook URL for the Channel Provider where this channel provider will listen to the events:

  * Recommended to use the service name of the component in the `Channel Provider > Provider Webhook` field. However, **FQDN** can also be used with some additional custom configurations.
  * Provide the service name of the Connector in the Provider Webhook field as `http://{SERVICE-NAME}:{SERVICE_PORT}`. Replace the `{SERVICE_NAME}` and `{SERVICE-PORT}` in the URL with the component’s k3s-based service name and port (it can be fetched using the following command: `kubectl get svc -n expertflow` )

The provider webhook URL is given in the following format:**_For Web provider_** Kubernetes based: `http://ef-web-channel-manager-svc:7000`HELM based: `http://ef-cx-web-channel-manager-svc:7000`  
** _For WhatsApp_** Kubernetes based: `http://ef-whatsapp-connector-svc:8080`HELM based: `http://cx-channels-whatsapp-connector-svc:8080`  
** _For Facebook_** Kubernetes based: `http://ef-facebook-connector-svc:8080`HELM based: `http://cx-channels-facebook-connector-svc:8080`  
  
![whatsapp.png](attachments/2524407/509607940.png?width=805)

Follow the [360-Connector Configuration Guide](360-Connector-Configuration-Guide_2531584.html) to configure WhatsApp via Dialog 360. 

See [Facebook Comment/DM Connector - Configuration Guide](Facebook---Configuration-Guide_2531616.html) for configuring Facebook Social Media.

### Step 10: Add Channel Connector 

You may create a channel connector for each new **Channel Provider** added to the system.

**Tip**

See [Channel related terms](Channel-Related-Objects_276594689.html) to learn more on **Channel Connectors**.

On the **Channel Connector** list, click the **Add New Connector** button to add a new channel connector with the help of the following table:

**Field**| **Description**  
---|---  
**Name**|  This is the name of the channel connector.  
**Channel Provider**|  Select the desired Channel Provider (created in the above step) to configure this channel connector for the channel provider. Based on the selected channel provider, you'll see the corresponding configuration attributes to be specified for this channel connector. _See the illustration below._  
**Custom Attributes**|  This shows the list of other custom attributes created while defining the Channel Provider you selected above. Available only if some custom attributes were added while defining the Channel Provider in the above step. For example, for the default Dialog 360, `HOST-URL``API-KEY`For details on Dialog 360 connector configurations, see [360-Connector Configuration Guide for WhatsApp](360-Connector-Configuration-Guide_2531584.html)  
  
![add a new channel provider.gif](attachments/2524407/66650199.gif?width=800)

  * If a Channel Connector for a particular Channel Provider exists, the system does not allow to delete such a Channel Provider until the association is removed.




Follow the [360-Connector Configuration Guide](360-Connector-Configuration-Guide_2531584.html) to configure WhatsApp via Dialog 360. 

See [Facebook Comment/DM Connector - Configuration Guide](Facebook---Configuration-Guide_2531616.html) for configuring Facebook Social Media.

### Step 11: Set up a new Channel

Add customer channels in the system to receive customer requests from relevant channels.

**Tip**

Learn more about channels in [Channel related terms](Channel-Related-Objects_276594689.html)

**Field**| **Description**  
---|---  
**Channel Name**|  Specify a channel name.   
**Service Identifier**|  This is the service identifier of the service that the customer dialed or reached. It could be a DN (Dialed Number) such as a WhatsApp number, any website URL, Facebook ID, Viber ID.   
**Bot ID**|  This is the Bot Connector that was added under Bot Settings. You need to choose a bot connector here regardless of the Channel Mode. This is because a bot is an integral part of a conversation who acts as an authoring party, monitors the conversation events, identifies intents, and takes appropriate actions (for instance, closes a chat if the customer activity timeout reaches).   
**Channel Connector**|  This is the Channel Connector that should be used to send/receive messages to/from the channel. Choose the desired channel connector created in the above step to be associated with this channel.This list is rendered based on the Channel Type.  
**Customer Activity Timeout**|  This is the time in seconds that the system waits for the customer's response against a message sent by the agent or bot. When this time reaches, the system considers the chat as inactive. The bot closes the channel session of the customer and the agent receives `Channel_Session_Ended` notification within the conversation. The message composer on the agent side is greyed out to disable sending messages.  
**Channel Mode**|  Choose a channel mode. Possible values are:

  * Hybrid: This the default mode of communication where a bot is always there to assist agents in the background (even if not conversating with the customer directly). This is the only available mode as of today. 
  * Bot: Choose this option for self-service, Bot-only conversations. Reserved for future use.
  * Agent: Choose this for requests to be routed to agents. Reserved for future use.

  
**Routing Mode**|  This determines if the channel needs to push incoming requests to a queue to be routed to agents, or, broadcast to a Pull-based List to be taken up by any agents subscribed to the List. Possible values are:

  * Push 
  * Pull 

  
**Agent Selection Policy**|  This determines how to select an agent when multiple agents match the criteria.Possible values are:

  * Longest Available: Picks the agent who's available for the longest time duration with a lesser number of active tasks. This is currently the only one supported. 
  * Least Skilled: Picks the agent who's the least skilled on the skills that are required to handle such a customer request. Reserved for future use.
  * Most Skilled: Picks the agent who's most skilled on the skills required to handle such a customer request. Reserved for future use.

This is applicable only if the channel mode selected above is other than **Bot** and the selected Routing Mode is **Push**.  
**Agent Request TTL (time-to-leave)**|  This is the time in seconds that the system waits for an agent to be assigned to a queued request. Once this TTL is elapsed, the `No-Agent-Available` event is posted to BOT.**Disclaimer:**  
Agent TTL value must be greater than RONA value.When the`NO-AGENT-AVAILABLE` event is received, the Controller takes no further action on the conversation  
**Default Queue**|  This is the default queue where requests coming on the channel will be enqueued. This is enabled only if you have selected the Routing Mode as **Push**.   
**Default List**|  This is the default list where requests coming on the channel will be published. This is enabled only if you have selected the Routing Mode as **Pull**.  
**Route to the last agent**|  Reserved for future.This setting is used to route the request to the last agent who previously handled a request from the same customer.   
  
On the **Channels** list, you can see a dropdown for each channel type defined in the system. Expand a channel type to add a new channel of this channel type. 

![add a new channel.png](attachments/2524407/65864145.png?width=800)

## Other Configurations

###  **Add Web Widget**

Web widget is Expertflow's customer chat widget that loads on the company's website when a web visitor initiates a chat.

This Web widget is loaded based upon the settings defined in **Web Widget** configurations on Unified Admin.

Business administrators can add multiple web widget instances in Unified Admin, having their own set of configurations that work independently of the other widget instances.

For instance, if have different configuration requirements for a customer portal and a partner portal, you may define two web widget instances here.

Using the Web Widget REST APIs, the relevant widget configurations can then be loaded by the chat widget based on the widget identifier.

To add a new web widget, go to Web Widget on the left, and click **Create Web Widget.**

On the **Web Widget** Settings, fill in the form using the following table:

**Field**| **Description**  
---|---  
**Widget Identifier**|  A short string defining this web-widget instance, such as, **web** , **customer-widget** , **partner-widget**(Alphanumeric code). Following validations are applied to the widget identifier.

  * All Alphanumeric characters are allowed. Alphabets (A-Z), Numbers (0-9).
  * Special characters are allowed including Esterik (*), Dashes (-) and underscores (_)
  * Maximum character length of 50 characters

  
**Widget Title**|  This is the title text shown on the customer widget. Could be a company name or any short string.   
**Widget Subtitle**|  This is the subtitle text shown beneath the title text. Could be any short string, for instance, the opening hours of the contact center.  
**Pre-Chat Form**|  Select a form of the web widget.This dropdown shows the list of pre-conversation type forms specified in **Form** Builder.  
**Customer Reconnect Time (in seconds)**|  Not applicable for now. The reconnect time in case the customer chat widget is disconnected in defined in the configuration files for now.  
**Language**|  This determines the language of the web widget. This dropdown shows the list of supported languages specified in **General Settings → Locale** settings.  
**Color Pallet**|  Choose a color of the web widget from this color pallet.  
**Download Transcript**|  If enabled, customers can download the full chat transcript at the end of the webchat.  
**Dynamic Link**|  If enabled, this auto-converts a URL to a hyperlink, whether sent by the customer or by the system (agent/bot).  
**Emoji**|  If enabled, customers can send emojis during the web chat.  
**File Transfer**|  If enabled, customers can send and receive file attachments  
**Font size**|  If the value is `true, `the widget shows 3 font size options for customers to choose from; i.e. `Large`, `Medium`, `Low`.  
  
### Add Reason Codes

Reason codes are configured for agents to select a reason while going not ready and/or logging out. 

To add a reason, go to the **Reason Codes** list and create a new reason using the following table:

**Field**| **Description**  
---|---  
**Label**|  Specify a reason label. This label will be displayed in the reasons list to agents in AgentDesk.  
**Type**|  Select a type from one of the following:`Not Ready` | `Logout`  
**Description**|  An optional description for the reason  
  
![add reason codes.png](attachments/2524407/66879567.png?width=800)

Some reasons are available by default. You can add more for agents to choose from.

### Add New Channel Type

You may also create additional channel types to provision new channels of the desired channel type.

**Tip**

Learn more about Channel Types in [Channel related terms](Channel-Related-Objects_276594689.html)

To add a new channel type, go to the Channel Manager menu on the left and click **Channel Type.**

While adding a new channel type, provide the following info:

**Field**| **Description**  
---|---  
**Name**|  Provide a name for the channel type.  
**Media Routing Domain**|  Choose the MRD created above for this channel type.  
**Channel Type Logo**|  Upload a logo for this channel type. This logo or icon is then used in Unified Agent to show media channel data.  
**Interactive**|  Reserved for future use.  
  
![add new channel type.png](attachments/2524407/66420827.png?width=800)

__

### Pull Mode - No Routing

Pull mode allows incoming customer requests to be parked on a List instead of being queued to a queue and is available to all List Agents (who are subscribed to the List) to pick and join a conversation.

**Tip**

  * See [Subscribed Lists](Join-Pull-based-Requests_2528122.html) to see how agents get subscribed to and join Pull-based requests




The Lists created from here are mapped to Channels while setting up a channel, with the **Routing Mode** → **Pull**. 

#### Add Lists

Go to **Pull Mode List** and click the **Create List** button to add a new List using the following table.

**Field**| **Description**  
---|---  
**Name**|  Specify the List Name here. List names are not unique. So you can have two Lists having the same names.  
**Description**|  Specify an optional description of this List. For instance, what type of requests this List is expected to take in.   
  
![add Pull Mode List.gif](attachments/2524407/66912324.gif?width=800)

**Lists** can only be deleted if they are not being used by any channel.

## Teams Configuration

### Create a new team

  1. To create a team, click on the Teams tab. We will now see a section with heading **Teams** containing all the teams and their members (primary supervisor, secondary supervisor and agents).

  2. Click on **New Team** button to create the team. Dialog Box will appear.


![new team.png](attachments/2524407/774209577.png?width=760)

  3. Enter the team name and **Click** on Create button. Team should be created. 

     1. Description, supervisor(primary), secondary supervisors and agents are optional.

     2. You can select multiple secondary supervisors and multiple agents.


![create team.png](attachments/2524407/774209584.png?width=760)

  4. Once the team is created, you should be able to see your team in the teams list.


![team list.png](attachments/2524407/774209590.png?width=760)

  5. Once the team is created, you should be able to optionally assign some of the team agents directly to one of the secondary supervisors (aka Team Lead) of the team. You'll see option to assign; click on the icon.


![](attachments/2524407/774209596.png?width=760)

  6. A dialogue box will appear with three sections

     1. Secondary supervisors - This section will list all the secondary supervisors.

     2. Assigned agents - Agents assigned to the specific secondary supervisor listed here.

     3. Available agents - Agents that are part of the team but not assigned to any secondary supervisor in that team will be listed here.


![](attachments/2524407/774209602.png?width=760)

### Update a team

To update or edit the team, hover over the specific team. There is an option to edit; click on the edit team icon.

![edit button.png](attachments/2524407/774209608.png?width=760)

### Delete a team

  * To delete a team, hover over the specific team. You’ll see the option to delete; click on the delete team icon.


![Delete Team Button.png](attachments/2524407/774209614.png?width=760)

  * A confirmation box will appear. You can delete the team by clicking on the delete button.




![Delete team dialog.png](attachments/2524407/774209620.png?width=760)

See [Supervisor Access to Unified Admin](Supervisor-Access-to-Unified-Admin_1160151146.html) to see how a supervisor can manage his teams, queues, and agents by logging in to Unified Admin.

## Agent Desk Settings 

Enable admin to give the ability to agents format messages, file sharing, emoji support etc

**Field**| **Description**  
---|---  
**Message Formatting**|  Turn on for agents to send formatted messages  
**File Sharing**|  Turn on for agents to share and receive attachments.  
**Emoji**|  Turn on for agents to send and receive emojis.  
**Auto answer**|  With Auto-answer enabled, a new incoming Conversation request is automatically accepted on the agent. The agent does not need see incoming notification.(NOT FOR CISCO CALLS)  
**Conversation Participants**|  Turn on for agents to see conversation participants list for a conversation  
**Show Active Sessions Data**|  When turned on, it will allow the agents to see the active sessions data in the **Customer Info** panel on Agent Desk while handling a conversation.  
**Outbound SMS**|  If turned on, agents will be able to use the SMS service to send an outbound SMS to a customer regardless of a conversation.  
**Pause Conversation**|  Select timer options for holding a conversation. This allows configuring only the desired pause options that admins want their agents to see while pausing the conversion.  
  
Active Channels are now renamed to Active Sessions

![Screenshot 2025-08-05 at 5.14.43 PM.png](attachments/2524407/1226637416.png?width=830)

## Form Builder

Enables the business administrators to create, manage, and utilize multiple forms introducing new question types, sections, weightage, and form type categorization to enhance the user experience and data collection capabilities.

A default **Wrap-up** form is available on the **Forms** list. The business administrators can create other types of forms as per requirement:

![Form Solution.png](attachments/2524407/923697331.png?width=900)

For more detail click [here](https://expertflow-docs.atlassian.net/wiki/x/KAB1Bw?atlOrigin=eyJpIjoiNjhhNWM1NzBlN2VkNGYxYmJiZTVjNzZiNGM2MDcwMjEiLCJwIjoiYyJ9).

### Default Wrap-Up Form

A default Wrap-up form is available on the **Forms** page. 

Go to the form, **Wrap-Up,** and select edit action against the form to add wrap-up categories and reasons as per your business needs. 

![image-20241030-130438.png](attachments/2524407/636157953.png?width=900)

**Field**| **Description**  
---|---  
**Form Title**|  A default title to the Wrap-up form is provided on AgentDesk. The title changes to the form here won't take any effect on the AgentDesk.  
**Description**|  Specify an optional description of the form here. This won't be shown on AgentDesk.  
**New Attribute**|  Leave it as it is.In the default Wrap-up form, an attribute with the type **Options** is already added. You cannot change the type of this attribute in the default Wrap-up form.   
**Multiple choice**|  Turn this on if you want agents to be able to apply multiple reasons.   
**Add Category**|  A default category with the name, 'Category 1' is added. Change it according to your business requirements of wrap-up categories.  
**Add Options**|  Add options in each category. These are the actual wrap-up reasons per category defined above.  
  
You may add as many categories and options as needed in the Wrap-up form.

### Pre-Conversation Form

Business Administrators can create a pre-conversation form to use in the customer widget. 

  1. Click on the Forms object.

  2. Click on the **New Form** button.

  3. Select form type **Pre-conversation**.

  4. Add attributes (questions) as per your business needs.

  5. Now click the **Save Form** button.


![image-20250225-074121.png](attachments/2524407/923795579.png?width=900)

**Field**| **Description**  
---|---  
**Form Title**|  A default title to the Pre-conversation form is provided on the Customer Widget. The title changes to the form here do not have any effect on the Customer Widget.  
**Description**|  Specify an optional description of the form here. This will not be visible on the Customer Widget.  
**First Name**|  For instance, the `First Name` field, with the keys `first_name`, is optional. However, if the `First Name` is provided, the customer's name will be displayed in the conversation view of the Agent Desk. 

  * **First Name** → `first_name`

  
**Last Name**|  The `Last Name` fields, with the key `last_name`, are optional. However, if the `Last Name` is provided, the customer's name will be displayed in the conversation view.

  * **Last Name** → `last_name`

  
**Phone**|  To ensure personalized interactions in the conversation view of the Agent Desk, it is mandatory to create a `Phone` field for customer identification. The key for this field should be `phone`, and it is case-sensitive.

  * While the `Phone` is compulsory, other fields can be tailored based on business requirements.
  * **Phone** → `phone`

  
**Helping Text (Optional)**|  The optional helping text helps customers to understand the field.  
  
For a detailed understanding of the pre-conversation form, click [here](Customer-Widget-Admin-Guide_26838047.html).

## Campaign Configuration

CX Outbound Campaigns component empowers businesses to conduct bulk outbound campaigns directed at customers, including calls and messages. This component is integrated within the Unified Admin. Each campaign manages its contact list and utilizes a dedicated flow within the [Conversation Studio](As-a-Campaign-Manager_308510727.html).

![](attachments/2524407/924057652.png?width=900)

### Create Campaign

To create a new campaign, 

  1. Click on the **"Add New Campaign** " button. 

  2. A popup will appear to add a title for the new campaign. 

  3. Click on **Create** to create a new campaign

  4. If the "More detail" checkbox is selected, the campaign will open in editable mode immediately after creation, allowing one to attach contact sources via CSV and create control flows for the campaign.


![Add-20241007-122359.png](attachments/2524407/914456585.png?width=900)

### Campaign Controls

Following are the Campaign Controls to tailor campaign execution:

  * **Unpublish** : If the campaign is in a published state, it will be unpublished. 

  * **Publish** : If the campaign is currently unpublished, it will be published.

  * **Delete** : Confirming this action will permanently delete the campaign.

  * **End** : This action will terminate the campaign regardless of its state (published or unpublished). Once ended, the campaign cannot be re-published.


![Campaign Controls-20241007-123558.png](attachments/2524407/914456591.png?width=900)

### Edit Campaign

To edit campaign:

  1. Click on the **"Edit** " button of any specific campaign from the campaign table. 

  2. The campaign editing interface will be visible, which includes several key sections:

     1. **Edit:** Make amendments to the campaign. 

     2. **Title** : Enter Campaign title.

     3. **Description** : Provide a detailed description of the campaign.

     4. **Unpublish** : If the campaign is in a published state, it will be unpublished. 

     5. **Publish** : If the campaign is currently unpublished, it will be published.

     6. **Delete** : Confirming this action will permanently delete the campaign.

     7. **End/Stop** : This action will terminate the campaign regardless of its state (published or unpublished). Once ended, the campaign cannot be re-published.


![User Interface Features-20241007-123402.png](attachments/2524407/914456597.png?width=900)

For a detailed user guide for campaigns click [here](https://expertflow-docs.atlassian.net/wiki/pages/resumedraft.action?draftId=308510727&atlOrigin=eyJpIjoiYzgyZTc1MjliMjgyNDI2NzlmZjMzNmVkMjk3MDUyYTIiLCJwIjoiYyJ9).

## Quality Management

The business admins/Quality Managers can create and assign evaluation jobs to Evaluators. The solution provides several different reports ranging from review volume, team comparison, individual team/ agent performance over time, and Evaluators' calibration.

### Design an Evaluation Form

The Forms tab allows Quality Managers to create, edit, and manage evaluation forms (Questionnaires) used by evaluators to evaluate customer interactions with contact center agents.

#### Forms List View:

Displays existing forms with,

  * Name

  * Created On date and time.


![2.png](attachments/2524407/924549123.png?width=900)

#### Creating a New Form

  * Steps to create a new form:

    * Click **\+ New Form**.

    * Provide a form title and description.

    * Select the questionnaire type form.

    * Enable Sections and Weightage (required for Questionnaire Type Forms).

    * Add sections and questions:

      * Add Section: Break down forms into logical categories.

      * Add Question: Insert multiple-choice, single-choice, or text-based questions.




#### Save the Form

![12 \(1\).png](attachments/2524407/924549129.png?width=900)

### Reviews

Viewing and Filtering Reviews

#### Accessing Reviews

  * Select the Reviews option under the QM menu.

  * The Review Screen opens and lists all tasks assigned to a Quality Manager or others (Evaluators/ Reviewers).




#### Filter Options

  * Use the dropdown menu to filter reviews by

    * All

    * Pending

    * In Progress

    * Completed

  * Toggle "Assigned to me" to view tasks specifically assigned to Quality Manager/Evaluator.


![3 \(1\).png](attachments/2524407/924549135.png?width=900)

#### Starting a Review

  * Select a review from the list available on the review screen and click "Start Review". It will open Conversation View.

  * Use the form on the right-hand panel to evaluate agent interactions.

  * Assign scores or feedback to specific questions or sections.


![15 \(2\).png](attachments/2524407/924549141.png?width=903)

### Schedules

The Schedules tab (Review Schedular) allows Quality Managers to assign reviews to evaluators systematically.

#### Manage Schedules:

  1. Open the Schedules section in the left menu.

  2. Select _Manage Schedule_

  3. The list displays active schedules with details such as

     * Name: Schedule title.

     * Status: Current state (e.g., Active, Inactive).

     * Date: Scheduled end date.




#### Managing Schedules

  * Click the edit icon to modify a schedule.

  * Use the toggle switch to activate or deactivate schedules.




If toggled to deactivate, reviews created by the schedule will not be removed. Only future tasks assigned by the schedule are halted.

  * Delete schedules using the trash icon if no longer needed.




This will remove all pending/in-progress reviews.

![5 \(1\).png](attachments/2524407/924549147.png?width=900)

### Create a New Schedule

#### Scheduling Screen

After selecting the 'Schedule' tab at the top of the Schedules section, the screen displays two tabs: 

  * One for viewing all available schedules. 

  * Second for configuring a new schedule for quality management tasks.


![](attachments/2524407/924549147.png?width=916)

#### Basic Information

  * Schedule Name:

    * Enter a name for the schedule to easily identify it (e.g., "Weekly Agent Review").

  * Questionnaire:

    * Select a pre-configured form from the dropdown ('QM Form', ‘Score’, ‘Quality Manager Form’). This form will be used during the evaluation process.

  * Reviewer(s):

    * Assign one or more reviewers from the dropdown. Use the ‘Search’ feature to find specific reviewers quickly.

  * Agents and Teams to be Reviewed:

    * Select agents or teams that are to be reviewed under this schedule. You can select individuals or entire teams from the dropdown.




#### Search Criteria

  * Start Date & Time / End Date & Time:

    * Set the date and time range for when the review schedule will be active. Use the calendar picker to select the desired dates and times.

  * Add Another Filter:

    * Use this feature to refine the criteria by additional parameters (e.g., "Wrapup", "Direction", "Duration").

    * Select filters to narrow down specific interactions or criteria for the schedule.




#### Additional Settings

  * Set Deadline:

    * Specify the number of days within which the schedule must be completed. Use the dropdown to select a value.

  * Set Reminder:

    * Enable reminders for assigned reviewers. You can choose the reminder interval (e.g., 1, 2, or 3 days). Reminders can only be scheduled up to one day before the deadline.

  * Repeat Schedule:

    * Enable repetition for recurring schedules. Options include:

      * Daily

      * Weekly

      * Fortnightly

      * Monthly




For a Repeat Schedule, only new conversations that meet the search criteria will be assigned. The "Start Date & Time / End Date & Time" must be configured to ensure repetitions occur within the specified date range.

#### End Repetition Options

  * Date:

    * Specify the exact date when the recurring schedule will end.

  * After Occurrences:

    * Specify the number of occurrences after which the schedule will end.


![6 \(2\).png](attachments/2524407/924549153.png?width=908)

### Conversation List

The Conversation List provides an overview of all agent interactions for evaluation and quality management. This screen is crucial for accessing, filtering, and managing conversations. Below are the key components and functionalities:

#### Conversation Overview

  * Columns:

    * Direction: Indicates whether the conversation is inbound or outbound.

    * Date: The date the conversation took place.

    * Time: The starting time of the conversation.

    * Duration: Total time of the interaction.

    * From: The origin of the conversation (e.g., a phone number or a client).

    * To: The recipient of the conversation.

    * Agent(s): The agent(s) involved in the conversation.

    * Reviews: Shows progress in percentages or whether the review is Assigned.

    * Wrap-up: Notes or summaries added by agents.




#### Filtering Options

  * Click the Filter Icon to open the filter panel.

  * Available filters:

    * Start Date & Time / End Date & Time: Specify a date and time range for filtering conversations.

    * Agents and Teams: Filter by specific agents or teams.

    * Direction: Select Inbound or Outbound Conversations.

    * Wrap-ups: Filter by wrap-up codes or notes.

    * Duration: Set a time range in minutes, seconds, or hours.




The default operator between different filters is **AND** , while the operator within the “Agents and Teams” and “Wrap-ups” filters is **OR**.

  * **Actions:**

    * Apply: Filter the list using the selected criteria.

    * Reset: Clear all applied filters.


![7 \(4\).png](attachments/2524407/924549159.png?width=908)

### Reviewing Conversations

  * Click on a conversation to open its detailed view.

  * The conversation view displays:

    * A chronological history of messages or call records.

    * Interaction details, such as client responses, agent replies, and system actions.

  * **Actions:**

    * Assign: Opens the Assign Panel where you can:

      * Select an evaluator.

      * Assign an agent for review.

      * Choose a questionnaire.

      * Set a due date and reminders.

      * Confirm by clicking Assign.

    * Review: Opens the Review Panel where you can:

      * Select an agent to review.

      * Choose a questionnaire for the evaluation.

      * Click Start Review to begin the process.

    * **Viewing Conversation Types**

      * Use the dropdown at the top-right to filter by:

        * **All:** Displays both chat and voice conversations.

        * **Chat:** Shows only chat-based interactions.

        * **Voice:** Displays voice calls.


![](attachments/2524407/923664710.png?width=1166)

### Review Notifications

Notifications alert evaluators about new reviews and deadlines.

  1. New Assignments: Displays recently assigned reviews.

  2. Reminders: Alerts for approaching deadlines.




![9.png](attachments/2524407/923959501.png?width=1026)
