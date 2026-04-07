---
title: "RASA-X Deployment Guide"
summary: "Instructions for deploying Rasa-X using Helm charts to enable NLU model management and training."
audience: [hosting-partner]
product-area: [ai-features, nlu]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-11
---

# RASA-X Deployment Guide

Rasa-X is the interface for managing and training your NLU models. In an ExpertFlow CX environment, Rasa-X is deployed on Kubernetes to provide a collaborative environment for AI Specialists.

## 1. Prerequisites
- **Helm v3** installed and configured.
- **ExpertFlow CX** already deployed in the `expertflow` namespace.
- **Persistent Volume (PV)** storage class configured for Rasa's SQLite/PostgreSQL database.

## 2. Deployment Steps

### Step 1: Add the Rasa Helm Repository
```bash
helm repo add rasa-x https://rasahq.github.io/rasa-x-helm
helm repo update
```

### Step 2: Configure `values.yaml`
Download the default values and update the following:
*   `rasax.token`: Set a secure secret for API authentication.
*   `rasa.model`: Path to your initial model file.

### Step 3: Execute Installation
```bash
helm install rasa-x rasa-x/rasa-x \
  --namespace ef-ai \
  --values rasa-values.yaml
```

## 3. Verification
Access the Rasa-X UI via the ingress or by port-forwarding:
```bash
kubectl -n ef-ai port-forward svc/rasa-x 5002:5002
```

---

## Related Guides
*   [Configuring AI-Powered Quality Audits](../Conversation_Designer/Configuring-AI-Powered-Quality-Audits.md)
*   [AI Orchestration and LLM Logic](../Conversation_Designer/AI-Orchestration-and-LLM-Logic.md)
