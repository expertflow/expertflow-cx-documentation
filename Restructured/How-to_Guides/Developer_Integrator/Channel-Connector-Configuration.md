---
title: "Channel Connector Configuration API"
summary: "Reference guide for the Channel Connector Configuration APIs in ExpertFlow CX — covering the Push-based API (POST /connector-configurations) that CCM uses to notify connectors of configuration changes, and the Pull-based API (GET /ccm/channel-connectors/configurations) that connectors use to fetch their own configuration."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: reference
difficulty: advanced
keywords: ["channel connector configuration API CX", "connector-configurations API CX", "CCM channel config CX", "channel connector API CX", "serviceIdentifier config CX"]
aliases: ["connector configuration API CX", "channel config API CX", "CCM connector config CX"]
last-updated: 2026-03-10
---

# Channel Connector Configuration API

Channel connector configurations are the **custom attributes** defined in Unified Admin under **Channel Provider** (e.g., API Key, Host URL). Two APIs allow connectors to stay in sync with these configurations: a push-based API that CCM calls when configurations change, and a pull-based API that connectors can call to fetch their own configuration on demand.

---

## Push-Based API — Receive Configuration Updates

CCM calls this endpoint on the **third-party connector** whenever a channel provider's configuration is created or updated in Unified Admin.

**Method**: `POST`
**Endpoint**: `{connector-host}/connector-configurations`

The endpoint path is fixed as `connector-configurations`. The connector host (FQDN) is specified when the connector is registered.

### Request Body

| Property | Type | Required | Description |
|---|---|---|---|
| `serviceIdentifier` | String | Yes | ID of the channel |
| `connectorConfigurations` | List\<Attribute\> | Yes | List of configuration attributes to update |

Each attribute in `connectorConfigurations` contains:

| Field | Type | Description |
|---|---|---|
| `key` | String | Attribute name (e.g., `HOST-URL`, `API-KEY`) |
| `type` | ValueType | Data type (e.g., `String100`) |
| `value` | Object | Attribute value |

### Example Request

```json
{
  "serviceIdentifier": "123124",
  "connectorConfigurations": [
    {
      "key": "HOST-URL",
      "type": "String100",
      "value": "https://waba-sandbox.360dialog.io"
    },
    {
      "key": "API-KEY",
      "type": "String100",
      "value": "X4IpWk_sandbox"
    }
  ]
}
```

---

## Pull-Based API — Fetch Configuration

Third-party connectors call this endpoint on CCM to retrieve their channel connector configuration at any time.

**Method**: `GET`
**Endpoint**: `{{FQDN}}/ccm/channel-connectors/configurations/:serviceIdentifier`

Replace `:serviceIdentifier` with the connector's service identifier.

### Response Properties

| Property | Type |
|---|---|
| `key` | String |
| `type` | ValueType |
| `value` | Object |

---

## Related Articles

- [Register Channel Connector](Register-Channel-Connector.md)
- [Channel Connector Developer Guide](Channel-Connector-Developer-Guide.md)
- [Add Bot Connector](Add-Bot-Connector.md)
