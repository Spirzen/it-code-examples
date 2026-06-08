'use client';

import { useEffect, useState } from 'react';

type Note = { id: number; text: string };

export default function NotesPage() {
  const [notes, setNotes] = useState<Note[]>([]);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('http://127.0.0.1:3000/notes')
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then(setNotes)
      .catch((e) => setError(e.message));
  }, []);

  if (error) return <p>Ошибка: {error}</p>;

  return (
    <ul className="list-disc pl-6">
      {notes.map((n) => (
        <li key={n.id}>{n.text}</li>
      ))}
    </ul>
  );
}
