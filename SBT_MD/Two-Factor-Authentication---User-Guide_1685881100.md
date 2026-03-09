# CX Knowledgebase : Two Factor Authentication - User Guide

Expertflow CX supports two-factor authentication (2FA) to provide an additional layer of security when you sign in.

If 2FA is enabled for your account, you will sign in with:

  1. Your username and password, and then

  2. A one-time password (OTP) or passcode delivered through one of the configured 2FA channels.




Expertflow CX supports the following 2FA channels:

  * Authenticator mobile app (Google Authenticator or Microsoft Authenticator)

  * Email

  * SMS

  * RSA SecurID




### **How 2FA Works**

At a high level, the login flow is:

  1. You enter your username and password on the Expertflow CX login screen and click **Login**.

  2. If 2FA is enabled for your account, you are redirected to a second step where you must complete verification using one of the configured 2FA channels.

  3. You will be provided with an OTP or passcode from your configured 2FA channel.

  4. If the OTP or passcode is valid, you are logged in successfully.




The following sections describe the detailed steps for each 2FA channel.

## 2FA with Google/Microsoft Authenticator

Use this method if your organization has enabled 2FA with the Google Authenticator or Microsoft Authenticator mobile app.

| 

#### **When you are not yet registered for 2FA**

| 

#### **When you are already registered for 2FA**  
  
---|---|---  
1| On the login screen, enter your username and password and click **Login**.![Screenshot 2025-04-22 at 12.11.32 PM.png](attachments/1685881100/1685881172.png?width=342)| On the login screen, enter your username and password and click **Login**.  
2| The system opens a registration screen that shows:

  * A QR code, and
  * A secret key (for manual entry if you do not scan the QR code).  
The screen also shows an OTP input field.

![QR Code](attachments/1685881100/1685881169.png?width=342)| You are redirected to a screen with an OTP input field.![OTP code secret](attachments/1685881100/1685881163.png?width=700)  
3| On your mobile device, open the Google Authenticator or Microsoft Authenticator app.![Secret key for authenticator app](attachments/1685881100/1685881166.png?width=700)| Open the Google Authenticator or Microsoft Authenticator app on your device and locate the OTP for your Expertflow CX account.  
4| In the app, add a new account and either:

  * Scan the QR code on the screen, or
  * Enter the secret key manually.

![Secret key for authenticator app](attachments/1685881100/1685881166.png?width=700)|   
5| The app displays a one-time password (OTP) for your account and refreshes the OTP every 30 seconds.| Enter the currently visible OTP from the app into the OTP field and click **Send**.  
6| If the OTP is valid:

  * You are logged in successfully, and
  * Your account is registered for 2FA using the Authenticator app for future logins.

| If the OTP is valid, you are logged in successfully.  
7| Enter the currently visible OTP from the app into the OTP field on the screen and click **Register**.|   
  
## 2FA with Email

Use this method if your organization has enabled 2FA via email.

#### **Prerequisite (for administrators):**

Make sure the configurations described here are completed before using the Email 2FA solution:  
[2FA Configuration Guide - Email](2FA-Configuration-Guide---Email_1690927131.html)

| 

#### **When you are not yet registered for 2FA**

| 

#### **When you are already registered for 2FA**  
  
---|---|---  
1| Enter your username and password on the login screen and click **Login**.![Login screen](attachments/1685881100/1685881172.png?width=342)| Enter your username and password on the login screen and click **Login**.  
2| The system opens a registration screen and prompts you to enter your email address for 2FA.![email verification](attachments/1685881100/1685881121.png?width=931)| The system opens a 2FA screen with an OTP input field and sends an OTP to your registered email address.  
3| Enter your email address in the input field and click **Next**.| If you do not receive the email, click Resend OTP after at least one minute to request a new OTP.  
4| The system shows a confirmation dialog that asks you to verify your email address.

  * If the email address is incorrect, edit it and confirm again.
  * If the email address is correct, confirm it. The system sends an OTP to that email address.

![Email confirmation](attachments/1685881100/1685881118.png?width=931)| Enter the OTP from the email into the OTP field and click Submit.  
5| The system shows an OTP input field on the screen.![enter OTP screen](attachments/1685881100/1685881115.png?width=931)| When the OTP is valid, the system signs you in.  
6| If you do not receive the email, click Resend OTP to request another code. The Resend OTP button becomes available after one minute.|   
7| Open your email inbox and find the message that contains the OTP![OTP received via email](attachments/1685881100/1685881112.png?width=931)|   
8| Enter the OTP from the email into the OTP field and submit it.|   
9| When the OTP is valid, the system signs you in and registers your account for 2FA with Email.![received OTP is entered via email](attachments/1685881100/1685881109.png?width=931)|   
  
## 2FA with SMS

