# CX Knowledgebase : Segregating Facebook DM vs. Social Media Message in Channel Sessions

### Objective  
  
The objective of this task is to implement a mechanism to segregate Facebook Direct Messages (DM) from other Social Media (SM) interactions during channel session creation. This differentiation will aid in customizing handling processes across different components based on the message type.

### Description

In the current setup, we need to pass additional data within the `Header` of the `CimMessage` object. Specifically, the `additionalAttributes` should be populated under `channelData` in the `MessageHeader` to indicate the type of message. This enhancement will enable us to identify whether a message is a Facebook DM or an SM message right from the point of session creation.

#### Data Requirements

  * **Message Types:**

    * **DM:** Indicates that the message is a Facebook Direct Message.

    * **SM:** Indicates that the message is a Social Media interaction other than DM.

  * **Attribute Details:**

    * **KEY:** `MESSAGE_TYPE`

    * **VALUE:** Either `DM` (Direct Message) or `SM` (Social Media)

    * **TYPE:** `String100` \- a data type that supports up to 100 characters.




Based on the `MESSAGE_TYPE` attribute in `additionalAttributes`, we will differentiate the message type on various components and apply the required processes accordingly.

### Implementation Steps

  1. **Update MessageHeader:**  
Modify the `MessageHeader` of `CimMessage` to include the `additionalAttributes` key, containing the specified `KEY`, `VALUE`, and `TYPE` details.

  2. **Populate Additional Attributes:**  
Ensure that the `additionalAttributes` field under `channelData` is correctly populated with either "DM" or "SM" based on the message source. This classification should occur before the session creation process.

  3. **Component Configuration:**  
Adjust configurations across components to recognize and handle the `additionalAttributes` values. This may involve routing, filtering, or specific handling procedures for DMs versus SM messages.

  4. **Testing and Validation:**

     * Create test cases to verify that messages with "DM" and "SM" values are correctly identified and processed.

     * Validate that the segregation works across all relevant components, ensuring that each message type is handled as expected.




### Expected Outcome

With the implementation of this segregation mechanism, components will be able to distinguish between Facebook DMs and other social media messages. This will streamline message processing workflows, allowing for more tailored responses and actions based on the message type.
