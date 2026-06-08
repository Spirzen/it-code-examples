
import { useState, useEffect } from 'react';

function NotesList() {
  const [notes, setNotes] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('http://127.0.0.1:3000/notes')
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then(setNotes)
      .catch((e) => setError(e.message));
  }, []);

  if (error) return <p>Ошибка: {error}</p>;
  if (!notes.length) return <p>Заметок пока нет</p>;

  return (
    <ul>
      {notes.map((n) => (
        <li key={n.id}>{n.text}</li>
      ))}
    </ul>
  );
}
