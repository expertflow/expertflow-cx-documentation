# CX Knowledgebase : JavaScript SDK for customer-facing channels

This SDK is used for embedding customer-facing channel capabilities in a mobile-app (native, hybrid) or a web-app. Developers can use their own user interface on a mobile or a web-app. 

## SDK Capabilities

With this SDK, the developer can enable the customer to:

  * start and end chat

  * Make an audio or a video call via WebRTC

  * receive system events and notifications and deliver necessary information to the customer

  * send and receive delivery notifications

  * send and receive all of the supported chat messages including rich-media messages

  * enable call controls in the customer app for audio and video calls 

  * get contact center stats ROADMAP

  * contact center available timings ROADMAP

  * get to know the availability of agents before initiating a request ROADMAP

  * get to know the expected waiting time ROADMAP




**Show If macro has stopped working**

Visibility for Confluence requires an active app subscription

### **Dependencies**

Add the following custom library to your project. 

**Name**| **Description**  
---|---  
config.js| All the required configurations related to Chat, Audio and Video Calls from client app should be in this file.  
  
## **Update Config File**

Make sure to pass following configurations from the config file to SDK.

**Properties**| **Explanation**| **Sample Value**  
---|---|---  
widgetIdentifier| String value required to get widget configurations.| widgetIdentifier = "Web"  
serviceIdentifier| String value required to get channel manager details| serviceIdentifier = "5155"  
socketUrl| String value of web channel manager IP or FQDN| socketUrl = "https://<public_ip>"  
fileServerUrl| String value of file server engine IP or FQDN| fileServerUrl = "https://<public_ip>"  
ccmUrl| String value of customer channel manager IP or FQDN| ccmUrl = "https://<public_ip>"  
transcriptUrl| String value of chat transcript IP or FQDN| transcriptUrl = "https://<public_ip>"  
channel| String value required to check client device info.| channel = "Mobile"  
  
## **Widget Configurations for webRTC**

Make sure you have access to Unified Admin Panel of the Expertflow CX. The Following configurations are needs to be added in the Web Widget Settings.

**Properties**| **Explanation**| **Sample Value**  
---|---|---  
wssServerIp| String value of EF switch IP or FQDN| wssServerIp = '192.168.1.201'  
wssServerPort| String value of EF switch webRTC port| wssServerPort = '7443'  
diallingUri| EF switch DN| diallingUri = '369852'  
sipExtension| Extension dedicated for dialling| sipExtension = 'ext'  
extensionPassword| Extension password for registration| extensionPassword = 'password'  
webSocket| String value required to get web socket.| webSocket =  _"ws"_  
iceServers| Set of array values required to get servers| iceServers : [{"urls": [ "stun: [stun.l.google.com](http://stun.l.google.com):19302", "stun: [stun1.l.google.com](http://stun1.l.google.com):19302"]}]  
form| Pre-chat form Id from Unified Admin Forms| form = "12312312sdfsdf23123"  
  
## **In-App Customer Channels with our SDKs & CDN links**

This is fully customizable and easy to use. Now, it has become possible with Expertflow CX's SDKs and CDN links for

  * In-App Chat

  * Voice and

  * Video Calling Widgets.




### **Web Application SDK as CDN Link**

##### **Normal CDN Script**
[code] 
    <script src="https://cdn.jsdelivr.net/gh/expertflow/sdk-for-customer-facing-channels@latest/sdk.js"></script>
[/code]

##### **Minified CDN Script**
[code] 
    <script src="https://cdn.jsdelivr.net/gh/expertflow/sdk-for-customer-facing-channels@latest/sdk.min.js"></script>
[/code]

**Note** : Just add any of these CDN script into the head tag of html file to enable the SDK. 

### **Native Application SDK as NPM Installer Package**

##### **NPM Command**
[code] 
    npm i @expertflow/sdk-for-customer-facing-channels
[/code]

