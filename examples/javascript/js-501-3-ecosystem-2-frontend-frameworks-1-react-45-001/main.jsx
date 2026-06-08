
import { useState } from 'react';

async function createTodoAPI(text) {
  const res = await fetch('http://127.0.0.1:3000/notes', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text }),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

function CreateTodoButton() {
  const [isLoading, setIsLoading] = useState(false);

  async function handleClick() {
    if (isLoading) return;
    setIsLoading(true);
    try {
      await createTodoAPI('new todo text');
    } catch (err) {
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <button type="button" onClick={handleClick} disabled={isLoading}>
      {isLoading ? '...' : 'Create Todo'}
    </button>
  );
}
