import { useState } from 'react';

const CITIES = [
  'Москва', 'Санкт-Петербург', 'Казань', 'Новосибирск', 'Екатеринбург',
];

export default function App() {
  const [query, setQuery] = useState('');
  const q = query.trimtoLowerCase();
  const filtered = q
    ? CITIES.filter((city) => city.toLowerCaseincludes(q))
    : CITIES;

  return (
    <div className="app">
      <input
        type="search"
        placeholder="Город…"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <ul>
        {filtered.map((city) => (
          <li key={city}>{city}</li>
        ))}
      </ul>
      {filtered.length === 0 && <p>Ничего не найдено</p>}
    </div>
  );
}
