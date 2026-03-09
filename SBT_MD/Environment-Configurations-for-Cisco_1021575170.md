# CX Knowledgebase : Environment Configurations for Cisco

To integrate CX with Cisco UCCX/UCCE, you need to update in the values.yaml of the Agent desk helm chart file as mentioned below. 

  1. Update the following CTI config variables added in the unified-agent configurations
[code] # To enable Cisco contact center integration, isCiscoEnabled should be true.
         isCiscoEnabled":"true"
         
         # Specify Cisco Finesse domain name
         domain: "<finesse domain>"
         
         # Specify Cisco secondary Finesse domain name. Leave blank if there is no secondary.
         subDomain" : "<secondary finesse domain>"
         
         # Specify Cisco Finesse BOSH URL
         boshUrl: "<finesse bosh api URL>"
         
         # Specify Cisco secondary Finesse BOSH URL. Leave blank if there is no secondary.
         "subBoshUrl" : "<secondary finesse bosh api URL>"
         
         # If Cisco finesse is SSO enabled. Specify SSO backend URL
         "ssoBackendUrl": "<SSO backend URL>"
         
         # Specify the Cisco UCC flavor. This could be any of the following values: 
         # UCCE - for all UCCE and PCCE deployments
         # UCCX - for all UCCX deployments 
         finesseFlavor: "[UCCE|UCCX]"
         
         # Specify RONA timeout as defined in Cisco configurations
         ronaStateOnCisco:"<call timeout reason configured on finesse>",
         
         # To enable Cisco contact center integration if finesse is running in HA, IS_FINESSE_HA_ENABLED should be true.
         IS_FINESSE_HA_ENABLED:true/false
         
         # Specify Cisco Finesse FQDN or Cisco Finesse IP address
         finesseURLForAgent: https://[Cisco-Finesse-FQDN/IP]
         
         # Specify secondary Cisco Finesse FQDN or Cisco Finesse IP address in case if finesse is running in HA
         SECONDARY_FINESSE_URL:https://[Secodary-Finesse-FQDN/IP]
         
         # Specify the static identifier to be used as channel identifier
         CISCO_SERVICE_IDENTIFIER: "<static identifier(number) to be used as a channel identifier on CX for CISCO_CC type channel>"
[/code]

  2. Share the cf-admin credentials with the Expertflow support team. With the encryption utility, they will encrypt the credentials and update the following configurations. 
[code] "ctiParam": "<Encrypted cf admin username>"
         "ctiParam2": "<Encrypted cf admin password>"
[/code]

  3. After updating the configurations, run the following command.
[code] helm upgrade --install --namespace expertflow   --set global.efCxReleaseName="ef-cx"  cx-agent-desk  --debug --values helm-values/cx-agent-desk-custom-values.yaml expertflow/agent-desk  
[/code]




If the agent-manager is unable to make a connection with Finesse, you need to add the following in the values.yaml of the Core helm chart under _**agent-manager**_
[code] 
    hostAliases:
      - ip: "192.168.1.33"
        hostnames:
          - "uccx12-5p.ucce.ipcc"
[/code]
