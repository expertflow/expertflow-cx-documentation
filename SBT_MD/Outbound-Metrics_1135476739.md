# CX Knowledgebase : Outbound Metrics

Our omni-channel outbound solution provides a comprehensive set of metrics, accessible via intuitive dashboards powered by Prometheus and visualized in Grafana (real-time) and Superset (historical). These metrics enable business users to monitor outbound campaign performance in real time, analyze historical trends, and optimize both operational efficiency and SLA adherence.  
  
This document outlines the integrated metrics and reporting capabilities of our platform. The analytics suite combines real-time tracking with historical reporting to support performance monitoring, trend analysis, and data-driven decision-making.

We offer a set of standard **dashboards** and **historical reports** for immediate visibility into key KPIs. For advanced analysis, users can leverage a wide range of exposed metrics to create **custom dashboards** and **reporting views** aligned to specific business needs.

For example, you can track precisely:

  * The rate at which contacts are loaded into a campaign.

  * The number of contacts that pass or fail a condition node (e.g., "is customer balance > $500?").

  * The success and failure rates of digital messages, segregated by channel type.




This level of detail provides unparalleled power for campaign optimization, allowing you to pinpoint the exact stage in a customer journey that may be causing friction or drop-off.

## 1\. Metrics 

This section outlines key metrics, the nodes that expose them, and their relevance.

  * Each metric has attributes such as a name, description, method of calculation, unit of measure (e.g., seconds, percentage), and context (channel, time period).

  * defined by _standardized formulas_ and measurement guidelines (e.g., how to calculate AHT or FRT).




### Summary Table of a Typical Contact Center Metric Definition Elements

Attribute| Description  
---|---  
Metric Name| The recognized name, e.g., First Response Time (FRT)  
Metric Purpose| What aspect of performance does it measure  
Measurement Unit| Time (seconds/minutes), count, percentage, score, etc.  
Calculation Method| Formula or approach (e.g., FRT = time from customer contact to first agent response)  
Context/Scope| Which channels, agent groups, or periods does the metric apply to  
Benchmark/Standard| Industry typical target or range values  
  
### 1.1. Granularity

Granularity in metrics refers to the level of detail (i.e., how finely or coarsely) at which the data is measured, recorded, or aggregated, especially over time. It answers the question of _how detailed_ or _how often_ a metric is captured or reported. In short, you choose your granularity based on whether you need to see **every tiny detail** (High) or prioritize **efficiency and long-term views** (Low). Data collected every minute is more granular than data collected hourly. First Response Time data might be recorded with granularity down to the **second level** (fine granularity) or aggregated as daily averages (coarser granularity).

  * **High**(or Fine): The data is recorded or aggregated over very short time intervals (e.g., every 1 second, 10 seconds, or 1 minute).

  * **Intermediate** : The data is recorded or aggregated over medium time intervals. This level provides a balance between detail and storage efficiency, making it ideal for operational monitoring. (e.g., every 5 minutes, 10 minutes, or 30 minutes)

  * **Low**(or Coarse): The data is aggregated over longer time intervals (e.g., every 1 hour, 1 day, or 1 week).




### 1.2. Labels

Key-value pairs that enable a **multi-dimensional data model** in Prometheus. They allow you to segment and filter the base metric. For example, the metric `ob_dial_attempts_total` can be filtered by `campaign_id` to see attempts for a specific campaign, or by `dial_result` to see only busy signals.

### 1.3. Metric Types

**Metric Type**|  Description  
---|---  
Counter| A cumulative metric that represents a single monotonically increasing counter whose value can only be incremented or reset to zero on restart. _Use for counts of events (e.g., successful dials, total calls)._  
Gauge| A metric that represents a single numerical value that can arbitrarily go up and down. _Use for current states (e.g., contacts remaining, number of active agents)._  
Histogram| Samples observations (usually durations or sizes) and counts them in configurable buckets. It also provides a sum of all observed values. _Use for request latencies or durations (e.g., wait time, wrap time)._  
Summary| Similar to a Histogram, but also calculates configurable client-side quantiles over a sliding time window. _Use for service-level objective (SLO) monitoring of durations._  
  
