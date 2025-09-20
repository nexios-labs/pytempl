import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: 'PyTemplate Engine',
  description: 'A powerful template engine that transpiles component-based files into pure Python code.',
  base: "/pytempl/",
  markdown: {
    // Configure syntax highlighting
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    },
    lineNumbers: true
  },
  
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Getting Started', link: '/getting-started' },
    ],

    sidebar: [
      {
        text: 'Introduction',
        items: [
          { text: 'Getting Started', link: '/getting-started' },
        ]
      },
      {
        text: 'Core Concepts',
        items: [
          { text: 'Components', link: '/components' },
          { text: 'Interpolation', link: '/interpolation' },
          { text: 'Conditionals', link: '/conditionals' },
          { text: 'Loops', link: '/loops' },
          { text: 'Scripts', link: '/scripts' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/nexios-labs/pytempl' }
    ],

    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2025 PyTemplate Engine'
    }
  }
})
