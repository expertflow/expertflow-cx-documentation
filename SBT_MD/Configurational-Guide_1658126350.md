# CX Knowledgebase : Configurational Guide

This document is a configuration guide for integrating Expertflow CX with Google Play Store app reviews. This guide is for developers and system administrators who will install, configure, and maintain this integration in your environment.  
  
By following this guide, you will configure Google Play Store as a channel in Expertflow CX and connect it to your Android application so that you can manage and reply to reviews from within CX.

### Prerequisites 

  1. Ensure you have successfully completed Helm-Based EFCX Deployment (add link of deployment guide)

  2. After your system administrator completed [Google Play Store onboarding](Onboarding-Guide_1511653389.html), and set up your service account and linked it to Google Play Console you should have the following details:

     1. Google Service Account access to Google Play Store Application and JSON file containing all authentication credentials

     2. Google Play Package Name (e.g., com.yourcompany.yourapp)

     3. Google Play App Name (your application's display name)

     4. Confirmation that the Service Account has "**Manage reviews and reply to reviews** " permission in Google Play Console

     5. Service Account JSON File Contents containing:

        1. `type` (usually "service_account")

        2. `project_id`

        3. `private_key_id`

        4. `private_key`

        5. `client_email`

        6. `client_id`

        7. `auth_uri`

        8. `token_uri`

        9. `auth_provider_x509_cert_url`

        10. `client_x509_cert_url`

        11. `universe_domain`




## Unified Admin Configuration

This section outlines the procedure for setting up the Google Play Store Channel.

  1. Open Unified Admin

  2. Click on Channel Manager dropdown to setup the further configurations:




### Setup Channel Type

  1. Google Play Store channel type should already be shown in the list here as out-of-the-box Channels as "**PLAY_STORE** ". If not please add one.

  2. Select the MRD as **CHAT**.

  3. Upload the icon (if not already uploaded).

  4. Save.


![image-20260121-142555.png](attachments/1658126350/1671168207.png?width=800)

### Setup Channel Provider

It's recommended to use the service name of the component in the **"Channel Provider - > Provider's Webhook"** field. However, FQDN can also be used with some additional custom configurations.

  1. Set a name i.e. **Google Play Store Provider**.

  2. Select Channel Type as `PLAY_STORE`.

  3. In **Provider Webhook** , enter the service name of the Google Play Store Connector as: `http://{SERVICE-NAME}:{SERVICE-PORT}`. Replace the `{SERVICE-NAME}` and {SERVICE-PORT} in the URL with the component's k3s-based service name and port (It can be fetched using `kubectl get svc -n expertflow`)

**Example:** Set the "Provider Webhook" field as `http://cx-channels-google-playstore-connector-svc:8080`

  4. Add the following 13 attributes as Custom Attributes, by cl Add Custom Attribute**** button, and replace the dummy value "New attribute1.." in the attribute field with

     1. **GOOGLE_SA_TYPE** and select data-type as String(50)

     2. **GOOGLE_SA_PROJECT_ID** and select data-type as “String 50”

     3. **GOOGLE_SA_PRIVATE_KEY_ID** and select data-type as “String 100”

     4. **GOOGLE_SA_PRIVATE_KEY** and select data-type as “String 2000”

     5. **GOOGLE_SA_CLIENT_EMAIL** and select data-type as “String 100”

     6. **GOOGLE_SA_CLIENT_ID** and select data-type as “String 50”

     7. **GOOGLE_SA_AUTH_URI** and select data-type as “String 100”

     8. **GOOGLE_SA_TOKEN_URI** and select data-type as “String 100”

     9. **GOOGLE_SA_AUTH_PROVIDER_CERT_URL** and select data-type as “String 100”

     10. **GOOGLE_SA_CLIENT_CERT_URL** and select data-type as “String 100”

     11. **GOOGLE_SA_UNIVERSE_DOMAIN** and select data-type as “String 50”

     12. **GOOGLE_PLAY_PACKAGE_NAME** and select data-type as “String 50”

     13. **GOOGLE_PLAY_APP_NAME** and select data-type as “String 50”

  5. Add the following permissions related attributes as Custom Attributes

     1. **LIKE_SUPPORT_SM** and select data-type as “Boolean”

     2. **HIDE_SUPPORT_SM** and select data-type as “Boolean”

     3. **DELETE_SUPPORT_SM** and select data-type as “Boolean”

     4. **ALLOW_VIEW_FULL_POST_SM** and select data-type as “Boolean”

     5. **PRIVATE_REPLY_SUPPORT_SM** and select data-type as “Boolean”

     6. **COMMENT_REPLY_SUPPORT_SM** and select data-type as “Boolean”

     7. **EDIT_MESSAGE_SUPPORT_SM** and select data-type as “Boolean”

  6. Save.


![image-20260121-142654.png](attachments/1658126350/1671266583.png?width=800)

### Setup Channel Connector

  1. Set any name i.e. **My App Play Store Connector**.

  2. Select Channel Provider as "**Google Play Store Provider** ".

  3. In **GOOGLE_SA_TYPE** field, insert `service_account`

  4. In **GOOGLE_SA_PROJECT_ID** field, insert the `project_id` from your Service Account JSON file

  5. In **GOOGLE_SA_PRIVATE_KEY_ID** field, insert the `private_key_id` from your Service Account JSON file

  6. In **GOOGLE_SA_PRIVATE_KEY** field, insert the complete `private_key` from your Service Account JSON file (including `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----`)

  7. In **GOOGLE_SA_CLIENT_EMAIL** field, insert the `client_email` from your Service Account JSON file

  8. In **GOOGLE_SA_CLIENT_ID** field, insert the `client_id` from your Service Account JSON file

  9. In **GOOGLE_SA_AUTH_URI** field, insert the `auth_uri` from your Service Account JSON file (usually `https://accounts.google.com/o/oauth2/auth`)

  10. In **GOOGLE_SA_TOKEN_URI** field, insert the `token_uri` from your Service Account JSON file (usually `https://oauth2.googleapis.com/token`)

  11. In **GOOGLE_SA_AUTH_PROVIDER_CERT_URL** field, insert the `auth_provider_x509_cert_url` from your Service Account JSON file

  12. In **GOOGLE_SA_CLIENT_CERT_URL** field, insert the `client_x509_cert_url` from your Service Account JSON file

  13. In **GOOGLE_SA_UNIVERSE_DOMAIN** field, insert the `universe_domain` from your Service Account JSON file (usually [googleapis.com](http://googleapis.com))

  14. In **GOOGLE_PLAY_PACKAGE_NAME** field, insert your Google Play app's package name (e.g., com.yourcompany.yourapp, and make sure it is exactly same as on google play store)

  15. In **GOOGLE_PLAY_APP_NAME** field, insert your Google Play app's display name




**Set the values of Permissions related custom attributes to**

  1. **LIKE_SUPPORT_SM** : `false`

  2. **HIDE_SUPPORT_SM** : `false`

  3. **DELETE_SUPPORT_SM** : `false`

  4. **ALLOW_VIEW_FULL_POST_SM** `true`

  5. **PRIVATE_REPLY_SUPPORT_SM** : `false`

  6. **COMMENT_REPLY_SUPPORT_SM** : `true`****

  7. **EDIT_MESSAGE_SUPPORT_SM** : `false`




Save

### Setup Channel

  1. Click on **Google Play Store** to expand the panel and click on "**Add new Channel** ".

  2. Set a name i.e. **My App Reviews Channel**.

  3. Set **Service Identifier** as your app's package name that you have used in **GOOGLE_SA_CLIENT_ID** while setting up Channel Connector.

  4. Select the Bot from the drop down list.

  5. Select the connector name you have created i.e. "**My App Play Store Connector** " from Channel Connector drop down list.

  6. Set any value in seconds as **Customer Activity Timeout(sec)**. (You can change it as per your need. Normally it would be 0sec (1 hour) for reviews)

  7. Set **Channel Mode** as **HYBRID**.

  8. Set **Routing Mode** as **PULL**. (As it works best in PULL mode)

  9. Set **Queue** or **List** (As required based on PUSH or PULL mode).

  10. Set **Agent Selection Policy** as **LONGEST AVAILABLE**.

  11. Set any value as **Agent Request TTL (sec)**. (You can change it as per your need. Normally it would be 300sec (5mins))

  12. Save.


![Channel.png](attachments/1658126350/1680048291.png?width=800)

The connector uses an automatic discovery mechanism. Once the channel is configured in Unified Admin, the connector will automatically detect it during the next polling cycle by querying CCM for channels with channel type "PLAY_STORE". No additional webhook setup is required as the connector proactively fetches its configuration from CCM.
