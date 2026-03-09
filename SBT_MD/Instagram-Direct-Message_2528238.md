# CX Knowledgebase : Instagram Direct Message

Allows businesses, using Expertflow CX, to connect with their customers and manage conversations initiated through Instagram DM.

**Limitations**  
See [**Instagram Limitations**](Instagram-Connector---Limitation_1022132245.html) for what is not supported.

## Channel Capabilities

### Text Message

Enables the business to send and receive text messages.

### File Transfer

Allows sending and receiving **media messages** , including:

**Media Type**| **Instagram Supported Formats**| **EFCX Supported Formats**  
---|---|---  
**Audio**| `aac`, `m4a`, `wav`, `mp4`| `mp3` only  
**Image**| `png`, `jpeg`, `gif`| `jpg`, `png`  
**Video**| `mp4`, `ogg`, `avi`, `mov`, `webm`| `mp4` only  
**File**|  Supported only as a shared link or a preview| Supported only as a shared link or an attachment preview  
  
**Max File size** : 25MB (depends on media type and Instagram limitations)

### Audio Message

  * **Inbound audio** messages are functioning however, **Outbound Audio** is not functional due to format incompatibility. Although it provides support for the transfer of audio files. See: [_CIM Media Messages → Audio Message Format_](Multimedia-Messages_2525501.html)


![image-20250414-064748.png](attachments/2528238/1022197781.png?width=506)

### File Message

Instagram has**limitations** around file attachments. Instead, customers may share cloud storage links. Agent-side file sharing is supported.

![image-20250411-060946.png](attachments/2528238/1021870155.png?width=250)

### Image Message

Supports sending and receiving images. To view supported types and format requirements, see [_CIM Media Messages → Image Message Format_](Multimedia-Messages_2525501.html)

![image-20250411-060921.png](attachments/2528238/1022001232.png?width=250)

### Video Message

Allows sending and receiving videos via Instagram DMs. Format and size requirements apply. For details, refer to [_CIM Media Messages → Video Message Format_](Multimedia-Messages_2525501.html)

![image-20250411-060837.png](attachments/2528238/1021870147.png?width=250)

### Support Emojis

Supports sending and receiving **emojis**.

![image-20250414-065949.png](attachments/2528238/1021182179.png?width=1055)

### Send a Quoted Reply

Enables agents to **reply to a specific message** using a quoted format. The quoted message is visually distinct, and reply context is maintained in the chat history.

![image-20250414-070247.png](attachments/2528238/1021477036.png?width=1055)

### Send URL

Converts valid URLs into clickable links within messages. These are processed in the same format as supported audio files. See: [_CIM URL MESSAGE_](URL-Message_2532489.html)

![image-20250414-070600.png](attachments/2528238/1021509848.png?width=1055)

### Button Messages

Supports **Quick Replies** , allowing businesses to present customers with a set of predefined response buttons below a message. When a customer selects a quick reply, the response is sent to the agent, and the reply options disappear.

![image-20250416-111930.png](attachments/2528238/1027277209.png?width=618)
