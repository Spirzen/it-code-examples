import { useState } from 'react';
import { Button } from './components/Button';

export default function App() {
  const [busy, setBusy] = useState(false);

  function simulateSave() {
    setBusy(true);
    setTimeout(() => setBusy(false), 1200);
  }

  return (
    <div className="app">
      <h1>Кнопки</h1>
      <div className="button-row">
        <Button variant="primary">Сохранить</Button>
        <Button variant="outline">Отмена</Button>
        <Button variant="danger">Удалить</Button>
        <Button variant="primary" loading={busy} onClick={simulateSave}>
          Отправить
        </Button>
      </div>
    </div>
  );
}
