type User = { id: string; name: string };

type FetchCallbacks = {
  onStart?: () => void;
  onSuccess: (user: User) => void;
  onError: (error: unknown) => void;
};

async function fetchUser(id: string, callbacks: FetchCallbacks): Promise<void> {
  callbacks.onStart?.();
  try {
    const res = await fetch(`/api/users/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const user = (await res.json()) as User;
    callbacks.onSuccess(user);
  } catch (error: unknown) {
    callbacks.onError(error);
  }
}
