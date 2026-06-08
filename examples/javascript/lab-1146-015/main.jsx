import { useState } from 'react';

function validate(email, password) {
  const errors = {};
  if (!email.includes('@')) errors.email = 'Нужен символ @';
  if (password.length < 6) errors.password = 'Минимум 6 символов';
  return errors;
}

export default function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({});
  const [ok, setOk] = useState('');

  function onSubmit(e) {
    e.preventDefault();
    const next = validate(email, password);
    setErrors(next);
    setOk('');
    if (Object.keys(next).length === 0) {
      setOk(`Вход выполнен для ${email}`);
    }
  }

  return (
    <div className="app">
      <h1>Вход</h1>
      <form onSubmit={onSubmit} noValidate>
        <label>
          Email
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          {errors.email && <span className="error">{errors.email}</span>}
        </label>
        <label>
          Пароль
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          {errors.password && <span className="error">{errors.password}</span>}
        </label>
        <button type="submit">Войти</button>
      </form>
      {ok && <p className="success">{ok}</p>}
    </div>
  );
}
