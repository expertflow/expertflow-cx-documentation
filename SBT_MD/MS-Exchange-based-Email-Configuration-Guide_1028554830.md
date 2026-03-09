# CX Knowledgebase : MS Exchange based Email Configuration Guide

  * Overview
  * Pre-Requisites
  * Required Items from MS Exchange Server
  * Unified Admin Configuration
    * Setup MRD
    * Setup Channel Type
    * Setup Channel Provider
    * Setup Channel Connector
    * Setup Channel
  * Setup Webhook
  * Conclusion



## Overview

Email provides support to various features. Sending and receiving emails are the basic features that comes along with some additional features like Reply, Reply all, Forward, Email Attachments, Email threading and Email Signature features to make the experience richer.

## Pre-Requisites

Email is implemented using **On-Prem MS Exchange** _(Primarily 2019)_ for sending and receiving emails using **EWS** (Exchange Web Service). Pull mode mechanism is used to pull the emails every certain number of time via EWS. An **On-Prem MS Exchange** account is required to integrate it with CX Hybrid Chat application. Also, we need to ensure that the account is publicly accessible or otherwise, you can only test it within that exchange. Along with that EWS should be enabled on this On-Prem MS Exchange server to make it accessible from Third Party Applications like CX Hybrid Chat application.

## Required Items from MS Exchange Server

Once your IT-Admin has setup your account on **On-Prem MS Exchange** then you should also ask them the following details.

  * Exchange URI e.g. _< exchange-fqdn>/EWS/Exchange.asmx_

  * Username or email address of the account to be connected with CX Hybrid Chat application

  * Password associated with the account to be connected with CX Hybrid Chat application




## Unified Admin Configuration

In our CX Hybrid Chat application, we need to setup email same like we setup any other connector. The detailed setups are mentioned below.

### Setup MRD

  1. Create MRD from Unified Admin → Routing Engine → MRD menu.

  2. Set the name and description.

  3. Select MRD Type: **EMAIL**.

  4. Set Max Task Request**** = 5 _(Or any other as needed)_

  5. Save.




**Note:** Go to Unified Admin → Channel Manager menu to setup the further configurations.

### Setup Channel Type

  1. Email channel type should be already shown in the list here as out-of-the-box Channels. If not please add one.

  2. Select the MRD as **EMAIL**.

  3. Upload the icon (if not already uploaded).

  4. Save.




### Setup Channel Provider

It's recommended to use the service name of the component in the **"Channel Provider - > Provider's Webhook"** field. However, FQDN can also be used with some additional custom configurations.

  1. Set any name i.e. MS Exchange Email Provider.

  2. Select Channel Type as “EMAIL”.

  3. Provide the service name of the Email Connector in the **Provider Webhook** field as http://{SERVICE-NAME}:{SERVICE-PORT}. Replace the {**SERVICE-NAME}** and**{SERVICE-PORT}** in the URL with the component's k3s-based service name and port _(It can be fetched using**k get svc -n expertflow**)_

     1. Example: Set the “Provider Webhook” field as [_http://cx-channels-ms-email-connector-svc:8080_](http://cx-channels-ms-email-connector-svc:8080)

  4. Add 3 Attributes as Custom Attributes

     1. **USERNAME** type **String(100)**

     2. **PASSWORD** type **Password**

     3. **EXCHANGE-URI** type **String(2000)**

     4. **PUBLIC-EMAIL-ID** type **String(2000)**

     5. **DOMAIN-PART** type **String(100)**

  5. Save




### Setup Channel Connector

  1. Set any name i.e. MS Exchange Email Connector.

  2. Select Channel Provider as “MS Exchange Email Provider”.

  3. In **USERNAME** field, insert the username/email-address received from IT Team

  4. In **PASSWORD** field, insert the password of username/email-address received from IT Team

  5. In **EXCHANGE-URI** field, insert the exchange-uri received from IT Team

  6. In **PUBLIC-EMAIL-ID** field, insert the email-address which is publicly available _(not the internal ms-exchange based)_

  7. In **DOMAIN-PART** field, insert the domain part of your ms exchange email address. _(E.g: for email_[ _ef.demo@mailhost.expertflow.com_](mailto:ef.demo@mailhost.expertflow.com) __`mailhost.expertflow.com` _is domain part) It will be used for sending email message from connector to ms exchange._

  8. Save.




### Setup Channel

  1. Click on Email to expand the panel and click on “Add new Channel”.

  2. Set any name i.e. MS Exchange Email Channel.

  3. Set Service Identifier as your email address that you have used in **USERNAME** while setting up Channel Connector.

  4. Select the Bot from the drop down list.

  5. Select the connector name you have created i.e. “MS Exchange Email Connector“ from Channel Connector drop down list.

  6. Set any value in seconds as Customer Activity Timeout(sec). _(You can change it as per your need. Normally it would be 300sec (5mins))_

  7. Set Channel Mode as HYBRID.

  8. Set Routing Mode as PULL. (As it works best in PULL mode)

  9. Set Queue or List (As required based on PUSH or PULL mode).

  10. Set Agent Selection Policy as LONGEST AVAILABLE.

  11. Set any value as Agent Request TTL (sec). (You can change it as per your need. Normally it would be 300sec (5mins))

  12. Save.




## Setup Webhook

Once the MS Exchange based Email account is setup and Configurations on unified admin is already finished with working ms-email-connector on some instance, then we need to setup the webhook using this [postman](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-cbf6dc25-d34a-4cd4-9442-1685c68f554d?action=share&source=copy-link&creator=34919800) request.

Snapshot is shown below:

![image-20250416-105251.png](attachments/1028554830/1028260036.png?width=903)

**Post Url**  
[https://<FQDN>/ms-email-connector/channel-type-configurations](https://cim-dev3.expertflow.com/ms-email-connector/channel-type-configurations)

**Post Body**

{ “channelTypeId”: “id-of-channel-type” }

**Post Response**

![image-20240318-111042.png](attachments/1028554830/1028751453.png?width=1390)

**Note:** You can fetch the ChannelTypeId from [this](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-5f5e97cc-3250-461c-9a55-2b5302d51a55?action=share&source=copy-link&creator=34919800) channels list API, and search for the EMAIL channel Type from the list and then use that ChannelTypeId.

## Conclusion

This will setup MS Exchange based EMAIL as a channel in CX Hybrid Chat Solution.
