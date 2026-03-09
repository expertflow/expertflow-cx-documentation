# CX Knowledgebase : CIM Messages

The `CIMMessage` object is the standardized message format for communication within the Expertflow CX. All 3rd-party customer/agent/BOT applications must adhere to this format when sending or receiving messages. 

## Communication Protocols

CX supports two types of communication protocols for message exchange:

### **REST API**

  * Allows sending and receiving messages using standard HTTP requests

  * The [Channel Connectors](Channel-Connector-Developer-Guide_2528843.html) can send/received messages in the form of `CIMMessage`using [CIM Message REST APIs](https://api.expertflow.com/#3e917ac7-bf4d-4d3c-b8a5-1054ff41577a).

  * The [Bot Connector](Bot-Connector-Developer-Guide_2526409.html) can send/receive messages in the form of `CIMMessage`




### **WebSocket:**

  * Facilitates real-time, bidirectional communication for sending and receiving messages.

  * [Agent applications](Agent-Desk-Developer-Guide_2523754.html) can send/receive the messages in the form of `CIMMessage` through <http://Socket.io> connection. 




# Object Structure

### **ID**

A universally unique identifier (UUID) to uniquely identify each message.

### **Header**  


[Message Header](Message-Header_479952918.html) contains the message metadata such as timestamp, sender information ,and other relevant detail. 

### **Body**

The body contains the actual content of the message e.g. plain text audio, video etc. Refer to [this](https://expertflow-docs.atlassian.net/wiki/x/EYCeH) page for details of supported messages types.

For message response examples, visit <https://api.expertflow.com/#6644e840-95a1-4002-bf8b-965ab07e0c7e>.   


  

