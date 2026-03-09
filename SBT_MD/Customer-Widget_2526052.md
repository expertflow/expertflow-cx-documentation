# CX Knowledgebase : Customer Widget

The Customer Widget is an embeddable, omni-channel engagement component that you add to your existing digital properties—such as websites and web applications—using a lightweight JavaScript snippet. Once embedded, it lets customers access AI-powered knowledge base for self-service or start real-time conversations with your contact center over chat, voice, or video, directly from the page they are on. The widget also surfaces interaction history and live contact center status (including opening and closing hours).

Follow this guide to configure the widget.

[Configure the Customer widget](Add-a-Web-Channel_1496449025.html)

## Customizable Branding

The widget integrates naturally with your existing digital properties by supporting extensive, no-code configuration options.

  * **Personalization Options:** Easily set the company name, opening lines, languages, and pop-out modes to align the widget's experience with your brand identity. You may also fully theme the Customer Widget to match your brand's colors, fonts, icons, logos, and styling, ensuring visual consistency across all digital properties.

  * **No-code management:** Customize the user experience when customers click your widget launcher icon. Choose to attach a pre-conversation form before starting a new conversation and display business hours through widget settings without any additional coding efforts.




## Responsive Customer widget Sizing

customer widget adapts to different website sizes, whether mobile or web applications. Customers can adjust the widget’s length and dimensions when embedding it into their products.

## Communication Modes

The widget provides a single entry point for all communication modes:

  * **Web Chat:** Supports standard text chat functionality, including rich media messaging (emojis, attachments, links, images, videos). 

  * **Voice and video calls:** Facilitates the immediate initiation of secure, high-quality audio and video calls directly from the browser to the agent.

  * Switching chat-to-voice, chat-to-video. For more details, see [here](WebRTC-for-CX_687211264.html). 




## Context Capture and Proactive Engagement

The widget captures context when a customer initiates contact, improving service personalization.

  * **Contextual Data Capture:** It captures data such as browser language, URL, and host application User ID, which is immediately integrated with the [**Interaction Profile**](/wiki/pages/createpage.action?spaceKey=SBT&title=CX%20Customer%20Interaction%20Profile&linkCreation=true&fromPageId=2526052) for use in personalized routing.

  * **Proactive Triggers:** The widget can be configured to proactively launch a chat window based on predefined customer behaviors (e.g., spending more than 60 seconds on a payment page) to offer assistance.




## Identity and Authentication Methods

The Customer Widget supports various deployment models based on the required level of customer identification and security. This flexibility allows contact center owners to embed the widget differently across various digital properties (e.g., public websites vs. secured portals).

  * **Anonymous (Public Website):** The widget is set up to allow communication without requiring user credentials. This is ideal for engaging general website visitors and tracking their activity. Identification can be based on non-PII data like the browser's device ID.

  * **Explicit Login (Self-Service Portal):** Users are required to provide credentials (e.g., username/password) within the widget before initiating communication. This ensures the customer is formally identified and their full **Interaction Profile** is accessed immediately.

  * **Seamless Authentication (SSO/Mobile App):** When a user is already authenticated in the host portal or mobile app, the widget automatically recognizes the user's identity. Communication starts immediately with the customer already identified, eliminating the need for the user to provide login credentials again (Single Sign-On).




## Knowledgebase Integration

Leverage AI-driven Knowledgebases integrated with the Customer widget to deliver intelligent self-service experiences. By harnessing advanced artificial intelligence, customers can quickly access relevant information through natural language queries and resolve issues independently. This AI-powered approach not only enhances customer satisfaction but also drives operational excellence for the contact center.

## Accessibility Compliance (WCAG)

The Customer Widget is built to comply with **WCAG (Web Content Accessibility Guidelines)** standards, ensuring that users with disabilities can easily access and interact with the communication features.

  * **Keyboard Navigation:** All interactive elements within the widget can be accessed and operated using only a keyboard (Tab key and Enter key), supporting users who cannot use a mouse.

  * **Screen Reader Optimization (ARIA):** The widget incorporates ARIA (Accessible Rich Internet Applications) attributes to properly label elements and announce state changes. This ensures that customers using screen readers (like NVDA or JAWS) can understand the conversation flow, button functions, and field inputs.

  * **Color Contrast:** Configuration options ensure sufficient color contrast between text and backgrounds, making the content legible for users with low vision. 




## Widget Embedding Options

The widget is embedded using a JavaScript code snippet. The snippet includes parameters to define the widget's appearance, enable communication channels (chat, voice, video), and specify the data fields to be captured and passed to the Interaction Profile.

The following embedding options are available:

  * Direct Embedding

  * Google Tag Embedding




### Direct Embedding

This allows for direct embedding of the JavaScript code into the HTML of the host application.

### Google Tag Manager Integration

Expertflow CX supports seamless deployment via Google Tag Manager (GTM), enabling marketing teams to manage the widget's visibility and tracking without developer intervention.

  * **Seamless GTM Deployment:** Deploy the widget effortlessly via GTM, eliminating direct code changes on your site or app. Simply paste the widget script as a Custom HTML tag, trigger on page views or custom events, and manage updates centrally.

  * **Event Tracking:** Capture interactions like widget opens, messages sent, or escalations as custom GTM events for analytics in GA4 or other tools.

  * **No-Code Management:** Use GTM's preview mode to test, then publish. This is ideal for managing widget visibility and data flows without code redeployment.

  * **Cross-Platform:** This method works effectively for web, mobile apps, and Single Page Applications (SPAs) by pushing interaction data to the dataLayer for unified tracking.




## JavaScript SDK

Expertflow provides a **JavaScript SDK** (Software Development Kit) to embed Customer widget capabilities into your own web widgets or mobile apps. The SDK provides APIs that allow developers to trigger custom events, update customer context dynamically, or programmatically open/close the widget based on application logic.

For more details of the SDK functions, please visit the [SDK](JavaScript-SDK-for-customer-facing-channels_1496743937.html).

## Browser Compatibility

The widget runs smoothly in Google Chrome and Firefox. A testing cycle can be carried out on other browsers on demand.

**Limitation**

  * Screen sharing is not yet supported. This will soon become a part of the future release.



