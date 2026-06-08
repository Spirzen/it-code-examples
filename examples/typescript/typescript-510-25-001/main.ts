type User = { id: string; name: string };
type Page<T> = { items: T[]; hasMore: boolean };

async function* fetchAllUsers(baseUrl: string): AsyncGenerator<User> {
  let page = 1;
  let hasMore = true;
  while (hasMore) {
    const res = await fetch(`${baseUrl}?page=${page}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const body = (await res.json()) as Page<User>;
    for (const user of body.items) {
      yield user;
    }
    hasMore = body.hasMore;
    page += 1;
  }
}

async function consume(): Promise<void> {
  for await (const user of fetchAllUsers("/api/users")) {
    console.log(user.name);
  }
}
