# CX Knowledgebase : IMAP-SMTP based Email Configuration Guide

  * Overview
  * Pre-Requisites
  * Get Started - Setup Email
  * Unified Admin Configuration
    * Setup MRD
    * Setup Channel Type
    * Setup Channel Provider
    * Setup Channel Connector
    * Setup Channel
  * Setup Webhook
  * Conclusion



## Overview

Email provides support to various features. Sending and receiving emails are the basic features that comes along with some more features like Reply, Reply all, Forward, Email Attachments, Email threading and Email Signature features to make the experience richer.

## Pre-Requisites

Email is implemented using **SMTP** (for sending emails) and **IMAP** (for receiving emails) protocols. Pull mode mechanism is used to pull the emails every certain number of minutes from the queue. The current supported mailbox is **Gmail** , so in this documentation, a gmail account is needed to generate an app password, also IMAP and SMTP settings should be supported _(by defaults its supported and enabled in gmail)_.

## Get Started - Setup Email

In order to setup Email, we first need to generate a password from google account. Once done, we will be able to proceed with setting up the email connector on Unified Admin.

Here is how to generate the password:  


  * From your browser, Go to your Google account, then go to Security tab:


![email connector setup 1.png](attachments/112001145/160858215.png?width=894)

  * From there, scroll down to 2-Step Verification  


![image-20240312-141333.png](attachments/112001145/160202800.png?width=870)

  


  * Scroll down till **App passwords** :

![image-20240312-141432.png](attachments/112001145/160137279.png?width=823)
  * Enter your app name and hit create. Now it is created, you need to keep it saved so you can use it later in Unified admin.

  * By default IMAP and SMPT settings are enabled and supported in gmail account.




![image-20240705-105849.png](attachments/112001145/370278555.png?width=722)

## Unified Admin Configuration

In our CX Hybrid Chat application, we need to setup email same like we setup any other connector. The detailed setups are mentioned below.

### Setup MRD

  1. Create MRD from Unified Admin → Routing Engine → MRD menu.

  2. Set the name and description.

  3. Select MRD Type: **EMAIL**.

  4. Set Max Task Request**** = 5

  5. Save.




**Note:** Go to Unified Admin → Channel Manager menu to setup the further configurations.

### Setup Channel Type

  1. Email channel type should be already shown in the list here as out-of-the-box Channels. If not please add one.

  2. Select the MRD as **EMAIL**.

  3. Upload the icon (if not already uploaded).

  4. Save.




### Setup Channel Provider

It's recommended to use the service name of the component in the **"Channel Provider - > Provider's Webhook"** field. However, FQDN can also be used with some additional custom configurations.

  1. Set any name i.e. Email Provider.

  2. Select Channel Type as “EMAIL”.

  3. Provide the service name of the Email Connector in the **Provider Webhook** field as http://{SERVICE-NAME}:{SERVICE-PORT}. Replace the {**SERVICE-NAME} and**{**SERVICE-PORT}** in the URL with the component's k3s-based service name and port _(It can be fetched using k get svc -n expertflow)_

     1. Example: Set the “Provider Webhook” field as http://cx-channels-email-connector-svc:8080

  4. Add 11 Attributes as Custom Attributes

     1. IMAP-HOST type String(100)

     2. IMAP-USERNAME type String(100)

     3. IMAP-PORT type PositiveNumber

     4. IMAP-PASSWORD type String(100)

     5. IMAP-SSL-ENABLED type Boolean

     6. SMTP-HOST type String(100)

     7. SMTP-USERNAME type String(100)

     8. SMTP-PASSWORD type String(100)

     9. SMTP-PORT type PositiveNumber

     10. SMTP-AUTH type Boolean

     11. SMTP-TTLS-ENABLE type Boolean

  5. Save




### Setup Channel Connector

  1. Set any name i.e. Email Connector.

  2. Select Channel Provider as “Email Provider”.

  3. In IMAP-HOST field, paste the Gmail IMAP host : [imap.gmail.com](http://imap.gmail.com).

  4. In IMAP-USERNAME field, insert the email you want to use for your channel, for example, your business email.

  5. In IMAP-PORT field, insert Gmail IMAP port: 993.

  6. In IMAP-PASSWORD field, paste the previously generated **App Password**. _(**Note:** Your normal Gmail password will not work here)_

  7. Enable IMAP-SSL-ENABLED.

  8. In SMTP-HOST field, paste the Gmail SMTP host : [smtp.gmail.com](http://smtp.gmail.com).

  9. In SMTP-USERNAME field, insert the email you want to use for your channel, for example, your business email. Note that it has to match the IMAP-USERNAME.

  10. In SMTP-PASSWORD field, paste the previously generated password.

  11. In SMTP-PORT field, use the Gmail SMTP port: 587.

  12. Enable SMTP-AUTH.

  13. Enable SMTP-TTLS-ENABLE**.**

  14. Save.




### Setup Channel

  1. Click on Email to expand the panel and click on “Add new Channel”.

  2. Set any name i.e. Email Channel.

  3. Set Service Identifier as your email that you have used in SMTP-USERNAME and IMAP-USERNAME.

  4. Select the Bot from the drop down list.

  5. Select the connector name you have created i.e. “Email Connector“ from Channel Connector drop down list.

  6. Set any value in seconds as Customer Activity Timeout(sec). (You can change it as per your need. Normally it would be 300sec (5mins))

  7. Set Channel Mode as HYBRID.

  8. Set Routing Mode as PULL. (As it works best in PULL mode)

  9. Set Queue or List (As required based on PUSH or PULL mode).

  10. Set Agent Selection Policy as LONGEST AVAILABLE.

  11. Set any value as Agent Request TTL (sec). (You can change it as per your need. Normally it would be 300sec (5mins))

  12. Save.




## Setup Webhook

Once the Email account is setup and Configurations on unified admin is already finished with working email-connector on some instance, then we need to setup the webhook using this [postman](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-fe50a334-b9cf-451b-9196-266de3a4566b?action=share&source=copy-link&creator=4288348) request.

Snapshot is shown below:

![image-20240312-145523.png](attachments/112001145/160727102.png?width=807)

**Post Url**  
[https://<FQDN>/email-connector/channel-type-configurations](https://cim-dev3.expertflow.com/email-connector/channel-type-configurations)

**Post Body**

{

“channelTypeId”: “id-of-channel-type”

}

**Post Response**

![image-20240318-111042.png](attachments/112001145/170623375.png?width=1390)

**Note:** You can fetch the ChannelTypeId from [this](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-5f5e97cc-3250-461c-9a55-2b5302d51a55?action=share&source=copy-link&creator=4288348) channels list API, and search for the EMAIL channel Type from the list and then use that ChannelTypeId.

## Conclusion

This will setup EMAIL as a channel in CX Hybrid Chat Solution.
