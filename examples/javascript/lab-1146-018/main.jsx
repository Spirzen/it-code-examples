import { useState } from 'react';
import { Counter } from './components/Counter';

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <Counter
      value={count}
      onIncrement={() => setCount((c) => c + 1)}
      onDecrement={() => setCount((c) => c - 1)}
      onReset={() => setCount(0)}
    />
  );
}
