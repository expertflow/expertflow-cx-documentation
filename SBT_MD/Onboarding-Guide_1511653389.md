# CX Knowledgebase : Onboarding Guide

This guide helps you connect your Google Play Store app with the Official Google Play Developer API (Android Publisher API. It is intended for administrators responsible for setting up Google Play Developer API. At a high level, the Google Play Store Connector uses the Google Play Developer API v3 and a Google Cloud service account to securely access your app’s reviews. Pull mode mechanism is used to pull the reviews every 60 seconds (configurable) via the Google Play Developer API. Ensure that the Service Account is linked to your Google Play Console account with appropriate permissions. 

## **Capabilities of the Official Google Play Developer API**

Google provides the Android Publisher API for Play Store apps. With this API, you can:

  * **Fetch Reviews** – retrieve all customer reviews for your app.

  * **Reply to Reviews** – respond to reviews programmatically.

  * **Check Ratings** – view rating details through the API.

  * **Automate Responses** – integrate automatic or assisted reply flows.




The API is **free to use** , as long as you have the required access to the app in Google Play Console.

### **API Endpoints (For Developers)**

#### **Fetch Reviews**
[code] 
    GET https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/reviews
[/code]

Example:
[code] 
    GET https://androidpublisher.googleapis.com/androidpublisher/v3/applications/com.example.myapp/reviews
[/code]

#### **Reply to a Review**
[code] 
    POST https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/reviews/{reviewId}:reply
[/code]

Example:
[code] 
    POST https://androidpublisher.googleapis.com/androidpublisher/v3/applications/com.example.myapp/reviews/gp:AOqpTOH...:reply
[/code]

**Request body:**
[code] 
    {
      "replyText": "Thank you for your feedback!"
    }
[/code]

## **Onboarding Steps**

To use the Android Publisher API, you must meet the following requirements.

### Prerequisites

  * Service Account Access to Google Playstore Application 

  * Application Name 




You can only reply to reviews for apps where you have appropriate permissions in the Play Console. 

### **1\. Google Cloud Project**

Your **Google Play Console** must be linked to a **Google Cloud Project**.  
This is where you will create the Service Account and manage API access.

### **2\. Create a Service Account**

Create a **Service Account** in Google Cloud and download a **JSON key** that the system will use to authenticate.

  1. To create the service account, the user should have admin access <https://console.cloud.google.com/>

  2. Once the app admin provides you access, you must be able to see the app here.

  3. Click on IAM & Admin


![console.png](attachments/1511653389/1692106766.png?width=800)

  4. Click **Service Account** in the left side bar

  5. Click **Create Service Account** and provide:

     1. A name (for example: `play-store-integration`)

     2. A description (optional)

     3. Assign the following role to the Service Account

        *  _“Service Account User”_


![ServiceAccount..png](attachments/1511653389/1690501184.png?width=800)![ServiceAcc.png](attachments/1511653389/1691942929.png?width=800)

  6. Open the Service Account you just created and click on link under email

     1. Go to the **Keys** tab.


![Link.png](attachments/1511653389/1692860444.png?width=800)

b. Click **Add Key → Create new key**

![keys.png](attachments/1511653389/1690796077.png?width=800)![popup.png](attachments/1511653389/1690927171.png?width=800)

  7. Now copy this service Account User_Name 

  8. Go to **Google Play Console → API Access (Only Admin or User have Developer access to app can provide this access)**

  9. ![image-20260129-105144.png](attachments/1511653389/1702068233.png?width=1264)

  10. Link this service account user to the Google Play Console in the Users and Permission Section.

     1. Assign at least the following permissions:

        1. **View app information**

        2. **Reply to reviews** (if you want our system to respond to reviews on your behalf)

  11. Utilize the JSON file (Step 6b), and this package name in the connector, and you can start testing. 




Without these permissions correctly assigned, the API will return errors such as `403 PERMISSION_DENIED`.

### **4\. Confirm the Package Name**

Once the access is granted, you will see your **package name** (also called the **bundle ID**) uniquely identifies your Android app.

Examples:

  * `com.whatsapp`

  * `com.expertflow.ccaas`

  * `pk.elitefinds.app`




You can confirm your package name:

  * In your **Android project** (`applicationId` in `build.gradle`).

  * In **Google Play Console** under your app’s details.




Note the exact package name for API requests and to connect to the correct app when following [Configurational Guide](Configurational-Guide_1658126350.html)
