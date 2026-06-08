type User = { id: string; name: string };

type LoadState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; user: User }
  | { status: "error"; message: string };

function Profile() {
  const [state, setState] = React.useState<LoadState>({ status: "idle" });

  React.useEffect(() => {
    let cancelled = false;

    async function load() {
      setState({ status: "loading" });
      try {
        const res = await fetch("/api/me");
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const raw: unknown = await res.json();
        if (!isUser(raw)) throw new Error("Invalid payload");
        if (!cancelled) setState({ status: "success", user: raw });
      } catch (e: unknown) {
        if (!cancelled) {
          setState({
            status: "error",
            message: e instanceof Error ? e.message : "Unknown",
          });
        }
      }
    }

    load();
    return () => {
      cancelled = true;
    };
  }, []);

  switch (state.status) {
    case "idle":
      return <p>Нажмите для загрузки</p>;
    case "loading":
      return <p>Загрузка…</p>;
    case "error":
      return <p>Ошибка: {state.message}</p>;
    case "success":
      return <h2>{state.user.name}</h2>;
  }
}

function isUser(v: unknown): v is User {
  if (typeof v !== "object" || v === null) return false;
  const o = v as Record<string, unknown>;
  return typeof o.id === "string" && typeof o.name === "string";
}
