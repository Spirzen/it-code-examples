import { useState } from 'react';

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="app">
      <h1>Счётчик: {count}</h1>
      <button type="button" onClick={() => setCount(count - 1)}>−</button>
      <button type="button" onClick={() => setCount(0)}>Сброс</button>
      <button type="button" onClick={() => setCount(count + 1)}>+</button>
    </div>
  );
}
