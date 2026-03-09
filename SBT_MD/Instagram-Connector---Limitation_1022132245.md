# CX Knowledgebase : Instagram Connector - Limitation

* * *

## Instagram Connector Limitations

Below are the known limitations of the **Instagram Connector** in the current release of Expertflow CX

**Media Type**| **Instagram Supported Formats**| **EFCX Supported Formats**  
---|---|---  
**Audio**| `aac`, `m4a`, `wav`, `mp4`| `mp3` only  
**Image**| `png`, `jpeg`, `gif`| `jpg`, `png`  
**Video**| `mp4`, `ogg`, `avi`, `mov`, `webm`| `mp4` only  
**File**|  Supported only as shared link or preview| Supported only as shared link or attachment preview  
  
* * *

### 1\. Multimedia in Comments Not Supported

  * Instagram does **not support multimedia attachments (images, audio, video, files)** in **public comment threads**.




* * *

### 2\. Audio Incompatible 

  * outgoing audio messages are not functioning due to format incompatibility although,Instagram connector supports transfer of audio files.




* * *

### 4\. No Support for Message Reactions

  * Instagram **does not support emoji reactions** (e.g., ❤️ or 👍) to specific messages.

  * These are not visible on the agent side.




* * *

### 5\. No Support for Quoted Reply

  * Instagram **does not support sending quoted reply via API** to a specific message.




* * *

### 6\. Real-time Typing Indicators or Read Receipts

  * The API does **not support typing indicators**.

  * **Read receipts** is supported from instagram as part of incoming message however, from the perspective of outgoing read receipts it is not supported.




or further **constraints** related to Instagram, checkout [Instagram Documentation](https://developers.facebook.com/docs/messenger-platform/instagram/features/send-message)
