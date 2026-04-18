---
audience: [administrator]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Migrating Keycloak Groups to CX Teams

This guide details the procedure for exporting team and membership data from Keycloak and importing it into the Expertflow CX Team structure (MongoDB).

## Mandatory Rules
- **Single Team**: An agent can only belong to one team. Multiple memberships will be consolidated during import.
- **Role Requirement**: Team assignment is mandatory for **Agent** and **Supervisor** roles only.
- **Role Integrity**: A user should only have one primary CX role (e.g., an Admin should not also be an Agent).

## Migration Procedure

### 1. Export Teams from Keycloak
Run the `export_teams_from_keycloak.sh` script to extract group and user data from the Keycloak Postgres database into a `teams.json` file.

### 2. Format Team Data
Use the `formatting_teams.sh` script (utilizing `jq`) to transform the raw export into a structured format compatible with the CX import engine.

### 3. Import to MongoDB
Run the `import_teams_to_mongo.sh` script. This script handles:
- Creating team objects in the `adminPanel.teams` collection.
- Mapping members (agents and supervisors) in the `adminPanel.teammembers` collection.
- Handling secondary supervisors and Cisco Team ID mappings.

## Verification
- Changes are reflected after the user next logs into the system.
- Check the **Unified Admin > Team Management** section to verify the imported hierarchy.
