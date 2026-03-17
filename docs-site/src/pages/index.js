import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

const sections = [
  {
    icon: '🚀',
    title: 'Getting Started',
    description: 'Platform overview, persona entry points, and the "Before You Begin" reference material.',
    link: '/docs/Phase4/Getting_Started',
  },
  {
    icon: '👤',
    title: 'Role-Based Guides',
    description: 'Deep-dive guides for each persona — Agents, Supervisors, Admins, Developers, and more.',
    link: '/docs/Phase4/Role_Based_Guides',
  },
  {
    icon: '📋',
    title: 'Functional Areas',
    description: 'Feature documentation by product area: Voice, Digital Channels, Quality Management, Reporting, and Security.',
    link: '/docs/Phase4/Functional_Areas',
  },
];

const roles = [
  { role: 'Agent handling customer interactions', link: '/docs/Phase4/Getting_Started/Agent-Quick-Start-Guide', label: 'Agent Quick-Start Guide' },
  { role: 'Supervisor managing a team', link: '/docs/Phase4/Getting_Started/Monitoring-Your-Team-in-Real-Time', label: 'Monitoring Your Team in Real-Time' },
  { role: 'Solution Admin configuring the platform', link: '/docs/Phase4/Getting_Started/Unified-Admin-Guide', label: 'Unified Admin Guide' },
  { role: 'Quality Manager running QA workflows', link: '/docs/Phase4/Getting_Started/Managing-the-Quality-Assurance-Workflow', label: 'Managing the QA Workflow' },
  { role: 'Human Evaluator scoring interactions', link: '/docs/Phase4/Getting_Started/Evaluator-Guide', label: 'User Guide for Evaluator' },
  { role: 'Decision Maker / CTO evaluating the platform', link: '/docs/Phase4/Getting_Started/Security-and-Compliance-Whitepaper', label: 'Security & Compliance Whitepaper' },
  { role: 'Frontend Developer building custom UIs', link: '/docs/Phase4/Role_Based_Guides/Frontend_Developer', label: 'Frontend Developer Guide' },
  { role: 'Conversation Designer building flows', link: '/docs/Phase4/Getting_Started/Conversation-Studio-Configuration-Guide', label: 'Conversation Studio Overview' },
  { role: 'Integration Specialist connecting systems', link: '/docs/Phase4/Getting_Started/Cisco-Contact-Center-Integration-Reference', label: 'Cisco UCCE/X Integration Reference' },
  { role: 'AI / NLU Specialist tuning AI models', link: '/docs/Phase4/Getting_Started/Configuring-AI-Powered-Quality-Audits', label: 'Configuring AI-Powered Quality Audits' },
  { role: 'Partner deploying the platform', link: '/docs/Phase4/Getting_Started/Deploying-the-RKE2-Control-Plane', label: 'Deploying the RKE2 Control Plane' },
  { role: 'Reseller onboarding tenants', link: '/docs/Phase4/Getting_Started/Onboarding-a-New-Tenant', label: 'Onboarding a New Tenant' },
];

function SectionCard({icon, title, description, link}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="card margin--sm" style={{height: '100%', display: 'flex', flexDirection: 'column'}}>
        <div className="card__header">
          <Heading as="h3">{icon} {title}</Heading>
        </div>
        <div className="card__body" style={{flex: 1}}>
          <p>{description}</p>
        </div>
        <div className="card__footer">
          <Link className="button button--primary button--block" to={link}>
            Browse {title} →
          </Link>
        </div>
      </div>
    </div>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout title={siteConfig.title} description={siteConfig.tagline}>
      <header className={clsx('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <Heading as="h1" className="hero__title">{siteConfig.title}</Heading>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link className="button button--secondary button--lg" to="/docs/Phase4/Getting_Started/Expertflow-CX-Platform-Overview">
              Platform Overview →
            </Link>
            <Link className="button button--outline button--secondary button--lg margin-left--md" to="/docs/Phase4">
              Browse All Docs →
            </Link>
          </div>
        </div>
      </header>

      <main>
        <section className="padding-vert--xl">
          <div className="container">
            <Heading as="h2" className="text--center margin-bottom--lg">Browse Documentation</Heading>
            <div className="row">
              {sections.map((props, idx) => (
                <SectionCard key={idx} {...props} />
              ))}
            </div>
          </div>
        </section>

        <section className="padding-vert--xl" style={{background: 'var(--ifm-color-emphasis-100)'}}>
          <div className="container">
            <Heading as="h2" className="text--center margin-bottom--lg">Start Here: Pick Your Role</Heading>
            <p className="text--center margin-bottom--lg">Find your role below to jump straight to the right guide.</p>
            <table style={{width: '100%'}}>
              <thead>
                <tr>
                  <th>I am a...</th>
                  <th>First stop</th>
                </tr>
              </thead>
              <tbody>
                {roles.map(({role, link, label}, idx) => (
                  <tr key={idx}>
                    <td>{role}</td>
                    <td><Link to={link}>{label}</Link></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        <section className="padding-vert--xl">
          <div className="container text--center">
            <Heading as="h2">New to ExpertFlow CX?</Heading>
            <p>Start with the Platform Overview for a conceptual introduction, then follow your role's path above.</p>
            <Link className="button button--primary button--lg" to="/docs/Phase4/Getting_Started/Expertflow-CX-Platform-Overview">
              Read the Platform Overview →
            </Link>
          </div>
        </section>
      </main>
    </Layout>
  );
}
