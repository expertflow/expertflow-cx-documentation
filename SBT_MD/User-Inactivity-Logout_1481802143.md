# CX Knowledgebase : User Inactivity Logout

## Overview  
  
The User Inactivity Logout feature automatically logs out users from the Agent Desk after a specified period of inactivity has elapsed. This helps maintain security and ensures that unattended sessions do not remain active.

## Purpose

  * Enhance security by preventing unauthorized access due to unattended sessions.

  * Optimize resource usage by ensuring only active users remain logged in.




## Configuration

### Enabling Inactivity Timeout

  1. Navigate to **Admin** > **Agent Desk Settings**.

  2. Locate the **Inactivity Timeout** toggle and enable it.

  3. Specify the inactivity timeout duration (in seconds).

     * Allowed range: **30 seconds** to **3600 seconds**.

  4. Click **Save** to apply the changes.


![inactivity-setting.png](attachments/1481802143/1480622280.png?width=1326)

## User Experience

  * When enabled, any user on the Agent Desk will be automatically logged out after the specified period of inactivity.

  * Inactivity is defined as no keyboard, mouse, or microphone activity within the Agent Desk application.

  * At 80% of the configured timeout duration, a warning message will appear on the user's screen.

    * If the user interacts with the application (keyboard or mouse activity), the warning is dismissed and the session continues.

    * If there is no interaction after the warning, the user is logged out automatically.

  * If the user is logged out while having active conversations, those conversations will be rerouted to other available agents according to the controller's routing logic.


![inactivity-warning-prompt.png](attachments/1481802143/1480818801.png?width=1326)

## Exceptions

Inactivity is **not** counted in the following scenarios:

  * The Agent Desk window is minimized.

  * The browser tab is not in the foreground.

  * The user is handling an active voice or video call within the Agent Desk.




## Notes

  * Ensure that the inactivity timeout is set according to your organization's security policies.

  * Users should be informed about this feature to avoid unexpected logouts.



