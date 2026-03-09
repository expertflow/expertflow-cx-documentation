# CX Knowledgebase : Add a Customer Widget

To add a Customer Widget, you first need to add a [Web Channel](https://expertflow-docs.atlassian.net/wiki/x/AQAyWQ) in Unified Admin. If you have already created one, follow this guide to configure and customize the appearance of the Customer Widget in the system.

It serves as the customer-facing front end of the CX system, providing visitors AI assistance and allow them to reach to contact center agents when needed.   
Business administrators can create **multiple widget instances** , each with its own configuration, appearance, and behavior.

For example, if your organization has both a **Customer Portal** and a **Partner Portal** , you can create two separate web widget instances — each with different branding, routing, and behavior — that operate independently of one another. 

## **To Create a New Web Widget**

  1. Open the **Unified Admin** and navigate to the **Channel Manager** section.

  2. Click on **Create Web Widget**




## Widget Configurations

The following sections explain each configuration option in detail and describe how it impacts the overall widget functionality.

### **Widget Identifier**

Each widget instance is identified by a **Widget Identifier** , which is used by the **Web Widget REST APIs** to load the correct configuration when the widget initializes on a webpage.

This is a short, unique string that defines your widget instance.  
For example, you can name it `web`, `customer-widget`, or `partner-widget`.  
It’s used as the identifier for loading this specific widget configuration on your website.

The identifier can contain **letters (A–Z)** , **numbers (0–9)** , and **special characters** such as asterisks (*), dashes (-), and underscores (_).  
The maximum length allowed is **50 characters**.

### **Widget Title**

The **Widget Title** is the main heading displayed on the chat widget.  
It could be your **company name** , **brand name** , or any short descriptive text that helps customers identify who they are chatting with.

### **Widget Subtitle**

The **Widget Subtitle** appears just below the title text inside the chat widget.  
It can include helpful information such as **business hours** , **support type** , or a **welcome tagline** (e.g., “We’re here to help 24/7!”).

### **Pre-Chat Form**

From this dropdown, you can select a **pre-conversation form** that customers will see before starting the chat.  
These forms are created in the **Form Builder** , and may include fields like name, email, or issue type.  
Selecting a form here helps you collect useful information before routing the chat to an agent or bot.

**Tip:** Please go through this guide to create forms. 

<https://expertflow-docs.atlassian.net/wiki/x/HABiFw>

### **Language**

This option allows you to define the **language** in which the chat widget will appear.  
It pulls available options from **General Settings → Locale Settings**.  
Select the preferred default language for your customers — for example, **English** , **Arabic** , or **French**.

### **Color Palette**

Choose a color scheme that aligns with your website or brand identity.  
The **Color Palette** field lets you define the widget’s accent and background colors, giving the chat window a consistent look and feel with your site.

### **Download Transcript**

Enable this setting if you want customers to **download the full chat transcript** once the conversation ends.  
This can be useful for customers who need a record of their discussion for future reference.

### **Dynamic Link**

If this setting is turned on, the widget will automatically **convert URLs into clickable hyperlinks** — whether they’re sent by the customer or by the agent/bot.  
This improves usability by allowing customers to directly open shared links.

### **Emoji Support**

When this option is enabled, customers can **send emojis** during chat conversations.  
It adds a more natural, expressive element to customer communication and improves the overall user experience.

### **File Transfer**

Enable **File Transfer** if you want customers to **send and receive file attachments** during a chat.  
This is especially useful for exchanging documents, screenshots, or images that help resolve customer issues faster.

### **Font Size Options**

If enabled, the widget will display **three font size options** for customers to choose from — **Large** , **Medium** , and **Small**.  
This accessibility feature helps users adjust text readability according to their preferences.

### **Enable WebRTC**

Enabling **WebRTC** allows customers to seamlessly initiate **audio or video calls** with agents directly from the web widget helping real-time issue resolution, enabling smoother escalations and more personalized customer interactions.

**Tip:** Want to learn more about setting up WebRTC and its configuration options?  
Check out our detailed guide here:<https://expertflow-docs.atlassian.net/wiki/x/AAP2K>

### **Enable Callback**

Turn on to enable feature for scheduling callback options

**Tip:** Explore further about callbacks in this guide. 

<https://expertflow-docs.atlassian.net/wiki/x/nYfzK>

### **Enable Webhook Notifications**

A Webhook notification on Google Workspace provides agents the flexibility to get notified in their Google spaces/groups of recently initiated web chat sessions.
