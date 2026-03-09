# CX Knowledgebase : Bot Connector Developer Guide

## Purpose

The purpose of this guide is to provide information to bot developers on how to develop a custom bot connector to interface between the custom bot and Expertflow CX. Bot connectors for Rasa and Dialogflow are built into the system. However, for connecting to other custom bots, a connector must be developed to connect and process communication (request/response transmission) with the custom bot.

## Intended Audience

The document is intended for developers with understanding of Bot Framework and synchronous/asynchronous APIs. The document will help in building understanding of developing connectors and adapters for communication between bot and channel(s). 

## Technical Overview

The following diagram outlines the placement of various connectors (Dialogflow, Rasa and Custom) within Bot Framework. Bot Framework controls all aspects of the [conversation](Conversation_93192236.html) with the custom bot. The Bot Framework is described [here](https://expertflow-docs.atlassian.net/wiki/spaces/CXDOC/pages/2529293/Platform+Architecture+Overview). 

The custom bot connector is a communication interface between the Bot Framework and the custom Bot. Following are the properties of the connector:

  * The connector should be able to send and receive messages using REST APIs from the custom bot. For this, the bot must expose a webhook and register it with Expertflow CX. The registration process is described [here](Register-Custom-Bot_2529899.html). 

  * The connector should also be able to translate the received message for the Bot framework.

  * A bot framework adapter may be developed to translate the user messages into a language ([messages, intents and actions](Custom-Connector-Bot-Communication_2527859.html)) understood by the custom bot.




### Assumptions and Constraints

It should be noted that internal architecture and development of the bot/adapter is left at the discretion of the developers and not included in this guide. However, the [messages, intents and actions](Custom-Connector-Bot-Communication_2527859.html) are documented for development of an adapter.

## Next Steps

1| **Register Custom Bot**|  The bot needs to expose a Webhook to communicate with the connector. The bot name and URL for the webhook will be specified in the Unified Admin Console as explained in [Register Custom Bot Connector](Register-Custom-Bot_2529899.html).   
---|---|---  
2| **Bot Training**|  This section [Custom Connector-Bot Communication](Custom-Connector-Bot-Communication_2527859.html) describes the messages, intents and actions format required for connector and adapter development.The format of the messages is described in detail in [Custom Connector-Bot Message Exchange](Custom-Connector-Bot-Communication_2527859.html) section.
