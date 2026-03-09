# CX Knowledgebase : Outbound Flows Limitations

  1. The campaign duplication feature is disabled for now and will be available in future versions.  
  
  2. Contact Sources: When you upload a CSV file, contacts are not stored and loaded immediately. Being stored in chunks a manual refresh is required to see the updated view on the front end.

  3. Up to a total of 50,000 contacts can be uploaded in one CSV file.

  4. RESTful API via the Contact Source section is currently disabled; the API however is now available.

  5. The decision node is not handling all the call results coming from EF CC (Freeswitch). CX Campaigns unified call results are available here: [Outbound Result Notifications - to be reviewed and updated](Outbound-Result-Notifications---to-be-reviewed-and-updated_978747415.html)

  6. When you modify a running campaign's flow, only **unexecuted contacts** will be affected. This includes contacts not yet dialed and any newly uploaded contacts.

  7. In case a call is transferred or consulted, the campaign report does not show records for multiple agents involved in that call.

  8. The call duration time shown in campaign reports includes the ringing time as well, not just the customer talking time.

  9. Multiple wrap-ups for a single call in UCCE are not allowed.

  10. When an agent’s team is changed and the pipeline is run, the updated team is displayed in the campaign reports even for older data.

  11. Dial Rate and Success Rate in campaign reports can exceed 100% if the dialer node is deleted and re-configured within the same published campaign.

  12. Data for personal callbacks of the campaign is currently not displayed in the campaign reports separately.

  13. Integration with Cisco (Dialers) is not available as part of the CX Multi-Tenant Solution.

  14. In UCCX 12.0 HA setup, if a node switch occurs during an active call, the conversation data is not generated on the Cisco side, resulting in missing conversation records in Unified Admin.



