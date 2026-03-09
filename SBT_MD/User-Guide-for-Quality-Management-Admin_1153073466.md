# CX Knowledgebase : User Guide for Quality Management Admin

As a **QM Admin** , you can configure how performance alerts are delivered to Quality Managers. This includes setting:

  * **Real-time notifications** for individual reviews.

  * **Scheduled bulk summaries** at defined intervals.




These settings are managed in the **QM Configuration tab**. This guide provides step-by-step instructions for setting up notification thresholds and delivery preferences.

### Login Screen

Users provisioned in [IAM](/wiki/pages/createpage.action?spaceKey=SBT&title=Security%20and%20User%20Permissions&linkCreation=true&fromPageId=1153073466) with the required permissions can authenticate using their credentials. The 'Remember Me' feature enables persistent login cookies for returning users

![1 \(1\).png](attachments/1153073466/1155334625.png?width=865)

## 1\. Defining the Evaluation Score Threshold

Configure the minimum acceptable evaluation score to trigger automatic notifications to quality managers when thresholds aren't met.

**To set the threshold:**

  1. Navigate to the **Configuration** section within the Quality Management module.

  2. Locate the **Define Threshold (%)** field.

  3. Specify the minimum acceptable score percentage. For example, a value of "40" means any evaluation scoring less than 40% will be flagged.

  4. This value is adjustable to accommodate changes in quality assurance policies.




![image-20250623-122620.png](attachments/1153073466/1155826053.png?width=678)

## 2\. Configuring Notification Type

The system lets quality managers set notification rules for low-scoring evaluations and customize alerts to match team workflows.

### 2.1. Notification Type

  * **Individual:** This option sends a separate notification for each evaluation that scores below the defined threshold. When a quality manager clicks on an individual notification, they will be taken directly to the specific conversation in question for immediate review. This is ideal for teams that require real-time, granular oversight.

  * **Bulk:** This option consolidates all low-scoring evaluation notifications into a single, summary alert. Clicking on this bulk notification will direct the quality manager to a list of all the reviews that did not meet the threshold within a specified time frame. This method is useful for managers who prefer to review quality issues in batches, preventing a constant stream of individual alerts.




**To select a notification type:**

  1. In the Configuration screen, find the **Notification Type** section.

  2. Choose either **Bulk** or **Individual** by selecting the corresponding radio button.




![image-20250623-122633.png](attachments/1153073466/1155105181.png?width=678)

### 2.2. Bulk Notification Interval 

When Bulk notifications are enabled, this setting specifies the minimum duration (in minutes) for aggregating low-scoring evaluations before notification delivery, reducing alert frequency through consolidation.

**To set the bulk notification interval:**

  1. Ensure that **Bulk** is selected as the Notification Type.

  2. In the **Min time for bulk notifications interval (mins)** field, enter the desired time in minutes. For instance, entering "1" means the system will gather all low-scoring reviews within a 1-minute interval and send them in a single notification.

  3. Adjust this time based on the call/chat volume and the desired frequency of summary alerts for quality managers.




![image-20250623-122529.png](attachments/1153073466/1155334615.png?width=678)
