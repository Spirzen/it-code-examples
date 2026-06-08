import { useEffect, useState } from 'react';

export default function App() {
  const [status, setStatus] = useState('loading'); // loading | ok | error
  const [data, setData] = useState([]);

  useEffect(() => {
    const timer = setTimeout(() => {
      if (Math.random() > 0.2) {
        setData(['Альфа', 'Бета', 'Гамма']);
        setStatus('ok');
      } else {
        setStatus('error');
      }
    }, 800);
    return () => clearTimeout(timer);
  }, []);

  if (status === 'loading') return <p>Загрузка…</p>;
  if (status === 'error') return <p className="error">Не удалось загрузить данные</p>;
  if (!data.length) return <p>Список пуст</p>;

  return (
    <ul>
      {data.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </ul>
  );
}
