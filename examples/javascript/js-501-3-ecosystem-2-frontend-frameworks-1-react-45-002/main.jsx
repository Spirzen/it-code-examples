
import { useState } from 'react';

function LoadingButton({ onClick, children }) {
  const [isLoading, setIsLoading] = useState(false);

  async function handleClick() {
    if (isLoading) return;
    setIsLoading(true);
    try {
      await onClick();
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <button type="button" onClick={handleClick} disabled={isLoading}>
      {isLoading ? '...' : children}
    </button>
  );
}

function CreateTodoButton() {
  return (
    <LoadingButton
      onClick={async () => {
        await createTodoAPI('new todo text');
      }}
    >
      Create Todo
    </LoadingButton>
  );
}
