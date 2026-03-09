# CX Knowledgebase : FAQs and Troubleshooting

![](images/icons/grey_arrow_down.png)Who should use the Google Play Store channel in Expertflow CX?

This channel is intended for contact center agents and supervisors who handle customer feedback on your Android app’s Google Play Store listing. Administrators are responsible for completing the onboarding and connector configuration before agents can start using it.

![](images/icons/grey_arrow_down.png)What types of messages are supported from Google Play Store?

The integration supports public app reviews and star ratings submitted on your app’s Google Play Store listing. Each new review is treated as an incoming media request and routed to an available agent based on your routing rules.

![](images/icons/grey_arrow_down.png)Can agents send private replies to customers?

No. Google Play reviews and developer or agent replies are public by design. The Google Play Store channel does not support private or direct messages. All responses appear publicly under the customer’s review on the Play Store.

![](images/icons/grey_arrow_down.png)Can agents edit or delete a customer’s review from Expertflow CX?

No. Agents can only send public replies to reviews. Editing or deleting the original customer review is not supported and is controlled entirely by Google Play.

![](images/icons/grey_arrow_down.png)What happens if a customer updates their review on Google Play Store?

If the same user updates their review for the same app, the update appears in the same conversation thread in Conversation View. Agents can see the updated review text and rating, along with the historical context in the review thread.

![](images/icons/grey_arrow_down.png)What information about the review can an agent see in Conversation View?

Within a Google Play Store review conversation, agents can see the app name and app logo, review text and star rating, top four reviews with reviewer name, star rating, review time, and any existing reply in threaded view, and the full review thread or history in the View Full Post panel.

![](images/icons/grey_arrow_down.png)How does routing work for Google Play Store reviews?

Each new review appears as a new incoming media request in Expertflow CX. It is then passed to the routing engine using your configured rules, such as skills, queues, or priorities, assigned to an available agent in the relevant queue, and handled as a normal conversation session in Conversation View.

![](images/icons/grey_arrow_down.png)Can multiple agents reply to the same review?

A single review is handled as one conversation session at a time. When an agent accepts the session, they own the conversation while it is active. If re-routed or reassigned, another agent may then respond, but the entire exchange still appears in the same review thread.

![](images/icons/grey_arrow_down.png)Are file attachments or multimedia replies supported?

No. Currently, replies to Google Play Store reviews from Expertflow CX support text only. Multimedia attachments such as images or videos are not supported for this channel.

![](images/icons/grey_arrow_down.png)How can I analyze Google Play Store review handling in Expertflow CX?

Google Play Store review sessions are included in the standard Channel Session Detail report. Each row in this report represents one channel session, including Google Play Store review conversations.

[Channel Session Detail](Channel-Session-Detail_2527421.html)

![](images/icons/grey_arrow_down.png)Why can’t I see Google Play Store as a channel in Agent Desk?

Check the following possible causes.

  * Onboarding not completed. Ensure that Google Play Store onboarding is completed as per the onboarding guide.

[Google Play Store Onboarding Guide](Onboarding-Guide_1511653389.html)

  * Connector not configured or not active. Verify that the Google Play Store connector is configured and activated in Unified Admin so the channel becomes available in Agent Desk and Conversation View. [Google Play Store Configurational Guide](Configurational-Guide_1658126350.html)

  * Permissions or roles. Confirm that the agent’s role has access to the Google Play Store channel.




![](images/icons/grey_arrow_down.png)Why is my reply not visible on the Google Play Store listing?

Possible reasons include propagation delay, policy or moderation, or use of an incorrect channel.

  * Propagation delay. It can take some time for Google Play to display new replies publicly.

  * Policy or moderation. Replies are subject to Google Play policies and may be moderated or blocked by Google.

  * Incorrect channel. Confirm that the reply was sent from a conversation where the channel is Google Play Store, not another channel.




![](images/icons/grey_arrow_down.png)Troubleshooting: I don’t receive any new reviews in Expertflow CX

Check the following possible causes.

  * Connector and onboarding. Confirm that onboarding is complete and the Play Store connector is configured and active.

  * Correct app configuration. Verify that the connector is linked to the correct Google Play app.

  * No new reviews in the store. Ensure that there are new reviews being posted on the app’s Play Store listing.

  * System health or logs. Ask your administrator to review connector logs or monitoring dashboards if the issue persists.