### 1.4. Terminologies

Term|  Definition  
---|---  
Recently| between the last 5 minutes and the last 30 days  
Interval| The sampling interval can be any time duration between 1s and 15 m.  
  
## 2\. Functional Metric Classification

To ensure comprehensive monitoring, all platform metrics are grouped into three functional categories based on their purpose within the system and the teams they serve. This classification ensures distinct visibility into **business outcomes** , **system health** , and **user experience** , allowing for targeted dashboarding and alerting.

**Category Title**| **Purpose**  
---|---  
**Entity**(Object State & Flow) Metrics| Monitors the aggregate state and flow of core business entities (e.g., **Contacts, Campaigns, Agents**). Metrics track the population count residing in specific states (**Inventory/Backlogs** via Gauges) and the cumulative volume that has completed transitions (Throughput/Outcomes via Counters).

  * e.g., `ob_contacts_to_load`****(Gauge): The current count of contacts awaiting processing (Inventory/Backlog).
  * e.g., `ob_contacts_loaded_total` (Counter): The cumulative number of contacts that have completed the loading step (Throughput).

  
**Flow** Metrics| Monitors the real-time operational values and dynamic performance ratios generated at key decision and control points _within the Outbound Dialing Flow_. These metrics are crucial for controlling the system's behavior (e.g., dialing mode/efficiency, agent reservation, cpa logic, error rate, etc. ) and optimizing the flow's moment-to-moment efficiency. They represent instantaneous calculated states or ratios, and do not track the aggregate status or cumulative outcome of contact entities.

  * e.g., `ob_cpa_machine_ratio` (Gauge): The instantaneous ratio of calls currently classified as Machine vs. Human by the Call Progress Analysis (CPA) node. (A real-time performance indicator of the flow's effectiveness).
  * e.g., `ob_init_calls_per_agent` (Gauge): The calculated value used by the INIT Node that determines the**** rate of call initiation per every reserved agent, which dictates the dynamic dialing mode (predictive vs. power). (A real-time flow control parameter).

  
**Performance** Metrics| Measures the time taken to complete critical system actions and state transitions (Service Level Indicators).

  * e.g., `api_fetch_duration_seconds_p99`****(Histogram/Summary): The 99th percentile of time taken to fetch a contact record from the database (System Responsiveness).
  * e.g., `agent_handle_time_seconds_avg`****(Gauge): The average time an agent spends on a single connected call (Process Speed).

  
  
### 2.1. Entity (Object State & Flow) Metrics

Below are the currently available metrics for each entity type.

#### 2.1.1 Entity: OB Flow (campaign) metrics

**Metric Name**| **Metric Type**| **Overview**| **Key Label(s)**| **Granularity**| **Source Node**  
---|---|---|---|---|---  
`ob_contacts_to_load`PLANNED | Gauge| The number of contacts pending (from CX Filters) to be ingested into this campaign.**Allows you to monitor:**

  * The backlog and speed of the contact ingestion process.

| 

  * campaignName

| 

  * **High** (Fine): 1 Minute

| Campaign Init  
`ob_contacts_loaded_total`AVAILABLE | Counter| The cumulative number of unique (unless a restart occurs) contacts successfully **ingested** and made available for dialing/contacting in this campaign flow.**Allows you to monitor** :

  * The total size of the contact list and verify ingestion completion.

| 

  * campaignName
  * order (FIFO/LIFO)

| 

  * **High** (Fine): 1 Minute

| Campaign Init  
`ob_contacts_unqualified_total`PLANNED | Counter| The cumulative count of contacts scrubbed/removed from the list _before_ any dialing attempt.**Allows you to monitor** :

  * List **data quality** and loss volume.

| 

  * campaignName
  * reason
    * (e.g., format_issue, duplicate)

| 

  * **Intermediate** (5-10 Minutes)

| Dialer Nodes

  * CCX Dialer
  * CCE Dialer
  * CX Dialer

  
`ob_contact_condition_evaluations_total`PLANNED | Counter| The cumulative count of contacts that have been evaluated against a specific condition set up within the campaign flow.**Allows you to monitor** :

  * The **throughput and success rate** of a specific business rule or segment filter within the execution flow.

| 

  * campaignName
  * condition_name
    * The name of the specific condition node, e.g., "CountryCheck"
  * status
    * **passed** or **failed**

| 

  * **Intermediate**(5 Minutes)

| Condition  
`ob_contact_decision_evaluations_total`PLANNED | Counter| This metric counts the number of contacts that have passed a specific condition within a campaign's **decision node**.**Allows you to monitor** :

  * The volume and effectiveness of **contact recent filtering** to ensure only eligible contacts continue in the campaign flow.

| 

  * campaignName
  * decision_name
    * The name of the specific decision node, e.g., "RetryOnBusy"
  * status
    * **passed** or **failed**
  * ~~reasonCode~~
    * ~~e.g., busy, read~~

| 

  * **Intermediate**(5 Minutes)

| Decision  
**Dialer Metrics**  
`ob_contacts_sent_for_dialing`AVAILABLE | Counter| This metric counts the total number of contacts pushed to the Dialer Nodes for execution. It can be broken down for more granular insights:**I would like to monitor** : 

  * number of `ob_contacts` sent for dialing every execution cycle
  * total `ob_contacts` sent for dialing so far (per channel)
  * **dialing volume by hour** , i.e. number of outbound contacts sent for dialing in each hour of the day to compare campaign dialing volume trends by time

| 

  * campaignName
  * channelType

| 5 min| UCCE/UCCX Dialer, EFCX Dialer  
`ob_call_results`AVAILABLE | Counter| This metric counts the total number of recent call results generated by the dialer. It can be broken down for more granular insights:**I would like to monitor** : 

  * the total number of recent call results, **segregated by outcome,** so that I can analyse performance effectively.
  * call results segmented by **status** and **reasonCode** , so that I can perform a more detailed analysis.

| 

  * campaignName
  * channelType
  * status _(high-level result: answered, busy, etc)_
  * reasonCode _(user_declined_

|  5 min| UCCE/UCCX Dialer, EFCX Dialer  
`ob_dialing_in_progress`AVAILABLE | Gauge| This metric offers a live snapshot of your dialer's workload by counting the number of in-progress contacts currently being dialed.**I would like to monitor** : 

  * I would like to monitor **dialer load in real time**.
  * I would like to track dialing volume versus available agents so that I can help avoid overload.

| 

  * campaignName
  * channelType

| 5 min| UCCE/UCCX Dialer, EFCX Dialer  
**Digital Messaging Metrics**  
`ob_messages_sent_total`AVAILABLE | Counter| This metric counts the number of outbound messages sent per campaign and per channel type, allowing you to track the total message volume across all digital channels, like SMS and email. Key uses include:

  * **Channel Load Monitoring** : Identify if certain channels are handling disproportionately high volumes, which may indicate overuse
  * **Campaign Activity Tracking** : Confirm that campaigns are actively sending messages as expected
  * **Historical Trend Analysis** : Track message volume trends over time to evaluate seasonality, growth, or decline in outreach
  * **Quota and Cost Monitoring** : Estimate costs or monitor message limits, especially in environments with channel-based pricing (e.g., SMS)

| 

  * campaignName
  * channelType

| 5 min| Digital Channel Message  
`ob_message_results_total`AVAILABLE| Counter| This metric counts the number of outbound messages that came back with a message result per campaign and channel type, allowing you to track the delivery performance of digital messaging campaigns, investigate failures by channel or campaign, and refine strategy by identifying high-performing channels.Key uses include:

  * Measure the effectiveness and delivery success rates of your digital messaging campaigns.
  * Diagnose delivery problems by filtering for failed results on specific channels or campaigns.
  * Optimize your channel strategy by identifying which channels (`channelType`) provide the highest delivery success rates.

| 

  * campaignName
  * channelType
  * result
    * e.g., Failed/ Sent

| 5 min| Digital Channel Message  
`ob_message_delivered_total`ROADMAP | Counter| Counts the total number of digital outbound messages (SMS, WhatsApp, Email, etc.) that were successfully delivered to recipients, as confirmed by the provider.

  1. **Delivery Assurance** : Verifies how many outbound messages reached the intended recipient.
  2. **Channel Performance Tracking** : Helps compare delivery success across channels.
  3. **Failure Diagnosis Support** : When paired with failure metrics, helps identify drop rates, blocks, or provider issues.

**I would like to monitor** :

  * Number of messages successfully delivered per campaign and channel
  * Delivery rate per channel: `(message_delivered_total ÷ message_sent_total) × 100`

| 

  * campaignName
  * channelType

| 5 min| Digital Channel Message _(via provider delivery APIs)_  
`ob_message_failed_total` ROADMAP 2026 | Counter| Counts the number of outbound digital messages (SMS, WhatsApp, Email, etc.) that failed to deliver due to issues like invalid numbers, content rejections, or provider/network errors.

  * **Failure Tracking** : Shows how many messages did not reach the end user.
  * **Channel Quality Control** : Helps detect which channels have higher error rates.
  * **Diagnostic Signal** : Indicates list quality, opt-out enforcement, or content/template issues.

**I would like to monitor** :

  * Total number of failed messages per campaign and channel
  * Common failure types: invalid number, blocked content, opt-out violation
  * Channels with high failure rates to improve targeting or compliance

| 

  * campaignName
  * channelType
  * failureReason _(e.g. WhatsApp: template_rejected, unregistered_number, rate_limited, session_expired, provider_error, SMS: carrier_blocked, unsupported_country, Email: spam_blocked, hard_bounce, soft_bounce…)_

|  5 min| Digital Channel Message _(via provider delivery APIs)_  
`ob_message_read_total` ROADMAP May be available for **limited** channels. | Counter| Counts the number of outbound digital messages (e.g., WhatsApp, Messenger) that were successfully **read or seen** by the recipient, based on read receipts supported by the messaging platform.

  * **Engagement Tracking** : Measures the level of actual message interaction, beyond just delivery.
  * **Channel Performance Indicator** : Helps compare user engagement across different digital channels.
  * **Supports Optimization** : Enables refining retry and fallback logic based on whether users are actually reading messages.

**I would like to monitor** :

  * How many messages per campaign were read after delivery
  * Compare engagement across WhatsApp, Messenger, etc.
  * Identify low-engagement channels or message formats

| 

  * campaignName
  * channelType

| 5 min| Digital Channel Message _(via provider delivery APIs)_  
`ob_message_read_rate`ROADMAP May be available for **limited** channels. | Gauge (Calculated)| Measures the percentage of delivered messages that were actually read/opened **(where supported by the channel).**

  1. **Engagement Indicator** : Reading behavior signals contact interest, not just delivery.
  2. **Performance Benchmarking** : Helps determine which channel generates more engagement

**I would like to monitor** :

  * percentage of messages read per channel or campaign
  * Compare engagement between WhatsApp, SMS, email, etc.
  * Improve fallback logic based on read behaviour

**Formula**

  * `(ob_message_read_total ÷ ob_message_delivered_total) × 100`

| 

  * campaignName
  * channelType

| 5 min| Digital Channel Message _(via provider delivery APIs)_  
  
#### 2.1.2 Entity: Agent

**Metric Name**| **Metric Type**| **Overview**| **Key Label(s)**| **Granularity**| **Source Node**  
---|---|---|---|---|---  
`ob_agents_seized_gauge`AVAILABLE DEV-PLANNED for the addition of the queueName label. | Gauge| The current number of agents actively reserved ("seized") by the system for the campaign's current dialing requirements. This is a real-time count. This metric directly reflects the success of the pacing algorithm in reserving the necessary human resources calculated by the Seize Node. **Allows you to monitor:**

  * Real-time agent reservation to ensure the dialer has the required resources to match the dynamic dialing ratio.
  * The success of the pacing algorithm in reserving resources. Observing this value against `ob_agents_needed_gauge` (the calculated requirement) shows if the Seize Node is actively meeting the need or is over-seizing/under-seizing.

| 

  * campaignName
  * queueName

| 10 Seconds (or less)| SIEZE  
`ob_agents_available_gauge`ROADMAP 2026 | Gauge| The total number of agents currently logged in, ready, and potentially available for seizing by any outbound campaign in the Contact Center (CC) that utilizes the specified Queue. This represents the total capacity pool.**Allows you to monitor:**

  * The overall available capacity of the Contact Center for outbound work, segmented by skill or queue.
  * Capacity shortfalls: Comparing this metric to the****`outbound_agents_seized_gauge` metric identifies if the outbound demand is exhausting the total agent pool, triggering a staffing alert if the remaining capacity is too low.

| 

  * queueName

| 1 min| SIEZE  
`ob_agents_idle_gauge`ROADMAP 2026 | Gauge| The current number of agents who are logged in, available, and are currently in an idle/waiting state (i.e., not seized and not on a call) and available to be seized for outbound work.**Allows you to monitor:**

  * The immediate surplus capacity that is not yet utilized by the dialer.
  * Agent Utilization: A persistently high idle count indicates the dialer is not aggressive enough or the list is exhausted, leading to low utilization.

| 

  * queueName

| 1 min| SIEZE  
`ob_agents_acw_gauge`ROADMAP 2026 | Gauge| The current number of agents actively performing After Contact Work (ACW), which is post-call wrap-up, data entry, etc. These agents are temporarily unavailable for new calls.**Allows you to monitor:**

  * Resource recovery timing. These agents represent the _next wave_ of available resources.
  * ACW adherence: A high or fluctuating count may signal that agents are not using ACW time efficiently, impacting overall productivity.

| 

  * queueName

| 1 min| SIEZE  
`ob_agent_talk_time_seconds_sum`ROADMAP 2026 | Counter| The cumulative sum of time (in seconds) spent by agents talking to connected contacts within the campaign flow. Used with the `ob_connected_calls_total` to calculate the Average Talk Time (ATT).**Allows you to monitor:**

  * Agent Productivity: Track agent-level talk time volume (quantity).
  * Pacing Algorithm Input: The historical average talk time is a critical component for predicting when an agent will become free.

| 

  * campaignName
  * agentId

| 5 min| Dialer Nodes  
  
### 2.2. **Flow** Metrics

Below are the currently available flow/operational metrics.

**Metric Name**| **Metric Type**| **Overview**| **Key Label(s)**| **Granularity**| **Source Node**  
---|---|---|---|---|---  
`ob_dial_ratio_setting`DEV-PLANNED | Gauge| The current contact ratio (contact per agent siezed) is currently configured or dynamically calculated for this campaign.**Allows you to monitor:**

  * Track the dialing mode and confirm the dynamic calculation logic is functioning correctly.

| 

  * campaignName

| 5 Seconds (or less)| INIT  
`ob_cpa_result_count` DEV-PLANNED | Counter| | 

  * campaignName
  * result
    * human
    * answering machine
    * failed

| | Dailer Node  
`ob_cpa_machine_ratio` DEV-PLANNED | Gauge (Calculated)| The instantaneous ratio of calls currently classified as Machine vs. Human by the Call Progress Analysis (CPA) node within the outbound flow. A real-time performance indicator of the flow's effectiveness. The value ranges from 0.0 to 1.0.**Allows you to monitor:**

  * Dynamic Pacing Adjustment: Provides real-time input for the predictive dialing algorithm. Change Indication: A rising ratio signals the pace must slow down; a falling ratio signals the pace can safely increase.
  * Instant List Quality Check: Sustained high ratio -> Current list segment has poor answer quality (high voicemail rate).
  * SLA and Efficiency: A sharp spike triggers an alert, indicating an immediate need for operational review to prevent an agent idle-time event.

**Formula**

  * `ob_cpa_result_count{human/ansering_machine}`

| 

  * campaignName

| 10 Seconds (or less)| CPA  
`ob_pending_sieze_requests_total`ROADMAP | Gauge| | 

  * campaignName
  * queueName

| |   
`ob_agents_needed_gauge`ROADMAP | Gauge| The real-time number of agents that the Pacing/INIT Node has determined are immediately required to prevent connected contacts from being abandoned. This value represents the current _human resource demand_ of the flow.**Allows you to monitor:**

  * Demand Signal Health: Tracks the instantaneous need created by the current rate of answered calls that require an agent connection.
  * Resource Gap Analysis: Used in conjunction with `ob_agents_seized_gauge` to measure the gap (shortage or surplus) between the calculated need and the agents actually reserved by the flow.
  * Abandoned Call Risk

| 

  * campaignName
  * queueName

| 5 secs| INIT  
  
### 2.3. **Performance** Metrics

Below are the currently available Performance**** metrics.

**Metric Name**| **Metric Type**| **Overview**| **Key Label(s)**| **Granularity**| **Source Node**  
---|---|---|---|---|---  
`ob_abandoned_calls_total` DEV-PLANNED | Counter| Counts outbound calls that were abandoned before reaching an agent or IVR — whether the contact hung up during ringing or the dialer failed to connect an agent on time.**I would like to monitor** :

  * total outbound abandoned calls per campaign
  * breakdown by **True** vs **Compliance** abandon types
  * hourly abandonment rate to detect agent capacity constraints or pacing issues

| 

  * campaignName

| | UCCE/UCCX Dialer or EF Voice Dialer, derived from `ob_call_results`  
`ob_connected_calls_total`ROADMAP 2026 | Counter| The cumulative number of successful outbound calls that were answered by a human and connected to an agent in the campaign flow.**Allows you to monitor:**

  * Agent Throughput (Quantity): The total volume of productive interactions handled by an agent or campaign.
  * Average Talk Time (ATT) Denominator: This metric serves as the count for calculating ATT (when divided into `ob_agent_talk_time_seconds_sum`).
  * Hit Rate/Conversion Rate: Forms the base for calculating the percentage of calls that lead to a business outcome or sale.

| 

  * campaignName
  * agentId

| 5 min| Dialer/CPA Node  
`ob_dial_to_connect_duration_seconds`ROADMAP 2026 | Histogram / Summary| The duration (latency) from the moment the dialer initiates the call to the moment a live person answers (i.e., CPA is confirmed human).**Allows you to monitor:**

  * Network Latency and List Responsiveness: Measures how quickly calls are answered, which is key for accurate predictive timing.
  * Service Objective: A primary SLI for the quality of the dialing infrastructure. The target **P95** should be set (e.g., < 4.0 seconds).

| 

  * campaignName
  * result (e.g., success, timeout)

| Per Call Event| Dialer/CPA Node  
`ob_hold_time_seconds_avg`ROADMAP 2026 | Gauge / Summary| The average time a successfully answered contact spends on the line waiting for a seized agent to become available. (Also known as "Agent Wait Time" for the customer).This is the most critical compliance and customer experience SLI for predictive dialing. It is regulated by law (ACR, which is directly impacted by high hold time).**Allows you to monitor:**

  * Customer Experience SLI: A measure of the dialing system's over-aggressiveness. High latency here directly leads to high abandoned calls.
  * Pacing Health Check: A high average indicates the dialer ratio (`ob_dial_ratio_setting`) is set too high for the current agent availability.

| 

  * campaignName
  * queueName

| 10 secs| SIEZE/ INIT  
`ob_amd_detection_errors_total`ROADMAP 2026 | Counter| The cumulative number of calls where the Call Progress Analysis (CPA/AMD) node incorrectly classified the answer (e.g., mistook a human for a machine, or vice versa).**Allows you to monitor:**

  * CPA Reliability SLI: An indicator of the technical quality of the answering machine detection (AMD) algorithm.
  * Compliance Risk: A high error rate (especially failing to detect a machine) impacts agent efficiency and list utilization.

| 

  * campaignName
  * detectionType (e.g., Human-to-Machine Error)

| 5 mins| CPA Node  
`ob_contact_rate_ratio`ROADMAP 2026 **Core Campaign Effectiveness (Highest Importance):** This is the ultimate metric for list quality and dialer performance combined. A low rate means the dialer is wasting resources (time, lines) on non-productive dials (busy, no answer, disconnected). It must be constantly monitored to ensure the list is viable and the campaign is economically efficient.| Gauge (Calculated)| The instantaneous ratio of calls resulting in a live human answer (Right Party Contact or any live person) compared to the total number of dials made.**Allows you to monitor:**

  * Real-Time List Quality: A low contact rate signals poor list data (e.g., disconnected numbers, high volume of non-human answers).
  * Overall Dialer Effectiveness: Confirms that the dialer is successfully reaching humans
  * Economic Efficiency: Helps determine if the cost of placing dials is justified by the return in live connections.

**Formula**

  * `ob_connected_calls_total` / `ob_dials_total`

| 

  * campaignName

| 10 secs| Calculated from Dialer/ CPA Nodes  
`ob_dropped_call_rate_ratio`ROADMAP 2026 This high frequency is **mandatory** for maintaining regulatory compliance, as the abandoned call rate must be continuously tracked and controlled to stay below a legally mandated threshold (typically 3% or 5%).| Gauge (Calculated)| The instantaneous ratio of calls that were answered by a contact but dropped (abandoned) before being connected to an available human agent or in IVR.**Allows you to monitor:**

  * Regulatory Compliance SLI: Tracks adherence to laws governing predictive dialing aggressiveness (e.g., Federal Trade Commission rules).
  * Customer Experience Impact: A high rate signals over-aggressiveness, leading to poor customer experience and potential complaints.
  * Pacing Algorithm Health: Directly shows when the dialer's predictions about agent availability are incorrect.

**Formula**

  * `ob_abandoned_calls_total` / `ob_answered_calls_total`

| 

  * campaignName
  * abandonType (_true / compliance_)
  * AbandonReasonCode (_Dialer Abandon, Abandon to IVR, Customer Abandon_)

| 10 secs| Calculated (from Dialer/INIT)  
`ob_list_penetration_ratio`  
ROADMAP 2026 This metric tracks the completeness of the dialing effort. It helps managers understand how close the campaign is to being finished and whether the dialer is stuck, cycling on a small subset of records, or ignoring parts of the list. It is crucial for deciding when to stop the campaign or transition to a different dialing mode (e.g., from predictive to power).| Gauge (Calculated)| The ratio of the number of unique contacts that have been dialed (attempted) at least once, compared to the total number of contacts loaded into the campaign.**Allows you to monitor:**

  * Campaign Completion Progress: Tracks the percentage of the contact list that has been engaged by the dialer.
  * List Health and Stuck Records: A low penetration rate over an extended period indicates the dialer is cycling repeatedly on a small subset of records or failing to access the rest of the list.
  * Management Decision Point: Informs managers when to terminate the campaign, change the list, or switch to a less aggressive dialing mode for the remaining records.

**Formula:**

  * `ob_unique_contacts_dialed` / `ob_contacts_loaded_total`

| 

  * campaignName

| 1 hourThis metric is best aggregated over a campaign batch or hour, as it represents progress toward list exhaustion rather than real-time flow control.| INIT
