# CX Knowledgebase : CX Media Server API

CX Media Server API is to establish communication between the Media Server and Agent Desk. When an agent wants to initiate voice calls via SIP, then this API is used. 

This API can be used either as a standalone implementation or with EFCX.

###   
API Version Compatibility with ExpertFlow CX versions

The following table matches the compatibility of API with Expertflow CX:

**EFCX Version**| **SIP JS Version**  
---|---  
4.5.3| `3.2.8_b-CIM-15311`  
4.6| `3.2.9_b-EMR-4039`  
4.7| `3.3`  
4.8| `3.4`  
4.9| `3.5`  
4.9.1 / 4.9.2 / 4.9.5| `3.6`  
4.10 / 4.10.1 / 4.10.3| `3.7`  
  
  
To send commands, you need to import certain libraries of Media Server. For this authentication is required, please contact RTC team for assistance. 

### Sample Commands
[code] 
    {
    				"action": "login",
    				"parameter":
    				{
    					"loginId": "jazeb",
    					"password": "1234",
    					"extension": "448899",
    					"clientCallbackFunction": eventCallback
    				}
    			};
[/code]

### Commands for CTI

| **Story**| **Description**| **Commands**| **Events**  
---|---|---|---|---  
1| login| The Login command is used to actually Register an agent associated extension and log in to CTI. Login command parameters are

  * Agent Login ID (Agent Name)
  * Password (Extenstion password and Agent password must be same)
  * extension 

First JS API will register extension to webphone, If Registeration got failed, the following event will be thrown Following errors are possible:

  1. subscriptionFailed
  2. networkIssue

If a Registeration is successful, will send the following event. agentState and dialogState events. Now the agent will be able to make and receive calls on the client application.| **Sample**

##### **Sample**
[code] 
    {
    				"action": "login",
    				"parameter":
    				{
    					"loginId": "jazeb",
    					"password": "1234",
    					"extension": "448899",
    					"clientCallbackFunction": eventCallback
    				}
    			};
[/code]

| **Successful Events :**

  1. agentInfo
  2. dialogState

**Failure Events :**

  1. subscriptionFailed
  2. invalidState

  
2| makeCall| This command allows a user to make a call. To make a call, a new Dialog object is created that specifies the <Extension_Number> (the destination target). The new Dialog object is posted to the Dialog collection for that user. Here **callType** parameter value would be audio/video/screenshare| **Sample**   


##### **Sample**
[code] 
    {
    "action": "makeCall",
    "parameter":
    {
    "callType" : "audio",
    "Destination_Number":"1777",
    "calledNumber": "1777",
    "clientCallbackFunction": eventCallback
    }
    }
    
[/code]

| 

  1. outboundDialing(INITIATING, INITIATED)
  2. dialogState (ACTIVE)

  
3| makeOBCall| This command allows a user to make a Manual Outbound call. To make a call, a new Dialog object is created that specifies the (the destination target). The new Dialog object is posted to the Dialog collection for that user. Here **callType** parameter value would be audio| **Sample**

##### **Sample**
[code] 
    {
    "action": "makeOBCall",
    "parameter":
    {
    "callType" : "audio",
    "Destination_Number":"1777",
    "calledNumber": "1777",
    "clientCallbackFunction": eventCallback
    }
    }
    
[/code]

| 

  1. outboundDialing(INITIATING, INITIATED)
  2. dialogState (ACTIVE)

  
4| answerCall| This command allows a user to answer a call.   
  
Here **answerCalltype** parameter value would be audio/video/screenshare/onlyviewscreenshare  
| **Sample**   


##### **Sample**
[code] 
    {
    				"action": "answerCall",
    				"parameter":
    				{
    					"dialogId": "c1cc4fb6-3676-123b-ea94-005056bc90cf",
    					"clientCallbackFunction": eventCallback,
    					"answerCalltype" : "audio"
    				}
    			};
[/code]

| 

  1. dialogState(ACTIVE)

  
5| releaseCall| This command allows a user to drop a call. | **Sample**  


##### **Sample**
[code] 
    {
    	"action" 	: "releaseCall",
    	"parameter"	:
    		{
          "dialogId": "c1cc4fb6-3676-123b-ea94-005056bc90cf"
    		}
    };
