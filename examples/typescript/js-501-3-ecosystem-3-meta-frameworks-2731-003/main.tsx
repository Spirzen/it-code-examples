'use client';

import { useState } from 'react';

export default function CounterPage() {
  const [count, setCount] = useState(0);
  return (
    <section>
      <h1 className="text-xl font-semibold">Счётчик: {count}</h1>
      <button
        type="button"
        className="mt-2 rounded bg-black px-4 py-2 text-white"
        onClick={() => setCount((c) => c + 1)}
      >
        +1
      </button>
    </section>
  );
}
