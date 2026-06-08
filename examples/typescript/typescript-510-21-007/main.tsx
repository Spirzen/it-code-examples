function SearchBox({ onSearch }: { onSearch: (q: string) => void }) {
  const [q, setQ] = React.useState("");

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setQ(e.target.value);
  };

  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    onSearch(q.trim());
  };

  return (
    <form onSubmit={onSubmit}>
      <input value={q} onChange={onChange} aria-label="Поиск" />
      <button type="submit">Найти</button>
    </form>
  );
}
