---
title: "Queue Priority"
summary: "Explanation and how-to guide for configuring queue priority in ExpertFlow CX — covering the priority range, routing order (Queue Priority → Task Priority → FIFO), the IS_QUEUE_PRIORITY_ENABLED feature flag, known limitations, and best practices."
audience: [solution-admin]
product-area: [routing]
doc-type: how-to
difficulty: intermediate
keywords: ["queue priority CX", "IS_QUEUE_PRIORITY_ENABLED CX", "routing priority CX", "queue routing order CX", "task priority CX", "configure queue priority CX", "priority routing CX"]
aliases: ["CX queue priority", "queue priority configuration CX", "set queue priority CX"]
last-updated: 2026-03-10
---

# Queue Priority

Queue Priority allows ExpertFlow CX to route interactions from high-priority queues before interactions from lower-priority queues when an agent becomes available. This is useful when different customer segments or channels require different levels of urgency.

---

## How Queue Priority Works

When an agent becomes available, CX selects the next interaction using the following three-step order:

1. **Queue Priority** — Interactions from the highest-priority queue are served first.
2. **Task Priority** — Within the same queue, interactions with the higher task priority are served first.
3. **FIFO** — Within the same queue and same task priority, the oldest interaction is served first.

### Priority Range

Queue priority is a numeric value from **1 to 10**:

| Value | Priority Level |
|---|---|
| `1` | Lowest (default) |
| `10` | Highest |

---

## Enable Queue Priority

Queue Priority is controlled by a feature flag. It is **disabled by default**.

To enable it, set the following value in your Helm custom values file:

```yaml
global:
  IS_QUEUE_PRIORITY_ENABLED: "true"
```

Then apply the change:

```bash
helm upgrade --install ef-cx \
  --namespace=expertflow \
  --values=cx-custom-values.yaml \
  expertflow/cx
```

---

## Configure Priority on a Queue

Once the feature flag is enabled:

1. Navigate to **Unified Admin → Routing Engine → Queues**.
2. Select or create a queue.
3. Set the **Queue Priority** field to a value between `1` and `10`.
4. Save.

Repeat for all queues where you want to set a non-default priority.

---

## Example

| Queue | Priority | Description |
|---|---|---|
| VIP Customers | `10` | Highest — served first |
| Premium Support | `7` | High priority |
| General Inquiries | `3` | Below average |
| Survey Callbacks | `1` | Lowest — served last |

When an agent is free, CX picks the next task from **VIP Customers** before any other queue, regardless of when interactions arrived in the other queues.

---

## Known Limitations

### Reserved-State Limitation with a Single Agent

If only one agent is available and that agent enters a **Reserved** state for an interaction, CX cannot simultaneously serve interactions from other queues until the agent's current interaction concludes or is released. This means that in single-agent scenarios, effective queue prioritization requires multiple agents to be available at the same time.

---

## Best Practices

- Reserve priority `10` only for your most critical customer segment to avoid priority inflation.
- Use priority `1` (default) for low-urgency queues such as callbacks or survey follow-ups.
- Monitor queue wait times after enabling this feature — if lower-priority queues accumulate large backlogs, consider staffing adjustments.
- Do not assign the same priority to all queues — this nullifies the feature and routing falls back to FIFO across all queues.

---

## Related Articles

- [Routing Attributes and Queues](Routing-Attributes-and-Queues.md)
- [Precision Routing](Precision-Routing.md)
- [Priority Routing](Priority-Routing.md)
- [Pull-Mode Routing](Pull-Mode-Routing.md)
- [Media Routing Domains (MRD) Overview](Media-Routing-Domains-MRD-Overview.md)
