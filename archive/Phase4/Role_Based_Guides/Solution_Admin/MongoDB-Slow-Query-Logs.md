---
title: "MongoDB Slow Query Logs"
summary: "How-to guide for enabling, querying, and disabling the MongoDB profiler to identify slow queries in an ExpertFlow CX deployment — covering profiling levels, threshold configuration, sample rate, and system.profile collection queries."
audience: [solution-admin, partner]
product-area: [platform]
doc-type: how-to
difficulty: intermediate
keywords: ["MongoDB slow query logs CX", "MongoDB profiler CX", "system.profile MongoDB CX", "setProfilingLevel CX", "MongoDB performance CX"]
aliases: ["MongoDB profiling CX", "slow queries MongoDB CX", "MongoDB query logs CX"]
last-updated: 2026-03-10
---

# MongoDB Slow Query Logs

This guide enables slow query logging in MongoDB to identify queries causing high latency or heavy load on the MongoDB server in an ExpertFlow CX deployment.

> **Warning**: Profiling impacts database performance and uses disk space. Evaluate performance and storage implications before enabling in production. Profiling level 2 (all operations) and low `slowms` thresholds have the highest overhead.

---

## Prerequisites

Access to the MongoDB primary pod. Get connection instructions from Helm:

```bash
helm -n ef-external status mongo
```

Follow the printed instructions to either exec into the primary pod directly or use a mongo-client pod.

---

## Enabling Slow Query Logs

MongoDB slow query logging is controlled by the **Profiler**. Use `db.setProfilingLevel()` to configure it.

### Profiling Levels

| Level | Behavior |
|---|---|
| `0` | Profiling off (default) |
| `1` | Log only operations slower than `slowms` threshold |
| `2` | Log all operations |

### Enable profiling with a threshold

Log all queries taking longer than 200 milliseconds:

```javascript
db.setProfilingLevel(1, { slowms: 200 })
```

### Enable with a sample rate

Log only 50% of queries exceeding the threshold (useful for reducing overhead on high-traffic systems):

```javascript
db.setProfilingLevel(1, { slowms: 200, sampleRate: 0.50 })
```

---

## Querying the Slow Query Log

When profiling is active, MongoDB writes log entries to the `system.profile` collection in each database. Switch to the target database first:

```javascript
use ccm_db;
```

### View the 10 most recent entries

```javascript
db.system.profile.find().limit(10).sort({ ts: -1 }).pretty()
```

### View all non-command operations

```javascript
db.system.profile.find({ op: { $ne: 'command' } }).pretty()
```

### Filter by collection

```javascript
db.system.profile.find({ ns: 'ccm_db.ChannelConnector' }).pretty()
```

### Filter by execution time

Operations taking longer than 5 milliseconds:

```javascript
db.system.profile.find({ millis: { $gt: 5 } }).pretty()
```

### Filter by time range

```javascript
db.system.profile.find({
  ts: {
    $gt: new ISODate("2024-05-10T03:00:00Z"),
    $lt: new ISODate("2024-05-11T03:40:00Z")
  }
}).pretty()
```

### Time range with sorted results (suppressing user field)

```javascript
db.system.profile.find(
  {
    ts: {
      $gt: new ISODate("2024-06-12T03:00:00Z"),
      $lt: new ISODate("2024-06-12T03:40:00Z")
    }
  },
  { user: 0 }
).sort({ millis: -1 })
```

### Show the 5 most recent slow operations (mongosh shorthand)

```javascript
show profile
```

This shows the 5 most recent operations that took at least 1 millisecond.

---

## Disabling Profiling

When investigation is complete, disable profiling to eliminate the performance and storage overhead:

```javascript
db.setProfilingLevel(0)
```

---

## Related Articles

- [Redis Log Monitoring via Slowlogs](Redis-Slowlogs.md)
- [Accessing Kubernetes Logs](Accessing-Kubernetes-Logs.md)
