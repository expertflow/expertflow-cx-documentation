---
title: "Archival Configuration"
summary: "Reference for configuring voice recording archival in ExpertFlow CX Voice Recording Solution — covering SFTP server settings, archive-only and copy-and-archive modes, copy time, and purge time."
audience: [solution-admin]
product-area: [voice]
doc-type: reference
difficulty: intermediate
keywords: ["archival configuration CX", "voice recording archival", "SFTP archival CX", "recording archive mode", "copy and archive recordings", "recording purge time CX", "voice recording storage", "CX recording archival"]
aliases: ["recording archival CX", "archive voice recordings CX", "SFTP recording archive"]
last-updated: 2026-03-10
---

# Archival Configuration

The Archival Configuration page in the **Voice Recording Solution** controls how call recordings are moved from the primary recording server to a long-term archival destination. Archival is used to manage storage capacity on the main recording server while preserving recordings for compliance and quality review.

## Enabling Archival

The **Enable Archival Service** toggle must be turned on to activate the archival process. When disabled, no recordings are archived regardless of other settings.

---

## Configuration Settings

| Setting | Description |
|---|---|
| **Enable Archival Service** | Master toggle. Must be enabled for archival to function. |
| **SFTP Server IP Address** | IP address of the remote archival server. |
| **Folder Path** | Path on the archival server where recordings will be stored. |
| **Username** | Username for SFTP authentication. Must have write permissions on the target folder. |
| **Password** | Password for the SFTP user. |
| **Archival Mode** | Select `Archive Only` or `Copy and Archive` (see below). |

---

## Archival Modes

### Archive Only

Recordings are moved to the archival server after the specified number of days. The original file is removed from the main recording server once archived.

### Copy and Archive

Recordings are **copied** to the archival server and the originals are retained on the main server for a configurable period before being purged.

| Sub-setting | Description |
|---|---|
| **Copy Time** | Time threshold after which files are copied to the archival server. |
| **Purge Time** | Number of days after which successfully copied files are removed from the main recording server. |

**Use Copy and Archive when:** you need recordings to remain immediately accessible on the main server for active review, while also being backed up to a remote location for long-term retention.

---

## Related Articles

- [Media Server Configuration CX Voice](Media-Server-Configuration-CX-Voice.md)
- [Accessing CX Voice Components](Accessing-CX-Voice-Components.md)
- [Voice Recording and Compliance Features](../Decision_Maker/Voice-Recording-and-Compliance-Features.md)
