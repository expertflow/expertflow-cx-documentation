---
title: "topicSubscription"
summary: "Emitted by Agent Desk to Agent Manager when an agent requests to subscribe to a conversation topic."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["topicSubscription socket event CX", "topicSubscription Agent Manager CX", "Socket.IO CX"]
aliases: ["topicSubscription event ExpertFlow", "topicSubscription socket CX"]
last-updated: 2026-03-12
---

# topicSubscription

Agent requests the Agent Manager to subscribe to a conversation topic by emitting this event.

| Property | Value |
|---|---|
| **Event Name** | `topicSubscription` |
| **Emitter** | Agent Desk |
| **Direction** | Agent Desk → Agent Manager |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `topicParticipant` | Object | The topic participant object, including participant `id`. |
| `conversationId` | String | ID of the conversation for which subscription is requested. |
| `agentId` | String | ID of the agent for whom the event has been emitted. |
| `taskId` | String | ID of the task subscribed by the agent. |
| `roomInfo` | Object | Contains `id` (room ID) and `mode` (room mode). |

## Example Payload

```json
{
  "topicParticipant": {
    "id": "688ef131-9cd6-4108-893e-033943eb2be0",
    "type": "AGENT",
    "participant": {
      "id": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
      "participantType": "CCUser",
      "keycloakUser": {
        "id": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
        "username": "faizan",
        "permittedResources": {
          "Resources": [
            {
              "scopes": [
                "view",
                "manage"
              ],
              "rsid": "44e205bc-86f0-4e6a-b03a-844c1317722d",
              "rsname": "leave-chat"
            },
            {
              "scopes": [
                "dummy"
              ],
              "rsid": "6e8c5866-3f42-4131-b72a-f9da6ba1bfa5",
              "rsname": "dummy"
            },
            {
              "scopes": [
                "view",
                "manage"
              ],
              "rsid": "24978903-b9c3-4823-b3bb-e5731ee37a65",
              "rsname": "state-change"
            },
            {
              "scopes": [
                "view",
                "manage"
              ],
              "rsid": "dbcb5f8c-03d5-4171-989f-b4f3365882e9",
              "rsname": "subscribed-list"
            },
            {
              "scopes": [
                "view",
                "manage"
              ],
              "rsid": "e59b98ee-9fff-4583-9a09-8f85ed78459d",
              "rsname": "customer-list"
            },
            {
              "scopes": [
                "view",
                "manage"
              ],
              "rsid": "33020afa-6fee-4c3b-830d-96c241a997ca",
              "rsname": "customer-conversation-view"
            }
          ]
        },
        "roles": [
          "agent",
          "offline_access",
          "default-roles-university",
          "uma_authorization"
        ],
        "realm": "university"
      },
      "associatedRoutingAttributes": []
    },
    "token": null,
    "topicId": "261c271a-58e6-4571-9d25-77ad26d745d6",
    "role": "PRIMARY",
    "userCredentials": null,
    "state": "SUBSCRIBED"
  },
  "conversationId": "261c271a-58e6-4571-9d25-77ad26d745d6",
  "agentId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
  "taskId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
  "roomInfo": {
    "id": "65a625609487373651365bfb",
    "mode": "CONTACT_CENTER"
  }
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [topicUnsubscription](./topicUnsubscription_2531762.md)
- [topicClosed](./topicClosed_2531758.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
