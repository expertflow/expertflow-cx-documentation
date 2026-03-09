# CX Knowledgebase : Facebook Social Media

Facebook is a supported customer channel that enables businesses to handle interactions with customers and potential customers on the most common social network.

Expertflow CX provides integration of Facebook Channel via

  * Facebook Social Media Posts/Comments

  * [Facebook Direct Message](Facebook-Direct-Message_2526025.html)




## Getting Started

To begin with Facebook, one must have a Facebook App and must be a registered user to create a personal profile and add others for customer interactions. For this, he should have a Facebook account, which must have been added to the Facebook Page. Also need to grant access to the Facebook App.

The Administrators can create a Facebook Page, [grant a user access to the Facebook App](Facebook---Configuration-Guide_2531616.html), and create a Page Access Token by following the step-by-step procedure of [Create Page Access Token](Facebook---Configuration-Guide_2531616.html)

To set up the Facebook Channel, the Facebook connector needs to be configured in the [Unified Admin](Unified-Admin-Guide_2524407.html) of the Expertflow CX's application. This one-time configuration will help the business interact with both channels of Facebook on a single interface.

## Facebook Social Media Posts/Comments

allows the business to handle public Facebook comments made on the company's Facebook page. The contact centre representatives can respond to the post comment visible publicly. A new channel session will be created for each new comment from a Facebook customer. The comment will be considered a chat request and will be the representative with the customer's Facebook name. In the case of PULL mode, the contact centre representatives can join the chat from the customer's list.

### Channel Capabilities

The agent receives the comment as a new incoming media request. Upon accepting the request, a new session will be started in the Conversation View. The agent can see the customer's comments and can perform the following actions.

#### Reply to a Comment

A Facebook comment can be replied to by hovering the mouse on top of the comment. The 'Reply' button will appear at the top of the comment. Clicking this will bring the agent to the Message Composer area and the selected channel will automatically be set as **'Facebook'.** In this way, the comment can be replied to on the company's Facebook Page as shown in the screenshot below.

![](attachments/2526031/2549610.png?width=738)

_Reply to a Comment_

#### Edit a Comment

A Facebook comment sent from Agent Desk can be edited during the active channel session only, and agents are restricted to editing only their own comments. This functionality is enabled by default; however, you can explicitly manage it using the `EDIT_MESSAGE_SUPPORT_SM` boolean field in the channel provider configuration. If this attribute is not added, the edit action remains available, allowing an edit icon to appear on outgoing comments so that updates are reflected on the Facebook post accordingly. To specifically disable this feature, the attribute must be added and set to `false`.

![image-20260127-135034.png](attachments/2526031/1690763326.png?width=600)

#### Like a Comment

Enables the agent to like a comment by simply clicking on the 'Like' button, at the top of the respective comment. A 'thumbs up' will pop up along with the comment on the company's Facebook Page.

![](attachments/2526031/2549615.png?width=680)

#### Hide or Unhide a Comment

To hide a specific comment, expand the arrow on the top right of the comment, as shown below. Click on the 'Hide' button on a comment. The specific comment will be hidden from the Facebook Post. It will be shown as blurred, with the indication of 'Hidden Message' in the Conversation View. Once hidden, you can see an Unhide icon at the top of the hidden message, which can be used to unhide the comment message.

  


![](attachments/2526031/2549605.gif?width=680)![Hidden Message-Facebook.png](attachments/2526031/1693024277.png?width=385)

#### Delete a Comment

To delete a specific comment, expand the arrow on the top right of the comment, as shown below. Click on the 'Delete' button from the top. The comment will be blurred with the indication of 'Deleted Message' and will also be deleted from the company's Facebook Page.

![](attachments/2526031/2549600.gif?width=680)

### Support Multimedia Comments

Expertflow CX's Facebook connector provides support to receive multimedia comments of the following types

  * **Photos**




Enables to receive photos from the customer's Facebook page. The business can then respond to this type of media comment just as a 'reply' to a comment.

![](attachments/2526031/2549580.png?width=680)

  


  * **GIF**




Enables the business to receive and respond to gifs from the customer's page shown as in the screenshot below.

![](attachments/2526031/2549585.png?width=680)

By default, the file size of multimedia is set to 5MB. However, File size and extensions are configurable. For details see [CIM Media Messages](Multimedia-Messages_2525501.html)

  * Gif is shown as a video file. 

  * can be played upon clicking the 'Play' button.




### Limitation

Support for video comments is not provided as of now.

### View Full Post

Enables to see Facebook posts and first-level comments on the post including text and multi-media comments as shown below. To view the full post, expand the arrow at top of the comment and click on the 'View Full Post' button. To view the complete post, scroll down.

![](attachments/2526031/2549595.gif?width=868)

Once a view full post screen pops up, one can see the comments section along with the page name adjusted in the header of the page. For example, in the above gif, one can observe the Test Cim Page written on the top right corner along with the cross sign. The name of that page serves as a hyperlink and redirects the user to the original Facebook post where the comment was posted. 

### Limitations

  * Nested comments of multimedia photos, stickers and GIFs) are not supported as of now.

  * Profile photo of the user is not shown in Full View Post.




### Private Reply to a Comment

Enables the business to send a private response to a customer instead of responding publicly as a reply to a comment. send a one-time private reply to the customer on [**Facebook Messenger**](Facebook-Direct-Message_2526025.html)
