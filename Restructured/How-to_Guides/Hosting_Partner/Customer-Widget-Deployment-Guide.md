---
title: "Customer Widget Deployment Guide"
summary: "How-to guide for deploying the ExpertFlow Live Chat widget via Google Tag Manager — covering three deployment methods (GTM Tag Template, GitHub import, Custom HTML script), Google Analytics customer identification, and widget customization options."
audience: [hosting-partner]
product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["customer widget deployment CX", "ExpertFlow live chat GTM", "Google Tag Manager CX widget", "deploy chat widget CX", "web widget deployment CX", "GTM tag template CX", "customer widget script CX"]
aliases: ["CX widget deployment", "live chat widget setup CX", "web widget GTM CX"]
last-updated: 2026-03-10
---

# Customer Widget Deployment Guide

This guide covers deploying the ExpertFlow Live Chat widget on a website via **Google Tag Manager (GTM)**. Three deployment methods are available — choose the one that fits your setup.

## Prerequisites

- Google Tag Manager account and container created and installed on the target website. See [Google's guide](https://support.google.com/tagmanager/answer/6103696) for setup instructions.
- ExpertFlow CX deployed with a public FQDN.
- Widget Identifier and Service Identifier from Unified Admin.

---

## Method 1: GTM Tag Template (Community Gallery)

The easiest method — install directly from the GTM Template Gallery.

1. Log in to Google Tag Manager and open your workspace.
2. Click **Templates** in the left navigation, then **Search Gallery** under Tag Templates.
3. Search for **"Expertflow"** and select **Expertflow Live Chat**.
4. Click **Add to Workspace**, accept the third-party policies, and click **Add**.
5. Open the template in Template Editor. Navigate to **Permissions** and replace `[Hostname]` with your Init-Widget URL (your CX FQDN).
6. Click **Refresh** then **Save**. Confirm the console is error-free before saving.
7. Go to **Tags → New**, name the tag, and select **Expertflow Live Chat** as the Tag Type.
8. Fill in the required fields (Widget URL, Widget Identifier, Service Identifier).
9. Add a **Page View** trigger to fire the tag.
10. Click **Save**, then **Submit** to publish the container.

---

## Method 2: Import Template from GitHub

Use this if the template is not available in the Community Gallery.

1. Download the tag template source from the [expertflow-cim-tag-template](https://github.com/expertflow/expertflow-cim-tag-template/tree/develop) repository.
2. Extract the files — confirm the folder contains `template.tpl`.
3. In GTM, go to **Templates → New**.
4. Click the three-dot menu (top right) and select **Import**.
5. Select the `template.tpl` file from the extracted folder.
6. In Template Editor, go to **Permissions** and replace `[Hostname]` with your CX FQDN.
7. Click **Refresh** then **Save**. Confirm the console is error-free.
8. Create a Tag and Trigger following steps 7–10 from Method 1.

---

## Method 3: Custom HTML Script in GTM

Embed the widget using a raw JavaScript snippet — useful when you need full control over the script.

1. In GTM, go to **Tags → New**.
2. Name the tag and select **Custom HTML** as the tag type.
3. Paste the following script, updating the values for your deployment:

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

| Parameter | Description |
|---|---|
| `customerWidgetUrl` | IP or FQDN of the server hosting the Customer Widget |
| `widgetIdentifier` | Web identifier configured in Unified Admin (case-sensitive) |
| `serviceIdentifier` | Service Identifier configured in Unified Admin |

4. Add a **Page View** trigger.
5. Click **Save**, then **Submit** to publish.

> You can also embed this script directly in the `<head>` tag of your website HTML without GTM.

---

## Method 4: GTM Browser CX Activity (Embed + Push Browser Data)

This method deploys the widget and pushes browser activity as a CX event simultaneously.

1. Clone or download the [expertflow/GTM-Browser-CX-Activity](https://github.com/expertflow/GTM-Browser-CX-Activity) repository.
2. In GTM, go to **Admin → Import Container**.
3. Select the `workspace.json` file from the cloned repository.
4. Choose **Merge** (recommended, to avoid losing existing tags).
5. Once imported, navigate to **Tags** and click the **cx-activity** tag.
6. Update all FQDN values to match your CX server deployment.
7. Save changes, then **Submit** to publish.

> The widget deployment tag is included in this container — no need to import it separately.

---

## Preview and Debug Before Publishing

Before publishing, validate your setup:

1. Click **Preview** in the top right of your workspace.
2. Enter your site's URL and click **Connect** — your site opens with GTM connected.
3. Click back to the **Tag Assistant** tab and click **Continue**.
4. Monitor fired tags in **Tag Assistant** to confirm the widget loads correctly.
5. Click **Submit** to publish only after confirming no errors.

---

## Customer Identification via Google Analytics

ExpertFlow CX can use the Google Analytics unique ID (`_gid`) as the `channelCustomerIdentifier` to recognize returning customers.

### Prerequisites

Google Analytics must be active on the site — either via direct script embed or a GTM tag. Once active, `_gid` is available in browser cookies and the widget reads it automatically.

### Enabling GA via GTM (Universal Analytics)

1. In GTM, create a new **Variable** of type **Google Analytics Settings** with your GA Tracking ID.
2. Create a new **Tag** — type: `Google Analytics: Universal Analytics`, track type: `Page View`.
3. Attach the GA variable and add a **Page View** trigger. Save and publish.

### Enabling GA via GTM (GA4)

1. Create a new **Tag** — type: `Google Analytics: GA4 Configuration`.
2. Add the Measurement ID from your GA4 Data Stream. Check the **Page View** event box.
3. Add a **Page View** trigger. Save and publish.

---

## Widget Customization

### Custom Logo vs Chat Icon

To switch from the default chat icon to a custom logo, set the custom logo boolean to `true` in the Customer Widget custom values file. Set it to `false` to revert to the chat icon.

### Additional Panel

An optional additional panel can be shown alongside the chat widget. Enable it in the Customer Widget custom values file by setting the panel boolean to `true`, and uncomment the relevant HTML in `index.md`. Set to `false` to hide it.

---

## Related Articles

- [Configuring the Customer Widget](../Administrator/Configuring-the-Customer-Widget.md)
- [Customer Widget Features and Capabilities](../Administrator/Customer-Widget-Features-Capabilities.md)
- [JavaScript SDK for Customer-Facing Channels](../Developer_Integrator/JavaScript-SDK.md)
- [Customer-Facing SDK for Omnichannel Communication](../Developer_Integrator/Customer-Facing-SDK.md)