**Note** : Just run this command in the directory of the project root to enable the SDK. For complete reference [click here](https://www.npmjs.com/package/@expertflow/sdk-for-customer-facing-channels).

##### **Customer Data Payload**
[code] 
    {
    
           serviceIdentifier : "2342342",
    
           channelCustomerIdentifier : "2342342342",
    
           browserDeviceInfo : {
    
                  browserId : '123124',
    
                  browserIdExpiryTime :  '9999',
    
                  browserName : 'chrome',
    
                  deviceType : 'desktop'
    
            },
    
           queue : ' ',
    
           locale : {
    
                  timezone : 'asia/karachi',
    
                  language : 'english',
    
                  country : 'pakistan'
    
             },
    
           formData : {
    
                  attributes : [{ 
    
                                     value : 'test',
    
                                     key : 'firstName',
    
                                     type : 'string'
    
                 }, ...],
    
           createdOn : "Standard GMT DateTime",
    
           filledBy : "web-init",
    
           formId : "0.0313465461351",
    
           id : "0.1025556665461"
    
           }
    
    }
[/code]

## **All About SDK Chat Functions**

**S.No#**| **Function**| **Parameters**| **Sample Payload/Data**| **Sample Response**  
---|---|---|---|---  
1| **widgetConfigs(**_ccmUrl, widgetIdentifier, callback_**)**| 

  * ccmUrl → Customer Channel Manager Url.
  * widgetIdentifier → Widget Identifier.
  * callback → callback function with the response data.

| ccmUrl → 'https://<public FQDN>'widgetIdentifier → 'Web' → case sensitive| {  
id: "629dd96ac2fc5e06bf842c19",  
widgetIdentifier : "123123",  
theme : "yellow_theme",  
title : "Dummy widget",  
subTitle : "Call center",  
enableFontResize : true,  
enableEmoji : true,  
enableFileTransfer : true,  
enableDynamicLink : true,  
enableDownloadTranscript : true,  
customerReconnectTime : 100,  
language : {  
code : "en",  
policy : null  
},  
webRtcConfig : {  
serverIp : "192.168.1.23", ... }  
}  
2| **establishConnection(** serviceIdentifier, channelCustomerIdentifier, callback**)**| 

  * serviceIdentifier → Service Identifier to identify the service in channel manager.
  * channelCustomerIdentifier → Customer Channel Identifier to identify the customer.
  * callback → Callback function with the response data.

|   
| In Callback Response socket returns an object{ type : "SOCKET_CONNECTED", data : { socket connection details. } }  
3| **chatRequest(**_data_**)**| 

  * data → includes an object with type "CHAT_REQUEST" and customer information in data

| { type : "CHAT_REQUEST", data : { See Customer Data Section at the last for Payload }}| In Callback Response socket returns an object of channel session start{ type : "CHANNEL_SESSION_STARTED", data : { channel session details. } }  
4| **sendMessage(**_data_**)** For cimMessage Payload****[**click here**](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/686522810/4.6+CIM+Messages)| 

  * data → parameter includes message payload.

| check **cimMessage** section for different messages payload.| In Callback Response socket returns an object{ type : "MESSAGE_RECEIVED", data : { message details [click here](https://docs.expertflow.com/x/7qSgC) } }  
5| **chatEnd(**_data_**)**| 

  * data → parameter includes customer information.

| check customer information payload | In Callback Response socket returns an object { type : "CHAT_ENDED", data : { end chat details }}  
6| **uploadToFileEngine(**_data, callback_**)**| 

  * data → File data includes file name and random 5 digits number.


  * callback → function to call right after file upload.

| { file : "file name with ext", conversationId : random 5 digits number}| In Callback Response, Api returns an object { message : "File uploaded successfully", etag:"9109239e595cd2706c3b2180594351b6",name:"13318_developer.png",type:"image/png",size:52991}  
7| **setConversationData(**_conversationUrl_ , _conversationId_ , _data_**)**| 

  * conversationId → Conversation Id received on chat session start.
  * conversationUrl → Conversation Manager Url
  * data → data includes any data in the form of key value pair e.g: form data.

|   
|   
  
8| **getConversationData(**_conversationUrl_ , _conversationId_**)**| 

  * conversationId → Conversation Id received on chat session start.
  * conversationUrl → Conversation Manager Url

|   
|   
  
9| **getPreChatForm(**_formUrl, formId, callback_**)**| 

  * fomUrl → Unified Admin form Url
  * formId → Form Id Received in widgetConfigs response
  * callback → Call any function to render that form.

|   
|   
  
  
## **Chat Resume Scenarios**

**S.No#**| **Function**| **Parameters**| **Scenarios**| **Sample Response**  
---|---|---|---|---  
1| **establishConnection(** serviceIdentifier, channelCustomerIdentifier, callback**)**| 

  * serviceIdentifier → Service Identifier to identify the service in channel manager.
  * channelCustomerIdentifier → Customer Channel Identifier to identify the customer.
  * callback → Callback function wFith the response data.

| On page refresh if you get SOCKET_CONNECTED event then you first need to check the local storage. If user information (serviceIdentifier, channelCustomerIdentifier) is stored in local storage that means the session already exists and you need to send a chat resume request with that information| { type : "SOCKET_CONNECTED", data : { socket connection details. } }  
2| **establishConnection(** serviceIdentifier, channelCustomerIdentifier, callback**)**| 

  * serviceIdentifier → Service Identifier to identify the service in channel manager.
  * channelCustomerIdentifier → Customer Channel Identifier to identify the customer.
  * callback → Callback function wFith the response data

| If you receive a SOCKET_RECONNECTED event, you should call the chat resume function with user information (get that information from local storage or from anywhere you store that information)|   
3| **resumeChat(**{ serviceIdentifier, channelCustomerIdentifier },callback**)**| 

  * serviceIdentifier → Service Identifier to identify the service in channel manager.
  * channelCustomerIdentifier → Customer Channel Identifier to identify the customer.
  * callback → Callback function with the response data.

| | {  
"isChatAvailable": true,  
"data": "previous chat data"  
}  
  
## **Socket Event Listeners**

On calling **establish_connection( )** function → following Event Listeners are enabled during chat session and return an object in callback response. 

**S.No#**| **Socket Event Listener**| **Callback Response**  
---|---|---  
1| connect| { type : "SOCKET_CONNECTED", data: { ... socket details }}  
2| connect_error| { type : "CONNECT_ERROR", data: { ... socket details }}  
3| disconnect| { type : "SOCKET_CONNECTED", data: { ... socket details }}  
4| CHANNEL_SESSION_STARTED| { type : "CHANNEL_SESSION_STARTED", data: { ... socket details }}  
5| MESSAGE_RECEIVED| { type : "MESSAGE_RECEIVED", data: { ... socket details }}  
6| CHAT_ENDED| { type : "CHAT_ENDED", data: { ... socket details }}  
7| ERRORS| { type : "ERRORS", data: { ... socket details }}  
  
## **All about WebRTC functions in SDK**

**Action**| **Message Parameters**| **Sample Request**| **Related Events**| **Comments**  
---|---|---|---|---  
  
#### Register User

| event callback| registerUser(event_callback);  
| Agent Registration EventAgent Registration Failed|   
  
  
  
  
  
#### Initiate a Call (Audio/ Video)

| <calltype>→ audio (initiating audio call)→ video (initiating video call for web channel only) <mediaStreamID>→ id assigned to the audio media stream→ id assigned to the video media stream<localmediaStreamID>→ id assigned to the local video media stream**Note:** mediaStreamID,localmediaStreamID are for **web channel**. set them to empty string for **mobile channel.** <customerData>→ **Sample payload**   

[code] 
    let userData = {
                    "first_name": name,
                    "last_name": last_name,
                    "email": email,
                    "Customer-Caller-Id-number": number
                  }
[/code]

  
| sendInvite('audio','remoteAudio','',userData,event_callback)| confirmed  
session-acceptedsession-failed|   
  
  
#### Toggle audio

|   
| audioControl();  
|   
| if the audio is mute it would be unmuted and wise versa  
**(Currently this is for web channel only)**  
  
#### Toggle video

|   
| videoControl();  
  
|   
| if the video is paused it would be unpaused and wise versa   
**(Currently this is for web channel only)**  
  
#### End Call

|   
| hangUp();|   
session-ended|   
  
  
#### Unregister User 

|   
| terminateCurrentSession(event_callback);  
| unregistered| in order to call the call audio or video.  
  
### Event Received on Callback for WebRTC

All the events are received in the callback function named **events_callback(event)** the sipcontrol.js look for this function calls if you have implemented it with event parameters.

In order to initiate a webRTC audio or video call, chat customers should be registered with EFswitch, when you calls Initiate a Call(Audio/ Video) command it tries to register an agent and sends the respective callback.

  
| **Event**| **Description**| **Payload**  
---|---|---|---  
1| 

#### Agent Registration Event

| if the customer is successfully registered sends this messagenow you need to call an**Initiate a Call (Audio/ Video)** command to start call initiation.| `{`  
` 'event'` `: 'registered',`  
` 'response'` `:`  
` {`  
` `  
` }`  
`};`  
2| 

#### Agent Registration Failed

| if the customer is unable to register to EF switch then it sends this error message | `{`  
` 'event'` `: 'registrationFailed',`  
` 'response'` `:`  
` {`  
` `  
` }`  
`};`  
3| 

#### Start Initiating a Call

| when your call has started dialling DN. | `{`  
` 'event'` `: 'Channel Creating',`  
` 'response'` `:`  
` {`  
` `  
` }`  
`};`  
4| 

#### Call Answered

| when your call has been connected to the agent we receive a callback event | `{`  
` 'event'` `: 'session-accepted',`  
` 'response'` `:`  
` {`  
` `  
` }`  
`};`  
5| 

#### Fail to connect to an agent

| calls **End Call (Audio/Video)** command | `{`  
` 'event'` `: 'session-failed',`  
` 'response'` `:`  
` {`  
` `  
` }`  
`};`  
6| 

#### Session Terminated

| when the session is terminated it sends this message| `{`  
` 'event'` `: 'session-terminated',`  
` 'response'` `:`  
` {`  
` `  
` }`  
`};`  
7| 

#### Session Confirmed

| when session is confirmed it sends this message| `{`  
` 'event'` `: 'session-confirmed',`  
` 'response'` `:`  
` {`  
` `  
` }`  
`};`  
8| 

#### Session Ended

| when session is ended it sends this message| `{`  
` 'event'` `: 'session-ended',`  
` 'response'` `:`  
` {`  
` `  
` }`  
`};`  
  
  

