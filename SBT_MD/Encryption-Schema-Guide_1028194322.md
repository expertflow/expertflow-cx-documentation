# CX Knowledgebase : Encryption Schema Guide

**Location:** `CX-4.10/kubernetes/pre-deployment/conversation-manager/encryption/encryption-schema.json`   
This document outlines the rules for encrypting and decrypting fields in MongoDB collections used by the **Conversation Manager** service. Other services can define their own encryption schema by using this guide as a reference.

## Example Schema
[code] 
    {
      "CustomerTopicEvents": {
        "encrypt": [
          "cimEvent.data.body.markdownText",
          "cimEvent.data.body.jsonNode"
        ],
        "notSkipIf": {
          "cimEvent.name": ["BOT_MESSAGE", "CUSTOMER_MESSAGE", "AGENT_MESSAGE"]
        }
      },
      "ConversationActivities": {
        "encrypt": [
          "activity.data.body.markdownText",
          "cimEvent.data.body.jsonNode"
        ],
        "notSkipIf": {
          "activity.name": ["BOT_MESSAGE", "CUSTOMER_MESSAGE", "AGENT_MESSAGE"]
        }
      }
    }
[/code]

## Schema Fields

### Collection Keys

Each top-level key (e.g., `CustomerTopicEvents`, `ConversationActivities`) represents a **MongoDB collection name**.   
The associated value defines rules for **encrypting and decrypting** fields in the documents of that collection.

### `encrypt`

A list of **field paths** (in dot notation) to be encrypted when stored and decrypted when retrieved.

  * Example: `cimEvent.data.body.markdownText`

  * If the field points to an object, list, or map, all nested fields will be encrypted/decrypted recursively.

  * Used for both **encryption** (pre-storage) and **decryption** (post-retrieval).




### `notSkipIf` (Optional)

A conditional map that allows encryption/decryption **only when any of the conditions match**.

**Format:**
[code] 
    "notSkipIf": {
      "<fieldPath>": ["value1", "value2"]
    }
[/code]

If omitted, encryption/decryption is applied unless restricted by `skipIf`.

### `skipIf` (Optional)

A conditional map that **prevents encryption/decryption** if any of the listed values match.

**Format:**
[code] 
    "skipIf": {
      "<fieldPath>": ["value1", "value2"]
    }
[/code]

Takes precedence over `notSkipIf`. If both match, the document is skipped.

## How to Modify the Schema

Action| What to Do  
---|---  
Add new collection | Add a new top-level key matching the MongoDB collection name   
Add encrypted field | Update the `encrypt` array with the new field path   
Add conditions | Use `notSkipIf` to target specific documents, `skipIf` to exclude   
Encrypt nested fields | Use dot notation for deep nesting (e.g., `event.data.body.text`)   
  
## Sample Use Case

Encrypt only customer-facing messages, skip bot messages ones:
[code] 
    {
      "CustomerTopicEvents": {
        "encrypt": ["cimEvent.data.body.markdownText"],
        "notSkipIf": {
          "cimEvent.name": ["CUSTOMER_MESSAGE"]
        },
        "skipIf": {
          "cimEvent.name": ["BOT_MESSAGE"]
        }
      }
    }
[/code]
