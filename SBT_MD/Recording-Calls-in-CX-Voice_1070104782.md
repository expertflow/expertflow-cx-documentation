# CX Knowledgebase : Recording Calls in CX Voice

The recording mechanism for CX Voice is based on a set of scripts and even hooks that trigger for starting/stopping/pausing/resume recordings based on certain events.

## Dialplan

The **user_record** dialplan in CX Voice must have the last section configured as below:

![](attachments/1070104782/1070334195?width=800)

It set certain variables required for basic recording configuration.

## Events and Scripts

The EFSwitch events to note are:

### CHANNEL_BRIDGE

This event occurs during the following times:

  * Agent answers inbound call

  * Agent answers consult call

  * Agent answers direct transferred call

  * Customer answers outbound call

  * Consult transfer call between A2 and C1 is bridged




This even triggers a script that will check the data from the event and decide which type of call this is i.e. manual outbound, consult, direct transfer etc. Based on this, a filename will be created with the format dialogId**:** agentExtension**:** ani**:** legStartTime and recording started.

### CHANNEL_UNBRIDGE

This event occurs during the following times:

  * A call ends

  * A customer call is transferred by an agent to another agent or queue

  * Consult transfer occurs




This even triggers a script that stops any ongoing recordings.

### CHANNEL_STATE

This event is triggered on hold and resume events, and call recordings are held and resumed accordingly.

## Barge/Consult Conference

When a supervisor barges into a call, or a consult conference is created, or a member is added to any conference, the **CHANNEL_BRIDGE** event above is not triggered. Therefore recordings are started in the barge and consult conference scripts respectively, rather than the hook scripts.

## Issues

  * Due to the manual recording pause/resume for hold/resume events, there will be at most one second of music during some calls.