[/code]

| 

  1. dialogState(DROPPED)

  
6| holdCall| This command allows a user to hold a call| 

##### **Sample**
[code] 
    {
    				"action": "holdCall",
    				"parameter":
    				{
    					"dialogId": "c1cc4fb6-3676-123b-ea94-005056bc90cf",
    					"clientCallbackFunction": eventCallback
    				}
    			};
[/code]

| 

  1. dialogState(HELD)

  
7| retrieveCall| This command allows a user to Resume a call. | 

##### **Sample**
[code] 
    {
    				"action": "retrieveCall",
    				"parameter":
    				{
    					"dialogId": "c1cc4fb6-3676-123b-ea94-005056bc90cf",
    					"clientCallbackFunction": eventCallback
    				}
    			};
[/code]

| 

  1. dialogState(ACTIVE)

  
8| logout| This command will logout the agent from the CTI| 

##### **Sample**
[code] 
    {
    				"action": "logout",
    				"parameter":
    				{
    					"reasonCode": "Logged Out",
    					"userId": "448899",
    					"clientCallbackFunction": eventCallback
    				}
    			};
[/code]

| 

  1. agentState

  
9| mute| This command will mute the audio of call from agent side.   
  
| 
[code] 
    {
       "action": "mute_call",
        "parameter":
         {
             "clientCallbackFunction": eventCallback,
             "dialogId": "c1cc4fb6-3676-123b-ea94-005056bc90cf",
          }
    }
    
[/code]

| 

  1. dialogState(participants.mute = true)

  
10| unmute| This command will unmute the audio of call from agent side. | 
[code] 
    {
    				"action": "unmute_call",
    				"parameter":
    				{
    					"dialogId": "c1cc4fb6-3676-123b-ea94-005056bc90cf",
    					"clientCallbackFunction": eventCallback,
    				}
    			}
[/code]

| 

  1. dialogState(participants.mute = false)

  
11| SST (blind transfer)| This command allows a user to transfer the call on agent extension blindly without waiting for the other agent to receive the call.| 
[code] 
    {
    				"action": "SST",
    				"parameter":
    				{
    					"dialogId": "0334343",
    					"numberToTransfer":"99887766",
    					"clientCallbackFunction": eventCallback
    				}
    			}
[/code]

| **Agent A**

  1. dialogState(DROPPED)

**Agent B**

  1. newInboundCall

  
12| SST_Queue(Blind transfer on queue)| This command allows a user to transfer the call on queue blindly.| 
[code] 
    {
    				"action": "SST_Queue",
    				"parameter":
    				{
    					"dialogId": "0334343",
    					"queue":"queue_name",
    					"queueType ":"queueType ",
    					"clientCallbackFunction": eventCallback,
    					"numberToTransfer" : "00000000"					}
    			}
[/code]

| **Agent A**

  1. dialogState(DROPPED)

**Agent B**

  1. newInboundCall

  
