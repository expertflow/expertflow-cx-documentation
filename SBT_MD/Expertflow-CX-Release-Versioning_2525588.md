# CX Knowledgebase : Expertflow CX Release Versioning

This guide explains how Expertflow CX versions are numbered and what each type of release means for your deployment or upgrade planning.

**Summary for Managers:**

  * Always use GA releases for production.

  * Plan for major upgrades annually, minor upgrades quarterly, and apply patches as soon as they’re available.

  * Monitor EoL dates to avoid running unsupported versions.




## How Expertflow CX Versions Work

Expertflow CX uses [Semantic versioning](https://semver.org/), which means every release has a version number like:

**CX <major>.<minor>.<patch>**

  * **CX** : Always present as a prefix for all releases.

  * **< major>**: Major version (e.g., 4)

  * **< minor>**: Minor version (e.g., 5)

  * **< patch>**: Patch version (e.g., 0)




**Example:**  
CX4.5.0

![](images/icons/grey_arrow_down.png)Naming a CX version
[code] 
    The CX release version is named as “CX”<major>”.”<minor>”.”<patch>, where: 
    
    "CX" is the version name prefix for all CX releases
    
    <major> ::= <numeric identifier>
    <minor> ::= <numeric identifier>
    <patch> ::= <numeric identifier>
    
    <numeric identifier> ::= "0"
                           | <positive digit>
                           | <positive digit> <digits>
    <digits> ::= <digit>
               | <digit> <digits>
    
    <digit> ::= "0"
              | <positive digit>
    
    <positive digit> ::= "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
[/code]

## Types of Releases

### Major Releases

A major release increases the **< major>** number (e.g., CX4.0.0 → CX5.0.0). It’s done usually once a year. A major release is done when there are: 

  * Breaking changes in public APIs

  * Major architectural changes or new solution components




Major upgrades may require more planning, testing, and possibly changes to integrations.

### Minor Releases

A minor release increases the **< minor>** number (e.g., CX4.5.0 → CX4.6.0). It’s done when:

  * Backward-compatible new features

  * Enhancements and security updates that don’t break existing functionality




Usually, one minor release is done per quarter. Minor upgrades are generally safe and easy to adopt.

### Maintenance (Patch) Releases

A maintenance release increases the **< patch>** number (e.g., CX4.5.0 → CX4.5.1). A maintenance release addresses critical bugs or security vulnerabilities. It is done for: 

  * Bug fixes

  * Security patches

  * Small enhancements to existing features




Expertflow produces maintenance releases for all the GA releases until their [EoL](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/edit-v2/2525588#End-of-Life-\(EoL\)-Announcements). 

Always apply patch releases to stay secure and stable.

## Release Support & End-of-Life (EoL)

Every Major and Minor release of Expertflow CX is supported for a defined period. This policy ensures customers receive critical updates, patches, and necessary support for a predictable duration.

  * Each GA release is supported for a defined period.

  * After EoL, no further updates or patches are provided.




### End-of-Life (EoL) Policy

The EoL policy governs the lifecycle of a release version:

  * **Support Period:** Both Major and Minor releases are supported for a defined period, typically ranging from one to three years.

  * **End-of-Support (EoS) / End-of-Life (EoL):** Once the support period expires, the specific release version series is considered **End-of-Life (EoL)**.

  * **Post-EoL Status:** After a release reaches EoL, no further updates, security patches, or technical support are provided for that version.

  * **Maintenance Releases:** Expertflow continues to produce maintenance (patch) releases for all General Availability (GA) versions until their defined EoL date is reached.




plan and execute upgrades to a newer, supported release before their current version reaches its EoL date to ensure business continuity, security, and access to support services. See <https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/edit-v2/2525588#End-of-Life-(EoL)-Announcements>

## Pre-releases

A pre-release is an early versions for testing new features for field trials – not for production. A pre-release is named under [Semantic versioning - spec item# 9](https://semver.org/#spec-item-9). 

Do not deploy pre-releases in production. Always review release notes for known limitations.

For instance, for a planned production release CX1.0, a pre-release version is named as: 

**CX1.0** -rc.1| A pre-release 1 for the planned production release CX 1.0  
---|---  
**CX1.0** -rc.2| A pre-release 2 for the planned production release CX 1.0 
