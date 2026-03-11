---
title: "CX Dialer Benchmarks"
summary: "Reference benchmark test results for the CX Dialer running at 10 and 30 calls per second, including hardware specs, contact counts, CPU usage, and call success rates."
audience: [solution-admin, decision-maker]
product-area: [voice, dialer]
doc-type: reference
difficulty: intermediate
keywords: ["CX Dialer benchmarks", "dialer performance", "calls per second", "FreeSWITCH CPU", "dialer load testing", "outbound dialer capacity", "CALLS_PER_SECOND"]
aliases: ["dialer performance benchmarks", "CX Dialer load test results", "dialer capacity planning"]
last-updated: 2026-03-10
---

# CX Dialer Benchmarks

This reference documents benchmark test results for the CX Dialer to assist with capacity planning for outbound campaign deployments. Tests were conducted using IVR-based calls to customer numbers via the Scheduler POST API.

> **Version tested:** CX Dialer 4.5-SR11

## Test Hardware Specifications

| Specification | Details |
|---|---|
| **CPU Cores** | 8 |
| **RAM** | 12–16 GB |
| **Storage** | 150 GB |
| **Operating System** | Linux (Debian 12) |
| **FusionPBX Version** | 5.2.2 |

> Both CX Dialer and FreeSWITCH ran on the same virtual machine for these tests.

## Benchmark Results: 10 Calls Per Second

| Test | Contacts Submitted | Contacts in DB | Connected Calls | Failed Calls | FreeSWITCH CPU Usage | Call Result |
|---|---|---|---|---|---|---|
| 1 | 500 | 500 | 500 | 0 | 40.3% | NORMAL_CLEARING |
| 2 | 1,000 | 962 | 962 | 0 | 57.1% | NORMAL_CLEARING |
| 3 | 1,500 | 1,500 | 1,500 | 0 | 81.8% | NORMAL_CLEARING |
| 4 | 2,000 | 1,972 | 1,972 | 0 | 89.3% | NORMAL_CLEARING |

## Benchmark Results: 30 Calls Per Second

| Test | Contacts Submitted | Contacts in DB | Connected Calls | Failed Calls | FreeSWITCH CPU Usage | Call Result |
|---|---|---|---|---|---|---|
| 1 | 500 | 497 | 497 | 0 | 41.0% | NORMAL_CLEARING |
| 2 | 1,000 | 994 | 994 | 0 | 69.8% | NORMAL_CLEARING |
| 3 | 1,500 | 1,326 | 1,326 | 0 | 100.0% | NORMAL_CLEARING |
| 4 | 2,000 | 1,990 | 1,990 | 0 | 100.0% | NORMAL_CLEARING |

## Interpretation

**At 10 calls/second:**
- The system handles up to 2,000 contacts cleanly with 0 failures.
- CPU usage stays under 90% even at 2,000 contacts — acceptable headroom for production use on this hardware tier.
- Minor discrepancies between contacts submitted and contacts in DB (e.g., 1,000 submitted, 962 in DB at Test 2) reflect the natural timing of contact ingestion during the test window.

**At 30 calls/second:**
- CPU reaches 100% at 1,500+ contacts. At full CPU saturation, the system continues to process calls successfully, but there is no headroom for other workloads running on the same server (inbound calls, manual outbound, etc.).
- For production deployments at 30 calls/second, dedicate the FreeSWITCH/Dialer server exclusively to outbound workloads, or scale up hardware.

## Capacity Planning Guidance

| Target `CALLS_PER_SECOND` | Recommended Action |
|---|---|
| ≤ 10 | Standard hardware (8 core / 12 GB RAM) is sufficient for up to 2,000-contact batches. Monitor CPU at peak. |
| 11–30 | Increase RAM to 16+ GB. Dedicate the server to outbound workload. Cap `MAX_CONCURRENT_CALLS` conservatively. |
| > 30 | Scale out to a larger server (16+ core) or distribute across multiple FreeSWITCH instances. Validate SIP trunk concurrent call limits before increasing. |

> The `CALLS_PER_SECOND` value must always remain below the `sessions-per-second` value configured in FreeSWITCH. Exceeding this leaves contacts stuck in `dialed` state. See [CX Dialer Reference](CX-Dialer-Reference.md) for configuration details.

## Related Articles

- [CX Dialer Reference](CX-Dialer-Reference.md)
- [CX Voice Platform Sizing](CX-Voice-Platform-Sizing.md)
- [Outbound Calls](Outbound-Calls.md)
- [Managing Outbound Campaigns](../../Solution_Admin/Managing-Outbound-Campaigns.md)
