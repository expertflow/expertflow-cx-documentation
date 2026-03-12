# CX Knowledgebase : onChannelTypes

**Event Name**|  onChannelTypes  
---|---  
**Event Description**|  Event is triggered once connection is established through a channel  
**Emitter**|  Agent Manager  
  
**Name**| **Description**  
---|---  
id| type: Stringsystem generated channel ID   
name| type: Stringname of the channel e.g. FACEBOOK  
channelLogo| type: Image Objectlogo of the channel  
isInteractive| type: Booleanfor chat based channels  
mediaRoutingDomain| type: MRD Object
[code] 
       {
            "id": "622222cb5bd05f57c1c1841d",
            "name": "FACEBOOK",
            "channelLogo": "_FACEBOOK.svg",
            "isInteractive": false,
            "mediaRoutingDomain": null
        },
        {
            "id": "622222cc5bd05f57c1c1841e",
            "name": "VIBER",
            "channelLogo": "_VIBER.svg",
            "isInteractive": false,
            "mediaRoutingDomain": null
        },
        {
            "id": "622222cc5bd05f57c1c1841f",
            "name": "WHATSAPP",
            "channelLogo": "_WHATSAPP.svg",
            "isInteractive": true,
            "mediaRoutingDomain": "62302def6b1fba2525db2713"
        },
        {
            "id": "622222cc5bd05f57c1c18420",
            "name": "SMS",
            "channelLogo": "_SMS.svg",
            "isInteractive": false,
            "mediaRoutingDomain": null
        },
        {
            "id": "622222cc5bd05f57c1c18421",
            "name": "WEB",
            "channelLogo": "_WEB.svg",
            "isInteractive": true,
            "mediaRoutingDomain": "6223b491ef484b28639e9ca4"
        },
        {
            "id": "622222cc5bd05f57c1c18422",
            "name": "GENERIC",
            "channelLogo": "_GENERIC.svg",
            "isInteractive": false,
            "mediaRoutingDomain": null
        },
        {
            "id": "6233de0e3ef6175890847d4c",
            "name": "web",
            "channelLogo": "32917_web-1873373_1280.png",
            "isInteractive": true,
            "mediaRoutingDomain": "6233dde8c004592808ad3c0d"
        }
[/code]
