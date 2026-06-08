import { useState } from 'react';

export default function App() {
  const [name, setName] = useState('');

  return (
    <div className="app">
      <label>
        Ваше имя:
        <input
          type="text"
          value={name}
          placeholder="Анна"
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      {name.trim() && <h2>Привет, {name.trim()}!</h2>}
    </div>
  );
}
