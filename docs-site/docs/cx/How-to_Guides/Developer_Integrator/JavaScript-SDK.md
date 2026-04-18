---
title: "JavaScript SDK for Customer-Facing Channels"
summary: "Complete guide to the ExpertFlow CX JavaScript SDK — covering supported capabilities, installation, configuration, chat functions, WebRTC calls, socket events, and chat resume scenarios."
audience: [developer-integrator]
product-area: [sdk, channels]
doc-type: reference
difficulty: intermediate
keywords: ["JavaScript SDK CX", "customer facing SDK CX", "omnichannel SDK CX", "web chat SDK CX", "WebRTC SDK CX", "socket events SDK CX", "ExpertFlow JS SDK", "customer widget SDK CX"]
aliases: ["CX JS SDK", "JavaScript SDK customer-facing CX", "web SDK CX", "customer-facing SDK CX", "omnichannel communication SDK CX"]
last-updated: 2026-04-07
---

# JavaScript SDK for Customer-Facing Channels

The ExpertFlow CX JavaScript SDK enables developers to embed real-time communication features — web chat, audio calls, video calls, and screen sharing — into mobile (native or hybrid) and web applications.

The SDK handles all backend communication with ExpertFlow CX while allowing developers to build and use a **fully custom user interface**.

---

## Supported Capabilities

| Capability | Status |
|---|---|
| Web Chat | Available |
| Audio Calls (WebRTC) | Available |
| Video Calls (WebRTC) | Available |
| Screen-sharing Calls | Available |
| Contact Center Stats (queue depths, wait times) | Roadmap |
| Contact Center Availability Timings | Roadmap |
| Agent Availability Check | Roadmap |
| Expected Waiting Time | Roadmap |

---

## Use Cases

- **Custom chat widget**: Embed a branded chat experience in your website or mobile app without using the standard ExpertFlow widget.
- **In-app calling**: Add WebRTC audio/video call capability to a mobile app using the SDK's call controls.
- **Omnichannel customer experience**: Enable customers to switch between chat and voice within a single app session.

---

## Installation

### CDN (Web Applications)

```html
<!-- Standard -->
<script src="https://cdn.jsdelivr.net/gh/expertflow/sdk-for-customer-facing-channels@latest/sdk.js"></script>

<!-- Minified -->
<script src="https://cdn.jsdelivr.net/gh/expertflow/sdk-for-customer-facing-channels@latest/sdk.min.js"></script>
```

### NPM (Mobile / Native Apps)

```bash
npm i @expertflow/sdk-for-customer-facing-channels
```

Full NPM package reference: `https://www.npmjs.com/package/@expertflow/sdk-for-customer-facing-channels`

---

## Configuration

### `config.js` — Chat Configuration

| Property | Type | Description | Example |
|---|---|---|---|
| `widgetIdentifier` | String | Widget configuration identifier | `"Web"` |
| `serviceIdentifier` | String | Channel manager service identifier | `"5155"` |
| `socketUrl` | String | Web Channel Manager IP or FQDN | `"https://<public_ip>"` |
| `fileServerUrl` | String | File Server Engine IP or FQDN | `"https://<public_ip>"` |
| `ccmUrl` | String | Customer Channel Manager IP or FQDN | `"https://<public_ip>"` |
| `transcriptUrl` | String | Chat Transcript service IP or FQDN | `"https://<public_ip>"` |
| `channel` | String | Client device type | `"Mobile"` |

### WebRTC Configuration (Unified Admin)

| Property | Type | Description | Example |
|---|---|---|---|
| `wssServerIp` | String | EFSwitch IP or FQDN | `"192.168.1.201"` |
| `wssServerPort` | String | EFSwitch WebRTC port | `"7443"` |
| `diallingUri` | String | EFSwitch DN for dialling | `"369852"` |
| `sipExtension` | String | SIP extension for customer registration | `"ext"` |
| `extensionPassword` | String | SIP extension password | `"password"` |
| `webSocket` | String | WebSocket protocol | `"ws"` |
| `iceServers` | Array | STUN/TURN server configuration | See below |
| `form` | String | Pre-chat form ID from Unified Admin | `"12312312sdfsdf23123"` |

**ICE Servers example:**
```json
[{"urls": ["stun:stun.l.google.com:19302", "stun:stun1.l.google.com:19302"]}]
```

---

## Chat Functions

