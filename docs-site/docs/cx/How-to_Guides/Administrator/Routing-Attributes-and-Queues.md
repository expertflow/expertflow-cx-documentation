---
title: "Routing Attributes and Precision Queues"
summary: "Guide for Solution Admins to configure skills-based routing logic using attributes and precision queue steps."
audience: [administrator]
product-area: [routing, platform]
doc-type: how-to
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Routing Attributes and Precision Queues

As a Solution Admin (Olivia), you control how interactions are distributed to agents. This is achieved through **Routing Attributes** (Skills) and **Precision Queues**.

## 1. Creating Routing Attributes
Attributes define the capabilities of your agents (e.g., Language, Product Knowledge).
1.  Go to **Routing Engine > Routing Attributes**.
2.  **Define Type:**
    - **Proficiency:** A scale from 1 to 10 (e.g., English=10).
    - **Boolean:** A True/False flag (e.g., Certified=True).
3.  **Default Value:** Set a baseline value that is automatically assigned to agents when the attribute is linked to them.

## 2. Assigning Attributes to Agents
1.  Navigate to **Routing Engine > Agent Attributes**.
2.  Hover over an agent and click the **+** icon to add an attribute.
3.  **Override:** You can manually adjust the proficiency level or boolean state for each specific agent here.

## 3. Building Precision Queues
Queues use logic to match a customer's needs with the right agent attributes.
1.  Go to **Routing Engine > Queues** and click **Add Queue**.
2.  **Basic Details:** Link the queue to a **Media Routing Domain (MRD)** (e.g., CHAT or VOICE).
3.  **Define Steps:** This is the heart of your routing logic.
    - **Example Step:** `(English >= 8 AND Sales == True)`.
    - **Step Timeout:** Define how long the system waits (e.g., 30s) before moving to the next step if no matching agent is available.
4.  **Service Levels:** Set the **Service Level Threshold** (e.g., 20 seconds) to enable accurate SLA reporting.

### Best Practices for Olivia:
- **Logical Flow:** Start with strict criteria in Step 1 and relax the requirements in subsequent steps to ensure the customer eventually gets an agent.
- **MRD Mapping:** Ensure the queue's MRD matches the channel's MRD, otherwise interactions will never land in the queue.

---

*Once routing is configured, proceed to [Channel and Connector Setup](Channel-and-Connector-Setup.md).*