13| ConsultCall| This command allows a user to initiate a consult call with another agent. Once the call is accepted by the other agent, the user can either transfer this call to the other agent or can drop the consult call. | 
[code] 
    {
    				"action": "makeConsult",
    				"parameter":
    				{
    					"numberToConsult":"4488992",
    					"clientCallbackFunction": eventCallback
    				}
    			
[/code]

| **For Agent A:**

  1. dialogState(Held)  

  2. consultCall (Initiating)
  3. consultCall (Initiated)

**For agent B:**

  1. consultCall (Alerting)

  
14| ConsultCall_Queue  
  
| This command allows a user to initiate a consult call with another agent using Queue. Once the call is accepted by the other agent, the user can either transfer this call to the other agent or can drop the consult call. | 
[code] 
    {
    				"action": "makeConsultQueue",
    				"parameter":
    				{
    					"numberToTransfer":"99887766",
    					"queue":"65bb2dcbba1aab2d0a4742d6",
    					"queueType":"ID",
    					"clientCallbackFunction": eventCallback,
    				}
    			}
    
[/code]

| **For Agent A:**

  1. dialogState(Held)  

  2. consultCall (Initiating)
  3. consultCall (Initiated)
  4. consultCall (Active)

**For agent B:**

  1. consultCall (Alerting)

  
15| Consult Transfer  
  
| This command allows a user to merge / Bridge Customer Call with another agent. The Other agent must be in Call with First Agent.| 
[code] 
    {
    				"action": "consultTransfer",
    				"parameter":
    				{
    					"clientCallbackFunction": eventCallback
    				}
    			}
    
[/code]

| **For Agent A:**

  1. consultCall (Drop)
  2. dialogState(Drop)

**For agent B:**

  1. consultCall (Drop)
  2. dialogState(Active)

  
16| Consult Conference| This command allows a user to initiate a consult conference with the Consulted agent and the customer| 
[code] 
    {
        "action": "conference_consult",
        "parameter": {
            "dialogId": "mnsghhjec8ncflpgfcv2",
            "clientCallbackFunction" : eventCallback
        }
    }
[/code]

| **For Agent A:**

  1. consultCall (Drop)
  2. dialogState(Active)

**For agent B:**

  1. consultCall (Drop)
  2. dialogState(Active)

  
17| SendDtmf| This command allows user to send dtmf during the IVR playing.Here **message** is the dtmf that we need to send. | 
[code] 
    postMessages({
    "action": "SendDtmf",
    "parameter":
    {
    "dialogId": dialogid,
    "message":"1",
    "clientCallbackFunction": eventCallback
    }
    });
    
[/code]

| 

  1. DTMF

  
18| Click To Call| This command will allow user to make call in cross domain like if the user domain is different then the FS JS API domain then user must send us window.postMessage that contains required parameters. 

  * callType
  * Destination_Number
  * calledNumber

Here above are dynamic values while SourceType value will remain static | 
[code] 
    var obj = {
        "callType" : "audio",//audio/video/screenshare
        "Destination_Number":"1777",
        "calledNumber": "1777",
        "SourceType" : "CTI"
        }
        window.postMessage(obj, "*"); // "*" means sending to all origins
    
[/code]

| 

  1. outboundDialing(INITIATING, INITIATED)

  
19| ConvertCall| This Command will allow the user to Enable / Disable Stream while in webrtc Call.  
stream: video / screensharestreamStatus: on / off| 
[code] 
    {
    				"action": "convertCall",
    				"parameter":
    				{
    					"dialogId": "c1cc4fb6-3676-123b-ea94-005056bc90cf",
    					"clientCallbackFunction": eventCallback,
    					"streamStatus" : streamStatus ,    //on , off
    					"streamType" : streamType   //screenshare, video
    
    				}
    			}
    
[/code]

| 

  1. mediaConversion(success)

  
20| Silent Monitor| This command allows the supervisor to silently monitor a call.  
  
| 
[code] 
    {
    				"action": "silentMonitor",
    				"parameter":
    				{
    					"calledNumber":  "1777",
                        "callType": "audio",
                        "Destination_Number": "1777",
    					"service_Identifier": serviceIdentifier,
    					"clientCallbackFunction": eventCallback
    				}
    			}
    
[/code]

| 

  1. outboundDialing(INITIATING, INITIATED)
  2. dialogState (ACTIVE)

  
21| BargeIn| This command allows the supervisor to BargeIn on a call after a silent monitoring session has been established.| 
[code] 
    {
    "action": "bargeIn",
    "parameter":
    {
    "clientCallbackFunction": eventCallback,
    "dialogId" : dialogId,
    }
    }
    
[/code]

| 

  1. dialogState (Dropped)
  2. dialogState (ACTIVE)

  
  
### Event for CTI

1| agentInfo|  JS API sends this event when the device logged in successfully with state LOGIN. This event will never be sent again in a session| **Sample**

##### **Sample**
[code] 
    {
        "event": "agentInfo",
        "response": {
            "loginId": "448899",
            "extension": "448899",
            "state": "LOGIN",
            "cause": "null"
        }
    }
[/code]

##### **Sample**
[code] 
    {
        "event": "agentInfo",
        "response": {
            "loginId": "448899",
            "extension": "448899",
            "state": "LOGOUT",
            "cause": "Connection Error"
        }
    };
[/code]

Possible value for state

  * LOGIN
  * LOGOUT

  
---|---|---|---  
2| dialogState|  Dialog state event represents the current state of the dialog.| Use both dialog's state and participant's state provided in response JSON object to figure out call state.  
**Sample**

##### **Sample**
[code] 
    {
        "event": "dialogState",
        "response": {
            "loginId": null,
            "dialog": {
                "id": null,
                "fromAddress": null,
                "dialedNumber": null,
                "customerNumber": null,
                "dnis": null,
                "serviceIdentifier": null,
                "callType": null,
                "ani": null,
                "wrapUpReason": null,
                "wrapUpItems": null,
                "callEndReason": null,
                "queueName": null,
                "queueType": null,
                "associatedDialogUri": null,
                "secondaryId": null,
                "participants": [
                    {
                        "actions": {
                            "action": [
                                "TRANSFER_SST",
                                "HOLD",
                                "SEND_DTMF",
                                "DROP"
                            ]
                        },
                        "mediaAddress": null,
                        "mediaAddressType": "SIP.js/0.21.2-CTI/Expertflow",
                        "startTime": null,
                        "state": null,
                        "stateCause": null,
                        "stateChangeTime": null,
                        'mute': false
    
                    },
                ],
                "callVariables": {
                    "CallVariable": []
                },
                "state": null,
                "isCallAlreadyActive": false,
                "callbackNumber": null,
                "outboundClassification": null,
                "scheduledCallbackInfo": null,
                "isCallEnded": 0,
                "eventType": "PUT",
                "mediaType":null,
                "channelType": "WEB_RTC",
                "primaryDN": null
    
            }
        }
    }
[/code]

The current state of the dialog. Possible values are:

  * INITIATING
  * INITIATED
  * ALERTING
  * ACTIVE
  * F~~AILED~~
  * DROPPED
  * ~~ACCEPTED~~

  
3| newInboundCall| This event occurs when an incoming call is ringing for the agent. This event specifies from address, call variables, and dialog id for the agent. The client needs to activate the control for accepting or rejecting the call. | **Sample**

##### **Sample**
[code] 
    {
        "event": "newInboundCall",
        "response": {
            "loginId": null,
            "dialog": {
                "id": null,
                "ani": null,
                "customerNumber": null,
                "associatedDialogUri": null,
                "callbackNumber": null,
                "outboundClassification": null,
                "scheduledCallbackInfo": null,
                "isCallEnded": 0,
                "eventType": "PUT",
                "callType": null,
                "queueName": null,
                "queueType": null,
                "dialedNumber": null,
                "dnis": null,
                "serviceIdentifier": null,
                "secondaryId": null,
                "state": "ALERTING",
                "isCallAlreadyActive": false,
                "wrapUpReason": null,
                "wrapUpItems": null,
                "callEndReason": null,
                "fromAddress": null,
                "callVariables": {
                    "CallVariable": []
                },
                "participants": [
                    {
                        "actions": {
                            "action": [
                                "ANSWER",
                            ]
                        },
                        "mediaAddress": null,
                        "mediaAddressType": "SIP.js/0.21.2-CTI/Expertflow",
                        "startTime": null,
                        "state": null,
                        "stateCause": null,
                        "stateChangeTime": null,
                        'mute': false
                    },
                ],
                "mediaType":null,
                "channelType": "WEB_RTC",
                "primaryDN": null
            }
        }
    }
    
[/code]  
  
4| outboundDialing| This event will trigger when the user starts the outbound Dialing| **Sample**

##### **Sample**
[code] 
    {
        "event": "outboundDialing",
        "response": {
            "loginId": "448899",
            "dialog": {
                "id": "0lsns4ou3n9bi7erg9lq",
                "ani": "448866",
                "customerNumber": "448866",
                "associatedDialogUri": null,
                "callbackNumber": null,
                "outboundClassification": null,
                "scheduledCallbackInfo": null,
                "isCallEnded": 0,
                "eventType": "PUT",
                "callType": "OUT",
                "queueName": null,
                "dialedNumber": "448866",
                "dnis": "448866",
                "serviceIdentifer" : 448899,
                "secondaryId": null,
                "state": "INITIATING",
                "isCallAlreadyActive": false,
                "wrapUpReason": null,
    			"wrapUpItems": null,
                "callEndReason": null,
                "fromAddress": "448899",
                "callVariables": {
                    "CallVariable": []
                },
                "participants": [
                    {
                        "actions": {
                            "action": [
                                "TRANSFER_SST",
                                "HOLD",
                                "SEND_DTMF",
                                "DROP"
                            ]
                        },
                        "mediaAddress": "448899",
                        "mediaAddressType": "SIP.js/0.15.11-CTI/Expertflow",
                        "startTime": "2023-06-20T08:51:35.993Z",
                        "state": "INITIATING",
                        "stateCause": null,
                        "stateChangeTime": "2023-06-20T08:51:35.993Z",
                        "mute": false
                    }
                ],
                "mediaType":null,
                "callOriginator" : "webrtc"
            }
        }
    }
[/code]  
  
5| consultCall | This event informs the client about the current state of consult call for an agent. The current state of the dialog. Possible values are:

  * INITIATING
  * INITIATED
  * ALERTING
  * ACTIVE
  * DROPPED

| 

##### **Sample**
[code] 
    {
        "event": "ConsultCall",
        "response": {
            "loginId": null,
            "dialog": {
                "id": null,
                "ani": null,
                "customerNumber": null,
                "associatedDialogUri": null,
                "callbackNumber": null,
                "outboundClassification": null,
                "scheduledCallbackInfo": null,
                "isCallEnded": 0,
                "eventType": "PUT",
                "callType": null,
                "queueName": null,
                "queueType": null,
                "dialedNumber": null,
                "dnis": null,
                "serviceIdentifier": null,
                "secondaryId": null,
                "state": "INITIATING",
                "isCallAlreadyActive": false,
                "wrapUpReason": null,
                "wrapUpItems": null,
                "callEndReason": null,
                "fromAddress": null,
                "callVariables": {
                    "CallVariable": []
                },
                "participants": [
                    {
                        "actions": {
                            "action": [
                                "TRANSFER_SST",
                                "HOLD",
                                "SEND_DTMF",
                                "DROP"
                            ]
                        },
                        "mediaAddress": null,
                        "mediaAddressType": "SIP.js/0.21.2-CTI/Expertflow",
                        "startTime": null,
                        "state": null,
                        "stateCause": null,
                        "stateChangeTime": null,
                        'mute': false
                    },
                ],
                "mediaType":null,
                "channelType": "WEB_RTC",
                "primaryDN": null
            }
        }
    }
[/code]  
  
6| RONA| The customer initiated the call and the call is ringing on the agent's side, the agent does not accept the call and alerting/ringing times outThe customer initiated the call and the call is ringing on the agent's side, and the customer ends the call.In above both case the value of the key **endCallReason** would be **Canceled** in dialogState event. | 
[code] 
    {
        "event": "dialogState",
        "response": {
            "loginId": "448899",
            "dialog": {
                "id": "2a8f41ba-579d-123c-c78a-005056bc90cf",
                "fromAddress": "448866",
                "dialedNumber": "258963",
                "serviceIdentifer" : 258963,
                "customerNumber": "448866",
                "dnis": "911",
                "callType": "OTHER_IN",
                "ani": "448866",
                "wrapUpReason": "Queue Call",
                "queueName": null,
                "associatedDialogUri": null,
                "secondaryId": null,
                "participants": {
                    "Participant": [
                        {
                            "actions": {
                                "action": [
                                    "TRANSFER_SST",
                                    "HOLD",
                                    "SEND_DTMF",
                                    "DROP"
                                ]
                            },
                            "mediaAddress": "448899",
                            "mediaAddressType": "SIP.js/0.15.11-CTI/Expertflow",
                            "startTime": "2023-4-17 13:32:0",
                            "state": "DROPPED",
                            "stateCause": null,
                            "stateChangeTime": "2023-3-17 13:32:19",
                            "localstream": null,
                            "remotestream": null,
                            "mute": false
                        }
                    ]
                },
                "callVariables": {
                    "CallVariable": [
                        {
                            "name": "callVariable0",
                            "value": "507d8a23-71b2-43e0-919a-09d125fa51ab"
                        },
                        {
                            "name": "callVariable1",
                            "value": "Umer"
                        },
                        {
                            "name": "callVariable2",
                            "value": "Saeed"
                        },
                        {
                            "name": "callVariable3",
                            "value": "Model Town"
                        },
                        {
                            "name": "callVariable4",
                            "value": "08-December-2008"
                        },
                        {
                            "name": "callVariable5",
                            "value": "03401234567"
                        },
                        {
                            "name": "callVariable6",
                            "value": "Japan"
                        },
                        {
                            "name": "callVariable7",
                            "value": "80094"
                        },
                        {
                            "name": "callVariable8",
                            "value": "34618-8449511-7"
                        },
                        {
                            "name": "callVariable9",
                            "value": "Japanese"
                        },
                        {
                            "name": "callVariable10",
                            "value": "05145679"
                        }
                    ]
                },
                "state": "Canceled",
                "callbackNumber": null,
                "outboundClassification": null,
                "scheduledCallbackInfo": null,
                "isCallEnded": 0,
                "eventType": "PUT"
            }
        }
    }
[/code]  
  
7| xmppEvent| This event will be triggered when network connection status changes i.e it will be triggered when network status is connected or disconnected.| 
[code] 
    {
        "event" : "xmppEvent",
        "response" :
        {
            "loginId" : username,
            "type" : "IN_SERVICE",
            "description":"connected",
        }
    }
[/code]

types:OUT_OF_SERVICEIN_SERVICE  
8| DTMF| This event will be triggered when we send DTMF during IVR playing. | 
[code] 
    {
                        "event": "DTMF",
                        "response":
                        {
                            "loginId": loginid,
                            "type": 0,
                            "description": "Failure response ",
                        }
                    }
    
[/code]

type:1 for success response0 for failure response   
9| mediaStreamUpdate| This Event will be triggered when any Participant of the webrtc call enable/disable a stream| 
[code] 
    {
        "event": "mediaStreamUpdate",
        "status": null,
        "loginId": "",
        "dialog": {
            "id": null,
            "eventRequest": null,
            "stream": null,
            "streamStatus":null,
            "errorReason": null, 
            "timeStamp": null 
        }
    }
[/code]

status: error/success  
event request: local / remote  
stream: video / screenshare  
streamStatus: on / off  
  
  
  
### Error Event for CTI

| **Error Event Types**| **Description**| **Events**  
---|---|---|---  
1| subscriptionFailed| This error occurs when JS API tries to get a subscription of an agent with supplied credentials and those credentials are invalid.| **Sample**

##### **Sample**
[code] 
    {
    	"event"		: "Error",
    	"response"	: 
    		{
    "type":"subscriptionFailed",
     "loginId":"Malik 3",
     "description":"Invalid Username or Password"/"INVALID_DOMAIN"   }
    };
[/code]  
  
2| generalError| We define its type as general error and its description will tell what is the root cause of this error.| **Sample**

##### **Sample**
[code] 
    {
    	"event"		: "Error",
    	"response"	: 
    		{
    "type":"generalError",
     "loginId":"1234",
     "description":"XMPP Connection Failed"
    		}
    };
[/code]

In some cases description can also be "description": "Sorry we are unable to process your request"  
3| invalidState| The object is in the incorrect state for the request, Send the request again.| 

##### **Sample**
[code] 
    {
        "event": "Error",
        "response": {
            "type": "invalidState",
            "loginId": null,
            "description": "The object is in the incorrect state for the request makeCall",
            "event_time": "2023-5-13 3:22:51.778"
        }
    };
[/code]  
  
**SR No**| **Parameter**| **Details**  
---|---|---  
1| callType| callTypes ={  
inboundType : "OTHER_IN",  
outboundType : "OUT",  
consultType : "CONSULT",  
externalConsult: “EXTERNAl-CONSULT”,  
externalConsultType : "EXTERNAL-CONSULT",  
consultTransferType : "CONSULT_TRANSFER",  
bargeInType: "BARGE_CONFERENCE",  
consultConferenceInType: "CONSULT_CONFERENCE",  
externalConsultConferenceType: "EXTERNAL_CONSULT_CONFERENCE"  
}
