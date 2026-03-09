# CX Knowledgebase : Personalized Agent Information in Customer widget

### Introduction

We've recently introduced a new feature to enhance the personalization of the customer widget. This feature allows for a dynamic display of the agent's name in the active chat view based on the configuration settings of the customer widget.

#### Configuration Variable

  * `USERNAME_ENABLED`: A boolean configuration variable was added in the `helm-values/ef-cx-custom-values.yaml` file and is used to control the display of the agent's name in the customer widget.


![image-20250123-192659.png](attachments/453967896/829554733.png?width=1105)

  * Upgrade the `helm-values/ef-cx-custom-values.yaml` file with the following commands to update the pods.

    * `helm upgrade --install --namespace expertflow --create-namespace ef-cx --debug --values helm-values/ef-cx-custom-values.yaml expertflow/cx --version <release-name>`




#### Behavior-Based on Configuration

  1. **When**`USERNAME_ENABLED` is `true` only the agent's username will be shown.

     * **Notification** : The username will appear in the customer widget notifications.

     * **Message Header** : The username will also be displayed in the message header of the active chat view.

  2. **When**`USERNAME_ENABLED` is `false` the widget will display the agent's full name if available. If both the first and last names are empty, a default string of `"AGENT"` will be shown.

     * **Notification** : The full name (or "AGENT" if the name parts are missing) will be displayed in the notification section.

     * **Message Header** : The first name and last name as full name (or `"AGENT"`) will appear in the message header of the active chat view.




#### Detailed Display Logic

  1. **Active Chat View - Notifications**

     * If `USERNAME_ENABLED` is `true`:

       * Display: `Username`

     * If `USERNAME_ENABLED` is `false`:

       * If `firstName` and `lastName` are available:

         * Display: `FirstName LastName`

       * If `firstName` or `lastName` is empty:

         * Display: available name like `firstName`

       * If `firstName` and `lastName` both are empty:

         * Display: `"AGENT"`

  2. **Active Chat View - Message Header**

     * If `USERNAME_ENABLED` is `true`:

       * Display: `Username`

     * If `USERNAME_ENABLED` is `false`:

       * If `firstName` and `lastName` are available:

         * Display: `FirstName LastName`

       * If `firstName` or `lastName` is empty:

         * Display: available string like `firstName` or `lastName`.

       * If `firstName` and `lastName` are empty:

         * Display: `"AGENT"`




#### Example Scenarios

  1. **Scenario 1** : `USERNAME_ENABLED` is `true`, `username` is `"john_doe"`, `firstName` is `"John"`, `lastName` is `"Doe"`

     * **Notification** : `"john_doe"`

     * **Message Header** : `"john_doe"`

  2. **Scenario 2** : `USERNAME_ENABLED` is `false`, `username` is `"john_doe"`, `firstName` is `"John"`, `lastName` is `"Doe"`

     * **Notification** : `"John Doe"`

     * **Message Header** : `"John Doe"`

  3. **Scenario 3** : `USERNAME_ENABLED` is `false`, `username` is `"john_doe"`, `firstName` is `"John"`, `lastName` is `""`

     * **Notification** : `"John"`

     * **Message Header** : `"John"`

  4. **Scenario 3** : `USERNAME_ENABLED` is `false`, `username` is `"john_doe"`, `firstName` is `""`, `lastName` is `"Doe"`

     * **Notification** : `"Doe"`

     * **Message Header** : `"Doe"`

  5. **Scenario 4**: `USERNAME_ENABLED` is `false`, `username` is `"john_doe"`, `firstName` is `""`, `lastName` is `""`

     * **Notification** : `"AGENT"`

     * **Message Header** : `"AGENT"`




This feature allows for a customizable and personalized experience for users interacting with the customer widget, based on the configMaps of the Customer Widget.
