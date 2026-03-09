# CX Knowledgebase : Updating AgentDesk Environment Variables for CX Voice

### Disclaimer

  * Assuming that the deployed Media Server instance has self-signed certificates. In that case, the certificates should be added manually in the browser using https://<Media-Server-IP>:<PORT, before trying to log in and connect to the Media Server.




To update the CX env variables for CX Voice Configuration,

  * On the CX deployment machine, navigate to the following path, 
[code] vi <cx-install-dir>/kubernetes/helm-values/cx-agent-desk-custom-values.yaml
[/code]

  * Update the following config to _**true**_ in case the Media Server environment is to be enabled in the unified-agent environment variables. If the _MRD_ associated with the _CX_VOICE_ channel type is changed, it must be updated in the configs as well.
[code] "isCxVoiceEnabled":"<boolean>", // to be set to `true`, if system is being used with the Media Server 
[/code]

  * Update the following **Sip.js** config variables added in the unified-agent config map,
[code] "SIP_SOCKET_URL": "<wss://Media-Server-IP-addr:7443>",
        "SIP_URI": "<Media Server Domain/IP>",
        "EXT_STATIC": "<Encrypted Static Password Set For Media Server Extensions>",
        "ENABLE_SIP_LOGS": "<SIP_LOGS>" // to be set to true if sip.js logs are required
[/code]




### Disclaimer

  * From the CX-4.3 release, the encrypted Extension Password will be required. The credentials need to be shared with the CX team and they will provide the encrypted values to be added to the deployment.




  * For **CX4.3** and onwards, the following configs are added to the unified-agent config map,
[code] "STATIC_QUEUE_TRANSFER_DN": "<Static DN to transfer Queue Calls>", // pre-configured DN on EF-Switch
        "AUTO_CALL_ANSWER_TIMER": "<Timer to Auto Accept the Outbound Call>" // in seconds
[/code]




  * The minimum value for _AUTO_CALL_ANSWER_TIMER_ should be 2 seconds.__




  * If the _MRD_ associated with the _CX_VOICE_ channel type is changed, it must be updated in the following env variable.
[code] "CX_VOICE_MRD":"<MRD associated with CX_VOICE channel type>"
[/code]

  * For **CX4.5.2** and onwards, the following configs are added to the unified-agent config map.
[code] "SIP_MONITORING_DN": "<Static DN for SM>", // Pre-configured DN for initiating SM request
[/code]

  * For **CX4.6** and onwards, the following configs are added to the unified-agent config map.
[code] "Enable_Voice_Events_For_CRM": "<boolean>", // to expose Voice events via Sip.js for third party applications
[/code]

  * For **CX4.8** and onwards the following configs are added in the unified agent environment variables.
[code] "SIP_EXTERNAL_DN":"<Static DN for External>", // Pre-configured DN for external number dialing
[/code]

  * Save the file and run the following sequence of commands in the _**< cx-install-dir>/kubernetes**_ directory:



[code] 
    helm upgrade --install --namespace expertflow   --set global.efCxReleaseName="ef-cx"  cx-agent-desk  --debug --values helm-values/cx-agent-desk-custom-values.yaml expertflow/agent-desk
[/code]

  * Log out of your voice agents and reload **Agent Desk**.



