# CX Knowledgebase : Facebook Direct Message

Allows the clients using EFCX to connect to their customers and take their chats being initiated from a Facebook messenger. 

See [Facebook Connector Limitations](Facebook-Connector-Limitations_74350672.html) for what is not supported in this release.

## Getting Started

To begin with Facebook, one must have a Facebook App and must be a registered user to create a personal profile and add others for customer interactions. For this, one should have a Facebook account, which must have been added to the Facebook Page. Also need to grant access to the Facebook App.

The Administrators can create a Facebook Page, [grant a user access to the Facebook App](Facebook---Configuration-Guide_2531616.html), and create a Page Access Token by following the step-by-step procedure of [Create Page Access Token](Facebook---Configuration-Guide_2531616.html)

The Facebook connector needs to be configured to [set up a new channel in the Unified Admin](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2524407/Unified+Admin+Guide#Step-11%3A-Set-up-a-new-Channel) of Expertflow CX's application to set up a Facebook Channel. This one-time configuration will help the business interact with both Facebook channels on a single interface.

## Channel Capabilities

### Text Message

Expertflow CX's Facebook connector enables the business to send and receive direct text messages to or from customers. For this, Facebook supports a text message to be of UTF-8 and less than 2000 characters.

### File Transfer

allows the business to send and receive media messages containing audio, images, videos and files to/from the customers.

The following media types are supported:

**Media**| **Supported Content Type**  
---|---  
audio| `audio/aac`, `audio/mp4`, `audio/amr`, `audio/mpeg`,  
`audio/ogg;`  
file| Any valid MIME-type.   
image| `image/jpeg`, `image/png`  
video| `video/mp4`, `video/3gpp`  
  
Max File size: 25MB

#### Audio Message

Enables sending and receiving audio messages to/from the customers, as shown in the screenshot below. To see the properties of audio messages, see [CIM Media Messages -> Audio Message Format](Multimedia-Messages_2525501.html)

![](attachments/2526025/2549554.png?width=1800)

#### File Message

Enables the business to send and receive file messages. The file size and supported types are mentioned [here](Multimedia-Messages_2525501.html) in the File Message Format.

![](attachments/2526025/2549564.png?width=680)

### Limitation

Multiple file attachments (from messenger) are currently not supported in Facebook Connector - As of now, if a user attaches multiple files (in a single chat), the Facebook connector will picks only one file out of the multiple files that were attached and relay that to CCM while the rest of the other files attachment are ignored. This limitation is not entirely a Facebook connector problem but rather a File Engine & CCM limitation - the API they expose currently do not support multiple file uploads. 

#### Image Message

Allows the business to exchange images to/from the customers as shown below. To know the supported type and size, see [CIM Media Messages -> Image Message Format](Multimedia-Messages_2525501.html)   


![](attachments/2526025/2549549.png?width=680)

#### Video Message

Allows the business to send and receive video messages to/from the customer. The video size and types are mentioned in the table of [Video Message Format](Multimedia-Messages_2525501.html)

![](attachments/2526025/2549509.png?width=578)

#### Sticker Message

Enables the business to receive sticker messages. This visual facilitates the agent to interpret the emotions and expressions of the customer quickly and then respond to them. To know more about the sticker message properties, see [CIM Media Messages -> Sticker Message Format](Multimedia-Messages_2525501.html)

![](attachments/2526025/2549544.png?width=680)

#### Support Gifs

Enables the business to receive GIFs and respond to them as any other message.

![](attachments/2526025/2549529.gif?width=578)

### Send A Quoted Reply

Expertflow CX's Facebook connector enables the business to reply to a specific message _from_ the customer. To reply to a specific message, the contact center representative can quote the specific message by clicking on the reply button, as shown below, and can respond to that specific message by selecting the channel from the message composer bar. This quoted reply will become a part of the conversation history. For indication purposes, they are visible in a different color. In the quoted reply, the representative's name will be visible in blue color, and the customer's name will be seen in grey color.  


![](attachments/2526025/2549534.gif?width=680)

### Send URL

Enables the business to send and receive URLs from the customer. This feature converts the plain text into URL format, as shown below.

  


![](attachments/2526025/2549514.png?width=1800)

### Send A Button Reply

Supports **Quick Replies** via buttons. This allows businesses to present customers with a set of predefined response buttons below a message. When a customer selects a quick reply, the response is sent to the agent, and the reply options disappear.

Quick Replies are useful for guiding users through a conversation, minimizing typing effort, and speeding up interactions.

![button-reply.png](attachments/2526025/1022132264.png?width=800)

  


  

