# CX Knowledgebase : Meta - WhatsApp Cloud API

  * Getting Started
  * Supported Message Types
    * Plain Message
    * Audio Message
    * Video Message
    * Image Message
    * Stickers
      * Limitations
    * Emoji
      * Limitations
    * Quoted Reply
    * File Message
    * Contact Message
    * Location Message
    * Read Notification
    * Interactive/Button Messages
    * URLs



WhatsApp support in Expertflow CX lets businesses engage with their customers through real-time messaging on WhatsApp. Whether it's a simple text or rich media like files, images, or location data, the connector ensures seamless communication from within the Expertflow CX interface.

Refer to [WhatsApp Connector Limitations ](1014169625.html)to understand current constraints.

## Getting Started

To get started, a business must have a verified WhatsApp Business Account linked to a phone number. This account needs to be integrated into Expertflow CX through Unified Admin. Once the connection is set up, agents can start handling WhatsApp conversations like any other supported channel.

## Supported Message Types

Below are the types of messages currently supported by the WhatsApp connector.

### Plain Message

**What it is:**  
A basic text message exchanged between the customer and the agent without any formatting or attachments.

**How it works:**  
When a user types a message, it's sent as plain text on the agent's side.Text appears instantly in the chat window. Agents can reply using the “**Reply Bar** “ below. 

**Maximum Length** : 4096 characters.

**Format** : UTF-8 encoded text.

![image-20250425-053127.png](attachments/131006630/1046675483.png?width=760)

### Audio Message

**What it is:**  
Voice notes or audio clips sent during chat.

**How it works:**  
Audio files are played inline with a click. Agents can listen and reply with voice messages directly from their interface by uploading from “**attachment Icon** “ present in **Reply bar**.

![image-20250425-060554.png](attachments/131006630/1046675512.png?width=760)

Maximum Audio size supported by WhatsApp : 16MB

### Video Message

**What it is:**  
Short video files shared to explain or show something visually.

**How it works:**  
Videos show a thumbnail and play button. Agents can view customer videos and reply with video by uploading from “**attachment Icon** “ present in **Reply bar**.

![image-20250425-060249.png](attachments/131006630/1046642732.png?width=760)

Maximum Video size supported by WhatsApp : 16MB

To check the supported media types of video and some constraints, [see](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media#supported-media-types).

### Image Message

**What it is:**  
Photos or screenshots exchanged for visual context.

**How it works:**  
Images show as thumbnails. Agents can send images in response by uploading from “**attachment Icon** “ present in **Reply bar**..

![image-20250425-054820.png](attachments/131006630/1046675505.png?width=760)

Maximum Image size supported by WhatsApp: 5MB

To check the supported media types of image and some constraint [see](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media#supported-media-types).

### Stickers

**What it is:**  
Expressive graphics sent by customers to convey mood or reaction.

**How it works:**  
Stickers display as static or animated images. Agents can view them but cannot send stickers due to format restrictions.

![image-20250425-055017.png](attachments/131006630/1046413640.png?width=760)

Maximum Sticker size supported by WhatsApp:   
Static stickers: 100KB  
Animated stickers: 500KB

#### Limitations

Media type for sticker from WhatsApp is **image/webp,** but our system doesn't support this type for outbound.

### Emoji

#### Limitations

Support for Emoji is not provided as of now.

### Quoted Reply

**What it is:**  
A feature that links a reply to a specific previous message for clarity.

**How it works:**

Agents can also use quoted replies to answer specific questions — by selecting a message and clicking “**Reply** ,” their message will carry the reference.

[Screencast from 2025-04-25 10-22-20.mp4](attachments/131006630/1046675468.mp4?width=760)

### File Message

**What it is:**  
Document files (PDFs, DOCs, etc.) sent for reference, instructions, or records.

**How it works:**  
Files appear in the chat with filename, type, and size displayed.  
Clicking opens or downloads the file directly.  
Agents can upload and send files from their desktop, such as invoices, manuals, or forms.  
This feature must be enabled in admin settings before use.

![File sharing.png](attachments/131006630/1013841925.png?width=556)

By enabling file sharing, the file name and file size are visible as in the screenshot below. You can click to open, read, and download it.

![image-20250425-060922.png](attachments/131006630/1046577169.png?width=760)

Maximum File size supported by WhatsApp: 100MB

### Contact Message

**What it is:**  
A structured contact card with fields like name, email, phone, and organization.

**How it works:**  
Shared contact cards appear as a contact block showing all fields.  
Agents can click to view full details the contact.  
Bot can also send their own, through button message .

![image-20250425-050906.png](attachments/131006630/1046577153.png?width=546)

![image-20250425-050039.png](attachments/131006630/1046380830.png?width=562)

### Location Message

**What it is:**  
A map location or pin sent for navigation or confirmation.

**How it works:**  
Received locations are shown as a mini map with a clickable link to Google Maps.  
Agents can click to view the place.  
Bot can also send their own, through button message .

.

![image-20250425-051942.png](attachments/131006630/1046380837.png?width=760)

### Read Notification

**What it is:**  
A system-generated update indicating that the customer has seen a message.

**How it works:**  
When the message is read on WhatsApp, a “**read** ” signal is sent back and reflected in the agent’s interface with **Customer’s Name**.  
This helps agents confirm delivery and follow up if no response is received.  
Applies to both incoming and outgoing messages.

![image-20250425-043952.png](attachments/131006630/1046446088.png?width=760)

### Interactive/Button Messages

**What it is:**  
Predefined button options sent by the business to help users respond faster.

**How it works:**  
Bot send a message with buttons.  
Customers reply with specific “**Button** “,for their relevant choices.  
When clicked, the selected option is shown in the conversation feed.

![image-20250425-042815.png](attachments/131006630/1046478849.png?width=760)

### URLs

**What it is:**  
Web links sent within messages to direct users to external resources.

**How it works:**  
Links are automatically detected and made clickable.  
Clicking opens the URL in a new browser window.

![image-20250425-043255.png](attachments/131006630/1046347794.png?width=760)
