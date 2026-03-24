---
audience: [platform-overview]
doc-type: explanation
difficulty: beginner
aliases: []
---

# Two-Factor Authentication (2FA) Business Overview

The EFCX 2FA Service provides a critical security layer that requires a secondary verification step during agent login, mitigating risks of unauthorized access and credential theft.

## Business Value
- **Enhanced Security**: Protects against phishing, weak passwords, and SIM-swapping.
- **Regulatory Compliance**: Helps meet industry standards like PCI-DSS and SOC2.
- **Operational Flexibility**: Multiple delivery methods (Email, SMS, Auth Apps) to balance cost and security.

## Key Concepts

### Tenant-Wide Enforcement
2FA is a global setting. Once enabled for a tenant, it applies to **all users** (Agents, Supervisors, Admins) without exception, ensuring no security gaps.

### Supported Channels
- **Email**: Low cost, easy deployment.
- **Authenticator App (TOTP)**: High security, works offline (e.g., Google/Microsoft Authenticator).
- **SMS/WhatsApp**: Reliable delivery, though higher per-message costs.

### Just-in-Time Registration
Agents do not need pre-registration. The system guides them through a mandatory setup flow during their first login after 2FA is enabled.

## Strategy for Implementation
1. **Choose a Method**: Organizations concerned with telecom costs should prioritize **Authenticator Apps**.
2. **Define Policy**: Set OTP validity duration and retry limits for security.
3. **Deploy**: Enable via Tenant Settings for immediate global enforcement.
