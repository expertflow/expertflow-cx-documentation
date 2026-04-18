---
title: "System Behaviour in Case of Failover"
summary: "Reference analysis of failover behavior across ExpertFlow CX channels — covering Email and Web channel scenarios at each conversation stage, session recovery behavior, and known limitations with stateful components."
audience: [platform-operator]
product-area: [platform]
doc-type: reference
difficulty: advanced
keywords: ["failover behavior CX", "HA failover CX", "system failover CX", "email failover CX", "web channel failover CX", "conversation recovery CX", "high availability CX behavior"]
aliases: ["CX failover behavior", "system behaviour failover CX", "HA conversation recovery CX"]
last-updated: 2026-03-10
---

# System Behaviour in Case of Failover

This reference covers how active and new conversations behave across ExpertFlow CX channels during a failover event in a High Availability (HA) deployment. It is intended for system architects, DevOps engineers, QA teams, and product managers.

---

## Email Channel

| Scenario | Current Behavior | Roadmap Improvement |
|---|---|---|
| Customer sends email while system is down | EFCX cannot fetch emails from the exchange server. Emails remain on the exchange but are **not fetched** when the system recovers. | Store last-fetch timestamp. On recovery, fetch all emails received during downtime. **Target: Aug 2025** |
| Email fetched by connector but not yet sent to CCM when system goes down | Email is not processed. Not retried after recovery. | Resolved by the timestamp-based fetch improvement above. |
| Email sent to CCM but conversation not yet created when system goes down | On recovery, email is processed normally and routed to agent or bot. | — |
| CCM received email, created conversation, routed to bot — bot has not responded yet | Bot does not respond after recovery. | **Target: Q4 2025** |
| Conversation queued and waiting for agent assignment | On recovery, routing engine restores all queued conversations and routes them to available agents. | — |
| Conversation offered to agent (ringing), agent has not accepted | System down: agent sees error, cannot accept. On recovery: conversation rings again for the agent to accept. | — |
| Agent has accepted conversation — active state | System down: agent sees error, cannot respond. On recovery: all active chats are restored. | All timers should resume from point of failure. **Target: Q4 2025** |
| Conversation in wrap-up state | System down: agent cannot apply wrap-up. On recovery: all wrap-up conversations are restored. | — |

---

## Web Channel

| Scenario | Current Behavior |
|---|---|
| Customer tries to open widget while system is down | Widget does not load — chat is never initiated. |
| Customer fills form and starts chat, but system goes down before connector receives request | Request is not processed and is not retried after recovery. |
| Connector received request but not yet forwarded to CCM | Not processed after recovery. |
| CCM received `START_CHAT` intent but system goes down before processing | Not processed after recovery. |
| CCM published `CHANNEL_SESSION_STARTED` | On recovery, all active sessions are restored. |
| Active session: customer sent first message (published to AMQ topic) | On recovery, all active chats and customer messages are restored from ActiveMQ. |
| Bot received customer message but has not responded yet | Bot does not respond after recovery. |
| Customer message triggers agent routing — conversation queued | On recovery, routing engine restores all queued conversations and routes them to available agents. |
| Conversation ringing on agent, not yet accepted | System down: agent sees error. On recovery: conversation rings again. |
| Agent has accepted — active state | System down: agent sees error. On recovery: all active chats are restored. |
| Conversation in wrap-up state | System down: agent cannot apply wrap-up. On recovery: all wrap-up conversations are restored. |

---

## Critical: Stateful Component Limitations

> Redis, ActiveMQ/PostgreSQL, and MongoDB are typically deployed **outside** the Kubernetes cluster and are a **single point of failure**.

If any of these components go down:

- **All active conversations are permanently lost** — they cannot be recovered even after the components come back up.
- **No new conversations are accepted** while any of these components are unavailable.
- The system will exhibit unexpected behavior.

**Recommendation**: Deploy Redis, ActiveMQ, PostgreSQL, and MongoDB as HA StatefulSets (or managed HA services) to eliminate this single point of failure.

---

## Related Articles

- [Failover Cluster with Replicated Block Volume](../../Reference/Archive-Notice.md)
- [Kubernetes Distributions](Kubernetes-Distributions.md)
- [Deploying the RKE2 Control Plane](Deploying-the-RKE2-Control-Plane.md)
