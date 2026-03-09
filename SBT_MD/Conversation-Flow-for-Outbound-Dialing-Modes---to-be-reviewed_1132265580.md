# CX Knowledgebase : Conversation Flow for Outbound Dialing Modes - to be reviewed

A **Conversation Flow** , built by sequencing nodes in the Conversation Studio, defines a controlled flow of interaction for both inbound and outbound communications. The following sections detail common outbound flows.  
  
> **Note on DNC Validation:** A critical step in any flow is DNC validation. This is typically configured as an early step (e.g., within the WAIT node) and involves checking if a contact profile in CX-Customers has a specific DNC label assigned that is relevant to the current campaign. See [DNC Lists](DNC-Lists_739147899.html)

## Conversation Flow for Power and Predictive Modes

This flow reserves resources before initiating multiple calls.

  1. **Outbound SEIZE Node:** Flow starts when an agent (or a fraction of their capacity) from a specified skill group is SEIZED, or a specific agent is reserved based on campaign strategy. The agent is seized for the _skill_ or as a _named individual_ , but not yet for a _specific conversation_.

  2. **Optional WAIT Node:** (DNC checks can be integrated here) Final conditional check before initiating calls. Examples: Confirm current time is within permitted calling hours; check if campaign status is "active"; verify contact does not have a "DNC" label.

  3. **INIT Node:** Initiates 'x' number of interaction sessions (e.g., voice calls). 'x' is determined by the Power or Predictive dialing logic.

  4. **Call Progress Analysis (CPA) - IVR/Chatbot:** An IVR (voice) or a chatbot (messaging) performs initial CPA. Detected Outcomes: Busy, answering machine, fax, no answer, live answer, customer requests opt-out.

  5. **Branching based on CPA Outcome:** Flow proceeds based on CPA result.

     * Answering Machine: Route to a voicebot to leave a message.

     * Busy/No Answer: Schedule re-attempt after a defined interval using flow logic.

     * **Customer requests opt-out:** Use the **Add Contact Label** node to assign the "DNC" label to the contact, preventing future outreach from relevant campaigns.

  6. **Customer Reached - ROUTING Node:** If a live customer is reached, a standard **ROUTING** node is triggered.

     * **Routing Logic:** Directs the connected call based on the initial seizure strategy and defined rules:

       * **Queue-based/Shared:** Routes to an available agent within the seized skill group/queue (e.g., longest idle, skill match).

       * **Direct Agent Routing/Personal Callback:** Routes directly to the specifically reserved agent if they were targeted in the SEIZE step.

       * **Mixed Routing:** May involve initial qualification (e.g., by an IVR) before directing to a specific agent or queue.

     * **Timeout Configuration:** Routing attempts can have a configurable timeout, triggering actions like transfer to an alternate queue/IVR or call abandonment.

  7. **Agent Assignment:** A seized agent is formally assigned to the connected call.

  8. **Optional Personalized Agent Greeting (IVR):** A pre-recorded audio file specific to the agent can be played to the customer via conference. The `.wav` file is stored with the agent's profile and played by an IVR.

  9. **Screen Pop:** Customer data is displayed on the agent's interface when the call is connected.




## Conversation Flow for Preview and Progressive Modes

This flow assigns an agent to a contact before initiating the interaction. (DNC checks are typically performed before routing to an agent).

  1. **ROUTING Node (Agent First):** (Contact pre-validated against DNC lists) A customer contact record (as a task) is routed to an agent.

     * **Routing Logic:** The system selects an agent based on defined strategies:

       * **Queue-based/Shared:** Assigns the task to the next available agent in a relevant queue.

       * **Direct Agent Routing/Personal Callback:** Assigns the task directly to a pre-determined specific agent (e.g., for a follow-up or dedicated account manager).

       * **Mixed Routing:** Could involve an initial system step before assignment to a specific agent or queue.

     * The selected agent is reserved for this interaction.

  2. **Screen Pop:** Customer data is displayed on the agent's interface.

  3. **Call Initiation (Mode Dependent):**

     * **Progressive Mode:** System automatically initiates CPA and dialing.

     * **Preview Mode:** Agent manually triggers CPA and dialing via an interface action (e.g., "Dial" button).

  4. **Call Progress Analysis (CPA):** Executed as in Power/Predictive modes.

  5. **Customer Reached & Connection:** Occurs when the dialed party answers.

  6. **Optional Personalized Agent Greeting (IVR):** As described in the Power/Predictive flow, step 8.



