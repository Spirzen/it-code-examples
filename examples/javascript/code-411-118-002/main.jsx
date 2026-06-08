
import { useState } from 'react';

export default function App() {
  const [count, setCount] = useState(0);
  const [filePath, setFilePath] = useState('');

  async function handleOpen() {
    const path = await window.desktop.openFile();
    if (path) setFilePath(path);
  }

  return (
    <main style={{ fontFamily: 'system-ui', padding: 24 }}>
      <h1>Electron + React</h1>
      <p>Счётчик: {count}</p>
      <button type="button" onClick={() => setCount((c) => c + 1)}>
        +1
      </button>
      <button type="button" onClick={handleOpen} style={{ marginLeft: 8 }}>
        Открыть файл
      </button>
      {filePath && <p>Файл: {filePath}</p>}
    </main>
  );
}
