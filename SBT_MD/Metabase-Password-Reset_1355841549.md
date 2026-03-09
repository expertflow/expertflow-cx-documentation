# CX Knowledgebase : Metabase Password Reset

1\. Stop the running Metabase application.  
  
2\. Restart Metabase with reset-password [email@example.com](mailto:email@example.com), where “email@example.com” is the email associated with the admin account:
[code] 
    kubectl exec -it -n metabase <pod-name> -- java -jar /app/metabase.jar reset-password email@example.com
[/code]

3\. Metabase will print out a random token as this:
[code] 
    Resetting password for email@example.com...
    
    OK [[[1_7db2b600-d538-4aeb-b4f7-0cf5b1970d89]]]
[/code]

4\. Start Metabase normally again (without the reset-password option).

5\. Navigate to it in your browser using the path /auth/reset_password/:token, where “: token” is the token that was generated from the step above. The full URL should look something as this:
[code] 
    HTTPS:<FQDN>/metabase/auth/reset_password/1_7db2b600-d538-4aeb-b4f7-0cf5b1970d89
[/code]

6\. You should now see a page where you can input a new password for the admin account.
