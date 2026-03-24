---
audience: [administrator]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# 2FA Email Configuration Guide

This guide details the requirements and steps to enable Two-Factor Authentication (2FA) using the Email delivery channel.

## Prerequisites
1. **Email Connector**: You must have a working IMAP-SMTP based email channel configured in Unified Admin.
2. **Channel Identity**: Ensure you have the identifier (email address) used by the sender channel ready.

## Configuration Steps

### 1. Update Tenant Settings
The following configuration must be added to the `tenantSettings` object via the Update Tenant API.

```json
{
  "tenantSettings": {
    "keyCloak": {
      "Otp_Manager_Url": "http://ef-cx-otp-manager-svc:3000/"
    },
    "twoFAConfigs": {
      "is2FAEnabled": true,
      "channelType": "EMAIL",
      "channelServiceIdentifier": "sender@yourdomain.com",
      "otpExpiry": 60,
      "otpMaxAttempts": 3
    }
  }
}
```

### 2. Parameter Definitions
- **is2FAEnabled**: Set to `true` to activate 2FA for all users in the tenant.
- **channelType**: Set to `EMAIL`.
- **channelServiceIdentifier**: The email address configured in the Unified Admin for sending OTPs.
- **otpExpiry**: Time in seconds before a code becomes invalid (recommended: 60-120s).
- **otpMaxAttempts**: Number of failed entries allowed before a cooldown/lockout.

## User Experience
- **Enrollment**: Upon the next login, users will be prompted to enter and verify the email address where they wish to receive OTPs.
- **Verification**: After entering username/password, the system will challenge the user for the 6-digit OTP sent to their registered email.

For troubleshooting and common issues, refer to the [2FA Technical Reference](../../_unmapped/Archive-Notice.md).
