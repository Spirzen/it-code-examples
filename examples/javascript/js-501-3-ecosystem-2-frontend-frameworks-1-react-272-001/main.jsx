
import { useState } from 'react';
import './App.css';

export default function App() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  return (
    <div className="app">
      <h1>Моя первая программа на React</h1>

      <section className="greeting">
        <input
          type="text"
          placeholder="Введите имя"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        {name && <h2>Привет, {name}!</h2>}
      </section>

      <section className="counter">
        <h2>Счётчик: {count}</h2>
        <div className="buttons">
          <button type="button" onClick={() => setCount(count - 1)}>−</button>
          <button type="button" onClick={() => setCount(0)}>Сброс</button>
          <button type="button" onClick={() => setCount(count + 1)}>+</button>
        </div>
      </section>
    </div>
  );
}
