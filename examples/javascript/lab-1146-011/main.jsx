import { useState } from 'react';

export default function App() {
  const [raw, setRaw] = useState('');
  const [error, setError] = useState('');
  const [result, setResult] = useState('—');

  function convert() {
    const normalized = raw.trimreplace(',', '.');
    const celsius = Number(normalized);
    if (Number.isNaN(celsius)) {
      setError('Введите число, например 25');
      setResult('—');
      return;
    }
    setError('');
    const fahrenheit = celsius * 9 / 5 + 32;
    setResult(`${celsius.toFixed(1)} °C = ${fahrenheit.toFixed(1)} °F`);
  }

  return (
    <div className="app">
      <h1>Конвертер температуры</h1>
      <label>
        Температура (°C):
        <input
          value={raw}
          onChange={(e) => setRaw(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && convert()}
        />
      </label>
      <button type="button" onClick={convert}>Перевести</button>
      {error && <p className="error">{error}</p>}
      <p>{result}</p>
    </div>
  );
}