| # | Function | Parameters | Description |
|---|---|---|---|
| 1 | `widgetConfigs(ccmUrl, widgetIdentifier, callback)` | ccmUrl, widgetIdentifier, callback | Fetches widget configuration from CCM. |
| 2 | `establishConnection(serviceIdentifier, channelCustomerIdentifier, callback)` | serviceIdentifier, channelCustomerIdentifier, callback | Establishes a Socket.IO connection. Returns `SOCKET_CONNECTED`. |
| 3 | `chatRequest(data)` | `{ type: "CHAT_REQUEST", data: <customerData> }` | Initiates a chat session. Returns `CHANNEL_SESSION_STARTED`. |
| 4 | `sendMessage(data)` | CIM message payload | Sends a message of any supported CIM type. |
| 5 | `chatEnd(data)` | Customer information | Ends the chat session. Returns `CHAT_ENDED`. |
| 6 | `uploadToFileEngine(data, callback)` | `{ file, conversationId }` | Uploads a file attachment to the File Engine. |
| 7 | `setConversationData(conversationUrl, conversationId, data)` | conversationUrl, conversationId, key-value data | Stores custom data (e.g., form data) on the conversation. |
| 8 | `getConversationData(conversationUrl, conversationId)` | conversationUrl, conversationId | Retrieves custom data stored on the conversation. |
| 9 | `getPreChatForm(formUrl, formId, callback)` | formUrl, formId, callback | Fetches a pre-chat form definition for rendering. |

### Customer Data Payload

```json
{
  "serviceIdentifier": "2342342",
  "channelCustomerIdentifier": "2342342342",
  "browserDeviceInfo": {
    "browserId": "123124",
    "browserIdExpiryTime": "9999",
    "browserName": "chrome",
    "deviceType": "desktop"
  },
  "queue": "",
  "locale": {
    "timezone": "asia/karachi",
    "language": "english",
    "country": "pakistan"
  },
  "formData": {
    "attributes": [
      { "value": "test", "key": "firstName", "type": "string" }
    ],
    "createdOn": "Standard GMT DateTime",
    "filledBy": "web-init",
    "formId": "0.0313465461351",
    "id": "0.1025556665461"
  }
}
```

---

## Chat Resume Scenarios

| Scenario | Action |
|---|---|
| Page refresh → `SOCKET_CONNECTED` received | Check local storage. If user info exists, call `resumeChat()` to restore the session. |
| `SOCKET_RECONNECTED` received | Call `resumeChat()` with user info from local storage. |
| `resumeChat({ serviceIdentifier, channelCustomerIdentifier }, callback)` | Returns `{ isChatAvailable: true, data: "previous chat data" }` if session is live. |

---

## Socket Event Listeners

After calling `establishConnection()`, the following event listeners are active for the duration of the chat session:

| Event | Callback Response |
|---|---|
| `connect` | `{ type: "SOCKET_CONNECTED", data: { ...socket details } }` |
| `connect_error` | `{ type: "CONNECT_ERROR", data: { ...socket details } }` |
| `disconnect` | `{ type: "SOCKET_CONNECTED", data: { ...socket details } }` |
| `CHANNEL_SESSION_STARTED` | `{ type: "CHANNEL_SESSION_STARTED", data: { ...session details } }` |
| `MESSAGE_RECEIVED` | `{ type: "MESSAGE_RECEIVED", data: { ...message details } }` |
| `CHAT_ENDED` | `{ type: "CHAT_ENDED", data: { ...end chat details } }` |
| `ERRORS` | `{ type: "ERRORS", data: { ...error details } }` |

---

## WebRTC Functions

| Action | Function Call | Related Events |
|---|---|---|
| Register user | `registerUser(event_callback)` | `registered`, `registrationFailed` |
| Initiate audio call | `sendInvite('audio', 'remoteAudio', '', userData, event_callback)` | `session-accepted`, `session-failed` |
| Initiate video call | `sendInvite('video', 'remoteVideo', 'localVideo', userData, event_callback)` | `session-accepted`, `session-failed` |
| Toggle audio mute | `audioControl()` | — |
| Toggle video pause | `videoControl()` | — |
| End call | `hangUp()` | `session-ended` |
| Unregister user | `terminateCurrentSession(event_callback)` | `unregistered` |

### WebRTC Callback Events

| Event | Description |
|---|---|
| `registered` | Customer successfully registered with EFSwitch. Proceed to initiate a call. |
| `registrationFailed` | Customer failed to register with EFSwitch. |
| `Channel Creating` | Call is dialling the DN. |
| `session-accepted` | Call connected to an agent. |
| `session-failed` | Call failed to connect. |
| `session-terminated` | Session terminated. |
| `session-confirmed` | Session confirmed. |
| `session-ended` | Session ended. |

---

## Related Articles

- [Customer Widget Features and Capabilities](../Administrator/Customer-Widget-Features-Capabilities.md)
- [WebRTC Configuration Guide](../Administrator/WebRTC-Configuration-Guide.md)
- [CIM Messages](../../Reference/Schemas_and_Data_Model/CIM_Message_Schema/CIM-Messages.md)
- [Socket Events](../../Reference/Schemas_and_Data_Model/Socket_Events/index.md)
- [Form APIs](Form-APIs.md)
