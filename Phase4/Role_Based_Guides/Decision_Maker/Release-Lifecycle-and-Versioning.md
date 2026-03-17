---
title: "Release Lifecycle and Versioning"
summary: "Policy guide for stakeholders to understand semantic versioning, release types, and support windows for ExpertFlow CX."
audience: [decision-maker, partner, reseller]
product-area: [platform, strategic]
doc-type: explanation
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Release Lifecycle and Versioning

ExpertFlow CX follows a predictable release schedule and semantic versioning model to ensure that enterprises and partners can plan upgrades with minimal disruption.

## 1. How Versions Are Numbered
We use the **CX \<major\>.\<minor\>.\<patch\>** format:
- **Major (CX 5.0.0):** Includes breaking changes, significant architectural shifts, or new core modules. Usually released once per year.
- **Minor (CX 5.1.0):** Includes new backward-compatible features and performance enhancements. Released quarterly.
- **Maintenance (CX 5.1.1):** Addresses critical bugs, security vulnerabilities, and minor refinements. Applied as needed.

## 2. Release Stability & Support
- **GA (General Availability):** The stable release recommended for all production environments.
- **Pre-releases (RC):** Early versions for testing new features in lab environments. **Do not use pre-releases for production.**
- **End-of-Life (EoL):** Every Major and Minor release is supported for a defined period (typically 1-3 years). Once EoL is reached, no further security patches or technical support will be provided for that version.

## 3. Planning Recommendations
- **Strategic Alignment:** Budget for one major upgrade annually to leverage new architectural improvements.
- **Stability Maintenance:** Apply maintenance patches immediately to ensure system security and stability.
- **Compliance:** Monitor EoL announcements to ensure your production environment remains on a supported version.

---

*For technical hardware requirements associated with these releases, see [Dialer Performance Benchmarks](Dialer-Performance-Benchmarks.md).*
