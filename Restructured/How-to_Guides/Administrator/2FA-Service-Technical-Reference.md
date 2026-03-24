---
audience: [administrator]
doc-type: reference
difficulty: beginner
aliases: []
---

# 2FA Service Technical Reference

This document provides technical details on the OTP-based Two-Factor Authentication (2FA) service in Expertflow CX.

## Architecture
The 2FA service is a native EFCX component that manages the entire OTP lifecycle: generation, delivery, validation, and expiry.

## Prerequisites
1. **Channel Configuration**: The delivery channel (e.g., Email) must be configured in **Unified Admin**.
2. **Tenant Settings**: 2FA must be enabled via the Tenant Settings API.
3. **User Data**: Ensure users have unique identifiers (email/phone) as the system does not support shared contact points for 2FA.

## Key Capabilities

### OTP Lifecycle Management
- **Expiry**: OTPs are valid only for a configurable duration.
- **Single Use**: An OTP is invalidated immediately upon successful login.
- **Regeneration**: Users can request a new code after a "cooldown" period.
- **Generic Feedback**: Error messages are generic (e.g., "Invalid or expired code") to prevent information leakage to attackers.

### Registration Flow
- **First Login**: Users are prompted to register their contact details or scan a QR code (for TOTP).
- **Persistence**: Verified contact identifiers are stored in the IAM profile for subsequent logins.

## Limitations
- **Single Channel**: Only one delivery channel can be active per tenant at a time.
- **No Fallback**: If the primary channel is unavailable, there is no secondary fallback (e.g., cannot switch from Email to SMS on the fly).
- **Global Scope**: Enrollment is mandatory for all roles; there is no role-based exclusion.

## Troubleshooting
- **Invalid OTP**: Often caused by entering an old code after a new one was generated or the code expiring.
- **Shared Emails**: If two users share an email, only the most recently generated OTP across both accounts will be valid.
