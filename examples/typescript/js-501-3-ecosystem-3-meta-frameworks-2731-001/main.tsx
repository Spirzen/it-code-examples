
import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'Моё Next-приложение',
  description: 'Первая программа на Next.js',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ru">
      <body className="p-8 font-sans">
        <nav className="mb-6 flex gap-4">
          <Link href="/">Главная</Link>
          <Link href="/about">О проекте</Link>
          <Link href="/counter">Счётчик</Link>
          <Link href="/notes">Заметки</Link>
        </nav>
        <main>{children}</main>
      </body>
    </html>
  );
}
