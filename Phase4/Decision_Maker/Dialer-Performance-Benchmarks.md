---
title: "Dialer Performance Benchmarks"
summary: "Technical and operational benchmarks for the ExpertFlow CX Dialer, highlighting hardware specs and calls-per-second capabilities."
audience: [decision-maker, partner, integrator]
product-area: [campaigns, infrastructure]
doc-type: reference
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Dialer Performance Benchmarks

This document provides the official performance benchmarks for the ExpertFlow CX Dialer (Outbound Engine). Use these metrics to plan your infrastructure requirements and estimate campaign throughput.

## 1. Reference Infrastructure (Test Lab)
The following specifications were used to achieve the benchmarks listed in this document.

- **Operating System:** Debian 12 (Linux)
- **Core Engine:** FreeSWITCH with FusionPBX 5.2.2
- **CPU:** 8 Cores
- **RAM:** 12-16 GB
- **Storage:** 150 GB ROM

## 2. Calls-per-Second (CPS) Performance
Tests were conducted using IVR-based outbound calls to 2,000 unique customer numbers.

### Case A: 10 Calls Per Second (CPS)
| Concurrent Calls | CPU Usage (FreeSWITCH) | Call Success Rate | Result |
| :--- | :--- | :--- | :--- |
| 500 | 40.3% | 100% | Normal Clearing |
| 1,000 | 57.1% | 100% | Normal Clearing |
| 2,000 | 89.3% | 100% | Normal Clearing |

### Case B: 30 Calls Per Second (CPS)
| Concurrent Calls | CPU Usage (FreeSWITCH) | Call Success Rate | Result |
| :--- | :--- | :--- | :--- |
| 500 | 41.0% | 100% | Normal Clearing |
| 1,500 | 100% | 88.4% | Resource Saturated |
| 2,000 | 100% | 99.5% | High Latency Observed |

## 3. Decision-Maker Recommendations
1.  **Safety Buffer:** For production environments, we recommend keeping CPU utilization below 70% to ensure voice quality and system stability. 
2.  **Scalability:** If your campaign requires more than 1,000 concurrent calls at 30 CPS, we recommend horizontal scaling of the FreeSWITCH nodes.
3.  **Dialer Optimization:** Ensure your [Campaign Strategy](../Solution_Admin/Managing-Outbound-Campaigns.md) accounts for these hardware limits when setting the "Init" node pulse interval.

---

*For detailed deployment instructions, see [Deploying the RKE2 Control Plane](../Getting_Started/Deploying-the-RKE2-Control-Plane.md).*
