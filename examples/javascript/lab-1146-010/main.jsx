import { useState } from 'react';

const FILTERS = ['all', 'active', 'done'];

export default function App() {
  const [text, setText] = useState('');
  const [filter, setFilter] = useState('all');
  const [items, setItems] = useState([
    { id: 1, title: 'Изучить JSX', done: false },
    { id: 2, title: 'Собрать Todo', done: true },
  ]);

  function addItem(e) {
    e.preventDefault();
    const title = text.trim();
    if (!title) return;
    setItems((prev) => [
      ..prev,
      { id: Date.now title, done: false },
    ]);
    setText('');
  }

  function toggle(id) {
    setItems((prev) =>
      prev.map((item) =>
        item.id === id ? { ..item, done: !item.done } : item
      )
    );
  }

  const visible = items.filter((item) => {
    if (filter === 'active') return !item.done;
    if (filter === 'done') return item.done;
    return true;
  });

  return (
    <div className="app">
      <h1>Задачи</h1>
      <form onSubmit={addItem}>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Новая задача"
        />
        <button type="submit">Добавить</button>
      </form>

      <div className="filters">
        {FILTERS.map((f) => (
          <button
            key={f}
            type="button"
            className={filter === f ? 'active' : ''}
            onClick={() => setFilter(f)}
          >
            {f === 'all' ? 'Все' : f === 'active' ? 'Активные' : 'Готово'}
          </button>
        ))}
      </div>

      <ul>
        {visible.map((item) => (
          <li key={item.id}>
            <label>
              <input
                type="checkbox"
                checked={item.done}
                onChange={() => toggle(item.id)}
              />
              <span className={item.done ? 'done' : ''}>{item.title}</span>
            </label>
          </li>
        ))}
      </ul>
      {visible.length === 0 && <p>Список пуст для выбранного фильтра</p>}
    </div>
  );
}