Use this method when your organization enables 2FA via SMS to your mobile phone number.

| 

#### **When you are not yet registered for 2FA**

| 

#### **When you are already registered for 2FA**  
  
---|---|---  
1| On the login screen, enter your username and password and click **Login**.| On the login screen, enter your username and password and click **Login**.  
2| This redirects you to a registration screen and prompts you to enter your mobile phone number for 2FA.![Enter phone number for 2FA](attachments/1685881100/1685881160.png?width=700)| This redirects you to a screen with an OTP input field. An OTP is sent automatically to your registered phone number via SMS.  
3| Enter your phone number in the input field and click **Register**.| If you do not receive the SMS:

  1. Return to the login screen and sign in again to trigger a new OTP.

  
4| A confirmation dialog appears asking you to verify your phone number:

  * If the number is incorrect, you can edit it and confirm again.
  * If the number is correct, an OTP is sent to your phone via SMS.

![phone number confirmation for 2FA sms](attachments/1685881100/1685881157.png?width=700)| Enter the OTP received via SMS in the OTP field and click **Send**.   
  
5| An OTP input field is displayed on the screen.| If the OTP is valid, you are logged in successfully.  
6| If you do not receive the SMS, you can click **Resend OTP** to request another one.  
This resend option is available while you are registering for 2FA.  
7| Enter the OTP received via SMS in the OTP field and submit.![enter OTP via SMS](attachments/1685881100/1685881154.png?width=700)  
8| If the OTP is valid:

  1. You are logged in successfully, and
  2. Your account is registered for 2FA using SMS for future logins.

  
  
## 2FA with Email

Prerequisite: Make sure following configurations are done for using 2FA Email solution: [2FA Configuration Guide - Email](2FA-Configuration-Guide---Email_1690927131.html)

  1. **User has not registered for 2FA**

     1. User enters his login credentials on login screen and clicks “Login”.

![image-20260126-074145.png](attachments/1685881100/1685881124.png?width=931)
     2. User will be redirected to another screen and will be prompted to enter their email in the input field shown for 2FA registration.

![image-20260126-074458.png](attachments/1685881100/1685881121.png?width=931)
     3. User will enter their email in input field and click “Next”.

     4. A dialogue box will be displayed to user to confirm their email address.

![image-20260126-074634.png](attachments/1685881100/1685881118.png?width=931)
        1. If it’s wrong then user will be allowed to edit their email address.

        2. If it’s correct then an OTP will be sent to user’s entered email.

     5. An input field will be shown to user to enter the OTP.

![image-20260126-083019.png](attachments/1685881100/1685881115.png?width=931)
     6. User can also request to resend OTP (if it is not received) by clicking “Resend OTP” button. For email, the resend button is set to be available after a minute.

     7. User receives the OTP on email

![image-20260126-075058.png](attachments/1685881100/1685881112.png?width=931)
     8. User enters the OTP received on email. If OTP is valid then user will be successfully logged in and registered for 2FA.

![image-20260126-082836.png](attachments/1685881100/1685881109.png?width=931)
  2. **User has already registered for 2FA**

     1. User enters his login credentials on login screen (email image 1) and clicks “Login”.

     2. User will be redirected to another screen (email image 4) where an input field will be shown to user to enter OTP sent to his registered email.

     3. If OTP is not received then user can click resend (after 1 minute is completed) to receive another OTP.

     4. User will enter the OTP received via registered email in OTP field and click “Submit”.

     5. If OTP is valid then user will be successfully logged in.




## 2FA with RSA SecurID

  * Unlike the other two 2FA channels, there will be no 2FA registration flow for RSA SecurID. This process will be managed by the Customer/Administrator.

  * If 2FA is enabled on the solution, each user will be required to enter an OTP during login. If a user does not have access to the OTP, they should contact the Administrator.




  * User enters his login credentials on login screen and clicks “Login”.

![Login screen.png](attachments/1685881100/1685881151.png?width=700)
  * User will be redirected to another screen where an input field will be shown to user to enter OTP.  


![Screenshot 2025-05-23 at 8.49.51 PM.png](attachments/1685881100/1685881133.png?width=700)
  * User will enter a 14 characters passcode in OTP field. First 8 characters will be the PIN setup by the user in SecurID Self Service Console and last 6 characters will be the OTP received on RSA Authenticator App.

  * User will be able to show/hide passcode by clicking on the **eye** icon.  


![Screenshot 2025-05-23 at 8.50.24 PM.png](attachments/1685881100/1685881130.png?width=700)
  * If OTP is valid then user will be successfully logged in.




The following error will be visible if:

  1. The OTP is invalid.

  2. The configurations are invalid.

  3. There is an issue with the RSA server.

![Screenshot 2025-05-23 at 8.57.08 PM.png](attachments/1685881100/1685881127.png?width=670)


