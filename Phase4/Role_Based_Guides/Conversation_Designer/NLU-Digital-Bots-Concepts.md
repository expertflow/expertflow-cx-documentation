---
audience: [designer]
doc-type: explanation
difficulty: beginner
aliases: []
---

# NLU and Digital Bots for Voice

Expertflow CX enables the integration of speech-to-text (ASR) and Natural Language Understanding (NLU) engines into live voice conversations to provide automated assistance and intelligent routing.

## Concepts
During an ongoing phone call, the system can forward audio streams to an NLU engine (similar to Google Contact Center AI or Cisco Answer Services).

### Real-Time Pipeline
1. **ASR (Speech-to-Text)**: The system monitors the live audio stream.
2. **Silence Detection**: When the engine detects silence or the end of a sentence, it generates a "marker" (start/end time).
3. **Activity Trigger**: This marker information is treated as an activity that can be processed through the CX pipeline.
4. **Intelligent Response**: Based on the detected intent, the system can provide real-time guidance to the agent or trigger an automated voice response to the customer.

## Use Cases
- **Real-Time Coaching**: Suggesting scripts or articles to the agent based on what the customer is saying.
- **Automated Authentication**: Using NLU to capture account numbers or verify identity during the conversation.
- **Sentiment Monitoring**: Detecting customer frustration live on the call.
