# CX Knowledgebase : Updating Environment Variables for WebRTC

## Agent Desk Variables

### Disclaimer

  * Assuming that the deployed Media Server instance has self-signed certificates. In that case, the certificates should be added manually in the browser using https://<Media-Server-IP>:<PORT, before trying to log in and connect to the Media Server.




  * On the CX deployment machine, navigate to the following path, 
[code] vi <cx-install-dir>/kubernetes/helm-values/cx-agent-desk-custom-values.yaml
[/code]

  * Update the following config to _**true**_ in case the Media Server environment is to be enabled in the unified-agent environment variables.
[code] "isCxVoiceEnabled": "<boolean>", // to be set to `true`, if system is being used with the Media Server 
[/code]

  * Update the following **Sip.js** config variables added in the unified-agent configurations.
[code] "SIP_SOCKET_URL": "<wss://Media-Server-IP-addr:7443>",
        "SIP_URI": "<Media Server Domain/IP>",
        "EXT_STATIC": "<Encrypted Static Password Set For Media Server Extensions>",
        "ENABLE_SIP_LOGS": "<SIP_LOGS>", // to be set to true if sip.js logs are required
        "Enable_Voice_Events_For_CRM": "<boolean>" // to expose Voice events via Sip.js for third party applications
[/code]

  * If the _MRD_ associated with the _WebRTC_ channel type is changed, it must be updated in the following environment variable.
[code] "CX_VOICE_MRD": "<MRD associated with CX_VOICE channel type>"
[/code]

  * Update the following config variable added in the unified-agent configurations to enable video calls.
[code] "IS_WEBRTC_VIDEO_ENABLED": "<boolean>" // to be set to `true`, if video calls are to be enabled
[/code]

  * Save the file and run the following sequence of commands in the _**< cx-install-dir>/kubernetes**_ directory:
[code] helm upgrade --install --namespace expertflow   --set global.efCxReleaseName="ef-cx"  cx-agent-desk  --debug --values helm-values/cx-agent-desk-custom-values.yaml expertflow/agent-desk
[/code]

  * Log out of your voice agents and reload **Agent Desk**.




## Customer Widget Variables 

  * On the CX deployment machine, navigate to the following path, 
[code] vi <cx-install-dir>/kubernetes/helm-values/ef-cx-custom-values.yaml
[/code]

  * Navigate to the _**customer-widget**_ section.




Both of the following variables cannot be _**true**_ at the same time for audio calls, whereas they can be simultaneously true if video calls are to be configured.

  * The following variable should be set to `true` to enable audio calls from the customer widget.
[code] "IS_DIRECT_WEBRTC_CALL_ENABLED": "<boolean>"
[/code]

  * The following variable should be set to `true` to enable video calls from the customer widget.
[code] "VIDEO": "<boolean>"
[/code]

  * The following variable value should be set to `phone` to enable WebRTC calls on the customer widget.
[code] "CHANNEL_IDENTIFIER": "phone"
[/code]

  * Save the file and run the following sequence of commands in the _**< cx-install-dir>/kubernetes**_ directory:
[code] helm upgrade --install --namespace expertflow --create-namespace   ef-cx  --debug --values helm-values/ef-cx-custom-values.yaml expertflow/cx
[/code]



