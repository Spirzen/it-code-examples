import { ThemeSwitch } from './components/ThemeSwitch';

export default function App() {
  return (
    <div className="app">
      <header>
        <ThemeSwitch />
      </header>
      <main>
        <h1>Контент страницы</h1>
        <p>Фон и текст меняются через класс <code>theme-dark</code> на <code>&lt;html&gt;</code>.</p>
      </main>
    </div>
  );
}
