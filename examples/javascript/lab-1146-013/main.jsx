import { useState } from 'react';

const TABS = [
  { id: 'home', label: 'Главная', body: 'Добро пожаловать на сайт.' },
  { id: 'about', label: 'О нас', body: 'Мы учим React на практике.' },
  { id: 'contact', label: 'Контакты', body: 'hello@example.com' },
];

export default function App() {
  const [active, setActive] = useState('home');
  const current = TABS.find((t) => t.id === active);

  return (
    <div className="app">
      <div className="tabs" role="tablist">
        {TABS.map((tab) => (
          <button
            key={tab.id}
            type="button"
            role="tab"
            aria-selected={active === tab.id}
            className={active === tab.id ? 'active' : ''}
            onClick={() => setActive(tab.id)}
          >
            {tab.label}
          </button>
        ))}
      </div>
      <div role="tabpanel">{current?.body}</div>
    </div>
  );
}
