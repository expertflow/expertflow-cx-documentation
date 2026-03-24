---
title: "Monitoring Your Team in Real-Time"
summary: "Operational guide for Supervisors to use real-time dashboards for queue monitoring and agent management."
audience: [supervisor-qa]
product-area: [reporting, platform]
doc-type: how-to
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Monitoring Your Team in Real-Time

As a Supervisor (Sam), your primary tool for managing daily operations is the **Real-time Dashboard**. This guide covers how to assess queue health, monitor live conversations, and manage your team's availability.

## 1. Assessing Queue Health
Use the **Summary Dashboard** to get an instant snapshot of your contact center's performance.

### Key Metrics to Watch:
- **Service Level (SL%):** Ensure your queues are meeting targets (e.g., 80/20). Note that this updates every 5 minutes.
- **Oldest in Queue:** Identify customers who have been waiting the longest.
- **Average Wait Time:** Monitor trends to decide if you need to move agents between skills.

### How to Filter:
1. Select your **Team Name** from the top dropdown.
2. Select the specific **Queues** you wish to monitor.
3. The panels will update automatically to show data only for your selected scope.

## 2. Monitoring Active Conversations
Navigate to the **Ongoing Conversations Detail** dashboard to see what is happening *right now*.

### What you can see:
- **Active Since:** How long the agent has been talking to this customer.
- **Channel:** Whether the conversation is via WhatsApp, Voice, or Webchat.
- **Hold Status:** Identify conversations that have been on hold for an extended period.

### Supervisor Interventions:
- **Silent Monitoring:** Click the **Eye icon** to listen or read along without the customer knowing.
- **Whisper Coaching:** Use the **Yellow Whisper Tab** to send tips to the agent.
- **Barge-in:** If an interaction is going poorly, click **Barge-in** to join the conversation and speak directly to the customer.

## 3. Managing Agent Availability
The **Available Agents Detail** dashboard allows you to manage your team's workforce state in real-time.

### Taking Action:
If an agent has been in a "Not Ready" state for too long or forgot to log out:
1. Locate the agent in the list.
2. Click the **Change State** dropdown.
3. Select **Ready** to put them back into the queue, or **Log Out** to end their session.

## 4. Proactive KPI Alerts
The system monitors your configured thresholds. If a KPI (like Wait Time) exceeds a limit, you will receive a **Real-Time Performance Alert**. 
- Review these alerts in the **Alerts Tab** to identify conversations requiring immediate attention.

---

### Important Notes:
- **Refresh Rate:** Detailed dashboards refresh every 10 seconds.
- **Team Scope:** You will only see data for agents and queues assigned to your specific team in Keycloak.
- **Persistence:** Your dashboard filters (Team/Queue) are saved in your browser cache and will remain active even if you navigate away.

*Next Step: Learn how to analyze long-term trends in the [Historical Reporting Guide](../../How-to_Guides/Supervisor_and_QA_Lead/Historical-Reports-Reference.md).*
