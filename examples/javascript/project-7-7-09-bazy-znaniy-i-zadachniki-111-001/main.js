module.exports = {
  // ...
  navbar: {
    title: 'Техническая Документация',
    logo: {
      alt: 'Логотип Проекта',
      src: '/img/logo.svg',
    },
    items: [
      {
        type: 'docSidebar',
        sidebarId: 'tutorialSidebar',
        position: 'left',
        label: 'Руководство',
      },
      {
        type: 'doc',
        docId: 'intro',
        position: 'left',
        label: 'Введение',
      },
      {
        href: 'https://github.com/user/repo',
        label: 'GitHub',
        position: 'right',
      },
    ],
  },
};
