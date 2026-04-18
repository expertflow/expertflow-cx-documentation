---
title: "Customer Widget Embedding Guide"
summary: "How-to guide for embedding the ExpertFlow CX live chat web widget into a website — covering Google Tag Manager (GTM) tag template, GitHub template import, custom HTML tag, and direct HTML script embedding methods."

product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["customer widget embedding", "GTM widget integration", "live chat widget embed", "widget script embedding", "Google Tag Manager CX widget", "CX widget HTML", "web widget deployment", "customerWidgetUrl", "widgetIdentifier", "serviceIdentifier"]
aliases: ["embed chat widget", "add widget to website", "CX web widget embed", "GTM live chat"]
last-updated: 2026-03-10
---

# Customer Widget Embedding Guide

This guide explains how to embed the ExpertFlow CX live chat web widget into any website. There are two main approaches: embedding via **Google Tag Manager (GTM)** or **directly adding the script to the site's HTML**. Choose based on whether you have GTM access or prefer direct code control.

## Prerequisites

- The ExpertFlow Customer Widget is deployed and publicly accessible (e.g., `https://yourdomain.com/customer-widget`).
- A Web Channel is configured in Unified Admin with a **Service Identifier** and **Widget Identifier**.
- For GTM methods: A Google Tag Manager account and container are set up on your site.

---

## Method 1: Google Tag Manager — Tag Template (Recommended)

### Install the GTM Container Code

1. Log in to Google Tag Manager and open your **Workspace**.
2. In your workspace, find your container ID (format: `GTM-XXXXXX`).
3. Click the container ID to open the **Install Tag Manager** window.
4. Copy the container snippet and add it to your website's `<head>` tag.
5. Publish your container.

### Search and Install the Expertflow Live Chat Template

1. In GTM, navigate to **Templates → Tag Templates → Search Gallery**.
2. Search for **"Expertflow"** to find the official template.
3. Click **Expertflow Live Chat** to open the Template Details page.
4. Click **Add to Workspace** and accept the third-party policy prompt.
5. After adding, click the template to open the **Template Editor**.
6. Go to the **Permissions** section and replace `[Hostname]` with your widget's FQDN (Init-Widget URL).
7. Click **Refresh** then **Save**. Confirm the Template Editor console shows no errors.

### Create a Tag and Trigger

1. Navigate to **Tags → New**.
2. Name the tag and click **Tag Configuration**.
3. Under **Custom**, select the **Expertflow Live Chat** tag type.
4. Fill in the required fields (widget URL, widget identifier, service identifier).
5. Add a **Trigger**: select **All Pages (Page View)** to fire on every page load.
6. Click **Save**, then click **Submit** to publish the container.
7. Refresh your target website to confirm the widget appears.

---

## Method 2: Google Tag Manager — Import from GitHub

Use this method if the Expertflow template is not available in the GTM Community Gallery.

1. Download the tag template source code from the [Expertflow GTM GitHub repository](https://github.com/expertflow/expertflow-cim-tag-template/tree/develop).
2. Extract the files and locate the **template.tpl** file.
3. In GTM, navigate to **Templates** and click **New**.
4. In the Template Editor, click the three-dot icon (top right) and select **Import**.
5. Select the `template.tpl` file.
6. In the Template Editor's **Permissions** section, replace `[Hostname]` with your widget FQDN.
7. Click **Refresh** then **Save**. Confirm no console errors.
8. Follow steps from Method 1 to create a Tag and Trigger using this imported template.

---

## Method 3: Google Tag Manager — Custom HTML Tag

Use this method for manual control without a template.

1. In GTM, navigate to **Tags → New → Custom HTML**.
2. Paste and configure the following script:

```html
<!-- CIM Script Tags -->
<script type="text/javascript">
  var __cim = __cim || {};
  __cim.customerWidgetUrl = "<Public FQDN>/customer-widget";
  __cim.widgetIdentifier = "web";
  __cim.serviceIdentifier = "+921218";
  (function () {
    var __cimScript = document.createElement("script"),
        __cimScriptTag = document.getElementsByTagName("script")[0];
    __cimScript.src = __cim.customerWidgetUrl + "/widget-assets/widget/init_widget.js";
    __cimScript.charset = "UTF-8";
    __cimScriptTag.parentNode.insertBefore(__cimScript, __cimScriptTag);
  })();
</script>
<!-- End CIM Script Tags -->
```

3. Update the three configuration values:

| Parameter | Description |
|---|---|
| `customerWidgetUrl` | FQDN of the server hosting the Customer Widget |
| `widgetIdentifier` | Widget identifier defined in Unified Admin (case-sensitive) |
| `serviceIdentifier` | Service identifier of the Web Channel defined in Unified Admin |

4. Add a **Trigger**: **All Pages (Page View)**.
5. Click **Save** then **Submit** to publish.

---

## Method 4: Direct HTML Embedding

Embed the widget without GTM by adding the script directly to your site's HTML source.

1. Add the following script inside the `<head>` tag of your HTML page:

```html
<!-- CIM Script Tags -->
<script type="text/javascript">
  var __cim = __cim || {};
  __cim.customerWidgetUrl = "https://[HostName]/customer-widget";
  __cim.widgetIdentifier = "web";
  __cim.serviceIdentifier = "+921218";

  (function () {
    var __cimScript = document.createElement("script"),
        __cimScriptTag = document.getElementsByTagName("script")[0];
    __cimScript.src = __cim.customerWidgetUrl + "/widget-assets/widget/init_widget.js";
    __cimScript.charset = "UTF-8";
    __cimScriptTag.parentNode.insertBefore(__cimScript, __cimScriptTag);
  })();
</script>
<!-- End CIM Script Tags -->
```

2. Replace the three parameter values with your environment's actual values (see table above).
3. Deploy your updated HTML. The widget will appear on the page after deployment.

---

## Customer Identification via Google Analytics

The widget can use the **Google Analytics Unique ID** stored in the browser cookie (`_gid` or `_ga`) to identify returning customers and maintain chat continuity.

Once a Google Analytics tag is configured on your site (via direct embedding or GTM), the widget automatically reads the GA cookie as the **Customer Channel Identifier** — no additional configuration is needed in the widget script.

---

## Related Articles

- [Configuring the Customer Widget](../Administrator/Configuring-the-Customer-Widget.md)
- [Customer Widget](../../Capabilities/Digital_Channels/Customer-Widget-Features-Capabilities.md)
- [Business Calendars](../../Capabilities/Digital_Channels/Business-Calendars.md)
- [Channel and Connector Setup](../Administrator/Channel-and-Connector-Setup.md)
