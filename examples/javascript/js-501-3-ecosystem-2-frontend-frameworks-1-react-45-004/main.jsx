
import { useState } from 'react';

function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function LoadingButton({ onClick, children, className }) {
  const [label, setLabel] = useState(children);
  const [isLoading, setIsLoading] = useState(false);

  async function handleClick() {
    if (isLoading) return;
    setIsLoading(true);
    setLabel(children);

    try {
      const result = onClick();

      if (result && typeof result[Symbol.asyncIterator] === 'function') {
        for await (const step of result) {
          setLabel(step);
        }
      } else {
        await result;
      }
    } finally {
      setIsLoading(false);
      setLabel(children);
    }
  }

  return (
    <button
      type="button"
      className={className}
      onClick={handleClick}
      disabled={isLoading}
    >
      {isLoading ? label : children}
    </button>
  );
}

function Demo() {
  return (
    <LoadingButton
      className="counter"
      onClick={async function* () {
        yield 'Starting some process';
        await wait(1000);
        yield 'Oops, taking longer than usual';
        await wait(2000);
        yield (
          <span>
            Maybe there is a <code>Retry-after</code>?
          </span>
        );
        await wait(3000);
        yield 'Nevermind, I got it';
      }}
    >
      Click me
    </LoadingButton>
  );
}
