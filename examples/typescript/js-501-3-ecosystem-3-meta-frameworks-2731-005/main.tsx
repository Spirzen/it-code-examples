type Note = { id: number; text: string };

async function getNotes(): Promise<Note[]> {
  const res = await fetch('http://127.0.0.1:3000/notes', {
    cache: 'no-store',
  });
  if (!res.ok) throw new Error('Failed to fetch');
  return res.json();
}

export default async function NotesServerPage() {
  const notes = await getNotes();
  return (
    <ul>
      {notes.map((n) => (
        <li key={n.id}>{n.text}</li>
      ))}
    </ul>
  );
}
