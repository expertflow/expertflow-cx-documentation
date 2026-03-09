# CX Knowledgebase : CX Customer Widget Embedding Guide

This guide provides step-by-step instructions for embedding the Expertflow Live Chat Web Widget into a website. The widget can be integrated using **Google Tag Manager (GTM)** or by **directly embedding the script into the website’s HTML** , depending on your deployment preference and level of control.

**Audience:** Webmasters, developers, or administrators who want to add the chat widget to their site without modifying the site’s source code

### 1: Embedding via Google Tag Manager (GTM)

When using GTM, the widget can be embedded in the following ways:

  * **Using the official Tag Template (Recommended)**

  * **Importing the Template from GitHub** (if not available in the GTM Community Gallery)

  * **Embedding via a Custom HTML Tag**




### 2: Direct Website Embedding

Alternatively, the widget can be embedded by **directly adding the widget script to the website’s HTML** , within the `<head>` section.

For direct embedding, scroll down to this.   
<https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/2531378/CX+Customer+Widget+Embedding+Guide#2%3A-Embed-in-Website>

# 1: Embedding via Google Tag Manager (GTM)

#### Prerequisite

Before embedding the widget:

  * Ensure you have a **Google Tag Manager account** and **container** created.




Follow the official steps here: [Create a GTM Account and Container](https://support.google.com/tagmanager/answer/6103696?hl=en)

  * The **Expertflow Customer Widget** should already be **deployed and publicly accessible** on your CX server (e.g., `https://yourdomain.com/customer-widget`).




## Option 1: Emed via Tag Template _(Recommended)_

Use a custom tag template to set up Expertflow live chat on your website, connecting customers to the business for inbound, outbound, and self-service interactions.

### Expertflow Live Chat Template Installation

#### Installation

  1. Log in to GTM → Open your **Workspace**.

  2. In Google Tag Manager, click Workspace. Near the top of the window, find your container ID, formatted as GTM-XXXXXX. Click your container ID to launch the Install Tag Manager window.

  3. Copy and install the GTM container code on your website (inside the `<head>` tag).

  4. **Publish** Your container. For more information, [_click here_](https://developers.google.com/tag-platform/tag-manager/web).




#### Search Tag Template:

Once the GTM account and container are created and configured on your site.

  1. In GTM, navigate to **Templates → Tag Templates → Search Gallery**.

  2. Search “Expertflow” in the search bar, and this will filter the template from the Gallery.

  3. Click on theThe **Expertflow Live Chat** template and it will navigate to the Template Details Section.

![](attachments/2531378/1612873747.png?width=510)
  4. Click on the **Add to Workspace** button to install it on the Current Workspace.

![](attachments/2531378/1612873755.png?width=510)
  5. Read the third-party policies and click on the **Add** button.

  6. After adding to the workspace, the Tag Template will be visible in the templates section.

  7. Click on the template to open it in Template Editor. Navigate to the **Permissions** section and replace the [Hostname] with the Init-Widget Url (FQDN).

  8. Click on the Refresh and then the Save button to save the Template.




Make sure the Template Editor's Console is error-free before saving the Template.

**The Expertflow Live Chat** template is added to your current workspace.

## Option 2: **Importing the Template from GitHub**

You can also import the Expertflow Live Chat template from the Github Repository, in case you don’t find it in the Community Gallery of Tag Manager.

### Import from GitHub Repository

  1. Download the Tag template source code from [_here_](https://github.com/expertflow/expertflow-cim-tag-template/tree/develop).

  2. Extract files in a folder and make sure the folder contains the **template.tpl** file.

  3. Open Google Tag Manager, navigate to the templates section from the sidebar, and click on the **New** button as shown in the figure below.

  4. Template Editor will open up, click on the three-dot icon at the top right corner to select the **import** Option from the dropdown as shown in the figure below.

  5. Select the template.tpl file from the source code folder to open it in the Template Editor.

  6. Click on the template to open it in Template Editor. Navigate to the **Permissions** section and replace the [Hostname] with the Init-Widget Url (FQDN).

  7. Click on the Refresh and then the Save button to save the Template.

![](attachments/2531378/1612873761.png?width=442)



Make sure the Template Editor's Console is error-free before saving the Template.

**The Expertflow Live Chat** The template is added to your current workspace.

### Create a Tag and a Trigger for the Template

  1. Navigate to the **Tag** section and click on the **New** button to add a new Tag.

  2. Name the tag and add Tag Configuration.

  3. Choose the Tag Type => Expertflow Live Chat template under the Custom headings.

  4. Fill in the required fields with valid configurations.

  5. Once configurations are filled, the final step is to add the trigger to fire the tag on the page view.

  6. Finally, the Tag will look like this:

  7. Click on the **Save** button.




## Preview Before Publish

To enable preview and debug mode for the current workspace: 

  1. Click Preview in the top right of your workspace. 

  2. Enter your site's URL. 

  3. Click Connect. Your site opens in a new window and displays as Connected in the bottom right.

  4. Click back on the Tag Assistant tab and click Continue to access the debug interface.

  5. You can monitor fired tags in **Tag Assistant.**  





For more information regarding Preview and Debug Mode: [_Click Here_](https://support.google.com/tagmanager/answer/6107056)

Click**Submit** button to **Publish the Container** online. Refresh the target website to see the **Expertflow Live Chat** widget. 

![](plugins/servlet/confluence/placeholder/unknown-attachment)

# Embed Widget & Pushing Browser Information as CX Activity via GTM

### Prerequisite

Make sure you have already created the **Google Tag Manager** account and container. For details on how to create a Google Tag Manager account and container, follow the steps listed in [ _this_](https://support.google.com/tagmanager/answer/6103696?hl=en) guide.

Clone/Download this repository [_expertflow/GTM-Browser-CX-Activity_](https://github.com/expertflow/GTM-Browser-CX-Activity)

On Google Tag Manager's home page, click on the admin tab.

![](attachments/2531378/1612873767.png?width=680)

Click on the Import Container to import the workspace.json file downloaded from the above repository.

![](attachments/2531378/1612873773.png?width=523)

Select the workspace.json file from the locally cloned repository, Also, one can decide whether to override or merge the importing container. Recommended to use merge option to avoid any existing tag lost. 

![](attachments/2531378/1612873779.png?width=476)

Once selected, it will list all the imported tags and triggers in the preview mode.

![](attachments/2531378/1612873785.png?width=476)

Once the import is complete, navigate to the tag section and click on the cx-activity tag, and update the FQDN as per the preferred EFCX Server Deployment.

![](attachments/2531378/1612873791.png?width=462)

Once all FQDNs are updated in all tags, save the changes.

## Preview Before Publish

To enable preview and debug mode for the current workspace: 

  1. Click Preview in the top right of your workspace. 

  2. Enter your site's URL. 

  3. Click Connect. Your site opens in a new window and displays as Connected in the bottom right.

  4. Click back on the Tag Assistant tab and click Continue to access the debug interface.

  5. You can monitor fired tags in **Tag Assistant.**




For more information regarding Preview and Debug Mode: [_Click Here_](https://support.google.com/tagmanager/answer/6107056)

Click**Submit** button to **Publish the Container** online. Refresh the target website to see the **Expertflow Live Chat** widget. 

![](attachments/2531378/1612873797.png?width=251)

**Note:** If using the above-provided repository to embed and push the cx activity, then the web widget deployment tag is also part of this container, so no need to import it separately.

## Option 3: Embed via Script in Google Tag Manager

### Use this if you prefer manual control or want to copy-paste the code directly.

  1. Go to **Tags → New → Custom HTML**.

  2. Paste this script and edit the values accordingly:
[code] <!-- CIM Script Tags -->
         <script type="text/javascript">
               var __cim = __cim || {};
               __cim.customerWidgetUrl = "<Public FQDN>/customer-widget"; //Url where Customer Widget is Deployed 
               __cim.widgetIdentifier = "web"; //Widget Identifier (Case Sensitive)
               __cim.serviceIdentifier = "+921218"; //Service Identifier
               (function () {
                        var __cimScript = document.createElement("script"),
                        __cimScriptTag = document.getElementsByTagName("script")[0];
                        __cimScript.src = __cim.customerWidgetUrl + "/widget-assets/widget/init_widget.js";
                        __cimScript.charset = "UTF-8";
                        __cimScriptTag.parentNode.insertBefore(__cimScript, __cimScriptTag);
                })();
         </script>
         <!-- End CIM Script Tags -->
[/code]

Change the configurations in the script before adding the tag.

     * **Customer Widget URL** is the IP or FQDN of the server where the Customer Widget is hosted.

     * The **widget Identifier** is the web identifier for CIM chat. Make sure the widget identifier is the same as used in Unified Admin and it's case-sensitive.

     * **Service Identifier** is the service identifier for CIM chat.

**You can also embed this script directly into the head tags of your origin site html file.**

  3. Add a trigger to fire on **All Pages (Page View)**.

  4. Click on the Save and then Submit button to publish the container online.




The final view of the tag looks like this:

![](attachments/2531378/1612873803.png?width=408)

Once the custom HTML tag is created and saved, follow the same [_installation_](https://expertflow-docs.atlassian.net/wiki/pages/resumedraft.action?draftId=2531544#CustomerWidgetDeployment-Installation) The step given above shows the widget on the target website.

# Enabling Customer Identification via Google Analytics

To identify returning customers, the widget can use the **Google Analytics Unique ID (GA _gid)** stored in the browser cookie.

### How It Works

  * When a visitor lands on your site, Google Analytics assigns a unique **_gid** or **_ga** value.

  * The Expertflow widget automatically reads this value and uses it as the **Customer Channel Identifier**.

  * This allows the system to recognize returning visitors and maintain chat continuity.




**Setting Up Google Analytics**

You can integrate Google Analytics in **two ways** , depending on your setup preference:

## Option 1: Direct Embedding GA Tracking Script

  1. **Universal Analytics**

     1. Assuming that you already have a Google Analytics **Account** , **Property** and **View** Created, if not [_Click Here_](https://cxl.com/blog/google-analytics-setup-101/). 

     2. Navigate to Admin > Account > Property Section and click on the Tracking Code Option to get the Tracking Script to embed into the website

![](attachments/2531378/1612873809.png?width=578)
     3. Once Tracking Code is embedded into your site, GA Unique ID is now available on that browser's cookies.

![](attachments/2531378/1612873815.png?width=442)
     4. Now customer widget can automatically fetch the **_gid** as a Customer Channel Identifier.

  2. **Google Analytics 4 (GA4)**

     1. Assuming that you already have a Google Analytics account **Account** , **Property** and **Data Streams** Created, if not [_Click Here_](https://www.datadrivenu.com/understanding-data-streams-google-analytics-4/). 

     2. Navigate to Admin > Account > Property Section > Data Streams and click on the Data Stream Option to get the **Measurement ID** to embed into the website or GTM Tag.

![](attachments/2531378/1612873821.png?width=1280)
     3. Once Tracking Code is embedded into your site, GA Unique ID is now available on that browser's cookies.

![](plugins/servlet/confluence/placeholder/unknown-attachment)
     4. Now customer widget can automatically fetch the **_gid** as a Customer Channel Identifier.




## Option 2: Add Google Analytics via Google Tag Manager (Recommended)

  1. **Universal Analytics**

     1. Assuming that you already have a Google Analytics account **Account** , **Property,** **View,** and GTM account created, if not [_Click Here_](https://cxl.com/blog/google-analytics-setup-101/).

     2. Navigate to Admin > Account > Property Section and click on the Tracking Code Option to get the Tracking ID from the script to use in GTM.

![](attachments/2531378/1612873827.png?width=578)
     3. Now open the GTM account and create a new variable, **name** it, add **variable type** as Google Analytics settings and add that **Tracking ID** Copy from the GA tracking script, then click the Save button to save the variable.

![](attachments/2531378/1612873833.png?width=340)
     4. Create **New** Tag, **Name** The tag, select **Tag Type** "Google Analytics: Universal Analytics", select **Track Type** as Page View, select the GA variable previously created in **Google Analytics Settings** and fire the tag on **Page View** Trigger.

![](attachments/2531378/1612873839.png?width=476)
     5. Click the Save button and publish the Container of GTM to sync GTM with your website.

     6. Once the container is synced into your site, the GA Unique ID is now available on that browser's cookies.

![](attachments/2531378/1612873815.png?width=442)
     7. Now customer widget can automatically fetch the **_gid** as a Customer Channel Identifier.

  2. **Google Analytics (GA4)**

     1. Assuming that you already have a Google Analytics **Account** , **Property,** **Data Streams,** and GTM account created, if not [_Click Here_](https://searchengineland.com/how-to-set-up-google-analytics-4-using-google-tag-manager-374584#:~:text=Step%201%3A%20To%20start%20setting,to%20enter%20your%20Measurement%20ID.).

     2. Navigate to Admin > Account > Property Section and click on the Data Streams Option to get the Measurement ID from the script to use in GTM.

![](attachments/2531378/1612873856.png?width=1280)
     3. Create **New** Tag, **Name** the tag, select **Tag Type** "Google Analytics: GA4 Configuration", add Measurement Id from the GA4 account and also check the check box of page view event and fire the tag on **Page View** Trigger.

![](attachments/2531378/1612873862.png?width=564)
     4. Final view of the tag would look like this:

![](attachments/2531378/1612873868.png?width=326)
     5. Click the Save button and publish the Container of GTM to sync GTM with your website.

     6. Once the container is synced into your site, the GA Unique ID is now available on that browser's cookies.

![](attachments/2531378/1612873815.png?width=442)
     7. Now customer widget can automatically fetch the **_gid** as a Customer Channel Identifier.




Once the GTM container is published and synced, GA cookies will be available on your site, and the widget will automatically use them for customer identification.Once the GTM container is published and synced, GA cookies will be available on your site, and the widget will automatically use them for customer identification.

# 2: Direct Website Embedding

The Web Widget can be embedded in any third-party website to enable web widget capabilities.

### Prerequisites

Make sure you have the following things available before embedding:

  1. Configured Web Widget [Click here](https://docs.expertflow.com/cx/4.7/unified-admin-guide#id-\(4.7\)UnifiedAdminGuide-OtherConfigurations).

  2. Any website that serves as a host, where you can embed the widget.

  3. Widget Embedding Script with all the required credentials explained below.




#### Installation

Follow these steps to embed the web widget on your host site:

  1. Once the web widget is properly configured. Update the configuration details as per the table given below.

  2. Once the configuration is updated, add that script at the top in the Head tag <head> of the HTML Code of the target web application script provided below. 




### Script

  1. Update the following configuration in the script.




**Config Parameter**| **Description**  
---|---  
customerWidgetUrl| IP or FQDN of the server where the Customer Widget is hosted.  
widgetIdentifier| The widget identifier of the web widget instance is defined in the Unified Admin.   
serviceIdentifier| This is the service identifier of the web channel defined in the Unified Admin.  
  
  2. Add the script in the head section of the target web application.



[code] 
    <!-- CIM Script Tags -->
    <script type="text/javascript">
      var __cim = __cim || {};
      __cim.customerWidgetUrl = "https://[HostName]/customer-widget"; //Customer Widget Url 
      __cim.widgetIdentifier = "web"; //Widget Identifier
      __cim.serviceIdentifier = "+921218"; //Service Identifier
    
      (function () {
        var __cimScript = document.createElement("script"),
            __cimScriptTag = document.getElementsByTagName("script")[0];
        __cimScript.src = __cim.customerWidgetUrl + "/widget-assets/widget/init_widget.js";
        __cimScript.charset = "UTF-8";
        __cimScriptTag.parentNode.insertBefore(__cimScript, __cimScriptTag);
      })();
    </script>
    <!-- End CIM Script Tags -->
    
[/code]

After embedding the script and deploying, the widget will be visible on the website. 

## 
