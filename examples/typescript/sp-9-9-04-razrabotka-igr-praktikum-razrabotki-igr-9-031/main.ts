import { VitePWA } from 'vite-plugin-pwa';

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      manifest: {
        name: 'Приключения Урала Батыра',
        short_name: 'Урал Батыр',
        theme_color: '#0a0806',
        background_color: '#0a0806',
        display: 'standalone',
        icons: [{ src: 'favicon.svg', sizes: 'any', type: 'image/svg+xml' }],
      },
      workbox: { globPatterns: ['**/*.{js,css,html,json,svg}'] },
    }),
  ],
  base: './',
});
