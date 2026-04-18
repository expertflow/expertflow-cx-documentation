---
title: "Redis Log Monitoring via Slowlogs"
summary: "How-to guide for enabling and reading Redis slowlogs in an ExpertFlow CX deployment — covering threshold configuration, buffer size limits, slowlog retrieval, the monitor command, and disabling slowlogs when done."
audience: [administrator, platform-operator]
product-area: [platform]
doc-type: how-to
difficulty: intermediate
keywords: ["Redis slowlogs CX", "Redis slow query CX", "SLOWLOG GET CX", "Redis performance monitoring CX", "Redis CONFIG SET slowlog CX"]
aliases: ["Redis slow query log CX", "Redis monitoring CX", "slowlog Redis CX"]
last-updated: 2026-03-10
---

# Redis Log Monitoring via Slowlogs

This guide configures and queries Redis slowlogs to identify commands taking longer than expected in an ExpertFlow CX deployment. Redis slowlogs record commands that exceed a configurable execution time threshold.

---

## Prerequisites

Connect to the Redis CLI via the redis-client pod. Get connection instructions:

```bash
helm status -n ef-external redis
```

Follow the printed instructions to connect to the redis-client pod. Once inside the pod, you will be connected to the Redis master.

---

## Step 1: Set the Slow Log Threshold

Configure the execution time threshold. Any command taking longer than this value is recorded in the slowlog:

```
CONFIG SET slowlog-log-slower-than <threshold_in_microseconds>
```

For example, to log commands slower than 10 milliseconds (10,000 microseconds):

```
CONFIG SET slowlog-log-slower-than 10000
```

| Value | Behavior |
|---|---|
| Positive integer | Log commands slower than this many microseconds |
| `0` | Log every command |
| `-1` | Disable slowlogs |

---

## Step 2: Set the Slowlog Buffer Size

Limit the number of entries saved to avoid memory exhaustion:

```
CONFIG SET slowlog-max-len <amount>
```

The default is 128 entries. When the buffer is full, the oldest entries are dropped. Set a value appropriate for your investigation window.

---

## Step 3: Retrieve Slowlog Entries

View the most recent slowlog entries:

```
SLOWLOG GET <no-of-entries>
```

For example, to retrieve the 25 most recent slow commands:

```
SLOWLOG GET 25
```

Each entry includes:
- Unique log ID
- Timestamp (Unix epoch) when the command was logged
- Execution time in microseconds
- Command and arguments
- Client IP and name

---

## Using the Monitor Command

For real-time observation of all active Redis operations, use:

```
monitor
```

> **Caution**: `monitor` streams every command processed by Redis in real time and has significant performance impact. Use it only briefly during active investigation, then exit with `Ctrl+C`.

---

## Step 4: Disable Slowlogs

When your investigation is complete, disable slowlogs to avoid ongoing overhead:

```
CONFIG SET slowlog-log-slower-than -1
```

---

## Related Articles

- [MongoDB Slow Query Logs](MongoDB-Slow-Query-Logs.md)
- [Accessing Kubernetes Logs](Accessing-Kubernetes-Logs.md)
