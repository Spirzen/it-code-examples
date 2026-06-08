const themes = require('docusaurus-theme-classic');

module.exports = {
  themeConfig: {
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    prism: {
      theme: require('prism-react-renderer/themes/vsLight'),
      darkTheme: require('prism-react-renderer/themes/dracula'),
    },
    algolia: {
      appId: 'APPLICATION_ID',
      apiKey: 'API_KEY',
      indexName: 'INDEX_NAME',
    },
  },
};
