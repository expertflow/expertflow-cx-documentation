# CX Knowledgebase : Channel Session

A Channel Session represents customer's presence on the respective Channel. It maintains the flow of the customer communication with CX. A Channel Session has a start and end time. A [Conversation](Conversation_93192236.html) may have one or more active Channel Sessions at a time. 

A Channel Session is a container of all customer related [activities](Messages%2C-Events%2C-and-Activities_2528021.html) happening on a [media channel](Omnichannel-Engagement_2529366.html). CX-core creates a channel session upon receiving the first event for the respective [media channel](Omnichannel-Engagement_2529366.html). A Channel Session remains active as long as actors publish events. A Channel Session is expired when there is no activity from actors for the configured inactivity timeout.

A Channel Session has Channel Data attributes. It's a set of key-value pairs associated to a channel session. For example, 

  1. For a web chat session, the web user’s browser info (Chrome, Safari), locale, browser-id, and any pre-chat form data are the channel data attributes. During an active Channel Session, Channel Data attributes may be modified via an API. 

  2. For a call, all call variables are set as Channel Data attributes.




For more details, see [channelSession](channelSession_2527365.html) .
