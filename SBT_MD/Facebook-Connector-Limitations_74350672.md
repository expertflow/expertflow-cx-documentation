# CX Knowledgebase : Facebook Connector Limitations

  * Nested comments having photos and videos, stickers, and GIFs are not returned by the FB Graph API sometime (**API used for View full Post**), only their captions are being returned.

  * For now, the FB Graph API is only returning first-level video comments posted by the admin of the page.

  * The FB Graph API does not return the profile photo of the users commenting on the post.

  * In case of a single FB comment, some GIFs will not land on the agent's desk because of the broken payload received from Facebook.

  * When a single comment arrives on the agent's desk we can't show where it was posted because it does not contain the FB page info. 

  * Highlighted text is not supported on Facebook DM.

  * Emojis are not supported by the agent desk.

  * Menu buttons are not supported



