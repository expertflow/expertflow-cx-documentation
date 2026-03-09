# CX Knowledgebase : Auto-Sync MRD State

#### **Overview**

Normally, when an agent wants to set their MRD state to **Ready** (to start receiving requests), they need to do it manually for each MRD one by one. Additionally, setting the **Parent State** to Ready does **not** affect the state of any MRD — it only updates the parent state.

With the **Auto-Sync MRD** feature, this behavior is improved. Now, whenever an agent sets their **Parent State** to **Ready** , all MRDs that are configured to be auto-synced will also be automatically set to the **Ready** state.

**Limitation**

While creating a new MRD, the **"Autosync state with the parent state"** toggle **must be enabled** ; otherwise, a new MRD will **not be created**. Once the MRD is created, the Autosync option can be **disabled** if needed.

If auto synced is enabled for **CX-Voice** MRD for **non voice** users or free switch connection fails , CX-Voice MRD **cannot** be changed to **Not ready** manually.

#### **MRD Auto-Sync Configuration**

The auto-sync behavior for each MRD can be enabled or disabled via the **Unified Admin** portal. Only those MRDs that are explicitly configured for auto-sync will be updated to **Ready** when the agent sets their parent state to **Ready**.

![image-20250415-095749.png](attachments/1025802251/1026064426.png?width=1322)

#### **Reverse Sync Behavior**

Additionally, if the **last MRD** of an agent is manually set to **Not Ready** , the **Parent State** of the agent will also be automatically updated to **Not Ready**.

#### **Feature Flag**

This functionality is controlled by a feature flag at the backend. If the feature flag is disabled, the auto-sync behavior will be turned off.

To disable this feature, set the following environment variable in the **Routing Engine** deployment:
[code] 
    IS_MRD_AUTO_SYNC_ENABLED=false 
[/code]

This variable should be under the `extraEnvVars` section of the Routing Engine's Kubernetes deployment configuration.
