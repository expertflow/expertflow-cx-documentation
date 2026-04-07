// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'ExpertFlow CX Documentation',
  tagline: 'Official documentation for the ExpertFlow CX Platform',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://expertflow.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/expertflow-cx-documentation/',

  // GitHub pages deployment config.
  organizationName: 'expertflow',
  projectName: 'expertflow-cx-documentation',
  trailingSlash: false,

  onBrokenLinks: 'throw',



  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  plugins: [
    function symlinksPlugin() {
      return {
        name: 'symlinks-webpack-plugin',
        configureWebpack() {
          return { resolve: { symlinks: false } };
        },
      };
    },
  ],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/expertflow/expertflow-cx-documentation/tree/main/DocWithGeminiCLI/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: '',
        logo: {
          alt: 'ExpertFlow Logo',
          src: 'img/ef-logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Docs',
          },
          {
            href: 'https://github.com/expertflow/expertflow-cx-documentation',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Get Started',
            items: [
              { label: 'For Agents', to: '/docs/cx/Getting_Started/For_Agents' },
              { label: 'For Administrators', to: '/docs/cx/Getting_Started/For_Administrators' },
              { label: 'For Partners', to: '/docs/cx/Getting_Started/For_Partners' },
            ],
          },
          {
            title: 'Explore',
            items: [
              { label: 'Platform Overview', to: '/docs/cx/Platform_Overview' },
              { label: 'Capabilities', to: '/docs/cx/Capabilities' },
              { label: 'How-to Guides', to: '/docs/cx/How-to_Guides' },
              { label: 'Reference', to: '/docs/cx/Reference' },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/expertflow/expertflow-cx-documentation',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} ExpertFlow. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
