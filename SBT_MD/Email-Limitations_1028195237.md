# CX Knowledgebase : Email Limitations

  * Related to attachments, only types mentioned [here](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/1042221531/4.9%2BSend%2Ba%2BMessage#Send-File-Attachments) are supported generally. There could be some more types as well which we also able to send. Below are the file types tested with Email Connector:

    * Agent Desk to Email: 

      * png, jpg/jpeg, pdf, doc/docx, ppt/pptx, xls/xlsx, txt, mp4, mp3

    * Email to Agent Desk: 

      * png, jpg/jpeg, pdf, doc/docx, ppt/pptx, xls/xlsx, txt, mp4, mp3, gif

  * The indentation of emails while replying and forwarding might not match all the Email clients because it is different for Gmail, MS Exchange etc. So, it might be slightly disturbing as part of UX but the content is 100% visible and accurate. It’s just the indentation and lines that might be slightly distorted based on the email client you use.

  * We do not support to send outbound email to any email-address directly however if any conversation is on going with customer’s interaction then we allows to send a new email to the on-going customer using the Email Icon from the right top of the customer interactions screen in case of Email messages.

  * In order to ensure the smooth processing, whatever time we set as part of the configuration in config map param `SCHEDULER_FIXED_RATE_IN_MS` for the pooling of data via EWS (Exchange Web Service), we minus that time with `1 minute` and try to search in that window. This will allow exchange servers sufficient time to fetch newly received emails, process them, index them and make them available when we try to search them. This will ensure no email loss due to processing issues of exchange server. This limitation exists specifically for Email Exchange based Email Connector. 

    * _E.g: If we set time 5mins. Then if the first iteration time was 00:00:00 and after 5 mins when it gets executed, it will try to fetch the data from 23:59:00 till 00:04:00 instead of 00:00:00 till 00:05:00. Then in the next iteration it will fetch from 00:04:00 till 00:09:00 and so on… It will not impact customer point of view, but it will just allow the exchange server to process the recently fetched emails easily in this 1minute gap._

  * Using two different email aliases for single email address will not work in case of existing EMAIL feature. If we have the serviceIdentifier in Channels section of unified admin = “abc@email.com“ and this abc email is also receiving emails if any customer sends and email to “abc2@email.com”, then in that case agent will be able to receive emails but while doing “ReplyAll” **from** email will be same as its mentioned in serviceIdentifier of unified admin channels section however the **to/cc** will contain [abc2@email.com](mailto:abc2@email.com) as well because ReplyAll will logic is that other than sender all emails will be part of Cc or To. Thats why while using ReplyAll in case of multiple aliases might not work as expected and agent might receive his own email as well.



