# CX Knowledgebase : Understanding the YouTube Data API v3 Quota System

The **YouTube Data API v3** offers powerful features, such as uploading videos, retrieving channel statistics, managing playlists, and more. To ensure fair usage and system stability, Google enforces a **quota system** based on **units**.  
  
* * *

### Daily Quota

  * **Default Limit:**  
Every Google Cloud project is granted a **default daily quota of 10,000 units** for YouTube Data API v3 usage.




* * *

### Quota Costs per Operation

Each API request consumes a specific number of quota units:

Operation| Quota Cost (Units)  
---|---  
**Search Query**|  100 units  
**Video Upload**|  1,600 units  
**Fetching Video or Comment Details**|  1 unit  
**Comment Insert/Delete/Reply**|  ~50–100 units  
**List Playlists/Videos/Comments**|  1 unit  
  
So even seemingly light actions like loading comment threads across multiple videos can consume thousands of units if done in bulk.

* * *

### Cost Considerations

  * **Quota Exhaustion:**  
Once the daily quota is used up, your application will receive `403 quotaExceeded` errors for the rest of the day.

  * **No Charge for More Quota:**  
Google does **not charge** for quota increases. However, approval is based on the **merits and compliance** of your application.

  * **Quotas Are Per Project:**  
Quota is tied to your Google Cloud project—not your app or account—so be sure you're requesting increases for the correct project.




* * *

## Requesting a YouTube API Quota Increase

You can request more quota by submitting a formal request to Google.

* * *

### Option 1: Using the Quota Dashboard (Recommended)

#### Step 1: Go to Google Cloud Console

  * Open: <https://console.cloud.google.com>

  * Select the appropriate project.




#### Step 2: Navigate to Quotas

`IAM & Admin > Quotas `

or directly: <https://console.cloud.google.com/iam-admin/quotas>

#### Step 3: Filter for YouTube Data API v3

  * In the **Service** filter box, type:

`YouTube Data API v3 `

  * Check the box beside **Queries per day** or other quotas you want to increase.




#### Step 4: Click "Edit Quotas"

  * A request form will appear.




#### Step 5: Fill Out the Quota Request Form

Provide:

  * **Contact Information**

  * **OAuth Client ID** (if asked)

  * A **description of your app**

  * **Why you need more quota** (include estimated usage and number of users)




#### Step 6: Submit the Request

  * Google will review your request and typically respond within 3–5 business days.




* * *

### Option 2: Using the Direct Quota Request Form

You can also use this official form:

[**YouTube API Project Quota Increase Form**](https://support.google.com/youtube/contact/yt_api_form?hl=en)

Fill in:

  * Project name

  * Project number (found in your GCP dashboard)

  * API name: `YouTube Data API v3`

  * Reason for the quota increase

  * Expected usage (requests/day)




* * *

### What actually happens when you exceed 10,000 quota units/day:

  1. **You have to apply for a quota increase** via a form (which you're filling out).

  2. Google reviews your request — often they’ll ask:

     * Why you need more quota

     * How your app works

     * If it’s public or private

     * If it’s monetized

  3. If approved, **you still won’t be charged** — **but** :

     * They expect you to comply with strict API policies.

     * They may require **OAuth verification** or **branding review**.

     * They might ask you to switch to a **commercial license** **if** you’re using it at scale for a product/business.




* * *

### Summary:

**Usage**| **Charged?**| **Notes**  
---|---|---  
< 10,000 units/day| ❌ No| Free  
> 10,000 units/day (with approval)| ❌ No| Still free if approved  
High-scale or monetized apps| ⚠️ Maybe| Might need commercial agreement or other terms  
  
* * *

### 🧠 Pro Tips

  * Keep your request **clear, specific, and honest**.

  * Make sure your **OAuth consent screen is verified** , especially if requesting large quotas.

  * Mention **data retention policies** , user control, and how your app respects YouTube policies.

  * If rejected, you can **improve your justification and reapply**.



