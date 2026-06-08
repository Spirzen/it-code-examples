const config = {
  title: 'Заголовок Сайта',
  tagline: 'Подзаголовок Описания',
  url: 'https://example.com',
  baseUrl: '/',
  favicon: 'img/favicon.ico',
  organizationName: 'Organization Name',
  projectName: 'Project Name',
  
  // Интеграции
  i18n: {
    defaultLocale: 'ru',
    locales: ['ru', 'en'],
  },
  
  // Плагин для поиска
  plugins: [
    require.resolve('docusaurus-plugin-content-docs'),
  ],
};

module.exports = config;
