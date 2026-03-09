# CX Knowledgebase : License Consumption Status

This feature allows business administrators to view license details, monitor expiry statuses, and receive proactive warnings for licenses linked to a master key.   
The License Info page now also includes [License product statuses](https://expertflow-docs.atlassian.net/wiki/x/SADDOg) and configurable expiry warnings to help admins manage renewals.

## Feature Details

### Master Key and Product Association

  * A **master key** can be associated with multiple products purchased from the EF shop.

  * Each product’s license details, including expiry status and warnings, are displayed separately under the master key.




### Accessing the License Info Page

  1. Navigate to **Unified Admin → License Info**.

  2. The system automatically displays the uploaded master key and its associated products.




### Displayed Information

Field| Description| Example  
---|---|---  
**Master License Key**|  The uploaded master key.| `MK-XXXX-XXXX-XXXX`  
**Product Name**|  Name of the purchased product.| "EF Analytics Pro"  
**Status**|  Current Order status for your product subscription. See list of possible [License Status](https://expertflow-docs.atlassian.net/wiki/x/SADDOg)| `ACTIVE`  
**Expiry Date**|  Date when the license Subscription expires. | `2024-12-31`  
**License Type**| `Concurrent Users` or `Activities`.| `Concurrent Users`  
**Purchased Licenses**|  Total licenses purchased.| `100`  
**Consumed Licenses**|  Licenses in use/activated.| `75`  
  
![Screenshot 2025-05-08 160651.png](attachments/985595918/1072431383.png?width=940)

### Expiry Warning Banner

  * A warning banner is displayed for licenses with an expiry date **within** the configured `LICENSE_EXPIRY_WARNING_DAYS` threshold.

  * **Warning Message**

 _"Your license will expire soon. Please renew to avoid any service interruption."_

  * **Conditions for Display**

    * Compares the expiry date against the current date. If the remaining days ≤ `LICENSE_EXPIRY_WARNING_DAYS`, the banner appears.

    * Example: If `LICENSE_EXPIRY_WARNING_DAYS = 60`, the banner shows when the license expires in ≤60 days.




## Configuration Settings

  * **ConfigMap Variable** : `LICENSE_EXPIRY_WARNING_DAYS` in unified-admin ConfigMap

    * **Purpose** : Defines the threshold (in days) for displaying the expiry warning.

    * **Validation** :

      * Minimum value: `30` days.

      * Maximum value: `180` days.

    * **Default** : If not configured, the system uses `30` days.

  * **Behavior** :

    * Admins can adjust this value via the platform’s configuration management.

    * Changes require a unified-admin ConfigMap and a Deployment restart to take effect.




## Feature Limitations and Operational Considerations

### 1\. Expiry Warning Precision

**Calendar-Day Calculation**

  * The expiry warning banner calculates days based on **calendar days** (not business days). Weekends and public holidays are **not excluded** from the count.

    * _Example_ : If a license expires in 30 calendar days and the warning threshold is set to 30 days, the banner will trigger immediately, even if weekends fall within that period.




### 2\. License Status Synchronization

**Manual Refresh Required for Status Updates**

  * License status changes (e.g., expiry, consumption updates) are **not displayed in real time**.

  * Users must **refresh the License Info page** to view the latest status.




### 3\. Configuration Management

**Configuration Update Restart Requirement**

  * Changes to the `LICENSE_EXPIRY_WARNING_DAYS` ConfigMap value require a **system restart** to take effect.

  * This applies to both increases and decreases in the threshold.




### 4\. Product Purchase and Activation Workflow

4.1 **Sequential Product Purchase Requirement**

  * Multiple product purchases linked to a single master key **cannot be purchased in a single transaction**. Each product must be procured individually via the EF shop.




**4.2 Agent Login Dependency for Activation Visibility**

  * Newly purchased products **do not appear on the dashboard** until an authorized agent logs into the product at least once; thereafter, license details will be displayed.




4.3 **Product-Specific Login Requirement (Excluding Testing Products)**

  * **Exception** : Testing products purchased from the EF shop are displayed immediately without agent login.

  * **All Other Products** : License details (e.g., consumption, expiry) are visible **only after an agent’s initial login** to the product.




### 5\. Order Status Reversion Impact

**Subscription Renewal Requirement**

  * If an order’s status is reverted from any state (e.g., `suspended`, `pending`) back to `completed`, the customer must **resubscribe to the subscription** via the EF shop to reactivate the license, or the Admin has to manually reactivate the subscription. Here is the [guide](https://expertflow-docs.atlassian.net/wiki/x/8QDkOg).



