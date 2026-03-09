# CX Knowledgebase : 2FA Configuration Guide - Email

This guide explains what prerequisites for enabling 2FA are and what configurations are required to be set up.  
  
Pre-Reqs for enabling 2FA via email

  1. Visit this guide to set up the email connector – [IMAP-SMTP based Email Configuration Guide](IMAP-SMTP-based-Email-Configuration-Guide_112001145.html#Pre-Requisites)

  2. There must be at least one email channel configured that will be used for sending the OTP.

![image-20260127-073513.png](attachments/1690927131/1690894358.png?width=963)
  3. Following`twoFAConfigs`must be part of the tenantSettings object - add these either at the time of tenant creation or add these later using [update tenant API](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/example/21457238-c45a857e-656c-4097-a27b-e34a437be2f9):

     1. `"Otp_Manager_Url": "http://ef-cx-otp-manager-svc:3000/",` // must be inside `keyCloak` object in tenant and required if is2FAEnabled is true

     2. 
[code]"twoFAConfigs": {              // must be inside tenantSettings object
              "is2FAEnabled": true,        // true | false
              "channelType": "EMAIL",      // channel type configured for OTP for the tenant - 'EMAIL' | 'SMS'
              "channelServiceIdentifier": "nasirkhan36616@gmail.com",    // identifier set while configuring the channel
              "otpExpiry": 60,             // OTP Expiry time in seconds
              "otpMaxAttempts": 5         // maximum attempts to validate OTP
            
            }
[/code]




example payload for update request:
[code] 
    {
        "tenantSettings": {
            "keyCloak": {
                "Otp_Manager_Url": "http://ef-cx-otp-manager-svc:3000/"
            },
            "twoFAConfigs": {
                "is2FAEnabled": true,
                "channelType": "EMAIL",
                "channelServiceIdentifier": "nasirkhan36616@gmail.com",
                "otpExpiry": 60,
                "otpMaxAttempts": 3
            }
        }
    }
[/code]

example payload for creating a new tenant with 2FA enabled:
[code] 
    {
        "tenantName": "expertflow",
        "tenantId": "expertflow",
        "tenantCode": "13135",
        "tenantSettings": {
            "keyCloak": {
                "credentials": {
                    "secret": "ef61df80-061c-4c29-b9ac-387e6bf67052"
                },
                "realm": "expertflow",
                "auth-server-url": "http://keycloak.ef-external.svc/auth/",
                "ef-server-url": "http://ef-cx-unified-admin-svc:3000/",
                "Otp_Manager_Url": "http://ef-cx-otp-manager-svc:3000/",
                "ssl-required": "external",
                "resource": "cim",
                "verify-token-audience": false,
                "use-resource-role-mappings": true,
                "confidential-port": 0,
                "CLIENT_ID": "cim",
                "CLIENT_DB_ID": "ef61df80-061c-4c29-b9ac-387e6bf67052",
                "GRANT_TYPE": "password",
                "GRANT_TYPE_PAT": "client_credentials",
                "USERNAME_ADMIN": "admin",
                "PASSWORD_ADMIN": "admin",
                "SCOPE_NAME": "Any default scope",
                "bearer-only": true,
                "FINESSE_URL": "",
                "TWILIO_SID": "AC99cffb57f6d7e3c3da5f0f149ddc2b47",
                "TWILIO_VERIFY_SID": "VA73622e86ae131799532a804ec9e230e3",
                "TWILIO_AUTH_TOKEN": "31bea9d152d6c1dd053cd4a8481fc234",
                "RSA_Server_URL": "",
                "RSA_Client_Key": "",
                "RSA_Client_ID": "",
                "MASTER_USERNAME": "admin",
                "MASTER_PASSWORD": "admin",
                "policy-enforcer": {}
            },
            "redis": {
                "userName": "expertflow",
                "password": "Expertflow123"
            },
            "mongo": {
                "userName": "expertflow",
                "password": "Expertflow123"
            },
            "fqdn": "efcx-dev2.expertflow.com",
            "campaigns": {
                "url": "http://cx-campaigns-campaign-studio-svc:1880",
                "username": "admin",
                "password": "admin"
            },
            "surveys": {
                "url": "http://cx-surveys-survey-studio-svc:1880",
                "username": "admin",
                "password": "admin"
            },
            "finesse": {
                "url": "https://finesseurl",
                "adminUser": "user",
                "adminPass": "pass"
            },
            "dialer": {
                "serviceIdentifier": "8224",
                "maxConcurrentCalls": "5",
                "maxCallTime": "60",
                "callsPerSecond": "15"
            },
            "secureLink": {
                "linkExpiryTime": 30
            },
            "mediaServer": {
                "wssUrl": "wss://192.168.2.24:7443",
                "domainManagerUrl": "http://192.168.2.24:8000/add-domain/"
            },
            "twoFAConfigs": {
                "is2FAEnabled": true,
                "channelType": "EMAIL",
                "channelServiceIdentifier": "nasirkhan36616@gmail.com",
                "otpExpiry": 60,
                "otpMaxAttempts": 3
            }
        },
        "status": "inActive",
        "createdBy": "admin",
        "updatedBy": "admin"
    }
[/code]
