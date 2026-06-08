import { useEffect, useState } from 'react';

const STORAGE_KEY = 'app-theme-dark';

export function ThemeSwitch() {
  const [dark, setDark] = useState(() => localStorage.getItem(STORAGE_KEY) === '1');

  useEffect(() => {
    document.documentElement.classList.toggle('theme-dark', dark);
    localStorage.setItem(STORAGE_KEY, dark ? '1' : '0');
  }, [dark]);

  return (
    <label className="switch switch--theme">
      <input
        type="checkbox"
        className="switch__input"
        role="switch"
        checked={dark}
        onChange={(e) => setDark(e.target.checked)}
        aria-labelledby="theme-switch-label"
      />
      <span className="switch-track" aria-hidden="true" />
      <span id="theme-switch-label" className="switch__label">
        {dark ? 'Тёмная тема' : 'Светлая тема'}
      </span>
    </label>
  );
}
