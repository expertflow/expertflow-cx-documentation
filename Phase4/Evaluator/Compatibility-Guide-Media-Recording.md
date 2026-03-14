---
title: "Compatibility Guide — Media Recording"
summary: "Compatibility reference for ExpertFlow CX Media Recording — covering OS, Docker, phone, database, recorder, browser, and Cisco platform compatibility requirements."
audience: [solution-admin, evaluator, quality-manager]
product-area: [voice]
doc-type: reference
difficulty: intermediate
keywords: ["media recording compatibility CX", "voice recording compatibility", "CX recording OS compatibility", "Docker recording CX", "Cisco recording compatibility CX", "VRS compatibility guide", "screen recording browser CX", "PostgreSQL recording CX"]
aliases: ["recording compatibility guide CX", "media recording support matrix", "CX VRS compatibility"]
last-updated: 2026-03-10
---

# Compatibility Guide — Media Recording

ExpertFlow Media Recording supports single and multi-site contact centers with up to 100 concurrent agents. It records individual call legs including hold, transfer, and conference. This guide details the supported platforms and versions.

## OS Compatibility

| Item | Notes |
|---|---|
| **Debian** | Debian 12 (full version) |
| **Windows (Screen Recording)** | Windows 10 or Windows 11 |

## Docker Engine Compatibility

| Item | Version |
|---|---|
| **Docker CE** | 18+ |
| **Docker Compose** | 2.35.1 |

## Phone Compatibility

Formal testing and QA are executed with the following phones only.

| Phone | Tested Version |
|---|---|
| **MicroSIP** | 3.21.3 |
| **Cisco IP Communicator** | 8.6.1.13 |

## Database Compatibility

| Database | Recommended Version |
|---|---|
| **SQL Server** | `mcr.microsoft.com/mssql/server:2019-latest` |
| **PostgreSQL** | v13 or higher |

## Recorder Compatibility

| Recorder | Version |
|---|---|
| **FreeSWITCH** (for Cisco environments) | 1.10.10 |
| **FusionPBX** (for EFCX environments) | 5.2.2 |

## Browser Compatibility

| Browser | Version | Notes |
|---|---|---|
| **Chrome** | 134.0.x | Tested |
| **Firefox** | 136.0.x | Tested |
| **Edge** | — | Not tested; on-demand testing can be planned |

## Cisco Platform Compatibility

### Cisco Unified CCX

- UCCX 12.5.1.x, Non-SSO
- UCCX 15.0.1.x, Non-SSO

### Cisco Unified CCE

- UCCE 12.5.1.x, Non-SSO

### Cisco Unified CM

- CUCM 12.5.1.x (no Active Directory configured)
- CUCM 15.0.1.x (no Active Directory configured)

## Related Articles

- [Playing Screen Recordings in Quality Management](Playing-Screen-Recordings.md)
- [Handle Voice Recordings](Handle-Voice-Recording.md)
- [As an Evaluator](../Getting_Started/Evaluator-Guide.md)
- [Voice Recording and Compliance Features](../Decision_Maker/Voice-Recording-and-Compliance-Features.md)
