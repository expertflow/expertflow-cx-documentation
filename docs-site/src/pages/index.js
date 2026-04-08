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
    link: '/docs/cx/Getting_Started',
  },
  {
    icon: '📖',
    title: 'How-to Guides',
    description: 'Step-by-step guides for each persona — Agents, Supervisors, Admins, Developers, and more.',
    link: '/docs/cx/How-to_Guides',
  },
  {
    icon: '📋',
    title: 'Capabilities',
    description: 'Feature documentation by product area: Voice, Digital Channels, Quality Management, Reporting, and Security.',
    link: '/docs/cx/Capabilities',
  },
];

const roles = [
  { role: 'Agent handling customer interactions', link: '/docs/cx/Getting_Started/For_Agents/', label: 'Agent Quick-Start Guide' },
  { role: 'Administrator configuring the platform', link: '/docs/cx/Getting_Started/For_Administrators/', label: 'Getting Started for Administrators' },
  { role: 'Supervisor or QA Lead managing a team', link: '/docs/cx/Getting_Started/For_Supervisors_and_QA_Leads/', label: 'For Supervisors & QA Leads' },
  { role: 'Platform Operator deploying infrastructure', link: '/docs/cx/Getting_Started/For_Platform_Operators/', label: 'Getting Started: Platform Operators' },
  { role: 'Partner or Reseller onboarding tenants', link: '/docs/cx/Getting_Started/For_Partners/', label: 'Quick Start for Reseller Partners' },
  { role: 'Conversation Designer or AI Specialist building flows', link: '/docs/cx/Getting_Started/For_Conversation_Designers/', label: 'Quick Start for Conversation Designers' },
  { role: 'Developer or Integration Specialist', link: '/docs/cx/Getting_Started/For_Developers_and_Integrators/', label: 'Developer & Integrator Quick Start' },
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
            <Link className="button button--secondary button--lg" to="/docs/cx/Platform_Overview/Expertflow-CX-Platform-Overview">
              Platform Overview →
            </Link>
            <Link className="button button--outline button--secondary button--lg margin-left--md" to="/docs/cx">
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
            <Link className="button button--primary button--lg" to="/docs/cx/Platform_Overview/Expertflow-CX-Platform-Overview">
              Read the Platform Overview →
            </Link>
          </div>
        </section>
      </main>
    </Layout>
  );
}
