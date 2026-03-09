# CX Knowledgebase : WhatsApp

WhatsApp is a supported customer channel that allows businesses to start a conversation with a bot. an agent and a customer and interact with each other. This document serves as a guide to the business on how to configure WhatsApp Channel and start the chat.

## Getting Started

Businesses can get access to WhatsApp APIs either through

  * direct subscription from WhatsApp via their cloud APIs. or

  * by using a service provider to provide access to WhatsApp APIs




Expertflow does not support cloud APIs as of now. However, Expertflow has integrated with two service providers. One is Dialog360 and the other is Twillio. Businesses can choose any one service provider of their own choice for WhatsApp API subscription.

Configuration of WhatsApp Channel using ****[**Dialog360**](360-Connector-Configuration-Guide_2531584.html)

Configuration of setting up WhatsApp Channel using [**Twilio**](2529631.html)

After making the necessary configurations, a WhatsApp channel needs to be created by using [**< Unified Admin -> Channel Configuration**](360-Connector-Configuration-Guide_2531584.html)**** for Dialog360 and [**< Unified Admin -> Channel Configuration**](2529631.html)**** for Twilio.

## Channel Capabilities

### Plain Text Message

Expertflow's WhatsApp integration allows agents and customers to send and receive text messages to each other. For this, the maximum character limit is of 4096 characters is supported. For details of message body properties, see [**CIM Messages - > Plain Text Message**](Plain-Text-Message_2532510.html)

#### Text Message Formatting

Use the following symbols to format your text.

**Formatting**| **Symbol**| **Example**  
---|---|---  
Bold| Asterisk (*total*)| Your **total** is $10.50  
Italic| Underscore (_WhatsApp_)| Welcome to _WhatsApp_  
Strike-through| Tilde (~hi~)| This is ~~hi~~  
Code/pre-formatted| Three backticks(```Hello World```)|  Hello World  
  
Administrators can enable/disable this feature by switching the toggle button on/off as it is set to **off** by default. To enable message formatting, go to **< Unified Admin -> Agent Desk -> Enable Message Formatting -> Save**

![](attachments/2526019/15204670.png?width=500)

### Interactive Messages

Interactive Messages provide a preset list of options that facilitate the customers to find and select what they want from the business quickly and easily. WhatsApp supports two types of Interactive Messages

  * List Messages

  * Reply Buttons




List Messages

Includes a menu of up to 7 options that offers a simpler and more consistent way for the customers to make the selection while interacting with the business. These options are fully customizable according to the business need. Administrators can customize them as a single option/button or many options/buttons up to their business requirements. For the configuration see [**CIM Messages - > Button Message**](Button-Message_2532516.html)**.**

The words List/Button are used in terms of Interactive Messages.

Reply Buttons

Includes the messages of up to 3 options. Each option is a button. This offers a quicker way for the customers to make a selection from a menu when interacting with the business. 

  * For now, customers can not select more than one option at the same time from a list or button message.

  * List Messages or Reply Buttons can only be sent within the 24-hour timeframe. Use templates outside of the 24-hour session.




### **Media Messages**

#### Audio Message

Enable the customer to send and receive voice notes instantly. To know the properties of the message body, see [**CIM Media Messages - > Audio Message** **Format**](Multimedia-Messages_2525501.html). The voice notes will be displayed as shown in the screenshot below and can easily be played with a single click.

![](attachments/2526019/15008104.png?width=400)

#### Video Message

WhatsApp supports and allows the customer to send/receive Video Files. To know the size and format, see [**CIM Media Messages - > Video Message** **Format**](Multimedia-Messages_2525501.html). Video files will be visible as in the screenshot below and can be played by simply clicking on the 'Play' button.  


![](attachments/2526019/14682127.png?width=400)

#### Image Message

Enables the customer to send an image/photo instantly. You can simply choose the image to send. Image Message will be visible as in the following screenshot. To zoom in and out, simply click on the image. To perceive the properties of Image Message, see [**CIM Media Messages - > Image Message** **Format**](Multimedia-Messages_2525501.html).

![image message.png](attachments/2526019/81920025.png?width=300)

#### Stickers

This feature enables the customer to send/receive WhatsApp supported Stickers as these are character-driven emoticons to add flavor to the conversation. To understand the properties of Sticker Message, see [**CIM Media Messages - > Sticker Message** **Format**](Multimedia-Messages_2525501.html)

![sticker message.png](attachments/2526019/81821726.png?width=211)

**Emoji**

This feature enables the customer to send and receive Emoji characters as this is informal, personable and often used to inject humour into the digital conversation. 

### Limitations

Support for Emoji is not provided as of now.

### **Send Quoted Reply**

Enables the customer to reply to one of the sent messages from the business by selecting that message and choosing the "reply" option which is referred to as a quoted response. This enables the customer to see his original message along with the organization's response (agent's message)

### **File Message**

Enables the customer to send/receive File Messages. To see the size and properties of the file, see [**CIM Media Messages - > File Message** **Format**](Multimedia-Messages_2525501.html). Administrators can enable/disable this feature by switching the toggle button on/off as this is set to off by default. To enable** <Unified Admin -> AgentDesk -> Enable File Sharing -> Save **

![File sharing.png](attachments/2526019/81920034.png?width=500)

By enabling file sharing, file name and file size is visible as in the screenshot below. You can click to open, read, and download it.

### **URLs**

Enables the customer to send and receive URLs to/from the business. To know the method of sending URLs, see [**CIM URL Message**](URL-Message_2532489.html)

### **Contact Message**

This feature enables the customer to send/receive Contact Messages containing the information of

  * Address

  * Email

  * Name

  * Organization

  * Phone

  * URLs




The contact message can be seen as shown in the above screenshot. The parameters and properties of sending the message are****[**CIM Contact Message**](Contact-Message_2532495.html)

### **Location Message**

Enables the customer to send/receive Location Messages containing the information of 

  * Longitude

  * Latitude

  * Name

  * Address




Location messages will be rendered as a map image with a Google Maps link.

To know the properties of the message body, see [**CIM Location Message**](Location-Message_2532513.html)
