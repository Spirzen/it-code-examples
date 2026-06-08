
import { useAsyncCallback } from 'react-async-hook';

function AppButton({ onClick, children }) {
  const asyncOnClick = useAsyncCallback(onClick);

  return (
    <button
      type="button"
      onClick={asyncOnClick.execute}
      disabled={asyncOnClick.loading}
    >
      {asyncOnClick.loading ? '...' : children}
    </button>
  );
}
