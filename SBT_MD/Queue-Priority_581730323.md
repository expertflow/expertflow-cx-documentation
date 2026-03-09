# CX Knowledgebase : Queue Priority

Queue Priority allows you to control which customer requests get handled first when you have multiple queues competing for the same agents. Think of it as a VIP system - high-priority queues (like Premium Support or Emergency Issues) get served before standard queues.

**Why use Queue Priority?**

  * Ensure VIP customers get faster service

  * Handle urgent issues before routine requests

  * Meet different Service Level Agreements (SLAs) for different customer tiers

  * Optimize agent efficiency by routing the most important requests first




## How Queue Priority Works

### Priority Levels

  * Queue priority ranges from **1 to 10**

  * **1 = Lowest Priority** (handled last)

  * **10 = Highest Priority** (handled first)




### Request Routing Order

When multiple requests are waiting and an agent becomes available, the system follows this order:

**Step 1: Queue Priority First**

  * Requests from higher-priority queues are always handled before lower-priority ones

  * Example: Priority 8 queue requests go before Priority 5 queue requests




**Step 2: Task Priority Within Queues**

  * If multiple queues have the same priority, the individual request priority determines the order

  * Higher-priority requests within any queue get handled first




**Step 3: First In, First Out (FIFO)**

  * If both queue priority and request priority are equal, the longest waiting request goes first

  * This ensures fairness for requests with the same importance level




## Setting Up Queue Priority

### When Creating a New Queue

  1. In the queue creation form, locate the **"Queue Priority"** field

  2. Enter a number between 1-10 based on your business needs:

     * **8-10** : Critical/VIP queues (Emergency Support, Premium Customers)

     * **5-7** : Standard queues (General Support, Sales)

     * **1-4** : Low priority queues (Follow-ups, Surveys)




### For Existing Queues

  1. Navigate to your queue list

  2. Click the dropdown (⋮) next to the queue you want to modify

  3. Select "Edit Queue"

  4. Update the Queue Priority field

  5. Save your changes




## Real-World Examples

### Example 1: Customer Service Tiers

**Setup:**

  * VIP Support Queue: Priority **9**

  * Standard Support Queue: Priority **5**

  * General Inquiries Queue: Priority **3**




**Result:** VIP customers always get connected first, even if standard customers have been waiting longer.

### Example 2: Departmental Priorities

**Setup:**

  * Emergency Technical Issues: Priority **10**

  * Sales (Hot Leads): Priority **7**

  * Sales (General): Priority **5**

  * Billing Questions: Priority **4**




**Result:** Technical emergencies get immediate attention, followed by sales leads, then routine inquiries.

### Example 3: Time-Sensitive Requests

**Setup:**

  * Live Chat (immediate response needed): Priority **8**

  * Email Support (24-hour SLA): Priority **4**

  * Feedback Forms (no strict SLA): Priority **2**




**Result:** Live chat customers get instant routing while emails and forms can wait for available agents.

## Best Practices

### Priority Assignment Guidelines

  * **Reserve 9-10** for true emergencies or highest-tier customers

  * **Use 6-8** for standard business-critical queues

  * **Use 1-5** for routine, non-urgent requests




### Balancing Service Levels

  * Don't make too many queues high priority - this defeats the purpose

  * Monitor queue performance to ensure lower-priority customers aren't neglected

  * Consider time-based escalation for requests that wait too long




### Agent Distribution

  * Ensure you have enough agents skilled for your highest-priority queues

  * Consider dedicated agents for critical queues during peak hours

  * Monitor agent workload to prevent burnout from constant high-priority requests




## Important Considerations

### Agent Availability Impact

  * Priority only matters when agents are busy and multiple requests are waiting

  * If you have plenty of available agents, all requests get handled quickly regardless of priority

  * During off-peak hours, priority differences may not be noticeable




### Mixed Priority Scenarios

  * An agent handling a low-priority request will finish that request before taking a high-priority one

  * Priority affects which request gets routed next, not which request gets interrupted




## System Configuration (Advanced Users)

### Enabling/Disabling Queue Priority Feature

 _Note: This section is for technical administrators. If you experience issues with these steps, please contact your system administrator or support team._

Queue Priority is controlled by a backend feature flag. By default, this feature is disabled. To enable or disable it:

  1. Navigate to the core components values file in your Helm deployment folder:
[code] cim-solution/kubernetes/helm-values
[/code]

  2. Locate this environment variable in the core component's helm values file:
[code] extraEnvVars:
             - name: IS_QUEUE_PRIORITY_ENABLED
               value: "false"
[/code]

  3. Update the value as needed:

     * `"true"` to enable Queue Priority

     * `"false"` to disable Queue Priority

  4. Update the Helm release for the core group using this command from the `cim-solution/kubernetes` directory:
[code] helm upgrade --install --namespace expertflow --create-namespace ef-cx --debug --values helm-values/ef-cx-custom-values.yaml expertflow/cx --version <Specify Chart Version here>
[/code]




**Important:** Always backup your configuration before making changes and test in a staging environment first.

## Monitoring Queue Priority Performance

Track these metrics to optimize your priority settings:

  * **Average wait times by queue priority**

  * **Service level achievement by priority**

  * **Agent utilization across priority levels**




## **Limitation**

### Agent Reserved State Limitation

When an agent is in the **RESERVED** state (due to receiving a chat request), the following behavior occurs:

**Scenario:** Single agent available, currently in RESERVED state

  1. Agent receives a chat request and enters RESERVED state

  2. New requests from other queues arrive while agent is reserved

  3. Agent accepts the original chat request

  4. **Issue:** The agent will NOT receive the waiting requests from other queues automatically




**Why this happens:**

  * Only the queue associated with the accepted chat remains active for that agent

  * Other queues are not triggered during this time

  * Requests from different queues remain unrouted to that specific agent




**Workarounds:**

  * **Multiple agents:** This limitation only affects scenarios with a single available agent

  * **Manual intervention:** Agent can manually change the MRD (Media Routing Domain) associated with the queue

  * **Wait for availability:** Requests will be routed when another agent becomes available




**Impact:** This primarily affects deployments with very few agents or during off-peak hours when only one agent is available across multiple queues.

* * *

_Need help with Queue Priority setup or configuration? Contact your system administrator or support team for assistance._
