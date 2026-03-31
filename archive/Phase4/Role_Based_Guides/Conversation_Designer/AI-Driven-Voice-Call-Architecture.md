---
title: "AI-Driven Voice Call Architecture"
summary: "Explains how an AI-driven voice call flows through ExpertFlow CX — from inbound call through Jambonz and a voice AI agent, through N8N for business logic, and how control converges with the digital channel path at Channel Manager for human agent handoff."
audience: [designer]
product-area: [voice, ai, channels]
doc-type: explanation
difficulty: intermediate
keywords: ["AI voice call CX", "Jambonz CX", "ElevenLabs CX", "N8N CX", "voice AI agent CX", "human handoff voice CX", "channel manager API CX"]
aliases: ["voice AI architecture CX", "AI voice flow CX"]
last-updated: 2026-03-21
---

# AI-Driven Voice Call Architecture

ExpertFlow CX supports two interaction paths: **digital channels** (chat, WhatsApp, email, social) and **AI-driven voice**. Both paths converge at the same point — Channel Manager — before routing to a human agent. Understanding this architecture helps you design flows and handoff conditions correctly.

---

## The Two Paths

### Voice AI Path

```
Inbound call
     ↓
Jambonz  (Voice AI Gateway / Media Server)
     ↓
Voice AI Agent  (ElevenLabs / Hamsa or equivalent)
— listens, understands intent, responds in natural language
     ↓
N8N  (business logic orchestration)
— deterministic workflows: account lookup, ticket creation, order status, etc.
     ↓
[ human agent needed ]
     ↓
Jambonz  (control returned to Media Server)
     ↓
Channel Manager API  (CX-Core)
     ↓
[ same as digital path from here ]
```

### Digital Channel Path

```
Customer message
     ↓
Channel Connector API
     ↓
Channel Manager  (CX-Core)
     ↓
Conversation Manager  (CX-Core)
     ↓                          ↓
Conversation Studio         Routing Engine
(control flow logic)              ↓
                            Agent Manager
                            (tracks all active agents)
                                  ↓
                            Agent Desk
                            (ExpertFlow UI or 3rd-party app via Agent SDK)
```

### Where the Paths Merge

Both paths enter CX-Core through the **Channel Manager API**. Once a voice AI call requires a human agent, Jambonz calls the same Channel Manager API that a digital channel connector uses. From that point on, the routing, agent selection, and handoff logic is identical.

---

## Component Roles

| Component | Role | Owned by |
| :--- | :--- | :--- |
| **Jambonz** | Voice AI Gateway and Media Server — receives inbound calls, bridges to the voice AI agent, returns control when handoff is needed | Infrastructure / Hosting Partner |
| **Voice AI Agent** (ElevenLabs, Hamsa, or equivalent) | Handles the voice conversation — speech-to-text, intent understanding, text-to-speech response | AI Specialist |
| **N8N** | Executes deterministic business workflows triggered by the AI agent (data lookups, API calls, conditional routing) | AI Specialist / Integration Specialist |
| **Channel Connector API** | Entry point for digital channel messages into CX-Core | Infrastructure / Hosting Partner |
| **Channel Manager** | Receives all inbound interactions — both voice (via Jambonz) and digital (via Channel Connector). Single entry point into CX-Core | CX Platform |
| **Conversation Manager** | Orchestrates the conversation lifecycle — invokes Conversation Studio for flow logic and Routing Engine for agent selection | CX Platform |
| **Conversation Studio** | Where you design control flows — bot logic, conditions, survey nodes, handover triggers | **Conversation Designer** |
| **Routing Engine** | Selects the right agent or queue based on skills, availability, and routing rules | Solution Admin |
| **Agent Manager** | Maintains real-time state of all active agents and their availability | CX Platform |
| **Agent Desk** | The UI agents use to handle interactions. Can be ExpertFlow's native Agent Desk or any 3rd-party application built on the Agent SDK | Agent / Frontend Developer |

---

## Conversation Designer's Responsibilities

Your work as a Conversation Designer lives inside **Conversation Studio**, which is part of the digital channel path. For AI-driven voice, Conversation Studio is not involved in the voice AI conversation itself — that is handled by the voice AI agent and N8N.

**You are responsible for:**
- Designing control flows in Conversation Studio for digital channels
- Configuring bot-to-agent handover conditions (sentiment, intent, explicit customer request)
- Building outbound and survey flows
- Registering bot connectors

**You are not responsible for:**
- Configuring the voice AI agent on ElevenLabs or Hamsa — that is the AI Specialist's role
- Building N8N workflows — that is the AI Specialist or Integration Specialist's role
- Deploying or configuring Jambonz — that is the Infrastructure / Hosting Partner's role

---

## Human Handoff in the Voice AI Path

When N8N determines a human agent is needed (based on workflow conditions), it returns control to Jambonz. Jambonz then calls the **Channel Manager API** with the interaction context. From that point, Conversation Manager takes over, invokes the Routing Engine to select the right agent, and the interaction appears in Agent Desk.

The handoff trigger logic lives in N8N — not in Conversation Studio. If you need to influence handoff conditions in a voice AI flow, coordinate with the AI Specialist who owns the N8N workflow.

---

## Related Articles

- [AI Sentiment-Based Handover](./AI-Sentiment-Based-Handover.md)
- [Registering Bot Connectors](./Registering-Bot-Connectors.md)
- [NLU and Digital Bots for Voice](./NLU-Digital-Bots-Concepts.md)
- [Conversation Flow for Outbound Dialing Modes](./Conversation-Flow-for-Outbound-Dialing-Modes.md)
