---
audience: [agent]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Accepting a Conversation

This guide covers how agents receive and manage incoming interactions on the Agent Desk, including auto-answer features and customer lookups.

## Auto-Answer
If enabled in Unified Admin, new incoming conversation requests are automatically accepted. You will not see a notification; the conversation will simply appear in your active list.
*Note: This is currently not available for Cisco Voice channels.*

## Answering Push-Based Requests
When a request is assigned to you:
1. An incoming notification appears with the customer's name (if known) or "Jane Doe".
2. **Color Coding**: 
   - **Green**: Identified customer match.
   - **Red**: Anonymous or "Jane Doe" profile.
3. Click **Accept** to open the interaction.

## Customer Profile Management
Upon acceptance, the right panel expands to show:
- **Customer Info**: Profile details and custom attributes.
- **Conversation Data**: Context passed from the channel (e.g., form data).
- **Active Sessions**: All channels the customer is currently using.

### Profile Linking
If the system matches the customer incorrectly or creates an anonymous profile for a known customer:
1. Click **Link Profile** in the Customer Profile pane.
2. Search for the correct customer in the list.
3. Click the **Link** icon.
4. (Optional) Check the box to add the current channel identity (e.g., phone number) to the linked profile for future recognition.

## Conversation History
The central view shows the full history of interactions with the customer across all channels, including past chats, voice call logs, recordings, and wrap-up notes. Use **Load More** to view older interactions.
