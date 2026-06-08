import { useState } from 'react';

export default function App() {
  const [on, setOn] = useState(false);

  return (
    <div className="app">
      <p>Статус: {on ? 'включено' : 'выключено'}</p>
      <button type="button" onClick={() => setOn((v) => !v)}>
        {on ? 'Выключить' : 'Включить'}
      </button>
    </div>
  );
}
