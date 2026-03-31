---
title: "Google Play Store FAQs and Troubleshooting"
summary: "Frequently asked questions and troubleshooting steps for the Google Play Store integration in Expertflow CX."
audience: [admin, supervisor, agent]
product-area: [channels, google-play]
doc-type: reference
difficulty: beginner
last-updated: 2026-03-13
---

# Google Play Store FAQs and Troubleshooting

## 1. Frequently Asked Questions (FAQs)

**Q: Can agents send private replies to customers on the Play Store?**
**A:** No. Google Play Store reviews and developer replies are public. The integration only supports public responses.

**Q: Can I edit or delete a customer’s review from the Expertflow Agent Desk?**
**A:** No. You can only post replies. Review management (editing/deleting) is controlled entirely by Google.

**Q: What happens if a customer updates their review?**
**A:** The update appears in the same conversation thread. Agents can see the updated review text and rating.

**Q: Are multimedia attachments (images/videos) supported in replies?**
**A:** No. Google Play Store review replies are text-only.

**Q: How can I track how many reviews we have replied to?**
**A:** Use the **Channel Session Detail** report. Each Google Play Store review conversation is recorded as a session.

## 2. Troubleshooting Guide

### Why can't I see Google Play Store as a channel?
-   Verify **onboarding** is complete (Google Cloud and Play Console).
-   Check if the **connector** is active in Unified Admin.
-   Ensure the agent has the correct **role permissions**.

### Why is my reply not visible on the Play Store?
-   **Propagation Delay:** It can take several minutes to an hour for Google to display new replies.
-   **Policy Violation:** Google may moderate or block replies that violate their content policies.
-   **Authentication Error:** Check connector logs in the Unified Admin for `401` or `403` errors.

### Why are we not receiving new reviews in Expertflow CX?
-   Ensure the **Package Name** in the connector matches your app's bundle ID exactly.
-   Check the **polling interval** in the connector configuration.
-   Verify that the Service Account has the **View app information** permission.
-   If the issue persists, check the system logs for connection errors with the Google API.
