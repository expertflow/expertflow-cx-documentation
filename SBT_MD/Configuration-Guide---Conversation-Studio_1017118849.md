# CX Knowledgebase : Configuration Guide - Conversation Studio

This guide provides step-by-step instructions for deploying and configuring Conversation Studio access within your CX environment. It covers the deployment process through the CX Core Helm chart and IAM (Keycloak) configuration required for user access.

This guide needs to be followed to access Conversation Studio after the CX Deployment

The intended audience for this guide, including deployment, access, troubleshooting, and setup procedures for Conversation Studio, is Support/OPS teams and System Administrators responsible for deploying and accessing Conversation Studio on the target machine.

### Pre-requirements

  * CX Deployment [Helm-based Deployment for Expertflow CX](Helm-based-Deployment-for-Expertflow-CX_2528431.html)



#### **Step 1: Deploy the CX Core Helm Chart**

Conversation Studio will be deployed as part of the CX Core Helm chart installation. 

No separate deployment is required for Conversation Studio.

#### **Step 2: IAM (Keycloak Configuration) - Mandatory**

To access the Conversation Studio UI, make sure you perform the following steps in Keycloak:

  1. Create a new user.

  2. Assign the `conversation-studio-admin` role to that user.

  3. Log in to the UI using this user's credentials.




#### **Step 3: Accessing Conversation Studio**

Once the deployment completes successfully, Conversation Studio will be available at:
[code] 
    https://<FQDN>/conversation-studio 
[/code]

* * *

# **Setting Up Survey Messages**

In versions **prior to CX 5.0** , survey handling inside the _Participant Role Changed_ flow was done through a Function node named **Evaluation** as shown in**figure 1**.  
This node performed the following actions:

  * Retrieved all available survey forms

  * Selected a survey form to use

  * Generated the survey message

  * Sent the message to the Conversation Manager

  * Passed the original message forward to the next Node-RED node




![image-20251121-110607.png](attachments/1017118849/1473085471.png?width=700)

## **Changes in CX 5.0**

Starting from the **5.0 release** , the **Evaluation** Function node has been replaced with a dedicated node called **Survey Message** as shown in**figure 2**. This new node is included in the _Participant Role Changed_ flow **but is disabled by default** , because it requires a survey form to be selected.

![image-20251121-111523.png](attachments/1017118849/1474494467.png?width=826)

## **How to Enable Survey Message Sending**

Before enabling survey message sending, ensure that the required **survey form is already configured in Unified Admin**. Only the forms configured in Unified Admin will appear in the dropdown list of the **Survey Message** node.

### **For Deployments Using Default Training**

To activate the survey message functionality:

  1. Open the **Survey Message** node in the flow

  2. Select the survey form that you have configured in **Unified Admin** from the dropdown list as shown in **figure 3**.

  3. Deploy the flow




Once configured, this node will send the selected survey message through the Conversation Manager.

![image-20251121-111617.png](attachments/1017118849/1473118254.png?width=465)

### **For Deployments Using Custom Training**

If your deployment includes **custom training** , your flow might contain the legacy **Evaluation** Function node from earlier versions.

In such cases:

  1. **Remove the legacy Evaluation node** from the _Participant Role Changed_ flow

  2. **Add the new Survey Message node** in its place

  3. Configure the node by selecting the survey form from the dropdown (as described above)

  4. Deploy the updated flow




This ensures the environment uses the new, supported Survey Message mechanism introduced in CX 5.0.
