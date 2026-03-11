---
title: "AI Orchestration and LLM Logic"
summary: "High-level technical explanation of the division of labor between the LLM Reasoning core and the Execution orchestrator."
audience: [ai-specialist, developer, partner]
product-area: [platform, ai, security]
doc-type: explanation
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# AI Orchestration and LLM Logic

ExpertFlow CX utilizes a decoupled AI architecture that separates **Reasoning** from **Execution.** This ensures high reliability, security, and the ability to leverage multiple AI engines simultaneously.

## 1. The Division of Labor
The system architecture is split into two primary layers:

### The LLM (The Brain)
Responsible for natural language understanding and decision-making.
- **Intent Detection:** Identifies what the user wants to achieve.
- **RAG Pipeline:** Fetches relevant knowledge for general queries.
- **BPMN Triggering:** Recommends deterministic business processes for transactional queries.

### The Orchestrator (The Body)
The secure execution layer that interacts with the platform and external systems.
- **Tool Integration:** Connects to CRMs, APIs, and AI engines (ASR/TTS).
- **Security Guardrails:** Sanitizes inputs to prevent prompt injection and enforces data anonymization (PII masking) before sending data to public LLMs.
- **Validation:** Verifies that LLM outputs match the allowed business logic.

## 2. Engine-Agnostic Design
The Orchestrator communicates through a standardized adapter layer, allowing you to choose your preferred model provider:
- **Commercial APIs:** OpenAI GPT, Google Gemini, Anthropic Claude.
- **Open-Source / Private:** Ollama, Llama 2, Mistral, or ExpertFlow’s proprietary on-premise engine.

## 3. Data Privacy & Sovereignty
- **PII Anonymization:** No customer-specific sensitive data is transmitted to public cloud LLMs. 
- **Hybrid Deployment:** Reasoning can occur in the cloud while all data, workflows, and execution logic remain within your private, secure infrastructure.

---

*To see how this logic applies to bot communication, see [Message Schema Interoperability](Message-Schema-Interoperability.md).*
