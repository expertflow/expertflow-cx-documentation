// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    // ── 1. Getting Started ────────────────────────────────────────────────
    {
      type: 'category',
      label: 'Getting Started',
      collapsed: false,
      link: { type: 'doc', id: 'cx/Getting_Started/index' },
      items: [
        { type: 'doc', id: 'cx/Getting_Started/For_Agents/Agent-Quick-Start-Guide', label: 'For Agents' },
        { type: 'doc', id: 'cx/Getting_Started/For_Administrators/Unified-Admin-Guide', label: 'For Administrators' },
        { type: 'doc', id: 'cx/Getting_Started/For_Supervisors_and_QA_Leads/Supervisor-and-QA-Lead-Quick-Start', label: 'For Supervisors & QA Leads' },
        { type: 'doc', id: 'cx/Getting_Started/For_Hosting_Partners/Platform-Operator-Quick-Start', label: 'For Platform Operators' },
        { type: 'doc', id: 'cx/Getting_Started/For_Hosting_Partners/Reseller-Partner-Quick-Start', label: 'For Reseller Partners' },
        { type: 'doc', id: 'cx/Getting_Started/For_Conversation_Designers/Conversation-Designer-Quick-Start', label: 'For Conversation Designers' },
        { type: 'doc', id: 'cx/Getting_Started/For_Developers_and_Integrators/Developer-and-Integrator-Quick-Start', label: 'For Developers & Integrators' },
      ],
    },

    // ── 2. Platform Overview ──────────────────────────────────────────────
    {
      type: 'category',
      label: 'Platform Overview',
      link: { type: 'doc', id: 'cx/Platform_Overview/Expertflow-CX-Platform-Overview' },
      items: [
        'cx/Platform_Overview/Platform-Architecture',
        'cx/Platform_Overview/AI-Self-Service-Capabilities',
        'cx/Platform_Overview/Customer-Journey-Orchestration',
        'cx/Platform_Overview/Security-and-Compliance-Whitepaper',
        'cx/Platform_Overview/Conversation-Studio',
      ],
    },

    // ── 3. Capabilities ───────────────────────────────────────────────────
    {
      type: 'category',
      label: 'Capabilities',
      items: [
        {
          type: 'category',
          label: 'Digital Channels',
          link: { type: 'doc', id: 'cx/Capabilities/Digital_Channels/index' },
          items: [
            // ── Chat & Messaging ─────────────────────────────────────────────
            {
              type: 'category',
              label: 'Chat & Messaging',
              items: [
                'cx/Capabilities/Digital_Channels/Customer-Widget-Features-Capabilities',
                'cx/Capabilities/Digital_Channels/Customer-Widget-Embedding-Guide',
                {
                  type: 'category',
                  label: 'WhatsApp',
                  link: { type: 'doc', id: 'cx/Capabilities/Digital_Channels/WhatsApp/index' },
                  items: [
                    'cx/Capabilities/Digital_Channels/WhatsApp/WhatsApp-Cloud-API',
                    'cx/Capabilities/Digital_Channels/WhatsApp/360dialog-WhatsApp-Overview',
                  ],
                },
                'cx/Capabilities/Digital_Channels/Telegram-Channel-Overview',
                'cx/Capabilities/Digital_Channels/Telegram-Bot-Creation-Guide',
                'cx/Capabilities/Digital_Channels/Telegram-Configuration-Guide',
                'cx/Capabilities/Digital_Channels/Telegram-Media-Types',
                'cx/Capabilities/Digital_Channels/Telegram-Connector-Limitations',
                'cx/Capabilities/Digital_Channels/SMPP-Channel-Overview',
                'cx/Capabilities/Digital_Channels/SMPP-Configuration-Guide',
              ],
            },
            // ── Social Media ─────────────────────────────────────────────────
            {
              type: 'category',
              label: 'Social Media',
              items: [
                'cx/Capabilities/Digital_Channels/Facebook-Channel-Overview',
                'cx/Capabilities/Digital_Channels/Facebook-Configuration-Guide',
                'cx/Capabilities/Digital_Channels/Facebook-Connector-Limitations',
                'cx/Capabilities/Digital_Channels/Twitter-Channel-Overview',
                'cx/Capabilities/Digital_Channels/Twitter-Configuration-Guide',
                'cx/Capabilities/Digital_Channels/LinkedIn-Channel-Overview',
                'cx/Capabilities/Digital_Channels/LinkedIn-Account-Onboarding',
                'cx/Capabilities/Digital_Channels/LinkedIn-Configuration-Guide',
                'cx/Capabilities/Digital_Channels/LinkedIn-Dev-Connector-Deployment',
                'cx/Capabilities/Digital_Channels/YouTube-Channel-Overview',
                'cx/Capabilities/Digital_Channels/Google-Play-Store-Channel-Overview',
                'cx/Capabilities/Digital_Channels/Google-Play-Store-Account-Onboarding',
                'cx/Capabilities/Digital_Channels/Google-Play-Store-Configuration-Guide',
                'cx/Capabilities/Digital_Channels/Google-Play-Store-FAQs-and-Troubleshooting',
              ],
            },
            // ── Email ─────────────────────────────────────────────────────────
            {
              type: 'category',
              label: 'Email',
              items: [
                'cx/Capabilities/Digital_Channels/Email-Channel-Overview',
                'cx/Capabilities/Digital_Channels/Email-Configuration-IMAP-SMTP',
                'cx/Capabilities/Digital_Channels/Email-Configuration-MS-Exchange',
                'cx/Capabilities/Digital_Channels/Email-Limitations',
              ],
            },
          ],
        },
        {
          type: 'category',
          label: 'Voice & Video',
          link: { type: 'doc', id: 'cx/Capabilities/Voice_and_Video/Voice-and-Video-Overview' },
          items: [{ type: 'autogenerated', dirName: 'cx/Capabilities/Voice_and_Video' }],
        },
        {
          type: 'category',
          label: 'Reporting & Analytics',
          link: { type: 'doc', id: 'cx/Capabilities/Reporting_and_Analytics/Reports-and-Analytics' },
          items: [{ type: 'autogenerated', dirName: 'cx/Capabilities/Reporting_and_Analytics' }],
        },
        {
          type: 'category',
          label: 'Security & Compliance',
          link: { type: 'doc', id: 'cx/Capabilities/Security_and_Compliance/index' },
          items: [{ type: 'autogenerated', dirName: 'cx/Capabilities/Security_and_Compliance' }],
        },
        // ── Customer Management ────────────────────────────────────────────
        {
          type: 'category',
          label: 'Customer Management',
          link: { type: 'doc', id: 'cx/Capabilities/Customer_Management/index' },
          items: [
            'cx/Capabilities/Customer_Management/Customer-Labels',
            'cx/Capabilities/Customer_Management/Customer-Advanced-Filters',
          ],
        },
        'cx/Capabilities/Digital_Channels/Conversation-View',
        {
          type: 'category',
          label: 'Business Calendars',
          link: { type: 'doc', id: 'cx/Capabilities/Digital_Channels/Business-Calendars' },
          items: [
            'cx/Capabilities/Digital_Channels/Business-Calendars-Limitations',
          ],
        },
        {
          type: 'category',
          label: 'Workforce Management',
          link: { type: 'doc', id: 'cx/Capabilities/Workforce_Management/Workforce-Management-Overview' },
          items: [{ type: 'autogenerated', dirName: 'cx/Capabilities/Workforce_Management' }],
        },
      ],
    },

    // ── 4. How-to Guides ──────────────────────────────────────────────────
    {
      type: 'category',
      label: 'How-to Guides',
      items: [
        {
          type: 'category',
          label: 'Agent',
          link: { type: 'doc', id: 'cx/How-to_Guides/Agent/index' },
          items: [
            { type: 'autogenerated', dirName: 'cx/How-to_Guides/Agent' },
            'cx/Capabilities/Digital_Channels/Browser-and-Sound-Notifications',
          ],
        },
        {
          type: 'category',
          label: 'Administrator',
          link: { type: 'doc', id: 'cx/How-to_Guides/Administrator/index' },
          items: [{ type: 'autogenerated', dirName: 'cx/How-to_Guides/Administrator' }],
        },
        {
          type: 'category',
          label: 'Supervisor & QA Lead',
          link: { type: 'doc', id: 'cx/How-to_Guides/Supervisor_and_QA_Lead/index' },
          items: [{ type: 'autogenerated', dirName: 'cx/How-to_Guides/Supervisor_and_QA_Lead' }],
        },
        {
          type: 'category',
          label: 'Conversation Designer / AI Specialist',
          link: { type: 'doc', id: 'cx/How-to_Guides/Conversation_Designer/index' },
          items: [{ type: 'autogenerated', dirName: 'cx/How-to_Guides/Conversation_Designer' }],
        },
        {
          type: 'category',
          label: 'Developer / Integrator',
          link: { type: 'doc', id: 'cx/How-to_Guides/Developer_Integrator/index' },
          items: [{ type: 'autogenerated', dirName: 'cx/How-to_Guides/Developer_Integrator' }],
        },
        {
          type: 'category',
          label: 'Platform Operator',
          link: { type: 'doc', id: 'cx/How-to_Guides/Hosting_Partner/index' },
          items: [{ type: 'autogenerated', dirName: 'cx/How-to_Guides/Hosting_Partner' }],
        },
        {
          type: 'category',
          label: 'Reseller Partner',
          link: { type: 'doc', id: 'cx/How-to_Guides/Reseller_Partner/index' },
          items: [{ type: 'autogenerated', dirName: 'cx/How-to_Guides/Reseller_Partner' }],
        },
      ],
    },

    // ── 5. Reference ──────────────────────────────────────────────────────
    {
      type: 'category',
      label: 'Reference',
      items: [
        { type: 'doc', id: 'cx/Reference/Agent-Desk-Developer-Guide', label: 'AgentManager SDK Reference' },
        { type: 'doc', id: 'cx/Reference/Release-Lifecycle-and-Versioning', label: 'Release Lifecycle & Versioning' },
        { type: 'doc', id: 'cx/Reference/WFM-Compatibility-Guide', label: 'WFM Compatibility Guide' },
        { type: 'doc', id: 'cx/Reference/Hybrid-Chat-to-CX-Migration-Comparison', label: 'Hybrid Chat to CX Migration Comparison' },
        { type: 'doc', id: 'cx/Reference/Dialer-Performance-Benchmarks', label: 'Dialer Performance Benchmarks' },
        {
          type: 'category',
          label: 'Schemas & Data Model',
          items: [
            {
              type: 'category',
              label: 'CIM Message Schema',
              link: { type: 'doc', id: 'cx/Reference/Schemas_and_Data_Model/CIM_Message_Schema/CIM-Messages' },
              items: [{ type: 'autogenerated', dirName: 'cx/Reference/Schemas_and_Data_Model/CIM_Message_Schema' }],
            },
            {
              type: 'category',
              label: 'Socket Events',
              link: { type: 'doc', id: 'cx/Reference/Schemas_and_Data_Model/Socket_Events/index' },
              items: [{ type: 'autogenerated', dirName: 'cx/Reference/Schemas_and_Data_Model/Socket_Events' }],
            },
          ],
        },
        {
          type: 'category',
          label: 'Glossary',
          items: [{ type: 'autogenerated', dirName: 'cx/Reference/Glossary' }],
        },
      ],
    },
  ],
};

export default sidebars;
