import { useState } from 'react';

export default function App() {
  const [notify, setNotify] = useState(true);
  const [sound, setSound] = useState(false);
  const [role, setRole] = useState('user');

  const enabled = [
    notify && 'уведомления',
    sound && 'звук',
  ].filter(Boolean);

  return (
    <div className="app">
      <label>
        <input
          type="checkbox"
          checked={notify}
          onChange={(e) => setNotify(e.target.checked)}
        />
        Уведомления
      </label>
      <label>
        <input
          type="checkbox"
          checked={sound}
          onChange={(e) => setSound(e.target.checked)}
        />
        Звук
      </label>

      <p>Роль:</p>
      <label>
        <input
          type="radio"
          name="role"
          checked={role === 'user'}
          onChange={() => setRole('user')}
        />
        Пользователь
      </label>
      <label>
        <input
          type="radio"
          name="role"
          value="admin"
          checked={role === 'admin'}
          onChange={() => setRole('admin')}
        />
        Администратор
      </label>

      <p className="hint">
        Роль: {role}; включено: {enabled.length ? enabled.join(', ') : 'ничего'}
      </p>
    </div>
  );
}
