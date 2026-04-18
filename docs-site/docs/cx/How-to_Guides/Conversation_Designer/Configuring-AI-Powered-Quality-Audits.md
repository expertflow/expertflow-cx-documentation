---
title: "Configuring AI-Powered Quality Audits"
summary: "Technical guide for implementing automated and hybrid conversation scoring using LLMs."
audience: [conversation-designer]
product-area: [ai-features, quality-management]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# Configuring AI-Powered Quality Audits

Automated Quality Management (QM) enables objective evaluation of 100% of customer interactions. This guide details how to configure the AI Evaluator, tune prompts, and manage hybrid human-AI workflows.

## 1. Prerequisites

Ensure the following components are deployed and accessible:
- **AI Evaluator Service:** Deployed via Helm in the `ef-ai` namespace.
- **LLM Connector:** Active connection to OpenAI, Azure OpenAI, or a local LLM.
- **Unified Admin:** Quality Management module enabled.
- **Conversation Manager:** Configured to push closed interactions to the AI queue.

## 2. Setting the Operational Mode

ExpertFlow supports two modes for quality auditing. Configure these in **Unified Admin > Quality > Global Settings**.

| Mode | Description | Primary Use Case |
|------|-------------|------------------|
| **Full Automation** | AI scores 100% of interactions. | High-volume retail or tier-1 support. |
| **Hybrid** | System distributes audits between AI and Humans. | Regulated industries requiring human calibration. |

### Steps to Configure Hybrid Distribution:
1. Navigate to **Audit Assignment Rules**.
2. Set the **AI Weight** percentage (e.g., 80%).
3. Assign the remaining **Human Weight** to specific Evaluator (Eva) groups.

## 3. Prompt Engineering for Quality Rubrics

The AI scores interactions by interpreting a **Prompt Template** derived from your Evaluation Forms.

### Mapping Rubrics to LLM Logic
For each question in your evaluation form, the AI Specialist must define a prompt condition.

**Example Rubric Item:** "Did the agent use the standard greeting?"
**AI Instruction:** "Search the first 3 interaction turns. If the agent used the phrase 'Welcome to [Brand]', set Score = 1. Else, set Score = 0."

### Updating the Scoring Prompt:
1. Access the **NLU Config Tool** or use the **AI Evaluator API**.
2. Update the `scoring_template.json` with your specific business rules.
3. Validate the prompt using the **Test Interaction** sandbox.

## 4. Calibrating the AI Evaluator

To ensure accuracy, Quality Managers (Quentin) must perform periodic calibration.

1. **Review AI Scores:** Filter the **Conversation List** for "AI-Audited" interactions.
2. **Override Scores:** If an AI score is incorrect, click **Override** and enter the manual score.
3. **Feedback Loop:** Overridden interactions are flagged for the AI Specialist to retrain the model or tune the prompt.

## 5. Supported Languages

The AI Evaluator currently supports:
- **English:** All dialects.
- **Arabic:** Specialized support for Egyptian dialect.

---

*Need help tuning your LLM? Contact the AI Implementation Team.*
